# **NEET Testline Analyzer**

A Python-based solution to analyze quiz performance and provide personalized recommendations for students preparing for NEET.

---

## **Features**
- Fetches quiz data (current and historical) from provided API links.
- Analyzes performance across topics and questions.
- Identifies weak and strong areas for each student.
- Generates actionable recommendations to improve preparation.

---

## **Project Structure**

```plaintext
NEET_Testline_Analyzer/
│
├── main.py                        # Main script to execute the project
├── config.py                      # Configuration file with constants
├── data_fetcher.py                # Script to fetch and process data
├── analyzer.py                    # Script to analyze quiz performance
├── recommender.py                 # Script to generate recommendations
├── requirements.txt               # Required Python libraries
└── README.md                      # Project documentation

```


## **Setup Instructions**

Follow these steps to set up and run the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AdityaSrivastavDS/NEET_Testline_Analyzer_AI-Internship
   cd NEET_Testline_Analyzer_AI-Internship
   ```

2. Install Dependencies: Use the following command to install required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Project: Execute the main script to analyze quiz performance and generate recommendations:
    ```bash
    python main.py
    ```

## Approach
1. **Data Fetching:**

- Quiz data is fetched from two APIs:
- Current quiz performance data.
- Historical quiz data.
- The data_fetcher.py module handles the API requests and parses JSON responses.

2. **Data Analysis:**

- The analyzer.py module processes the fetched data to:
- Analyze performance in current and historical quizzes.
- Identify weak and strong topics based on response accuracy and question difficulty.

3. **Recommendation Generation:**

- The recommender.py module generates insights and actionable advice:
- Highlights weak areas to focus on.
- Suggests topics where the student excels.


## Dependencies
The following Python libraries are required:

- requests
- pandas


## License
This project is licensed under the [MIT License](LICENSE).


