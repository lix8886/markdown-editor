import psutil
import socket
import subprocess
import streamlit as st
from st_screen_stats import ScreenData
import streamlit.components.v1 as components

from config import PORT


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
    ._container_gzau3_1 {
        display: none !important;
    }
    ._profileContainer_gzau3_53 {
        display: none !important;
    }
</style>
"""
)


def check_port(host, port, timeout=1):
    try:
        socket.setdefaulttimeout(timeout)
        with socket.create_connection((host, port)):
            return True
    except Exception:
        return False


def get_ip():
    """获取当前主机的非回环 IP 地址"""
    ip_list = []
    for iface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET and not addr.address.startswith("127."):
                ip_list.append(addr.address)
    return ip_list


HOST = get_ip()[0]
URL = f"http://{HOST}:{PORT}"

if "__first_server__" not in st.session_state:
    st.session_state["__first_server__"] = True

    print(f"正在检查API服务（{URL=}）...")
    if not check_port(HOST, PORT):
        subprocess.Popen(
            ["python", "server.py"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print(f"API服务启动成功{URL=}")
        st.toast(f"API服务启动成功{URL=}")
    else:
        print(f"API服务已启动{URL=}")
        st.toast(f"API服务已启动{URL=}")


screen_stats = ScreenData(setTimeout=10).st_screen_data()
innerHeight = screen_stats["innerHeight"] - 10
components.iframe(URL, height=innerHeight)
