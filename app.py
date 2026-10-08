import streamlit as st

st.set_page_config(
    page_title="Medical Appointment Analytics",
    layout="wide"
)

st.title("🏥 Medical Appointment No-Show Prediction & Demand Forecasting")

tab1, tab2 = st.tabs(
    ["No-Show Prediction", "Demand Forecasting"]
)

with tab1:

    st.header("Patient No-Show Risk Prediction")

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=100,
        value=30
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    appointment_shift = st.selectbox(
        "Appointment Shift",
        ["Morning", "Afternoon", "Evening"]
    )

    if st.button("Predict No-Show Risk"):
        st.success("Prediction Generated Successfully")
        st.info("This is a demo interface. Connect your saved model for live prediction.")

with tab2:

    st.header("Appointment Demand Forecasting")

    days = st.slider(
        "Forecast Days",
        1,
        30,
        7
    )

    if st.button("Generate Forecast"):
        st.success("Forecast Generated Successfully")
        st.info("This is a demo forecast interface.")
