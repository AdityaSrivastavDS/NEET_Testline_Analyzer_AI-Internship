# analyzer.py

import pandas as pd

# Analyze current quiz performance
def analyze_current_quiz(data):
    # Extract key metrics
    metrics = {
        "score": data.get("score"),
        "accuracy": data.get("accuracy"),
        "correct_answers": data.get("correct_answers"),
        "incorrect_answers": data.get("incorrect_answers"),
        "response_map": data.get("response_map", {}),
    }
    print("Current Quiz Analysis Complete!")
    return metrics

# Analyze historical quiz performance
def analyze_historical_quiz(data):
    # Create a DataFrame from historical question data
    questions = data.get("quiz", {}).get("questions", [])
    df = pd.DataFrame(questions)

    # Analyze topics and difficulty
    topic_summary = df["topic"].value_counts()
    print("Historical Quiz Analysis Complete!")
    return topic_summary
