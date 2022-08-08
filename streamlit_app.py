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

def predict(dt,th):
  X_predict = pd.DataFrame()
  dict = {'fusedhour':th,  'weekDay': dt, 'AVERAGE_SPEED':50, 'temp':24.0, 'rain':0, 'rain,snow':0, 'snow':0}
  X_predict= X_predict.append(dict, ignore_index = True)
  prediction = loaded_model.predict(X_predict)
  return int(prediction)

output = predict(dt,th)
st.title("Metroda vardığınızda "+ str(output) +" kişi olacak.")

