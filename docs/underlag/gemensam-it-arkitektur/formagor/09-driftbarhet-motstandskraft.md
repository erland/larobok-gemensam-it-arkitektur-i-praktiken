# Förmåga: Driftbarhet och motståndskraft

> **Status:** Utkast  
> **Ansvarig:** Gemensam IT-arkitektur / stödjande IT-område  
> **Senast reviderad:** 2026-08-18

## 1. Syfte, omfattning och relationer

### 1.1 Syfte

Förmågan ska ge utvecklingsområden stöd för att kunna förstå, övervaka, felsöka, drifta och återställa IT-stöd samt hantera tekniska störningar på ett kontrollerat och förvaltningsbart sätt.

Syftet är att tillhandahålla gemensamma mekanismer för observability, monitorering, larm, backup, återställning, redundans och teknisk motståndskraft, utan att dessa mekanismer i sig blir utgångspunkt för kravställningen.

Krav på exempelvis tillgänglighet, kontinuitet, RTO och RPO ska härledas från verksamhets- och IT-stödsbehov. Denna förmåga beskriver hur sådana behov kan realiseras och följas upp.

### 1.2 Omfattning

Förmågan omfattar bland annat:

- central loggning
- strukturerade applikationsloggar
- metrics
- tracing
- korrelation mellan komponenter
- monitorering
- tekniska hälsokontroller
- larm och notifieringar
- dashboards för drift
- applikations- och plattformsobservability
- backup
- restore
- återställning av tekniska tjänster
- tekniskt stöd för hög tillgänglighet
- redundans och failover
- disaster recovery
- tekniska kontinuitetslösningar
- kapacitetsövervakning
- felisolering
- driftstatus och service health
- runbooks och operativa återställningsprocedurer
- verifiering av backup och restore
- stöd för incidentdiagnostik

### 1.3 Utanför förmågan

Följande hör primärt hemma i andra förmågor eller perspektiv:

- själva kravet på tillgänglighet, kontinuitet, RTO eller RPO – **Krav- och kvalitetsdimensioner**
- applikationens exekveringsmiljö och runtime – **Applikationsexekvering och runtime**
- informationsägarskap, retention och datalivscykel – **Data- och informationshantering**
- nätverk, messaging och API-kommunikation – **Integration och kommunikation**
- identiteter och behörigheter – **Identitet och tillit**
- CI/CD, release och deploymentprocess – **Programvaruutveckling och leverans**

Förmågan ska inte användas för att automatiskt kräva maximal redundans, loggning eller backup för alla IT-stöd.

### 1.4 Relation till andra förmågor

**Applikationsexekvering och runtime** behöver mekanismer för health checks, restart, scaling och plattformsövervakning.

**Data- och informationshantering** uttrycker behov av dataåterställning och informationskontinuitet; denna förmåga realiserar backup-, restore- och DR-mekanismer.

**Integration och kommunikation** behöver korrelation, köövervakning, nätverksmonitorering och felanalys.

**Programvaruutveckling och leverans** behöver kunna leverera loggning, metrics, tracing och driftkonfiguration tillsammans med applikationen.

---

## 2. Behov och användningsområden

### 2.1 Typiska behov

Ett utvecklingsområde kan behöva stöd när ett IT-stöd ska:

- kunna felsökas snabbt vid incident
- ge samlad bild av hälsa och belastning
- korrelera fel över flera tjänster
- larma innan användare upptäcker allvarliga problem
- återställa data efter fel
- återstarta tjänster automatiskt
- tåla bortfall av en instans eller komponent
- failover till redundant miljö
- återställas efter större driftstörning
- verifiera att backup faktiskt går att återläsa
- följa kapacitetsutveckling över tid
- skilja applikationsfel från plattforms- eller nätverksfel
- mäta teknisk tillgänglighet och servicenivåer
- ha dokumenterade runbooks för återkommande incidenter

### 2.2 Typiska användningsfall

#### Distribuerad applikationsfelsökning

En användartransaktion går genom flera tjänster och integrationer. Loggning och tracing gör det möjligt att följa flödet genom hela kedjan.

#### Proaktiv monitorering

Metrics och hälsokontroller visar gradvis ökande fel eller resursbelastning innan tjänsten blir otillgänglig.

#### Dataåterställning

Verksamhetsdata behöver återställas till en definierad tidpunkt efter korruption eller tekniskt fel.

#### Automatisk återstart

En stateless tjänsteinstans som blir ohälsosam ersätts automatiskt av runtimeplattformen.

#### Disaster recovery

Ett kritiskt IT-stöd behöver kunna återetableras i alternativ miljö efter omfattande störning.

### 2.3 Centrala arkitekturfrågor

Utvecklingsområdet bör bland annat ta ställning till:

- Vilka verksamhetskonsekvenser får avbrott?
- Vilka RTO/RPO eller motsvarande behov finns?
- Vilka delar av lösningen behöver redundans?
- Behöver fel hanteras automatiskt eller manuellt?
- Vilken observability behövs för felsökning?
- Vilka events och metrics är verksamhetsmässigt viktiga?
- Vilken loggdata får lagras ur säkerhets- och integritetsperspektiv?
- Hur länge behöver loggar och metrics behållas?
- Behöver end-to-end tracing?
- Hur verifieras backup och restore?
- Behöver DR övas?
- Vilka beroenden kan bli single points of failure?
- Vilken kapacitet och vilka tröskelvärden behöver följas?
- Hur skiljs teknisk hälsa från verksamhetsmässig tillgänglighet?

---

## 3. Förmågespecifika arkitekturprinciper

Gemensamma principer finns i `../styrning/gemensamma-arkitekturprinciper.md`.

### P-DM-01 Driftkrav ska härledas från verksamhetskonsekvens

**Princip:**  
Nivå på redundans, backup, återställning, monitorering och larm ska utgå från dokumenterade behov och konsekvenser.

**Motivering:**  
Maximal teknisk robusthet är kostsam och inte alltid motiverad.

**Konsekvens:**  
Plattformen bör kunna erbjuda flera kvalitetsprofiler snarare än en enda högsta nivå.

### P-DM-02 Observability ska byggas in från början

**Princip:**  
Applikationer och plattformar ska utformas så att relevant loggning, metrics och tracing kan användas för drift och felsökning.

**Motivering:**  
Observability är svårt och dyrt att lägga till först när incidenter uppstår.

### P-DM-03 Hälsa ska mätas på rätt nivå

**Princip:**  
Teknisk hälsa, beroendehälsa och verksamhetsmässig funktion ska skiljas åt.

**Motivering:**  
En process kan vara tekniskt igång men ändå inte leverera fungerande tjänst till användaren.

### P-DM-04 Återställning ska verifieras, inte antas

**Princip:**  
Backup och DR ska betraktas som fungerande först när återställningsförmågan är testad på lämplig nivå.

**Motivering:**  
En skapad backup är inte samma sak som en verifierad återställningsförmåga.

### P-DM-05 Fel ska isoleras där det är möjligt

**Princip:**  
Arkitekturen bör begränsa hur fel i en komponent sprider sig till andra delar av lösningen.

**Motivering:**  
Felisolering ökar motståndskraft och förenklar återställning.

### P-DM-06 Automatiserad återhämtning där det är lämpligt

**Princip:**  
Automatisk restart, failover, scaling och annan självläkning bör användas där beteendet är förutsägbart och säkert.

**Motivering:**  
Automatisering minskar återställningstid men ska inte dölja fel eller skapa nya risker.

### P-DM-07 Loggning ska vara ändamålsenlig och dataminimerad

**Princip:**  
Loggar ska innehålla tillräckligt för drift och spårbarhet men inte mer skyddsvärd information än vad behovet kräver.

**Motivering:**  
Observability får inte skapa onödig informationsspridning.

---

## 4. Krav och styrande riktlinjer

### KR-DM-01 Grundläggande observability

**Krav:**  
Produktionssatta IT-stöd ska ha tillräcklig loggning och teknisk hälsodata för att incidenter ska kunna upptäckas och felsökas på en nivå som motsvarar tjänstens betydelse.

**Motivering/källa:**  
Driftbarhet och tillgänglighet.

### KR-DM-02 Korrelation

**Krav:**  
Distribuerade lösningar ska använda en gemensam korrelationsmekanism när felsökning eller spårbarhet kräver att ett flöde följs över komponentgränser.

**Motivering/källa:**  
Spårbarhet och verifierbarhet.

### KR-DM-03 Loggskydd

**Krav:**  
Loggar, traces och metrics ska hanteras enligt informationsklassning och får inte innehålla credentials, secrets eller onödiga skyddsvärda data.

**Motivering/källa:**  
Säkerhet och informationsskydd.

### KR-DM-04 Backupbehov ska dokumenteras

**Krav:**  
IT-stöd med persistent verksamhetsdata ska dokumentera vilka data som behöver backup eller annan återställningsmekanism samt vilken återställningsnivå som krävs.

**Motivering/källa:**  
Kontinuitet och återställningsförmåga.

### KR-DM-05 Restore ska verifieras

**Krav:**  
Kritiska backup- och återställningslösningar ska testas återkommande i en omfattning som motsvarar konsekvensen av misslyckad återställning.

**Motivering/källa:**  
Kontinuitet och verifierbarhet.

### KR-DM-06 Single points of failure

**Krav:**  
IT-stöd med höga tillgänglighetskrav ska identifiera och hantera single points of failure i enlighet med beslutad kvalitetsnivå.

**Motivering/källa:**  
Tillgänglighet och kontinuitet.

### KR-DM-07 Larm ska vara åtgärdsbara

**Krav:**  
Produktionslarm ska så långt som möjligt vara kopplade till ett tydligt felvillkor, ansvar och möjlig åtgärd.

**Motivering/källa:**  
Driftbarhet och minskad larmtrötthet.

### KR-DM-08 DR-plan där behovet kräver det

**Krav:**  
IT-stöd med krav på återetablering efter större störning ska ha dokumenterad och verifierbar DR-strategi.

**Motivering/källa:**  
Kontinuitet och återställningsförmåga.

---

## 5. Guidelines och vägledning

### Logs, metrics eller traces?

Använd **logs** för detaljerade händelser och diagnostik.

Använd **metrics** för numeriska tidsserier som felgrad, latency, kapacitet och resursförbrukning.

Använd **traces** för att följa distribuerade request- eller processflöden över flera komponenter.

De kompletterar varandra och bör inte ses som utbytbara.

### Vad bör loggas?

Logga sådant som behövs för:

- felanalys
- säkerhets- och auditbehov
- teknisk spårbarhet
- centrala verksamhetshändelser där detta är motiverat

Undvik:

- lösenord
- access tokens
- privata nycklar
- kompletta skyddsvärda payloads utan dokumenterat behov

### Health checks

Skilj exempelvis mellan:

- **liveness** – processen fungerar tillräckligt för att inte behöva startas om
- **readiness** – instansen kan ta emot trafik
- **dependency health** – viktiga beroenden fungerar
- **business health** – tjänsten kan faktiskt utföra sin verksamhetsfunktion

### Backup eller replikering?

Replikering förbättrar tillgänglighet men skyddar inte alltid mot:

- logiska fel
- felaktig borttagning
- korruption som replikeras
- ransomware eller administrativa misstag

Backup och replikering löser olika problem.

### Hur bestäms RPO och RTO?

Utgå från:

- konsekvens av dataförlust
- konsekvens av avbrott
- återuppbyggbar information
- beroenden
- kostnad för högre skyddsnivå

Teknikområdet bör erbjuda profiler som kan matchas mot dessa behov.

### När behövs disaster recovery?

DR är särskilt relevant när:

- en hel miljö eller geografisk plats kan bli otillgänglig
- tjänsten har mycket höga kontinuitetskrav
- återuppbyggnad från normal backup tar för lång tid
- externa krav styr återetableringsförmågan

DR ska inte automatiskt innebära aktiv/aktiv arkitektur.

### Automatisk retry eller manuell åtgärd?

Automatisk retry är lämplig vid tillfälliga fel där operationen är säker att upprepa.

Använd begränsad retry med backoff och undvik retry-stormar.

Permanent verksamhetsfel eller icke-idempotenta operationer kan kräva annan hantering.

### Circuit breaker och felisolering

Circuit breaker, timeouts, bulkheads och liknande mekanismer kan begränsa felkaskader i distribuerade lösningar.

De bör användas utifrån konkret beroende- och felbild, inte som obligatoriska standardmönster överallt.

### Hur bör observability centraliseras?

Gemensamma tjänster bör erbjuda:

- logginsamling
- metrics
- tracing
- dashboards
- alerting
- retentionprofiler
- åtkomstkontroll

Applikationen ansvarar fortfarande för att producera meningsfull telemetri.

### När standardlösningen inte passar

Beskriv behovet i termer av:

- tillgänglighetsnivå
- RTO
- RPO
- datamängd
- backupfönster
- restoretid
- loggvolym
- retention
- tracevolym
- kritiska beroenden
- geografisk redundans
- regulatoriska krav

Därefter bedöms lämplig plattformsprofil och teknisk realisering.

---

## 6. Plattformar och tjänsteerbjudanden

I detta steg identifieras kandidater. Detaljerade plattformsdokument skapas separat senare eller tidigare vid konkret behov.

| Erbjudande | Syfte | Lämpligt för | Status |
|---|---|---|---|
| Central Logging Service | Samla, söka och behålla loggar | applikations- och plattformsloggning | Kandidat |
| Metrics and Monitoring Service | Samla metrics och övervaka hälsa | kapacitet, felgrad, latency och resursstatus | Kandidat |
| Distributed Tracing Service | Följa distribuerade flöden | mikrotjänster och integrationsintensiva lösningar | Kandidat |
| Alerting Service | Hantera larm och notifiering | driftkritiska fel och tröskelvärden | Kandidat |
| Backup Service | Säkerhetskopiera definierade data och komponenter | persistent data och konfiguration | Kandidat |
| Restore Service / Recovery Support | Standardiserad återställning | verifierbar restore och återetablering | Kandidat |
| High Availability Profile | Gemensamma mekanismer för redundans | workloads med högre tillgänglighetskrav | Kandidat |
| Disaster Recovery Service | Återetablering efter omfattande störning | kritiska IT-stöd | Kandidat |
| Operational Dashboard Service | Gemensam driftvisualisering | plattformar och IT-stöd | Kandidat |
| Runbook / Automation Service | Automatisera återkommande driftåtgärder | incident- och recoveryprocedurer | Kandidat |

---

## 7. Standarder och teknikval

| Standard/teknikval | Status | Tillämpning |
|---|---|---|
| Gemensam loggstandard | Kandidat | struktur, nivåer och metadata |
| Korrelations-ID-standard | Kandidat | end-to-end-spårbarhet |
| Metrics-standard | Kandidat | namn, labels och tekniska nyckelmått |
| Distributed tracing-standard | Kandidat | trace/span-konventioner |
| Health check-standard | Kandidat | readiness/liveness/health |
| Alerting-standard | Kandidat | severity, ansvar och notifiering |
| Backup-profiler | Kandidat | typer och kvalitetsnivåer |
| Restore-verifieringsstandard | Kandidat | test av återställning |
| DR-profil | Kandidat | återetableringsnivåer |
| Retentionstandard för telemetri | Kandidat | logg-, metric- och tracedata |

Exakta produkter och versioner ska dokumenteras separat.

---

## 8. Relaterade artefakter och kvalitetsdimensioner

### 8.1 Relevanta kvalitetsdimensioner

Denna förmåga realiserar särskilt följande kvalitetsdimensioner:

- **Tillgänglighet** – redundans, health checks, monitorering och failover.
- **Kontinuitet och återställningsförmåga** – backup, restore och DR.
- **Prestanda** – metrics och kapacitetsövervakning.
- **Skalbarhet och kapacitet** – övervakning och automatisk skalning.
- **Spårbarhet och verifierbarhet** – loggning, korrelation och tracing.
- **Säkerhet och informationsskydd** – loggskydd, incidentdetektion och säker recovery.
- **Förvaltningsbarhet och förändringsbarhet** – observability och automatiserade driftprocedurer.
- **Livscykel och hållbarhet** – backupformat, retention och långsiktig återställningsförmåga.
- **Kostnads- och resurseffektivitet** – rätt nivå av redundans och retention.

### 8.2 Lösningsmönster

Identifierade kandidater:

- Centralized Logging
- Structured Logging
- Correlation ID
- Distributed Tracing
- Health Check
- Retry with Backoff
- Circuit Breaker
- Bulkhead
- Graceful Degradation
- Automated Restart
- Active/Passive Failover
- Backup and Restore
- Point-in-Time Recovery
- Disaster Recovery
- Runbook Automation
- SLO-based Alerting

### 8.3 Plattformar

Identifierade kandidater:

- Central Logging Service
- Metrics and Monitoring Service
- Distributed Tracing Service
- Alerting Service
- Backup Service
- Restore Service / Recovery Support
- High Availability Profile
- Disaster Recovery Service
- Operational Dashboard Service
- Runbook / Automation Service

### 8.4 Tekniska standarder

Identifierade kandidater:

- loggstandard
- korrelations-ID-standard
- metrics-standard
- tracing-standard
- health check-standard
- alerting-standard
- backup-profiler
- restore-verifieringsstandard
- DR-profil
- telemetri-retentionstandard

### 8.5 Kandidater till referensarkitekturer

Följande kandidater stärks eller identifieras:

- **Högtillgängligt verksamhetssystem**
- **Kritiskt internt handläggningsstöd**
- **Publik e-tjänst med höga tillgänglighetskrav**
- **Containerbaserad mikrotjänstelösning med full observability**
- **Integrationsintensivt verksamhetssystem**
- **Geografiskt redundant verksamhetslösning**
- **Disaster recovery för verksamhetskritisk tjänst**
- **Dataintensiv lösning med verifierad backup och återställning**

### 8.6 Teknisk dokumentation

När konkreta drift- och observabilityplattformar dokumenteras bör teknisk referens exempelvis omfatta:

- loggformat
- agent/collector-konfiguration
- metrics-endpoints
- traceexport
- dashboards
- alerts
- retention
- backupjobs
- restoreprocedurer
- DR-runbooks
- failover
- test av återställning
- åtkomstkontroll
- kostnads- och volymgränser
- tekniska begränsningar

---

## Arbetsanteckningar

### Identifierade kandidater

**Lösningsmönster**
- Centralized Logging
- Structured Logging
- Correlation ID
- Distributed Tracing
- Health Check
- Retry with Backoff
- Circuit Breaker
- Bulkhead
- Graceful Degradation
- Automated Restart
- Active/Passive Failover
- Backup and Restore
- Point-in-Time Recovery
- Disaster Recovery
- Runbook Automation
- SLO-based Alerting

**Plattformar/tjänster**
- Central Logging Service
- Metrics and Monitoring Service
- Distributed Tracing Service
- Alerting Service
- Backup Service
- Restore Service / Recovery Support
- High Availability Profile
- Disaster Recovery Service
- Operational Dashboard Service
- Runbook / Automation Service

**Tekniska standarder**
- loggstandard
- korrelations-ID-standard
- metrics-standard
- tracing-standard
- health check-standard
- alerting-standard
- backup-profiler
- restore-verifieringsstandard
- DR-profil
- telemetri-retentionstandard

**Referensarkitekturer**
- högtillgängligt verksamhetssystem
- kritiskt internt handläggningsstöd
- publik e-tjänst med höga tillgänglighetskrav
- containerbaserad mikrotjänstelösning med full observability
- integrationsintensivt verksamhetssystem
- geografiskt redundant verksamhetslösning
- disaster recovery för verksamhetskritisk tjänst

**Gränsdragningsfrågor**
- hur SLO/SLA-styrning ska fördelas mellan kvalitetsdimensioner och denna förmåga
- var gränsen går mellan backupbehov i Data- och informationshantering och backupplattform här
- hur health checks delas mellan runtime- och driftbarhetsförmågan
- om incident management ska ligga här eller betraktas som ITSM/process utanför denna arkitekturtaxonomi
- hur mycket HA/DR som bör beskrivas som plattformprofil i stället för separat tjänsteerbjudande
