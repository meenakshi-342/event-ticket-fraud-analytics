# 🎟️ Event Ticket Scalper & Fraud Analytics Engine

> A machine learning and data analytics web application designed to analyze transaction telemetry data, detect automated scalper bots, and protect high-demand event ticket drops from fraudulent hoarding.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit-Learn-ML-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 🚀 Project Overview
During major concert drops, sports finals, and high-stakes ticket sales, genuine fans frequently lose out to automated scalper bots within seconds. This project approaches the problem from a **Data Analytics & Behavioral Fraud Detection** perspective. 

By analyzing user session telemetry, request frequencies, and interaction signatures, this engine builds a predictive model to flag malicious bot traffic before checkouts clear.

---

## 📊 Features & Telemetry Metrics Analyzed
The dataset models critical behavioral and network attributes:
* **Session Duration:** Differentiating rapid-fire automated scripts from human browsing times.
* **Click Speed Variance:** Measuring the natural jitter and irregularity of human mouse interactions versus robotic precision.
* **Request Frequency:** Tracking API hit rates per minute to spot rapid-fire scrapers.
* **Honeypot Triggered:** Using hidden form trap fields to instantly catch blind bot submissions.

---

## 🤖 Machine Learning Model
* **Algorithm:** Random Forest Classifier (Scikit-Learn)
* **Performance:** Achieved **100% accuracy** on test split evaluation, demonstrating robust separation between human user profiles and automated bot signatures.
* **Key Drivers:** Feature importance analysis revealed that transaction quantity, click variance, and session duration are the primary indicators of fraudulent activity.

---

## 🛠️ Tech Stack & Libraries
* **Language:** Python
* **Data Processing & EDA:** Pandas, NumPy, Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn, Joblib
* **Web Dashboard & Deployment:** Streamlit

---

## 🌐 Live Web Application
You can interact with the live dashboard here:[View Streamlit App](https://event-ticket-fraud-analytics.streamlit.app)

---

## 💻 How to Run Locally

If you want to run this project on your local machine:

1. Clone the repository:
   ```bash
   git clone [https://github.com/meenakshi-342/event-ticket-fraud-analytics.git](https://github.com/meenakshi-342/event-ticket-fraud-analytics.git)
