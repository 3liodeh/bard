import streamlit as st
from bardapi import Bard
import os

os.environ['_BARD_API_KEY']="XAhr4hmTK4v2pnZB4rzBvSjAeDSMOF5DtqO42EfHGYOQL2i66RcFQJD-eh9SknrVElY-iw."

                      
def appearance():
    dark_theme = """
        <style>
        .stApp {
        background-color: #1F2227;
        background-image: linear-gradient(to bottom right, #33FFE9, #2E8B57);
        background-size: cover;
        
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        text-align: center;}
        
                                          
       .stTextInput label {
        display: flex;
        justify-content: center;
        border: none;
        box-shadow: none;
        }
        
        [data-testid="stHeader"]{
            background-color: #000000;
            }
        </style>
        """
    st.markdown(dark_theme, unsafe_allow_html=True)


appearance()

st.title('Ask Bard')

# Create a box container
with st.container():
    
    text = st.text_input('Enter your text')
    
    click=st.button("ASK")
    if click:
        st.write('The asnwer :',Bard().get_answer(text)['content'])


