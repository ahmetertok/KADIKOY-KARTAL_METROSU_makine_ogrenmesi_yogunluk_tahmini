import streamlit as st
import numpy as np
import pandas as pd
import datetime
import pickle
import os, time
import requests
import json


x = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=40.988925&lon=29.038308&appid=53609485ee8d32929ce452d8cdb1f82e&units=metric')
y = json.loads(x.text)

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
  dict = {'fusedhour':th,  'weekDay': dt, 'AVERAGE_SPEED':50, 'temp':float(y["main"]['temp']), 'rain':0, 'rain,snow':0, 'snow':0}
  X_predict= X_predict.append(dict, ignore_index = True)
  prediction = loaded_model.predict(X_predict)
  return int((int(prediction)*100)/22742)

output = predict(dt,th)
st.title("Metro vardığınızda %"+ str(output) +" yoğun olacak.")
#a = json.loads(str(y["weather"])[1:len(str(y["weather"]))-1])
st.title(str(y["weather"][0]['id']))

#https://api.openweathermap.org/data/2.5/weather?lat={40.988925}&lon={29.038308}&appid={53609485ee8d32929ce452d8cdb1f82e}