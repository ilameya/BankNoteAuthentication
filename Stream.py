import pandas as pd
import numpy as np
import pickle
#from flasgger import Swagger
import streamlit as st

#app = Flask(__name__)
#Swagger(app)

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

#@app.route('/')
def Welcome():
    return "Welcome All"

#@app.route('/predict', methods = ["GET"])
def predict_note_authentication(variance, skewness, curtosis, entropy):
    """Let's Authenticate the Bank Note
    This is using docstrings for specification.
    ---
    parameters:
     - name: variance
       in: query
       type: number
       required: true
     - name: skewness
       in: query
       type: number
       required: true
     - name: curtosis
       in: query
       type: number
       required: true
     - name: entropy
       in: query
       type: number
       required: true
    responses:
       200:
           descriprion: The output values
    """
    
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return "The predicted value is"+ str(prediction)


def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style = "background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("skewness")
    curtosis = st.text_input("curtosis","Type Here")
    entropy = st.text_input("entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Laarn")
        st.text("Built with Streamlit")



if __name__ == '__main__':
    main()