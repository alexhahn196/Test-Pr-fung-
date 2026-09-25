"""Map Instagram /popular/ topic slugs to analysis groups and coding priority."""
import re

# (group, priority, regex) - first match wins. priority 1 = core niche, 2 = adjacent, 3 = peripheral
RULES = [
    ("ai", 1, r"(^ai-|-ai$|-ai-|midjourney|render|virtual-staging)"),
    ("cozy_ambience", 1, r"(cozy|rain|rainy)"),
    ("fantasy_dream", 1, r"(fantasy|impossible|surreal|dream-life|dream-room|waterfall|capsule|dream-house-design)"),
    ("future_arch", 1, r"(futur|parametric|2050)"),
    ("hotel_resort", 1, r"(hotel|resort|airbnb|glamping|overwater|suite|bora-bora|hunza|cook-islands|rooftop-pools)"),
    ("location", 1, r"(dubai|bali|maldives|monaco|swiss|chalet|new-york|tokyo|santorini|ibiza|como|malibu|beverly|miami|amalfi|tulum|mykonos|aspen|los-angeles|london|saudi|marrakech|faroe)"),
    ("unusual_home", 1, r"(cliff|glass-house|treehouse|cabin|mountain-house|beach-house|lake-house|desert|underground|container|forest|bunker)"),
    ("pool", 1, r"(pool)"),
    ("luxury_home", 1, r"(luxury-home|luxury-house|dream-house|dream-home|modern-house|modern-villa|luxury-villa|villa|mansion|penthouse|house-tour|luxury-apartment|luxury-real-estate|jamesedition|modern-luxury-house|ultra-modern|luxury-modern)"),
    ("architecture", 1, r"(architect|brutalist)"),
    ("luxury_room", 1, r"(luxury-(bed|living|kitchen|bath|dining|closet|room|master|home-theater)|dream-(bed|kitchen|closet)|quiet-luxury|dreamy-walk)"),
    ("style", 1, r"(japandi|organic-modern|dark-luxury|minimalist|biophilic|scandinavian|industrial|neoclassical|modern-classic|wabi-sabi|mediterranean|tropical|art-deco|mid-century|cyberpunk|coastal|cottagecore|dark-academia|green-minimalist)"),
    ("room_generic", 2, r"(bedroom|living-room|kitchen|bathroom|closet|home-theater|home-library|dining|wine-cellar|home-office|kids-room|rooftop-terrace|outdoor-kitchen)"),
    ("interior_generic", 2, r"(interior|luxury-lifestyle|luxury-life|luxury-furniture|furniture-design)"),
    ("garden_outdoor", 3, r"(garden|landscape|backyard|outdoor)"),
    ("decor_commerce", 2, r"(decor|amazon|makeover|styling)"),
    ("real_estate", 3, r"(real-estate|mansion-tour|penthouse-tour)"),
]


def topic_group(slug):
    s = (slug or "").lower()
    for g, p, rx in RULES:
        if re.search(rx, s):
            return g, p
    return "other", 3


if __name__ == "__main__":
    import csv, os, collections
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    st = list(csv.DictReader(open(os.path.join(root, "data", "processed", "topics_status.csv"))))
    c = collections.defaultdict(list)
    for r in st:
        c[topic_group(r["slug_used"])].append(r["slug_used"])
    for k, v in sorted(c.items()):
        print(k, len(v), ", ".join(v))
