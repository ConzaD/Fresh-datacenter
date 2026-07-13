Pourquoi les centres de données orbitaux utilisent le refroidissement passif — Un modèle de masse au lancement

Un petit modèle Python, transparent, qui répond à une question simple : pour un satellite de calcul de 1 MW en orbite terrestre basse (LEO), est-il un jour avantageux — en termes de masse à lancer — d’ajouter une pompe à chaleur ou des cellules thermoradiatives (TRC) à la chaîne de rejet thermique, plutôt que d’utiliser uniquement des radiateurs passifs ?

Avec des paramètres réalistes à court terme, la réponse est non. Ce dépôt explique quantitativement pourquoi et calcule les seuils exacts à partir desquels de futures technologies deviendraient intéressantes. Les résultats négatifs sont aussi des résultats.

Contexte

Dans le vide, la seule façon d’évacuer la chaleur est par rayonnement (loi de Stefan-Boltzmann, q ∝ T⁴). Un mégawatt de chaleur dissipée par des GPU à environ 60 °C nécessite de l’ordre de 1 200 à 1 700 m² de radiateurs déployables, soit environ 20 fois la capacité de rejet thermique de la Station spatiale internationale (ISS).

Deux améliorations « astucieuses » viennent naturellement à l’esprit :

1. Une pompe à chaleur (par exemple thermoacoustique, sans pièces mobiles à grande échelle) : augmenter la température de rejet afin de réduire la surface des radiateurs grâce à la loi en T⁴.
2. Des cellules thermoradiatives (TRC) : l’équivalent inverse de panneaux photovoltaïques — des panneaux qui produisent de l’électricité tout en rayonnant leur chaleur vers l’espace froid, récupérant ainsi une partie de la chaleur perdue.

Ces approches échangent une réduction de la surface des radiateurs contre une augmentation d’autres masses à lancer (panneaux solaires, matériel de la pompe, radiateurs potentiellement plus lourds). Ce modèle évalue entièrement ce compromis.

Principaux résultats (hypothèses par défaut)

Scénario	Température de rejet	Radiateurs	Masse totale au lancement
Passif	55 °C	~1 250 m²	15,8 t
Pompe à chaleur (optimum)	61 °C	~1 150 m²	15,3 t
Pompe + TRC (5 %)	61 °C	~1 150 m²	16,6 t

Deux conclusions sont plus importantes que le tableau lui-même :

L’effet de levier de la loi en T⁴ est plus faible qu’il n’y paraît. En orbite terrestre basse, le puits thermique radiatif n’est pas le vide profond à 3 K : les radiateurs reçoivent également le rayonnement infrarouge et l’albédo de la Terre, ce qui correspond à une température de puits équivalente d’environ 220 K. Face à un puits déjà relativement chaud, augmenter la température de rejet apporte un gain limité, tandis que chaque kelvin supplémentaire d’élévation thermodynamique se paie en masse de panneaux solaires et de pompe. L’optimum revient donc très près de la température des puces : le refroidissement passif reste la meilleure solution.

Les TRC sont limitées par leur masse surfacique, bien plus que par leur rendement. Avec un rendement de conversion de 5 %, une couche de TRC ne doit ajouter moins de 0,33 kg/m² au radiateur pour réduire la masse totale à lancer (0,13 kg/m² avec le rendement actuel d’environ 2 % ; 1,33 kg/m² avec un rendement futuriste de 20 %). Cela correspond à des technologies de couches minces, sans même tenir compte de l’électronique de puissance. À ma connaissance, ce seuil de rentabilité n’a jamais été publié.

Exécution

python orbital_dc_thermal.py

Aucune dépendance en dehors de numpy et matplotlib. Toutes les hypothèses sont regroupées dans la classe de données Params située au début du fichier : modifiez-les puis relancez le modèle.

Le programme affiche le tableau des différents scénarios, les seuils de rentabilité des TRC, une étude de sensibilité sur la masse surfacique des radiateurs, puis enregistre le graphique mass_vs_temperature.png.

Limites du modèle

Il s’agit d’un modèle de premier ordre centré sur le bilan de masse, volontairement simple : une température de puits équivalente unique (sans variations orbitales transitoires), aucune prise en compte des masses de structure ou du contrôle d’attitude, pas de batteries pour les périodes d’éclipse (une orbite héliosynchrone à l’aube et au crépuscule est supposée), une efficacité de la pompe à chaleur constante vis-à-vis de la deuxième loi de la thermodynamique, et aucun modèle économique (la masse servant d’approximation du coût de lancement).

Son objectif est de mettre en évidence la forme de l’espace des compromis, et non de remplacer un outil de simulation thermique détaillé comme ESATAN. Les corrections et propositions d’amélioration (pull requests) sont les bienvenues.
