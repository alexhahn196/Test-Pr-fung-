#!/bin/bash
# Usage: tt_recent.sh <username> -> prints the newest ~10 video URLs of a TikTok account via the public creator embed page
u="${1#@}"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
curl -sSL -m 30 -A "$UA" "https://www.tiktok.com/embed/@$u" | python3 -c '
import sys,re
html=sys.stdin.read()
ids=[]
for m in re.finditer(r"/video/(\d{15,20})",html):
    if m.group(1) not in ids: ids.append(m.group(1))
if not ids:
    for m in re.finditer(r"\"id\":\"(\d{17,20})\"",html):
        if m.group(1) not in ids: ids.append(m.group(1))
u=sys.argv[1]
for i in ids: print(f"https://www.tiktok.com/@{u}/video/{i}")
print("count",len(ids),file=sys.stderr)' "$u"
