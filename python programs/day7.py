# -*- coding: utf-8 -*-
"""Day7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g7WFF-GR7rLMkGtv7LFmdx-fix3VKtmJ
"""

import nltk
from nltk.corpus import stopwords
import spacy

# Download stopwords if not already downloaded
nltk.download('stopwords')

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Load NLTK stopwords
    stop_words = set(stopwords.words('english'))

    # Load SpaCy English model
    nlp = spacy.load("en_core_web_sm")

    # Use SpaCy for tokenization
    doc = nlp(text)

    # Remove stopwords
    filtered_words = [token.text for token in doc if token.text not in stop_words and token.is_alpha]

    return filtered_words

# Example usage
if __name__ == "__main__":
    sample_text = input("Enter the text: ")
    processed_words = preprocess_text(sample_text)
    print("Processed words (without stopwords):")
    print(processed_words)