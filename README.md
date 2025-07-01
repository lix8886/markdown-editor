# Markdown 排版公众号文章

## 预览

https://gitee.com/lx__8866/markdown-editor/blob/main/assets/demo.gif

![image](https://gitee.com/lx__8866/markdown-editor/blob/main/assets/demo.gif)

## 使用方法

### 方法 1：使用 Python HTTP 服务器（推荐）

1. 确保已安装 Python 3
2. 在项目目录下运行：

   ```bash
   python server.py
   ```

   > win 系统最简单的方法：直接双击 `startup.bat`

3. 打开浏览器访问：`http://localhost:8080`

### 方法 2：使用其他 HTTP 服务器

#### Node.js (http-server)

```bash
npx http-server -p 8080
```

#### PHP

```bash
php -S localhost:8080
```

#### Python 3 (内置)

```bash
python -m http.server 8080
```

### 方法 3：使用 Live Server (VS Code 扩展)

1. 在 VS Code 中安装 Live Server 扩展
2. 右键点击 `index.html` 文件
3. 选择 "Open with Live Server"

## 文件说明

- `index.html` - 主页面文件
- `server.py` - 简单的 Python HTTP 服务器
- `README.md` - 本说明文件
