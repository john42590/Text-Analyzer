from collections import Counter
import string
from nltk. readability import FleschKincaidReadability

def clean_text(text):
  # Preprocess text by removing punctuation and converting to lowercase
  text = text.translate(str.maketrans('', '', string.punctuation))
  text = text.lower()
  return text

def analyze_text(text, min_word_count):
  # Split text into words and remove stop words (replace with actual stop word list)
  stop_words = ["the", "a", "is", "of", "and", ...]
  words = [word for word in clean_text(text).split() if word not in stop_words and len(word) >= min_word_count]
  
  # Calculate word frequency and other statistics
  word_counts = Counter(words)
  total_words = len(words)
  total_chars = len(clean_text(text))
  readability_score = FleschKincaidReadability(text).grade_levels()
  
  # Identify most frequent words
  most_frequent_words = word_counts.most_common(10)
  
  return {
    "word_count": total_words,
    "char_count": total_chars,
    "readability_score": readability_score,
    "most_frequent_words": most_frequent_words
  }

def main():
  # Get user input for text source (direct input or file)
  text_source = input("Enter text directly (d) or provide a file path (f): ").lower()
  
  if text_source == 'd':
    text = input("Enter your text here:\n")
  else:
    # Handle file reading (replace with error handling)
    with open(input("Enter file path: "), 'r') as f:
      text = f.read()
  
  # (Optional) Get user input for minimum word count
  min_word_count = int(input("Enter minimum word count for frequency (optional, default: 2): ") or 2)
  
  # Analyze text and display results
  analysis_results = analyze_text(text, min_word_count)
  print("Text Analysis Results:")
  print(f"Word Count: {analysis_results['word_count']}")
  print(f"Character Count: {analysis_results['char_count']}")
  print(f"Readability Score: {analysis_results['readability_score']}")
  print("\nMost Frequent Words:")
  for word, count in analysis_results["most_frequent_words"]:
    print(f"{word} ({count})")

if __name__ == "__main__":
  main()
