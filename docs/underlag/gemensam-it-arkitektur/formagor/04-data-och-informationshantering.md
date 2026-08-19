# Förmåga: Data- och informationshantering

> **Status:** Utkast  
> **Ansvarig:** Gemensam IT-arkitektur / stödjande IT-område  
> **Senast reviderad:** 2026-08-18

## 1. Syfte, omfattning och relationer

### 1.1 Syfte

Förmågan ska ge utvecklingsområden stöd för att hantera data och information genom hela livscykeln – från skapande och lagring till åtkomst, förändring, historik, delning, bevarande och avveckling.

Syftet är att utvecklingsområden ska kunna uttrycka sina behov i termer av informationskaraktär, åtkomstmönster, konsistens, volym, retention, återställningsbehov och andra kvaliteter, och därefter välja lämpliga plattformstjänster och tekniska realiseringar.

Förmågan ska motverka att begrepp som "lagring", "databas" eller en viss produkt blir utgångspunkt för kravställningen.

### 1.2 Omfattning

Förmågan omfattar bland annat:

- strukturerad och ostrukturerad data
- relationell datahantering
- dokument och filer
- objektlagring
- cache och temporär data
- metadata
- masterdata och referensdata
- datahistorik och versionshantering
- transaktionshantering och konsistens
- retention, bevarande och gallring
- arkivering
- backup och återställning ur ett dataperspektiv
- kryptering och skydd av data
- datalokalitet
- export och import
- datamigrering
- schema- och modellförändringar
- åtkomstmönster och datatjänster
- dataägarskap och informationsansvar
- teknisk datareplikering där detta krävs för datahanteringen

### 1.3 Utanför förmågan

Följande hör primärt hemma i andra förmågor:

- BI, rapportering, avancerad analys, sökning och AI – **Analys, sökning och AI**
- API:er, messaging och transport av information mellan system – **Integration och kommunikation**
- process-/ärendestatus som del av processmotor – **Process, workflow och ärendehantering**
- exekveringsmiljö för databaser och datatjänster – **Applikationsexekvering och runtime**
- övergripande backup-/DR-tjänster och observability – **Driftbarhet och motståndskraft**
- behörighet, autentisering och tjänsteidentitet – **Identitet och tillit**

Tekniska lagringsprodukter som Ceph, SAN, NAS eller block storage är normalt underliggande byggblock och inte egna förmågor.

### 1.4 Relation till andra förmågor

**Analys, sökning och AI** konsumerar ofta data från denna förmåga men har fokus på bearbetning, sökning och analys snarare än primär informationshantering.

**Integration och kommunikation** ansvarar för transport och utbyte av data mellan system.

**Process, workflow och ärendehantering** kan ha intern processdata men bör inte oavsiktligt bli system of record för verksamhetsinformation.

**Driftbarhet och motståndskraft** realiserar delar av tillgänglighet, backup, återställning och övervakning, medan denna förmåga uttrycker informationsbehoven som driver dessa mekanismer.

**Identitet och tillit** används för åtkomstkontroll till data och informationsresurser.

---

## 2. Behov och användningsområden

### 2.1 Typiska behov

Ett utvecklingsområde kan behöva stöd när ett IT-stöd ska:

- lagra transaktionell verksamhetsdata
- hantera dokument eller filer
- lagra stora binära objekt
- upprätthålla stark konsistens mellan relaterade data
- stödja hög skriv- eller läsvolym
- bevara historiska versioner
- gallra information efter definierad retention
- lagra data under lång tid
- stödja cache för prestanda
- migrera data mellan tekniska plattformar
- hantera strukturerad och semistrukturerad information
- säkerställa att verksamhetsdata kan återställas
- skilja system of record från index, cache eller kopior
- dela referens- eller masterdata mellan flera system
- uppfylla krav på geografisk eller organisatorisk placering av data

### 2.2 Typiska användningsfall

#### Transaktionell verksamhetsdata

Ett verksamhetssystem behöver lagra strukturerade data med ACID-liknande egenskaper, tydliga relationer och krav på konsistens.

#### Dokument och bilagor

Ett ärende eller verksamhetsobjekt har dokument, bilder eller andra större binära objekt som behöver lagras och livscykelhanteras separat från transaktionsdatabasen.

#### Temporär cache

En tjänst behöver kortlivad data för att minska svarstid eller belastning på bakomliggande system.

#### Historik och revision

Ett system behöver bevara tidigare tillstånd eller ändringar över tid för spårbarhet eller verksamhetsbehov.

#### Master- och referensdata

Flera system behöver använda gemensamma kodverk eller informationsmängder med tydligt ägarskap.

#### Arkivering och gallring

Information behöver efter viss tid flyttas, bevaras eller gallras utifrån verksamhets- och regelkrav.

### 2.3 Centrala arkitekturfrågor

Utvecklingsområdet bör bland annat ta ställning till:

- Vilken information är verksamhetsmässigt primär?
- Vilket system är system of record?
- Vilka konsistenskrav finns?
- Hur stora är datamängderna idag och över tid?
- Vilka läs- och skrivmönster dominerar?
- Behövs transaktioner över flera objekt eller datakällor?
- Hur länge ska information bevaras?
- När och hur ska information gallras?
- Vilka historik- och revisionskrav finns?
- Vilken återställningsförmåga krävs?
- Vilken informationsklassning gäller?
- Får information kopieras till cache, index eller analysplattform?
- Behöver information kunna exporteras i öppet format?
- Finns krav på datalokalitet eller särskild jurisdiktion?
- Hur hanteras schemaförändringar och migrering?
- Vilka delar av datat bör ligga i databas, dokumentlager, objektlagring eller annan tjänst?

---

## 3. Förmågespecifika arkitekturprinciper

Gemensamma principer finns i `../styrning/gemensamma-arkitekturprinciper.md`.

### P-DI-01 Informationsbehov före lagringsteknik

**Princip:**  
Val av datatjänst ska utgå från informationens egenskaper och åtkomstbehov, inte från en på förhand vald produkt eller lagringsteknik.

**Motivering:**  
Olika informationsbehov kräver olika kompromisser kring konsistens, prestanda, kostnad och livscykel.

**Konsekvens:**  
Utvecklingsområden bör beskriva behov i termer av data och kvalitet innan produktval görs.

### P-DI-02 System of record ska vara tydligt

**Princip:**  
För varje väsentlig informationsmängd ska det vara tydligt vilket system eller vilken tjänst som är auktoritativ källa.

**Motivering:**  
Otydligt ägarskap skapar dubbla sanningar, svårigheter vid fel och osäker förvaltning.

### P-DI-03 Kopior ska ha ett definierat syfte och en definierad livscykel

**Princip:**  
Cache, index, repliker och andra kopior ska ha tydligt syfte, källa och strategi för synkronisering eller återuppbyggnad.

**Motivering:**  
Kopior får inte oavsiktligt bli nya oberoende informationskällor.

### P-DI-04 Informationens livscykel ska designas från början

**Princip:**  
Retention, historik, arkivering, gallring och avveckling ska beaktas när lösningen designas.

**Motivering:**  
Det är ofta dyrt och riskfyllt att lägga till livscykelhantering i efterhand.

### P-DI-05 Verksamhetsdata ska inte bindas onödigt hårt till en teknisk representation

**Princip:**  
När det är rimligt ska data kunna migreras, exporteras och förstås utan beroende av en enskild produkts interna format.

**Motivering:**  
Det stödjer livscykel, interoperabilitet och långsiktig förvaltning.

### P-DI-06 Data ska lagras där dess ansvar naturligt hör hemma

**Princip:**  
Verksamhetsdata ska normalt ägas och lagras nära den domän eller tjänst som ansvarar för informationen.

**Motivering:**  
Gemensamma databaser mellan oberoende applikationer skapar stark koppling och otydligt ansvar.

**Konsekvens:**  
Informationsdelning bör i första hand ske via definierade tjänster, events eller andra kontrollerade mekanismer.

### P-DI-07 Säkerhets- och skyddsåtgärder ska följa informationens behov

**Princip:**  
Kryptering, åtkomstkontroll, loggning och andra skydd ska härledas från informationens skyddsbehov.

**Motivering:**  
Samma tekniska skyddsnivå behöver inte vara rätt för alla informationsmängder.

---

## 4. Krav och styrande riktlinjer

### KR-DI-01 Identifierat informationsägarskap

**Krav:**  
Väsentliga informationsmängder ska ha identifierat verksamhetsmässigt ägarskap och tekniskt ansvar.

**Motivering/källa:**  
Förvaltningsbarhet, datakvalitet och ansvar.

### KR-DI-02 System of record

**Krav:**  
IT-stöd ska dokumentera vilket system eller vilken tjänst som är system of record för väsentliga informationsmängder när flera kopior förekommer.

**Motivering/källa:**  
Konsistens och spårbarhet.

### KR-DI-03 Retention och gallring

**Krav:**  
Information som omfattas av krav på retention, bevarande eller gallring ska ha en dokumenterad livscykel och teknisk realisering för denna.

**Motivering/källa:**  
Regelefterlevnad och informationsförvaltning.

### KR-DI-04 Backup och återställning ska härledas från informationsbehov

**Krav:**  
Krav på backup, återställning och dataförlust ska dokumenteras utifrån verksamhetens behov och omsättas i RPO/RTO eller motsvarande när det är relevant.

**Motivering/källa:**  
Kontinuitet och återställningsförmåga.

### KR-DI-05 Kryptering och åtkomst

**Krav:**  
Skydd av data i vila och under åtkomst ska följa myndighetens säkerhetskrav och informationsklassning.

**Motivering/källa:**  
Säkerhet och informationsskydd.

### KR-DI-06 Schema- och datamigrering

**Krav:**  
Förändringar i datastrukturer som påverkar persistent verksamhetsdata ska hanteras med en definierad migrerings- och rollbackstrategi där riskbilden kräver det.

**Motivering/källa:**  
Förvaltningsbarhet och kontinuitet.

### KR-DI-07 Direkt databasdelning mellan oberoende system

**Krav:**  
Oberoende IT-stöd ska inte använda direkt gemensam databasåtkomst som standardmekanism för integration.

**Motivering/källa:**  
Minskar koppling och otydligt ägarskap.

**Kommentar:**  
Eventuella undantag ska motiveras utifrån faktiskt behov.

### KR-DI-08 Kopior och index

**Krav:**  
Sekundära kopior, index och cache som kan återskapas ska dokumentera källa och återuppbyggnadsstrategi.

**Motivering/källa:**  
Korrekthet och driftbarhet.

### KR-DI-09 Export och avveckling

**Krav:**  
För långlivade informationsmängder ska det finnas en realistisk möjlighet att exportera eller migrera information inför teknikbyte eller avveckling.

**Motivering/källa:**  
Livscykel och portabilitet.

---

## 5. Guidelines och vägledning

### Hur väljer man typ av datalagring?

Utgå från:

- datamodell
- relationer
- konsistensbehov
- transaktionsbehov
- åtkomstmönster
- datavolym
- förändringstakt
- retention
- återställningsbehov
- kostnad

Välj därefter lämpligt erbjudande, exempelvis relationell databas, objektlagring, filyta, cache eller dokumenttjänst.

### När passar en relationell databas?

En relationell databas är ofta lämplig när:

- data har tydliga relationer
- stark konsistens är viktig
- transaktioner behövs
- frågemönstren är relativt strukturerade
- schema och dataintegritet är centrala

### När bör objektlagring användas?

Objektlagring är ofta lämplig för:

- stora binära objekt
- dokument, bilder och filer
- stora mängder immutable data
- data som inte behöver relationsfrågor
- skalbar och kostnadseffektiv lagring

Metadata bör då modelleras så att objekten kan hittas och livscykelhanteras.

### Databas eller filserver?

Filer bör inte läggas i traditionell filyta endast för att det är tekniskt enkelt.

Bedöm:

- behöver filen kopplas till ett verksamhetsobjekt?
- krävs versionshantering?
- krävs metadata?
- krävs transaktionskoppling?
- krävs delning via mänsklig arbetsyta eller via applikation?

Filserver som mänsklig samarbetsyta hör delvis hemma under Arbetsplats, samarbete och produktivitet.

### När bör cache användas?

Cache är lämplig när den kan förbättra prestanda utan att bli system of record.

Definiera alltid:

- källa
- TTL eller invalidation
- konsekvens vid stale data
- återuppbyggnad
- om känslig information får cachelagras

### Oracle eller SQL Server?

Val mellan relationella databastjänster bör baseras på:

- funktionella krav
- workload
- tillgänglighet
- prestanda
- integrationsbehov
- kompetens
- licens/kostnad
- plattformens livscykel

Produktpreferens i sig är inte ett arkitekturkrav.

### Var passar JPA?

JPA är en teknisk standard för Java-baserad persistence och inte ett databaserbjudande.

Använd JPA när dess abstraktion och ORM-modell passar domänen. Direkt SQL eller annan accessmodell kan vara lämpligare vid exempelvis mycket komplexa frågor eller särskilda prestandabehov.

### Var passar Ceph?

Ceph bör normalt betraktas som ett underliggande tekniskt byggblock som kan realisera objekt-, block- eller fillagring.

Utvecklingsområdet bör i första hand konsumera en definierad lagrings- eller datatjänst med kvalitetsprofil, inte kravställas direkt mot Ceph.

### Hur hanteras historik?

Skilj på:

- teknisk transaktionslogg
- audit/händelsehistorik
- verksamhetsmässig versionshistorik
- arkiverad information

De löser olika behov och ska inte automatiskt ersätta varandra.

### När standardlösningen inte passar

Dokumentera behovet i termer av:

- datatyp
- datavolym och tillväxt
- transaktionsvolym
- läs-/skrivmönster
- konsistens
- retention
- återställning
- säkerhet
- latency
- integrationsbehov

Därefter bedöms om plattformserbjudandet bör utvecklas eller annan teknisk realisering väljas.

---

## 6. Plattformar och tjänsteerbjudanden

I detta steg identifieras kandidater. Detaljerade plattformsdokument skapas separat vid konsolidering eller tidigare vid behov.

| Erbjudande | Syfte | Lämpligt för | Möjlig realisering idag | Status |
|---|---|---|---|---|
| Relationell databastjänst | Persistent strukturerad transaktionsdata | verksamhetsdata med relationer och transaktioner | Oracle Database, SQL Server | Kandidat |
| Object Storage Service | Lagra objekt och större binära data | dokument, bilder, filer, stora objekt | Ceph eller annan objektlagring | Kandidat |
| File Storage Service | Delad filbaserad lagring för applikationsbehov | särskilda filbaserade workloads | Ceph/NAS/annan realisering | Kandidat |
| Cache Service | Kortlivad snabb dataåtkomst | prestanda, sessionnära eller återuppbyggbar data | Produkt ej beslutad i detta steg | Kandidat |
| Document Storage Service | Hantering av dokument med metadata/livscykel | dokumentintensiva IT-stöd | Produkt ej beslutad | Kandidat |
| Reference/Master Data Service | Gemensam förvaltning av delade referensdata | kodverk och gemensamma informationsmängder | Ej beslutad | Kandidat |

Det bör senare avgöras om Oracle och SQL Server är separata erbjudanden eller realiseringar/profiler inom ett gemensamt erbjudande "Relationell databastjänst".

---

## 7. Standarder och teknikval

| Standard/teknikval | Status | Tillämpning |
|---|---|---|
| JPA | Kandidat/befintligt teknikval att verifiera | Java-baserad relationell persistence |
| Oracle Database | Befintlig produkt att klassificera | Möjlig realisering av relationell databastjänst |
| Microsoft SQL Server | Befintlig produkt att klassificera | Möjlig realisering av relationell databastjänst |
| Ceph | Befintlig produkt att klassificera | Underliggande block-/fil-/objektlagring |
| Gemensam datamigrationsstandard | Kandidat | Schema- och datamigrering |
| Gemensam backup-/restore-profil | Kandidat | Koppling mellan informationsbehov och teknisk återställning |
| Standard för dataexport | Kandidat | Portabilitet och avveckling |
| Retention-/gallringsmetadata | Kandidat | Livscykelhantering |

Exakta produktversioner ska dokumenteras separat.

---

## 8. Relaterade artefakter och kvalitetsdimensioner

### 8.1 Relevanta kvalitetsdimensioner

Särskilt viktiga dimensioner är:

- **Säkerhet och informationsskydd** – data är ofta den primära skyddsvärda resursen.
- **Tillgänglighet** – verksamhetskritiska data måste vara åtkomliga när verksamheten kräver det.
- **Kontinuitet och återställningsförmåga** – dataförlust och återställning är centrala arkitekturfrågor.
- **Prestanda** – åtkomstmönster och frågetyper påverkar plattformsval.
- **Skalbarhet och kapacitet** – datamängder och transaktionsvolym växer över tid.
- **Spårbarhet och verifierbarhet** – historik och audit kan krävas.
- **Regelefterlevnad** – retention, gallring och skydd kan härledas från externa krav.
- **Förvaltningsbarhet och förändringsbarhet** – schema, migrering och dataevolution är centralt.
- **Interoperabilitet och portabilitet** – export och teknikbyte kan vara viktiga.
- **Livscykel och hållbarhet** – information lever ofta längre än tekniska plattformar.
- **Kostnads- och resurseffektivitet** – datavolym och lagringsprofil påverkar kostnad kraftigt.

### 8.2 Lösningsmönster

Identifierade kandidater:

- Database per Service
- System of Record
- Cache-aside
- Object Storage for Binary Content
- Read Model / Materialized View
- Data Replication for Read
- Reference Data Distribution
- Schema Migration
- Data Archiving
- Event Sourcing (att bedöma senare)
- Transactional Outbox (gränsar mot Integration och kommunikation)

### 8.3 Plattformar

Identifierade kandidater:

- Relationell databastjänst
- Object Storage Service
- File Storage Service
- Cache Service
- Document Storage Service
- Reference/Master Data Service

### 8.4 Tekniska standarder

Identifierade kandidater:

- JPA
- Oracle Database-standard
- SQL Server-standard
- Ceph som teknisk realisering
- datamigrationsstandard
- backup-/restore-profil
- dataexportstandard
- retention-/gallringsmetadata

### 8.5 Kandidater till referensarkitekturer

Följande kandidater stärks eller identifieras:

- **Internt handläggningsstöd** – relationell verksamhetsdata, dokument och historik.
- **Publik e-tjänst** – inskickade uppgifter, dokument och temporär data.
- **Data- och analyslösning** – denna förmåga är käll- och informationsgrund för senare analysförmåga.
- **Informationsutbyte med annan myndighet** – dataägarskap, kopior och retention behöver tydliggöras.
- **Dokumentintensivt verksamhetssystem** – kandidat där objekt-/dokumentlagring är central.

### 8.6 Teknisk dokumentation

När konkreta databaser och lagringsplattformar dokumenteras bör teknisk referens exempelvis omfatta:

- anslutningsmönster
- databasschema och migrationsverktyg
- backup/restore
- HA och repliker
- kryptering
- autentisering
- kapacitetsgränser
- monitorering
- patchning och versionsstöd
- export/import
- produktbegränsningar

---

## Arbetsanteckningar

### Identifierade kandidater

**Lösningsmönster**
- Database per Service
- System of Record
- Cache-aside
- Object Storage for Binary Content
- Read Model / Materialized View
- Data Replication for Read
- Reference Data Distribution
- Schema Migration
- Data Archiving
- Event Sourcing
- Transactional Outbox

**Plattformar/tjänster**
- Relationell databastjänst
- Object Storage Service
- File Storage Service
- Cache Service
- Document Storage Service
- Reference/Master Data Service

**Tekniska standarder**
- JPA
- Oracle Database
- Microsoft SQL Server
- Ceph
- datamigrationsstandard
- backup-/restore-profil
- dataexportstandard
- retention-/gallringsmetadata

**Referensarkitekturer**
- internt handläggningsstöd
- publik e-tjänst
- data- och analyslösning
- informationsutbyte med annan myndighet
- dokumentintensivt verksamhetssystem

**Gränsdragningsfrågor**
- hur dokumenthantering ska avgränsas mot arbetsplats/samarbete
- hur masterdata och referensdata bör organiseras
- hur sökindex och analyskopior ska beskrivas mot nästa förmåga
- hur backupbehov härleds här men tekniskt realiseras under Driftbarhet och motståndskraft
- om Oracle och SQL Server ska vara separata tjänsteerbjudanden eller alternativa realiseringar av samma tjänst
