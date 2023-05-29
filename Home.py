import streamlit as st
import streamlit.components.v1 as components
import pandas as pd


# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
  return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
  if make_hashes(password) == hashed_text:
    return hashed_text
  return False
  
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()

# DB  Functions
def create_usertable():
  c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
  c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
  conn.commit()

def login_user(username,password):
  c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
  data = c.fetchall()
  return data

def view_all_users():
  c.execute('SELECT * FROM userstable')
  data = c.fetchall()
  return data

def main():
  """Manless"""
  st.markdown("<h1 style='text-align: center;'>Welcome to MANLESS </h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='text-align: center; color: orange;'>Register & Login Page</h3>", unsafe_allow_html=True)
  st.write("")
  st.write("")

  tab1, tab2= st.tabs(["Register", "Login"])
  with tab1:
    st.markdown("<h5 style='text-align: left; color: orange;'>Create new account </h5>", unsafe_allow_html=True)
    new_user = st.text_input("New Username")
    new_password = st.text_input("New Password",type='password')

    if st.button("Signup"):
      create_usertable()
      add_userdata(new_user,make_hashes(new_password))
      st.success("You have successfully created a valid Account")
      st.info("Go to Login Menu to login")


  with tab2:
    st.markdown("<h5 style='text-align: left; color: orange;'>Login Section </h5>", unsafe_allow_html=True)
    username = st.text_input("User Name")
    password = st.text_input("Password",type='password')
		
    if st.checkbox("Login"):
      create_usertable()
      hashed_pswd = make_hashes(password)

      result = login_user(username,check_hashes(password,hashed_pswd))
	
      if result:
        st.success("Welcome {}! You can control the door now. Please click the button below.".format(username))
        st.button("✨ **Open the door** ✨",use_container_width=True)   
 
      else:
        st.warning("Incorrect Username/Password")


if __name__ == '__main__':
  main()