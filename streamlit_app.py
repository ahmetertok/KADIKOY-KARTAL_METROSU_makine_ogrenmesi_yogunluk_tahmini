import streamlit as st
import numpy as np
import pandas as pd
import datetime
import pickle
import os, time

os.environ['TZ'] = 'Turkey'
time.tzset()

loaded_model = pickle.load(open('model.sav','rb'))

st.title('M4 Metrosu yoğunluğu')

d = st.date_input('Lütfen metroya bineceğiniz tarihi seçin.')
dt = pd.to_datetime(d).weekday()
st.write('Seçilen tarih: ',dt)

t =  st.time_input('Lütfen metroya bineceğiniz zamanı seçin')
th = t.hour
#tm = t.minute

#tt = round(th + (tm / 60), 1)
st.write('Seçilen saat: ', th)



