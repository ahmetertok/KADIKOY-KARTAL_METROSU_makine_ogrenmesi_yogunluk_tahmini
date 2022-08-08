import streamlit as st
import numpy as np
import pandas as pd
import datetime
import pickle
import os, time

os.environ['TZ'] = 'Turkey'
time.tzset()

loaded_model = pickle.load(open('model.sav','rb'))


d = st.date_input('Lütfen metroya bineceğiniz tarihi seçin.')
dt = pd.to_datetime(d).weekday()


st.title('deneme')

