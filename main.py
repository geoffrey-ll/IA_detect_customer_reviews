import re

import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
from wordcloud import WordCloud


# Chargement du fichier CSV
df = pd.read_csv("reviews.csv")

# # Affichage des premières lignes
# print("Aperçu des données :")
# print(df.head())
#
# # Dimensions du dataset
# print(f"\nNombre total d'avis : {len(df)}")
#
# # Comptage des classes (positive, negative, neutral)
# print("\nRépartition des sentiments :")
# print(df['sentiment'].value_counts())

df['sentiment'].value_counts().plot(kind='hist', color=['green', 'red', 'gray'])
plt.title("Répartition des sentiments dans les avis")
plt.xlabel("Sentiment")
plt.ylabel("Nombre d'avis")
# plt.show()


# Pourquoi prétraiter le texte ?
# Le texte brut (comme "Ce produit est super !") est difficile à exploiter directement pour une machine. Il faut le transformer étape par étape en une forme plus simple et standardisée.
# Exemple d'objectifs :
#   Supprimer le bruit (ponctuation, majuscules, mots inutiles),
#   Découper les phrases en mots,
#   (Optionnel) Réduire les mots à leur racine (lemmatisation
#   Obtenir une liste de mots propres exploitables par un modèle.

# Étapes classiques de prétraitement
# On va faire ça avec pandas, re (regex) et nltk :
# Mettre en minuscules
#   Supprimer la ponctuation
#   Supprimer les chiffres
#   Tokenisation (découper en mots)
#   Supprimer les stopwords (mots comme "le", "et", "de"...)
#   (Optionnel) Lemmatisation (réduire "adorait", "adorer", "adorable" → "adorer")

# Un fois le ddl fais, c’est ligne ne sont plus nécessaire. Stockage en local
# nltk.download("punkt")
# nltk.download("stopwords")
# print(nltk.data.path)

stop_words = set(stopwords.words("french"))


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Zéèàùâêîôûçëïüœ\s]', '', text)

    # mots = word_tokenize(text, language="french")
    words = text.split()
    utils_words = [word for word in words if word not in stop_words]

    return " ".join(utils_words)



df["clean_review"] = df["review"].apply(clean_text)

# print(f"review:\n{df["review"].head()}"
#       f"\nclean\n{df['clean_review'].head()}")


# Concaténer toutes les reviews nettoyées en une seule chaîne
text_dirty = " ".join(df["review"])
text_clean = " ".join(df["clean_review"])


# Générer le nuage de mots
wordcloud_before = WordCloud(width=800, height=400, background_color="black", colormap="viridis").generate(text_dirty)
# Afficher le résultat
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_before, interpolation='bilinear')
plt.axis("off")
plt.title("Most Frequent Words in Dirty Reviews", fontsize=16)
# plt.show()

# Générer le nuage de mots
wordcloud = WordCloud(width=800, height=400, background_color="black", colormap="viridis").generate(text_clean)
# Afficher le résultat
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Most Frequent Words in Cleaned Reviews", fontsize=16)
plt.show()
