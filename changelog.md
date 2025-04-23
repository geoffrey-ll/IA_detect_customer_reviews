# Changelog

Toutes les modifications notables de ce projet seront consignées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/)
et ce projet adhère au principe de [versionnement sémantique](https://semver.org/lang/fr/).

---

## [1.1.0] - 2025-04-21

### Ajouté
- Création d’une fonction `clean_text()` pour nettoyer les commentaires (lowercase, suppression des caractères spéciaux, stopwords).
- Génération d’un nuage de mots (`WordCloud`) basé sur les commentaires nettoyés.
- Fonction `join_text()` pour concaténer les reviews.
- Fonction `generate_wordcloud()` + `display_wordcloud()` pour modulariser la visualisation.
- Script principal encapsulé dans une fonction `main()`.

### Modifié
- Code refactorisé pour plus de lisibilité et modularité : fonctions nommées proprement, constantes définies (`FILE`, `STOP_WORDS`).
- Séparation logique entre chargement, nettoyage, visualisation.

---

## [1.0.0] - 2025-04-20

### Ajouté
- Chargement du dataset CSV.
- Affichage des premières données et de la répartition des sentiments (`value_counts()` et histogramme).
- Import de `stopwords`, `matplotlib`, `nltk`, `wordcloud`.
