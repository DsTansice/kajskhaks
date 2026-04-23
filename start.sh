#!/bin/bash

chmod +x ./komari-agent

# 启动 Komari Agent（替换成你的参数）
./komari-agent \
  -e https://agent.0-5.art \
  -t YR3y8NXdWH7FkUbuzgiy6c 

# 启动 Streamlit（前台必须有东西）
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
