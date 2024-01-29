import streamlit as st
import pickle

with st.form("myform"):
    height = st.number_input(label="Enter Height in inches",min_value=32.0,max_value=120.0,value=50.00)
    submitted  = st.form_submit_button("Submit")
    print(type(height))
if submitted:
        model = pickle.load(open('./model.pkl','rb'))
        weight = model.predict([[height]])
        st.write("weight value is ", round(weight[0],2)," pounds")