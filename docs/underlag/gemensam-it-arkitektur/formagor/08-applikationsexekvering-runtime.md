# Förmåga: Applikationsexekvering och runtime

> **Status:** Utkast  
> **Ansvarig:** Gemensam IT-arkitektur / stödjande IT-område  
> **Senast reviderad:** 2026-08-18

## 1. Syfte, omfattning och relationer

### 1.1 Syfte

Förmågan ska ge utvecklingsområden stöd för att köra applikationer, tjänster, batchjobb och andra workloads i ändamålsenliga, säkra och förvaltningsbara exekveringsmiljöer.

Syftet är att utvecklingsområden ska kunna uttrycka behov i termer av exempelvis exekveringsmodell, skalning, isolering, tillgänglighet, resursprofil, operativsystemskrav och livscykel, medan den stödjande IT-organisationen erbjuder lämpliga runtime- och plattformstjänster.

Förmågan ska motverka att produktnamn som OpenShift, JBoss EAP eller RHEL blir krav i sig när det egentliga behovet handlar om exekveringsegenskaper.

### 1.2 Omfattning

Förmågan omfattar bland annat:

- exekvering av applikationer och tjänster
- containerbaserad runtime
- Java application runtime
- virtuella maskiner
- operativsystemsmiljöer
- batch- och schemalagda workloads
- serverless-/funktionsliknande exekvering där sådan erbjuds
- processisolering
- resursallokering
- CPU- och minnesprofiler
- skalning ur runtimeperspektiv
- deployment targets
- runtimekonfiguration
- miljövariabler och runtimeparametrar
- tekniska middleware-komponenter som del av exekveringsmiljö
- applikationsservrar
- web-/proxykomponenter nära runtime
- plattformsnivå för livscykel, patchning och uppgradering

### 1.3 Utanför förmågan

Följande hör primärt hemma i andra förmågor:

- CI/CD, bygg, test och releaseprocess – **Programvaruutveckling och leverans**
- loggning, metrics, tracing, backup och återställning – **Driftbarhet och motståndskraft**
- nätverk, API:er, messaging och kommunikation – **Integration och kommunikation**
- tjänsteidentiteter, certifikat och secrets – **Identitet och tillit**
- databaser och informationslagring – **Data- och informationshantering**
- användargränssnitt – **Interaktion, presentation och kanaler**

Operativsystem, containerplattformar och applikationsservrar är tekniska realiseringar inom denna förmåga och ska inte beskrivas som verksamhetsbehov.

### 1.4 Relation till andra förmågor

**Programvaruutveckling och leverans** producerar artefakter och deploymentpaket som denna förmåga exekverar.

**Driftbarhet och motståndskraft** tillhandahåller observability, backup, recovery och driftmekanismer för workloads och runtimeplattformar.

**Integration och kommunikation** ger nätverk, exponering, lastbalansering och systemkommunikation.

**Identitet och tillit** ger tjänsteidentiteter, certifikat och secrets som workloads behöver.

**Data- och informationshantering** tillhandahåller databaser och andra persistenta datatjänster.

---

## 2. Behov och användningsområden

### 2.1 Typiska behov

Ett utvecklingsområde kan behöva stöd när ett IT-stöd ska:

- köra stateless backendtjänster
- köra Java-applikationer
- köra containeriserade tjänster
- köra legacyapplikation som kräver viss runtime
- köra batchjobb
- köra schemalagda jobb
- använda virtuell maskin på grund av tekniska beroenden
- skala horisontellt
- ha särskilda CPU- eller minnesbehov
- isoleras från andra workloads
- köras i viss säkerhetszon
- använda viss operativsystemsfunktion
- uppfylla särskilda tillgänglighets- eller kontinuitetskrav
- kunna uppgraderas utan långvariga avbrott
- stödja blue/green, rolling eller annan deploymentmodell
- använda gemensam middleware nära runtime

### 2.2 Typiska användningsfall

#### Containeriserad backendtjänst

En stateless tjänst paketeras som container och körs på en gemensam containerplattform med standardiserad deployment, nätverk, secrets och observability.

#### Java-applikation på applikationsserver

En Java EE/Jakarta EE-applikation kräver en förvaltad applikationsserver och gemensamma runtimefunktioner.

#### Legacyapplikation på virtuell maskin

En applikation kräver operativsystemsnära installation eller produktberoenden som gör containerisering olämplig.

#### Batchjobb

Ett återkommande jobb behöver köras enligt schema, med kontrollerad resursallokering och tydlig felhantering.

#### Teknisk middlewarekomponent

En proxy-, webb- eller applikationsserverkomponent körs som del av en gemensam runtime- eller kommunikationstjänst.

### 2.3 Centrala arkitekturfrågor

Utvecklingsområdet bör bland annat ta ställning till:

- Är workloaden stateless eller stateful?
- Behöver den container, VM eller annan runtime?
- Vilka språk- och runtimekrav finns?
- Vilka CPU-, minnes- och lagringsbehov finns?
- Behövs horisontell eller vertikal skalning?
- Vilka tillgänglighetskrav finns?
- Kan workloaden startas om utan dataförlust?
- Vilken startup-/shutdownmodell krävs?
- Behövs särskild operativsystemsåtkomst?
- Finns produktberoenden som låser runtime?
- Hur hanteras konfiguration och secrets?
- Hur exponeras tjänsten?
- Vilka nätzoner behöver den finnas i?
- Hur snabbt behöver plattformen kunna skala?
- Hur sker patchning och uppgradering?
- Hur påverkas applikationen av runtimeplattformens versionslivscykel?
- Behövs GPU eller annan specialiserad hårdvara?

---

## 3. Förmågespecifika arkitekturprinciper

Gemensamma principer finns i `../styrning/gemensamma-arkitekturprinciper.md`.

### P-AR-01 Runtime väljs efter workloadens egenskaper

**Princip:**  
Val av containerplattform, applikationsserver, VM eller annan runtime ska utgå från workloadens faktiska behov.

**Motivering:**  
Olika runtimeformer har olika kompromisser kring isolering, flexibilitet, drift och kostnad.

**Konsekvens:**  
En viss teknisk plattform ska inte vara obligatorisk utan att behovet motiverar den.

### P-AR-02 Plattformen ska abstrahera onödig infrastruktur

**Princip:**  
Utvecklingsområdet bör konsumera en definierad runtimetjänst snarare än behöva hantera underliggande operativsystem, noder och infrastruktur när detta kan standardiseras.

**Motivering:**  
Det minskar lokal driftbörda och förbättrar standardisering.

### P-AR-03 Stateless där det är lämpligt

**Princip:**  
Applikationstjänster bör vara stateless när verksamhets- och teknikbehov tillåter det.

**Motivering:**  
Stateless workloads är enklare att skala, ersätta och återstarta.

**Konsekvens:**  
Persistent verksamhetsdata bör hanteras i avsedda datatjänster.

### P-AR-04 Runtime och applikationskod ska ha separata livscykler

**Princip:**  
Applikationer ska så långt som möjligt kunna uppgraderas oberoende av underliggande runtimeplattform, och plattformen ska kunna patchas utan onödiga applikationsändringar.

**Motivering:**  
Minskar koppling och förenklar säkerhetsuppdateringar.

### P-AR-05 Konfiguration ska separeras från artefakt

**Princip:**  
Miljöspecifik konfiguration och secrets ska inte byggas in i applikationsartefakten.

**Motivering:**  
Samma artefakt ska kunna flyttas mellan miljöer med kontrollerad konfiguration.

### P-AR-06 Runtimekrav ska uttryckas som egenskaper

**Princip:**  
Utvecklingsområden bör uttrycka behov av exempelvis Java-version, minne, CPU, nätzon och tillgänglighet snarare än krav på specifika underliggande produkter där detta inte är nödvändigt.

**Motivering:**  
Det gör plattformen utbytbar och arkitekturen mer långlivad.

### P-AR-07 Legacykrav ska synliggöras som begränsningar

**Princip:**  
Produkt- eller operativsystemskrav som följer av äldre applikationer ska dokumenteras som begränsningar och livscykelrisker, inte som generella arkitekturprinciper.

**Motivering:**  
Teknisk skuld ska inte institutionaliseras som framtida standard.

---

## 4. Krav och styrande riktlinjer

### KR-AR-01 Stödd runtime

**Krav:**  
Produktionsapplikationer ska köras på en runtimeplattform eller operativsystemsversion som är inom beslutad support- och livscykelperiod.

**Motivering/källa:**  
Säkerhet, förvaltningsbarhet och livscykel.

### KR-AR-02 Resursprofil

**Krav:**  
Workloads ska ha dokumenterade och rimligt dimensionerade resursbehov för CPU, minne och andra relevanta resurser.

**Motivering/källa:**  
Kapacitet och kostnadseffektivitet.

### KR-AR-03 Konfiguration och secrets

**Krav:**  
Miljöspecifik konfiguration och secrets ska hanteras utanför applikationsartefakten med godkända mekanismer.

**Motivering/källa:**  
Säkerhet och förändringsbarhet.

### KR-AR-04 Graceful shutdown och restart

**Krav:**  
Workloads som körs på plattformar där instanser kan ersättas eller startas om ska hantera kontrollerad nedstängning och återstart på ett sätt som inte orsakar onödig dataförlust eller korruption.

**Motivering/källa:**  
Driftbarhet och kontinuitet.

### KR-AR-05 Hälsokontroller

**Krav:**  
Långlivade applikationstjänster på gemensam runtimeplattform ska exponera eller stödja relevanta readiness-/liveness-/health-mekanismer när plattformen använder dessa.

**Motivering/källa:**  
Tillgänglighet och driftbarhet.

### KR-AR-06 Persistent data utanför lokal runtime

**Krav:**  
Persistent verksamhetsdata ska inte vara beroende av lokal ephemeral disk eller en enskild runtimeinstans om detta inte är uttryckligen avsett och dokumenterat.

**Motivering/källa:**  
Kontinuitet och datahantering.

### KR-AR-07 Tekniska beroenden

**Krav:**  
Kritiska beroenden till specifikt operativsystem, runtime, middleware eller native-komponent ska dokumenteras när de begränsar portabilitet eller uppgraderingsbarhet.

**Motivering/källa:**  
Livscykel och förändringsbarhet.

### KR-AR-08 Isolering

**Krav:**  
Workloads med särskilda säkerhets- eller stabilitetskrav ska använda den isoleringsnivå som motsvarar behovet.

**Motivering/källa:**  
Säkerhet och motståndskraft.

---

## 5. Guidelines och vägledning

### Container eller virtuell maskin?

Container är ofta lämplig när:

- workloaden kan paketeras med tydliga beroenden
- snabb deployment och skalning är viktig
- applikationen inte kräver full OS-kontroll
- standardiserad containerplattform finns

Virtuell maskin kan vara lämplig när:

- applikationen kräver operativsystemsnära installation
- legacyprodukt inte stödjer container
- särskilda drivrutiner eller systemkomponenter krävs
- leverantörssupport kräver VM/OS-installation

### När passar OpenShift?

OpenShift kan vara lämplig som realisering av en gemensam Container Application Platform för:

- containeriserade backendtjänster
- stateless applikationer
- vissa stateful workloads där plattformen och datamodellen stödjer det
- standardiserad deployment och skalning

Utvecklingsområdet bör i första hand konsumera **Container Application Platform**, inte kräva OpenShift som produkt om inte ett specifikt behov kräver det.

### När passar JBoss EAP?

JBoss EAP kan vara lämplig som realisering av en **Java Application Runtime** när applikationen behöver funktioner i Jakarta EE/Java EE eller annan support som plattformen erbjuder.

Nya applikationer bör inte bindas till applikationsserverfunktioner utan tydlig nytta.

### Var passar RHEL?

RHEL är främst ett tekniskt byggblock eller operativsystemstandard under exempelvis:

- VM Runtime
- Java Application Runtime
- containerplattformens noder
- vissa middlewareprodukter

Utvecklingsområdet bör normalt inte konsumera "RHEL" som förmåga utan en runtimetjänst med definierad supportmodell.

### Var passar JBoss Core Services?

JBoss Core Services kan realisera web server-, proxy- eller load balancing-funktioner nära runtime och Integration/kommunikation.

Klassificeringen bör utgå från vilken tjänst komponenten faktiskt realiserar. Produkten i sig behöver inte ha en unik förmågehemvist.

### När bör batch köras på gemensam plattform?

Gemensam Batch Runtime är lämplig när:

- jobb behöver schemaläggas
- resursanvändning ska styras
- execution history behövs
- retry/felhantering ska standardiseras
- flera utvecklingsområden har liknande behov

### Stateful workload på containerplattform?

Det är möjligt, men bedöm:

- persistent lagring
- failover
- ordering
- backup
- scaling
- uppgraderingsmodell
- leverantörsstöd

En containerplattform gör inte automatiskt en stateful applikation molnnativ eller lättförvaltad.

### Hur uttrycks runtimebehov?

Beskriv exempelvis:

- runtimefamilj
- språk/runtimeversion
- CPU/minne
- antal instanser
- scalingprofil
- nätzon
- persistent lagring
- startup time
- tillgänglighet
- specialhårdvara

Undvik produktkrav om tjänsteegenskaper räcker.

### När standardlösningen inte passar

Dokumentera:

- tekniskt beroende
- leverantörskrav
- operativsystemskrav
- native libraries
- resursprofil
- säkerhetszon
- hårdvarukrav
- availability
- supportlivscykel

Därefter bedöms om gemensam plattform kan utökas eller om särskild runtime behövs.

---

## 6. Plattformar och tjänsteerbjudanden

I detta steg identifieras kandidater. Detaljerade plattformsdokument skapas separat senare eller tidigare vid konkret behov.

| Erbjudande | Syfte | Lämpligt för | Möjlig realisering idag | Status |
|---|---|---|---|---|
| Container Application Platform | Exekvera och hantera containeriserade workloads | moderna backendtjänster och containerapplikationer | OpenShift | Kandidat |
| Java Application Runtime | Förvaltad runtime för Java/Jakarta EE | Java-applikationer med behov av applikationsserver | JBoss EAP | Kandidat |
| Virtual Machine Runtime | Exekvera workloads med OS-nära behov | legacy, COTS och särskilda tekniska beroenden | RHEL-baserade VM:er m.fl. | Kandidat |
| Linux Runtime | Standardiserad Linux-baserad exekveringsmiljö | serverapplikationer och middleware | RHEL | Kandidat |
| Batch Runtime | Schemalagd och kontrollerad jobbkörning | batch- och bakgrundsjobb | Produkt/plattform ej beslutad | Kandidat |
| Web/Proxy Runtime | Webbserver, proxy och närliggande runtimefunktioner | webbexponering och middleware | JBoss Core Services där relevant | Kandidat |
| Specialized Compute Runtime | Exekvering med specialiserade resurser | exempelvis AI/GPU-workloads | Ej beslutad | Kandidat |

Det bör senare avgöras vilka erbjudanden som är självständiga plattformstjänster och vilka som är profiler på samma underliggande plattform.

---

## 7. Standarder och teknikval

| Standard/teknikval | Status | Tillämpning |
|---|---|---|
| OpenShift | Befintlig produkt att klassificera | Container Application Platform |
| JBoss EAP | Befintlig produkt att klassificera | Java Application Runtime |
| RHEL | Befintlig produkt/OS-standard | Linux/VM Runtime och tekniska byggblock |
| JBoss Core Services | Befintlig produkt att klassificera | Web/proxy/runtimekomponent |
| OCI Container Image | Kandidat | containerformat |
| Java Runtime-versioner | Kandidat | stödpolicy för Java |
| Base image-standard | Kandidat | containerbaser och patchning |
| Runtime configuration-standard | Kandidat | miljöspecifik konfiguration |
| Resource profile-standard | Kandidat | CPU/minne/limits/requests |
| Health check-standard | Kandidat | readiness/liveness/health |

Exakta versioner ska hållas i separat livscykel- eller standarddokumentation.

---

## 8. Relaterade artefakter och kvalitetsdimensioner

### 8.1 Relevanta kvalitetsdimensioner

Särskilt viktiga dimensioner är:

- **Säkerhet och informationsskydd** – isolering, patchning och secrets påverkar runtime.
- **Tillgänglighet** – runtimeplattformens redundans och restartbeteende är centralt.
- **Kontinuitet och återställningsförmåga** – workloads behöver kunna återstartas och återetableras.
- **Prestanda** – CPU, minne, IO och startup påverkar lösningen.
- **Skalbarhet och kapacitet** – resursprofiler och autoscaling kan vara centrala.
- **Spårbarhet och verifierbarhet** – runtimeinstans, version och deployment behöver kunna identifieras.
- **Förvaltningsbarhet och förändringsbarhet** – patchning och plattformsuppgraderingar är kärnfrågor.
- **Interoperabilitet och portabilitet** – standardiserade containerformat och runtimekontrakt kan minska lock-in.
- **Livscykel och hållbarhet** – OS, runtime och middleware har tydliga supportcykler.
- **Kostnads- och resurseffektivitet** – överdimensionering och ineffektiv workloadplacering bör undvikas.

### 8.2 Lösningsmönster

Identifierade kandidater:

- Stateless Service
- Containerized Application
- Externalized Configuration
- Immutable Deployment Artifact
- Horizontal Scaling
- Rolling Deployment
- Blue/Green Deployment
- Graceful Shutdown
- Health Check
- Sidecar (att bedöma tvärgående)
- Scheduled Batch Job
- Runtime Isolation
- Legacy Application on VM

### 8.3 Plattformar

Identifierade kandidater:

- Container Application Platform
- Java Application Runtime
- Virtual Machine Runtime
- Linux Runtime
- Batch Runtime
- Web/Proxy Runtime
- Specialized Compute Runtime

### 8.4 Tekniska standarder

Identifierade kandidater:

- OpenShift-standard
- JBoss EAP-standard
- RHEL-standard
- JBoss Core Services-standard
- OCI Container Image
- Java runtime-policy
- base image-standard
- runtime configuration-standard
- resource profile-standard
- health check-standard

### 8.5 Kandidater till referensarkitekturer

Följande kandidater stärks eller identifieras:

- **Containerbaserad mikrotjänstelösning**
- **Internt handläggningsstöd**
- **Publik e-tjänst**
- **Legacy-/COTS-baserat verksamhetssystem**
- **Batchintensivt verksamhetssystem**
- **AI-baserat verksamhetsstöd med specialiserad compute**
- **Integrationsintensivt verksamhetssystem**

### 8.6 Teknisk dokumentation

När konkreta runtimeplattformar dokumenteras bör teknisk referens exempelvis omfatta:

- deployment
- images och artefakter
- namespace/projekt
- resursgränser
- konfiguration
- secrets
- nätverk
- storage mounts
- health checks
- autoscaling
- logging
- patchning
- versionsstöd
- backup av plattformsmetadata
- felsökning
- tekniska begränsningar

---

## Arbetsanteckningar

### Identifierade kandidater

**Lösningsmönster**
- Stateless Service
- Containerized Application
- Externalized Configuration
- Immutable Deployment Artifact
- Horizontal Scaling
- Rolling Deployment
- Blue/Green Deployment
- Graceful Shutdown
- Health Check
- Sidecar
- Scheduled Batch Job
- Runtime Isolation
- Legacy Application on VM

**Plattformar/tjänster**
- Container Application Platform
- Java Application Runtime
- Virtual Machine Runtime
- Linux Runtime
- Batch Runtime
- Web/Proxy Runtime
- Specialized Compute Runtime

**Tekniska standarder**
- OpenShift
- JBoss EAP
- RHEL
- JBoss Core Services
- OCI Container Image
- Java runtime-policy
- base image-standard
- runtime configuration-standard
- resource profile-standard
- health check-standard

**Referensarkitekturer**
- containerbaserad mikrotjänstelösning
- internt handläggningsstöd
- publik e-tjänst
- legacy-/COTS-baserat verksamhetssystem
- batchintensivt verksamhetssystem
- AI-baserat verksamhetsstöd med specialiserad compute
- integrationsintensivt verksamhetssystem

**Gränsdragningsfrågor**
- om Linux Runtime och VM Runtime bör vara separata erbjudanden
- hur JBoss Core Services ska delas mellan runtime och Integration/kommunikation
- hur mycket deploymentmönster som ska ligga här jämfört med Programvaruutveckling och leverans
- hur stateful workloads på OpenShift ska relateras till Data- och informationshantering
- om specialiserad compute/GPU ska vara egen tjänsteprofil eller del av runtimeplattform
