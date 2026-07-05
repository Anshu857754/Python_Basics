import streamlit as st
import pandas as pd

st.title("streamlit text input")
name = st.text_input("Enter your name ")

age=st.slider("Select your age:",0,100,20)

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}.")

st.write(f"Your age is {age}.")
if name:
    st.write(f"HELLO,  {name}")

data ={
"Name": ["John", "Jane", "Jake", "Jill"],
"Age": [28, 24, 35, 40],
"City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sample_data.csv")
st.write(df)

# create an upload button

upload_file =st.file_uploader("Choose a CSV file ",type="csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)
