# 🧩 Sudoku Deluxe

Bienvenue dans **Sudoku Deluxe**, un jeu de Sudoku complet réalisé en **Python** avec **Tkinter**.  
Ce projet met en pratique la **programmation orientée objet (POO)**, la gestion d’interfaces graphiques et la génération algorithmique de grilles de Sudoku.

---

## 📜 Sommaire

1. [Aperçu du projet](#-aperçu-du-projet)  
2. [Fonctionnalités](#-fonctionnalités)  
3. [Architecture du code](#-architecture-du-code)  
4. [Installation](#-installation)  
5. [Exécution](#-exécution)  


---

## 🎯 Aperçu du projet

**Sudoku Deluxe** est une application qui permet de :
- Générer automatiquement des grilles de Sudoku valides.
- Jouer à différents niveaux de difficulté.
- Bénéficier d’un chronomètre, d’un système de vies et d’animations interactives.
- Visualiser les erreurs en temps réel.

Ce projet a été conçu dans le cadre d’un travail pratique de **Programmation Orientée Objet (POO)**.

---

## ⚙️ Fonctionnalités

✅ **Génération automatique** de grilles complètes et valides.  
✅ **4 niveaux de difficulté** :  
- 🟢 Facile  
- 🟡 Moyen  
- 🔴 Expert  
- ⚫ Maître  

✅ **Interface graphique (Tkinter)** intuitive et colorée.  
✅ **Système de vies** : 3 erreurs maximum avant Game Over.  
✅ **Chronomètre en temps réel**.  
✅ **Animations** de victoire et d’échec.  
✅ **Réinitialisation** rapide de la partie.  
✅ **Changement de niveau** à tout moment.

---

## 🧱 Architecture du code

Le programme est découpé en deux parties :

### 1️⃣ Fonctions utilitaires
Situées au début du fichier :
- `init_sudoku()` → Initialise une grille vide (9×9).
- `est_valide()` → Vérifie la validité d’un chiffre dans la grille.
- `remplir_grille()` → Remplit la grille récursivement avec des chiffres valides.
- `enlever_chiffres()` → Supprime des valeurs pour créer la grille à jouer selon la difficulté.
- `reinitialiser_grille()` → Relance une partie complète.

### 2️⃣ Classe principale : `SudokuGUI`
Contient toute la logique d’interface et du jeu :
- Création des widgets Tkinter (Labels, Buttons, Entries…)
- Gestion des événements clavier/souris.
- Vérification des saisies.
- Gestion du chrono et des vies.
- Lancement des animations.

---

## 💻 Installation

### Prérequis
- **Python 3.8+ (développé sous spyder)** 
- Bibliothèques :
  ```bash
  pip install numpy


### ✅ Execution 
- **Lance le code en appuyant sur F5 ou la flèche en haut** 

**Régale toi !!!!**
