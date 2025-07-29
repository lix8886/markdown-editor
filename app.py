import sys
import socket
import subprocess
import streamlit as st
from st_screen_stats import ScreenData
import streamlit.components.v1 as components

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


port = "8080"
host = "localhost" if sys.platform == "win32" else "0.0.0.0"
URL = f"http://{host}:{port}"


def check_port(host, port, timeout=1):
    try:
        socket.setdefaulttimeout(timeout)
        with socket.create_connection((host, port)):
            return True
    except Exception:
        return False


if "__first_check__" not in st.session_state:
    st.session_state["__first_check__"] = True
    
    print(f">>> {URL=}")
    print("正在启动API服务...")
    if not check_port(*URL.split(":")):
        subprocess.Popen(
            ["python", "server.py"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    else:
        print("API服务已启动")


screen_stats = ScreenData(setTimeout=10).st_screen_data()
innerHeight = screen_stats["innerHeight"] - 10
components.iframe(URL, height=innerHeight)
