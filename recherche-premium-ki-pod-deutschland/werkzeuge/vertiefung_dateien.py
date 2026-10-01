#!/usr/bin/env python3
"""Erzeugt shortlist.md, wettbewerber.md und produktionspartner.md aus den Vertiefungs-Rohdaten.

Eingaben: rohdaten/vertiefung-batch*.json (Markt-, Produktions- und Prüferanalyse je Kandidat),
          rohdaten/endstatus.json (Endentscheidung je Shortlist-Kandidat, aus dem Bericht).
"""
import glob
import json
import os
import re

HIER = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HIER, "..")
ROH = os.path.join(ROOT, "rohdaten")


UMLAUTE = {"spaet": "spät", "Gaestebuch": "Gästebuch", "Zusaetzliche": "Zusätzliche", "oekonomie": "Ökonomie",
           "Oekonomie": "Ökonomie", "fuer": "für", "Groesse": "Größe", "Aenderung": "Änderung"}
PFAD_RE = re.compile(r"/tmp/claude-0/[^\s,;)]*")
NUM_RE = re.compile(r"^\s*\d+[.)]?\s+")


def cell(s, n=None):
    """Zelleninhalt säubern; kürzt nur an Satz- oder Wortgrenzen und nur, wenn n gesetzt ist."""
    if isinstance(s, (list, dict)):
        s = json.dumps(s, ensure_ascii=False)
    s = " ".join(str(s).split()).replace("|", "/")
    s = PFAD_RE.sub("(lokales Prüfskript)", s)
    for a, b in UMLAUTE.items():
        s = s.replace(a, b)
    if n is None or len(s) <= n:
        return s
    cut = s[:n]
    for sep in (". ", "; ", ", ", " "):
        i = cut.rfind(sep)
        if i > n * 0.6:
            return cut[: i + (1 if sep != " " else 0)].rstrip() + " […]"
    return cut.rstrip() + " […]"


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
         "**Hinweis:** Diese Datei gibt die Rohbefunde der Recherche-Agenten wieder (ungekürzt, mit ihren Kennzeichnungen). Tragende Aussagen wurden danach im Faktencheck geprüft (`rohdaten/faktencheck.json`); wo Abweichungen gefunden wurden, gilt die korrigierte Fassung in `bericht.md`, `finalisten.md` und `quellen.md`. Wertende Sätze der Agenten (z. B. zu Ursachen einer Insolvenz oder „frei werdender Nachfrage“) sind Einschätzungen, keine Belege.", "",
         "| Kandidat | Ø-Warenkorb brutto (Basis-Modell) | W/30 | M/20 | K/15 | Wb/15 | P/10 | S/10 | **Gesamt** | Datensicherheit | Ampel | Prüfer: finalisttauglich | Endstatus |",
         "|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|"]
    for k in sorted(kand, key=lambda k: -k["pruefer"]["punkte_gesamt_100"]):
        v = k["pruefer"]
        L.append(f"| **{k['id']}** {cell(k['titel'], 200)} | {de(aov(k))} € | {v['punkte_wirtschaft_30']} | {v['punkte_markt_20']} | {v['punkte_ki_15']} | {v['punkte_wettbewerb_15']} | "
                 f"{v['punkte_produktion_10']} | {v['punkte_social_10']} | **{v['punkte_gesamt_100']}** | {v['datensicherheit']} | {v['ampel']} | {'ja' if v['finalist_tauglich'] else 'nein'} | {cell(end.get(k['id'], '–'), 280)} |")
    L.append("")
    for k in kand:
        m, p, v = k["markt"], k["produktion"], k["pruefer"]
        kd = p["ki_details"]
        L += [f"## {k['id']}. {k['titel']}", "",
              f"**Ergebnis:** {v['punkte_gesamt_100']}/100, Datensicherheit {v['datensicherheit']}, Ampel {v['ampel']}, finalisttauglich laut Prüfer: {'ja' if v['finalist_tauglich'] else 'nein'}. "
              f"Endstatus: {end.get(k['id'], '–')}", "",
              f"- **Urteil des Prüfers:** {cell(v['urteil'])}",
              f"- **Wichtigste Unsicherheit:** {cell(v['wichtigste_unsicherheit'])}",
              f"- **Punktebegründung:** {cell(v['punkte_begruendung'])}",
              f"- **Produkt:** {cell(m['produktdefinition'])}",
              f"- **Kaufanlass und Timing:** {cell(m['kaufanlass_und_timing'])}",
              f"- **Zielgruppe und DE-Größe:** {cell(m['zielgruppe_und_groesse_de'])}",
              f"- **Warenkorb laut Markt:** {cell(m['markt_warenkorb'])}",
              f"- **Wiederkauf und Produktwelt:** {cell(m['wiederkauf'])}",
              f"- **Wettbewerb (Ampel {m['wettbewerbs_ampel']} laut Marktanalyse):** {cell(m['ampel_begruendung'])}",
              f"- **Einstiegschance:** {cell(m['einstiegschance'])}",
              f"- **Kanäle der Wettbewerber:** {cell(m['kanaele'])}",
              f"- **KI:** Schwierigkeit {kd['technische_schwierigkeit_1bis5']}/5; Vorschau {cell(kd['generierungen_vorschau'], 400)}; Käufer {cell(kd['generierungen_kaeufer'], 400)}; "
              f"Kosten je Vorschau-Sitzung ca. {de(kd['kosten_vorschau_sitzung_eur'], 2)} €, je Käufer ca. {de(kd['kosten_finalisierung_kaeufer_eur'], 2)} €; Nachbearbeitung: {cell(kd['manuelle_nachbearbeitung_wahrscheinlichkeit'], 600)}; "
              f"Konsistenzrisiken: {cell(kd['konsistenz_risiken'])}",
              f"- **Social-Creative-Potenzial:** {p['social']['creative_potenzial_1bis10']}/10 – {cell(p['social']['begruendung'])}",
              f"- **Produktion:** {cell(p['produktionsweg_fazit'])}",
              f"- **Rechtliche Besonderheiten:** {cell(p['recht_besonderheiten'])}", "",
              "**Stärkste Gegenargumente (Prüfer):**", ""]
        L += [f"{i}. {NUM_RE.sub('', cell(g))}" for i, g in enumerate(v["staerkste_gegenargumente"], 1)]
        L += ["", "**Nachgeprüfte Aussagen:**", "", "| Aussage | Ergebnis | Befund | Quelle |", "|---|---|---|---|"]
        for a in v["gepruefte_aussagen"]:
            L.append(f"| {cell(a['aussage'], 500)} | {a['ergebnis']} | {cell(a['befund'])} | {cell(a.get('url', ''), 400)} |")
        L += ["", f"**Offene Punkte:** {cell(m['offene_punkte'])} {cell(p['offene_punkte'])}", "", "---", ""]
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
        L.append(f"| **{k['id']}** {cell(k['titel'], 200)} | {zelle_g(g[0])} | {zelle_g(g[1]) if len(g) > 1 else '–'} | {rang.get(k['id'], {}).get('rang', '–')}. {rang.get(k['id'], {}).get('status', '–')} |")
    L += ["", f"**Gesamtfazit des Urteils:** {cell(nz['urteil']['gesamtfazit'])}", "",
          f"**Zuerst testen:** {cell(nz['urteil']['zuerst_testen'])}", "",
          f"**Lehren über alle Kandidaten:** {cell(nz['urteil']['querschnitt_lehren'])}", ""]
    for k in nz["kandidaten"]:
        n = k["neuzuschnitt"]
        r = rang.get(k["id"], {})
        L += [f"## {k['id']}. {k['titel']} – Neuzuschnitt", "",
              f"**Urteil:** {r.get('status', '–')} – {cell(r.get('begruendung', ''))}", "",
              f"**Neuzuschnitt:** {cell(n['neuzuschnitt_kurz'])}", "",
              f"**Angebotsarchitektur:** {cell(n['angebotsarchitektur'])}", "",
              "**Änderungen gegenüber der Vertiefung:**", ""]
        L += [f"- {cell(a['was'])} – *Warum:* {cell(a['warum'], 600)} – *Beleg:* {cell(a['beleg'])}" for a in n["aenderungen"]]
        L += ["", "**Kanalmix (Neuzuschnitt, vor Korrektur durch die Prüfer):**", "", "| Kanal | Anteil Neukunden (Basis) | CAC | Herleitung | Label |", "|---|---:|---:|---|---|"]
        L += [f"| {cell(c['kanal'], 200)} | {de(c['anteil_neukunden_basis'] * 100)} % | {de(c['cac_eur'])} € | {cell(c['herleitung'])} | {cell(c['label'], 200)} |" for c in n["kanalmix"]]
        L += ["", f"**Herleitung blended CAC:** {cell(n['blended_cac_herleitung'])}", ""]
        for g in k["gegenpruefung"]:
            L += [f"### Gegenprüfung: {cell(g['linse'], 240)}", "",
                  f"**{g['punkte_gesamt_100']}/100**, Datensicherheit {g['datensicherheit']}, Ampel {g['ampel']}, finalisttauglich: {'ja' if g['finalist_tauglich'] else 'nein'}", "",
                  f"- **Urteil:** {cell(g['urteil'])}", f"- **Bedingungen, unter denen es trägt:** {cell(g['bedingungen'])}",
                  f"- **Modellrechnung:** {cell(g['modellergebnis'])}", "", "**Einwände:**", ""]
            L += [f"{i}. {NUM_RE.sub('', cell(e))}" for i, e in enumerate(g["einwaende"], 1)]
            L += ["", "| Geprüfte Aussage | Ergebnis | Befund | Quelle |", "|---|---|---|---|"]
            L += [f"| {cell(a['aussage'], 400)} | {a['ergebnis']} | {cell(a['befund'], 700)} | {cell(a.get('url', ''), 320)} |" for a in g["gepruefte_punkte"]]
            L.append("")
        L += ["---", ""]
    return L


def wettbewerber(kand):
    L = ["# Wettbewerber je Shortlist-Kandidat", "",
         "Recherchedatum 01.10.2026. Erzeugt aus den Marktanalysen und den Ergänzungen des adversarialen Prüfers. "
         "Bewertungen sind keine Bestellungen; Bewertungszähler laufen weiter (Stand Abruf). Typen: Generalist, Spezialist, Atelier/Handarbeit, "
         "Marktplatz-Händler, Produktionspartner mit B2C-Angebot, DIY-Werkzeug, Nicht-KI-Alternative.", "",
         "**Hinweis:** Diese Datei gibt die Rohbefunde der Recherche-Agenten wieder (ungekürzt, mit ihren Kennzeichnungen). Tragende Aussagen wurden danach im Faktencheck geprüft (`rohdaten/faktencheck.json`); wo Abweichungen gefunden wurden, gilt die korrigierte Fassung in `bericht.md`, `finalisten.md` und `quellen.md`. Wertende Sätze der Agenten (z. B. zu Ursachen einer Insolvenz oder „frei werdender Nachfrage“) sind Einschätzungen, keine Belege.", "",
         "**Nachrecherche (nach dieser Datei):** Wettbewerber und Fallzahlen in AT und CH, KI-Hochzeitswerkzeuge in DE (MYPOSTER, WeddingPersonalCard, Lovart, Pixazo, Fotor) sowie Etsy-, Social-Commerce- und Shark-Tank-Daten wurden für die beiden Finalisten-Kategorien nachgeholt. "
         "Sie stehen in `finalisten.md` (Abschnitte 3, 5, 6 und Reserve), in `quellen.md` Abschnitt 7 und als Rohdaten in `rohdaten/nachrecherche-luecken.json`.", "",]
    for k in kand:
        m, v = k["markt"], k["pruefer"]
        L += [f"## {k['id']}. {k['titel']}", "",
              f"Wettbewerbsampel Marktanalyse: **{m['wettbewerbs_ampel']}** – Prüfer: **{v['ampel']}**. {cell(m['ampel_begruendung'])}", "",
              "| Anbieter | Land | Typ | Angebot/Bundles | Preise | Lieferzeit | Qualität | Personalisierung | Vorschau | Branding | Bewertungen | Größe | Social | KI | Stärken/Schwächen |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for w in m["wettbewerber"]:
            L.append(f"| [{cell(w['name'], 200)}]({w['url']}) | {cell(w['land'], 200)} | {cell(w['typ'], 200)} | {cell(w['angebot_und_bundles'], 440)} | {cell(w['preise'], 440)} | "
                     f"{cell(w.get('lieferzeit', '–'), 200)} | {cell(w.get('qualitaet', '–'), 240)} | {cell(w['personalisierungsgrad'], 240)} | {cell(w['vorschau'], 200)} | "
                     f"{cell(w.get('branding', '–'), 200)} | {cell(w['bewertungen'], 320)} | {cell(w.get('groesse', '–'), 280)} | {cell(w.get('social_media', '–'), 200)} | "
                     f"{cell(w.get('ki_einsatz', '–'), 200)} | {cell(w.get('staerken_schwaechen', '–'), 400)} |")
        if v["uebersehene_wettbewerber"]:
            L += ["", "**Vom Prüfer ergänzt (übersehen):**", ""]
            L += [f"- [{w['name']}]({w['url']}): {cell(w['relevanz'])}" for w in v["uebersehene_wettbewerber"]]
        L += ["", f"**Etsy/Amazon:** {cell(m['etsy_amazon'])}", "",
              f"**Nicht-KI-Alternativen mit gleichem Nutzen:** {cell(m['nicht_ki_alternativen'])}", "",
              "**US-Vorbilder:**", ""]
        for u in m["us_vorbilder"]:
            L.append(f"- [{u['name']}]({u['url']}): {cell(u['produkt_preise'], 500)} – Größe: {cell(u['groessenbeleg'])} – KI: {cell(u.get('nutzt_ki', '–'), 240)} – Übertragbar: {cell(u.get('uebertragbar', '–'), 400)}")
        L += ["", "---", ""]
    open(os.path.join(ROOT, "wettbewerber.md"), "w", encoding="utf-8").write("\n".join(L))


def produktionspartner(kand):
    L = ["# Produktionspartner je Shortlist-Kandidat", "",
         "Recherchedatum 01.10.2026. Erzeugt aus den Produktionsanalysen. Status je Prüfpunkt: „Auf der Website bestätigt“ / "
         "„Vom Anbieter beworben, nicht praktisch überprüft“ / „Noch anzufragen“. Es wurden keine Musterbestellungen, Registrierungen oder Kontaktaufnahmen durchgeführt; "
         "Konditionen hinter Login oder auf Anfrage sind deshalb offen. Preise netto, sofern nicht anders angegeben.", "",
         "**Hinweis:** Diese Datei gibt die Rohbefunde der Recherche-Agenten wieder (ungekürzt, mit ihren Kennzeichnungen). Tragende Aussagen wurden danach im Faktencheck geprüft (`rohdaten/faktencheck.json`); wo Abweichungen gefunden wurden, gilt die korrigierte Fassung in `bericht.md`, `finalisten.md` und `quellen.md`. Wertende Sätze der Agenten (z. B. zu Ursachen einer Insolvenz oder „frei werdender Nachfrage“) sind Einschätzungen, keine Belege.", "",
         "**Korrektur nach der Nachrecherche:** WIRmachenDRUCK erlaubt laut FAQ Nr. 188 im Checkout einen neutralen Absender, für den ganzen Warenkorb oder je Produkt (Auf der Website bestätigt). "
         "Die Angaben „Neutralversand nicht dokumentiert“ unten sind damit überholt; offen bleibt, ob Karton und Lieferschein WMD-Branding tragen. "
         "Partner in PL, CZ, AT und NL (Colours Factory mit Printendo/Drukomat/JustPrint, Piga, Caro Group, DIMEX, druck.at, Saxoprint, Probo) wurden nachträglich geprüft: `finalisten.md` Abschnitt 9 und Reserve, `rohdaten/nachrecherche-luecken.json`.", "",]
    index = {}
    for k in kand:
        p = k["produktion"]
        L += [f"## {k['id']}. {k['titel']}", "", f"**Fazit Produktionsweg:** {cell(p['produktionsweg_fazit'])}", "",
              "| Partner | Produktionsort | Produkte | ab 1 Stück | Direktversand | Neutral/White Label | Shopify | WooCommerce | API | Datei je Bestellung | Produktionszeit | Versand DE | Einkaufspreise | Versandkosten | Material/Größen | Reklamation | Status | Spezialhersteller |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for t in p["partner"]:
            index.setdefault(t["name"], set()).add(k["id"])
            L.append(f"| [{cell(t['name'], 200)}]({t['url']}) | {cell(t['land_produktionsort'], 200)} | {cell(t['produkte'], 240)} | {cell(t['ab_stueck_1'], 200)} | {cell(t['direktversand'], 200)} | "
                     f"{cell(t['white_label_neutral'], 200)} | {cell(t['shopify'], 200)} | {cell(t['woocommerce'], 200)} | {cell(t['api'], 200)} | {cell(t['datei_je_bestellung'], 200)} | "
                     f"{cell(t['produktionszeit'], 200)} | {cell(t['versandzeit_de'], 200)} | {cell(t['einkaufspreise'], 440)} | {cell(t['versandkosten'], 240)} | {cell(t['materialien_groessen'], 320)} | "
                     f"{cell(t['reklamation'], 240)} | {cell(t['status'], 480)} | {'ja' if t['spezialhersteller_schwer_skalierbar'] else 'nein'} |")
        L += ["", "**Angebote und Stücklisten (Vorschlag der Produktionsanalyse):**", ""]
        for a in p["angebote"]:
            L += [f"*{a['name']}* – Vorschlag {de(a['preis_brutto_vorschlag'], 2)} € brutto; Versand {de(a['versand_netto_eur'], 2)} € netto in {de(a['sendungen'])} Sendung(en); {de(a['produktionsdateien'])} Produktionsdatei(en)", "",
                  "| Artikel | Menge | Partner | Einkauf netto/Stück | Label | Quelle |", "|---|---:|---|---:|---|---|"]
            for b in a["bestandteile"]:
                L.append(f"| {cell(b['artikel'], 200)} | {de(b['menge'], 0)} | {cell(b['partner'], 200)} | {de(b['einkauf_netto_eur_je_stueck'], 2)} € | {b['label']} | {cell(b['quelle'], 320)} |")
            L.append("")
        if p["upsells"]:
            L += ["**Upsells:**", ""]
            L += [f"- {u['name']}: {de(u['preis_brutto_vorschlag'], 2)} € brutto, Einkauf {de(u['einkauf_netto_eur'], 2)} € netto, Quote-Annahme {de(u['quote_annahme'] * 100)} % – {cell(u.get('quelle', ''), 400)}" for u in p["upsells"]]
            L.append("")
        L += ["**KI-Pipeline:**", ""] + [f"{i}. {NUM_RE.sub('', cell(s))}" for i, s in enumerate(p["ki_pipeline"], 1)]
        kd = p["ki_details"]
        L += ["", f"Modelle und Preise: {cell(kd['modelle_und_preise'])}", "", f"Automatisierung: {cell(kd['automatisierung'])}", "",
              f"**Kostenlose Vorschau:** Wow-Effekt: {cell(p['kostenlose_vorschau']['wow_effekt'], 600)} Kosten: {cell(p['kostenlose_vorschau']['kosten_je_vorschau'], 400)} "
              f"Missbrauch: {cell(p['kostenlose_vorschau']['missbrauchsrisiko'], 500)} Wasserzeichen: {cell(p['kostenlose_vorschau']['wasserzeichen'], 400)} "
              f"Gratis-Varianten: {cell(p['kostenlose_vorschau']['gratis_varianten'], 300)} E-Mail vorab: {cell(p['kostenlose_vorschau']['email_vor_vorschau'], 400)} "
              f"Empfehlung: {cell(p['kostenlose_vorschau']['empfehlung'])}", "", "---", ""]
    L += ["## Partnerindex", "", "| Partner | genutzt bei Kandidat |", "|---|---|"]
    for n in sorted(index):
        L.append(f"| {cell(n, 200)} | {', '.join(sorted(index[n]))} |")
    open(os.path.join(ROOT, "produktionspartner.md"), "w", encoding="utf-8").write("\n".join(L))


def main():
    kand, end = lade()
    shortlist(kand, end)
    wettbewerber(kand)
    produktionspartner(kand)
    print(f"shortlist.md, wettbewerber.md, produktionspartner.md geschrieben ({len(kand)} Kandidaten)")


if __name__ == "__main__":
    main()
