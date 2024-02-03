import streamlit as st
import numpy as np 
import pickle

loaded_model = pickle.load(open('classifier.pkl', 'rb'))

# creating a function for Prediction

def banknote_predict(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The Note is Authentic'
    else:
      return 'The Note is Fake'

#CODING THE WEBSITE LAYOUT

st.title('Hello 👋This is my first WebApp in Streamlit')



'''
with st.sidebar:
  
  st.title('*THANKS 🙏🏻 FOR ATTENDING ML BOOTCAMP*')
  st.divider()

  st.write('Dear incredible students, Heartfelt gratitude for your exceptional dedication and enthusiasm during the ML Bootcamp. Your passion and hard work have made this program a resounding success. Thank you for being part of this transformative learning experience. Wishing you continued success in your journey with machine learning.')
  st.divider()'''
  
st.divider()
with st.expander('Project Features'):
  st.write('*The Project takes input of given features :*')
  st.caption('1. Variance')
  st.caption('2. skewness')
  st.caption('3. Curtosis')
  st.caption('4. Entropy')

#MAIN LOGIC
def main():
    # giving a title
    st.subheader('Enter the feature of 💵')
    
    
    # getting the input data from the user
    variance = st.text_input('Enter the value of variance')
    skewness = st.text_input('Enter the value of skewness')
    curtosis = st.text_input('Enter the value of curtosis')
    entropy =  st.text_input('Enter the value of entropy')
    
    # code for Prediction
    prediction = ''
    
    # creating a button for Prediction
    
    if st.button('Predict The Result'):
        prediction = banknote_predict([variance,skewness,curtosis,entropy])
        
        
    st.success(prediction)

    st.divider()
    st.subheader('Made with 💌 by GDSC KIET')

if __name__ == '__main__':
    main()
