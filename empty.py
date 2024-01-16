import time
import numpy as np
import pandas as pd
import streamlit as st

cases = []
for _ in range(100):
    cases.append(np.random.randint(1, 7))

data = []
for i in range(1, 7):
    data.append(cases.count(i))

st.header('Frequency of getting a face on dice')

st.bar_chart({'data': data})

with st.expander('See Explanation'):
    st.write('''
    This is the explanation of the dice experiment.
    ''')
    st.image("https://images.unsplash.com/photo-1570303345338-e1f0eddf4946?q=80&w=1071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")


    with st.empty():
        st.write('You need to wait for 10 seconds')
        for seconds in range(11):
            st.write('⏲️'+ str(seconds) + ' Remained seconds')
            time.sleep(1)
        st.write('10 seconds completed')