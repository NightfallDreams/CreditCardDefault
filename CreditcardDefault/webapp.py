# -*- coding: utf-8 -*-
"""


@author: NightfallDreams
"""

import pandas as pd
import streamlit as st
import pickle
import gzip

st.markdown(
    """
    <style>
    body {
        background-color: #e0f7fa; /* Light Blue */
        color: #000000; /* Text color black */
    }
    </style>
    """, unsafe_allow_html=True
)



with gzip.open("CreditCardModel.pkl.gz", 'rb') as f:
    model = pickle.load(f)

st.title("Predict Credit Card Default")
st.write("Enter the following details")
limit_bal=st.number_input('Enter your cards Limit',min_value=1000,max_value=1000000)
Sex=st.selectbox('Gender',options=['Male','Female'])
EDUCATION = st.selectbox('Education Level', options=['Graduate School', 'University', 'High School', 'Other', 'Unknown'])
MARRIAGE = st.selectbox('Marital Status', options=['Married', 'Single', 'Other'])
AGE = st.number_input('Age (in years)', min_value=18, max_value=100)

st.write("Repayment Status based on past 6 months :")
BILL_AMT1 = st.number_input('Bill Amount in September 2005', min_value=0)
PAY_AMT1 = st.number_input('Payment Amount in September 2005', min_value=0)
PAY_0 = st.selectbox('Repayment Status in September 2005', options=['Pay duly', 'Payment delay 1 month', 'Payment delay 2 months', 'Payment delay 3 months', 'Payment delay 4 months', 'Payment delay 5 months', 'Payment delay 6 months', 'Payment delay 7 months', 'Payment delay 8 months', 'Payment delay 9 months or more'])

BILL_AMT2 = st.number_input('Bill Amount in August 2005', min_value=0)
PAY_AMT2 = st.number_input('Payment Amount in August 2005', min_value=0)
PAY_2 = st.selectbox('Repayment Status in August 2005', options=['Pay duly', 'Payment delay 1 month', 'Payment delay 2 months', 'Payment delay 3 months', 'Payment delay 4 months', 'Payment delay 5 months', 'Payment delay 6 months', 'Payment delay 7 months', 'Payment delay 8 months', 'Payment delay 9 months or more'])

BILL_AMT3 = st.number_input('Bill Amount in July 2005', min_value=0)
PAY_AMT3 = st.number_input('Payment Amount in July 2005', min_value=0)
PAY_3 = st.selectbox('Repayment Status in July 2005', options=['Pay duly', 'Payment delay 1 month', 'Payment delay 2 months', 'Payment delay 3 months', 'Payment delay 4 months', 'Payment delay 5 months', 'Payment delay 6 months', 'Payment delay 7 months', 'Payment delay 8 months', 'Payment delay 9 months or more'])


BILL_AMT4 = st.number_input('Bill Amount in June 2005', min_value=0)
PAY_AMT4 = st.number_input('Payment Amount in June 2005', min_value=0)
PAY_4 = st.selectbox('Repayment Status in June 2005', options=['Pay duly', 'Payment delay 1 month', 'Payment delay 2 months', 'Payment delay 3 months', 'Payment delay 4 months', 'Payment delay 5 months', 'Payment delay 6 months', 'Payment delay 7 months', 'Payment delay 8 months', 'Payment delay 9 months or more'])


BILL_AMT5 = st.number_input('Bill Amount in May 2005', min_value=0)
PAY_AMT5 = st.number_input('Payment Amount in May 2005', min_value=0)
PAY_5 = st.selectbox('Repayment Status in May 2005', options=['Pay duly', 'Payment delay 1 month', 'Payment delay 2 months', 'Payment delay 3 months', 'Payment delay 4 months', 'Payment delay 5 months', 'Payment delay 6 months', 'Payment delay 7 months', 'Payment delay 8 months', 'Payment delay 9 months or more'])

BILL_AMT6 = st.number_input('Bill Amount in April 2005', min_value=0)
PAY_AMT6 = st.number_input('Payment Amount in April 2005', min_value=0)
PAY_6 = st.selectbox('Repayment Status in April 2005', options=['Pay duly', 'Payment delay 1 month', 'Payment delay 2 months', 'Payment delay 3 months', 'Payment delay 4 months', 'Payment delay 5 months', 'Payment delay 6 months', 'Payment delay 7 months', 'Payment delay 8 months', 'Payment delay 9 months or more'])


def convert_gender(Sex):
    return 1 if(Sex=='Male') else 2

def convert_education(EDUCATION):
    mapping = {'Graduate School': 1, 'University': 2, 'High School': 3, 'Other': 4, 'Unknown': 5}
    return mapping.get(EDUCATION,5)

def convert_marraige(MARRIAGE):
    mapping={'Married ':1,'Single':2,'Other':3}
    return mapping.get(MARRIAGE,3)

def convert_repayment_status(status):
    mapping = {
        'Pay duly': -1, 'Payment delay 1 month': 1, 'Payment delay 2 months': 2, 'Payment delay 3 months': 3,
        'Payment delay 4 months': 4, 'Payment delay 5 months': 5, 'Payment delay 6 months': 6, 
        'Payment delay 7 months': 7, 'Payment delay 8 months': 8, 'Payment delay 9 months or more': 9
    }
    return mapping.get(status, -1)

user_data={
    'LIMIT_BAL': limit_bal,
    'SEX': convert_gender(Sex),
    'EDUCATION': convert_education(EDUCATION),
    'MARRIAGE': convert_marraige(MARRIAGE),
    'AGE': AGE,
    'PAY_0': convert_repayment_status(PAY_0),
    'PAY_2': convert_repayment_status(PAY_2),
    'PAY_3': convert_repayment_status(PAY_3),
    'PAY_4': convert_repayment_status(PAY_4),
    'PAY_5': convert_repayment_status(PAY_5),
    'PAY_6': convert_repayment_status(PAY_6),
    'BILL_AMT1': BILL_AMT1,
    'BILL_AMT2': BILL_AMT2,
    'BILL_AMT3': BILL_AMT3,
    'BILL_AMT4': BILL_AMT4,
    'BILL_AMT5': BILL_AMT5,
    'BILL_AMT6': BILL_AMT6,
    'PAY_AMT1': PAY_AMT1,
    'PAY_AMT2': PAY_AMT2,
    'PAY_AMT3': PAY_AMT3,
    'PAY_AMT4': PAY_AMT4,
    'PAY_AMT5': PAY_AMT5,
    'PAY_AMT6': PAY_AMT6
    }
input_df=pd.DataFrame(user_data,index=[0])

if st.button('Predict'):
    st.write("Making prediction...")
    prediction = model.predict(input_df)
    prediction = int(prediction[0])
    st.write(f"Prediction: {prediction}")
    
    if prediction == 0:
        st.success("The Customer is likely to pay the next Installment")
        st.balloons()
    else:
        st.error("The Customer is not likely to pay the next Installment")
