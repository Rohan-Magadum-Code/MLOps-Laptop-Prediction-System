import streamlit as st
import pandas as pd

from app import PredictionPipeline

st.set_page_config(
    page_title="Laptop Price Prediction",
    page_icon="💻",
    layout="wide"
)

pipeline = PredictionPipeline()

options = pipeline.get_dropdown_options()

company_list = options["Company"]
type_list = options["TypeName"]
cpu_name_list = options["Cpu Name"]
cpu_brand_list = options["Cpu brand"]
gpu_list = options["Gpu Brand"]
os_list = options["OS"]

st.title("💻 Laptop Price Prediction")

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:

        company = st.selectbox(
            "Company",
            company_list
        )

        laptop_type = st.selectbox(
            "Laptop Type",
            type_list
        )

        inches = st.number_input(
            "Screen Size (Inches)",
            min_value=10.0,
            max_value=20.0,
            value=15.6
        )

        ram = st.selectbox(
            "RAM (GB)",
            [2, 4, 8, 16, 32, 64]
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=0.5,
            max_value=5.0,
            value=2.0
        )

        touchscreen = st.selectbox(
            "Touchscreen",
            [0, 1]
        )

        ips = st.selectbox(
            "IPS Display",
            [0, 1]
        )

        ppi = st.number_input(
            "PPI",
            min_value=50.0,
            max_value=500.0,
            value=141.0
        )

    with col2:

        cpu_name = st.selectbox(
            "CPU Name",
            cpu_name_list
        )

        cpu_speed = st.number_input(
            "CPU Speed (GHz)",
            min_value=1.0,
            max_value=5.0,
            value=2.5
        )

        cpu_brand = st.selectbox(
            "CPU Brand",
            cpu_brand_list
        )

        ssd = st.number_input(
            "SSD (GB)",
            min_value=0,
            max_value=4096,
            value=256
        )

        tb_hdd = st.number_input(
            "HDD (TB)",
            min_value=0,
            max_value=4,
            value=0
        )

        tb_hybrid = st.number_input(
            "Hybrid Storage (TB)",
            min_value=0,
            max_value=4,
            value=0
        )

        flash_storage = st.number_input(
            "Flash Storage (GB)",
            min_value=0,
            max_value=512,
            value=0
        )

        gpu = st.selectbox(
            "GPU Brand",
            gpu_list
        )

        operating_system = st.selectbox(
            "Operating System",
            os_list
        )

    submit = st.form_submit_button("🔍 Predict Price")

if submit:

    input_df = pd.DataFrame({

        "Company": [company],
        "TypeName": [laptop_type],
        "Inches": [inches],
        "Ram (GB)": [ram],
        "Weight": [weight],
        "Touchscreen": [touchscreen],
        "IPS": [ips],
        "ppi": [ppi],
        "Cpu Name": [cpu_name],
        "Cpu Speed (GHz)": [cpu_speed],
        "Cpu brand": [cpu_brand],
        "SSD": [ssd],
        "TB HDD": [tb_hdd],
        "TB Hybrid": [tb_hybrid],
        "Flash Storage": [flash_storage],
        "Gpu Brand": [gpu],
        "OS": [operating_system]

    })

    prediction = pipeline.predict(input_df)

    st.success(
        f"💰 Predicted Laptop Price: ₹ {prediction[0]:,.2f}"
    )