import socket
import sys


def check_port(host, port, timeout=3):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def main():
    ip = input("目标IP    : ").strip()

    try:
        port = int(input("目标端口  : "))
    except ValueError:
        print("端口必须是数字")
        return

    if not (0 <= port <= 65535):
        print("端口范围应为 0-65535")
        return

    try:
        resolved_ip = socket.gethostbyname(ip)
        if resolved_ip != ip:
            print(f"域名 {ip} 解析为 {resolved_ip}")
        ip = resolved_ip
    except socket.gaierror:
        print(f"无法解析 {ip}，将直接作为 IP 使用")

    if check_port(ip, port):
        print(f"{ip}:{port} 端口开放")
    else:
        print(f"{ip}:{port} 端口关闭或不可达")


def wait_for_space():
    print("\n按空格键退出...", end="", flush=True)
    try:
        if sys.platform == "win32":
            import msvcrt
            while msvcrt.getch() != b' ':
                pass
        else:
            import tty
            import termios
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                while sys.stdin.read(1) != ' ':
                    pass
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
    except Exception:
        input()  # 回退到回车
    print()


if __name__ == "__main__":
    main()
    wait_for_space()