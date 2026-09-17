# SOFACOMPANY DACH — Analyse der Google-Bewertungen

**Fragestellung:** Welche DACH-Filiale der SOFACOMPANY hat im Zeitraum **01.06.2026 – 31.08.2026** die meisten Google-Bewertungen erhalten?

**Stand der Recherche:** 17.09.2026

---

## 1. Kernergebnis

**Die Frage lässt sich mit öffentlich zugänglichen Daten nicht beantworten.** Eine Rangfolge „meiste Google-Bewertungen im Quartal Juni–August 2026" würde voraussetzen, dass für jede Filiale die **Einzelbewertungen mit Datum** vorliegen. Diese Daten gibt Google öffentlich nicht heraus:

- Google Maps zeigt im Interface nur **relative Datumsangaben** („vor 2 Monaten"), keine exakten Zeitstempel.
- Die offizielle **Places API (New)** liefert pro Standort **maximal 5 Bewertungen** — damit ist eine Zählung über ein Quartal strukturell unmöglich.
- Die **Google Business Profile API** liefert vollständige Bewertungen mit exaktem `createTime` — setzt aber **Inhaber- bzw. Verwaltungszugriff** auf die Standorte voraus.

Ich habe **bewusst keine Zahlen geschätzt oder aus Drittanbieter-Portalen hochgerechnet.** Die dort gespiegelten Werte (Cybo, 11880, golocal, werkenntdenbesten u. a.) sind Gesamtsummen unbekannten Alters, teils veraltet, und lassen keinen Rückschluss auf einen konkreten Drei-Monats-Zeitraum zu. Eine daraus gebildete Rangfolge wäre eine Scheingenauigkeit.

**Was dafür belastbar geliefert wird:** die vollständige, aus der offiziellen Unternehmensdatenbank verifizierte Filialliste als Grundgerüst der Analyse (Abschnitt 3) — plus der konkrete Weg zur Beantwortung (Abschnitt 5).

---

## 2. Wichtige Korrektur zur Fragestellung: „DACH" = DE + CH

Die Annahme „DACH-Filialen" trifft auf SOFACOMPANY nur eingeschränkt zu:

> **SOFACOMPANY betreibt in Österreich keinen einzigen Showroom.**

Die österreichische Präsenz besteht ausschließlich aus einem **Online-Shop** (`sofacompany.com/de-at`) und einem **Customer-Service-Eintrag** (`CS0801`). Der einzige Standort-Datensatz, der in der Unternehmensdatenbank dem Land `AT` zugeordnet ist, verweist auf die **Adresse des Münchner Showrooms** (Sonnenstraße 22) und ist als inaktiv markiert (`status=0`) — ein Verweiseintrag für österreichische Kund:innen, keine eigene Filiale.

Der Auswertungsraum „DACH" umfasst damit faktisch **14 Filialen in 2 Ländern**: 11 in Deutschland, 3 in der Schweiz.

---

## 3. Die 14 DACH-Filialen (verifiziert)

Quelle: offizielle Store-Locator-Datenbank von SOFACOMPANY, abgefragt über die öffentliche GraphQL-Schnittstelle `sofacompany.com/graphql` (Feld `sc_storelocator`, Storefront-Kontext `de_de`). Alle aufgeführten Standorte haben `status=1` und hinterlegte Öffnungszeiten, sind also im Betrieb.

| Land | Filiale | Adresse | Code | Links |
|---|---|---|---|---|
| DE | **Berlin Charlottenburg** | Lietzenburger Straße 76, 10719 Berlin | `STR0412` | [Maps](https://www.google.com/maps/search/SOFACOMPANY%20Lietzenburger%20Stra%C3%9Fe%2076%2C%2010719%20Berlin) · [Filialseite](https://sofacompany.com/de-de/storelocator/showroom-charlottenburg) |
| DE | **Berlin Mitte** | Leipziger Straße 54, 10117 Berlin | `STR0401` | [Maps](https://www.google.com/maps/search/SOFACOMPANY%20Leipziger%20Stra%C3%9Fe%2054%2C%2010117%20Berlin) · [Filialseite](https://sofacompany.com/de-de/storelocator/berlin-showroom) |
| DE | **Düsseldorf** | Erkrather Straße 228a, 40233 Düsseldorf | `STR0405` | [Maps](https://www.google.com/maps/search/SOFACOMPANY%20Erkrather%20Stra%C3%9Fe%20228a%2C%2040233%20D%C3%BCsseldorf) · [Filialseite](https://sofacompany.com/de-de/storelocator/dusseldorf-showroom) |
| DE | **Essen** | Huyssenallee 82, 45128 Essen | `STR0410` | [Maps](https://www.google.com/maps/search/SOFACOMPANY%20Huyssenallee%2082%2C%2045128%20Essen) · [Filialseite](https://sofacompany.com/de-de/storelocator/showroom-essen) |
| DE | **Frankfurt** | Große Friedberger Str. 33-35, 60313 Frankfurt | `STR0409` | [Maps](https://www.google.com/maps/search/SOFACOMPANY%20Gro%C3%9Fe%20Friedberger%20Str.%2033-35%2C%2060313%20Frankfurt) · [Filialseite](https://sofacompany.com/de-de/storelocator/showroom-frankfurt) |
| DE | **Hamburg Altona** | Große Elbstraße 86, 22767 Hamburg | `STR0403` | [Maps](https://www.google.com/maps/search/SOFACOMPANY%20Gro%C3%9Fe%20Elbstra%C3%9Fe%2086%2C%2022767%20Hamburg) · [Filialseite](https://sofacompany.com/de-de/storelocator/hamburg-altona) |
| DE | **Hamburg Eppendorf** | Eppendorfer Landstraße 112A, 20249 Hamburg | `STR0411` | [Maps](https://www.google.com/maps/search/SOFACOMPANY%20Eppendorfer%20Landstra%C3%9Fe%20112A%2C%2020249%20Hamburg) · [Filialseite](https://sofacompany.com/de-de/storelocator/showroom-hamburg-eppendorf) |
| DE | **Köln** | Hohenstaufenring 42, 50672 Köln | `STR0406` | [Maps](https://www.google.com/maps/search/SOFACOMPANY%20Hohenstaufenring%2042%2C%2050672%20K%C3%B6ln) · [Filialseite](https://sofacompany.com/de-de/storelocator/koln-showroom) |
| DE | **Leipzig** | Paunsdorfer Allee 1, 04329 Leipzig | `STR0407` | [Maps](https://www.google.com/maps/search/SOFACOMPANY%20Paunsdorfer%20Allee%201%2C%2004329%20Leipzig) · [Filialseite](https://sofacompany.com/de-de/storelocator/showroom-leipzig) |
| DE | **München** | Sonnenstraße 22, 80331 München | `STR0402` | [Maps](https://www.google.com/maps/search/SOFACOMPANY%20Sonnenstrasse%2022%2C%2080331%20M%C3%BCnchen) · [Filialseite](https://sofacompany.com/de-de/storelocator/munich-showroom) |
| DE | **Stuttgart** | Thouretstraße 6, 70173 Stuttgart | `STR0408` | [Maps](https://www.google.com/maps/search/SOFACOMPANY%20Thouretstra%C3%9Fe%206%2C%2070173%20Stuttgart) · [Filialseite](https://sofacompany.com/de-de/storelocator/filiale-stuttgart) |
| CH | **Basel** | Falknerstrasse 11, 4001 Basel | `STR0503` | [Maps](https://www.google.com/maps/search/SOFACOMPANY%20Falknerstrasse%2011%2C%204001%20Basel) · [Filialseite](https://sofacompany.com/de-de/storelocator/showroom-basel) |
| CH | **Bern** | Laupenstrasse 10, 3008 Bern | `STR0501` | [Maps](https://www.google.com/maps/search/SOFACOMPANY%20Laupenstrasse%2010%2C%203008%20Bern) · [Filialseite](https://sofacompany.com/de-de/storelocator/bern-showroom) |
| CH | **Zürich** | Räffelstrasse 26, 8045 Zürich | `STR0502` | [Maps](https://www.google.com/maps/search/SOFACOMPANY%20R%C3%A4ffelstrasse%2026%2C%208045%20Z%C3%BCrich) · [Filialseite](https://sofacompany.com/de-de/storelocator/showroom-zurich) |

**Hinweise zur Interpretation:**

- **Zwei Standorte je Stadt** in Berlin (Mitte + Charlottenburg) und Hamburg (Altona + Eppendorf). Beide haben jeweils ein **eigenes Google-Business-Profil** — bei der Auswertung dürfen sie nicht zusammengefasst werden, sonst verzerrt sich die Rangfolge zugunsten dieser beiden Städte.
- **Filialalter verzerrt Zeitraum-Vergleiche.** Frankfurt (eröffnet Anfang 2026) und Hamburg Eppendorf sind die jüngsten Standorte. Junge Filialen sammeln in den ersten Monaten überdurchschnittlich viele Bewertungen (Eröffnungs-Peak, aktive Bewertungsaufforderung), während etablierte Standorte wie Berlin Mitte oder Hamburg Altona auf einem stabileren Niveau liegen. Die absolute Zahl im Quartal ist deshalb **kein** Qualitätsindikator — für einen fairen Vergleich sollte zusätzlich „Bewertungen pro Monat seit Eröffnung" ausgewiesen werden.
- **Leipzig** liegt als einziger Standort in einem Einkaufszentrum (Paunsdorf Center) — deutlich höhere Passantenfrequenz, was das Bewertungsaufkommen strukturell beeinflusst.

---

## 4. Methodik: Was geprüft wurde

| Datenquelle | Ergebnis |
|---|---|
| SOFACOMPANY GraphQL `sc_storelocator` | ✅ **Erfolgreich** — vollständige, offizielle Filialliste (60 Standorte weltweit, davon 14 DACH) inkl. Adressen, Geokoordinaten, Öffnungszeiten, Status |
| Google Maps Web-UI (`/maps/place/…`) | ❌ Reine JavaScript-Shell, keine Bewertungsdaten im HTML |
| Google Maps Review-RPC (`/maps/rpc/listugcposts`) | ❌ HTTP 403 — auch mit Consent-Cookies und vollständigen Browser-Headern |
| Google Maps Legacy-Review-API (`listentitiesreviews`) | ❌ HTTP 404 — Endpunkt abgeschaltet |
| Google-Suche Review-Dialog (`/async/reviewDialog`) | ❌ HTTP 404 — Endpunkt abgeschaltet |
| Google Places API | ❌ Kein API-Key verfügbar; liefert zudem prinzipbedingt nur 5 Bewertungen/Standort |
| Google-Suche (Knowledge Panel) | ❌ JavaScript-gerendert, Ergebnisse nicht auslesbar |
| Browser-Automatisierung (Playwright/Chromium) | ❌ Nicht durchführbar — in dieser Session fehlt Chromium das Vertrauen in die Proxy-CA; die beiden möglichen Abhilfen (SPKI-Pinning, Installation von `libnss3-tools`) wurden von der Berechtigungsprüfung blockiert |
| Drittanbieter-Portale (11880, golocal, Cybo, werkenntdenbesten) | ⚠️ Nur Gesamtsummen unbekannten Alters, keine datierten Einzelbewertungen — **für die Fragestellung unbrauchbar** |
| Trustpilot | ⚠️ Datierte Bewertungen vorhanden, aber **shop-, nicht filialbezogen** (`de.sofacompany.com` / `ch.sofacompany.com`) — kein Filialvergleich möglich |

---

## 5. Wie die Frage beantwortet werden kann

Drei gangbare Wege, nach Belastbarkeit sortiert:

### Option A — Google Business Profile API *(exakt, wenn Zugriff besteht)*
Die einzige Quelle mit **vollständigen** Bewertungen und exaktem Zeitstempel (`createTime`). Über `accounts.locations.reviews.list` lassen sich alle Bewertungen je Standort abrufen und exakt nach Datum filtern.
- **Voraussetzung:** Inhaber- oder Verwaltungszugriff auf die SOFACOMPANY-Standorte (also Zugang über das Unternehmen selbst oder eine beauftragte Agentur).
- **Kosten:** keine. **Ergebnis:** tagesgenau, vollständig, revisionssicher.

### Option B — Kommerzieller Maps-Scraping-Dienst *(praktikabel ohne Inhaberzugriff)*
Anbieter wie SerpApi, Outscraper, DataForSEO oder Apify liefern alle Bewertungen je Place-ID inkl. Zeitstempel.
- **Voraussetzung:** API-Key (kostenpflichtig).
- **Aufwand:** 14 Standorte × Bewertungsabruf — im einstelligen bis niedrigen zweistelligen Euro-Bereich.
- **Genauigkeit:** hoch; je nach Anbieter exakte oder auf den Tag normalisierte Zeitstempel.
- **Hinweis:** Das Scraping von Google Maps bewegt sich außerhalb der Google-Nutzungsbedingungen — die Entscheidung liegt beim Auftraggeber.

### Option C — Manuelle Erhebung *(kostenlos, aber unscharf)*
Je Filiale Google Maps öffnen, Bewertungen nach **„Neueste"** sortieren und bis über das Zeitfenster hinaus zählen.
- **Aufwand:** ca. 10–15 Minuten für alle 14 Standorte.
- **Einschränkung:** Google zeigt nur relative Daten („vor 3 Monaten"). Für das Fenster 01.06.–31.08.2026 heißt das, gemessen am 17.09.2026: relevant sind grob die Einträge zwischen „vor 3 Wochen" und „vor 3–4 Monaten". **Die Ränder bleiben unscharf** — für eine reine Rangfolge reicht das meist, für exakte Zahlen nicht.

**Empfehlung:** Besteht Zugriff auf die Google-Business-Profile, ist **Option A** in jeder Hinsicht überlegen. Andernfalls liefert **Option B** in kurzer Zeit ein belastbares Ergebnis; **Option C** taugt als schnelle Plausibilitätsprüfung.

Sobald die Rohdaten vorliegen, ist die Auswertung trivial: Bewertungen je `place_id` auf das Fenster 01.06.2026–31.08.2026 filtern, gruppieren, zählen — sinnvollerweise ergänzt um Durchschnittsnote im Zeitraum und um die oben genannte Normierung „Bewertungen pro Monat seit Eröffnung".

---

## 6. Quellen

- [SOFACOMPANY Store-Locator Deutschland](https://sofacompany.com/de-de/storelocator) · [Schweiz](https://sofacompany.com/de-ch/storelocator) · [Österreich](https://sofacompany.com/de-at/storelocator)
- Offizielle GraphQL-Schnittstelle `sofacompany.com/graphql`, Feld `sc_storelocator` (Primärquelle der Filialliste)
- [MÖBELMARKT: Sofacompany — Sechster Showroom in Leipzig](https://www.moebelmarkt.de/beitrag/sofacompany-sechster-showroom-in-leipzig) (26.05.2023)
- [möbelkultur: Sofacompany — Expansion trotz Umsatzrückgang](https://www.moebelkultur.de/news/expansion-trotz-umsatzrueckgang/)
- [Google Business Profile API — Reviews](https://developers.google.com/my-business/reference/rest/v4/accounts.locations.reviews/list)
- [Google Places API (New) — Place Details](https://developers.google.com/maps/documentation/places/web-service/place-details) (Bewertungslimit: 5 pro Standort)
