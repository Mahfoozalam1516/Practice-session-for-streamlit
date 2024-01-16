import time
import numpy as np
import pandas as pd
import streamlit as st

#page configurtaion
st.set_page_config(page_title = 'Spinner', page_icon = '🧊', layout = 'wide', initial_sidebar_state = 'auto')

#Spinner
with st.spinner('Wait for it !'):
    time.sleep(5)
    st.write('Thanks for being patient !')

#Progress Bar
with st.empty():
    for percent_completed in range(100):
        time.sleep(.1)
        st.progress(percent_completed + 1, text= 'Processing')
    st.success('Congratulations!')

#Special effects at the end
st.snow()
st.balloons()