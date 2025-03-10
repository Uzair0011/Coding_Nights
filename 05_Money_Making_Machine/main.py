import streamlit as st
import random    # to generate random number
import time  # current time
import requests  # very important calls API

st.title("Money Macking Machine")


def generate_money():
    # random is module & randint is function
    return random.randint(1, 1000)


st.subheader("Instant Cash Generator")
if st.button("Generator Money"):
    st.write("Counting your Money...")
    time.sleep(2)
    amount = generate_money()
    st.success(f"You made ${amount}!")


# FIRST GO & RUN 04_API RUN 
# please Follow These Three Steps
# cd 04_API
# .venv\Scripts\activate
# fastapi dev main.py

# fetch side hustle from previous project 04_API
def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            # if this line so show document format
            # return hustles
            # if this line so only show key on clean format
            return hustles["side_hustle"]
            # if internet is off else message show
        else:
            return ["Freelancing"]
    except:
        return ("Something went wrong!")


st.subheader("Side Hustle Ideas")
if st.button("Generate Hustle"):
    idea = fetch_side_hustle()
    st.success(idea)



# fetch money qoute from previous project 04_API
def fetch_money_qoute():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quote"]
        else:
            return ("Money is the root of all evil!")
        # if API se error Ata h
    except:
        return ("Something went wrong!")


st.subheader("Money-Making Motivation")
if st.button("Get Inspired"):
    quote = fetch_money_qoute()
    st.success(quote)
