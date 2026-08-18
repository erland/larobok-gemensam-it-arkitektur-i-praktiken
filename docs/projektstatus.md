# Projektstatus

## Bok
- Titel: Gemensam IT-arkitektur i praktiken
- Språk: svenska
- Författare: Erland Lindmark
- Version: 0.1
- book_kind: factbook
- book_type: subject_overview

## Nuvarande fas
Skrivfas – del I och II kompletta i första utkast; del III pågår

## Kapitelstatus
| Kapitel | Titel | Status | Kommentar |
|---:|---|---|---|
| 0 | Inledning | Första utkast | Ska slutredigeras när resten av boken är färdig. |
| 1 | Varför gemensam IT-arkitektur? | Första utkast | Problem- och målbild etablerad; slutredigeras efter del I. |
| 2 | En arkitektur av flera lager | Första utkast | Helhetsmodell, abstraktionsnivåer, förändringstakt och spårbarhet etablerade. |
| 3 | Behov före teknik | Första utkast | Behov, constraints, teknikoberoende formuleringar, path dependency och arkitekturell teknikskuld etablerade. |
| 4 | Kvalitetsattribut som arkitekturens drivkrafter | Första utkast | Kravkedja, kvalitetsattributsscenarier, tolv kvalitetsdimensioner, RTO/RPO, trade-offs och verifiering etablerade. |
| 5 | Arkitekturbeslut och trade-offs | Första utkast | Beslutsdrivare, alternativ, trade-offs, ADR, riskacceptans, teknisk skuld, reversibilitet och omprövning etablerade. |
| 6 | Arkitekturprinciper som beslutsstöd | Första utkast | Principers roll, egenskaper hos användbara principer, tio gemensamma exempel, nivåindelning och relation till beslut, standarder och plattformar etablerade. |
| 7 | Att etablera modellen – ordning, ansvar och iteration | Första utkast | Nio-stegs etableringssekvens, tredelad ansvarmodell, beslutets räckvidd, top-down/bottom-up och iterativ etablering etablerade. |
| 8 | Vad är en IT-förmåga? | Första utkast | Distinktion mellan gemensam IT-förmåga, verksamhetsförmåga, tjänst, produkt, team, kompetens och kapacitet etablerad. |
| 9 | När något bör vara gemensamt | Första utkast | Bedömningsmodell för gemensamt, federerat och lokalt ansvar etablerad med skala, risk, kompetens, interoperabilitet, standardiserbarhet och differentiering som centrala drivkrafter. |
| 10 | Domäner, ansvar och gränser | Första utkast | Domänansvar, bounded context, cohesion/coupling, informationsägarskap och gränsen mellan gemensamma mekanismer och verksamhetslogik etablerade. |
| 11 | Information och data som arkitekturella ingångsvärden | Första utkast | Informationsbehov, semantik, informationsmodell, informationsägarskap, auktoritativ källa, master-/referensdata, data contracts, klassning och livscykel etablerade. |
| 12 | Interaktion, presentation och kanaler | Första utkast | Användningssituation, kanalval, design system, klientansvar, tillgänglighet, klient/backend-gräns, BFF som möjlig struktur, säkerhet och tekniklivscykel etablerade. |
| 13–37 | Se kapitelplan | Planerade | Ej skapade ännu. |

## Faktakontroll
- Öppna verifieringspunkter: se `docs/faktakontroll.md`
- Senast genomgången: 2026-08-18

## Öppna beslut
- Omslagskoncept och eventuell omslagsbild.
- Om slututgåvan ska ha synlig källförteckning/notapparat.
- Om arkitekturdiagram ska skapas successivt eller i en separat illustrationsfas.
- Slutlig målomfattning efter att 3–5 provkapitel skrivits.

## Nästa rekommenderade steg
- Kapitelplanen har helhetsgranskats för överlapp, kompletterats med ett explicit etableringskapitel och genomgått en slutlig förskrivningskontroll; aktuell plan är 37 kapitel före skrivstart.
- Tredelningen gemensam arkitektur → förmågeområde → lösning/produkt är nu en bärande ansvarmodell genom boken.
- Kapitel 1–7 är skapade som första utkast; del I är därmed komplett i första utkast.
- Gemensam överlapps- och terminologikontroll av kapitel 1–7 är genomförd inför del II; inga omskrivningar av del I bedömdes nödvändiga.
- Kapitel 8 – Vad är en IT-förmåga? är skapat som första utkast och etablerar den precisa begreppsgrunden för förmågedelen.
- Kapitel 9 – När något bör vara gemensamt är skapat som första utkast och etablerar kriterier för gemensamt, federerat och lokalt ansvar.
- Kapitel 10 – Domäner, ansvar och gränser är skapat som första utkast och etablerar skillnaden mellan gemensamma IT-förmågor och verksamhetsdomäner samt principer för ansvar, bounded contexts och coupling.
- Kapitel 11 – Information och data som arkitekturella ingångsvärden är skapat som första utkast och etablerar semantik, informationsägarskap, auktoritativa källor, data contracts, klassning och livscykel före tekniska lagringsval.
- Del II är därmed komplett i första utkast.
- Kort överlapps- och terminologikontroll av kapitel 8–11 är genomförd inför del III; inga omskrivningar bedömdes nödvändiga.
- Kapitel 12 – Interaktion, presentation och kanaler är skapat som första utkast och inleder del III med gemensamma principer för användningssituation, kanalval, design system, klientarkitektur och ansvar mot andra förmågor.
- Nästa steg: skriv Kapitel 13 – Process, workflow och ärendehantering.
- Kapitel 7 har gjort etableringsordning, ansvarssnitt och iterativt arbetssätt praktiskt tydliga.
- Använd avgränsningsreglerna i `docs/kapitelplan.md` när kapitel skapas så att senare delar fördjupar i stället för att upprepa.
