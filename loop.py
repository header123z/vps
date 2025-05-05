import psutil
import subprocess
import time
import datetime
import requests

threshold_percentage = 50
included_processes = ['msedge.exe', 'xmrig.exe']  # List of process names to include
log_file = "log.txt"
start_time = time.time()
send_log_after_minutes = 60
telegram_bot_token = '7588647057:AAE_1kfJBAZggHQoVs7c1LVHaOBs2c6qGfU'
chat_id = '7371969470'

def log_cpu_usage():
    with open(log_file, "a") as f:
        for process in psutil.process_iter(['name', 'cpu_percent']):
            process_name = process.info['name']
            cpu_percent = process.info['cpu_percent']
            if cpu_percent > threshold_percentage and process_name not in ['System Idle Process', 'python.exe']:
                f.write(f"{process_name} : {cpu_percent}%\n")

def send_log():
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendDocument"
    files = {'document': open(log_file, 'rb')}
    data = {'chat_id': chat_id}
    response = requests.post(url, files=files, data=data)

def main():
    start_time = time.time()
    while True:
        processes_exceeded_threshold = False
        for process in psutil.process_iter(['name', 'cpu_percent']):
            process_name = process.info['name']
            cpu_percent = process.info['cpu_percent']
            if process_name != 'Idle' and process_name in included_processes:
                try:
                    subprocess.run(['taskkill', '/F', '/IM', process_name], check=True)
                except subprocess.CalledProcessError:
                    pass  # Do nothing if process not found or failed to kill

            if cpu_percent > threshold_percentage:
                processes_exceeded_threshold = True

        if processes_exceeded_threshold:
            log_cpu_usage()

        current_time = time.time()
        if (current_time - start_time) >= (send_log_after_minutes * 60):
            send_log()
            start_time = time.time()

        time.sleep(10)

if __name__ == "__main__":
    main()
