"""
LocWarp 一键启动器
双击此文件即可启动 LocWarp
"""

import subprocess
import sys
import os
import time
import shutil
import webbrowser
import urllib.request
import socket

# 路径设置
ROOT = os.path.dirname(os.path.abspath(__file__))
BACKEND = os.path.join(ROOT, "backend")
FRONTEND = os.path.join(ROOT, "frontend")

BACKEND_PORT = 8777
FRONTEND_PORT = 5173

procs = []


def print_banner():
    print()
    print("  ╔══════════════════════════════════════════╗")
    print("  ║   LocWarp — iOS 虚拟定位模拟器 v0.1     ║")
    print("  ╚══════════════════════════════════════════╝")
    print()


def check_tool(name, hint):
    if shutil.which(name):
        print(f"  [✓] 已找到 {name}")
        return True
    else:
        print(f"  [✗] 找不到 {name}，请先安装：{hint}")
        return False


def is_port_open(port):
    """检查 port 是否有服务在监听"""
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=1):
            return True
    except (ConnectionRefusedError, OSError, TimeoutError):
        return False


def kill_port(port):
    """清理占用指定 port 的进程"""
    if os.name == "nt":
        result = subprocess.run(
            f'netstat -ano | findstr ":{port}" | findstr "LISTENING"',
            capture_output=True, text=True, shell=True,
        )
        for line in result.stdout.strip().splitlines():
            parts = line.split()
            if parts:
                pid = parts[-1]
                subprocess.run(f"taskkill /pid {pid} /f",
                               shell=True, capture_output=True)


def wait_for_port(port, label, timeout=60):
    print(f"      等待{label}启动中", end="", flush=True)
    start = time.time()
    while time.time() - start < timeout:
        if is_port_open(port):
            print(" OK ✓")
            return True
        print(".", end="", flush=True)
        time.sleep(2)
    print(" 超时！")
    return False


def install_backend():
    print("  [1/4] 检查后端依赖...", end=" ", flush=True)
    req = os.path.join(BACKEND, "requirements.txt")

    dry = subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", req, "--dry-run", "-q"],
        capture_output=True, text=True,
    )

    if "would install" not in dry.stdout.lower():
        print("已就绪 ✓")
    else:
        print("安装中...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", req, "-q"],
            cwd=BACKEND,
        )
        print("        完成 ✓")


def install_frontend():
    print("  [2/4] 检查前端依赖...", end=" ", flush=True)
    nm = os.path.join(FRONTEND, "node_modules")
    if os.path.isdir(nm):
        print("已就绪 ✓")
    else:
        print("安装中...")
        subprocess.run(["npm", "install"], cwd=FRONTEND, shell=True)
        print("        完成 ✓")


def start_backend():
    print(f"  [3/4] 启动后端服务 (port {BACKEND_PORT})...")

    # 清理残留
    if is_port_open(BACKEND_PORT):
        print(f"      Port {BACKEND_PORT} 被占用，清理中...")
        kill_port(BACKEND_PORT)
        time.sleep(1)

    p = subprocess.Popen(
        [sys.executable, "main.py"],
        cwd=BACKEND,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0,
    )
    procs.append(p)
    return wait_for_port(BACKEND_PORT, "后端")


def start_frontend():
    print(f"  [4/4] 启动前端服务 (port {FRONTEND_PORT})...")

    # 清理残留
    if is_port_open(FRONTEND_PORT):
        print(f"      Port {FRONTEND_PORT} 被占用，清理中...")
        kill_port(FRONTEND_PORT)
        time.sleep(1)

    # 用 --port 强制指定 port，避免 Vite 跳到其他 port
    p = subprocess.Popen(
        ["npx", "vite", "--host", "--port", str(FRONTEND_PORT), "--strictPort"],
        cwd=FRONTEND,
        shell=True,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == "nt" else 0,
    )
    procs.append(p)
    return wait_for_port(FRONTEND_PORT, "前端")


def cleanup():
    print("\n  正在关闭所有服务...")
    for p in procs:
        try:
            p.terminate()
            p.wait(timeout=5)
        except Exception:
            try:
                p.kill()
            except Exception:
                pass
    # 强制清理残留 port
    kill_port(BACKEND_PORT)
    kill_port(FRONTEND_PORT)
    print("  已停止。再见！")


def check_admin():
    """Check if running with administrator privileges."""
    import ctypes
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def main():
    os.system("title LocWarp")
    print_banner()

    # 检查管理员权限 (iOS 17+ 需要)
    if os.name == "nt" and not check_admin():
        print("  [!] 未以系统管理员身份执行")
        print("      iOS 17+ 设备需要管理员权限才能建立通道")
        print("      请右键 LocWarp.bat → 以系统管理员身份执行")
        print()

    # 检查环境
    ok = True
    ok = check_tool("python", "https://www.python.org/downloads/") and ok
    ok = check_tool("node", "https://nodejs.org/") and ok
    ok = check_tool("npm", "随 Node.js 一起安装") and ok
    print()

    if not ok:
        input("  缺少必要工具，请安装后重试。按 Enter 离开...")
        return

    # 安装依赖
    install_backend()
    print()
    install_frontend()
    print()

    # 启动服务
    if not start_backend():
        print("  [错误] 后端启动失败，请查看上方错误信息")
        cleanup()
        input("  按 Enter 离开...")
        return
    print()

    if not start_frontend():
        print("  [错误] 前端启动失败")
        cleanup()
        input("  按 Enter 离开...")
        return
    print()

    # 等待 Vite 完成首次编译后再开浏览器
    time.sleep(2)
    url = f"http://localhost:{FRONTEND_PORT}"
    webbrowser.open(url)

    print("  ╔══════════════════════════════════════════╗")
    print("  ║          LocWarp 已就绪！                ║")
    print("  ╠══════════════════════════════════════════╣")
    print(f"  ║  前端画面:  http://localhost:{FRONTEND_PORT}        ║")
    print(f"  ║  后端 API:  http://localhost:{BACKEND_PORT}        ║")
    print(f"  ║  API 文件:  http://localhost:{BACKEND_PORT}/docs   ║")
    print("  ╠══════════════════════════════════════════╣")
    print("  ║  按 Enter 停止所有服务                   ║")
    print("  ╚══════════════════════════════════════════╝")
    print()

    try:
        input()
    except (KeyboardInterrupt, EOFError):
        pass

    cleanup()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cleanup()
