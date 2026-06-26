from setuptools import setup, find_packages

setup(
    name="used_car_price_prediction",
    version="1.0.0",
    author="Shubham Mane",
    description="End-to-End Used Car Price Prediction using Machine Learning",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "xgboost",
        "joblib"
    ],
    python_requires=">=3.10",
)