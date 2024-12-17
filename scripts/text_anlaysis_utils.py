from nltk.tokenize import word_tokenize
import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

# Download stopwords and tokenizer resources once
nltk.download('stopwords')
nltk.download('punkt') 
stop_words = set(stopwords.words('english'))
nltk.download('vader_lexicon')

# Initialize the Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    
    # Lowercase and remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    
    # Tokenize the text
    tokens = word_tokenize(text, language='english')  # Ensure language is set explicitly
    
    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]
    
    return ' '.join(tokens)


def get_sentiment(text):
    scores = sia.polarity_scores(text)
    if scores['compound'] > 0.05:
        return 'positive'
    elif scores['compound'] < -0.05:
        return 'negative'
    else:
        return 'neutral'