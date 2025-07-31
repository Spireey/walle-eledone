# WALL-E - Eledone

Bienvenue dans **WALL-E**, une simulation où des robots ramassent des déchets dans une grille virtuelle.  

---

## Objectif

Simuler des robots intelligents (ou pas trop) qui nettoient une grille remplie de déchets.  
Ce projet est découpé en deux parties :

- **Backend** : en **Python/Django** avec API REST
- **Frontend** : en **React/TypeScript** avec **Tailwind CSS**

---

## Fonctionnalités

### Côté Backend (Django)
- `POST /create_grid?robots=X&trash=Y` → génère une grille de simulation
- `POST /start_simulation` → démarre la simulation
- `POST /step_simulation` → effectue une étape
- `POST /reset_simulation` → réinitialise tout

### Côté Frontend (React)
- Interface utilisateur pour créer une grille
- Affichage dynamique de la grille
- Bouton “Start Simulation” pour lancer automatiquement les étapes
- Arrêt automatique quand tous les déchets sont ramassés

---

## Lancement avec Docker

```bash
docker compose up --build
