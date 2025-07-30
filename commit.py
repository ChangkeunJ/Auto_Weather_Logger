import os
import datetime
import requests

#  KST 시간대 설정 (UTC+9)
KST = datetime.timezone(datetime.timedelta(hours=9))

# 현재 시간 및 로그 파일 경로 설정
now = datetime.datetime.now(KST)
date_str = now.strftime("%Y-%m-%d")
time_str = now.strftime("%Y-%m-%d %H:%M:%S")
log_dir = "logs"
log_file = f"{log_dir}/{date_str}.txt"

# 로그 디렉토리 생성
os.makedirs(log_dir, exist_ok=True)

# 도시별 위도, 경도 정보
cities = {
    "서울": {"lat": 37.5665, "lon": 126.9780},
    "부산": {"lat": 35.1796, "lon": 129.0756},
    "인천": {"lat": 37.4563, "lon": 126.7052},
    "대구": {"lat": 35.8714, "lon": 128.6014},
    "대전": {"lat": 36.3504, "lon": 127.3845},
    "광주": {"lat": 35.1595, "lon": 126.8526},
    "울산": {"lat": 35.5384, "lon": 129.3114},
    "세종": {"lat": 36.4801, "lon": 127.2890},
    "수원": {"lat": 37.2636, "lon": 127.0286},
    "청주": {"lat": 36.6424, "lon": 127.4890},
    "전주": {"lat": 35.8242, "lon": 127.1480},
    "경주": {"lat": 35.8562, "lon": 129.2247},
    "춘천": {"lat": 37.8813, "lon": 127.7298},
    "강릉": {"lat": 37.7519, "lon": 128.8761},
    "제주": {"lat": 33.4996, "lon": 126.5312},
    "목포": {"lat": 34.8118, "lon": 126.3922},
    "안동": {"lat": 36.5684, "lon": 128.7294}
}

# Open-Meteo API로 현재 온도 가져오기
weather_data = []
for kr_name, coords in cities.items():
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&current_weather=true"
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache"
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
        data = response.json()
        
        temp = data.get('current_weather', {}).get('temperature')
        if temp is not None:
            # 온도를 소수점 첫째 자리까지 반올림하고 부호 추가
            temp_str = f"{temp:+.1f}°C"
            weather_data.append(f"{kr_name}: {temp_str}")
        else:
            weather_data.append(f"{kr_name}: Data not found")

    except requests.exceptions.RequestException as e:
        weather_data.append(f"{kr_name}: API Error ({type(e).__name__})")
    except Exception as e:
        weather_data.append(f"{kr_name}: Error ({str(e)})")

# 로그 작성
log_entry = f"[{time_str}]\n" + "\n".join(weather_data) + f"\n# Auto log at {time_str}\n\n"
with open(log_file, "a", encoding="utf-8") as f:
    f.write(log_entry)

# Git 커밋 및 푸시 (비활성화)
# subprocess.run(["git", "add", "."])
# subprocess.run(["git", "commit", "-m", f"Weather auto commit {time_str}"])
# subprocess.run(["git", "push"])
