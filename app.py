import streamlit as st
import pandas as pd
import numpy as np
import pickle


@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No Failure ":0,"Power Failure":1,"Tool Wear Failure ":2,"Heat Dissipation Failure":4}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value
       
app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction'])
if app_mode=='Home':
    st.title('Machine Failure Classification:')
    st.subheader("This Application is a part of my MLOps Courses ,The application recives the User Input and Thanks to the saved model it can tel you does your Machine does have a failure or not and classify it into one of the 5 5 classes :")
    st.image('pdm.png') 
    st.write('App realised by : Soulaima Ben youssef') 
    
   
elif app_mode =='Prediction':
    st.image('images/pdm.png')
    st.subheader('Dear User ,U can put You input data Values ')
    st.sidebar.header("Informations about the Machine Status :")
    Type_dict = {"H":0,"M":1,"L":2}
    Type=st.sidebar.radio('Type',tuple(Type_dict.keys()))
    Airtemperture=st.sidebar.slider('Air temperture [°C] ',0,39)
    Processtemperature=st.sidebar.slider('Process temperature [°C]',20,45) #max of it is 45 and min is 33
    Torque=st.sidebar.slider('Torque [Nm]',3.0,79.0)
    Toolwear=st.sidebar.slider('Tool wear',0,255)
    Temperaturedifference=st.sidebar.slider('Temperature difference [°C]',0,20)
    Rotationalspeed=st.sidebar.slider('Rotational speed [rpm]',1000,3000)

    feature_list=[Airtemperture,Processtemperature,Rotationalspeed,Torque,Toolwear,Temperaturedifference,get_value(Type,Type_dict)]

    single_sample = np.array(feature_list).reshape(1,-1)

    if st.button("Predict"): 
        loaded_model = pickle.load(open('MybestModel','rb'))
        prediction = loaded_model.predict(single_sample)
        if prediction[0] == 0 :
            st.success(
    'According to our Calculations, There is no failure in your machine '
    )   
            st.image('images/Nofailure.jpg')
        elif prediction[0] == 1 :
            
            st.error(
    'According to our Calculations, Your failure type is Power Failure'
    )
            st.image('images/Power Failure.jpg')
            
        elif prediction[0]==2 :
            st.error(
    'According to our Calculations, Your failure type is Tool Wear Failure'
    )    
        elif prediction[0]==3 :
            st.error(
    'According to our Calculations, Your failure type is Overstrain Failure'
    )
        elif prediction[0]==4 :
            st.error(
    'According to our Calculations, Your failure type is Heat Dissipation Failure'
    )
        st.image('images\Heat Dissipation.jpg')          




