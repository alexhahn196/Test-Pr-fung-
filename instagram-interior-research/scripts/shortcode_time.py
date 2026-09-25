"""Derive the exact UTC publish time of an Instagram post from its shortcode.

Instagram media IDs (see Instagram Engineering, "Sharding & IDs at Instagram", 2012) store a
41-bit millisecond timestamp (custom epoch 2011-08-24T21:07:01.721Z) in the top bits. The public
shortcode is the media ID in base64 (alphabet A-Z a-z 0-9 - _). Verified against reels with known
dates (DBWhf0koR7_ -> 2024-10-20, C6rOLbLriyx -> 2024-05-07).
"""
import datetime

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
IG_EPOCH_MS = 1314220021721


def shortcode_to_datetime(shortcode):
    sc = (shortcode or "").strip()[:11]
    if not sc:
        return None
    n = 0
    for c in sc:
        i = ALPHABET.find(c)
        if i < 0:
            return None
        n = n * 64 + i
    ms = (n >> 23) + IG_EPOCH_MS
    dt = datetime.datetime.fromtimestamp(ms / 1000, datetime.timezone.utc)
    if not (2012 <= dt.year <= 2027):
        return None
    return dt


if __name__ == "__main__":
    import sys
    for s in sys.argv[1:]:
        print(s, shortcode_to_datetime(s))
