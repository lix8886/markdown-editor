#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的HTTP服务器，用于测试Markdown编辑器
"""

import os
import sys
import http.server
import socketserver


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)

    def end_headers(self):
        # 添加CORS头，允许跨域请求
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        # 处理预检请求
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        # 自定义日志格式
        print(f"[{self.log_date_time_string()}] {format % args}")


def main():
    port = 8080

    # 检查端口是否可用
    try:
        with socketserver.TCPServer(("", port), CustomHTTPRequestHandler) as httpd:
            print(f"服务器启动在 http://localhost:{port}")
            print(f"当前工作目录: {os.getcwd()}")
            print("按 Ctrl+C 停止服务器")
            print("-" * 50)

            # 列出当前目录的文件
            print("当前目录文件:")
            for file in os.listdir("."):
                if os.path.isfile(file):
                    print(f"  📄 {file}")
                else:
                    print(f"  📁 {file}/")
            print("-" * 50)

            httpd.serve_forever()
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"错误: 端口 {port} 已被占用")
            print("请尝试使用其他端口或关闭占用该端口的程序")
        else:
            print(f"启动服务器时出错: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n服务器已停止")


if __name__ == "__main__":
    main()
