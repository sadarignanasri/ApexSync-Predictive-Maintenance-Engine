import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="ApexSync Dashboard", layout="wide")
st.title("🏭 ApexSync: Industrial IoT Predictive Maintenance Control Center")
st.markdown("Real-time telemetry analysis and machine learning anomaly monitoring.")

# Load the data we prepared in Phase 4
df = pd.read_csv("executive_machinery_summary.csv")

# Explicitly convert relevant columns to numeric types to prevent potential TypeErrors
df['total_monitored_hours'] = pd.to_numeric(df['total_monitored_hours'], errors='coerce')
df['total_anomalies_detected'] = pd.to_numeric(df['total_anomalies_detected'], errors='coerce')
df['running_avg_temperature'] = pd.to_numeric(df['running_avg_temperature'], errors='coerce')

# Drop any rows where conversion might have failed (though previous check indicates no NaNs)
df.dropna(subset=['total_monitored_hours', 'total_anomalies_detected', 'running_avg_temperature'], inplace=True)


# Metrics Display Row
col1, col2, col3 = st.columns(3)
col1.metric("Total Monitored Hours", f"{df['total_monitored_hours'].sum():,}")
col2.metric("Total Anomalies Detected", f"{df['total_anomalies_detected'].sum()}")
col3.metric("System Health Index", f"{round((1 - (df['total_anomalies_detected'].sum() / df['total_monitored_hours'].sum())) * 100, 2)}%")

st.markdown("---")

# Visualizations Row
left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("⚠️ Anomalies Detected by Factory Floor")
    fig, ax = plt.subplots()
    floor_data = df.groupby("factory_floor")["total_anomalies_detected"].sum().reset_index()
    # Fix for Seaborn FutureWarning: Pass `x` to `hue` and set `legend=False`
    sns.barplot(data=floor_data, x="factory_floor", y="total_anomalies_detected", hue="factory_floor", legend=False, palette="Oranges_r", ax=ax)
    st.pyplot(fig)

with right_chart:
    st.subheader("🌡️ Running Average Temperature by Machine Type")
    fig, ax = plt.subplots()
    # Using pivot_table for robustness in case of unexpected data structure
    heatmap_data = df.pivot_table(index="machine_type", columns="factory_floor", values="running_avg_temperature")
    sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlOrRd", ax=ax)
    st.pyplot(fig)

# Data Table Display
st.subheader("📋 Raw Analytical Data Layer")
# Fix for Streamlit deprecation warning: Replace `use_container_width=True` with `width='stretch'`
st.dataframe(df, width='stretch')
