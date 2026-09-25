# Cover-frame + caption codebook (v2)

Used by coding agents that LOOK at the reel's cover frame (og:image, downloaded from Instagram's CDN)
and READ the caption. Motion, length and audio cannot be coded from a still and are left out here
(see NexLev subset + YouTube Shorts proxy for those).

Output one JSON object per reel with exactly these keys and allowed values:

visual (from the cover image):
- room_primary: bedroom | living_room | kitchen | bathroom | dining | closet | home_theater | office | pool | terrace_outdoor | garden_landscape | exterior_facade | hotel_room | lobby_common | spa | stairs_hall | other | none_person_only
- rooms_visible: list from the same set
- building_type: villa | penthouse | apartment | mansion | cabin_chalet | treehouse | hotel_resort | house | castle_palace | unusual_structure | none_visible
- landscape: ocean_beach | mountain | forest | desert | jungle_tropical | lake_river | snow | city_skyline | cliff | underwater | space_sky | rain_window | none
- style_primary: modern_luxury | minimalist | japandi | tropical | mediterranean | brutalist | futuristic | organic_modern | biophilic | scandinavian | dark_luxury | warm_luxury | industrial | cyberpunk | classical_luxury | neoclassical | art_deco | rustic_cozy | mid_century | maximalist | glam_feminine | traditional_regional | other
- style_secondary: same set or null
- palette_temp: warm | neutral | cool
- brightness: bright | medium | dark
- dominant_colors: up to 4 plain color words (e.g. beige, white, black, brown, gold, green, blue, grey, pink, terracotta)
- materials: subset of wood, natural_stone, marble, glass, concrete, metal, fabric, water, plants, leather, plaster, rattan, fire
- lighting: daylight | golden_hour | blue_hour | night_artificial | overcast_rain | candle_fire | mixed
- ambience_fx: subset of rain, snow, fireplace, fog, stars, city_lights, ocean_waves, none
- view_through_window: true | false  (a notable outside view/landscape visible through glass)
- people_present: true | false
- cover_text: verbatim on-screen text visible on the cover, or null
- cover_hooks: subset of text_overlay, exterior_reveal, view_reveal, pool, bed_focus, person, door_or_threshold, unusual_architecture, before_after_split, empty_room, dramatic_scale, water_feature, none
- realism: fantasy_impossible (physically implausible/surreal) | stylized_dreamy (plausible but idealized, dreamlike) | aspirational_realistic (could exist/buyable) | real_existing (real photo/footage of real place)
- production: ai_generated | 3d_render | real_footage | unclear
- production_evidence: short reason (e.g. caption says AI, typical AI artifacts, render look, real camera noise)
- shoppability: high (clearly identifiable, buyable-looking furniture/decor) | medium | low (fantasy, architecture-only, not buyable)
- visual_quality: high | medium | low
- notable: one sentence on what makes it scroll-stopping (or not)

caption-derived (from the caption text):
- caption_hook_category: first line of caption classified as curiosity | pov | aspirational | choice | question | status | money | location | fantasy | contrarian | instructional | descriptive | promotional | none
- caption_first_line: first line verbatim (max 120 chars)
- cta_type: comment_keyword | question_engagement | follow | save_share | link_in_bio | dm | shop_product | tag_friend | none
- location_claimed: place named in caption/cover, or null
- price_claimed: price/money figure named, or null
- ai_disclosed: true if caption/cover says AI / #ai / made with Midjourney etc., else false
- account_kind_hint: theme_page | designer_studio | real_estate | brand_manufacturer | contractor_trade | ai_creator | lifestyle_influencer | media_publication | other
- language: main caption language (en, es, pt, ar, id, ru, de, tr, fr, hi, other)
