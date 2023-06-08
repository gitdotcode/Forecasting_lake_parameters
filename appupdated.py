install_requires=['pandas', 'numpy', 'scipy', 'statsmodels', 'humanize', 'requests', 'matplotlib' ]

import pandas as pd
import numpy as np
import streamlit as st
import pickle
from pickle import dump
from pickle import load


from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.holtwinters import Holt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# ph_data = pickle.load(open('ph_dict.pkl','rb'))


ph = pd.read_excel('./Downloads/Lake_data/pH.xlsx')
tds = pd.read_excel('./Downloads/Lake_data/TDS.xlsx')
bod = pd.read_excel('./Downloads/Lake_data/BOD.xlsx')
cod = pd.read_excel('./Downloads/Lake_data/COD.xlsx')
do = pd.read_excel('./Downloads/Lake_data/DO.xlsx')



# array = ph.values
# pH
site1_model_ph = load(open('hwe_model_add_ph.sav','rb'))
site2_model_ph = load(open('hwe_model_add2_ph.sav','rb'))
site3_model_ph = load(open('hwe_model_add3_ph.sav','rb')) 

ph_o_trend = load(open('final_ph_predicted.sav','rb'))

# TDS
site1_model_tds = load(open('hwe_model_add_tds.sav','rb'))
site2_model_tds = load(open('hwe_model_add2_tds.sav','rb'))
site3_model_tds = load(open('hwe_model_add3_tds.sav','rb'))

tds_o_trend = load(open('final_tds_predicted.sav','rb'))

# BOD
site1_model_bod = load(open('hwe_model_add_bod.sav','rb'))
site2_model_bod = load(open('hwe_model_add2_bod.sav','rb'))
site3_model_bod = load(open('hwe_model_add3_bod.sav','rb'))

bod_o_trend = load(open('final_bod_predicted.sav','rb'))

# COD
site1_model_cod = load(open('hwe_model_add_cod.sav','rb'))
site2_model_cod = load(open('hwe_model_add2_cod.sav','rb'))
site3_model_cod = load(open('hwe_model_add3_cod.sav','rb'))

cod_o_trend = load(open('final_cod_predicted.sav','rb'))

# DO
site1_model_do = load(open('hwe_model_add_do.sav','rb'))
site2_model_do = load(open('hwe_model_add2_do.sav','rb'))
site3_model_do = load(open('hwe_model_add3_do.sav','rb'))

do_o_trend = load(open('final_do_predicted.sav','rb'))

# site1_pH_predictions = load(open('predicted_pH_Site_01.sav','rb'))
# site2_pH_predictions = load(open('predicted_pH_Site_02.sav','rb'))
# site3_pH_predictions = load(open('predicted_pH_Site_03.sav','rb'))

# site1_tds_predictions = load(open('predicted_tds_Site_01.sav','rb'))
# site2_tds_predictions = load(open('predicted_tds_Site_02.sav','rb'))
# site3_tds_predictions = load(open('predicted_tds_Site_03.sav','rb'))

# site1_bod_predictions = load(open('predicted_bod_Site_01.sav','rb'))
# site2_bod_predictions = load(open('predicted_bod_Site_02.sav','rb'))
# site3_bod_predictions = load(open('predicted_bod_Site_03.sav','rb'))

# site1_cod_predictions = load(open('predicted_cod_Site_01.sav','rb'))
# site2_cod_predictions = load(open('predicted_cod_Site_02.sav','rb'))
# site3_cod_predictions = load(open('predicted_cod_Site_03.sav','rb'))

# site1_do_predictions = load(open('predicted_do_Site_01.sav','rb'))
# site2_do_predictions = load(open('predicted_do_Site_02.sav','rb'))
# site3_do_predictions = load(open('predicted_do_Site_03.sav','rb'))






    
def main():
    
    # Giving title
    st.title('Forecasting the lake parameters : Water Quality')
    menu = ['Home', 'Forecast', 'Trend']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'Home':
        st.subheader('Home')
        option = st.selectbox('Select the parameter to see the required data',('Select','pH_data','TDS_data','BOD_data','COD_data','DO_data'))
        if option == 'pH_data':
            chart_d1 = st.line_chart(ph[['Site 01', 'Site 02', 'Site 03']])
            return st.dataframe(ph), chart_d1
        elif option == 'TDS_data':
            chart_d2 = st.line_chart(tds[['Site 01', 'Site 02', 'Site 03']])
            return st.dataframe(tds), chart_d2
        elif option == 'BOD_data':
            chart_d3 = st.line_chart(bod[['Site 01', 'Site 02', 'Site 03']])
            return st.dataframe(bod), chart_d3
        elif option == 'COD_data':
            chart_d4 = st.line_chart(cod[['Site 01', 'Site 02', 'Site 03']])
            return st.dataframe(cod), chart_d4
        elif option == 'DO_data':
            chart_d5 = st.line_chart(do[['Site 01', 'Site 02', 'Site 03']])
            return st.dataframe(do), chart_d5

    elif choice == "Forecast":
        st.subheader("Forecast the parameter")
    
    # Getting the input data from the user
        option1 = st.selectbox('Site',('Select',1,2,3))
        option2 = st.selectbox('Parameter',('Select','pH','TDS','BOD','COD','DO'))
        option3 = st.selectbox('Number of weeks to be predicted',('Select',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24))
    
        def forecasting(option1, option2, option3):
            
            if option1 == 1 and option2 == 'pH':
                prediction_site1_ph = site1_model_ph.forecast(option3)
                chart1_ph = st.line_chart(prediction_site1_ph.values)
                return prediction_site1_ph.values, chart1_ph
            
            elif option1 == 2 and option2 == 'pH':
                prediction_site2_ph = site2_model_ph.forecast(option3)
                chart2_ph = st.line_chart(prediction_site2_ph.values)
                return prediction_site2_ph.values, chart2_ph
            
            elif option1 == 3 and option2 == 'pH':
                prediction_site3_ph = site3_model_ph.forecast(option3)
                chart3_ph = st.line_chart(prediction_site3_ph.values)
                return prediction_site3_ph.values, chart3_ph  
            
            elif option1 == 1 and option2 == 'TDS':
                prediction_site1_tds = site1_model_tds.forecast(option3)
                chart1_tds = st.line_chart(prediction_site1_tds.values)
                return prediction_site1_tds.values, chart1_tds     

            elif option1 == 2 and option2 == 'TDS':
                prediction_site2_tds = site2_model_tds.forecast(option3)
                chart2_tds = st.line_chart(prediction_site2_tds.values)
                return prediction_site2_tds.values, chart2_tds   
            
            elif option1 == 3 and option2 == 'TDS':
                prediction_site3_tds = site3_model_tds.forecast(option3)
                chart3_tds = st.line_chart(prediction_site3_tds.values)
                return prediction_site3_tds.values, chart3_tds          
            
            elif option1 == 1 and option2 == 'BOD':
                prediction_site1_bod = site1_model_bod.forecast(option3)
                chart1_bod = st.line_chart(prediction_site1_bod.values)
                return prediction_site1_bod.values, chart1_bod     

            elif option1 == 2 and option2 == 'BOD':
                prediction_site2_bod = site2_model_bod.forecast(option3)
                chart2_bod = st.line_chart(prediction_site2_bod.values)
                return prediction_site2_bod.values, chart2_bod   
            
            elif option1 == 3 and option2 == 'BOD':
                prediction_site3_bod = site3_model_bod.forecast(option3)
                chart3_bod = st.line_chart(prediction_site3_bod.values)
                return prediction_site3_bod.values, chart3_bod
            
            elif option1 == 1 and option2 == 'COD':
                prediction_site1_cod = site1_model_cod.forecast(option3)
                chart1_cod = st.line_chart(prediction_site1_cod.values)
                return prediction_site1_cod.values, chart1_cod    

            elif option1 == 2 and option2 == 'COD':
                prediction_site2_cod = site2_model_cod.forecast(option3)
                chart2_cod = st.line_chart(prediction_site2_cod.values)
                return prediction_site2_cod.values, chart2_cod 
            
            elif option1 == 3 and option2 == 'COD':
                prediction_site3_cod = site3_model_cod.forecast(option3)
                chart3_cod = st.line_chart(prediction_site3_cod.values)
                return prediction_site3_cod.values, chart3_cod
            
            elif option1 == 1 and option2 == 'DO':
                prediction_site1_do = site1_model_do.forecast(option3)
                chart1_do = st.line_chart(prediction_site1_do.values)
                return prediction_site1_do.values, chart1_do    

            elif option1 == 2 and option2 == 'DO':
                prediction_site2_do = site2_model_do.forecast(option3)
                chart2_do = st.line_chart(prediction_site2_do.values)
                return prediction_site2_do.values, chart2_do
            
            elif option1 == 3 and option2 == 'DO':
                prediction_site3_do = site3_model_do.forecast(option3)
                chart3_do = st.line_chart(prediction_site3_do.values)
                return prediction_site3_do.values, chart3_do                
      
    

        if st.button('Forecast'):
            
            try:
                result = forecasting(option1, option2, option3)
            except:
                result = 'Not Found'
                
            st.write(result)
            
            
    elif choice == 'Trend':
        option_trend = st.selectbox('Select the parameter to see the forecasted trend at three sites',('Select','pH_data','TDS_data','BOD_data','COD_data','DO_data'))
        if option_trend == 'pH_data':
            chart_o1 = st.line_chart(ph_o_trend)
            return chart_o1
        elif option_trend == 'TDS_data':
            chart_o2 = st.line_chart(tds_o_trend)
            return chart_o2
        elif option_trend == 'BOD_data':
            chart_o3 = st.line_chart(bod_o_trend)
            return chart_o3
        elif option_trend == 'COD_data':
            chart_o4 = st.line_chart(cod_o_trend)
            return chart_o4
        elif option_trend == 'DO_data':
            chart_o5 = st.line_chart(do_o_trend)
            return chart_o5
    
            
#     else:
#          st.subheader('Description')
#          st.text('Forecasting the parameters of lake water')
            


                    
#             forecasted_values = site1_model.forecast(number3)
    
#     # For site 02:
#             forecasted_values = site2_model.forecast(number3)
    
#     # For site 03:
#             forecasted_values = site3_model.forecast(number3)
    
#             if selected_site == site1:
#                 return site1_predictions
#             elif selected_site == site2:
#                 return site2_predictions
#             else:
    
#                 return site3_predictions
    
    
    
#     selected_site = st.selectbox('Select Site',products['Product_ID'].values)


    
    
    
    # Forecasting
#     forecast = ''
#     # Button
#     if st.button('Site Result'):
#         forecast = forecasting([option1, option2, option3])
        
#     st.success(forecast)
    
    
    
if __name__ == '__main__':
    main()
        


    
