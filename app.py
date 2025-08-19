import streamlit as st

st.set_page_config(page_title="Hello Streamlit", page_icon="👋")

st.title("Hello World 👋")
st.write("This is my first time using Streamlit hosted on GitHub!")

name = st.text_input("Enter your name:")
if st.button("Say Hello"):
    st.success(f"Hello {name or 'World'}! 🎉")
