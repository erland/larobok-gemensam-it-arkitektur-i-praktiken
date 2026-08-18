# Förmåga: Integration och kommunikation

> **Status:** Utkast  
> **Ansvarig:** Gemensam IT-arkitektur / stödjande IT-område  
> **Senast reviderad:** 2026-08-18

## 1. Syfte, omfattning och relationer

### 1.1 Syfte

Förmågan ska ge utvecklingsområden stöd för att möjliggöra säkert, robust och förvaltningsbart informationsutbyte och kommunikation mellan applikationer, tjänster, tekniska miljöer, geografiska platser, externa organisationer och myndighetsgemensamma tjänster.

Syftet är att samla behov kring API:er, events, messaging, filutbyte och teknisk konnektivitet i en sammanhängande förmåga, samtidigt som de olika abstraktionsnivåerna hålls tydligt isär.

Utvecklingsområden ska i första hand kunna uttrycka **vilken kommunikation och vilka egenskaper de behöver**, medan plattformsområdet ansvarar för hur detta realiseras med exempelvis API gateway, IBM MQ, SGSI, WAN, brandväggar eller andra tekniska byggblock.

### 1.2 Omfattning

Förmågan omfattar bland annat:

- synkrona API:er
- tjänstegränssnitt
- API management
- eventdriven integration
- asynkron messaging
- köer och topics
- filbaserat informationsutbyte
- managed file transfer
- integrationsflöden och dataförflyttning
- transformation och meddelandekonvertering
- routing av tekniska meddelanden
- extern systemkommunikation
- myndighetsgemensam kommunikation
- service connectivity
- DNS och namnuppslag
- lastbalansering och proxyfunktioner ur kommunikationsperspektiv
- LAN, WAN och trådlös kommunikation
- internetanslutning
- site-to-site-kommunikation
- teknisk zonkommunikation
- kommunikation över säkerhetsgränser
- kommunikationsrelaterade brandväggs- och nätverkspolicyer som realisering

### 1.3 Utanför förmågan

Följande hör primärt hemma i andra förmågor:

- verksamhetsmässig processorkestrering – **Process, workflow och ärendehantering**
- verksamhetsregler och beslut – **Regler och beslut**
- primär datahantering och lagring – **Data- och informationshantering**
- identiteter, autentisering, certifikat och tjänsteidentiteter – **Identitet och tillit**
- säkerhet som generell kvalitetsdimension – **Krav- och kvalitetsperspektivet**
- exekveringsmiljöer och runtime – **Applikationsexekvering och runtime**
- observability, central loggning och incidentdiagnostik – **Driftbarhet och motståndskraft**

Routrar, switchar, brandväggar och accesspunkter är normalt **tekniska byggblock** inom realiseringen och inte egna kravperspektiv.

### 1.4 Relation till andra förmågor

**Process, workflow och ärendehantering** använder integrationsmekanismer för att kommunicera med andra system, men processen ansvarar för verksamhetsmässig koordinering medan denna förmåga ansvarar för tekniskt informationsutbyte.

**Data- och informationshantering** äger informationens persistens och livscykel. Integration transporterar eller distribuerar information mellan ansvariga parter.

**Identitet och tillit** tillhandahåller identiteter, certifikat och autentiseringsmekanismer som används i kommunikationsflöden.

**Driftbarhet och motståndskraft** tillhandahåller övervakning och felsökningsförmåga för integrations- och kommunikationstjänster.

**Applikationsexekvering och runtime** tillhandahåller miljöerna där integrationskomponenter och klienter körs.

---

## 2. Behov och användningsområden

### 2.1 Typiska behov

Ett utvecklingsområde kan behöva stöd när ett IT-stöd ska:

- exponera funktionalitet via API
- konsumera API:er från andra system
- kommunicera asynkront via meddelanden
- publicera eller konsumera events
- överföra filer säkert
- kommunicera med annan myndighet
- använda myndighetsgemensamma kommunikationstjänster
- flytta eller transformera data mellan system
- ge externa parter kontrollerad åtkomst
- koppla samman komponenter över olika nätsegment
- kommunicera mellan geografiska platser
- erbjuda trådlös anslutning för klienter eller utrustning
- få redundant eller högtilgänglig nätverkskommunikation
- skydda kommunikation över säkerhetsgränser
- hantera återförsök och buffring vid tillfälliga avbrott

### 2.2 Typiska användningsfall

#### Synkron tjänsteintegration

Ett system behöver hämta aktuell information eller initiera en funktion i ett annat system och behöver svar inom samma användar- eller processflöde.

#### Asynkron meddelandekommunikation

Ett system behöver skicka information till ett annat utan krav på omedelbart svar och med behov av robust leverans.

#### Händelsedriven integration

Ett system publicerar en verksamhetshändelse som flera konsumenter kan reagera på utan direkt koppling till producenten.

#### Filbaserat informationsutbyte

Större eller standardiserade informationsmängder behöver utbytas i filer, exempelvis med extern part eller batchorienterat system.

#### Myndighetsgemensam kommunikation

Ett IT-stöd behöver kommunicera med annan myndighet via en gemensam säker kommunikationstjänst såsom SGSI eller ett strukturerat informationsutbyte såsom SHS, beroende på faktiskt behov och lokal implementation.

#### Lokal eller geografisk konnektivitet

En applikation, användare eller teknisk komponent behöver nätverksåtkomst inom en byggnad, mellan platser eller till externa nät.

### 2.3 Centrala arkitekturfrågor

Utvecklingsområdet bör bland annat ta ställning till:

- Är kommunikationen synkron eller asynkron?
- Behövs svar i samma transaktion eller kan arbetet ske senare?
- Är informationsutbytet event-, meddelande-, fil- eller API-baserat?
- Vilka leveransgarantier krävs?
- Hur hanteras dubbletter?
- Krävs ordering?
- Hur stora är meddelanden eller filer?
- Hur hög är trafikvolymen?
- Hur känslig är informationen?
- Vilka parter och nätzoner kommunicerar?
- Behöver kommunikationen fungera under störningar?
- Ska information buffras vid mottagarens otillgänglighet?
- Hur versionshanteras gränssnitt och meddelandeformat?
- Hur hanteras autentisering och tjänsteidentitet?
- Behövs extern myndighetsgemensam tjänst?
- Är behovet egentligen verksamhetsmässig processorkestrering snarare än integration?
- Vilka delar av nätverkskravet är härledda från applikationens faktiska behov?

---

## 3. Förmågespecifika arkitekturprinciper

Gemensamma principer finns i `../styrning/gemensamma-arkitekturprinciper.md`.

### P-IK-01 Integrationsmönster väljs efter kommunikationsbehov

**Princip:**  
Val mellan API, messaging, event och filöverföring ska utgå från behov av synkronicitet, koppling, leveransgaranti, volym och livscykel.

**Motivering:**  
Ett enda integrationssätt passar inte alla behov.

**Konsekvens:**  
Teknisk standardisering får inte innebära att alla informationsutbyten tvingas in i samma mekanism.

### P-IK-02 Kontrakt ska vara tydliga och förvaltningsbara

**Princip:**  
Gränssnitt, meddelanden och events ska ha tydliga kontrakt och definierad livscykel.

**Motivering:**  
Integration skapar beroenden mellan självständiga lösningar som måste kunna förändras kontrollerat.

### P-IK-03 Asynkron kommunikation används när tidskoppling inte behövs

**Princip:**  
När producent och konsument inte behöver vara tillgängliga samtidigt bör asynkron kommunikation övervägas.

**Motivering:**  
Det kan förbättra robusthet, skalbarhet och lös koppling.

### P-IK-04 Events beskriver fakta, inte fjärrkommandon

**Princip:**  
Verksamhetshändelser bör uttrycka att något har inträffat och inte användas som dold synkron kommandomekanism.

**Motivering:**  
Tydlig semantik minskar koppling och förenklar flera konsumenter.

### P-IK-05 Nätverk och säkerhetskontroller ska härledas från kommunikationsbehov

**Princip:**  
Routing, brandväggsregler, zonöppningar och andra nätverkskontroller ska kunna härledas från dokumenterade kommunikationsflöden och säkerhetskrav.

**Motivering:**  
Tekniska nätverkskomponenter ska realisera behov, inte skapa egna verksamhetskrav.

### P-IK-06 Integration ska inte dela intern implementation i onödan

**Princip:**  
Gränssnitt ska exponera stabila kontrakt och inte ge andra system direkt beroende av interna databaser, filstrukturer eller implementation.

**Motivering:**  
Det minskar koppling och möjliggör teknisk förändring.

### P-IK-07 Extern kommunikation ska behandlas som tjänstekonsumtion

**Princip:**  
SGSI, SHS, externa API:er och andra externa kommunikationstjänster ska beskrivas som tjänster med kontrakt, ansvar och begränsningar.

**Motivering:**  
Extern leveransform förändrar ansvar, men inte behovet av tydliga arkitekturegenskaper.

---

## 4. Krav och styrande riktlinjer

### KR-IK-01 Dokumenterade integrationskontrakt

**Krav:**  
Produktionssatta gränssnitt mellan självständiga IT-stöd ska ha dokumenterade kontrakt för relevant data, semantik, fel och versionshantering.

**Motivering/källa:**  
Interoperabilitet och förvaltningsbarhet.

### KR-IK-02 Ingen direkt databasåtkomst som normal integration

**Krav:**  
Oberoende IT-stöd ska inte använda direkt åtkomst till varandras databaser som standardmekanism för integration.

**Motivering/källa:**  
Minskar stark koppling och otydligt informationsägarskap.

### KR-IK-03 Säker autentisering av systemkommunikation

**Krav:**  
System-till-system-kommunikation ska använda godkända mekanismer för tjänsteidentitet, autentisering och vid behov auktorisation.

**Motivering/källa:**  
Säkerhet och identitet.

### KR-IK-04 Definierat felbeteende

**Krav:**  
Integrationer ska definiera hur timeout, tekniskt fel, verksamhetsfel och mottagarens otillgänglighet hanteras när detta är relevant.

**Motivering/källa:**  
Kontinuitet och robusthet.

### KR-IK-05 Idempotens eller dubbletthantering

**Krav:**  
Asynkrona flöden där omleverans kan ske ska ha definierad strategi för idempotens eller dubbletthantering.

**Motivering/källa:**  
Korrekthet och spårbarhet.

### KR-IK-06 Spårbar korrelation

**Krav:**  
Väsentliga integrationsflöden ska kunna korreleras över komponentgränser i den utsträckning felsökning, audit eller verksamhetsbehov kräver detta.

**Motivering/källa:**  
Spårbarhet och driftbarhet.

### KR-IK-07 Versionshantering

**Krav:**  
API:er, meddelandeformat och events som används av självständiga konsumenter ska ha en definierad strategi för bakåtkompatibilitet och versionsförändring.

**Motivering/källa:**  
Förvaltningsbarhet och interoperabilitet.

### KR-IK-08 Brandväggs- och nätverksöppningar

**Krav:**  
Nätverksöppningar ska kunna kopplas till ett dokumenterat kommunikationsbehov, definierade parter och relevanta säkerhetskrav.

**Motivering/källa:**  
Säkerhet och spårbarhet.

### KR-IK-09 Externa tjänsters begränsningar

**Krav:**  
När extern kommunikationstjänst används ska beroenden, SLA/servicenivåer, informationsbegränsningar och ansvar dokumenteras.

**Motivering/källa:**  
Kontinuitet, regelefterlevnad och förvaltningsbarhet.

---

## 5. Guidelines och vägledning

### API eller messaging?

Välj API när:

- omedelbart svar behövs
- konsumenten behöver göra en direkt fråga eller begäran
- producent och konsument kan vara tillgängliga samtidigt

Välj messaging när:

- tidskoppling bör minskas
- information behöver buffras
- mottagaren kan vara tillfälligt otillgänglig
- robust leverans är viktig
- bearbetning kan ske senare

### Event eller meddelandekommando?

Använd event när producenten berättar att något har hänt och inte behöver känna till vilka som reagerar.

Använd kommando eller riktat meddelande när avsikten är att en specifik mottagare ska utföra en viss åtgärd.

### När passar IBM MQ?

IBM MQ kan vara lämpligt för robust enterprise messaging när:

- leveranssäkerhet är viktig
- asynkron kommunikation behövs
- traditionella system eller plattformar redan använder MQ
- transaktions- eller orderingsegenskaper är relevanta

Utvecklingsområdet bör konsumera en definierad Enterprise Messaging-tjänst snarare än förhålla sig direkt till queue managers och kluster.

### När passar SSIS?

SSIS kan vara lämpligt för batchorienterad dataförflyttning och transformation, särskilt i Microsoft-orienterade dataflöden.

Det bör inte automatiskt användas för realtidsintegration, API-exponering eller eventdriven kommunikation.

### När passar SHS?

Om SHS i organisationens kontext avser ett gemensamt system för strukturerat informationsutbyte bör det användas när dess informationsutbytesmodell, säkerhet och ansvar passar behovet.

Exakt lokal användning och tjänstebeskrivning måste verifieras innan detta blir styrande dokumentation.

### När passar SGSI?

SGSI kan vara relevant när myndighetskommunikation kräver den säkerhet, anslutningsmodell och robusthet som den gemensamma tjänsten erbjuder.

Utvecklingsområdet bör beskriva behovet av säker kommunikation; SGSI är därefter en möjlig eller beslutad realisering.

### Trådlöst nätverk som plattformstjänst

Trådlöst nätverk bör beskrivas som ett konsumerbart kommunikationserbjudande med exempelvis:

- täckning
- kapacitet
- användar-/enhetstyper
- autentiseringsmodell
- tillgänglighet
- säkerhetsprofil

Accesspunkter, controllers, switchar och radiokonfiguration är teknisk realisering.

### WAN och nätverkskommunikation

Utvecklingsområden bör uttrycka exempelvis:

- vilka platser eller zoner som behöver kommunicera
- latency
- kapacitet
- tillgänglighet
- säkerhetsbehov

De bör normalt inte behöva ställa krav på routermodell, protokoll eller fysisk förbindelseteknik.

### Brandvägg eller applikationskontroll?

Ett säkerhetskrav kan realiseras på flera nivåer:

- applikationsauktorisation
- API gateway
- service mesh
- nätverkspolicy
- brandvägg

Välj kontroll där den ger bäst effekt och tydligast ansvar. Brandvägg ska inte automatiskt användas för problem som bättre löses i applikations- eller identitetslagret.

### När standardlösningen inte passar

Beskriv behovet i termer av:

- parter
- synkron/asynkron kommunikation
- volym
- meddelandestorlek
- latency
- leveransgaranti
- ordering
- säkerhet
- nätzoner
- extern/intern part
- kontinuitet
- versionskrav

Därefter bedöms lämplig kommunikations- eller integrationsmekanism.

---

## 6. Plattformar och tjänsteerbjudanden

I detta steg identifieras kandidater. Detaljerade plattformsdokument skapas separat senare eller tidigare när konkret behov uppstår.

| Erbjudande | Syfte | Lämpligt för | Möjlig realisering idag | Status |
|---|---|---|---|---|
| API Management | Exponera, skydda och förvalta API:er | synkrona tjänstegränssnitt | Produkt ej beslutad i detta steg | Kandidat |
| Enterprise Messaging | Robust asynkron messaging | köer, meddelanden, systemkoppling | IBM MQ | Kandidat |
| Event Streaming | Publicera och konsumera events | händelsedrivna lösningar | Produkt ej beslutad | Kandidat |
| Managed File Transfer | Säker filöverföring | filbaserade flöden | Produkt/tjänst ej beslutad | Kandidat |
| Data Integration / ETL | Flytta och transformera data | batch- och dataflöden | MS SSIS | Kandidat |
| Secure Government Connectivity | Säker myndighetskommunikation | kommunikation med andra myndigheter | SGSI | Kandidat |
| Structured Government Exchange | Strukturerat informationsutbyte | standardiserade myndighetsflöden | SHS, om lokal användning motsvarar detta | Kandidat |
| Wireless Network Service | Trådlös nätverksåtkomst | klienter och utrustning | Befintligt trådlöst nät | Kandidat |
| WAN Connectivity | Kommunikation mellan platser | site-to-site och geografisk konnektivitet | Befintlig WAN-miljö | Kandidat |
| DNS/Name Service | Namnuppslag | applikations- och infrastrukturtjänster | Befintlig DNS-miljö | Kandidat |
| Load Balancing / Reverse Proxy | Trafikdistribution och exponering | redundanta tjänster och webbtrafik | JBCS eller annan realisering där relevant | Kandidat |

---

## 7. Standarder och teknikval

| Standard/teknikval | Status | Tillämpning |
|---|---|---|
| IBM MQ | Befintlig produkt att klassificera | Enterprise Messaging |
| Microsoft SSIS | Befintlig produkt att klassificera | Data Integration / ETL |
| SGSI | Befintlig extern/gemensam tjänst | Säker myndighetskommunikation |
| SHS | Befintlig tjänst att verifiera | Strukturerat informationsutbyte |
| Gemensam API-standard | Kandidat | REST/HTTP/API-kontrakt |
| Eventstandard | Kandidat | händelseformat och metadata |
| Meddelandekorrelationsstandard | Kandidat | tracing och spårbarhet |
| Filöverföringsstandard | Kandidat | filformat, checksumma, kvittens |
| Nätverkskommunikationsprofil | Kandidat | latency, kapacitet, zon och tillgänglighet |
| TLS-/transportstandard | Kandidat | säker transport |
| DNS-namnstandard | Kandidat | namn och tjänsteadressering |

Exakta produkter, versioner och nätverkskonfigurationer ska dokumenteras separat.

---

## 8. Relaterade artefakter och kvalitetsdimensioner

### 8.1 Relevanta kvalitetsdimensioner

Särskilt viktiga dimensioner är:

- **Säkerhet och informationsskydd** – kommunikation passerar ofta system- och organisationsgränser.
- **Tillgänglighet** – integrations- och nätverkstjänster kan vara kritiska beroenden.
- **Kontinuitet och återställningsförmåga** – buffring, retry och alternativa kommunikationsvägar kan vara viktiga.
- **Prestanda** – latency, throughput och meddelandestorlek påverkar lösningsval.
- **Skalbarhet och kapacitet** – trafik- och meddelandevolymer kan variera kraftigt.
- **Spårbarhet och verifierbarhet** – korrelation och audit är viktiga i distribuerade flöden.
- **Regelefterlevnad** – extern kommunikation och informationsutbyte kan omfattas av särskilda krav.
- **Förvaltningsbarhet och förändringsbarhet** – gränssnitt och kontrakt behöver kunna versioneras.
- **Interoperabilitet och portabilitet** – centralt för kommunikation mellan självständiga system.
- **Livscykel och hållbarhet** – integrationskontrakt lever ofta länge.
- **Kostnads- och resurseffektivitet** – särskilt för WAN, externa tjänster och högvolymskommunikation.

### 8.2 Lösningsmönster

Identifierade kandidater:

- Request/Response API
- Asynchronous Messaging
- Publish/Subscribe
- Event Notification
- Event-carried State Transfer
- Managed File Transfer
- API Facade
- Anti-Corruption Layer
- Retry with Backoff
- Idempotent Consumer
- Dead Letter Queue
- Store and Forward
- Transactional Outbox
- Gateway / Edge Proxy
- Secure Cross-Zone Communication
- Site-to-Site Connectivity

### 8.3 Plattformar

Identifierade kandidater:

- API Management
- Enterprise Messaging
- Event Streaming
- Managed File Transfer
- Data Integration / ETL
- Secure Government Connectivity
- Structured Government Exchange
- Wireless Network Service
- WAN Connectivity
- DNS/Name Service
- Load Balancing / Reverse Proxy

### 8.4 Tekniska standarder

Identifierade kandidater:

- IBM MQ-standard
- SSIS-standard
- SGSI-anslutningsstandard
- SHS-standard
- API-standard
- eventstandard
- korrelationsstandard
- filöverföringsstandard
- nätverkskommunikationsprofil
- TLS-/transportstandard
- DNS-namnstandard

### 8.5 Kandidater till referensarkitekturer

Följande kandidater stärks eller identifieras:

- **Integrationsintensivt verksamhetssystem**
- **Informationsutbyte med annan myndighet**
- **Publik e-tjänst med externa integrationer**
- **Internt handläggningsstöd med flera backendintegrationer**
- **Eventdrivet verksamhetssystem**
- **Geografiskt distribuerad verksamhetslösning**
- **Mobil operativ lösning med varierande konnektivitet**
- **Långlivad myndighetsöverskridande process**

### 8.6 Teknisk dokumentation

När konkreta integrations- och kommunikationsplattformar dokumenteras bör teknisk referens exempelvis omfatta:

- API-konfiguration
- queue/topic-konfiguration
- klientbibliotek
- certifikat och tjänsteidentitet
- nätverksanslutning
- brandväggsflöden
- routing
- DNS
- timeout/retry
- kapacitetsgränser
- monitorering
- loggning och korrelation
- versionshantering
- tekniska begränsningar

---

## Arbetsanteckningar

### Identifierade kandidater

**Lösningsmönster**
- Request/Response API
- Asynchronous Messaging
- Publish/Subscribe
- Event Notification
- Event-carried State Transfer
- Managed File Transfer
- API Facade
- Anti-Corruption Layer
- Retry with Backoff
- Idempotent Consumer
- Dead Letter Queue
- Store and Forward
- Transactional Outbox
- Gateway / Edge Proxy
- Secure Cross-Zone Communication
- Site-to-Site Connectivity

**Plattformar/tjänster**
- API Management
- Enterprise Messaging
- Event Streaming
- Managed File Transfer
- Data Integration / ETL
- Secure Government Connectivity
- Structured Government Exchange
- Wireless Network Service
- WAN Connectivity
- DNS/Name Service
- Load Balancing / Reverse Proxy

**Tekniska standarder**
- IBM MQ
- Microsoft SSIS
- SGSI
- SHS
- API-standard
- eventstandard
- korrelationsstandard
- filöverföringsstandard
- nätverkskommunikationsprofil
- TLS-/transportstandard
- DNS-namnstandard

**Referensarkitekturer**
- integrationsintensivt verksamhetssystem
- informationsutbyte med annan myndighet
- publik e-tjänst med externa integrationer
- internt handläggningsstöd med flera backendintegrationer
- eventdrivet verksamhetssystem
- geografiskt distribuerad verksamhetslösning
- mobil operativ lösning med varierande konnektivitet

**Gränsdragningsfrågor**
- hur långt ned nätverksteknik ska beskrivas i förmågedokumentet
- om WAN, LAN och trådlöst ska vara separata tjänsteerbjudanden eller profiler under gemensam Connectivity-tjänst
- hur SGSI och SHS bäst klassificeras utifrån faktisk lokal användning
- hur JBCS ska placeras mellan kommunikation och runtime
- var gränsen går mellan integrationsorkestrering och verksamhetsprocess
