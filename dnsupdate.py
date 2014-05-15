import sys
import subprocess
import time
print("-- -- BEGIN DNS UPDATING -- --")

SECRET_TOKEN = "YOUR-SECRET-TOKEN-HERE"

while True:
    bcurrent_IP = subprocess.check_output(["curl", "-s", "ifconfig.me"])
    current_IP = bcurrent_IP.decode(sys.stdout.encoding).strip()
    out = subprocess.check_output(["curl", "-s", "http://freedns.afraid.org/dynamic/update.php?{}&address={}".format(SECRET_TOKEN, current_IP)])
    if "ERROR" not in out.decode("utf-8"):
        subprocess.call(["notify-send", "Updated all DDNS entries."])
    time.sleep(300)
