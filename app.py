import streamlit as st
import subprocess
import os
import time

st.title("System Status Dashboard")

# 防止重复启动 agent
if "started" not in st.session_state:
    st.session_state.started = True

    # 后台启动（兜底）
    subprocess.Popen([
        "./komari-agent",
        "-e", "https://agent.0-5.art",
        "-t", "YR3y8NXdWH7FkUbuzgiy6c"
    ])

st.write("Service running...")
st.write("Time:", time.ctime())
