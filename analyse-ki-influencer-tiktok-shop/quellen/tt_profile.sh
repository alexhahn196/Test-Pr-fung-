#!/bin/bash
# Usage: tt_profile.sh <username>   -> prints JSON with public profile stats from TikTok's SSR JSON
u="${1#@}"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
curl -sS -m 30 -A "$UA" "https://www.tiktok.com/@$u" | python3 -c '
import sys,re,json
html=sys.stdin.read()
m=re.search(r"<script id=\"__UNIVERSAL_DATA_FOR_REHYDRATION__\" type=\"application/json\">(.*?)</script>",html,re.S)
if not m: print(json.dumps({"error":"no SSR json","len":len(html)})); sys.exit()
d=json.loads(m.group(1)); ud=d["__DEFAULT_SCOPE__"].get("webapp.user-detail",{})
ui=ud.get("userInfo",{}); u=ui.get("user",{})
out={"statusCode":ud.get("statusCode"),"statusMsg":ud.get("statusMsg"),"uniqueId":u.get("uniqueId"),"nickname":u.get("nickname"),"signature":u.get("signature"),"verified":u.get("verified"),"createTime":u.get("createTime"),"region":u.get("region"),"ttSeller":u.get("ttSeller"),"commerceUserInfo":u.get("commerceUserInfo"),"bioLink":(u.get("bioLink") or {}).get("link"),"isOrganization":u.get("isOrganization"),"stats":ui.get("stats")}
print(json.dumps(out,ensure_ascii=False))'
