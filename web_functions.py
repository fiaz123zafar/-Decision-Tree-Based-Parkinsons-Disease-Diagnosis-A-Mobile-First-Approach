# Import necessary modules
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st

@st.cache_data
def load_data():
    """This function returns the preprocessed data"""

    # Load the Parkinson's dataset into DataFrame
    df = pd.read_csv('Parkinson.csv')

    # Rename the column names in the DataFrame
    df.rename(columns={"MDVP:Fo(Hz)": "AVFF",
                       "MDVP:Fhi(Hz)": "MAVFF",
                       "MDVP:Flo(Hz)": "MIVFF"}, inplace=True)

    # Perform feature and target split
    X = df[["AVFF", "MAVFF", "MIVFF", "Jitter:DDP", "MDVP:Jitter(%)", "MDVP:RAP", 
            "MDVP:APQ", "MDVP:PPQ", "MDVP:Shimmer", "Shimmer:DDA", "Shimmer:APQ3", 
            "Shimmer:APQ5", "NHR", "HNR", "RPDE", "DFA", "D2", "PPE"]]
    y = df['status']

    return df, X, y

@st.cache_resource
def train_model(X, y):
    """This function trains the model and returns the model and model score"""

    # Ensure y is a mutable array
    y = np.array(y, copy=True)

    # Create the model
    model = DecisionTreeClassifier(
        ccp_alpha=0.0, class_weight=None, criterion='entropy',
        max_depth=4, max_features=None, max_leaf_nodes=None,
        min_impurity_decrease=0.0, min_samples_leaf=1,
        min_samples_split=2, min_weight_fraction_leaf=0.0,
        random_state=42, splitter='best'
    )

    # Fit the data on model
    model.fit(X, y)

    # Get the model score
    score = model.score(X, y)

    # Return the values
    return model, score

def predict(X, y, features):
    """This function uses the model to make a prediction based on input features"""

    # Get model and model score
    model, score = train_model(X, y)

    # Convert features to a numpy array and ensure correct shape
    features = np.array(features).reshape(1, -1)

    # Predict the value
    prediction = model.predict(features)

    return prediction, score
