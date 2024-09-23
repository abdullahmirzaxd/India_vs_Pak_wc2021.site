#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import plotly.express as px

# Custom CSS for colorful headings and background image
background_css = """
<style>
body {
    background-image: url("https://imageio.forbes.com/specials-images/imageserve/652973e24a6ce88b0a88b00d/CRICKET-WC-2021-T20-IND-PAK/0x0.jpg?format=jpg&crop=2950,1658,x162,y115,safe&width=1440");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
h1 {
    color: #FF4500;  /* OrangeRed color for the title */
    text-align: center;
    font-family: 'Arial', sans-serif;
    font-size: 50px;
}
h2 {
    color: #1E90FF;  /* DodgerBlue color for headers */
    text-align: center;
    font-family: 'Arial', sans-serif;
}
h3 {
    color: #32CD32;  /* LimeGreen color for subheaders */
    font-family: 'Arial', sans-serif;
    text-align: center;
}
</style>
"""

# Inject the custom CSS into the Streamlit app
st.markdown(background_css, unsafe_allow_html=True)

# Title and match header with styled headings
st.title("T20 World Cup 2021")
st.header("Match: Pakistan vs India")
st.subheader("Match Summary")
st.write("India: 151/7 (20 overs)")
st.write("Pakistan: 152/0 (17.5 overs)")
st.write("**Pakistan won by 10 wickets**")

# Hardcoded India Batting and Pakistan Bowling Data
india_batting_data = pd.DataFrame({
    "Player": ["KL Rahul", "Rohit Sharma", "Virat Kohli", "Rishabh Pant", "Suryakumar Yadav", "Hardik Pandya", "Bhuvneshwar Kumar", "Jasprit Bumrah"],
    "Runs": [3, 0, 57, 39, 11, 11, 0, 0],
    "Balls": [8, 1, 49, 30, 8, 8, 3, 1],
    "Fours": [0, 0, 5, 2, 1, 0, 0, 0],
    "Sixes": [0, 0, 1, 2, 0, 0, 0, 0],
})

pakistan_bowling_data = pd.DataFrame({
    "Bowler": ["Shaheen Afridi", "Haris Rauf", "Hasan Ali", "Shadab Khan", "Imad Wasim"],
    "Overs": [4, 4, 4, 4, 2],
    "Maidens": [0, 0, 0, 0, 0],
    "Runs Conceded": [31, 25, 44, 22, 10],
    "Wickets": [3, 0, 2, 1, 0],
    "Economy": [7.75, 6.25, 11.0, 5.5, 5.0]
})

# Hardcoded Pakistan Batting and India Bowling Data
pakistan_batting_data = pd.DataFrame({
    "Player": ["Mohammad Rizwan", "Babar Azam"],
    "Runs": [79, 68],
    "Balls": [55, 52],
    "Fours": [6, 6],
    "Sixes": [3, 2],
})

india_bowling_data = pd.DataFrame({
    "Bowler": ["Bhuvneshwar Kumar", "Mohammed Shami", "Jasprit Bumrah", "Ravindra Jadeja", "Varun Chakravarthy"],
    "Overs": [3, 3.5, 3, 4, 4],
    "Maidens": [0, 0, 0, 0, 0],
    "Runs Conceded": [25, 43, 22, 28, 33],
    "Wickets": [0, 0, 0, 0, 0],
    "Economy": [8.33, 11.21, 7.33, 7.0, 8.25]
})

# Display Batting and Bowling Scorecards
st.subheader("India Batting Scorecard")
st.dataframe(india_batting_data)

st.subheader("Pakistan Bowling Scorecard")
st.dataframe(pakistan_bowling_data)

st.subheader("Pakistan Batting Scorecard")
st.dataframe(pakistan_batting_data)

st.subheader("India Bowling Scorecard")
st.dataframe(india_bowling_data)

# Player performance bar chart (India Batting)
st.subheader("India Player Performance (Runs)")
fig = px.bar(india_batting_data, x="Player", y="Runs", title="India Player Runs", color="Runs", text="Runs")
st.plotly_chart(fig)

# Player performance bar chart (Pakistan Batting)
st.subheader("Pakistan Player Performance (Runs)")
fig2 = px.bar(pakistan_batting_data, x="Player", y="Runs", title="Pakistan Player Runs", color="Runs", text="Runs")
st.plotly_chart(fig2)

# Run rate over time (Hardcoded for India and Pakistan)
run_rate_data = pd.DataFrame({
    "Over": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    "India Runs": [5, 10, 15, 20, 30, 40, 45, 55, 60, 65, 75, 80, 90, 100, 110, 125, 130, 140, 145, 151],
    "Pakistan Runs": [10, 20, 25, 35, 40, 55, 65, 75, 85, 90, 100, 110, 115, 125, 135, 145, 150, 152, None, None]
})
fig3 = px.line(run_rate_data, x="Over", y=["India Runs", "Pakistan Runs"], title="Run Rate Progression (India vs Pakistan)")
st.plotly_chart(fig3)


# In[ ]:




