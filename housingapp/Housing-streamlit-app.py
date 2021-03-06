import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import numpy as np
from sklearn import metrics
st.set_page_config(layout="wide")
st.image(
    "https://www.freepnglogos.com/uploads/house-png/house-png-commonwealth-magazine-18.png",
   # "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/271/artist-palette_1f3a8.png",
    width=200,
)



st.title('House Price Estimator')
# load dataset
df = pd.read_csv('housing.csv')
df1 = pd.read_csv('../Data/perfData.csv')
# show the entire dataframe
st.write(df1)

# f-string
st.subheader('SalePrice')
#survival_count = df['Survived'].value_counts()
#st.text(f'Survival rate = {survival_count.values[1]/sum(survival_count):.2%}')

# simple plotting
fig, ax = plt.subplots(1, 1, figsize=(15, 5))
#survival_count.plot.bar(ax=ax[0])

df['SalePrice'].plot.hist()#ax=ax[0]
st.pyplot(fig)


st.subheader('Making Prediction')
st.markdown('**Please provide your input below**:')  # you can use markdown like this


# load models
tree_reg = joblib.load('Housing.pickle')
# get inputs
#'LotArea','BldgType','HouseStyle','YearBuilt','FullBath','HalfBath','BedroomAbvGr'
############
###Area of the housing data
dataset = st.sidebar.radio('Area', ['Newark-DE', 'Bear-DE', 'Wilmington-DE', 'Ames-IA'])
############Building type
#BldgType: ['1Fam', '2fmCon', 'Duplex', 'TwnhsE', 'Twnhs']


    
# initialize list of lists
data_BldgType = [['Single-family Detached', '1Fam'], ['Two-family Conversion; originally built as one-family dwelling', '2fmCon'], ['Duplex', 'Duplex'], ['Townhouse End Unit', 'TwnhsE'], ['Townhouse Inside Unit', 'Twnhs']]

# Create the pandas DataFrame
df_BldgType = pd.DataFrame(data_BldgType, columns=['Name', 'ID'])
values_BldgType = df_BldgType['Name'].tolist()
options_BldgType = df_BldgType['ID'].tolist()
dic_BldgType = dict(zip(options_BldgType, values_BldgType))

##########
############Housing Style
##HouseStyle: ['1Story',  '1.5Fin', '1.5Unf', '2Story', '2.5Fin','2.5Unf', 'SFoyer', 'SLvl']

# initialize list of lists
#data_HouseStyle = [['One story', '1Story'], ['One and one-half story: 2nd level finished', '1.5Fin'], ['One and one-half story: 2nd level unfinished', '1.5Unf'], ['Two story', '2Story'], ['Two and one-half story: 2nd level finished', #'2.5Fin'], ['Two and one-half story: 2nd level unfinished', '2.5Unf'], ['Split Foyer', 'SFoyer'],['Split Level', 'SLvl']]

# Create the pandas DataFrame
#df_HouseStyle = pd.DataFrame(data_HouseStyle, columns=['Name', 'ID'])
#values_HouseStyle = df_HouseStyle['Name'].tolist()
#options_HouseStyle = df_HouseStyle['ID'].tolist()
#dic_HouseStyle = dict(zip(options_HouseStyle, values_HouseStyle))
#HouseStyle = st.selectbox('Choose a Housing Style', options_HouseStyle, format_func=lambda x: dic_HouseStyle[x])

#st.write(HouseStyle)
year_range = range(1850, 2022)
garage_range = range(0, 6)
############

#HouseStyle = st.selectbox('Building Type', ['1Story', 'One and one-half story: 2nd level finished', 'One and one-half story: 2nd level unfinished', 'Two story', 'Two and one-half story: 2nd level finished', 'Two and one-half story: 2nd level #unfinished', 'Split Foyer', 'Split Level'])
###
with st.form(key='columns_in_form'):
    BldgType = st.selectbox('Choose a Building Type', options_BldgType, format_func=lambda x: dic_BldgType[x])
    BedroomAbvGr = int(st.number_input('# of Bedrooms', 0, 10, 5))
    HalfBath = int(st.number_input('# of Half Bath', 0, 5, 2))
    FullBath = int(st.number_input('# of Full Bath', 0, 10, 4))
    TotalSF = int(st.number_input('Total Square feet',step=1, value = 5000))
    LotArea = int(st.number_input('Lot Area',step=1, value = 50000))
    GarageCars = st.select_slider('# of Garage', options = garage_range, value = 2)
    YearBuilt = st.select_slider('Year Built', options = year_range, value = 1995)
    submitted = st.form_submit_button('Submit')

#num = st.number_input(
#   "Higher precision step",
#    min_value=1.0,
#    max_value=5.0,
#    step=1e-6,
#    format="%.5f")




# this is how to dynamically change text
prediction_state = st.markdown('calculating...')

housePrice = pd.DataFrame(
   {     
#       'dataset': [dataset],
       'LotArea': [LotArea],
       'BldgType': [BldgType], 
       'GarageCars': [GarageCars],
       'YearBuilt': [YearBuilt],
       'FullBath': [FullBath],
       'HalfBath': [HalfBath],
       'BedroomAbvGr': [BedroomAbvGr],
       'TotalSF' : [TotalSF]
   }
)

y_pred = tree_reg.predict(housePrice)

row_index = df1.set_index('City').index.get_loc(dataset)
baselinePrice = df1.iloc[row_index,5]

#baselineDf = pd.DataFrame(
#   {     
#       'baseline': [baseline]
#   }
#)

variance = (baselinePrice - y_pred[0])


#if y_pred[0] == 0:
#    msg = 'This passenger is predicted to be: **died**'
#else:
#    msg = 'This passenger is predicted to be: **survived**'

st.write('The predicted House value is', y_pred[0])



st.write("There could be a price variance of $",np.round(variance,2), "in", dataset )


st.write("check out this [link](https://public.tableau.com/shared/2JGJX9Y2H?:showVizHome=no#1)")

#st.write()
#st.write(df1)

#age = int(st.number_input('Age:', 0, 120, 20))
#sib_sp = int(st.number_input('# of siblings / spouses aboard:', 0, 10, 0))
#par_ch = int(st.number_input('# of parents / children aboard:', 0, 10, 0))
#pclass = st.selectbox('Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)', [1, 2, 3])
#fare = int(st.number_input('# of parents / children aboard:', 0, 100, 0))
#embarked = st.selectbox('Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)', ['C', 'Q', 'S'])