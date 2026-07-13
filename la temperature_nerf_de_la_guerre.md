# Pourquoi les datacenters spatiaux seront refroidis « passivement » — j'ai fait le calcul

Starcloud, Google et d'autres veulent mettre des datacenters en orbite : énergie solaire quasi continue, pas de foncier, pas de voisins. Mais il y a un mur physique dont on parle peu : dans le vide, la chaleur ne s'évacue que par rayonnement. Un mégawatt de GPU à 60 °C exige de l'ordre de 1 200 à 1 700 m² de radiateurs déployables — environ vingt fois la capacité de rejet thermique de toute la Station spatiale internationale.

Je suis parti d'une intuition : et si on améliorait ça avec une pompe à chaleur (rejeter plus chaud, donc rayonner plus fort grâce à la loi en T⁴) ou avec des cellules thermoradiatives — des panneaux photovoltaïques « inversés » qui produisent de l'électricité en rayonnant la chaleur vers le froid de l'espace ? Plutôt que d'en rester à l'intuition, j'ai construit un modèle de bilan de masse complet, en m'appuyant sur une IA pour dérouler la physique et vérifier l'état de l'art. Voici ce que les chiffres m'ont appris.

## Premier enseignement : le levier T⁴ est plus faible qu'il n'y paraît

En orbite basse, un radiateur ne rayonne pas vers les 3 K de l'espace profond : il voit la Terre, son infrarouge et son albédo. Le puits radiatif effectif est plutôt vers 220 K. Face à un puits aussi « chaud », remonter la température de rejet rapporte peu — et chaque degré de remontée thermodynamique se paie en panneaux solaires et en masse de pompe. Résultat : l'optimum de masse totale retombe quasiment à la température des puces. Le refroidissement passif de Starcloud n'est pas un choix conservateur, c'est le bon calcul.

## Deuxième enseignement : les cellules thermoradiatives meurent par leur masse, pas par leur rendement

C'est le chiffre que je n'ai trouvé publié nulle part. À 5 % de rendement de conversion, une couche thermoradiative doit ajouter moins de 0,33 kg/m² au radiateur pour économiser le moindre gramme de masse lancée. Au rendement actuel des laboratoires (~2 %), le budget tombe à 0,13 kg/m² — l'épaisseur d'un film mince, avant même de compter l'électronique de puissance. Même à un futuriste 20 %, le plafond n'est que de 1,33 kg/m². La technologie a un avenir pour alimenter des sondes lointaines, mais pas pour refroidir des datacenters, sauf percée radicale sur la masse surfacique.

## Troisième enseignement : le vrai levier est ailleurs

La sensibilité du modèle est sans appel : passer les radiateurs de 6 à 4 kg/m² économise 2,5 tonnes — plus que toutes les architectures « intelligentes » que j'ai testées réunies. Le nerf de la guerre, ce sont les matériaux et les mécanismes de déploiement, pas la thermodynamique.

## Ce que cette démarche m'a appris

J'ai commencé cette exploration en cherchant une invention brevetable. Le modèle a réfuté mes trois idées successives — pompe thermoacoustique, récupération thermoradiative, optimisation géométrique du puits — soit parce que le gain était mangé par la masse ajoutée, soit parce que l'antériorité existait déjà. C'est frustrant, et c'est précisément la valeur de l'exercice : quelques heures de modélisation valent mieux que des milliers d'euros de dépôt de brevet sur une idée non chiffrée.

Le code est ouvert, toutes les hypothèses sont dans une seule structure de paramètres, et je serais ravi qu'un thermicien me corrige : [lien vers le dépôt GitHub].

---
*Modèle d'ordre 1, construit avec l'aide de Claude (Anthropic) : puits équivalent constant, pas de transitoire orbital, pas de masse structurale ni de batteries d'éclipse (orbite héliosynchrone crépusculaire supposée). Les limites sont détaillées dans le README.*
