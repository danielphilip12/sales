import streamlit as st
import pandas as pd

# Profile Name Session

col1, col2 = st.columns(2, gap='small', vertical_alignment='center')

with col1:
    st.image('./assets/brain.png', width=250)
    
with col2:
    st.title("Clint Barton", anchor=False)
    st.write("Data Analyst that Always hits the mark")

# Skills Session