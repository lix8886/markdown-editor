import subprocess
import streamlit as st
from st_screen_stats import ScreenData
import streamlit.components.v1 as components
from streamlit_server_state import server_state, server_state_lock

st.set_page_config(
    page_title="Markdown Editor",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 清空 streamlit 所有原始页面信息
st.html(
    """
<style>
    .stAppToolbar {
        display: none;
        height: 0 !important;
    }
    .stAppHeader {
        min-height:0;
        height: 0 !important;
    }
    .stMainBlockContainer  {
        margin: 0 !important;
        padding: 0 !important;
    }
    .stAppViewContainer {
        padding: 0 !important;
    }
    .stBottomBlockContainer {
        padding: 0 !important;
    }
    .stDecoration {
        height: 0;
    }
    .stMainBlockContainer {
        padding: 0;
    }
    .stVerticalBlock {
        gap: 0 !important;
    }
    .st-key-screen_stats {
        height: 0 !important;
    }
</style>
"""
)

# 全局标识
with server_state_lock["api_lanuch"]:
    if "api_lanuch" not in server_state:
        server_state.api_lanuch = True
        print("启动API服务...")
        subprocess.Popen(
            ["python", "server.py"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )


screen_stats = ScreenData(setTimeout=10).st_screen_data()
innerHeight = screen_stats["innerHeight"] - 10
host = st.context.headers["host"].split(":")[0]
port = 8080
url = f"{host}:{port}"
print(f'>>> {url=}')

import socket
def check_port(host, port, timeout=2):
    try:
        socket.setdefaulttimeout(timeout)
        with socket.create_connection((host, port)):
            return True
    except Exception:
        return False

if st.button('check'):
    st.write(f'{url} 访问情况：{check_port(host, port)}')

components.iframe(url, height=innerHeight)
