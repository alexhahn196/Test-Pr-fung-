#!/bin/bash
# Usage: tt_video.sh <tiktok video url or id> -> prints JSON with public video stats (playCount etc.), anchors (product links), AIGC label flags
v="$1"; case "$v" in http*) url="$v";; *) url="https://www.tiktok.com/@_/video/$v";; esac
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
curl -sSL -m 30 -A "$UA" "$url" | python3 -c '
import sys,re,json
html=sys.stdin.read()
m=re.search(r"<script id=\"__UNIVERSAL_DATA_FOR_REHYDRATION__\" type=\"application/json\">(.*?)</script>",html,re.S)
if not m: print(json.dumps({"error":"no SSR json","len":len(html)})); sys.exit()
d=json.loads(m.group(1)); vd=d["__DEFAULT_SCOPE__"].get("webapp.video-detail",{})
it=vd.get("itemInfo",{}).get("itemStruct",{})
if not it: print(json.dumps({"statusCode":vd.get("statusCode"),"statusMsg":vd.get("statusMsg")})); sys.exit()
a=it.get("author",{}); s=it.get("stats",{})
out={"id":it.get("id"),"author":a.get("uniqueId"),"authorStats":it.get("authorStats"),"desc":it.get("desc"),"createTime":it.get("createTime"),"duration":it.get("video",{}).get("duration"),"stats":s,"isAd":it.get("isAd"),"aigcLabelType":it.get("aigcLabelType"),"AIGCDescription":it.get("AIGCDescription"),"anchors":[{"type":x.get("type"),"keyword":x.get("keyword"),"description":x.get("description")} for x in (it.get("anchors") or [])],"textExtra":[t.get("hashtagName") for t in (it.get("textExtra") or []) if t.get("hashtagName")],"music":(it.get("music") or {}).get("title"),"isECVideo":it.get("isECVideo"),"itemCommentStatus":it.get("itemCommentStatus")}
print(json.dumps(out,ensure_ascii=False))'
