# Kapitelplan

## Bokprofil
- `book_kind`: `factbook`
- `book_type`: `subject_overview`
- Planerad struktur: 37 kapitel i 6 delar, utöver inledningen.

## Inledning
- Syfte: Introducera bokens problemställning, läsarprofil, centrala modell och hur boken kan användas både linjärt och som referens.
- Status: första utkast skapat

## Övergripande dispositionsprincip
Boken följer en medveten progression:

1. varför gemensam IT-arkitektur behövs, hur beslut bör drivas av behov och kvaliteter samt hur modellen etableras stegvis med tydliga ansvarsnivåer,
2. vad gemensamma IT-förmågor är och var deras gränser går,
3. vilka förmågor ett stödjande IT-område behöver kunna erbjuda,
4. hur återkommande lösningsproblem fångas som lösningsmönster,
5. hur mönster och byggblock operationaliseras som plattformstjänster och standarder,
6. hur allt används, styrs och utvecklas i referens- och lösningsarkitektur.

Varje senare del får förutsätta begrepp från tidigare delar, men ska inte återförklara dem i full längd.

# Del I – Modellen bakom gemensam IT-arkitektur

## Kapitel 1: Varför gemensam IT-arkitektur?
- Kärnfråga: Vilket problem försöker gemensam IT-arkitektur lösa, och när blir den själv ett problem?
- Centralt innehåll: fragmentering, lokal optimering, återanvändning, autonomi, gemensamt kontra domänspecifikt, arkitektur som möjliggörare snarare än kontrollapparat.
- Avgränsning: beskriver problembilden och målbilden, inte den konkreta styrmodellen.
- Status: första utkast skapat

## Kapitel 2: En arkitektur av flera lager
- Kärnfråga: Hur hänger behov, kvaliteter, förmågor, mönster, plattformar, standarder, byggblock och produkter ihop?
- Centralt innehåll: metamodell, abstraktionsnivåer, stabilitet över tid, spårbarhet, relationer mellan modellens artefakter.
- Avgränsning: presenterar helhetsmodellen; respektive artefakttyp fördjupas senare.
- Status: första utkast skapat

## Kapitel 3: Behov före teknik
- Kärnfråga: Hur undviker man att dagens teknikplattform blir morgondagens verksamhetskrav?
- Centralt innehåll: behovsanalys, constraints, produktoberoende krav, mål kontra medel, teknikskuld och path dependency.
- Avgränsning: behandlar hur problemet formuleras före arkitekturval; kvalitetskrav behandlas i kapitel 4.
- Status: första utkast skapat

## Kapitel 4: Kvalitetsattribut som arkitekturens drivkrafter
- Kärnfråga: Hur översätts verksamhetskonsekvenser till mätbara kvalitetskrav och arkitekturdrivare?
- Centralt innehåll: tillgänglighet, kontinuitet, prestanda, skalbarhet, säkerhet, spårbarhet, interoperabilitet, användbarhet, förvaltningsbarhet, livscykel och kostnad.
- Fördjupning: quality attribute scenarios, prioritering och konflikt mellan kvaliteter, från konsekvens till verifierbart krav.
- Avgränsning: förklarar kravkedjan; enskilda förmågekapitel beskriver hur vissa kvaliteter realiseras tekniskt och ska inte upprepa kravmetoden.
- Status: första utkast skapat

## Kapitel 5: Arkitekturbeslut och trade-offs
- Kärnfråga: Hur gör man explicita, spårbara och omprövningsbara arkitekturbeslut?
- Centralt innehåll: alternativ, beslutskriterier, trade-offs, ADR, riskacceptans, konsekvenser, teknisk skuld och omprövningsdatum.
- Avgränsning: fokuserar på beslutets form och resonemang, inte organisatorisk governance eller standardernas livscykel.
- Status: första utkast skapat

## Kapitel 6: Arkitekturprinciper som beslutsstöd
- Kärnfråga: Hur används principer för att skapa konsekvens utan att ersätta arkitektens bedömning?
- Centralt innehåll: principers syfte, egenskaper hos användbara principer, behov före teknik, standardiserade erbjudanden, separation mellan stabil arkitektur och föränderlig teknik, säkerhet och driftbarhet som inbyggda egenskaper.
- Avgränsning: handlar om principerna som styrsignal; mandat, avsteg, förvaltning och governance behandlas samlat i kapitel 37.
- Status: planerad

## Kapitel 7: Att etablera modellen – ordning, ansvar och iteration
- Kärnfråga: I vilken ordning bör en organisation etablera gemensam IT-arkitektur, och vilka beslut hör hemma på gemensam nivå, förmågenivå respektive lösningsnivå?
- Centralt innehåll: etableringssekvens från behov och principer till första förmågekarta, ansvar och prioriterad fördjupning; tredelningen gemensam arkitektur → förmågeområde → lösning/produkt; mandat och ansvarssnitt; top-down för sammanhang och bottom-up för lärande; iterativ utveckling i stället för vattenfallsmodell.
- Rekommenderad etableringsordning: förstå återkommande behov och constraints → formulera gemensamma principer och kvalitetsdimensioner → skapa en tillräckligt bra första förmågekarta → avgränsa ansvar och beroenden → utse förmågeansvar → prioritera vilka förmågor som behöver fördjupas först → utveckla mönster, plattformstjänster och standarder inom förmågorna → identifiera tvärgående referensarkitekturer → följ upp, lär och justera modellen.
- Ansvarsprincip: gemensam nivå äger spelplanen och sådant som måste vara konsekvent över flera förmågor; förmågeansvar utvecklar innehåll och erbjudanden inom sitt område; lösnings-/produktteam kombinerar och tillämpar byggstenarna för konkreta verksamhetsbehov.
- Avgränsning: introducerar etablerings- och ansvarmodellen. Kapitel 8–11 fördjupar förmågebegrepp, gemensamhet, domängränser och information; kapitel 37 behandlar långsiktig governance, förvaltning, avsteg och evolution.
- Status: planerad

# Del II – Från verksamhet till gemensamma IT-förmågor

## Kapitel 8: Vad är en IT-förmåga?
- Kärnfråga: Vad betyder förmåga i detta sammanhang och hur skiljer den sig från verksamhetsförmåga, tjänst och produkt?
- Centralt innehåll: verksamhetsförmåga, gemensam IT-förmåga, capability map, tjänst, produkt, stabilitet och ansvar.
- Status: planerad

## Kapitel 9: När något bör vara gemensamt
- Kärnfråga: Vilka egenskaper motiverar en gemensam förmåga eller tjänst?
- Centralt innehåll: skalfördelar, risk, kompetens, interoperabilitet, standardisering, differentiering, centralisering kontra federation.
- Avgränsning: avgör *vad* som lämpar sig för gemensamt ansvar; kapitel 28–30 behandlar *hur* ett gemensamt tekniskt erbjudande utformas.
- Status: planerad

## Kapitel 10: Domäner, ansvar och gränser
- Kärnfråga: Vilka arkitekturfrågor löses inte av en gemensam förmågekarta?
- Centralt innehåll: domänarkitektur, bounded context, cohesion, coupling, ownership, lokalt kontra gemensamt ansvar.
- Avgränsning: handlar om verksamhets- och lösningsgränser, inte den gemensamma plattformens tjänstegränser.
- Status: planerad

## Kapitel 11: Information och data som arkitekturella ingångsvärden
- Kärnfråga: Hur kopplas informationsbehov, semantik, informationsägarskap och datans livscykel till arkitekturen innan lagringsteknik väljs?
- Centralt innehåll: informationsmodell, begrepp, informationsägarskap, datamodell, system of record, master- och referensdata, data contracts, klassning och livscykel.
- Avgränsning: handlar om informationens mening och ansvar. Kapitel 15 behandlar den tekniska förmågan för lagring, kopior, cache, historik, konsistens och retention.
- Status: planerad

# Del III – De gemensamma IT-förmågorna

Förmågekapitlen följer en gemensam struktur: problem och behov → vad förmågan omfattar → gränser mot närliggande förmågor → centrala arkitekturfrågor → typiska kvalitetskrav → möjliga mönster och tjänstetyper. De ska introducera relevanta mönster och plattformar, men inte göra den djupanalys som kommer i del IV och V.

## Kapitel 12: Interaktion, presentation och kanaler
- Kärnfråga: Hur skapas konsekventa, tillgängliga och förändringsbara användargränssnitt över flera kanaler?
- Centralt innehåll: webb, design system, kanalstrategi, BFF som möjlig lösningsstruktur, tillgänglighet och klientansvar.
- Status: planerad

## Kapitel 13: Process, workflow och ärendehantering
- Kärnfråga: När behövs processmotor, workflow eller case management – och när räcker vanlig domänlogik?
- Centralt innehåll: workflow, human tasks, case management, state, långlivade processer, orkestrering kontra domänansvar.
- Status: planerad

## Kapitel 14: Regler och beslut
- Kärnfråga: När bör verksamhetsregler externaliseras och hur hålls beslut begripliga och spårbara?
- Centralt innehåll: beslutslogik, regelmotor, DMN, versionshantering, förklarbarhet och ansvar för regler.
- Status: planerad

## Kapitel 15: Data- och informationshantering
- Kärnfråga: Hur väljer man lagrings- och datahanteringsmekanismer efter informationsbehov och kvalitetskrav?
- Centralt innehåll: relationsdata, objektlagring, cache, historik, retention, konsistens, kopior och återställningsbehov.
- Avgränsning: bygger på kapitel 11 och fokuserar på den tekniska förmågan, inte begrepps- eller informationsmodellering.
- Status: planerad

## Kapitel 16: Analys, sökning och AI
- Kärnfråga: Hur skiljer sig sökning, BI, ML och generativ AI – och hur kombineras de ansvarsfullt?
- Centralt innehåll: indexering, BI, ML, LLM, RAG, human-in-the-loop, informationsgrundning och AI-specifika kvalitetsfrågor.
- Status: planerad

## Kapitel 17: Integration och kommunikation
- Kärnfråga: Hur väljer man mellan API, meddelanden, events, filutbyte och strukturerat informationsutbyte?
- Centralt innehåll: synkront, asynkront, pub/sub, API, messaging, kontrakt, koppling och ansvar.
- Status: planerad

## Kapitel 18: Identitet och tillit
- Kärnfråga: Hur byggs tillit mellan människor, tjänster och organisationer?
- Centralt innehåll: workforce identity, federation, service identity, PKI, secrets, autentisering, auktorisation och trust boundaries.
- Status: planerad

## Kapitel 19: Applikationsexekvering och runtime
- Kärnfråga: Vad behöver en organisation erbjuda för att köra applikationer standardiserat men flexibelt?
- Centralt innehåll: containers, JVM/runtime, virtuella maskiner, stateless/stateful, isolation, runtime-ansvar och portabilitet.
- Status: planerad

## Kapitel 20: Driftbarhet och motståndskraft
- Kärnfråga: Hur designas system som går att förstå, återställa och hålla i drift?
- Centralt innehåll: observability, backup, restore, SLO, failure modes, resilience, kontinuitet och operativ återkoppling.
- Avgränsning: kapitel 4 definierar kvalitetskraven; detta kapitel behandlar förmågor och mekanismer för att realisera och verifiera dem.
- Status: planerad

## Kapitel 21: Programvaruutveckling och leverans
- Kärnfråga: Hur skapas en säker och reproducerbar väg från kod till produktion?
- Centralt innehåll: SCM, CI/CD, artifacts, software supply chain, build once/promote many och developer experience.
- Status: planerad

## Kapitel 22: Arbetsplats, samarbete och produktivitet
- Kärnfråga: Hur styrs en gemensam digital arbetsplats utan att låsa innovation eller skapa informationsrisker?
- Centralt innehåll: productivity suite, samarbetsytor, low-code, AI-assistenter, informationshantering och governance.
- Status: planerad

# Del IV – Från förmåga till återanvändbar lösning

## Kapitel 23: Lösningsmönster som återanvändbara beslut
- Kärnfråga: Vad gör ett lösningsmönster användbart och hur undviker man att det blir ett recept?
- Centralt innehåll: pattern language, context, forces, consequences, variationer, anti-patterns och relationen till principer, standarder och referensarkitekturer.
- Status: planerad

## Kapitel 24: Integrations- och kommunikationsmönster
- Kärnfråga: Hur används synkrona och asynkrona mönster för lös koppling och robust informationsöverföring?
- Centralt innehåll: BFF, messaging, pub/sub, idempotens, ordering, retries, dead-letter, korrelation och kontraktsutveckling.
- Status: planerad

## Kapitel 25: Process-, regel- och datamönster
- Kärnfråga: Hur kombineras workflow, regler, system of record, härledda kopior och cache utan otydligt ansvar?
- Centralt innehåll: human workflow, externaliserade regler, system of record, derived copies, cache-aside och konsekvenser av duplicerad state.
- Status: planerad

## Kapitel 26: AI-, identitets- och runtime-mönster
- Kärnfråga: Vilka återkommande mönster minskar risk när AI, identitet och applikationsdrift kombineras?
- Centralt innehåll: RAG, AI med mänsklig kontroll, service identity och containeriserad stateless tjänst.
- Status: planerad

## Kapitel 27: Drift- och leveransmönster
- Kärnfråga: Hur byggs deployment, observability och återställning in i lösningen från början?
- Centralt innehåll: build once/promote many, observability för distribuerade tjänster, backup och verifierad återställning samt kopplingen till SLO och releaseflöde.
- Status: planerad

# Del V – Plattformar som produkter och standarder som guardrails

## Kapitel 28: När ett byggblock blir en plattformstjänst
- Kärnfråga: Vad krävs för att något ska vara ett konsumerbart erbjudande och inte bara central infrastruktur?
- Centralt innehåll: service offering, tekniska byggblock, gränssnitt, ansvar, onboarding, support, service levels och konsumtionsmodell.
- Status: planerad

## Kapitel 29: Platform as a Product
- Kärnfråga: Hur gör man plattformar användbara, mätbara och efterfrågade?
- Centralt innehåll: plattformsteam, produktledning, developer experience, användarbehov, SLO, roadmap, feedback och adoption.
- Avgränsning: handlar om produktmodellen och teamets arbetssätt; självservice och styrmekanismer fördjupas i kapitel 30.
- Status: planerad

## Kapitel 30: Golden paths, paved roads och självservice
- Kärnfråga: Hur styr man genom den enklaste vägen i stället för genom dokument och granskningsköer?
- Centralt innehåll: golden paths, templates, automation, portals, policy-as-code, guardrails, escape hatches och självservice.
- Status: planerad

## Kapitel 31: Tekniska standarder och deras nivåer
- Kärnfråga: Vad bör standardiseras – arkitektur, teknik, produkt, version eller konfiguration?
- Centralt innehåll: standardtyper, rekommendation kontra krav, interoperabilitet, compliance, undantag och kopplingen till plattformar och mönster.
- Status: planerad

## Kapitel 32: Tekniklivscykel och kontrollerad förändring
- Kärnfråga: Hur hanteras introduktion, rekommendation, deprecation och retirement?
- Centralt innehåll: technology radar, lifecycle states, EOL, migration, sunset, produkt- och versionshantering samt tidsbegränsade undantag.
- Avgränsning: handlar om teknikportföljens livscykel; den övergripande arkitekturmodellens förvaltning behandlas i kapitel 37.
- Status: planerad

## Kapitel 33: Ekonomi, kostnad och kapacitet
- Kärnfråga: Hur påverkar kostnadsmodell och kapacitetsansvar arkitekturval och plattformsbeteenden?
- Centralt innehåll: FinOps-principer, showback/chargeback, kapacitet, kostnadsdrivare, gemensam investering, incitament och kostnad som kvalitetsdimension.
- Status: planerad

# Del VI – Referensarkitekturer och praktisk tillämpning

## Kapitel 34: Vad en referensarkitektur är – och inte är
- Kärnfråga: Hur ger en referensarkitektur vägledning utan att bli en frusen lösningsdesign?
- Centralt innehåll: scope, viewpoints, variation points, constraints, relation till lösningsmönster, standarder och solution architecture.
- Status: planerad

## Kapitel 35: Från behov till lösningsarkitektur
- Kärnfråga: Hur gör ett konkret initiativ resan från behov till valda mönster, plattformar, standarder och dokumenterade beslut?
- Centralt innehåll: architecture workflow, behov och kvalitetsprofil, förmågekarta, alternativ, pattern/platform selection, traceability, decision log och avsteg.
- Avgränsning: sammanför tidigare delar till en metod; introducerar inte nya artefakttyper.
- Status: planerad

## Kapitel 36: Sju återkommande lösningsscenarier
- Kärnfråga: Hur ser modellen ut när den används i olika typer av verkliga lösningar?
- Centralt innehåll: internt handläggningsstöd, publik e-tjänst, integrationsintensivt verksamhetssystem, informationsutbyte med extern part, containerbaserad tjänst, AI-baserat verksamhetsstöd och digital arbetsplats.
- Form: jämförande case studies som följer arbetsflödet från kapitel 35 och använder referensarkitekturbegreppen från kapitel 34.
- Avgränsning: scenarierna ska syntetisera tidigare innehåll, inte skapa sju nya mini-läroböcker.
- Status: planerad

## Kapitel 37: Governance, förvaltning och evolution
- Kärnfråga: Hur hålls förmågekarta, principer, mönster, plattformskatalog, standarder och referensarkitekturer levande utan att governance blir en flaskhals?
- Centralt innehåll: mandat, ownership, federerad styrning, avsteg, review cadence, telemetry, adoption, documentation-as-code, feedback loops, maturity, sunset och organisatoriskt lärande.
- Avgränsning: knyter ihop styrning och långsiktig evolution; teknikens specifika produkt-/versionslivscykel ligger i kapitel 32.
- Status: planerad

# Avgränsningsregler för att undvika onödig upprepning

1. **Kapitel 4 kontra 20:** Kapitel 4 beskriver hur kvalitetskrav härleds och prioriteras. Kapitel 20 beskriver tekniska och operativa mekanismer för driftbarhet och resiliens.
2. **Kapitel 11 kontra 15:** Kapitel 11 beskriver informationens semantik, ägarskap och livscykel. Kapitel 15 beskriver teknisk datahantering och lagringsmekanismer.
3. **Del III kontra del IV:** Förmågekapitlen beskriver *vilken förmåga som behövs och varför*. Mönsterkapitlen beskriver *återanvändbara sätt att strukturera lösningar* och deras trade-offs.
4. **Del III/IV kontra del V:** Förmågor och mönster får nämna plattformstyper, men plattformskapitlen beskriver *hur erbjudanden produktifieras, konsumeras och styrs*.
5. **Kapitel 6 kontra 31/32/37:** Kapitel 6 beskriver arkitekturprinciper. Kapitel 31 beskriver konkreta standarder. Kapitel 32 beskriver tekniklivscykel. Kapitel 37 beskriver organisatorisk governance och förvaltning.
6. **Kapitel 28 kontra 29:** Kapitel 28 definierar vad en plattformstjänst är och dess tjänstekontrakt. Kapitel 29 handlar om produktledningen och teammodellen kring plattformen.
7. **Kapitel 29 kontra 30:** Kapitel 29 fokuserar på plattformen som produkt; kapitel 30 på konsumtionsupplevelse, självservice och automatiserade guardrails.
8. **Kapitel 32 kontra 37:** Kapitel 32 hanterar produkter, versioner och teknikers livscykel. Kapitel 37 hanterar hela arkitekturmodellens governance och evolution.
9. **Kapitel 34–36:** Kapitel 34 definierar artefakten referensarkitektur, kapitel 35 beskriver arbetsflödet från behov till lösningsarkitektur och kapitel 36 visar arbetsflödet i jämförbara scenarier.

# Helhetskontroll

- **Ämnestäckning:** metamodell, behov, kvaliteter, beslut, principer, IT-förmågor, domäner/information, elva förmågor, lösningsmönster, plattformar, standarder, referensarkitekturer, ekonomi, governance och praktisk tillämpning.
- **Logisk ordning:** varför → modell och beslut → förmågor och gränser → tekniska förmågor → mönster → plattformar/standarder → referensarkitektur och tillämpning → governance/evolution.
- **Balans bredd/djup:** de elva förmågekapitlen ger ämnesbredd medan grund-, mönster-, plattforms- och tillämpningsdelarna ger selektiv fördjupning.
- **Minskad redundans:** det tidigare separata kapitlet om övergången från kvalitetsbehov till förmågekrav har absorberats i kapitel 4 och 35; de tidigare avslutande kapitlen om förvaltning och evolution har slagits samman; styrning i början har omformats till ett principkapitel och den operativa governance-frågan samlats sist.
- **Kapitel med särskilt faktakontrollbehov:** kvalitetsattribut, informations-/dataområden, AI, identitet, runtime, driftbarhet, utvecklingskedja, mönster, standarder, tekniklivscykel och referensarkitektur när externa standarder eller etablerade modeller nämns.
