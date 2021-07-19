import streamlit as st
import LoginSignup as ls
import pandas as pd

def home():
    st.subheader("Home")
    task = st.selectbox("Task", ["Videos", "Profile"])
    if task == "Videos":
        st.subheader("Watch Youtube Videos")
    elif task == "Profile":
        st.subheader("Your Profile")
        user_result = ls.view_all_users()
        clean_db = pd.DataFrame(user_result, columns=["Email", "Password", "Country"])
        st.dataframe(clean_db)
