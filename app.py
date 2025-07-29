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

PORT = 8080
HOST = "localhost" if sys.platform == "win32" else "0.0.0.0"
URL = f"http://{HOST}:{PORT}"


def check_port(host=HOST, port=PORT, timeout=1):
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
    if not check_port():
        subprocess.Popen(
            ["python", "server.py"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    else:
        print("API服务已启动")

    import socket
    import psutil

    def get_ip():
        """获取当前主机的非回环 IP 地址"""
        ip_list = []
        for iface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == socket.AF_INET and not addr.address.startswith(
                    "127."
                ):
                    ip_list.append(addr.address)
        return ip_list

    def scan_open_ports(host="localhost", port_start=1024, port_end=1100):
        """扫描指定范围内可用（未占用）的端口"""
        available_ports = []
        for port in range(port_start, port_end + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.2)
                try:
                    s.bind((host, port))
                    available_ports.append(port)
                except OSError:
                    continue  # 端口被占用
        return available_ports

    ips = get_ip()
    print("本机 IP 地址：", ips)
    if check_port(ips[0], 8080, timeout=3):
        print("8080 可访问")
    else:
        print("8080 不可访问")
    host = ips[0] if ips else "0.0.0.0"
    ports = scan_open_ports(host, 8000, 89000)
    print(f"{host} 可用端口（8000-8050 范围）有：", ports)


screen_stats = ScreenData(setTimeout=10).st_screen_data()
innerHeight = screen_stats["innerHeight"] - 10
components.iframe(URL, height=innerHeight)
