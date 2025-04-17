# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 00:14:18 2025

@author: OLADOYINBO BABATUNDE
"""

import numpy as np
import statsmodels.api as sm
import pickle
import streamlit as st

loaded_model_uganda = pickle.load(open('C:/Users/OLADOYINBO BABATUNDE/trained_uganda_model.sav', 'rb'))

#Creating a function 
def fin_stress_prediction(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model_uganda.predict(sm.add_constant(input_data_reshaped, has_constant='add'))
    
    prediction = prediction[0]
    if (prediction >= 21.3375):
        recommendation = """
        ----------------------------------PLEASE NOTE THAT I AM NOT A FORTUNE TELLER----------------------------------
        In accordance to the analysis done by the Predictive Model of 99.1% accuracy and Mean Square Error value of 591.56, below are some recommendations 
        for your household.
        
        1. It is advisable that you engage in various fund sourcing means around you such as Reducing Spending, Selling of Assets and Borrowing.
        2. Also, endeavor the use of Saving Groups and Saving Account.
        3. Here is a PROBABLE recommendation, if you stay in places such as Arua and Hoima, you might want to consider relocation.
        4. You might have need of more hands on farm. Please consider engaging family.
        5. Also consider having more knowledge about Farming, such as attending seminars and co.
        6. Endeavour to dedicate more time to your farm and livestock or other source of incomes.
        7. In reflection of the least financial stressed households pattern of crop harvesting, please endeavour to plant more and also plant earlier in season.
        8. Storage facilities should be implemented and used in order to reduce loss of crop and farm produce.
        """ 
        return recommendation
    else:
        recommendation = """
        ----------------------------------PLEASE NOTE THAT I AM NOT A FORTUNE TELLER----------------------------------
        In accordance to the analysis done by the Predictive Model of 99.1% accuracy and Mean Square Error value of 591.56, below are some recommendations 
        for your household.
        1. Due to the general flunctuating Crop Income that causes financial stress in households, endeavour to do better than previous years.
        2. In reflection of the relatively stable Crop Income of other households, it is advisable that you engage in short term planting crops in order to
           help during planting seasons.
        3. Storage facilities should be implemented and used in order to reduce loss of crop and farm produce.
        """ 
        return recommendation
        
def pred(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model_uganda.predict(sm.add_constant(input_data_reshaped, has_constant='add'))
    
    return prediction[0]



def main():
    
    
    st.title('Uganda Household Financial Stress Score Prediction')
    
    # y_pred = lm1.predict(sm.add_constant(X_test, has_constant='add'))
    #cons = 
    
    Is_Location = st.radio("Where do you live?", ['Mbale', 'Mbarara', 'Jinja', 'Fort Portal', 'Hoima', 'Lira', 'Arua', 'Gulu', 'Kampala', 'Masaka'])
    if Is_Location == 'Mbale':
        Location_Mbale = 1; Location_Mbarara = 0; Location_Jinja = 0; Location_Fort_Portal = 0; Location_Hoima = 0;
        Location_Lira = 0; Location_Gulu = 0; Location_Kampala = 0; Location_Masaka = 0
    elif Is_Location == 'Mbarara':
        Location_Mbale = 0; Location_Mbarara = 1; Location_Jinja = 0; Location_Fort_Portal = 0; Location_Hoima = 0;
        Location_Lira = 0; Location_Gulu = 0; Location_Kampala = 0; Location_Masaka = 0
    elif Is_Location == 'Jinja':
        Location_Mbale = 0; Location_Mbarara = 0; Location_Jinja = 1; Location_Fort_Portal = 0; Location_Hoima = 0;
        Location_Lira = 0; Location_Gulu = 0; Location_Kampala = 0; Location_Masaka = 0
    elif Is_Location == 'Fort Portal':
        Location_Mbale = 0; Location_Mbarara = 0; Location_Jinja = 0; Location_Fort_Portal = 1; Location_Hoima = 0;
        Location_Lira = 0; Location_Gulu = 0; Location_Kampala = 0; Location_Masaka = 0
    elif Is_Location == 'Hoima':
        Location_Mbale = 0; Location_Mbarara = 0; Location_Jinja = 0; Location_Fort_Portal = 0; Location_Hoima = 1;
        Location_Lira = 0; Location_Gulu = 0; Location_Kampala = 0; Location_Masaka = 0
    elif Is_Location == 'Lira':
        Location_Mbale = 0; Location_Mbarara = 0; Location_Jinja = 0; Location_Fort_Portal = 0; Location_Hoima = 0;
        Location_Lira = 1; Location_Gulu = 0; Location_Kampala = 0; Location_Masaka = 0
    elif Is_Location == 'Arua':
        Location_Mbale = 0; Location_Mbarara = 0; Location_Jinja = 0; Location_Fort_Portal = 0; Location_Hoima = 0;
        Location_Lira = 0; Location_Gulu = 0; Location_Kampala = 0; Location_Masaka = 0
    elif Is_Location == 'Gulu':
        Location_Mbale = 0; Location_Mbarara = 0; Location_Jinja = 0; Location_Fort_Portal = 0; Location_Hoima = 0;
        Location_Lira = 0; Location_Gulu = 1; Location_Kampala = 0; Location_Masaka = 0
    elif Is_Location == 'Kampala':
        Location_Mbale = 0; Location_Mbarara = 0; Location_Jinja = 0; Location_Fort_Portal = 0; Location_Hoima = 0;
        Location_Lira = 0; Location_Gulu = 0; Location_Kampala = 1; Location_Masaka = 0
    elif Is_Location == 'Masaka':
        Location_Mbale = 0; Location_Mbarara = 0; Location_Jinja = 0; Location_Fort_Portal = 0; Location_Hoima = 0;
        Location_Lira = 0; Location_Gulu = 0; Location_Kampala = 0; Location_Masaka = 1
        
        
    Family_Size = st.slider('What is your family size (Everyone Living together in the household)?',0,30,step=1)
    
    Is_Education = st.radio("What is the Education Level of your household?", ['Secondary', 'No_Education', 'Tertiary', 'Primary'])    
    if Is_Education == 'Secondary':
        Education_Level_Primary = 0; Education_Level_Secondary = 1; Education_Level_Tertiary = 0
    elif Is_Education == 'No_Education':
        Education_Level_Primary = 0; Education_Level_Secondary = 0; Education_Level_Tertiary = 0   
    elif Is_Education == 'Tertiary':
        Education_Level_Primary = 0; Education_Level_Secondary = 0; Education_Level_Tertiary = 1 
    elif Is_Education == 'Primary':
        Education_Level_Primary = 1; Education_Level_Secondary = 0; Education_Level_Tertiary = 0
        
    Employment_Type = st.radio("What is the Employment type of your Household?", ['Subsistence Farming', 'Livestock Rearing', 'Small Business', 'Casual Labor'])  
    if Employment_Type == 'Subsistence Farming':
        Employment_Type_Livestock_Rearing = 0; Employment_Type_Small_Business = 0; Employment_Type_Subsistence_Farming = 1
    elif Employment_Type == 'Livestock Rearing':
        Employment_Type_Livestock_Rearing = 1; Employment_Type_Small_Business = 0; Employment_Type_Subsistence_Farming = 0
    elif Employment_Type == 'Small Business':
        Employment_Type_Livestock_Rearing = 0; Employment_Type_Small_Business = 1; Employment_Type_Subsistence_Farming = 0
    elif Employment_Type == 'Casual Labor':
        Employment_Type_Livestock_Rearing = 0; Employment_Type_Small_Business = 0; Employment_Type_Subsistence_Farming = 0
        
    Is_Saving_Account = st.radio('Do you have a Saving Account? ', ['Yes', 'No'])
    if Is_Saving_Account == 'Yes':
        Has_Savings_Account = 1
    else:
        Has_Savings_Account = 0
        
    Use_Saving_Group = st.radio('Do you use Saving Group? ', ['Yes', 'No'])
    if Use_Saving_Group == 'Yes':
        Uses_Savings_Group = 1
    else:
        Uses_Savings_Group = 0
    
    Use_Mobile_Money = st.radio('Do you use Mobile Money? ', ['Yes', 'No'])
    if Use_Mobile_Money == 'Yes':
        Uses_Mobile_Money = 1
    else:
        Uses_Mobile_Money = 0
        
    Is_Borrowing = st.radio('Do you Borrow money during financial stress? ', ['Yes', 'No'])
    if Is_Borrowing == 'Yes':
        Borrowing = 1
    else:
        Borrowing = 0
        
    Is_Selling_Assets = st.radio('Do you Sell Assets during financial stress? ', ['Yes', 'No'])
    if Is_Selling_Assets == 'Yes':
        Selling_Assets = 1
    else:
        Selling_Assets = 0

    Is_Reducing_Spending = st.radio('Do you reduce spending during financial stress? ', ['Yes', 'No'])
    if Is_Reducing_Spending == 'Yes':
        Reducing_Spending = 1
    else:
        Reducing_Spending = 0
        
    Distance_to_Bank_km = st.number_input("How far is your house from the closest bank? (In Kilometres) ")
    
    Total_Income = st.number_input("What is the avarage total income for your household for past 2 years? (In UGX) ")

    
#    prediction = ''
    
    
    if st.button('Predict Financial Stress Score for Household'):
        prediction = fin_stress_prediction([Family_Size, Has_Savings_Account, Uses_Savings_Group,
       Uses_Mobile_Money, Distance_to_Bank_km, Borrowing,
       Selling_Assets, Reducing_Spending, Total_Income,
       Location_Fort_Portal, Location_Gulu, Location_Hoima,
       Location_Jinja, Location_Kampala, Location_Lira,
       Location_Masaka, Location_Mbale, Location_Mbarara,
       Education_Level_Primary, Education_Level_Secondary,
       Education_Level_Tertiary, Employment_Type_Livestock_Rearing,
       Employment_Type_Small_Business,
       Employment_Type_Subsistence_Farming])
        
        prediction1 = pred([Family_Size, Has_Savings_Account, Uses_Savings_Group,
       Uses_Mobile_Money, Distance_to_Bank_km, Borrowing,
       Selling_Assets, Reducing_Spending, Total_Income,
       Location_Fort_Portal, Location_Gulu, Location_Hoima,
       Location_Jinja, Location_Kampala, Location_Lira,
       Location_Masaka, Location_Mbale, Location_Mbarara,
       Education_Level_Primary, Education_Level_Secondary,
       Education_Level_Tertiary, Employment_Type_Livestock_Rearing,
       Employment_Type_Small_Business,
       Employment_Type_Subsistence_Farming])
        
        
    st.success(f'This is the Predicted Value of your Household Financial Stress: {prediction1}')
    st.success(prediction)
    
    
    
    
if __name__ == '__main__':
    main()

    
