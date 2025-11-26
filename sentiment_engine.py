import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


sia = SentimentIntensityAnalyzer()

NEGATIVE_KEYWORDS = [
    "dont like", "not good", "bad", "worst", "hate",
    "angry", "disappointed", "terrible", "poor", "upset", "frustrated",
    "useless", "not satisfied", "not happy"
]

def is_custom_negative(text):
    """Checks if the input text contains any custom negative keywords."""
    text = text.lower()
    for word in NEGATIVE_KEYWORDS:
        if word in text:
            return True
    return False

def get_sentiment_label(text):
    """
    (Tier 2) Determines the sentiment label (Positive, Negative, Neutral) 
    based on VADER compound score, with custom keyword override.
    """
    if is_custom_negative(text):
        return "Negative"

    score = sia.polarity_scores(text)
    compound_score = score['compound']
    
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def analyze_overall_sentiment(user_messages):
    """(Tier 1) Calculates the overall sentiment for the entire conversation."""
    combined_text = " ".join(user_messages)
    if not combined_text:
        return "Neutral - No input"
        
    score = sia.polarity_scores(combined_text)
    compound_score = score['compound']

    if compound_score >= 0.05:
        return "Positive - general satisfaction "
    elif compound_score <= -0.05:
        return "Negative - general dissatisfaction "
    else:
        return "Neutral - mixed or indifferent feedback "

def summarize_sentiment_trend(sentiment_history):
    """(Tier 2 Enhancement) Summarizes the shift in mood across the conversation."""
    if not sentiment_history:
        return "Trend: No data available."

    pos_count = sentiment_history.count("Positive")
    neg_count = sentiment_history.count("Negative")
    total = len(sentiment_history)
    
    if total < 3:
        return "Trend: Too short to determine a strong trend."
        
    if neg_count > pos_count * 2:
        return "Trend: Significant negative sentiment detected."
    elif pos_count > neg_count * 2:
        return "Trend: Predominantly positive mood detected."
    else:
        return "Trend: Sentiment remained mixed or balanced."