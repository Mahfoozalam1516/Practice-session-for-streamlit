import time
import numpy as np
import streamlit as st

#static
col1, col2, col3 = st.columns(3)
with col1:
    st.header('Nature')
    st.image('https://images.unsplash.com/photo-1433086966358-54859d0ed716?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', width = 200)
with col2:
    st.header('Cold')
    st.image("https://images.unsplash.com/photo-1519937010618-f8c8b7e135b7?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", width = 200)
with col3:
    st.header('Hot')
    st.image("https://plus.unsplash.com/premium_photo-1664803966458-c2ea9238991f?q=80&w=1136&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", width = 200)


#Dynamic
n= st.number_input('How many columns do you want in this section?', 1,10)
cols = st.columns(n)
for col in cols:
    with col:
        st.image("https://plus.unsplash.com/premium_photo-1664803966458-c2ea9238991f?q=80&w=1136&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")