import os
import subprocess
import datetime
import requests

# 전국 주요 도시 리스트
cities = [
    "Seoul", "Busan", "Incheon", "Daegu", "Daejeon", "Gwangju", "Ulsan", "Sejong",
    "Suwon", "Cheongju", "Jeonju", "Gyeongju", "Chuncheon", "Gangneung",
    "Jeju", "Mokpo", "Andong"
]

# 현재 시간 및 파일 이름 설정
now = datetime.datetime.now()
date_str = now.strftime("%Y-%m-%d")
time_str = now.strftime("%Y-%m-%d %H:%M:%S")
log_dir = "logs"
log_file = f"{log_dir}/{date_str}.txt"

# 로그 폴더 없으면 생성
os.makedirs(log_dir, exist_ok=True)

# 온도 크롤링
weather_data = []
for city in cities:
    try:
        response = requests.get(f"https://wttr.in/{city}?format=%t", timeout=10)
        temp = response.text.strip()
        weather_data.append(f"{city}: {temp}")
    except Exception as e:
        weather_data.append(f"{city}: Error ({str(e)})")

# 로그 작성
log_entry = f"[{time_str}]\n" + "\n".join(weather_data) + "\n\n"

with open(log_file, "a", encoding="utf-8") as f:
    f.write(log_entry)

# Git 커밋 및 푸시
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", f"Weather auto commit {time_str}"])
subprocess.run(["git", "push"])
