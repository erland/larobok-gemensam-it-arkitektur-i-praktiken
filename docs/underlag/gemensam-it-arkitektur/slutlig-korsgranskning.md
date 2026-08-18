# Slutlig korsgranskning och konsolidering

> **Status:** Genomförd  
> **Datum:** 2026-08-18  
> **Omfattning:** Steg 0–16

## 1. Syfte

Denna korsgranskning verifierar att den gemensamma IT-arkitekturen hänger ihop som en sammanhållen modell från behov och kvalitetskrav till förmågor, lösningsmönster, plattformserbjudanden, tekniska standarder och referensarkitekturer.

Granskningen fokuserar på:

- begreppskonsistens
- gränsdragning mellan förmågor
- separation mellan behov och teknisk realisering
- överlapp mellan mönster
- överlapp mellan plattformserbjudanden
- separation mellan standard och produkt/version
- referensarkitekturernas relation till underliggande artefakter
- identifierade kvarvarande öppna frågor

## 2. Samlad arkitekturmodell

Den konsoliderade modellen är:

```text
Verksamhets- och IT-stödsbehov
        ↓
Krav och kvalitetsdimensioner
        ↓
Gemensamma IT-förmågor
        ↓
Lösningsmönster
        ↓
Plattformar och tjänsteerbjudanden
        ↓
Tekniska standarder
        ↓
Tekniska byggblock
        ↓
Produkt / version / konfiguration
```

Referensarkitekturer kombinerar flera delar tvärs över modellen:

```text
Förmågor + mönster + plattformar + standarder
                    ↓
           Referensarkitektur
                    ↓
            Lösningsarkitektur
```

## 3. Verifierad förmågetaxonomi

Följande 11 förmågor bedöms tillsammans ge en tillräckligt heltäckande första struktur:

1. Interaktion, presentation och kanaler
2. Process, workflow och ärendehantering
3. Regler och beslut
4. Data- och informationshantering
5. Analys, sökning och AI
6. Integration och kommunikation
7. Identitet och tillit
8. Applikationsexekvering och runtime
9. Driftbarhet och motståndskraft
10. Programvaruutveckling och leverans
11. Arbetsplats, samarbete och produktivitet

### Bedömning

Taxonomin håller ihop utan behov av ytterligare huvudförmåga i denna version.

Särskilt viktiga gränsdragningar är tydliggjorda:

- **Datahantering** uttrycker informationsbehov; databas-/lagringsprodukt är realisering.
- **Integration** omfattar informationsutbyte och konnektivitet; nätverkskomponenter är byggblock.
- **Identitet och tillit** är en förmåga; säkerhet är fortsatt en tvärgående kvalitetsdimension.
- **Runtime** beskriver exekvering; CI/CD ligger i Programvaruutveckling och leverans.
- **Driftbarhet** realiserar tillgänglighets-/kontinuitetsbehov men definierar inte själv deras nivå.
- **Arbetsplats** hanterar generell produktivitet och ska inte bli standardplattform för verksamhetssystem.

## 4. Lösningsmönster

15 mönster har konsoliderats.

### Bedömning

Urvalet är lagom begränsat för en första version. Flera mindre teknikmönster har medvetet inte fått egna filer.

Detta är korrekt eftersom exempelvis:

- retry
- circuit breaker
- rolling deployment
- blue/green deployment
- RBAC/ABAC

kan dokumenteras som del av större mönster eller standarder tills ett tydligt återanvändningsbehov motiverar egna dokument.

### Kvarvarande förbättringsmöjlighet

Vid nästa större revision kan vissa mönster behöva brytas ut om de används brett i referensarkitekturer, särskilt:

- Transactional Outbox
- Idempotent Consumer
- Circuit Breaker
- API Gateway / Edge
- Decision Service

## 5. Plattformar och tjänsteerbjudanden

35 erbjudanden har konsoliderats.

### Bedömning

Katalogen skiljer på ett bra sätt mellan:

- det konsumerbara tjänsteerbjudandet
- underliggande produktrealisering

Exempel:

```text
Relationell databastjänst
   ├─ Oracle Database
   └─ Microsoft SQL Server
```

och:

```text
Container Application Platform
   ↓
OpenShift
```

### Konsolideringsprincip

En produkt kan realisera flera tjänster och en tjänst kan ha flera produktrealiseringar.

Detta är särskilt viktigt för:

- Microsoft 365
- Power Platform
- Ceph
- RHEL
- JBoss Core Services

### Kvarvarande öppna frågor

Följande bör lösas när faktisk plattformsorganisation och tjänstekatalog verifieras:

- om WAN/LAN/trådlöst ska vara egna tjänsteerbjudanden
- om Managed File Transfer behövs som separat tjänst
- om Authorization Service ska vara egen plattformstjänst
- om Work Queue Service ska brytas ut
- om Linux Runtime ska vara egen tjänsteprofil
- exakt roll för JBoss Core Services

## 6. Tekniska standarder

25 standarddokument har konsoliderats.

### Bedömning

Separationen mellan:

1. arkitektur-/teknikstandard
2. produktstandard
3. versions-/supportmatris
4. teknisk konfiguration

är central och bör behållas.

Exempel:

```text
Containerstandard
   ↓
OpenShift produktstandard
   ↓
Supportmatris
   ↓
OpenShift 4.x
   ↓
Klusterkonfiguration
```

### Rekommenderad framtida artefakt

En separat support-/livscykelmatris bör tas fram när faktisk nulägesdata finns.

Den bör minst innehålla:

- produkt
- tjänsteerbjudande
- rekommenderad version
- minsta stödda version
- supportslut
- planerad migrering
- ansvarig
- status

## 7. Referensarkitekturer

7 referensarkitekturer har tagits fram:

- Internt handläggningsstöd
- Publik e-tjänst
- Integrationsintensivt verksamhetssystem
- Informationsutbyte med annan myndighet
- Containerbaserad tjänst
- AI-baserat verksamhetsstöd
- Digital arbetsplats

### Bedömning

Referensarkitekturerna kompletterar förmågemodellen utan att duplicera den.

De fungerar som avsedda som:

> återanvändbara arkitekturella startpunkter

och inte som obligatoriska kompletta lösningar.

### Framtida kandidater

Vid konkret behov kan följande tillkomma:

- mobil operativ lösning
- dokumentintensivt verksamhetssystem
- batchintensivt verksamhetssystem
- geografiskt redundant lösning
- privilegierad administrationsmiljö
- data- och analysplattform

## 8. Terminologisk konsolidering

Följande termer används konsekvent i den slutliga modellen:

### Förmåga
Vad IT-organisationen behöver kunna stödja.

### Lösningsmönster
Återanvändbart sätt att lösa ett återkommande arkitekturproblem.

### Plattform/tjänsteerbjudande
Konsumerbar teknisk tjänst med tydligt ansvar och kvalitetsprofil.

### Teknisk standard
Styrande eller rekommenderad teknisk princip, konvention eller produktfamilj.

### Tekniskt byggblock
Lägre realiseringskomponent, exempelvis OS, nätverkskomponent eller lagringsmotor.

### Produkt
Konkret teknisk produkt eller tjänst.

### Referensarkitektur
Kombination av flera förmågor, mönster, plattformar och standarder för en återkommande lösningstyp.

## 9. Kvalitetsdimensioner

De 12 kvalitetsdimensionerna ligger kvar som tvärgående perspektiv och ska inte dupliceras som tekniska förmågor.

Detta bedöms vara en av modellens viktigaste styrkor.

Särskilt:

- säkerhet är inte likställt med Identitet och tillit
- tillgänglighet är inte likställt med Driftbarhet
- interoperabilitet är inte likställt med Integration
- användbarhet är inte likställt med Interaktion

Förmågorna realiserar kvalitetsbehov men ersätter dem inte.

## 10. Produktklassificering – slutlig kontroll

De ursprungliga konkreta teknikerna kan nu klassificeras utan större begreppskonflikt:

| Produkt/teknik | Primär klassificering |
|---|---|
| Angular | Web Application Framework / frontendstandard |
| Microsoft Office / Microsoft 365 | Productivity Suite |
| RHEL | runtimebyggblock / Linux-produktstandard |
| JBoss EAP | Java Application Runtime |
| JBoss Core Services | runtime-/proxybyggblock, slutlig tjänsteplacering kvarstår |
| Jenkins | CI/CD Platform |
| IntelliJ IDEA | Developer Tooling |
| JPA | Java persistence-standard |
| Oracle | Relationell databastjänst |
| Elasticsearch | Search and Indexing Service |
| Power BI | Business Intelligence and Reporting |
| SQL Server | Relationell databastjänst |
| Microsoft SSIS | Data Integration / ETL |
| Ceph | lagringsbyggblock / Object Storage-realisering |
| OpenShift | Container Application Platform |
| Trådlöst nätverk | kommunikationstjänst/realisering, detaljer kvarstår |
| Rakel | extern/särskild kommunikationstjänst, behöver separat behovsanalys |
| SGSI | Secure Government Connectivity |
| SHS | Structured Government Exchange, lokal verifiering krävs |
| IBM MQ | Enterprise Messaging |

### Notering om Rakel

Rakel har inte fått eget plattforms- eller standarddokument i denna version. Det bör göras först när det finns ett tydligt arkitekturbehov att beskriva dess roll i förhållande till operativ kommunikation, redundans, externa tjänster och verksamhetskritikalitet.

## 11. Dokumentationsstyrning

Följande styrprinciper bör gälla framåt:

- stabil arkitektur hålls separerad från snabbt föränderliga produktversioner
- produkter ska länkas till tjänster, inte bli förmågor
- nya lokala behov ska i första hand mappas till befintlig förmåga
- nya plattformar skapas först när det finns ett återkommande konsumentbehov
- nya mönster skapas först när lösningsproblemet återkommer
- referensarkitekturer skapas för återkommande lösningstyper, inte enskilda system
- återkommande avsteg ska användas som feedback på arkitekturen

## 12. Kvarvarande verifieringspunkter

Följande är medvetet inte slutligt verifierat och ska inte betraktas som faktiska nulägesbeslut:

- vilka produktversioner som är godkända
- exakt nuvarande Microsoft 365-/Power Platform-användning
- exakt roll och konfiguration för SGSI och SHS
- exakt användning av JBoss Core Services
- vilka nätverkstjänster som erbjuds som separata plattformstjänster
- vilka AI-/LLM-tjänster som faktiskt är godkända
- faktisk identitetsplattform
- faktisk observabilityplattform
- faktisk artefakt-/repositoryplattform

Dessa kräver lokal nulägesinventering.

## 13. Slutbedömning

Arkitekturmodellen bedöms efter steg 16 vara **sammanhängande och användbar som version 1.0 av en konceptuell gemensam IT-arkitektur**.

Den är tillräckligt konkret för att:

- klassificera befintliga tekniker
- styra dialog mellan utvecklingsområden och stödjande IT
- identifiera gemensamma plattformstjänster
- formulera tekniska standarder
- utgå från referensarkitekturer vid nya lösningar

Samtidigt undviker modellen att låsa stabil arkitektur till enskilda produkter och versioner.

## 14. Rekommenderad fortsättning efter version 1.0

Nästa naturliga arbete är inte fler huvudförmågor utan att fylla modellen med faktisk organisationsdata:

1. nulägesinventera faktiska plattformstjänster
2. utse tjänsteägare
3. klassificera erbjudanden som standard/rekommenderad/pilot/avveckling
4. skapa support- och livscykelmatris
5. verifiera SGSI, SHS, Rakel och övriga externa tjänster
6. lägga in faktiska produktversioner
7. testa modellen på 3–5 verkliga lösningar
8. justera utifrån återkommande avsteg och luckor
