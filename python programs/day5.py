# -*- coding: utf-8 -*-
"""Day5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1m73o3Mw3Vc_OJp3hF2GqFvnUiQLZxi6Z
"""

from collections import Counter

def calculate_word_frequency(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)

    # Split the text into words
    words = cleaned_text.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    # Print the words and their counts
    for word, count in word_counts.items():
        print(f"{word}: {count}")

# Example usage
if __name__ == "__main__":
    sample_text = input("Enter the text: ")
    calculate_word_frequency(sample_text)