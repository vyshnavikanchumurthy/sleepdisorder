import numpy as np
import streamlit as st 
import pickle 

import warnings
warnings.filterwarnings("ignore")

# loading the saved model
loaded_model = pickle.load(open('trained_adb_model.sav', 'rb'))

def sleep_disorder_prediction(input_data):
    input_data_as_np_array = np.asarray(input_data) 

    input_data_reshaped = input_data_as_np_array.reshape(1,-1) 

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    pred = loaded_model.predict_proba(input_data_reshaped)
    risk = pred[:,1]
    risk_percent = round(risk[0]*100, 2)
    
    if (prediction[0] == 0):
        return 'the person is not at a risk of sleep disorder'
    else:
        return 'the person is at a risk of sleep disorder'
    
def percentage_of_risk(input_data):
    input_data_as_np_array = np.asarray(input_data) 

    input_data_reshaped = input_data_as_np_array.reshape(1,-1) 

    pred = loaded_model.predict_proba(input_data_reshaped)
    risk = pred[:,1]
    risk_percent = round(risk[0]*100, 2)
    
    print(risk_percent)
    
    return str(risk_percent)

#ui
Gender=0
Occupation=0
BMI=0
gender=st.selectbox('gender',['male','female'])
age=st.text_input('age')
occupation=st.selectbox('occupation',['other','Doctor','teacher','Nurse','Engineer','Accountant','Lawyer','Salesperson'])
sd=st.text_input('sd')
qs=st.text_input('qs')
pal=st.text_input('pal')
sl=st.text_input('sl')
bmi=st.selectbox('bmi',['overweight','normal','obese'])
hr=st.text_input('hr')
ds=st.text_input('ds')
bpupper=st.text_input('bp upper')
bplower=st.text_input('bp lower')

if (gender=='Male'):
    Gender = 1
elif (gender=='Female'):
    Gender = 0
        
if (occupation=='Accountant'):
    Occupation = 0
elif (occupation=='Doctor'):
    Occupation = 1
elif (occupation=='Engineer'):
    Occupation = 2
elif (occupation=='Lawyer'):
    Occupation = 3
elif (occupation=='Nurse'):
    Occupation = 4
elif (occupation=='Other'):
    Occupation = 5
elif (occupation=='Salesperson'):
    Occupation = 6
elif (occupation=='Teacher'):
    Occupation = 7   
        
if (bmi=='Overweight'):
    BMI = 2
elif (bmi=='Normal'):
    BMI = 0
elif (bmi=='Obese'):
    BMI = 1

input_features=[Gender,age,Occupation,sd,qs,pal,sl,BMI,hr,ds,bpupper,bplower]

diagnosis=''
percent_of_risk=''

if st.button('risk prediction'):
    diagnosis=sleep_disorder_prediction(input_features)
st.write(diagnosis)    


if st.button('risk percentage'):
    percent_of_risk=percentage_of_risk(input_features)
st.write(percent_of_risk)    


