import streamlit as st
import pandas as pd 
import numpy as np

st.title("Hello streamlit")

# display simple text
st.write("This is a simple text")

# create a simple data frame 

df = pd.DataFrame({
    'First_Column': [1,2,3,4],
    'Second_Column':[10,20,30,40]
})

# display the dataframe
st.write("Here is the DataFrame.")
st.write(df)


# create a line chart
# chart data
chart_data = pd.DataFrame(
    np.random.rand(20,3),columns=['a','b','c']

)
st.line_chart(chart_data)