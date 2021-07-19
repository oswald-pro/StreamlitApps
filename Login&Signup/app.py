import streamlit as st
import HomePage

# DB Management
import sqlite3


conn = sqlite3.connect('system.db')
c = conn.cursor()

global email

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(email TEXT,password TEXT,country TEXT)')


def add_userdata(email, password, country):
    c.execute('INSERT INTO userstable(email,password,country) VALUES (?,?,?)', (email, password, country))
    conn.commit()


def login_user(email, password):

    c.execute('SELECT * FROM userstable WHERE email =? AND password = ?', (email, password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data


def main():
    st.title("Login App")

    menu = ["Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        st.subheader("Welcome Back!")

        email = st.sidebar.text_input("Email")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("login"):
            create_usertable()
            result = login_user(email, password)
            if result:
                st.success("Logged In with {}".format(email))
                HomePage.home()
        else:
            st.warning("Incorrect Username/Password")



    elif choice == "SignUp":
        st.subheader("Create New Account")

        new_email = st.text_input("Email")
        new_password = st.text_input("Password", type='password')
        new_country = st.text_input("Country")


        if st.button("Signup"):
            create_usertable()
            add_userdata(new_email, new_password, new_country)
            st.success("You have successfully created an account")
            st.info("Go to Login Menu to login")


if __name__ == '__main__':
    main()

