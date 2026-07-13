"""
Orbital Datacenter Thermal Architecture — Launched-Mass Model
==============================================================

Question: for a 1 MW compute satellite in LEO, does it ever pay (in launched
mass) to add a heat pump and/or thermoradiative cells (TRC) to the heat
rejection chain, instead of pure passive radiators?

Answer (spoiler): under near-term parameters, no. This model shows why the
industry (e.g. Starcloud) chose passive radiation, and quantifies the exact
break-even thresholds future technologies would need to beat.

Physics
-------
- Only heat rejection in vacuum: radiation, q = eps * sigma * (T^4 - T_sink^4).
- LEO effective sink is NOT 3 K: the radiator sees Earth IR + albedo.
  We use an equivalent sink temperature (default 220 K).
- A heat pump raises rejection temperature (smaller radiator, T^4 law) but
  consumes electric power (more solar array mass) and adds its own mass.
- TRCs are "reverse solar cells": they generate power while radiating heat
  to cold space, at the cost of extra areal mass on the radiator.

Author: built interactively with Claude (Anthropic) as an exploration of
whether an amateur-conceived architecture could beat passive cooling.
It could not — and the negative result is the point.

Usage
-----
    python orbital_dc_thermal.py            # run scenarios + save figure
"""

from dataclasses import dataclass, replace
import numpy as np

SIGMA = 5.670374419e-8  # Stefan-Boltzmann constant [W m^-2 K^-4]


@dataclass(frozen=True)
class Params:
    """All model assumptions in one place. Change them, rerun, argue."""

    Q_chips: float = 1.0e6      # chip heat load [W] (= compute power)
    T_cold: float = 333.0       # immersion fluid temp leaving chips [K] (60 C)
    T_sink: float = 220.0       # LEO equivalent radiative sink [K]
    dT_hx: float = 5.0          # heat-exchanger drop in passive mode [K]

    emissivity: float = 0.90    # radiator IR emissivity
    fin_eff: float = 0.85       # radiator fin efficiency
    double_sided: bool = True   # radiator radiates from both faces

    eta_2nd: float = 0.45       # heat pump 2nd-law efficiency (frac. of Carnot)

    m_radiator: float = 6.0     # radiator areal mass [kg/m^2]
    m_trc_extra: float = 1.5    # TRC layer extra areal mass [kg/m^2]
    m_solar: float = 1000/120   # solar array specific mass [kg/kW] (120 W/kg)
    m_pump: float = 8.0         # heat pump specific mass [kg per kW electric]


@dataclass(frozen=True)
class Result:
    T_reject: float      # radiator temperature [K]
    area: float          # radiator area [m^2]
    W_pump: float        # heat pump electric input [W]
    P_trc: float         # TRC recovered power [W]
    P_solar: float       # required solar power [W]
    m_rad: float         # radiator mass [kg]
    m_sol: float         # solar array mass [kg]
    m_pmp: float         # heat pump mass [kg]

    @property
    def total_tonnes(self) -> float:
        return (self.m_rad + self.m_sol + self.m_pmp) / 1000.0


def evaluate(p: Params, T_hot: float, trc_eff: float = 0.0) -> Result:
    """Mass balance for one rejection temperature and TRC efficiency."""
    if T_hot <= p.T_cold + 0.5:  # passive: no pump, small HX penalty
        W_pump, T_r = 0.0, p.T_cold - p.dT_hx
        Q_rej = p.Q_chips
    else:
        cop_cooling = p.eta_2nd * p.T_cold / (T_hot - p.T_cold)
        W_pump = p.Q_chips / cop_cooling
        Q_rej = p.Q_chips + W_pump
        T_r = T_hot

    faces = 2 if p.double_sided else 1
    q_net = faces * p.emissivity * p.fin_eff * SIGMA * (T_r**4 - p.T_sink**4)
    area = Q_rej / q_net

    P_trc = trc_eff * Q_rej
    P_solar = p.Q_chips + W_pump - P_trc

    areal = p.m_radiator + (p.m_trc_extra if trc_eff > 0 else 0.0)
    return Result(T_r, area, W_pump, P_trc, P_solar,
                  m_rad=area * areal,
                  m_sol=P_solar / 1000 * p.m_solar,
                  m_pmp=W_pump / 1000 * p.m_pump)


def optimize(p: Params, trc_eff: float = 0.0,
             T_range=(334.0, 460.0)) -> Result:
    """Best rejection temperature (minimum launched mass) for a scenario."""
    Ts = np.arange(*T_range, 1.0)
    results = [evaluate(p, T, trc_eff) for T in Ts]
    return min(results, key=lambda r: r.total_tonnes)


def trc_breakeven_areal_mass(p: Params, trc_eff: float) -> float:
    """Max extra kg/m^2 a TRC layer may add and still save launched mass.

    At break-even, solar-array mass saved per m^2 equals TRC mass added:
        trc_eff * q_net [kW/m^2] * m_solar [kg/kW]
    """
    r = evaluate(p, p.T_cold)  # passive operating point
    q_net_kw = (r.area and (p.Q_chips / r.area) / 1000)
    return trc_eff * q_net_kw * p.m_solar


def main() -> None:
    p = Params()

    passive = evaluate(p, p.T_cold)
    pump = optimize(p)
    trc5 = optimize(p, trc_eff=0.05)

    print(f"{'Scenario':<28}{'T rej':>8}{'Area':>10}{'Solar':>9}{'Mass':>9}")
    for name, r in [("Passive", passive),
                    ("Heat pump (optimum)", pump),
                    ("Pump + TRC 5% (optimum)", trc5)]:
        print(f"{name:<28}{r.T_reject-273.15:>6.0f} C"
              f"{r.area:>8.0f} m2{r.P_solar/1000:>7.0f} kW"
              f"{r.total_tonnes:>8.2f} t")

    print("\nTRC break-even extra areal mass (must weigh LESS than this):")
    for eff in (0.02, 0.05, 0.10, 0.20):
        print(f"  {eff:>4.0%} efficiency -> {trc_breakeven_areal_mass(p, eff):.2f} kg/m^2")

    print("\nSensitivity: radiator areal mass [kg/m^2] vs best strategy:")
    for m in (4, 6, 9, 12):
        q = replace(p, m_radiator=float(m))
        print(f"  {m:>2} kg/m2: passive {evaluate(q, q.T_cold).total_tonnes:5.2f} t"
              f" | pump opt {optimize(q).total_tonnes:5.2f} t"
              f" | pump+TRC5% {optimize(q, 0.05).total_tonnes:5.2f} t")

    plot(p)


def plot(p: Params, path: str = "mass_vs_temperature.png") -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    Ts = np.arange(334, 461, 2.0)
    for eff, label in [(0.0, "Heat pump only"), (0.05, "Pump + TRC 5%")]:
        masses = [evaluate(p, T, eff).total_tonnes for T in Ts]
        plt.plot(Ts - 273.15, masses, label=label)
    plt.axhline(evaluate(p, p.T_cold).total_tonnes, ls="--", c="gray",
                label="Passive baseline")
    plt.xlabel("Rejection temperature [°C]")
    plt.ylabel("Total launched mass [t]")
    plt.title("1 MW orbital datacenter — thermal architecture mass balance")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    print(f"\nFigure saved: {path}")


if __name__ == "__main__":
    main()
