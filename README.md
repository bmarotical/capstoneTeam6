# Abou

For a bank that originates mortgages, it is necessary to appraise the value of the property before lending the money to the borrower. 
An appraisal is performed during the mortgage loan process so that there is an objective way to assess the house’s market value and ensure that the amount of money requested by the borrower is appropriate. 
This process is important as it reduces the lender’s risk. If the appraised house value is not verified properly, it can expose the lender to undue risk. 
There is a need for mortgage originators to have an efficient and streamlined process to correctly verify appraised house values in order to run a profitable home lending business.

Project Objective:
The objective of this project is to build a machine learning model that can correctly predict the market value of a house for the home lending team to verify the house’s appraised value.

- This repo contains the code for predicting House prices with Advanced Regressions. 
- The housing dataset is taken from kaggle (https://www.kaggle.com/c/house-prices-advanced-regression-techniques) and the Sales Price is inflated using the CPI module.
- RMSE scores of each of the below mentioned regressors are compared and the best model is used to predict the house prices in Newark-DE, Wilmington-DE, Bear-DE and Ames-IA.
- The datasets for Newark-DE, Wilmington-DE, Bear-DE and Ames-IA are downloaded using US Real Estate api from RapidApi (https://rapidapi.com/datascraper/api/us-real-estate/).

- Models Executed
    - Support Vector Regressor
    - Ridge Regressor
    - XG Boost Regressor

## Local Setup

Clone the repo, go to the repo folder, setup the virtual environment, and install the required packages:


```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Run `$ jupyter lab` to go over the notebooks.

## House Prediction App

An app for public access has been created using Streamlit and hosted to cloud using Heroku.

The app can be accessed at [Link]https://housing-demo-team6.herokuapp.com/
