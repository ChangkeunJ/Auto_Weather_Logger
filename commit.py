import os
import subprocess
import datetime
import requests
import urllib.parse

# ⏰ KST 시간대 설정 (UTC+9)
KST = datetime.timezone(datetime.timedelta(hours=9))

# 현재 시간 및 로그 파일 경로 설정
now = datetime.datetime.now(KST)  # ← 변경된 부분
date_str = now.strftime("%Y-%m-%d")
time_str = now.strftime("%Y-%m-%d %H:%M:%S")
log_dir = "logs"
log_file = f"{log_dir}/{date_str}.txt"

# 로그 디렉토리 생성
os.makedirs(log_dir, exist_ok=True)

# 도시명 맵핑
cities = {
    "서울": "Seoul",
    "부산": "Busan",
    "인천": "Incheon",
    "대구": "Daegu",
    "대전": "Daejeon",
    "광주": "Gwangju",
    "울산": "Ulsan",
    "세종": "Sejong",
    "수원": "Suwon",
    "청주": "Cheongju",
    "전주": "Jeonju",
    "경주": "Gyeongju",
    "춘천": "Chuncheon",
    "강릉": "Gangneung",
    "제주": "Jeju",
    "목포": "Mokpo",
    "안동": "Andong"
}

# 온도 크롤링
weather_data = []
for kr_name, en_name in cities.items():
    try:
        encoded_city = urllib.parse.quote(en_name)
        timestamp = datetime.datetime.utcnow().timestamp()
        url = f"https://wttr.in/{encoded_city}?format=j1&_={timestamp}"
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache"
        }

        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        temp = f"+{data['current_condition'][0]['temp_C']}°C"
        weather_data.append(f"{kr_name}: {temp}")
    except Exception as e:
        weather_data.append(f"{kr_name}: Error ({str(e)})")

# Dummy line 추가로 매번 변경 감지
dummy_line = f"# Auto log at {time_str}"

# 로그 작성
log_entry = f"[{time_str}]\n" + "\n".join(weather_data) + f"\n{dummy_line}\n\n"
with open(log_file, "a", encoding="utf-8") as f:
    f.write(log_entry)

# Git 커밋 및 푸시
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", f"Weather auto commit {time_str}"])
subprocess.run(["git", "push"])
