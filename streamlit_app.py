import streamlit as st
import numpy as np
import pandas as pd
import datetime
import pickle
import os, time
import requests
import json

os.environ['TZ'] = 'Turkey'
time.tzset()

loaded_model = pickle.load(open('model.sav','rb'))

st.title('M4 Metrosu yoğunluğu')

d = st.date_input('Lütfen metroya bineceğiniz tarihi seçin.')
dt = pd.to_datetime(d).weekday()
#st.write('Seçilen tarih: ',dt)

t =  st.time_input('Lütfen metroya bineceğiniz zamanı seçin')
th = t.hour
#tm = t.minute

#tt = round(th + (tm / 60), 1)
#st.write('Seçilen saat: ', th)

def predict(dt,th):
  x = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=40.988925&lon=29.038308&appid=53609485ee8d32929ce452d8cdb1f82e&units=metric')
  x2 = requests.get('https://api.ibb.gov.tr/tkmservices/api/TrafficData/v1/TrafficIndexHistory/1/H')
  y2 = json.loads(x2.text)
  y = json.loads(x.text)
  X_predict = pd.DataFrame()
  dict = {'fusedhour':th,  'weekDay': dt, 'trafficIndex':y2[0]['TrafficIndex'], 'temp':float(y["main"]['temp']), 'rain':0, 'rain,snow':0, 'snow':0}
  if str(y["weather"][0]['id'])[0:1]=='6':
    dict['snow']=1
  if str(y["weather"][0]['id'])[0:1]=='5':
    dict['rain']=1
  X_predict= X_predict.append(dict, ignore_index = True)
  prediction = loaded_model.predict(X_predict)
  return int(prediction)

output = predict(dt,th)
st.title("Metro vardığınızda %"+ str(int((int(output)*100)/15000)) +" yoğun olacak.")
st.write("Seçilen tarihte ~"+str(output)+" yolcu var.")
#st.write(y2[0]['TrafficIndex'])
#a = json.loads(str(y["weather"])[1:len(str(y["weather"]))-1])
#st.title(str(y["weather"][0]['id'])[0:1])

#https://api.openweathermap.org/data/2.5/weather?lat={40.988925}&lon={29.038308}&appid={53609485ee8d32929ce452d8cdb1f82e}
