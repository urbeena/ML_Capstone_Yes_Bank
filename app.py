import streamlit as st
import pandas as pd
from Yes_Bank.pipeline.training_pipeline import TrainingPipeline
from Yes_Bank.exception.exception import YesBankException
import sys
from Yes_Bank.utils.ml_utils.estimator import YesBankModel
from Yes_Bank.utils.main_utils.utils import load_object

st.set_page_config(page_title="Yes Bank Stock Prediction", layout="centered")

st.title("📈 Yes Bank Stock Price Prediction")

st.markdown("---")

# =========================
# TRAINING SECTION
# =========================
st.header("🔧 Model Training")

if st.button("Train Model"):
    try:
        with st.spinner("Training model... Please wait ⏳"):
            training_pipeline = TrainingPipeline()
            training_pipeline.run_pipeline()
        st.success("✅ Model trained and saved successfully!")

    except Exception as e:
        st.error("❌ Training failed")
        raise YesBankException(e, sys)

st.markdown("---")

# =========================
# PREDICTION SECTION
# =========================
st.header("🔮 Make Prediction")

open_price = st.number_input("Open Price", min_value=0.0, step=1.0)
high_price = st.number_input("High Price", min_value=0.0, step=1.0)
low_price = st.number_input("Low Price", min_value=0.0, step=1.0)
month = st.number_input("Month", min_value=1, max_value=12, step=1)
year = st.number_input("Year", min_value=2000, max_value=2100, step=1)


if st.button("Predict"):
    try:
        preprocessor = load_object("final_model/preprocessor.pkl")
        model = load_object("final_model/model.pkl")
        prediction_pipeline = YesBankModel(preprocessor=preprocessor, model=model)
        input_df = pd.DataFrame([{
                                    "Open": open_price,
                                    "High": high_price,
                                    "Low": low_price,
                                    "Month": month,
                                    "Year": year
                                }])


        prediction = prediction_pipeline.predict(input_df)


        st.success(f"📊 Predicted Stock Price: **{prediction[0]}**")


    except Exception as e:
        st.error("❌ Prediction failed")
        raise YesBankException(e, sys)
