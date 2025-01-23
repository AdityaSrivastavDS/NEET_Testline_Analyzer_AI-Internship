# main.py

from config import CURRENT_QUIZ_DATA_URL, HISTORICAL_QUIZ_DATA_URL
from data_fetcher import fetch_data
from analyzer import analyze_current_quiz, analyze_historical_quiz
from recommender import generate_insights, create_recommendations

def main():
    # Step 1: Fetch data
    print("Fetching data...")
    current_quiz_data = fetch_data(CURRENT_QUIZ_DATA_URL)
    historical_quiz_data = fetch_data(HISTORICAL_QUIZ_DATA_URL)

    if not current_quiz_data or not historical_quiz_data:
        print("Data fetch failed. Exiting...")
        return

    # Step 2: Analyze data
    print("Analyzing data...")
    current_metrics = analyze_current_quiz(current_quiz_data)
    historical_summary = analyze_historical_quiz(historical_quiz_data)

    # Step 3: Generate insights
    print("Generating insights...")
    insights = generate_insights(current_metrics, historical_summary)

    # Step 4: Create recommendations
    print("Creating recommendations...")
    recommendations = create_recommendations(insights)

    # Step 5: Display recommendations
    print("\nPersonalized Recommendations:")
    for rec in recommendations:
        print(f"- {rec}")

if __name__ == "__main__":
    main()
