# Projektstatus

## Bok
- Titel: Gemensam IT-arkitektur i praktiken
- Språk: svenska
- Författare: Erland Lindmark
- Version: 0.1
- book_kind: factbook
- book_type: subject_overview

## Nuvarande fas
Revisionsfas – samtliga 37 huvudkapitel skrivna, helhetsrevision pass 1 och faktagranskning pass 1 genomförda

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
| 30 | Golden paths, paved roads och självservice | Första utkast | Golden paths, paved roads, templates, självservice, policy-as-code, guardrails, escape hatches, portal/katalog och mognadstrappa etablerade. |
| 31 | Tekniska standarder och deras nivåer | Första utkast | Standardnivåer, bindningsgrad, interoperabilitet, compliance, verifiering, undantag och kopplingen till plattformar/mönster etablerade. |
| 32 | Tekniklivscykel och kontrollerad förändring | Första utkast | Livscykelstatus, technology radar, supportfönster, deprecation, sunset, migration, experiment, undantag och retirement etablerade. |
| 33 | Ekonomi, kostnad och kapacitet | Första utkast | Kostnadsdrivare, enhetskostnad, showback/chargeback, gemensam investering, kapacitet, prognoser, incitament och FinOps som tvärfunktionell disciplin etablerade. |
| 34 | Vad en referensarkitektur är – och inte är | Första utkast | Scope, viewpoints, variation points, constraints, ansvar, spårbarhet och relationen till lösningsarkitektur/mönster/standard/plattform etablerade. |
| 35 | Från behov till lösningsarkitektur | Första utkast | Praktiskt arbetsflöde från behov och kvalitetsprofil via förmågor, referensarkitektur, mönster, plattformar och standarder till lokala beslut, verifiering, avsteg och återkoppling etablerat. |
| 36 | Sju återkommande lösningsscenarier | Första utkast | Sju jämförbara scenarier tillämpar arbetsflödet på handläggningsstöd, publik e-tjänst, integrationsintensivt system, externt informationsutbyte, containerbaserad tjänst, AI-stöd och digital arbetsplats. |
| 37 | Governance, förvaltning och evolution | Helhetsreviderad – pass 1 | Governance, mandat, federerad styrning, avsteg, återkoppling, dokumentation och mognad etablerade. |

## Faktakontroll
- Helmanusets begrepps- och konsistenspunkter är genomgångna i helhetsrevision pass 1.
- Faktagranskning pass 1 av externa och tidskänsliga sakpåståenden är genomförd 2026-08-19; resultat finns i `docs/faktagranskning-pass-1.md`.
- Endast organisationsspecifik kontext för kapitel 22 samt ett senare aktualitetspass för snabbt föränderliga standarder/ramverk återstår.
- Senast genomgången: 2026-08-19

## Öppna beslut
- Omslagskoncept och eventuell omslagsbild.
- Om slututgåvan ska ha synlig källförteckning/notapparat.
- Om arkitekturdiagram ska skapas successivt eller i en separat illustrationsfas.
- Slutlig målomfattning efter att 3–5 provkapitel skrivits.

## Nästa rekommenderade steg
- Genomför en full **språk- och stilrevision** av hela manuset: flyt, meningslängd, svengelska, konsekventa begrepp, exempelbalans och övergångar.
- Behåll ett kort aktualitetspass direkt före publicering för AI, identitets-/OAuth-profiler, SSDF, DMN, FinOps/FOCUS, WCAG och ISO/IEC/IEEE 42024.
- Gör organisationsspecifik rättslig/informationsstyrande kontroll av kapitel 22 om boken senare riktas mot en bestämd myndighet eller organisation.
- Därefter: besluta källförteckning/notapparat, illustrationer och omslag samt bygg första kompletta EPUB/PDF.
