import streamlit as st
import pickle
import pandas as pd
import numpy as np
pipe= pickle.load(open('pipe.pkl','rb'))
teams=[
    'Austrailia',
    'Zimbabwe',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'West Indies',
    'Pakistan',
    'United Arab Emirates',
    'Sri Lanka',
    'Netherlands'
]
cities=[
'Harare', 'Napier', 'Mount Maunganui', 'Auckland', 'Southampton',
       'Taunton', 'Cardiff', 'Chester-le-Street', 'Kanpur', 'Nagpur',
       'Bangalore', 'Lauderhill', 'Dubai', 'Abu Dhabi', 'Wellington',
       'Hamilton', 'Bloemfontein', 'Potchefstroom', 'Barbados',
       'Trinidad', 'Colombo', 'Jamaica', 'Nelson', 'Manchester',
       'Bristol', 'Delhi', 'Rajkot', 'Thiruvananthapuram', 'Lahore',
       'Johannesburg', 'Centurion', 'Cuttack', 'Indore', 'Mumbai',
       'Dhaka', 'Sylhet', 'Karachi', 'East London', 'Cape Town',
       'St Kitts', 'Kolkata', 'Lucknow', 'Chennai', 'Gros Islet',
       'Basseterre'
]
st.title('Cricket Score Predictor')
col1,col2=st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select Bowling team', sorted(teams))

city = st.selectbox('Select city',sorted(cities))
col3 , col4, col5 = st.columns(3)

with col3:
    current_score=st.number_input("Current Score")
with col4:
    overs_done = st.number_input('overs done(works for over>5)')
with col5:
    wickets= st.number_input("wickets_out")

last_five= st.number_input('runs scored in last five overs')

if st.button('Predict Score'):
    balls_left=120 -(overs_done*6)
    wicket_left = 10-wickets
    crr=current_score/overs_done

    input_df=pd.DataFrame(
        {'batting_team': [batting_team],'bowling_team': [bowling_team],'city':city,'current_score':[current_score],
         'balls_left':[balls_left],'wickets_left':[wicket_left],'crr':[crr],'last_five':[last_five]}
    )
    st.table(input_df)
    result = pipe.predict(input_df)
    st.header("Predicted Score " + str(int(result[0])))