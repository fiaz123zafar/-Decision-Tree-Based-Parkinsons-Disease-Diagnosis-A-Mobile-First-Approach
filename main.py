"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web_functions import load_data

# Configure the app
st.set_page_config(
    page_title="Parkinson's Disease Prediction",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import pages
from Tabs import home, data, predict, visualise



# Dictionary for pages
Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    "Visualisation": visualise
    
}

# Custom CSS for styling the sidebar
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
        }
        .sidebar .sidebar-content h2 {
            color: #4CAF50;
            font-size: 24px;
        }
        .sidebar .sidebar-content .radio-option {
            font-size: 18px;
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #e0e0e0;
            border-radius: 5px;
            transition: all 0.3s ease;
        }
        .sidebar .sidebar-content .radio-option:hover {
            background-color: #4CAF50;
            color: #fff;
            cursor: pointer;
        }
        .sidebar .sidebar-content .radio-option input {
            display: none;
        }
        .sidebar .sidebar-content .radio-option label {
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# Add title to sidebar
st.sidebar.title("Navigation")

# Create radio options with styling
page = st.sidebar.radio("Pages", list(Tabs.keys()), format_func=lambda x: f"📄 {x}")

# Loading the dataset
df, X, y = load_data()

# Call the app function of selected page to run
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df, X, y)
elif page == "Data Info":
    Tabs[page].app(df)
else:
    Tabs[page].app()