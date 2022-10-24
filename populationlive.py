import numpy as np
import pickle
import streamlit as st

# Load the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# Create a function for Prediction
def population_prediction(input_data):

    # Change the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not population'
    else:
      return 'The person is population'
  
def main():
    
    # Give a title
    st.title('Population Prediction Web App')
    
    # To get the input data from the user
    Area = st.text_input('Total population')
    Density = st.text_input('Pre Total population')
    GrowthRate = st.text_input('Population value')
    Rank = st.text_input('Total value')

    
    # Code for Prediction
    Population = ''
    
    # Create a button for Prediction
    
    if st.button('Population Test Result'):
        Live = population_prediction([Population, Area, Density, GrowthRate, Rank])
        
    st.success(Live)
    
if __name__ == '__main__':
    main()
