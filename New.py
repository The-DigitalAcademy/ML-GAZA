import streamlit as st
import pandas as pd
import pickle


background_image_url = "https://cdn.britannica.com/16/187216-131-FB186228/tomatoes-tomato-plant-Fruit-vegetable.jpg"

#Custom CSS
background_css = f"""
<style>
    .stApp {{
        background: url("{background_image_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
</style>
"""

#Inject the CSS into the Streamlit app
st.markdown(background_css, unsafe_allow_html=True)

# Load the pickle file containing the model and encoded features
def load_model():
    with open('mlr.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Main function to run the app
def main():
    st.title('Market Prediction')

    # Load the model
    model = load_model()
    st.write("Model loaded successfully.")

    # Display the list of features
    #st.subheader('Features:')
    #'Weight_Kg', 'Low_Price', 'High_Price', 'Province', 'Container', 'Month'
    features = ['Weight in Kg', 'Low Price in Rands', 'High Price in Rands', 'Province', 'Container', 'Month']
    #features = ['Weight_Kg', 'Low_Price', 'High_Price','Month_encoded', 'Province_encoded', 'Container_encoded','Size_Grade_encoded']
    
    month = ["April","August","February","December","January","July","June","March","May","October","September"]
    province = ["NATAL","NORTH EASTERN CAPE","TRANSVAAL"]
    container = ["BM050","BS060","BT070"]
    #sizegrade = ["1L", "1M","1R","1S","1U","1X","1Z","2L","2M","2R","2S","2X","2Z","3M","3R","3S","3Z"]
    
    user_inputs = {}
    for feature in features:
        if feature == "Province" or feature == "Container" or feature == "Month":
            if feature == "Province":
                ss = province
            elif feature == "Container":
                ss = container
            elif feature == "Month":
                ss = month
    
            display = (ss)

            options = list(range(len(display)))

            value = st.selectbox(feature, options, format_func=lambda x: display[x], key=feature)
            
            user_inputs[feature] = value
            
        else:
            user_input = st.text_input(f"Enter {feature}:")
            try:
                user_inputs[feature] = float(user_input)
            except:
                st.write("")

    # Prediction button
    if st.button('Predict'):
        # Convert user inputs into DataFrame
        user_inputs_df = pd.DataFrame([user_inputs])
        # st.write("User inputs:", user_inputs_df) # Debug statement
        
        # Predict using the loaded model
        try:
            prediction = model.predict(user_inputs_df)
            st.write('Predicting average price of Tomato-long life: R  ', prediction[0])
        except Exception as e:
            st.write("Error occurred during prediction:", e)

# Run the app
if __name__ == '__main__':
    main()