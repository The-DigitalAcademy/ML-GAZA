import streamlit as st
import numpy as np

st.title(" Durban Market Price prediction")

def Durban_market_price_prediction(input_data):
     # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'No average price'
    else:
      return 'The average price'

st.image("https://lh3.googleusercontent.com/p/AF1QipOcO8yiWIR3cXIW8QIRkyrTTIqdCrgdT8FimUA9=s1360-w1360-h1020")
st.title('Commodities average price prediction')
        
col1,col2 = st.columns(2)
def main():
    col1,col2 = st.columns(2)
    with col1:
        Commodities=st.radio("Commodities",['POTATO (WASHED) MONDIAL','TOMATOES-LONG LIFE','ONIONS BROWN','POTATO SIFRA (WASHED)','ONIONS MILD'])
        Provinces = st.selectbox('Province', ['CAPE', 'GAUTENG', 'TRANSVAAL', 'WESTERN FREESTATE', 'NATAL',
       'KWAZULU NATAL', 'IMPORTS - OUTSIDE RSA', 'OTHER AREAS',
       'NORTHERN CAPE', 'W.CAPE-BERGRIVER ETC',
       'SOUTH WESTERN FREE STATE', 'EASTERN FREESTATE', 'WEST COAST',
       'WESTERN CAPE - CERES', 'NORTH EASTERN CAPE', 'EASTERN CAPE',
       'ORANGE FREE STATE', 'MPUMALANGA', 'NORTH WEST',
       'MPUMALANGA MIDVELD', 'NAMIBIA', 'SOUTHERN CAPE'])
        Containers= st.selectbox('enter container type', ['EC120', 'M4183', 'AT200', 'BJ090', 'PP100', 'AP010', 'BI100',
       'JG110', 'LA020', 'AD100', 'BN150', 'AE050', 'BC180', 'BD100',
       'PD050', 'AG100', 'BJ100', 'LB043', 'JE090', 'LI060', 'BD050',
       'AF070', 'AZ035', 'HJ100', 'BM050', 'NE005', 'AG070', 'HF060',
       'AI200', 'BY150', 'KR200', 'BS200', 'IA400', 'BV150', 'AC030',
       'PA005', 'SL025', 'AC050', 'BS060', 'BF070', 'PE080', 'M6125',
       'P1070', 'MA053', 'JC070', 'AB020', 'BE060', 'KY148', 'A1001',
       'JF100', 'LC080', 'LH100', 'HG070', 'KA100', 'A2250', 'OA003',
       'AJ100', 'NP005', 'P2020', 'AA010', 'CZ015', 'LE040', 'SL030',
       'EF120', 'PC030', 'AF060', 'OP100', 'CB045', 'LD080', 'AX015',
       'AD040', 'AL120', 'TL020', 'JA050', 'KI175', 'BX150', 'OB008',
       'BW100', 'MA050', 'DL070', 'TS035', 'BB020', 'LC030', 'AH080',
       'AO150', 'BE100', 'LG050', 'PB008', 'AA015', 'NP002', 'TR020',
       'BA050', 'CC082', 'AQ170', 'AB030', 'SC250', 'NP040', 'BG080',
       'JI130', 'SP200', 'NT008', 'M9125', 'HR002', 'BA020', 'HL120',
       'LK070', 'IB420', 'KJ180', 'AC035', 'IF380', 'KM200', 'HH080',
       'A4125', 'EP120', 'A0160', 'LU150', 'M4155', 'ML100', 'LQ100',
       'AX250', 'HA010', 'B4085', 'IG500', 'JV040', 'BT070', 'BK080',
       'PP010', 'DT063', 'LF100', 'MB070', 'KF150', 'CA100', 'A8145',
       'SL035', 'SW300', 'BH090', 'LL075', 'HC030', 'NK020', 'A3305',
       'JP130', 'KG160', 'NR100', 'DL076', 'NJ010', 'SB270', 'HU008',
       'PC010', 'LM080', 'EG140', 'IE500', 'TT025', 'NN050'])
        Size_Grade= st.selectbox("size grade", ['1L', '1R', '2M', '1M', '2X', '3L', '2L', 'M', '1S', '1', 'L',
       '1Z', '2S', '2Z', '2', '1X', '3S', '4M', 'X', '1U', '3M', '4S',
       '1G', '1A', '2R', '1B', '2C', '3R', '2U', '0', '3Z', '2B', '2A',
       '1C', '2G', 'S', '4R', '3U', '4Z', '4L', '0M', 'G', '3X', '4U',
       '3G', 'U', '4X'])
    with col2:
            Weight_Kg= number = st.number_input("weight per kilo")
            Sales_Total= st.number_input('total sale')
            Total_Kg_Sold = st.number_input('total kg sold')
            Stock_On_Hand= st.number_input('stock on hand', step=1)
    
    
    # code for Prediction
    Average_price = ''
    
    # creating a button for Prediction
    
    if st.button('Average Price Test Result'):
        Average_price = Durban_market_price_prediction(['Province','Container','Size_Grade','Commodities','Weight_Kg',
 'Sales_Total','Total_Kg_Sold','Stock_On_Hand','selling_price'])
        
    st.success(Average_price)
    
if __name__ == '__main__':
    main()
    
  