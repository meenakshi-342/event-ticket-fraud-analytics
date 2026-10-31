import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(page_title="Event Ticket Fraud Analytics", page_icon="🎟️", layout="wide")

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load('ticket_fraud_model.pkl')

model = load_model()

# App Header
st.title("🎟️ Event Ticket Scalper & Fraud Analytics Engine")
st.markdown("Analyze transaction telemetry data in real-time to detect automated scalper bots during high-demand event drops.")

# Sidebar Controls for User Simulation
st.sidebar.header("🔍 Transaction Telemetry Input")
session_duration = st.sidebar.slider("Session Duration (seconds)", 0.1, 150.0, 45.0)
click_speed_var = st.sidebar.slider("Click Speed Variance", 0.0, 180.0, 50.0)
request_freq = st.sidebar.slider("Requests per Minute", 1, 100, 10)
ticket_qty = st.sidebar.selectbox("Ticket Quantity Attempted", [1, 2, 4, 6, 10])
honeypot = st.sidebar.selectbox("Honeypot Field Triggered?", [0, 1], format_func=lambda x: "Yes (Bot Sign)" if x == 1 else "No (Clean)")

# Input Dataframe
input_data = pd.DataFrame({
    'session_duration_sec': [session_duration],
    'click_speed_variance': [click_speed_var],
    'request_frequency_per_min': [request_freq],
    'ticket_quantity': [ticket_qty],
    'honeypot_triggered': [honeypot]
})

# Prediction Button & Output
st.subheader("📊 Real-Time Risk Analysis")
if st.button("Analyze Transaction Session"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]
    
    col1, col2 = st.columns(2)
    
    with col1:
        if prediction == 1:
            st.error("### 🚨 HIGH RISK: Scalper Bot Detected!")
            st.markdown(f"**Bot Probability:** `{probability[1]*100:.2f}%`")
            st.markdown("Action: Transaction blocked and flagged for manual security review.")
        else:
            st.success("### ✅ LOW RISK: Legitimate Fan Verified")
            st.markdown(f"**Legitimate Probability:** `{probability[0]*100:.2f}%`")
            st.markdown("Action: Transaction cleared for secure checkout.")
            
    with col2:
        st.markdown("### 📋 Session Telemetry Profile")
        st.dataframe(input_data, use_container_width=True)
