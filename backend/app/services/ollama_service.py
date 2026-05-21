import ollama

def predict_algorithm(analysis):

    prompt = f"""
    
    You are an AI Machine Learning expert.

    Based on this dataset information:

    Rows: {analysis['rows']}
    Columns: {analysis['columns']}
    Numeric Columns: {analysis['numeric_columns']}
    Categorical Columns: {analysis['categorical_columns']}
    Missing Values: {analysis['missing_values']}

    Predict the BEST machine learning algorithms
    for this dataset.

    Rules:
    - Return ONLY algorithm names
    - Give confidence percentage
    - Sort in descending order
    - Keep answer short
    - No long explanations
    - Format exactly like this:

    1. Random Forest - 92%
    2. XGBoost - 88%
    3. Logistic Regression - 75%
    4. SVM - 70%

    """

    response = ollama.chat(

        model="tinyllama",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]