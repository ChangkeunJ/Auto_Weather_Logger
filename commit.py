import os
import subprocess
import datetime
import requests
import urllib.parse

# 한글 도시 이름 → API용 영문 이름 맵핑
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

# 현재 시간 및 로그 파일 경로 설정
now = datetime.datetime.now()
date_str = now.strftime("%Y-%m-%d")
time_str = now.strftime("%Y-%m-%d %H:%M:%S")
log_dir = "logs"
log_file = f"{log_dir}/{date_str}.txt"

# 로그 디렉토리 생성 (없으면)
os.makedirs(log_dir, exist_ok=True)

# 온도 크롤링
weather_data = []
for kr_name, en_name in cities.items():
    try:
        encoded_city = urllib.parse.quote(en_name)
        url = f"https://wttr.in/{encoded_city}?format=%t&m"
        response = requests.get(url, timeout=10)
        temp = response.text.strip()
        weather_data.append(f"{kr_name}: {temp}")
    except Exception as e:
        weather_data.append(f"{kr_name}: Error ({str(e)})")
