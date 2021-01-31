"""
  DONT CHANGE AUTHOR NAME
"""
import json, time, os
from datetime import datetime
try:
  import requests
except ImportError:
  os.system("pip install requests")

time = datetime.today().strftime('%Y-%m-%d')

banner = """

\033[1;33m  _______     
 /  \033[1;36m12   \033[1;33m\    
|    \033[1;31m|    \033[1;33m|      \033[0;41mWAKTU SHOLAT\033[0m
\033[1;33m|\033[1;36m9   \033[1;31m|   \033[1;36m3\033[1;33m|   
\033[1;33m|     \033[1;31m\   \033[1;33m|   \033[0;41mCREATED BY AWOK ID\033[0m
\033[1;33m|         |   
 \___\033[1;36m6\033[1;33m___/    
\033[0m

"""
os.system("cls" if os.name == "nt" else "clear")
print(banner)
kota = input("\033[1;31mNama \033[1;37mKota •\033[1;32m> \033[1;34m")
url = f"https://api.pray.zone/v2/times/day.json?city={kota}&date={time}"
try:
    req = requests.get(url)
    res = json.loads(req.text)
    if res["code"] == 200:
      os.system("cls" if os.name == "nt" else "clear")
      print(banner)
      for hasil in res["results"]["datetime"]:
        print(f"\033[1;37m----------\033[1;34m=\033[1;32m[ \033[0;44m{kota.upper()}\033[0m \033[1;32m]\033[1;34m=\033[1;37m----------")
        print("")
        print("Tanggal       \033[1;33m: \033[1;32m",hasil["date"]["gregorian"])
        print("\033[1;37mHijriah       \033[1;33m: \033[1;32m",hasil["date"]["hijri"])
        print("")
        print("\033[1;37m----------\033[1;34m=\033[1;32m[  \033[0;44mJADWAL\033[0m  \033[1;32m]\033[1;34m=\033[1;37m----------")
        print("")
        print("Subuh         \033[1;33m: \033[1;32m",hasil["times"]["Fajr"])
        print("\033[1;37mDzuhur        \033[1;33m: \033[1;32m",hasil["times"]["Dhuhr"])
        print("\033[1;37mAshar         \033[1;33m: \033[1;32m",hasil["times"]["Asr"])
        print("\033[1;37mMaghrib       \033[1;33m: \033[1;32m",hasil["times"]["Maghrib"])
        print("\033[1;37mIsya          \033[1;33m: \033[1;32m",hasil["times"]["Isha"])
        print("\033[0m")
    else:
      exit("\n\033[0;41mNAMA KOTA TIDAK DITEMUKAN\033[0m")
except KeyboardInterrupt:
  exit("\033[0;41mSTOP PROGRAM\033[0m")
except Exception as e:
  exit("\033[0;41mERROR!!! PLEASE CHECK YOUR NETWORK\033[0m")
