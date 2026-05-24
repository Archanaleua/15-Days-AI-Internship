import nltk
from textblob import TextBlob

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

print("=" * 50)
print("       NLP BASICS - DAY 12")
print("=" * 50)

# Sample text
text = "Artificial Intelligence is amazing! It is changing the world. AI helps doctors, students and engineers."

print("\n📝 Original Text:")
print(text)

# 1. Sentence Tokenization
sentences = sent_tokenize(text)
print("\n📌 Sentence Tokenization:")
for i, sent in enumerate(sentences):
    print(f"  Sentence {i+1}: {sent}")

# 2. Word Tokenization
words = word_tokenize(text)
print("\n📌 Word Tokenization:")
print(words)

# 3. Remove Stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [w for w in words if w.lower() not in stop_words]
print("\n📌 After Removing Stopwords:")
print(filtered_words)

# 4. Sentiment Analysis
print("\n📌 Sentiment Analysis:")
sentences_list = [
    "I love Artificial Intelligence!",
    "This is terrible and boring.",
    "Python is okay I guess.",
    "AI is the best thing ever!"
]

for sentence in sentences_list:
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        result = "😊 Positive"
    elif sentiment < 0:
        result = "😞 Negative"
    else:
        result = "😐 Neutral"
    print(f"  '{sentence}' → {result} (score: {sentiment:.2f})")

print("\n✅ NLP Basics Complete!")
print("=" * 50)