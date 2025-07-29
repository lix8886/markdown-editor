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
    .data-testid="manage-app-button" {
        display:none;
    }
    ._container_gzau3_1 {
        display: none;
    }
    ._profileContainer_gzau3_53 {
        display: none;
    }
</style>
"""
)

screen_stats = ScreenData(setTimeout=10).st_screen_data()
innerHeight = screen_stats["innerHeight"] - 10
components.iframe('https://markdown.com.cn/editor/', height=innerHeight)
