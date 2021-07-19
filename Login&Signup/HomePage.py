import streamlit as st
import app as ap
import pandas as pd


def home():
    st.subheader("Home Page")
    task = st.sidebar.selectbox("Select", ["Videos", "Profile"])
    if task == "Videos":
        st.subheader("Watch Youtube Videos")
    elif task == "Profile":
        st.subheader("Your Profile")
        user_result = ap.view_all_users()
        clean_db = pd.DataFrame(user_result, columns=["Email", "Password", "Country"])
        st.dataframe(clean_db)
