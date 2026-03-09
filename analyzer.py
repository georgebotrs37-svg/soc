import re
import pandas as pd
import os
from collections import defaultdict
from colorama import Fore, init

init()

log_file = "auth.log" 
output_folder = "reports"
output_file = f"{output_folder}/security_report.csv"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

failed_logins = defaultdict(int)

pattern = r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)"

print(Fore.CYAN + "\n[+] جاري تحليل السجلات...")

if os.path.exists(log_file):
    with open(log_file, "r") as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                ip = match.group(1)
                failed_logins[ip] += 1
else:
    print(Fore.RED + f"[-] خطأ: ملف {log_file} غير موجود!")
    exit()

print(Fore.CYAN + "\n=== Failed Login Attempts ===")
data = []
for ip, count in failed_logins.items():
    print(Fore.WHITE + f"{ip} -> {count} attempts")
    data.append({"IP Address": ip, "Failed Attempts": count})

print(Fore.RED + "\n=== Possible Brute Force Attacks ===")
for ip, count in failed_logins.items():
    if count >= 3:
        print(Fore.RED + f"⚠ ALERT: Possible Brute Force from {ip} ({count} times!)")

if data:
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(Fore.GREEN + f"\n[✔] تم حفظ التقرير بنجاح في: {output_file}")
else:
    print(Fore.YELLOW + "\n[!] لم يتم العثور على محاولات فاشلة للتحليل.")