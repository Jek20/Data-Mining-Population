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
    
    prediction = loaded_model.index(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not Population'
    else:
      return 'The person is Population'
  
def main():
    
    # Give a title
    st.title('Population Prediction Website App')
    
    # To get the input data from the user
    Area = st.text_input('Total Population')
    Density = st.text_input('Pre Total Population')
    GrowthRate = st.text_input('Population Value')
    Rank = st.text_input('Total Value')

    # Code for Prediction
    Live = ''
    
    # Create a button for Prediction
    if st.button('Population Test Result'):
        Live = population_prediction([Area, Density, GrowthRate, Rank, Population])
   
    st.success(Live)
    
if __name__ == '__main__':
    main()
