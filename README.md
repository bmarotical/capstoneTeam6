# About

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

The app can be accessed at https://housing-demo-team6.herokuapp.com/
