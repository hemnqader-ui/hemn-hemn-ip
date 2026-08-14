import requests
import re

url = "https://karwan.tv/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://karwan.tv/"
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        links = re.findall(r'https?://[^\s\'"]+\.m3u8[^\s\'"]*', response.text)
        unique_links = list(set(links))
        
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            for idx, link in enumerate(unique_links, start=1):
                f.write(f"#EXTINF:-1, Channel {idx}\n")
                f.write(f"{link}\n")
        print("فایلی playlist.m3u ئامادەکرا.")
    else:
        print(f"Error: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
