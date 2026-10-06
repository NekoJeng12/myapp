import streamlit as st

st.title("My Streamlit App")
name = st.text_input("Enter your name:")
b =st.button("CLICK ME")
if b and name:
    st.write(f"Hello, {name}!")