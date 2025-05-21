# Projet de Simulation de Files d'Attente — M/M/1, G/M/1, M/G/1

## 📌 Description

Ce projet vise à simuler et analyser trois modèles de files d’attente mono-serveur :

- **M/M/1** : arrivées et services selon une loi exponentielle.
- **G/M/1** : arrivées générales (loi uniforme), services exponentiels.
- **M/G/1** : arrivées de type Poisson, services généraux (loi uniforme).

Le but est de visualiser l’impact de l’augmentation du taux d’arrivée (λ) sur les performances du système :  
temps d’attente moyen, temps de réponse moyen, et taux d’occupation.

## 📁 Structure du projet

Le projet est organisé en trois dossiers, un par modèle :

MM1/
├── simulate_mm1.py
├── experiments_mm1.py
├── main_mm1.py
├── plots_mm1.py
└── GRAPHEMM1/

GM1/
├── simulate_gm1.py
├── experiments_gm1.py
├── main_gm1.py
├── plots_gm1.py
└── GRAPHEGM1/

MG1/
├── simulate_mg1.py
├── experiments_mg1.py
├── main_mg1.py
├── plots_mg1.py
└── GRAPHEMG1/


## ⚙️ Dépendances

Installez les bibliothèques nécessaires avec :
pip install numpy matplotlib seaborn

# #🚀 Lancement des simulations
Dans chaque dossier, un script main_*.py permet de lancer les simulations et d’afficher les résultats.

# Simulation du modèle M/M/1
cd ../MM1
python main_mm1.py

# Simulation du modèle G/M/1
cd ../GM1
python main_gm1.py

# Simulation du modèle M/G/1
cd ../MG1
python main_mg1.py
Les graphiques seront générés automatiquement et enregistrés dans les dossiers GRAPHE*.

# #📊 Résultats produits
Pour chaque modèle, les courbes suivantes sont générées :

   -Temps d’attente moyen en fonction de λ

   -Temps de réponse moyen en fonction de λ

   -Taux d’occupation du serveur en fonction de λ

# #🎯 Objectif pédagogique
Ce projet permet de :
   -Comparer l’impact des distributions d’arrivée et de service sur les files d’attente.

   -Mettre en évidence les différences de performance entre les modèles M/M/1, G/M/1 et M/G/1.

   -Visualiser la dégradation des performances à l’approche de la saturation du système.

# #👨‍💻 Auteurs
   -CHETOUH Amira Narimane

   -SADAOUI Sara Rahma

   -DAHMANI Naila

USTHB — 3ème Année CS — 2024–2025


---
