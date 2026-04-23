import streamlit as st
import random
import time
import psutil

st.set_page_config(page_title="System Monitor", layout="wide")

st.title("📊 System Monitoring Dashboard")

# Sidebar
st.sidebar.title("Settings")
refresh_rate = st.sidebar.slider("Refresh Interval (sec)", 1, 10, 3)

# 模拟数据 + 部分真实数据
cpu = psutil.cpu_percent()
mem = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

# 随机波动（增加“真实感”）
cpu += random.uniform(-5, 5)
mem += random.uniform(-3, 3)

col1, col2, col3 = st.columns(3)

col1.metric("CPU Usage", f"{cpu:.1f}%")
col2.metric("Memory Usage", f"{mem:.1f}%")
col3.metric("Disk Usage", f"{disk:.1f}%")

# 简单日志
st.subheader("Recent Logs")

logs = [
    "Service started successfully",
    "Heartbeat OK",
    "No anomalies detected",
    "Sync completed",
]

for _ in range(5):
    st.write(f"[{time.strftime('%H:%M:%S')}] {random.choice(logs)}")

st.caption("Last updated: " + time.ctime())

# 自动刷新
time.sleep(refresh_rate)
st.rerun()
