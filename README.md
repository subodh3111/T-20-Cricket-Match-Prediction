# Cricket Score Predictor

## Overview
The Cricket Score Predictor is a web application that predicts the final score of a cricket match based on current game statistics. The application is built using **Streamlit**, and it utilizes a pre-trained machine learning model for score prediction. 

## Features
- Select batting and bowling teams from a predefined list.
- Choose the match city from available locations.
- Input current score, overs completed, wickets lost, and last five overs' runs.
- Predict the final score using a trained model.
- Display the predicted score in an interactive UI.

## Tech Stack
- **Python**: Main programming language.
- **Streamlit**: For web-based UI.
- **Pandas & NumPy**: For data manipulation.
- **Pickle**: For loading the trained model.

## Installation

### Prerequisites
Ensure you have **Python 3.7+** installed on your system.

### Steps
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd cricket-score-predictor
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   streamlit run app.py
   ```

## Usage
1. Open the application in your web browser (default: `http://localhost:8501`).
2. Select the **Batting Team** and **Bowling Team** from the dropdown lists.
3. Choose the **City** where the match is being played.
4. Enter the **Current Score**, **Overs Completed**, and **Wickets Lost**.
5. Input the **Runs scored in the last five overs**.
6. Click on the **Predict Score** button to get the predicted final score.

## Model Details
The prediction model is stored as `pipe.pkl` and is loaded using the `pickle` library. The model considers features like:
- Batting and Bowling Teams.
- Match Venue (City).
- Current Score and Overs Completed.
- Wickets Lost.
- Runs scored in the last five overs.

## File Structure
```
.
├── app.py                 # Main Streamlit application
├── pipe.pkl               # Trained machine learning model
├── requirements.txt       # Required dependencies
├── README.md              # Project Documentation
└── data_extraction_t_20.ipynb / feature_extraction.ipynb  # Notebooks for data processing
```

## Future Enhancements
- Improve model accuracy with more training data.
- Add more match conditions like pitch report and weather.
- Deploy the application online for public access.

## License
This project is open-source and available under the MIT License.

