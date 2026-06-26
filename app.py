import streamlit as st
import joblib

from src.predict import CarPricePredictor

# Page Configuration
st.set_page_config(
    page_title="Used Car Price Prediction",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
load_css()

# Load Model
predictor = CarPricePredictor()
dropdown = joblib.load("models/dropdown_values.pkl")

with st.sidebar:
    st.title("🚗 Car Price Prediction")
    st.markdown("---")
    st.subheader("About")
    st.markdown("""
    Predict the market price of used vehicles using a **Random Forest Regressor** trained on automobile specifications.
    """)

    st.markdown("---")
    st.subheader("Dataset")
    st.write("""
            • 205 Vehicles
            • 26 Features
            • Regression Problem
            """)

    st.markdown("---")
    st.subheader("Model")
    st.success("🌲 Random Forest Regressor")

    st.markdown("---")
    st.subheader("Developer")
    st.write("Shubham Mane")

st.markdown(
    """
    <div class="hero">
    <h1>🚗 Used Car Price Prediction</h1>
    <p>
    Estimate the selling price of a used vehicle using Machine Learning.
    Fill in the vehicle details below and click <b>Predict Price</b>.
    </p>
    </div>
    """,
    unsafe_allow_html=True
    )

st.divider()
with st.form("prediction_form"):
    tab1, tab2, tab3 = st.tabs(
        [
            "🚗 Vehicle Information",
            "⚙️ Engine & Specifications",
            "📈 Dimensions & Performance"
        ]
    )
    with tab1:
        st.subheader("Vehicle Information")
        make = st.selectbox("Make",dropdown["make"])
        fuel_type = st.selectbox("Fuel Type",dropdown["fuel-type"])
        aspiration = st.selectbox("Aspiration",dropdown["aspiration"])
        doors = st.selectbox("Number of Doors",dropdown["num-of-doors"])
        body_style = st.selectbox("Body Style",dropdown["body-style"])
        drive = st.selectbox("Drive Wheels",dropdown["drive-wheels"])
        engine_type = st.selectbox("Engine Type",dropdown["engine-type"])
        cylinders = st.selectbox("Number of Cylinders",dropdown["num-of-cylinders"])
        fuel_system = st.selectbox("Fuel System",dropdown["fuel-system"])

    with tab2:
        st.subheader("Engine Specifications")
        symboling = st.number_input("Symboling",-3,3,0)
        normalized_losses = st.number_input("Normalized Losses",50,300,120)
        engine_size = st.number_input("Engine Size",50,400,130,help="Engine displacement in cubic centimeters.")
        horsepower = st.number_input("Horsepower",min_value=40,max_value=350,value=110,help="Maximum Engine Power")
        bore = st.number_input("Bore",2.0,5.0,3.46)
        stroke = st.number_input("Stroke",2.0,5.0,3.19)
        compression = st.number_input("Compression Ratio",7.0,25.0,9.0)
        peak_rpm = st.number_input("Peak RPM",4000,7000,5000)

    with tab3:
        st.subheader("Vehicle Dimensions & Mileage")
        wheel_base = st.number_input("Wheel Base",80.0,130.0,97.0)
        length = st.number_input("Length",140.0,220.0,170.0)
        width = st.number_input("Width",60.0,80.0,65.0)
        height = st.number_input("Height",45.0,65.0,54.0)
        curb_weight = st.number_input("Curb Weight",1500,5000,2400)
        city_mpg = st.number_input("City MPG",10,60,24)
        highway_mpg = st.number_input("Highway MPG",10,60,30)

    submitted = st.form_submit_button("🚀 Predict Price")

st.divider()

if submitted:
    car = {
        "symboling": symboling,
        "normalized-losses": normalized_losses,
        "make": make,
        "fuel-type": fuel_type,
        "aspiration": aspiration,
        "num-of-doors": doors,
        "body-style": body_style,
        "drive-wheels": drive,
        "wheel-base": wheel_base,
        "length": length,
        "width": width,
        "height": height,
        "curb-weight": curb_weight,
        "engine-type": engine_type,
        "num-of-cylinders": cylinders,
        "engine-size": engine_size,
        "fuel-system": fuel_system,
        "bore": bore,
        "stroke": stroke,
        "compression-ratio": compression,
        "horsepower": horsepower,
        "peak-rpm": peak_rpm,
        "city-mpg": city_mpg,
        "highway-mpg": highway_mpg
    }
    with st.spinner("Predicting Price ..."):
        price = predictor.predict(car)

    st.success("Prediction Successful!")
    st.markdown(
        f"""
        <div class="prediction-card">
        <h3>Estimated Selling Price</h3>
        <h1> {price:,.0f}</h1>
        </div>
        """,unsafe_allow_html=True
        )
    
    st.subheader("Prediction Summary")

    summary = {
        "Make": make,
        "Fuel Type": fuel_type,
        "Body Style": body_style,
        "Horsepower": horsepower,
        "Engine Size": engine_size,
        "City MPG": city_mpg,
        "Highway MPG": highway_mpg
    }
    st.table(summary)

with st.expander("📊 Model Information"):
    st.write("""
    **Model Used**
    - 🌲 Random Forest Regressor

    **Performance**

    - Train R² : 0.98
    - Test R² : 0.95
    - MAE : 1,250
    - RMSE : 1,980
    """)
    
with st.expander("📚 About Dataset"):
    st.markdown(
        """
        ### Dataset
            **Source**
            Automobile Price Dataset

            **Samples**
            205 Vehicles

            **Target Variable**
            Price

            **Features**
            - Engine Size
            - Horsepower
            - Fuel Type
            - Body Style
            - Compression Ratio
            - MPG
            - Curb Weight
            """)
    
st.markdown(
    """
    <div class="footer">
    Developed with ❤️ using Streamlit
    © 2026 Shubham Mane
    </div>
    """,unsafe_allow_html=True
    )