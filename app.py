import streamlit as st
import pickle

st.header("Predict weight from height")
st.write("Demo of linear regression machine learning model")
with st.form("myform"):
    height = st.number_input(label="Enter Height in inches",min_value=32.0,max_value=120.0,value=50.00,step=1.0)
    submitted  = st.form_submit_button("Submit")
    print(type(height))
if submitted:
        model = pickle.load(open('./model.pkl','rb'))
        weight = model.predict([[height]])
        st.write(f"Expected weight value is **{round(weight[0],2)}** pounds")
