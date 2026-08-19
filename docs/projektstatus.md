# Projektstatus

## Bok
- Titel: Gemensam IT-arkitektur i praktiken
- Språk: svenska
- Författare: Erland Lindmark
- Version: 0.1
- book_kind: factbook
- book_type: subject_overview

## Nuvarande fas
Skrivfas – del I–IV kompletta i första utkast; del V står näst på tur

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
| 13 | Process, workflow och ärendehantering | Första utkast | Långlivade processer, human tasks, case management, process-/domängräns, orkestrering/koreografi, versionshantering och återupptagning etablerade. |
| 14 | Regler och beslut | Första utkast | Externalisering, beslutstabeller, DMN, beslutstjänster, versions-/giltighetsmodell, spårbarhet, förklarbarhet, test/simulering och gränsen mot process, domänlogik och AI etablerade. |
| 15 | Data- och informationshantering | Första utkast | Teknisk datahantering, lagring, konsistens, härledda kopior, cache, historik, retention, schemaevolution, migrering och återställningsbehov etablerade. |
| 16 | Analys, sökning och AI | Första utkast | Sökning, BI/analys, ML, generativ AI, RAG, human-in-the-loop, utvärdering, agentrisker och ansvarsnivåer etablerade. |
| 17 | Integration och kommunikation | Första utkast | Synkron/asynkron kommunikation, API, messaging, events, filutbyte, kontrakt, leveransbeteende, koppling, felhantering och ansvarsnivåer etablerade. |
| 18 | Identitet och tillit | Första utkast | Autentisering/auktorisation, workforce identity, federation, tjänsteidentitet, PKI, secrets, privilegierad åtkomst, tokenhantering och identitetslivscykel etablerade. |
| 19 | Applikationsexekvering och runtime | Första utkast | Workload-egenskaper, container/VM/runtimeprofiler, stateless/stateful, resursprofil, skalning, isolering, konfiguration, portabilitet och livscykel etablerade. |
| 20 | Driftbarhet och motståndskraft | Första utkast | Observability, SLI/SLO, larm, felisolering, recovery, backup/restore, RPO/RTO, DR, runbooks, kapacitet och operativ återkoppling etablerade. |
| 21 | Programvaruutveckling och leverans | Första utkast | SCM, reproducerbara builds, CI/CD, artefakter, build once/promote many, software supply chain, SBOM/provenance, signering, developer experience och ansvarsnivåer etablerade. |
| 22 | Arbetsplats, samarbete och produktivitet | Första utkast | Generell produktivitet kontra verksamhetssystem, samarbetsytor, low-code/citizen development, produktivitets-AI och ansvarsnivåer etablerade. |
| 23 | Lösningsmönster som återanvändbara beslut | Första utkast | Mönster som återanvändbar beslutserfarenhet, kontext/problem/forces, konsekvenser, variationer, pattern language, anti-patterns, urval och livscykel etablerade. |
| 24 | Integrations- och kommunikationsmönster | Första utkast | BFF, asynkron messaging, pub/sub, idempotens, retries, dead-letter, ordering, korrelation, kontraktsutveckling och mönsterkombinationer etablerade. |
| 25 | Process-, regel- och datamönster | Första utkast | Human workflow, externaliserade regler, system of record/härledda kopior, cache-aside, state-ansvar, eventual consistency och mönsterkombinationer etablerade. |
| 26 | AI-, identitets- och runtime-mönster | Första utkast | RAG, mänsklig kontroll, tjänsteidentitet och containeriserad stateless tjänst fördjupade som kombinerbara riskbegränsande mönster. |
| 27 | Drift- och leveransmönster | Första utkast | Build once/promote many, observability för distribuerade tjänster, backup/verifierad återställning, releaseverifiering och sammanhängande återställningskedja etablerade. |
| 28 | När ett byggblock blir en plattformstjänst | Första utkast | Tjänstekontrakt, ansvar, onboarding, kvalitetsprofiler, konsumtionsmodell, support, livscykel och mognad från byggblock till tjänst etablerade. |
| 29 | Platform as a Product | Första utkast | Målgrupp, värdelöfte, developer experience, user journeys, adoption, produktmätetal, feedback, roadmap, kostnad och livscykel etablerade. |
| 30–37 | Se kapitelplan | Planerade | Ej skapade ännu. |

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
- Kapitel 13 – Process, workflow och ärendehantering är skapat som första utkast och etablerar gränsen mellan vanlig domänlogik och explicit processhantering, långlivat tillstånd, human tasks, case management och processorkestrering.
- Kapitel 14 – Regler och beslut är skapat som första utkast och etablerar gränsen mellan lokal domänlogik och explicit beslutslogik, samt externalisering, DMN, versionering, förklarbarhet och regelägarskap.
- Kapitel 15 – Data- och informationshantering är skapat som första utkast och etablerar den tekniska dataförmågan: lagringsval, konsistens, kopior, cache, historik, retention, schemaevolution, migrering och återställningsbehov.
- Kapitel 16 – Analys, sökning och AI är skapat som första utkast och etablerar skillnaderna mellan sökning, analys, ML och generativ AI samt RAG, utvärdering, mänsklig kontroll och AI-specifik förvaltning.
- Kapitel 7 har gjort etableringsordning, ansvarssnitt och iterativt arbetssätt praktiskt tydliga.
- Använd avgränsningsreglerna i `docs/kapitelplan.md` när kapitel skapas så att senare delar fördjupar i stället för att upprepa.

- Kapitel 17 – Integration och kommunikation är skapat som första utkast och etablerar val mellan API, messaging, events, filutbyte och dataförflyttning samt kontraktslivscykel, koppling, felhantering och gemensamma integrationsplattformstjänster.
- Kapitel 18 – Identitet och tillit är skapat som första utkast och etablerar autentisering/auktorisation, federation, workforce identity, tjänsteidentiteter, PKI, secrets, privilegierad åtkomst och explicita tillitsrelationer.
- Kapitel 19 – Applikationsexekvering och runtime är skapat som första utkast och etablerar workload-baserat runtimeval, container/VM/runtimeprofiler, stateless/stateful, resursprofilering, isolering, portabilitet och separata livscykler för applikation och plattform.
- Kapitel 20 – Driftbarhet och motståndskraft är skapat som första utkast och etablerar observability, SLI/SLO, larm, felisolering, recovery, backup/restore, RPO/RTO, DR, runbooks, kapacitet och operativ återkoppling.
- Kapitel 21 – Programvaruutveckling och leverans är skapat som första utkast och etablerar SCM, reproducerbara builds, CI/CD, artefaktflöde, software supply chain, SBOM/provenance, signering, developer experience och ansvarsnivåer.
- Kapitel 22 – Arbetsplats, samarbete och produktivitet är skapat som första utkast och etablerar gränsen mellan generell produktivitet och verksamhetssystem, samarbetsytors ägarskap/livscykel, extern delning, low-code-eskalering, produktivitets-AI och gemensamma arbetsplatserbjudanden. Del III är därmed komplett i första utkast.
- Kapitel 23 – Lösningsmönster som återanvändbara beslut är skapat som första utkast och etablerar mönster som beslutsartefakt, pattern language, context/forces/consequences, variationer, anti-patterns, relationen till andra arkitekturartefakter samt urval och livscykel. Del IV är därmed påbörjad.
- Kapitel 25 – Process-, regel- och datamönster är skapat som första utkast och fördjupar human workflow, externaliserade regler, system of record/härledda kopior och cache-aside som kombinerbara mönster med tydligt ansvar för state och felgränser.
- Kapitel 26 – AI-, identitets- och runtime-mönster är skapat som första utkast och fördjupar RAG, mänsklig kontroll, tjänsteidentitet och containeriserad stateless tjänst som fyra separata men kombinerbara riskbegränsande mönster.
- Nästa planerade kapitel är kapitel 27 – Drift- och leveransmönster.

- Kapitel 24 – Integrations- och kommunikationsmönster är skapat som första utkast och fördjupar BFF, asynkron messaging, pub/sub, idempotens, retries, dead-letter, ordering, korrelation och kontraktsutveckling som återanvändbara mönster.
- Kapitel 27 – Drift- och leveransmönster är skapat som första utkast och fördjupar build once/promote many, observability för distribuerade tjänster och backup med verifierad återställning som en sammanhängande leverans- och återhämtningskedja.
- Del IV är därmed komplett i första utkast. Kapitel 28 – När ett byggblock blir en plattformstjänst är skapat som första utkast och inleder del V genom att etablera tjänstekontrakt, ansvar, konsumtionsmodell, kvalitetsprofiler, support och livscykel som skillnaden mellan rå teknik och konsumerbart erbjudande.
- Kapitel 29 – Platform as a Product är skapat som första utkast och etablerar målgrupper, värdelöfte, developer experience, användarresor, produktmätetal, feedbackloopar, roadmap, kostnad och plattformsproduktens livscykel. Nästa steg är kapitel 30 – Golden paths, paved roads och självservice.
