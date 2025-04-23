import re

import matplotlib.pyplot as plt
import pandas as pd
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud


FILE = "reviews.csv"
STOP_WORDS = set(stopwords.words("french"))


def load_csv(filename=FILE):
    return pd.read_csv(filename)


df = load_csv()


def load_nltk_element():
    # Un fois le ddl fais, ces lignes ne sont plus nécessaires.
    # Stockage en local.
    nltk.download("punkt")
    nltk.download("stopwords")


def display_path_nltk_ddl():
    print(nltk.data.path)


def display_generic_infos():
    print("Aperçu des données :")
    print(df.head())
    print(f"\nNombre total d'avis : {len(df)}")
    print("\nRépartition des sentiments :")
    print(df['sentiment'].value_counts())


def display_sentiment_distribution():
    df["sentiment"].value_counts().plot(kind="hist",
                                        color=["green", "red", "gray"])
    plt.title("Répartition des sentiments dans les avis")
    plt.xlabel("Sentiment")
    plt.ylabel("Nombre d'avis")
    plt.show()


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Zéèàùâêîôûçëïüœ\s]", "", text)
    words = text.split()
    filtered_words = [word for word in words if word not in STOP_WORDS]

    return " ".join(filtered_words)


def join_text(text):
    return " ".join(text)


def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400,
                                 background_color="black",
                                 colormap="viridis").generate(text)
    return wordcloud


def display_wordcloud(wordcloud, title="Most Frequent Words"):
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(title, fontsize=16)
    return plt.show()


def main():
    # display_generic_infos()
    # display_sentiment_distribution()

    df["clean_review"] = df["review"].apply(clean_text)
    full_text_clean = join_text(df["clean_review"])

    wordcloud = generate_wordcloud(full_text_clean)
    display_wordcloud(wordcloud)


if __name__ == "__main__":
    main()
