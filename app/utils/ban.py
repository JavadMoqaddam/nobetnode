import subprocess


def init_iptables():
    try:
        subprocess.run(["ipset", "create", "banned", "hash:ip",
                       "timeout", "0"], check=True, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        pass  # Already exists

    try:
        subprocess.run(["iptables", "-C", "INPUT", "-m", "set", "--match-set",
                       "banned", "src", "-j", "DROP"], check=True, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        subprocess.run(["iptables", "-A", "INPUT", "-m", "set", "--match-set",
                       "banned", "src", "-j", "DROP"], check=False, stderr=subprocess.DEVNULL)


def ban_ip(ip: str, seconds: int):
    subprocess.run(["ipset", "add", "banned", ip, "timeout", str(
        seconds), "-exist"], check=True, stderr=subprocess.DEVNULL)


def unban_ip(ip: str, seconds: int):
    subprocess.run(["ipset", "del", "banned", ip],
                   check=False, stderr=subprocess.DEVNULL)
