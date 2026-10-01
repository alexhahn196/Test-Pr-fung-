#!/usr/bin/env python3
"""Erzeugt shortlist.md, wettbewerber.md und produktionspartner.md aus den Vertiefungs-Rohdaten.

Eingaben: rohdaten/vertiefung-batch*.json (Markt-, Produktions- und Prüferanalyse je Kandidat),
          rohdaten/endstatus.json (Endentscheidung je Shortlist-Kandidat, aus dem Bericht).
"""
import glob
import json
import os

HIER = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HIER, "..")
ROH = os.path.join(ROOT, "rohdaten")


def cell(s, n=400):
    if isinstance(s, (list, dict)):
        s = json.dumps(s, ensure_ascii=False)
    s = " ".join(str(s).split()).replace("|", "/")
    return s if len(s) <= n else s[: n - 1] + "…"


def de(x, nk=0):
    return f"{x:,.{nk}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def lade():
    kand = []
    for fn in sorted(glob.glob(os.path.join(ROH, "vertiefung-batch*.json"))):
        kand += json.load(open(fn, encoding="utf-8"))
    kand.sort(key=lambda k: k["id"])
    end = {}
    fp = os.path.join(ROH, "endstatus.json")
    if os.path.exists(fp):
        end = json.load(open(fp, encoding="utf-8")).get("shortlist", {})
    return kand, end


def aov(k):
    mi = k["pruefer"]["modell_eingaben"]
    a = sum(x["preis_brutto"] * x["mix_basis"] for x in mi["angebote"])
    a += sum(u["preis_brutto"] * u["quote_basis"] for u in mi["upsells"])
    return a


def shortlist(kand, end):
    L = ["# Shortlist – 10 vertiefte Kandidaten", "",
         "Recherchedatum 01.10.2026. Erzeugt von `werkzeuge/vertiefung_dateien.py` aus `rohdaten/vertiefung-batch1.json` und `-batch2.json`. "
         "Je Kandidat gab es drei unabhängige Agenten: Markt- und Wettbewerbsanalyse DACH, Produktions-/KI-/Vorschau-/Social-Analyse und einen adversarialen Prüfer, "
         "der tragende Aussagen selbst nachgeprüft, übersehene Wettbewerber gesucht, die Punkte vergeben und vorsichtige Modelleingaben geliefert hat. "
         "Die Punkte unten sind die des Prüfers.", "",
         "| Kandidat | Ø-Warenkorb brutto (Basis-Modell) | W/30 | M/20 | K/15 | Wb/15 | P/10 | S/10 | **Gesamt** | Datensicherheit | Ampel | Prüfer: finalisttauglich | Endstatus |",
         "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|"]
    for k in sorted(kand, key=lambda k: -k["pruefer"]["punkte_gesamt_100"]):
        v = k["pruefer"]
        L.append(f"| **{k['id']}** {cell(k['titel'], 90)} | {de(aov(k))} € | {v['punkte_wirtschaft_30']} | {v['punkte_markt_20']} | {v['punkte_ki_15']} | {v['punkte_wettbewerb_15']} | "
                 f"{v['punkte_produktion_10']} | {v['punkte_social_10']} | **{v['punkte_gesamt_100']}** | {v['datensicherheit']} | {v['ampel']} | {'ja' if v['finalist_tauglich'] else 'nein'} | {cell(end.get(k['id'], '–'), 140)} |")
    L.append("")
    for k in kand:
        m, p, v = k["markt"], k["produktion"], k["pruefer"]
        kd = p["ki_details"]
        L += [f"## {k['id']}. {k['titel']}", "",
              f"**Ergebnis:** {v['punkte_gesamt_100']}/100, Datensicherheit {v['datensicherheit']}, Ampel {v['ampel']}, finalisttauglich laut Prüfer: {'ja' if v['finalist_tauglich'] else 'nein'}. "
              f"Endstatus: {end.get(k['id'], '–')}", "",
              f"- **Urteil des Prüfers:** {cell(v['urteil'], 1500)}",
              f"- **Wichtigste Unsicherheit:** {cell(v['wichtigste_unsicherheit'], 600)}",
              f"- **Punktebegründung:** {cell(v['punkte_begruendung'], 1500)}",
              f"- **Produkt:** {cell(m['produktdefinition'], 1000)}",
              f"- **Kaufanlass und Timing:** {cell(m['kaufanlass_und_timing'], 600)}",
              f"- **Zielgruppe und DE-Größe:** {cell(m['zielgruppe_und_groesse_de'], 800)}",
              f"- **Warenkorb laut Markt:** {cell(m['markt_warenkorb'], 900)}",
              f"- **Wiederkauf und Produktwelt:** {cell(m['wiederkauf'], 600)}",
              f"- **Wettbewerb (Ampel {m['wettbewerbs_ampel']} laut Marktanalyse):** {cell(m['ampel_begruendung'], 900)}",
              f"- **Einstiegschance:** {cell(m['einstiegschance'], 900)}",
              f"- **Kanäle der Wettbewerber:** {cell(m['kanaele'], 600)}",
              f"- **KI:** Schwierigkeit {kd['technische_schwierigkeit_1bis5']}/5; Vorschau {cell(kd['generierungen_vorschau'], 200)}; Käufer {cell(kd['generierungen_kaeufer'], 200)}; "
              f"Kosten je Vorschau-Sitzung ca. {de(kd['kosten_vorschau_sitzung_eur'], 2)} €, je Käufer ca. {de(kd['kosten_finalisierung_kaeufer_eur'], 2)} €; Nachbearbeitung: {cell(kd['manuelle_nachbearbeitung_wahrscheinlichkeit'], 300)}; "
              f"Konsistenzrisiken: {cell(kd['konsistenz_risiken'], 400)}",
              f"- **Social-Creative-Potenzial:** {p['social']['creative_potenzial_1bis10']}/10 – {cell(p['social']['begruendung'], 400)}",
              f"- **Produktion:** {cell(p['produktionsweg_fazit'], 700)}",
              f"- **Rechtliche Besonderheiten:** {cell(p['recht_besonderheiten'], 700)}", "",
              "**Stärkste Gegenargumente (Prüfer):**", ""]
        L += [f"{i}. {cell(g, 600)}" for i, g in enumerate(v["staerkste_gegenargumente"], 1)]
        L += ["", "**Nachgeprüfte Aussagen:**", "", "| Aussage | Ergebnis | Befund | Quelle |", "|---|---|---|---|"]
        for a in v["gepruefte_aussagen"]:
            L.append(f"| {cell(a['aussage'], 250)} | {a['ergebnis']} | {cell(a['befund'], 400)} | {cell(a.get('url', ''), 200)} |")
        L += ["", f"**Offene Punkte:** {cell(m['offene_punkte'], 600)} {cell(p['offene_punkte'], 600)}", "", "---", ""]
    L += neuzuschnitt()
    open(os.path.join(ROOT, "shortlist.md"), "w", encoding="utf-8").write("\n".join(L))


def neuzuschnitt():
    fp = os.path.join(ROH, "neuzuschnitt.json")
    if not os.path.exists(fp):
        return []
    nz = json.load(open(fp, encoding="utf-8"))
    L = ["# Neuzuschnitt der 4 stärksten Kandidaten (A, B, C, D)", "",
         "Weil kein Kandidat die Vertiefung als finalisttauglich bestanden hat, wurden die vier stärksten neu zugeschnitten "
         "(Preisarchitektur mit ausgewiesener Gestaltungsleistung, margenschwache Teile gestrichen, Partner und Sendungen gebündelt, Kanalmix) "
         "und von zwei unabhängigen Prüfern gegengeprüft (Linse Ökonomie/CAC und Linse Markt/Zahlungsbereitschaft). Rohdaten: `rohdaten/neuzuschnitt.json`.", "",
         "| Kandidat | Prüfer Ökonomie: Punkte, DS, Ampel, finalisttauglich | Prüfer Markt: Punkte, DS, Ampel, finalisttauglich | Urteil (Rangfolge) |",
         "|---|---|---|---|"]
    rang = {x["id"]: x for x in nz["urteil"]["rangfolge"]}
    for k in nz["kandidaten"]:
        g = k["gegenpruefung"]
        zelle_g = lambda x: f"{x['punkte_gesamt_100']} ({x['punkte_wirtschaft_30']}/{x['punkte_markt_20']}/{x['punkte_ki_15']}/{x['punkte_wettbewerb_15']}/{x['punkte_produktion_10']}/{x['punkte_social_10']}), {x['datensicherheit']}, {x['ampel']}, {'ja' if x['finalist_tauglich'] else 'nein'}"
        L.append(f"| **{k['id']}** {cell(k['titel'], 80)} | {zelle_g(g[0])} | {zelle_g(g[1]) if len(g) > 1 else '–'} | {rang.get(k['id'], {}).get('rang', '–')}. {rang.get(k['id'], {}).get('status', '–')} |")
    L += ["", f"**Gesamtfazit des Urteils:** {cell(nz['urteil']['gesamtfazit'], 4000)}", "",
          f"**Zuerst testen:** {cell(nz['urteil']['zuerst_testen'], 3000)}", "",
          f"**Lehren über alle Kandidaten:** {cell(nz['urteil']['querschnitt_lehren'], 4000)}", ""]
    for k in nz["kandidaten"]:
        n = k["neuzuschnitt"]
        r = rang.get(k["id"], {})
        L += [f"## {k['id']}. {k['titel']} – Neuzuschnitt", "",
              f"**Urteil:** {r.get('status', '–')} – {cell(r.get('begruendung', ''), 1500)}", "",
              f"**Neuzuschnitt:** {cell(n['neuzuschnitt_kurz'], 2000)}", "",
              f"**Angebotsarchitektur:** {cell(n['angebotsarchitektur'], 2000)}", "",
              "**Änderungen gegenüber der Vertiefung:**", ""]
        L += [f"- {cell(a['was'], 500)} – *Warum:* {cell(a['warum'], 300)} – *Beleg:* {cell(a['beleg'], 400)}" for a in n["aenderungen"]]
        L += ["", "**Kanalmix (Neuzuschnitt, vor Korrektur durch die Prüfer):**", "", "| Kanal | Anteil Neukunden (Basis) | CAC | Herleitung | Label |", "|---|---:|---:|---|---|"]
        L += [f"| {cell(c['kanal'], 80)} | {de(c['anteil_neukunden_basis'] * 100)} % | {de(c['cac_eur'])} € | {cell(c['herleitung'], 400)} | {cell(c['label'], 60)} |" for c in n["kanalmix"]]
        L += ["", f"**Herleitung blended CAC:** {cell(n['blended_cac_herleitung'], 1500)}", ""]
        for g in k["gegenpruefung"]:
            L += [f"### Gegenprüfung: {cell(g['linse'], 120)}", "",
                  f"**{g['punkte_gesamt_100']}/100**, Datensicherheit {g['datensicherheit']}, Ampel {g['ampel']}, finalisttauglich: {'ja' if g['finalist_tauglich'] else 'nein'}", "",
                  f"- **Urteil:** {cell(g['urteil'], 2500)}", f"- **Bedingungen, unter denen es trägt:** {cell(g['bedingungen'], 2000)}",
                  f"- **Modellrechnung:** {cell(g['modellergebnis'], 2500)}", "", "**Einwände:**", ""]
            L += [f"{i}. {cell(e, 500)}" for i, e in enumerate(g["einwaende"], 1)]
            L += ["", "| Geprüfte Aussage | Ergebnis | Befund | Quelle |", "|---|---|---|---|"]
            L += [f"| {cell(a['aussage'], 200)} | {a['ergebnis']} | {cell(a['befund'], 350)} | {cell(a.get('url', ''), 160)} |" for a in g["gepruefte_punkte"]]
            L.append("")
        L += ["---", ""]
    return L


def wettbewerber(kand):
    L = ["# Wettbewerber je Shortlist-Kandidat", "",
         "Recherchedatum 01.10.2026. Erzeugt aus den Marktanalysen und den Ergänzungen des adversarialen Prüfers. "
         "Bewertungen sind keine Bestellungen; Bewertungszähler laufen weiter (Stand Abruf). Typen: Generalist, Spezialist, Atelier/Handarbeit, "
         "Marktplatz-Händler, Produktionspartner mit B2C-Angebot, DIY-Werkzeug, Nicht-KI-Alternative.", ""]
    for k in kand:
        m, v = k["markt"], k["pruefer"]
        L += [f"## {k['id']}. {k['titel']}", "",
              f"Wettbewerbsampel Marktanalyse: **{m['wettbewerbs_ampel']}** – Prüfer: **{v['ampel']}**. {cell(m['ampel_begruendung'], 700)}", "",
              "| Anbieter | Land | Typ | Angebot/Bundles | Preise | Lieferzeit | Qualität | Personalisierung | Vorschau | Branding | Bewertungen | Größe | Social | KI | Stärken/Schwächen |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for w in m["wettbewerber"]:
            L.append(f"| [{cell(w['name'], 60)}]({w['url']}) | {cell(w['land'], 30)} | {cell(w['typ'], 40)} | {cell(w['angebot_und_bundles'], 220)} | {cell(w['preise'], 220)} | "
                     f"{cell(w.get('lieferzeit', '–'), 80)} | {cell(w.get('qualitaet', '–'), 120)} | {cell(w['personalisierungsgrad'], 120)} | {cell(w['vorschau'], 100)} | "
                     f"{cell(w.get('branding', '–'), 80)} | {cell(w['bewertungen'], 160)} | {cell(w.get('groesse', '–'), 140)} | {cell(w.get('social_media', '–'), 100)} | "
                     f"{cell(w.get('ki_einsatz', '–'), 100)} | {cell(w.get('staerken_schwaechen', '–'), 200)} |")
        if v["uebersehene_wettbewerber"]:
            L += ["", "**Vom Prüfer ergänzt (übersehen):**", ""]
            L += [f"- [{w['name']}]({w['url']}): {cell(w['relevanz'], 400)}" for w in v["uebersehene_wettbewerber"]]
        L += ["", f"**Etsy/Amazon:** {cell(m['etsy_amazon'], 700)}", "",
              f"**Nicht-KI-Alternativen mit gleichem Nutzen:** {cell(m['nicht_ki_alternativen'], 700)}", "",
              "**US-Vorbilder:**", ""]
        for u in m["us_vorbilder"]:
            L.append(f"- [{u['name']}]({u['url']}): {cell(u['produkt_preise'], 250)} – Größe: {cell(u['groessenbeleg'], 400)} – KI: {cell(u.get('nutzt_ki', '–'), 120)} – Übertragbar: {cell(u.get('uebertragbar', '–'), 200)}")
        L += ["", "---", ""]
    open(os.path.join(ROOT, "wettbewerber.md"), "w", encoding="utf-8").write("\n".join(L))


def produktionspartner(kand):
    L = ["# Produktionspartner je Shortlist-Kandidat", "",
         "Recherchedatum 01.10.2026. Erzeugt aus den Produktionsanalysen. Status je Prüfpunkt: „Auf der Website bestätigt“ / "
         "„Vom Anbieter beworben, nicht praktisch überprüft“ / „Noch anzufragen“. Es wurden keine Musterbestellungen, Registrierungen oder Kontaktaufnahmen durchgeführt; "
         "Konditionen hinter Login oder auf Anfrage sind deshalb offen. Preise netto, sofern nicht anders angegeben.", ""]
    index = {}
    for k in kand:
        p = k["produktion"]
        L += [f"## {k['id']}. {k['titel']}", "", f"**Fazit Produktionsweg:** {cell(p['produktionsweg_fazit'], 1200)}", "",
              "| Partner | Produktionsort | Produkte | ab 1 Stück | Direktversand | Neutral/White Label | Shopify | WooCommerce | API | Datei je Bestellung | Produktionszeit | Versand DE | Einkaufspreise | Versandkosten | Material/Größen | Reklamation | Status | Spezialhersteller |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for t in p["partner"]:
            index.setdefault(t["name"], set()).add(k["id"])
            L.append(f"| [{cell(t['name'], 50)}]({t['url']}) | {cell(t['land_produktionsort'], 80)} | {cell(t['produkte'], 120)} | {cell(t['ab_stueck_1'], 60)} | {cell(t['direktversand'], 60)} | "
                     f"{cell(t['white_label_neutral'], 90)} | {cell(t['shopify'], 50)} | {cell(t['woocommerce'], 50)} | {cell(t['api'], 60)} | {cell(t['datei_je_bestellung'], 60)} | "
                     f"{cell(t['produktionszeit'], 60)} | {cell(t['versandzeit_de'], 60)} | {cell(t['einkaufspreise'], 220)} | {cell(t['versandkosten'], 120)} | {cell(t['materialien_groessen'], 160)} | "
                     f"{cell(t['reklamation'], 120)} | {cell(t['status'], 240)} | {'ja' if t['spezialhersteller_schwer_skalierbar'] else 'nein'} |")
        L += ["", "**Angebote und Stücklisten (Vorschlag der Produktionsanalyse):**", ""]
        for a in p["angebote"]:
            L += [f"*{a['name']}* – Vorschlag {de(a['preis_brutto_vorschlag'], 2)} € brutto; Versand {de(a['versand_netto_eur'], 2)} € netto in {de(a['sendungen'])} Sendung(en); {de(a['produktionsdateien'])} Produktionsdatei(en)", "",
                  "| Artikel | Menge | Partner | Einkauf netto/Stück | Label | Quelle |", "|---|---:|---|---:|---|---|"]
            for b in a["bestandteile"]:
                L.append(f"| {cell(b['artikel'], 80)} | {de(b['menge'], 0)} | {cell(b['partner'], 50)} | {de(b['einkauf_netto_eur_je_stueck'], 2)} € | {b['label']} | {cell(b['quelle'], 160)} |")
            L.append("")
        if p["upsells"]:
            L += ["**Upsells:**", ""]
            L += [f"- {u['name']}: {de(u['preis_brutto_vorschlag'], 2)} € brutto, Einkauf {de(u['einkauf_netto_eur'], 2)} € netto, Quote-Annahme {de(u['quote_annahme'] * 100)} % – {cell(u.get('quelle', ''), 200)}" for u in p["upsells"]]
            L.append("")
        L += ["**KI-Pipeline:**", ""] + [f"{i}. {cell(s, 400)}" for i, s in enumerate(p["ki_pipeline"], 1)]
        kd = p["ki_details"]
        L += ["", f"Modelle und Preise: {cell(kd['modelle_und_preise'], 900)}", "", f"Automatisierung: {cell(kd['automatisierung'], 500)}", "",
              f"**Kostenlose Vorschau:** Wow-Effekt: {cell(p['kostenlose_vorschau']['wow_effekt'], 300)} Kosten: {cell(p['kostenlose_vorschau']['kosten_je_vorschau'], 200)} "
              f"Missbrauch: {cell(p['kostenlose_vorschau']['missbrauchsrisiko'], 250)} Wasserzeichen: {cell(p['kostenlose_vorschau']['wasserzeichen'], 200)} "
              f"Gratis-Varianten: {cell(p['kostenlose_vorschau']['gratis_varianten'], 150)} E-Mail vorab: {cell(p['kostenlose_vorschau']['email_vor_vorschau'], 200)} "
              f"Empfehlung: {cell(p['kostenlose_vorschau']['empfehlung'], 400)}", "", "---", ""]
    L += ["## Partnerindex", "", "| Partner | genutzt bei Kandidat |", "|---|---|"]
    for n in sorted(index):
        L.append(f"| {cell(n, 80)} | {', '.join(sorted(index[n]))} |")
    open(os.path.join(ROOT, "produktionspartner.md"), "w", encoding="utf-8").write("\n".join(L))


def main():
    kand, end = lade()
    shortlist(kand, end)
    wettbewerber(kand)
    produktionspartner(kand)
    print(f"shortlist.md, wettbewerber.md, produktionspartner.md geschrieben ({len(kand)} Kandidaten)")


if __name__ == "__main__":
    main()
