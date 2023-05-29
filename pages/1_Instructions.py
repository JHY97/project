import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center; color: orange;'>Instructions</h1>", unsafe_allow_html=True)
st.markdown("")
st.markdown("")
tab1, tab2, tab3 = st.tabs(["Step1", "Step2", "Step3"])

with tab1:
  st.markdown("<h3 style='text-align: left; color: orange;'>Step1</h3>", unsafe_allow_html=True)
  st.markdown("")
  st.markdown("1️⃣Please sign up first to use the Manless websit", unsafe_allow_html=True)
  st.markdown("2️⃣You can sign up through 'Home' tab.", unsafe_allow_html=True)
  st.markdown("")
  image = Image.open('instructions_image/Step1.png')
  st.image(image)

with tab2:
  st.markdown("<h3 style='text-align: left; color: orange;'>Step2</h3>", unsafe_allow_html=True)

with tab3:
  st.markdown("<h3 style='text-align: left; color: orange;'>Step3</h3>", unsafe_allow_html=True)
