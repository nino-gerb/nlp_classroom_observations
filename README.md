# Comparaison du discours d’enseignants pré-service et in-service  
**Mémoire de Master HEP Vaud – Discipline Informatique, Degré secondaire II**  
**Auteur :** Nino Gerber  
**Superviseur :** Gabriel Parriaux  
**Date de soutenance :** 23 juin 2025  

---

## Contexte  
Ce projet correspond à la rédaction et à l’analyse d’un mémoire de Master of Science à la Haute école pédagogique du canton de Vaud. Il explore les différences de style discursif entre enseignants en formation initiale (pré-service) et enseignants en exercice (in-service) à l’aide d’outils de Traitement Automatique du Langage (TAL).  

## Structure du dépôt  
- `data/` : transcriptions et métadonnées disponible sur demande
- `notebooks/` : jupyter notebooks pour le prétraitement, la génération d’embeddings, BERTopic, PCA, analyse de sentiments  
- `utiles/` : scripts Python auxiliaires    
- `images/` : figures et tableaux générés  
- `README.md` : description du projet  

## Pipeline méthodologique  
1. **Prétraitement**  
   - Tokenisation, lemmatisation, suppression des stop-words  
2. **Vectorisation sémantique**  
   - Sentence-BERT multilingue → embeddings de dimension 384  
3. **Modélisation thématique**  
   - BERTopic (UMAP + HDBSCAN + c-TF-IDF)  
   - Test z de proportion avec correction de multitests  
4. **Réduction de dimension**  
   - ACP (PCA) pour projeter les embeddings en 2D  
5. **Analyse de sentiments**  
   - Méthode lexicale + modèle pré-entraîné → score moyen par segment  

## Principaux résultats  

### 1. Analyse de sentiments  
Chaque segment de discours reçoit un score moyen (négatif / neutre / positif).  

<p align="center">
<img alt="sentiment_distribution" src="https://github.com/user-attachments/assets/55f2dff9-698f-4a0d-8f01-9c5d5f8fe0c1" 
    width="600" 
    style="max-width:100%; height:auto;">
</p>


- Les tests statistiques (z = –1.57, p = 0.1166) n’indiquent pas de différence significative au seuil 5 %, bien que la tendance graphique montre un léger discours plus négatif chez les enseignants in-service!


### 2. Modélisation thématique (BERTopic)  
Les vingt thèmes les plus discriminants entre pré-service et in-service :  

<p align="center">
<img alt="top_topics_discriminants" src="https://github.com/user-attachments/assets/60312810-8a6b-4799-9a75-7caa482b70ef" 
    width="600" 
    style="max-width:100%; height:auto;">
</p>

- **In-service (z > 0)** : “Références élèves”, “Couleurs et créativité”, “Configuration technique”, etc.  
- **Pré-service (z < 0)** : “Interjections”, “Excuses / retards”, “Expressions orales”, “Exercices et menus”, etc.

### 3. Projection PCA  
Projection des segments de discours dans l’espace sémantique 2D :  

<p align="center">
<img alt="pca" src="https://github.com/user-attachments/assets/f9c86749-ea9a-43ef-9f00-b1d8013aebc1" 
    width="600" 
    style="max-width:100%; height:auto;">
</p>
  
- **PC1 (axe horizontal)** : informel/spontané ←→ structuré/normatif  
- **PC2 (axe vertical)** : procédural/tâche immédiate ←→ conceptuel/réflexif

## Conclusion  
Ce travail illustre la complémentarité des méthodes de Traitement Automatique du Langage pour caractériser automatiquement les différences discursives entre enseignants pré-service et in-service.  
- L’analyse thématique (BERTopic) révèle des styles distincts : un discours spontané et ancré dans l’expérience pour les pré-service, versus un langage structuré et réflexif pour les in-service.  
- La projection PCA conforte ces observations en visualisant clairement la séparation sémantique entre les deux groupes.  
- L’analyse de sentiments, bien qu’elle ne mette pas en évidence de différence significative, suggère une tendance légèrement plus négative chez les enseignants en exercice.

Ces résultats offrent un cadre méthodologique reproductible pour analyser le discurs professionnel à travers l’exploitation de leurs discours.  

