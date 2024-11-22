import streamlit as st
import joblib
import numpy as np

st.title("Salary Prediction App")
st.divider()

st.write("With this app, You can predict the annual salary on the basis of job rates and years")

years = st.number_input("Enter the years at company",value=1, step=1,min_value=0)
job_rate = st.number_input("Enter the Job Rate",value = 3.5,step = 0.5,min_value=0.0)

X = (years,job_rate)

model = joblib.load('linearmodel.pkl')

st.divider()

predict = st.button("Press the button for salary prediction")

st.divider()

if predict:
    st.balloons()

    X1 = np.array([X])
    prediction = model.predict(X1)[0]
    
    st.write("Salary prediction is: {:,.2f}".format(float(prediction)))
else:
    'Please press the button for app to make the prediction'

