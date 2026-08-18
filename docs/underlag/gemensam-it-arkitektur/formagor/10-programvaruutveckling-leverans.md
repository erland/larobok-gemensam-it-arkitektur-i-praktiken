# Förmåga: Programvaruutveckling och leverans

> **Status:** Utkast  
> **Ansvarig:** Gemensam IT-arkitektur / stödjande IT-område  
> **Senast reviderad:** 2026-08-18

## 1. Syfte, omfattning och relationer

### 1.1 Syfte

Förmågan ska ge utvecklingsområden stöd för att utveckla, bygga, testa, paketera, kvalitetssäkra, versionshantera och leverera programvara på ett effektivt, reproducerbart och säkert sätt.

Syftet är att erbjuda gemensamma arbetssätt, plattformar och standarder för hela engineering-livscykeln från källkod till deploybar artefakt och produktionssättning.

Förmågan ska inte bli en generell kategori för all teknik som används av utvecklare. Teknik klassificeras här endast när dess primära funktion är att stödja programvaruutveckling och leverans.

### 1.2 Omfattning

Förmågan omfattar bland annat:

- källkodshantering
- versionshantering
- branch- och mergeflöden
- utvecklingsmiljöer
- IDE-stöd
- byggsystem
- dependency management
- paketering
- artefakthantering
- testautomation
- statisk kodanalys
- kodkvalitet
- säkerhetskontroller i utvecklingsflödet
- Software Composition Analysis
- SBOM
- container image build
- CI
- CD
- releasehantering
- deploymentautomation
- promotion mellan miljöer
- feature flags ur leveransperspektiv
- kvalitetsspärrar
- pipeline-as-code
- versionsmärkning
- releaseartefakter
- developer experience
- tekniska mallar och starter projects

### 1.3 Utanför förmågan

Följande hör primärt hemma i andra förmågor:

- applikationens exekveringsmiljö – **Applikationsexekvering och runtime**
- observability och driftövervakning – **Driftbarhet och motståndskraft**
- verksamhetsprocesser och workflow – **Process, workflow och ärendehantering**
- databaser och datahantering – **Data- och informationshantering**
- API:er, messaging och nätverkskommunikation – **Integration och kommunikation**
- användargränssnitt och frontendarkitektur – **Interaktion, presentation och kanaler**
- identitet, secrets och tjänsteidentiteter – **Identitet och tillit**

Angular, JPA och liknande hör därför inte primärt hemma här bara för att de används i utveckling. De klassificeras utifrån den förmåga de realiserar.

### 1.4 Relation till andra förmågor

**Applikationsexekvering och runtime** är målmiljö för de artefakter och deploymentpaket som denna förmåga producerar.

**Driftbarhet och motståndskraft** anger vilka observability- och driftkrav som behöver byggas in och verifieras innan leverans.

**Identitet och tillit** tillhandahåller utvecklaridentiteter, pipelineidentiteter, secrets och åtkomstkontroll.

**Integration och kommunikation** kan ge tekniska gränssnitt för deployment, artefaktdistribution och beroenden.

**Interaktion, presentation och kanaler**, **Data- och informationshantering** och övriga förmågor definierar de tekniska standarder som utvecklingsflödet behöver kunna bygga och verifiera.

---

## 2. Behov och användningsområden

### 2.1 Typiska behov

Ett utvecklingsområde kan behöva stöd när det ska:

- hantera källkod för flera team
- skapa reproducerbara byggen
- automatisera enhetstest och integrationstest
- hantera externa dependencies
- kontrollera sårbarheter i beroenden
- bygga container images
- skapa versionsmärkta releaseartefakter
- distribuera till test- och produktionsmiljöer
- genomföra samma leveransprocess konsekvent
- säkra att endast godkända artefakter når produktion
- spåra vilken kodversion som körs
- hantera rollback eller roll-forward
- standardisera projektstruktur
- ge utvecklare gemensamma IDE- och utvecklingsverktyg
- minska manuell hantering i releaseprocessen

### 2.2 Typiska användningsfall

#### CI för backendtjänst

Vid commit körs bygg, enhetstest, kodanalys, dependencykontroll och paketering automatiskt.

#### Containerbaserad leverans

En applikation byggs till en versionerad OCI-image, publiceras till artefaktregister och deployas vidare till containerplattform.

#### Java-applikation

Maven/Gradle-baserat bygge producerar en artefakt som deployas till Java runtime eller paketeras som container.

#### Frontendapplikation

Frontend byggs, testas och paketeras som statiska artefakter eller containerimage med spårbar versionsinformation.

#### Kontrollerad produktionsrelease

Samma versionsmärkta artefakt som verifierats i tidigare miljöer promoveras till produktion utan ombyggnad.

### 2.3 Centrala arkitekturfrågor

Utvecklingsområdet bör bland annat ta ställning till:

- Var lagras källkod?
- Hur ser branch- och mergeflödet ut?
- Hur skapas reproducerbara builds?
- Hur versionssätts programvara?
- Hur hanteras dependencies?
- Hur verifieras licenser och sårbarheter?
- Vilka tester ska automatiseras?
- Vilka kvalitetsspärrar krävs?
- Hur produceras och signeras artefakter?
- Var lagras artefakter?
- Hur sker promotion mellan miljöer?
- Byggs artefakten en gång eller på nytt per miljö?
- Hur hanteras secrets i pipelines?
- Vilken identitet använder en pipeline?
- Hur sker rollback eller roll-forward?
- Hur verifieras deployment?
- Vilken information behövs för spårbarhet från produktion tillbaka till commit?
- Hur mycket standardisering ska ske genom gemensamma pipeline-mallar?

---

## 3. Förmågespecifika arkitekturprinciper

Gemensamma principer finns i `../styrning/gemensamma-arkitekturprinciper.md`.

### P-PUL-01 Bygg en gång, promovera samma artefakt

**Princip:**  
En releaseartefakt bör byggas en gång och därefter promoveras mellan miljöer utan ombyggnad.

**Motivering:**  
Det ökar reproducerbarhet och säkerställer att testad artefakt är samma som produktionssätts.

### P-PUL-02 Automatisering före manuell leverans

**Princip:**  
Bygg, test, paketering och deployment bör automatiseras där det är praktiskt och proportionerligt.

**Motivering:**  
Manuella steg ökar risken för fel och gör leveranser svårare att reproducera.

### P-PUL-03 Pipeline som kod

**Princip:**  
Leveransflöden bör versionshanteras tillsammans med eller på samma kontrollerade sätt som övrig kod.

**Motivering:**  
Pipelineförändringar påverkar leveransen och behöver spårbarhet och review.

### P-PUL-04 Artefakter ska vara versionsmärkta och spårbara

**Princip:**  
Deploybara artefakter ska kunna kopplas till källkodsversion, bygg och relevanta kontroller.

**Motivering:**  
Det möjliggör felsökning, audit och reproducerbarhet.

### P-PUL-05 Kvalitet ska verifieras tidigt och automatiskt

**Princip:**  
Relevanta tester, kodkvalitetskontroller och säkerhetskontroller bör köras så tidigt som möjligt i utvecklingsflödet.

**Motivering:**  
Fel är billigare och säkrare att hitta före deployment.

### P-PUL-06 Miljöspecifik konfiguration ska hållas utanför byggartefakten

**Princip:**  
Samma artefakt ska kunna användas i flera miljöer med separat, kontrollerad konfiguration.

**Motivering:**  
Minskar miljöskillnader och förbättrar reproducerbarhet.

### P-PUL-07 Gemensamma mallar ska minska friktion, inte låsa arkitekturen

**Princip:**  
Starter projects, pipeline-mallar och gemensamma komponenter ska ge en bra standardväg utan att omotiverat förhindra avsteg där behovet skiljer sig.

**Motivering:**  
Standardisering ska ge effektivitet och kvalitet, inte skapa onödig teknisk inlåsning.

---

## 4. Krav och styrande riktlinjer

### KR-PUL-01 Versionshanterad källkod

**Krav:**  
Produktionsrelaterad källkod och centrala build-/pipeline-definitioner ska versionshanteras i godkänd källkodstjänst.

**Motivering/källa:**  
Spårbarhet, förändringskontroll och förvaltningsbarhet.

### KR-PUL-02 Reproducerbart bygge

**Krav:**  
Byggprocessen ska vara tillräckligt automatiserad och dokumenterad för att en releaseartefakt ska kunna återskapas på ett kontrollerat sätt.

**Motivering/källa:**  
Reproducerbarhet och livscykel.

### KR-PUL-03 Automatiserade tester

**Krav:**  
IT-stöd ska ha automatiserade tester på en nivå som motsvarar lösningens komplexitet, risk och förändringstakt.

**Motivering/källa:**  
Kvalitet och förändringsbarhet.

### KR-PUL-04 Dependencykontroll

**Krav:**  
Externa programvaruberoenden ska kunna inventeras och kontrolleras avseende relevanta sårbarheter och livscykel.

**Motivering/källa:**  
Säkerhet och programvarulivscykel.

### KR-PUL-05 Pipeline-secrets

**Krav:**  
Credentials och secrets som används i bygg- och leveransflöden ska hanteras via godkända secretsmekanismer och får inte lagras i klartext i pipelinekod eller repository.

**Motivering/källa:**  
Säkerhet och informationsskydd.

### KR-PUL-06 Spårbar release

**Krav:**  
Produktionssatt programvara ska kunna kopplas till relevant källkodsversion och releaseartefakt.

**Motivering/källa:**  
Spårbarhet och verifierbarhet.

### KR-PUL-07 Separata pipelineidentiteter

**Krav:**  
Automatiserade pipelines ska använda dedikerade tekniska identiteter och inte personliga utvecklarkonton för produktionsrelaterade åtgärder.

**Motivering/källa:**  
Säkerhet och ansvar.

### KR-PUL-08 Kontrollerad promotion

**Krav:**  
Promotion till produktionsmiljö ska ske genom definierat och spårbart leveransflöde.

**Motivering/källa:**  
Förändringskontroll och driftbarhet.

### KR-PUL-09 Artefaktregister

**Krav:**  
Deploybara binärer, paket och container images ska lagras i godkänd artefakttjänst med versions- och livscykelhantering.

**Motivering/källa:**  
Reproducerbarhet, säkerhet och förvaltning.

---

## 5. Guidelines och vägledning

### Jenkins som plattform eller produkt?

Jenkins bör primärt ses som möjlig realisering av en **CI/CD Platform**.

Utvecklingsområdet bör konsumera en definierad pipeline- och leveranstjänst med:

- standardiserade runners/agents
- gemensam autentisering
- secrets
- artefaktintegration
- mallar
- loggning
- supportmodell

Jenkins i sig bör inte bli ett generellt arkitekturkrav om annan realisering kan uppfylla samma behov.

### Var passar IntelliJ IDEA?

IntelliJ IDEA är ett utvecklarverktyg inom denna förmåga och kan ingå i ett gemensamt **Developer Tooling**-erbjudande eller standard.

Det är inte en plattformstjänst för applikationen och bör hållas skilt från runtime.

### CI eller CD?

**CI** fokuserar på att kontinuerligt bygga och verifiera förändringar.

**Continuous Delivery** innebär att programvaran hålls i levererbart skick och kan promoveras automatiserat eller kontrollerat.

**Continuous Deployment** innebär att godkända förändringar automatiskt går hela vägen till produktion.

Organisationen behöver inte välja samma nivå för alla system.

### Trunk-based eller långlivade branches?

Trunk-based development kan minska integrationsproblem och passar väl med frekvent CI.

Långlivade branches kan ibland behövas men ökar risk för divergens.

Branchstrategi bör anpassas till:

- teamstorlek
- releasefrekvens
- regulatoriska krav
- produktlivscykel
- parallella underhållsversioner

### Maven/Gradle/npm och liknande

Buildverktyg är tekniska standarder och bör väljas utifrån språk och ekosystem.

Det centrala arkitekturkravet är inte exakt verktyg utan att builden är:

- automatiserad
- reproducerbar
- spårbar
- dependencykontrollerad

### Hur bör dependencies hanteras?

Utvecklingsområdet bör:

- låsa eller kontrollera versioner där det är lämpligt
- undvika okontrollerade latest-versioner
- kunna inventera transitive dependencies
- följa sårbarheter
- ha strategi för uppgradering
- hantera licensrisk

### SBOM

SBOM är särskilt värdefullt när organisationen behöver kunna spåra vilka komponenter som ingår i levererad programvara.

Det bör integreras i build-/artefaktflödet om kravbilden motiverar det.

### Releaseversion från Git?

Version bör så långt som möjligt härledas automatiskt från en etablerad versionskälla, exempelvis release/tagg eller motsvarande, i stället för att manuellt dupliceras i flera filer.

Det minskar risken för inkonsistens.

### Deployment eller runtime?

Deploymentmekanismen hör primärt till denna förmåga.

Den miljö som tar emot deploymenten hör till **Applikationsexekvering och runtime**.

Exempel:

```text
CI/CD Platform
   ↓ deployerar
Container Application Platform
```

### När standardlösningen inte passar

Beskriv behovet i termer av:

- språk och buildmodell
- repositorymodell
- byggtid
- testbehov
- säkerhetskontroller
- artefakttyp
- deploymentmål
- releasefrekvens
- reglerade godkännanden
- offline-/isolerad miljö
- leverantörsberoenden

Därefter bedöms om standardpipeline kan utökas eller om särskilt leveransflöde behövs.

---

## 6. Plattformar och tjänsteerbjudanden

I detta steg identifieras kandidater. Detaljerade plattformsdokument skapas separat senare eller tidigare vid konkret behov.

| Erbjudande | Syfte | Lämpligt för | Möjlig realisering idag | Status |
|---|---|---|---|---|
| Source Code Management | Versionshantering och samarbete kring kod | samtliga utvecklingsteam | Produkt ej beslutad i detta steg | Kandidat |
| CI/CD Platform | Bygg, test, paketering och deployment | automatiserade leveransflöden | Jenkins | Kandidat |
| Artifact Repository | Lagra binärer, paket och images | versionsmärkta releaseartefakter | Produkt ej beslutad | Kandidat |
| Container Build Service | Bygga och verifiera OCI-images | containerbaserade lösningar | Jenkins/OpenShift-relaterad realisering möjlig | Kandidat |
| Code Quality Service | Statisk analys och kvalitetskontroller | kodbaser med automatiserad CI | Produkt ej beslutad | Kandidat |
| Dependency/Supply Chain Security | Inventera och kontrollera beroenden | samtliga produktionslösningar | Produkt ej beslutad | Kandidat |
| Test Automation Support | Gemensamma testverktyg och ramverk | automatiserade tester | Flera möjliga realiseringar | Kandidat |
| Developer Tooling | Standardiserade utvecklarverktyg | utvecklare | IntelliJ IDEA m.fl. | Kandidat |
| Project Templates / Golden Paths | Starter projects och pipeline-mallar | nya tjänster och applikationer | Gemensamma mallar | Kandidat |
| Release Management Support | Versions- och releaseflöden | lösningar med kontrollerad promotion | Produkt/process ej beslutad | Kandidat |

---

## 7. Standarder och teknikval

| Standard/teknikval | Status | Tillämpning |
|---|---|---|
| Jenkins | Befintlig produkt att klassificera | CI/CD Platform |
| IntelliJ IDEA | Befintligt utvecklarverktyg att klassificera | Developer Tooling |
| Git | Kandidat/befintlig standard att verifiera | versionshantering |
| Semantic Versioning eller beslutad versionsmodell | Kandidat | releaseversionering |
| Pipeline-as-Code | Kandidat | pipeline-definitioner |
| OCI Container Image | Kandidat | containerartefakter |
| SBOM-format | Kandidat | software supply chain |
| Dependency lock-policy | Kandidat | reproducerbara builds |
| Artefaktnamnsstandard | Kandidat | spårbarhet och versionshantering |
| Gemensam branch-/mergepolicy | Kandidat | kodflöde |
| Gemensam release/tag-policy | Kandidat | versionskälla och releaseidentifiering |

Exakta produktversioner och plugins ska dokumenteras separat.

---

## 8. Relaterade artefakter och kvalitetsdimensioner

### 8.1 Relevanta kvalitetsdimensioner

Särskilt viktiga dimensioner är:

- **Säkerhet och informationsskydd** – supply chain, pipelineidentiteter och secrets.
- **Tillgänglighet** – gemensamma utvecklings- och leveransplattformar påverkar leveransförmågan.
- **Spårbarhet och verifierbarhet** – commit, build, artefakt och deployment behöver kunna kopplas ihop.
- **Regelefterlevnad** – vissa lösningar kan kräva dokumenterade kontroller och godkännanden.
- **Förvaltningsbarhet och förändringsbarhet** – automatiserade flöden är centrala.
- **Interoperabilitet och portabilitet** – standardiserade artefakter och buildverktyg minskar beroenden.
- **Livscykel och hållbarhet** – dependencies, plugins och utvecklingsverktyg behöver aktiv förvaltning.
- **Kostnads- och resurseffektivitet** – gemensamma pipelines och mallar minskar duplicerat arbete.

### 8.2 Lösningsmönster

Identifierade kandidater:

- Continuous Integration
- Build Once, Promote Many
- Pipeline as Code
- Immutable Release Artifact
- Artifact Promotion
- Trunk-Based Development
- Feature Branch Workflow
- Automated Quality Gates
- Dependency Scanning
- SBOM Generation
- Git-based Versioning
- Blue/Green Deployment
- Rolling Deployment
- Feature Flags
- Golden Path / Paved Road
- Reusable Pipeline Template

### 8.3 Plattformar

Identifierade kandidater:

- Source Code Management
- CI/CD Platform
- Artifact Repository
- Container Build Service
- Code Quality Service
- Dependency/Supply Chain Security
- Test Automation Support
- Developer Tooling
- Project Templates / Golden Paths
- Release Management Support

### 8.4 Tekniska standarder

Identifierade kandidater:

- Jenkins-standard
- IntelliJ IDEA-standard
- Git-standard
- versionsmodell
- Pipeline-as-Code-standard
- OCI-image-standard
- SBOM-format
- dependency lock-policy
- artefaktnamnsstandard
- branch-/mergepolicy
- release/tag-policy

### 8.5 Kandidater till referensarkitekturer

Följande kandidater stärks eller identifieras:

- **Standardiserad leveranskedja för containerbaserad tjänst**
- **Standardiserad leveranskedja för Java-applikation**
- **Publik e-tjänst med automatiserad CI/CD**
- **Internt handläggningsstöd med kontrollerad promotion**
- **Software supply chain för myndighetskritisk programvara**
- **Legacy-/COTS-lösning med begränsad automatisering**
- **Utvecklingsplattform / golden path för nya tjänster**

### 8.6 Teknisk dokumentation

När konkreta utvecklings- och leveransplattformar dokumenteras bör teknisk referens exempelvis omfatta:

- repositoryskapande
- branch policies
- pipeline templates
- build agents
- credentials och secrets
- artefaktregister
- container build
- teststeg
- dependency scanning
- SBOM
- release tagging
- promotion
- deployment
- rollback
- pluginlivscykel
- tekniska begränsningar

---

## Arbetsanteckningar

### Identifierade kandidater

**Lösningsmönster**
- Continuous Integration
- Build Once, Promote Many
- Pipeline as Code
- Immutable Release Artifact
- Artifact Promotion
- Trunk-Based Development
- Feature Branch Workflow
- Automated Quality Gates
- Dependency Scanning
- SBOM Generation
- Git-based Versioning
- Blue/Green Deployment
- Rolling Deployment
- Feature Flags
- Golden Path / Paved Road
- Reusable Pipeline Template

**Plattformar/tjänster**
- Source Code Management
- CI/CD Platform
- Artifact Repository
- Container Build Service
- Code Quality Service
- Dependency/Supply Chain Security
- Test Automation Support
- Developer Tooling
- Project Templates / Golden Paths
- Release Management Support

**Tekniska standarder**
- Jenkins
- IntelliJ IDEA
- Git
- versionsmodell
- Pipeline-as-Code
- OCI Container Image
- SBOM-format
- dependency lock-policy
- artefaktnamnsstandard
- branch-/mergepolicy
- release/tag-policy

**Referensarkitekturer**
- standardiserad leveranskedja för containerbaserad tjänst
- standardiserad leveranskedja för Java-applikation
- publik e-tjänst med automatiserad CI/CD
- internt handläggningsstöd med kontrollerad promotion
- software supply chain för myndighetskritisk programvara
- legacy-/COTS-lösning med begränsad automatisering
- utvecklingsplattform / golden path för nya tjänster

**Gränsdragningsfrågor**
- hur deploymentmönster delas mellan denna förmåga och runtimeförmågan
- om release management huvudsakligen är teknisk förmåga eller delvis process/governance utanför taxonomin
- hur utvecklarnas lokala verktyg ska standardiseras utan onödig detaljstyrning
- hur mycket software supply chain-säkerhet som ska ligga här jämfört med gemensam säkerhetsstyrning
- om golden paths bör bli ett eget plattformserbjudande eller ett paket av flera tjänster
