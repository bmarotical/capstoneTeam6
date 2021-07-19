# About

This repo contains the code for predicting House prices with Prediction Project. 
The housing dataset is taken from kaggle (https://www.kaggle.com/c/house-prices-advanced-regression-techniques) and price adjusted using the CPI module.
RMSE scores of each of the below regressors are compared and the best model is used to predict the house prices in Newark-DE, Wilmington-DE, Bear-DE and Ames-IA.

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
