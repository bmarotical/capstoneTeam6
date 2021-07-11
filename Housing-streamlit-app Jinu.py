import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

st.title('Housing Price Prediction')
# load dataset
df = pd.read_csv('Data/housing.csv')

# show the entire dataframe
st.write(df)

# f-string
st.subheader('SalePrice')
#survival_count = df['Survived'].value_counts()
#st.text(f'Survival rate = {survival_count.values[1]/sum(survival_count):.2%}')

# simple plotting
fig, ax = plt.subplots(1, 1, figsize=(15, 5))
#survival_count.plot.bar(ax=ax[0])
df['SalePrice'].plot.hist()#ax=ax[0]
st.pyplot(fig)


st.subheader('Making Prediction jinu')
st.markdown('**Please provide your input below**:')  # you can use markdown like this


# load models
tree_reg = joblib.load('Housing.pickle')

# get inputs
#'LotArea','BldgType','HouseStyle','YearBuilt','FullBath','HalfBath','BedroomAbvGr'
############
###Area of the housing data
dataset = st.selectbox('Area', ['Newark, DE', 'Wilmington, DE', 'Bear, DE', 'Ames, IA'])
############
#BldgType: ['1Fam', '2fmCon', 'Duplex', 'TwnhsE', 'Twnhs']
BldgType = st.selectbox('Building Type', ['Single-family Detached', 'Two-family Conversion; originally built as one-family dwelling', 'Duplex', 'Townhouse End Unit', 'Townhouse Inside Unit'])
############
#HouseStyle: ['1Story',  '1.5Fin', '1.5Unf', '2Story', '2.5Fin','2.5Unf', 'SFoyer', 'SLvl']
HouseStyle = st.selectbox('Building Type', ['One story', 'One and one-half story: 2nd level finished', 'One and one-half story: 2nd level unfinished', 'Two story', 'Two and one-half story: 2nd level finished', 'Two and one-half story: 2nd level unfinished', 'Split Foyer', 'Split Level'])
###
BedroomAbvGr = int(st.number_input('# of Bedrooms', 0, 10, 0))
HalfBath = int(st.number_input('# of Half Bath', 0, 5, 0))
FullBath = int(st.number_input('# of Full Bath', 0, 10, 0))
LotArea = int(st.number_input('Lot Area'))

year_range = range(1850, 2021)
YearBuilt = st.select_slider('Year Built', options = year_range, value = 1970)


# this is how to dynamically change text
prediction_state = st.markdown('calculating...')

housePrice = pd.DataFrame(
   {     
#       'dataset': [dataset],
       'BldgType': [BldgType], 
       'HouseStyle': [HouseStyle],
       'BedroomAbvGr': [BedroomAbvGr],
       'HalfBath': [HalfBath],
       'FullBath': [FullBath],
       'LotArea': [LotArea],
       'YearBuilt': [YearBuilt],
   }
)

y_pred = tree_reg.predict(housePrice)

if y_pred[0] == 0:
    msg = 'This passenger is predicted to be: **died**'
else:
    msg = 'This passenger is predicted to be: **survived**'

prediction_state.markdown(msg)



#age = int(st.number_input('Age:', 0, 120, 20))
#sib_sp = int(st.number_input('# of siblings / spouses aboard:', 0, 10, 0))
#par_ch = int(st.number_input('# of parents / children aboard:', 0, 10, 0))
#pclass = st.selectbox('Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)', [1, 2, 3])
#fare = int(st.number_input('# of parents / children aboard:', 0, 100, 0))
#embarked = st.selectbox('Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)', ['C', 'Q', 'S'])