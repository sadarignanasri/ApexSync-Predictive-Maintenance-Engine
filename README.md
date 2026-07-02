# ApexSync-Predictive-Maintenance-Engine
# ApexSync: Industrial IoT Predictive Maintenance Engine

ApexSync is an end-to-end Data Science and Business Intelligence solution designed to process high-frequency industrial IoT sensor streams and predict equipment failure using unsupervised Machine Learning.

## 📁 Executive Reporting & Governance
📥 **[Download the Full ApexSync Executive BI Report (PDF)](ApexSync_Executive_Report.pdf)**

*The full interactive data control center was exported directly into an enterprise-ready executive brief for cross-department engineering reviews.*

## 🛠️ Tech Stack & Competencies
- **Frontend/UI:** Python (Streamlit, Seaborn, Matplotlib)
- **Machine Learning:** Scikit-Learn (Isolation Forest for Unsupervised Anomaly Detection)
- **Database Architecture:** SQL / SQLite (Window Functions, CTEs, Multi-table Joins)
- **Data Engineering:** Time-series simulation with micro-batch streaming mechanics

## 🧠 Data Science Architecture
Rather than relying on rigid, hardcoded thresholds (such as assuming a machine is broken if its temperature simply crosses an arbitrary number), this engine utilizes an **Isolation Forest** classifier. 

Because different industrial equipment lines maintain entirely different base thermodynamics (e.g., High-Speed Turbines naturally run hot at ~75.1°C, while CNC Milling Machines run much cooler at ~50.1°C), the model dynamically isolates multidimensional structural anomalies across concurrent thermal and vibration features.

## 📈 Key SQL Analytics Applied
- Constructed a continuous **3-hour rolling average temperature** baseline per machine using SQL window functions (`ROWS BETWEEN 2 PRECEDING AND CURRENT ROW`) to eliminate baseline data noise.
- Aggregated raw multi-source streams into an executive data view to instantly track floor-level performance and compute aggregate uptime health.

## 🎯 Operational Insights & Business Impact
- **Risk Zone Isolation:** Floor A was flagged as the highest critical hazard zone, generating 30 unique system anomalies across high-speed turbines and compressors.
- **High Operational Efficiency:** Maintained a global **99.8% System Health Index (Uptime SLA)** over 36,000 cumulative monitored operating hours.
