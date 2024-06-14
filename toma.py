import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load the trained model
model_save_path = "mlra.pkl"
with open(model_save_path, 'rb') as file:
    loaded_model = pickle.load(file)

# # Sidebar with input field descriptions
# st.sidebar.header("Description of The Required Input Fields")
# st.sidebar.markdown("**Province**: The provinces producing Onion brown.")   
# st.sidebar.markdown("**Size_Grade**: The sizes of the brown onion packages.")
# st.sidebar.markdown("**Weight_Kg**: The kilogram weight that the onion brown weigh.")
# st.sidebar.markdown("**Low_Price**: The lowest price the onion brown cost.")
# st.sidebar.markdown("**Sales_Total**: The total price purchase onion brown.")
# st.sidebar.markdown("**Stock_On_Hand**: The onion brown stock currently available in the warehouse.")



# Streamlit interface
st.title("Tomato-long life Average Price Prediction")


#Feature names: ['Weight_Kg', 'Low_Price', 'High_Price', 'Province', 'Container', 'Size_Grade', 'Month']
# Function to preprocess user inputs and make predictions
def predict_price(Weight_Kg,Low_Price,High_Price,Province,Container,Size_Grade,Month):
    # Assuming label encoding mappings are known
    province_mapping = {'NATAL':0,'NORTH EASTERN CAPE':1,'TRANSVAAL':2}
    # Replace with actual mappings
    weight_mapping ={}
    size_grade_mapping = {'1L':0, '1M':1,'1R':2,'1S':3,'1U':4,'1X':5,'1Z':6,'2L':7,'2M':8,'2R':9,'2S':10,'2X':11,'2Z':12,'3M':13,'3R':14,'3S':15,'3Z':16}
    Container_mapping = {'BM050':0,'BS060':1,'BT070':2}
    # Convert categorical inputs to numerical using label encoding
    province_encoded = province_mapping.get(Province,-1)  # Use -1 for unknown categories
    size_grade_encoded = size_grade_mapping.get(Size_Grade,-1)  # Use -1 for unknown categories
    Container_encoded= Container_mapping.get(Container,-1)

    # Prepare input data as a DataFrame for prediction
    input_data = pd.DataFrame([[Weight_Kg,Low_Price, High_Price, province_encoded,Container_encoded,size_grade_encoded,Month]],
                              columns=['Weight_Kg', 'Low_Price', 'High_Price', 'Province', 'Container', 'Size_Grade', 'Month'])
     # Rename columns to string names
     # Make sure the feature names match the model's expectations
    input_data.columns = ['Weight_Kg', 'Low_Price', 'High_Price', 'Province', 'Container', 'Size_Grade', 'Month']

    # Make prediction
    predicted_price = loaded_model.predict(input_data)

    return predicted_price[0]

# Organize input fields into columns
col1, col2, col3 = st.columns(3)

with col1:
    Province = st.selectbox('Province', ["NATAL","NORTH EASTERN CAPE","TRANSVAAL"])
    Size_Grade = st.selectbox("Size Grade", ["1L", "1M","1R","1S","1U","1X","1Z","2L","2M","2R","2S","2X","2Z","3M","3R","3S","3Z"])
    #Total_Kg_Sold = st.number_input('Total Kilos Sold', min_value=0)
    
with col2:
    Container = st.selectbox("Container", ["BM050","BS060","BT070"])
    Weight_Kg = st.selectbox("Weight(Kg)", [0.5,1,2,3.5,4,5,6,7,9,10,16,20])
    Month = st.slider("Month",1,12)

with col3:
    Low_Price = st.number_input("Low Price(R)", min_value=0)
    High_Price = st.number_input("High Price(R)", min_value=0)
    #Sales_Total = st.number_input('Total Sale', min_value=0)
    
    

# Make prediction
if st.button("Predict"):
     # Call the prediction function
    prediction_price=predict_price(Weight_Kg,Low_Price,High_Price,Province,Container,Size_Grade,Month)
    st.success(f'Predicted Average Price of Tomato-long life : R{prediction_price:.2f}')