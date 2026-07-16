# Glossaire technique & formules — Datacenter orbital

Document de référence du projet. Partie 1 : les termes, expliqués simplement.
Partie 2 : chaque formule utilisée, symbole par symbole, avec l'exemple
numérique tiré de nos calculs.

---

## PARTIE 1 — GLOSSAIRE

**Albédo** — Fraction de la lumière solaire qu'une planète réfléchit (~30 %
pour la Terre). Un radiateur en orbite reçoit ce reflet en plus de
l'infrarouge terrestre : ça réchauffe son « puits ».

**Boucle diphasique** — Circuit de refroidissement où le fluide change de
phase (liquide ↔ vapeur), transportant la chaleur via la chaleur latente.
Très efficace, mais délicat en apesanteur : les bulles ne « montent » pas.

**Caloduc (heat pipe)** — Tube scellé contenant un fluide qui s'évapore côté
chaud et se condense côté froid, transportant la chaleur passivement, sans
pompe. Brique de base des radiateurs spatiaux classiques.

**Chaleur latente (L)** — Énergie absorbée par un fluide pour changer d'état
sans changer de température. L'eau qui s'évapore emporte 2,26 MJ/kg : c'est le
principe des refroidisseurs « ouverts » (sublimateurs de scaphandres).

**Chaleur spécifique (cp)** — Énergie qu'il faut pour élever 1 kg d'une
substance de 1 °C (ou 1 K). Eau : ~4200 J/(kg·K) ; huile silicone :
~1600 J/(kg·K). Gouverne combien de chaleur un débit de fluide transporte.

**Charge par induction** — Méthode pour charger une gouttelette sans la
toucher : une électrode sous tension près du point de rupture du jet attire
des charges dans le liquide ; la goutte se détache en les emportant. C'est le
principe de l'imprimante jet d'encre continu.

**COP (coefficient de performance)** — « Rendement » d'une pompe à chaleur :
chaleur déplacée ÷ électricité consommée. Peut dépasser 1 (on déplace la
chaleur, on ne la crée pas). Plus l'écart de température à franchir est
grand, plus le COP chute.

**Coupelle de Faraday** — Récipient métallique relié à un mesureur de
courant : tout ce qui y dépose des charges est compté. Sert à mesurer la
charge portée par un jet de gouttelettes.

**Delta-v (Δv)** — « Budget de vitesse » d'une manœuvre spatiale, en km/s.
Mesure universelle du coût d'un déplacement orbital : changer de plan
orbital en orbite basse coûte plusieurs km/s, souvent plus qu'un lancement.

**Edge-on (de chant)** — Orientation d'un radiateur plat présentant sa
tranche (et non sa face) à une source chaude (Terre, Soleil) pour minimiser
ce qu'il en reçoit.

**Émissivité (ε)** — Aptitude d'une surface à rayonner, entre 0 (miroir
parfait) et 1 (corps noir idéal). Les revêtements de radiateurs spatiaux
atteignent ~0,9.

**Épaisseur optique** — Mesure de l'opacité d'un nuage de gouttelettes à son
propre rayonnement. Nappe trop dense : les gouttes du centre rayonnent vers
leurs voisines au lieu de l'espace ; trop diluée : on gaspille de la surface.

**Facteur de vue** — Fraction du « champ de vision » d'une surface occupée
par un objet donné. Un radiateur face à la Terre à 500 km a un facteur de vue
terrestre ~0,4 ; de chant, ~0,1. Pondère tous les échanges radiatifs.

**HOTDOCK** — Interface de docking robotique européenne standardisée
transférant mécanique, électricité, données et, en option, du fluide
caloporteur entre modules.

**ISAM** — In-Space Assembly and Manufacturing : le champ de l'assemblage et
de la fabrication en orbite (bras robotiques, interfaces standard).

**ISRU** — In-Situ Resource Utilization : utiliser les ressources locales
(régolithe lunaire → panneaux solaires, blindage) au lieu de tout lancer.

**LDR (Liquid Droplet Radiator)** — Radiateur à gouttelettes : le fluide
chaud est pulvérisé en nappe de gouttes qui rayonnent leur chaleur en vol
libre avant d'être collectées et repompées. Supprime le panneau, donc
l'essentiel de la masse.

**LEO (Low Earth Orbit)** — Orbite basse terrestre, ~300–1000 km d'altitude.
Période ~90 min. C'est là que visent les datacenters orbitaux.

**Limite de Rayleigh** — Charge électrique maximale qu'une gouttelette peut
porter avant que la répulsion interne ne la fasse éclater. Fixe le plafond
de « prise » électrostatique sur chaque goutte.

**Liquide ionique** — Sel liquide à température ambiante, à pression de
vapeur quasi nulle (10⁻⁹ à 10⁻¹¹ Pa) : il ne s'évapore pratiquement pas,
même dans le vide. Candidat idéal pour un LDR ; n'existait pas dans les
études des années 80.

**Masse surfacique (kg/m²)** — Masse d'un radiateur par mètre carré de
surface rayonnante. LA figure de mérite du projet : panneaux classiques
~6 kg/m², LDR équivalent ~1,4 kg/m².

**Monodisperse** — Se dit d'un ensemble de gouttes toutes de même taille.
Obtenu en forçant la rupture du jet à une fréquence fixe (piézo).

**Nadir** — La direction « droit vers le bas », vers le centre de la Terre,
depuis un satellite. Opposé : zénith.

**Orbite héliosynchrone crépusculaire (dawn-dusk)** — Orbite polaire qui
survole en permanence la frontière jour/nuit : le satellite voit le Soleil
quasi en continu (pas d'éclipse, donc pas de batteries) et le Soleil reste
perpendiculaire au plan de l'orbite.

**OSR (Optical Solar Reflector)** — Revêtement de radiateur « miroir au
soleil, corps noir en infrarouge » : absorbe ~8 % du visible mais émet ~80 %
en IR. Permet à un radiateur de tolérer un éclairage solaire oblique.

**Peltier (effet)** — Pompage de chaleur purement électrique dans un
semi-conducteur. Sans pièce mobile mais COP très faible : écarté par notre
modèle.

**Pompe à chaleur** — Machine qui déplace la chaleur d'une source froide vers
une source chaude en consommant du travail (électricité). Dans l'espace,
elle permet de rejeter plus chaud — mais ajoute sa consommation au bilan.

**Pompe thermoacoustique** — Pompe à chaleur où le « piston » est une onde
sonore dans un gaz : quasi aucune pièce mobile, d'où la fiabilité spatiale
(les cryoréfrigérateurs à tube pulsé volent depuis des décennies).

**Pression de vapeur** — Tendance d'un liquide à s'évaporer. Dans le vide,
un fluide à pression de vapeur trop haute « bout » et disparaît. Critère n° 1
du fluide d'un LDR.

**Puits radiatif (T_puits)** — Température équivalente unique résumant tout
ce que le radiateur « voit » (espace profond, Terre, Soleil), pondéré par
les facteurs de vue. En LEO : ~220 K. C'est le plancher de l'échange radiatif.

**Rayleigh-Plateau (instabilité de)** — Phénomène qui fait qu'un jet liquide
se brise spontanément en gouttes (comme un filet d'eau de robinet). En
l'excitant avec un piézo à fréquence fixe, on force des gouttes uniformes.

**Redondance N+k** — Stratégie de fiabilité : embarquer k unités de plus que
les N nécessaires, et router autour des pannes au lieu de réparer.

**Régolithe** — Poussière et débris couvrant la surface lunaire. Abrasif,
électrostatique, excellent isolant thermique (on ne peut pas y « enterrer »
de la chaleur).

**Stefan-Boltzmann (loi de)** — Loi physique : toute surface rayonne une
puissance proportionnelle à la puissance quatrième de sa température
absolue. Le fondement de tout le projet.

**Sublimateur / évaporateur flash** — Refroidisseur « ouvert » qui vaporise
de l'eau dans le vide, emportant la chaleur latente. Efficace mais consomme
la masse d'eau : réservé aux transitoires (scaphandres, navette).

**TRC (cellule thermoradiative)** — Photovoltaïque « inversé » : chaud et
face au froid de l'espace, il génère de l'électricité en rayonnant. Rendement
actuel ~2 % ; tué dans notre modèle par sa masse surfacique.

---

## PARTIE 2 — LES FORMULES, EXPLIQUÉES

### 1. Loi de Stefan-Boltzmann (le cœur de tout)

    q = ε · σ · (T⁴ − T_puits⁴)

- **q** : flux net rayonné, en watts par m² de surface.
- **ε** (epsilon) : émissivité de la surface (0,9 pour nous).
- **σ** (sigma) : constante de Stefan-Boltzmann = 5,67 × 10⁻⁸ W/(m²·K⁴).
  Constante universelle, mesurée, non négociable.
- **T** : température du radiateur en kelvins (K = °C + 273).
- **T_puits** : température équivalente de ce que le radiateur regarde.
- Les **puissances 4** : doubler T multiplie le rayonnement par 16. C'est
  pourquoi « rejeter plus chaud » est tentant — et pourquoi un puits chaud
  (220⁴ n'est pas négligeable devant 313⁴) gâche l'affaire.

Exemple du modèle : radiateur double face à 328 K, puits 220 K, avec un
rendement d'ailette de 0,85 :
q = 2 × 0,9 × 0,85 × 5,67e-8 × (328⁴ − 220⁴) ≈ 800 W/m²
→ pour 1 MW : A = 1 000 000 ÷ 800 ≈ 1 250 m².

### 2. Dimensionnement de surface

    A = Q_rejeté / q

- **A** : surface de radiateur nécessaire (m²).
- **Q_rejeté** : puissance thermique totale à évacuer (W) — les puces, plus
  la consommation de la pompe s'il y en a une.
- Division simple : tant de watts à évacuer, tant de watts par m².

### 3. Pompe à chaleur : COP de Carnot et COP réel

    COP_Carnot (froid) = T_froid / (T_chaud − T_froid)
    COP_réel = η₂ · COP_Carnot
    W_pompe = Q_puces / COP_réel

- **T_froid** : température où l'on prend la chaleur (les puces, 333 K).
- **T_chaud** : température où on la rejette (le radiateur).
- **COP_Carnot** : plafond théorique absolu fixé par la thermodynamique.
  Toutes les températures en kelvins, jamais en °C !
- **η₂** (rendement de second principe) : fraction du plafond de Carnot
  qu'une machine réelle atteint (0,45 = bonne machine).
- **W_pompe** : électricité consommée par la pompe (W).
- Lecture : plus l'écart T_chaud − T_froid grandit, plus le COP s'effondre
  et plus la pompe coûte cher en électricité — c'est ce qui tue l'idée n° 1.

Exemple : pomper de 333 K vers 373 K : COP_Carnot = 333/40 ≈ 8,3 ;
réel ≈ 0,45 × 8,3 ≈ 3,7 ; pour 1 MW de puces : W_pompe ≈ 270 kW.

### 4. Transport de chaleur par un débit de fluide

    Q = ṁ · cp · ΔT   →   ṁ = Q / (cp · ΔT)

- **ṁ** (« m point ») : débit massique, en kg/s.
- **cp** : chaleur spécifique du fluide (1600 J/(kg·K) pour le silicone).
- **ΔT** (delta T) : refroidissement du fluide entre l'entrée et la sortie.
- Lecture : pour transporter 1 MW avec un fluide qui se refroidit de 30 K,
  il faut ṁ = 1e6 / (1600 × 30) ≈ 20,8 kg/s. C'est de là que viennent les
  6,6 millions de tonnes recyclées en 10 ans (20,8 × nombre de secondes).

### 5. Refroidissement « ouvert » par évaporation

    ṁ_eau = Q / L

- **L** : chaleur latente de vaporisation (eau : 2,26 × 10⁶ J/kg).
- Pour absorber 1 MW en continu : 1e6 / 2,26e6 ≈ 0,44 kg/s ≈ 38 t/jour.
  C'est le calcul qui a réfuté le « frigo à gaz consommable ».

### 6. Temps de refroidissement d'une gouttelette

    t ≈ (ρ · cp · ΔT · r/3) / q_goutte

- **ρ** (rho) : masse volumique du fluide (~900 kg/m³).
- **r** : rayon de la goutte (100 µm = 10⁻⁴ m).
- **r/3** : rapport volume/surface d'une sphère (V/A = r/3) — c'est lui qui
  rend les petites gouttes si rapides à refroidir.
- **q_goutte** : flux net rayonné par la surface de la goutte (W/m²).
- Résultat : ~3 s pour une goutte isolée ; ~11 s dans la nappe (les gouttes
  se réchauffent mutuellement — effet d'épaisseur optique).
- Loi d'échelle : t ∝ r (moitié plus petites = moitié plus rapides) et
  t ∝ 1/T³ environ (des gouttes très chaudes refroidissent quasi
  instantanément).

### 7. Limite de Rayleigh (charge maximale d'une goutte)

    q_R = 8π · √(ε₀ · γ · r³)

- **q_R** : charge maximale en coulombs avant éclatement de la goutte.
- **ε₀** (epsilon zéro) : permittivité du vide = 8,85 × 10⁻¹² F/m
  (constante universelle de l'électrostatique).
- **γ** (gamma) : tension de surface du liquide (~0,02 N/m pour une huile) —
  la « peau » qui retient la goutte contre la répulsion de ses charges.
- **r³** sous la racine : les grosses gouttes encaissent plus de charge.
- Exemple : r = 100 µm → q_R ≈ 10⁻¹¹ C = 10 pC. On opère à ~30 % (3 pC).

### 8. Force et déflexion électrostatiques

    F = q · E      a = F / m      d = ½ · a · t²

- **q** : charge de la goutte (3 pC) ; **E** : champ électrique (V/m).
- **F = qE** : force de Coulomb sur la goutte (10⁵ V/m → 3 × 10⁻⁷ N).
- **m** : masse de la goutte = ρ · (4/3)πr³ ≈ 3,8 × 10⁻⁹ kg.
- **a = F/m** : accélération ≈ 80 m/s² — presque 10 g sur une gouttelette !
- **d = ½at²** : déflexion accumulée en un temps t (chute libre inversée) :
  en 0,1 s près du collecteur, d ≈ 0,4 m. C'est l'« autorité » du champ.

### 9. Évaporation dans le vide (flux de Langmuir)

    J = P_vap · √(M / (2π · R · T))

- **J** : masse évaporée par m² et par seconde (kg/m²/s).
- **P_vap** : pression de vapeur du fluide à la température T (Pa).
- **M** : masse molaire du fluide (kg/mol) ; **R** = 8,314 J/(mol·K),
  constante des gaz parfaits.
- Lecture : dans le vide, tout ce qui s'évapore part pour toujours. Notre
  budget (100 kg perdus en 10 ans sur 1 500 m²) impose P_vap < 4 × 10⁻⁸ Pa —
  le critère qui sélectionne huiles silicones et liquides ioniques.

### 10. Seuil de rentabilité des TRC

    Δm_max = η_TRC · q_net · m_solaire

- **Δm_max** : surcoût massique maximal admissible de la couche TRC (kg/m²).
- **η_TRC** : rendement de conversion de la cellule (0,02 à 0,20).
- **q_net** : flux rejeté par m² de radiateur (kW/m²).
- **m_solaire** : masse de panneau solaire par kW produit (8,33 kg/kW).
- Logique : chaque m² de TRC récupère η·q_net kilowatts, donc économise
  η·q_net·m_solaire kilos de panneaux. Si la couche pèse plus que ça,
  elle fait perdre de la masse. À 5 % : 0,33 kg/m². Implacable.

### 11. Budget de capture des gouttelettes

    fraction_perte_max = M_réserve / (ṁ · durée_mission)

- **M_réserve** : masse de fluide de réserve embarquée (kg).
- **ṁ · durée** : masse totale circulée (20,8 kg/s × 3,15 × 10⁸ s ≈
  6,6 × 10⁹ kg sur 10 ans).
- Exemple : 1 t de réserve → fraction max 1,5 × 10⁻⁷ → capture requise
  99,99998 %. La formule montre pourquoi le réservoir n'achète que peu :
  la masse circulée au dénominateur est astronomique.

---

*Astuce de lecture générale : dans toutes ces formules, les températures
sont en kelvins, les masses en kg, les puissances en watts. La plupart des
erreurs de calcul viennent d'un °C resté en °C ou d'un kW pris pour un W.*
