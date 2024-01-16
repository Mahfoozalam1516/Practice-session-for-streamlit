import time
import numpy as np
import pandas as pd
import streamlit as st

#static
tab1, tab2, tab3 = st.tabs(['cats', 'dogs', 'owl'])
tab1.image('https://images.unsplash.com/photo-1703982924533-22c9f7f34624?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', width= 200)
tab2.image('https://images.unsplash.com/photo-1705222594042-90f8f7280750?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', width= 200)
tab3.image('https://images.unsplash.com/photo-1705226384099-8ec9b1a16788?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', width= 200)

#dynamic

imgs = pd.read_csv("C:\\Users\\MAHFOOZ ALAM\\Desktop\\DATASET FOR USAGE\\wikiart_scraped.csv")['Link']

tabs = st.tabs(["ID"]*30)
for tab in tabs:
    img = imgs[np.random.randint(1, 1000)]
    tab.image(img, width= 400)