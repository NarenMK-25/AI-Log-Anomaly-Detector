import streamlit as st
import time
import os

st.set_page_config(page_title="System Monitor", page_icon="🛡️")

st.title("🛡️ AI Log Anomaly Detection System")
st.markdown("Live monitoring dashboard for Docker container health.")

while True:
    st.subheader("Latest System Logs")

    # Display the last 10 log entries
    if os.path.exists("logs.txt"):
        with open("logs.txt") as f:
            logs = f.readlines()[-10:]
        
        # Format logs for better UI reading
        formatted_logs = ""
        for log in logs:
            if "ERROR" in log:
                formatted_logs += f"🔴 {log}"
            else:
                formatted_logs += f"🟢 {log}"
                
        st.text(formatted_logs)
    else:
        st.info("Waiting for logs to be generated...")

    st.subheader("System Status")
    # Check if an anomaly alert exists
    if os.path.exists("alert.txt"):
        st.error("⚠️ Anomaly Detected! Auto-Healing Triggered...")
    else:
        st.success("✅ System Normal. No anomalies detected.")

    # Refresh the UI every 3 seconds
    time.sleep(3)
    st.rerun()
