# =================================================================
# PROJECT: NLP Sentiment Analysis Engine
# DESCRIPTION: Analyzing textual data (Reviews/Tweets) to detect mood.
# DELIVERABLE: Data Preprocessing, Sentiment Model, and Insights.
# =================================================================

import re

class SentimentAnalyzer:
    def __init__(self):
        # Basic Lexicon for Sentiment Scoring
        self.positive_words = {'good', 'great', 'awesome', 'excellent', 'happy', 'love', 'best'}
        self.negative_words = {'bad', 'worst', 'hate', 'poor', 'terrible', 'sad', 'awful'}
        print("🤖 NLP Sentiment Engine Initialized...")

    def preprocess_text(self, text):
        """Cleaning text: Lowercasing and removing special characters."""
        text = text.lower()
        text = re.sub(r'[^a-z\s]', '', text)
        return text

    def analyze_sentiment(self, review):
        """Calculating sentiment score based on word matching."""
        clean_review = self.preprocess_text(review)
        words = clean_review.split()
        
        score = 0
        for word in words:
            if word in self.positive_words:
                score += 1
            elif word in self.negative_words:
                score -= 1
        
        if score > 0:
            return "🟢 POSITIVE"
        elif score < 0:
            return "🔴 NEGATIVE"
        else:
            return "⚪ NEUTRAL"

# --- MAIN EXECUTION (Simulation with Real Insights) ---
if __name__ == "__main__":
    analyzer = SentimentAnalyzer()

    # Sample Dataset: Customer Reviews
    reviews = [
        "The new update is awesome and I love the speed!",
        "This is the worst experience ever, very bad service.",
        "The product is okay, not the best but works.",
        "Excellent build quality, I am very happy with it.",
        "Terrible battery life, I hate it."
    ]

    print("\n--- 📝 PROCESSING CUSTOMER FEEDBACK ---")
    results = {"POSITIVE": 0, "NEGATIVE": 0, "NEUTRAL": 0}

    for r in reviews:
        sentiment = analyzer.analyze_sentiment(r)
        results[sentiment.split()[-1]] += 1
        print(f"💬 Review: {r[:40]}... -> {sentiment}")

    # --- INSIGHTS GENERATION ---
    print("\n" + "="*45)
    print("📊 SENTIMENT ANALYSIS INSIGHTS")
    print("="*45)
    total = len(reviews)
    for mood, count in results
