# recommender.py

def generate_insights(current_metrics, historical_summary):
    # Analyze weak and strong areas
    insights = {
        "weak_topics": historical_summary.idxmin(),
        "strong_topics": historical_summary.idxmax(),
    }
    print("Insights Generated!")
    return insights

def create_recommendations(insights):
    # Generate actionable recommendations
    recommendations = [
        f"Focus on the topic: {insights['weak_topics']} to improve your score.",
        f"Continue excelling in: {insights['strong_topics']}."
    ]
    print("Recommendations Created!")
    return recommendations
