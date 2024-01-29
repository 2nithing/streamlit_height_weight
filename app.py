import streamlit as st
import pickle

with st.form("myform"):
    height = st.text_input(label="Enter Height in inches")
    submitted  = st.form_submit_button("Submit")
    print(type(height))
if submitted:
        model = pickle.load(open('./model.pkl','rb'))
        weight = model.predict([[int(height)]])
        st.write("weight value is ", round(weight[0],2)," pounds")