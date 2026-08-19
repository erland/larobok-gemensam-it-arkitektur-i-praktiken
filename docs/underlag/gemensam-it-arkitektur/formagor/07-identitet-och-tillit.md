# Förmåga: Identitet och tillit

> **Status:** Utkast  
> **Ansvarig:** Gemensam IT-arkitektur / stödjande IT-område  
> **Senast reviderad:** 2026-08-18

## 1. Syfte, omfattning och relationer

### 1.1 Syfte

Förmågan ska ge utvecklingsområden stöd för att identifiera människor, system, applikationer och tekniska komponenter samt etablera och verifiera tillit mellan dem.

Syftet är att erbjuda gemensamma mekanismer för autentisering, auktorisation, federation, tjänsteidentiteter, certifikat och annan tillitsinfrastruktur så att varje IT-stöd inte behöver bygga egna lösningar.

Förmågan ska samtidigt hållas tydligt åtskild från säkerhet som tvärgående kvalitetsdimension. Identitet och tillit tillhandahåller centrala säkerhetsmekanismer, men omfattar inte all informationssäkerhet.

### 1.2 Omfattning

Förmågan omfattar bland annat:

- digitala identiteter för människor
- digitala identiteter för tjänster och system
- autentisering
- flerfaktorsautentisering
- single sign-on
- federation
- identitetsintyg och claims
- auktorisation och behörighetsbeslut
- roller, attribut och policyunderlag
- tjänsteidentiteter
- maskin-till-maskin-autentisering
- certifikat
- PKI
- nyckel- och certifikatslivscykel
- secrets management
- privileged access
- delegering
- teknisk trust mellan miljöer och organisationer
- livscykel för konton och identiteter
- identitetskoppling mot externa aktörer eller tjänster

### 1.3 Utanför förmågan

Följande hör primärt hemma i andra förmågor eller perspektiv:

- generell säkerhetsarkitektur, hotmodellering och säkerhetskontroller – **Säkerhet och informationsskydd** som kvalitetsdimension
- nätverkssegmentering, brandväggar och transportskydd – **Integration och kommunikation**
- applikationsspecifika verksamhetsregler om vad en användare får göra – **Regler och beslut** när de är verksamhetsmässiga
- användargränssnitt för inloggning och kontoåterställning – **Interaktion, presentation och kanaler**
- drift, loggning och övervakning av identitetstjänster – **Driftbarhet och motståndskraft**

### 1.4 Relation till andra förmågor

**Integration och kommunikation** använder tjänsteidentiteter, certifikat och autentiseringsmekanismer för säkra system-till-system-flöden.

**Interaktion, presentation och kanaler** använder gemensamma identitetstjänster för inloggning, sessioner och användarupplevelse.

**Regler och beslut** kan använda roller och attribut som indata till verksamhetsbeslut men bör inte duplicera den tekniska identitetsmekanismen.

**Applikationsexekvering och runtime** behöver tjänsteidentiteter, certifikat och secrets för workloads.

**Programvaruutveckling och leverans** behöver identitet, secrets och privileged access för pipelines och utvecklingsverktyg.

---

## 2. Behov och användningsområden

### 2.1 Typiska behov

Ett utvecklingsområde kan behöva stöd när ett IT-stöd ska:

- autentisera interna användare
- autentisera externa användare
- använda single sign-on
- federera identitet med annan organisation
- autentisera tjänst-till-tjänst
- använda certifikat för teknisk tillit
- hantera API-klientidentiteter
- styra åtkomst utifrån roller eller attribut
- skydda tekniska secrets
- hantera privilegierade administrativa konton
- delegera åtkomst
- koppla identitet till loggning och audit
- hantera livscykel för användare, konton och tekniska identiteter

### 2.2 Typiska användningsfall

#### Intern användarinloggning

En intern användare autentiserar sig med myndighetens gemensamma identitetslösning och får tillgång till ett verksamhetsstöd.

#### Extern federation

En extern part autentiserar sig hos sin identitetsleverantör och identiteten federeras till myndighetens tjänst.

#### Tjänsteidentitet

En backendtjänst anropar en annan tjänst med en egen teknisk identitet utan att använda en personlig användares credentials.

#### Certifikatbaserad kommunikation

Två system etablerar teknisk tillit med certifikat och gemensam PKI.

#### Privileged access

Administrativ åtkomst till känslig plattform eller systemkomponent kräver särskild identitet, stark autentisering och kontrollerad livscykel.

### 2.3 Centrala arkitekturfrågor

Utvecklingsområdet bör bland annat ta ställning till:

- Vilka typer av identiteter finns?
- Är användarna interna, externa eller båda?
- Vilken autentiseringsstyrka behövs?
- Behövs federation?
- Vilka attribut behövs för åtkomstbeslut?
- Ska auktorisation ske centralt, lokalt eller i kombination?
- Behövs tjänsteidentitet?
- Hur ska certifikat eller secrets hanteras?
- Hur kopplas identitet till audit och spårbarhet?
- Hur hanteras identitetens livscykel?
- Behövs delegering eller impersonation?
- Hur minimeras delning av credentials?
- Hur hanteras privilegierad åtkomst?
- Vilka externa tillitsrelationer krävs?

---

## 3. Förmågespecifika arkitekturprinciper

Gemensamma principer finns i `../styrning/gemensamma-arkitekturprinciper.md`.

### P-IT-01 Gemensam identitet före lokal identitet

**Princip:**  
Gemensamma identitetstjänster ska användas när de uppfyller behovet.

**Motivering:**  
Lokala identitetslager skapar dubbla livscykler, sämre säkerhet och högre förvaltningskostnad.

### P-IT-02 Människor och tjänster ska ha separata identiteter

**Princip:**  
Tekniska tjänster ska använda egna tjänsteidentiteter och inte personliga användarkonton.

**Motivering:**  
Det ger tydligare ansvar, spårbarhet och livscykel.

### P-IT-03 Autentisering och auktorisation ska hållas isär

**Princip:**  
Att fastställa vem eller vad en aktör är ska skiljas från beslutet om vad aktören får göra.

**Motivering:**  
Det möjliggör tydligare ansvar och återanvändning av identitetstjänster.

### P-IT-04 Minsta privilegium

**Princip:**  
Identiteter ska endast få den åtkomst som krävs för sitt uppdrag eller sin tekniska funktion.

**Motivering:**  
Minskar konsekvensen av fel eller kompromettering.

### P-IT-05 Credentials ska inte spridas eller byggas in

**Princip:**  
Lösenord, nycklar och andra secrets ska hanteras i godkända mekanismer och inte byggas in i kod, images eller konfigurationsfiler.

**Motivering:**  
Minskar risk för läckage och förbättrar rotation.

### P-IT-06 Tillit ska vara explicit och tidsbegränsad där det är möjligt

**Princip:**  
Tillit mellan system, organisationer och tekniska miljöer ska vara dokumenterad och bygga på kontrollerade identiteter, certifikat eller federation.

**Motivering:**  
Implicit tillit gör arkitekturen svår att förstå och säkra.

### P-IT-07 Identitetslivscykel ska automatiseras där det är möjligt

**Princip:**  
Skapande, förändring och avveckling av identiteter och behörigheter bör kopplas till auktoritativa källor och automatiserade processer.

**Motivering:**  
Manuell livscykel skapar kvarvarande och felaktiga behörigheter.

---

## 4. Krav och styrande riktlinjer

### KR-IT-01 Gemensam autentisering

**Krav:**  
Nya IT-stöd ska använda myndighetens godkända gemensamma autentiseringslösningar när dessa stödjer målgruppen och säkerhetsbehovet.

**Motivering/källa:**  
Säkerhet, förvaltningsbarhet och användarupplevelse.

### KR-IT-02 Tjänsteidentiteter

**Krav:**  
System-till-system-kommunikation ska använda dedikerade tjänsteidentiteter eller motsvarande godkänd mekanism.

**Motivering/källa:**  
Spårbarhet, säkerhet och livscykel.

### KR-IT-03 Secrets management

**Krav:**  
Secrets ska lagras och distribueras med godkänd secrets-hantering och får inte lagras i klartext i källkod eller artefakter.

**Motivering/källa:**  
Säkerhet och informationsskydd.

### KR-IT-04 Certifikatslivscykel

**Krav:**  
Certifikat som används för produktionstjänster ska ha definierad ägare, förnyelseprocess och avvecklingsprocess.

**Motivering/källa:**  
Tillgänglighet och säkerhet.

### KR-IT-05 Behörighetsmodell

**Krav:**  
IT-stöd ska dokumentera sin behörighetsmodell och vilka identitetsattribut eller roller som används för åtkomstbeslut.

**Motivering/källa:**  
Säkerhet och verifierbarhet.

### KR-IT-06 Privilegierad åtkomst

**Krav:**  
Privilegierad administrativ åtkomst ska använda särskilt kontrollerade identiteter och stark autentisering enligt myndighetens säkerhetskrav.

**Motivering/källa:**  
Säkerhet och informationsskydd.

### KR-IT-07 Spårbar identitet

**Krav:**  
När en åtgärd behöver kunna granskas i efterhand ska relevanta loggar kunna koppla åtgärden till användar- eller tjänsteidentitet.

**Motivering/källa:**  
Spårbarhet och verifierbarhet.

### KR-IT-08 Ingen delning av personliga konton

**Krav:**  
Personliga användarkonton ska inte delas mellan flera personer eller användas som tekniska tjänstekonton.

**Motivering/källa:**  
Spårbarhet och ansvar.

---

## 5. Guidelines och vägledning

### Autentisering eller auktorisation?

Autentisering svarar på:

> Vem eller vad är detta?

Auktorisation svarar på:

> Vad får denna identitet göra?

Håll dessa frågor separata i arkitekturen även om samma plattform kan stödja båda.

### Rollbaserad eller attributbaserad auktorisation?

Rollbaserad åtkomst passar när behörigheter kan uttryckas stabilt utifrån roller.

Attributbaserad åtkomst kan vara lämplig när åtkomst beror på flera egenskaper, exempelvis organisatorisk tillhörighet, ärendekontext eller informationsklass.

Undvik komplexitet utan behov.

### När behövs federation?

Federation är lämplig när användare eller system tillhör annan organisatorisk identitetsdomän men ska kunna autentiseras utan lokala duplicerade konton.

Bedöm:

- trustmodell
- identitetsattribut
- livscykel
- incidentansvar
- autentiseringsstyrka

### När ska certifikat användas?

Certifikat är lämpliga för teknisk tillit där:

- stark maskinidentitet krävs
- TLS med ömsesidig autentisering används
- integration med externa parter kräver PKI-baserad trust

Certifikat är inte ersättning för all auktorisation.

### Tjänsteidentitet eller användardelegering?

Använd tjänsteidentitet när en tjänst agerar i eget ansvar.

Använd delegerad användaridentitet när den bakomliggande tjänsten behöver veta och kontrollera vilken användare som initierade åtgärden.

### Hur bör secrets hanteras?

Secrets bör:

- inte hårdkodas
- roteras
- ges minsta möjliga åtkomst
- ha tydlig ägare
- kunna återkallas
- exponeras endast till de workloads som behöver dem

### När passar centralt policybeslut?

Central policy engine kan vara lämplig när flera tjänster behöver konsekvent teknisk auktorisation.

Verksamhetsregler som avgör sakfrågor bör däremot ligga under **Regler och beslut**.

### Externa identiteter

Vid externa användare eller organisationer bör utvecklingsområdet först uttrycka:

- målgrupp
- identifieringsnivå
- autentiseringsstyrka
- attributbehov
- ansvar vid fel

Därefter väljs lämplig federation eller extern identitetstjänst.

### När standardlösningen inte passar

Beskriv behovet i termer av:

- identitetstyp
- intern/extern aktör
- autentiseringsstyrka
- federation
- attribut
- auktorisationsmodell
- tjänsteidentitet
- certifikat
- secrets
- livscykel
- audit

Därefter bedöms om gemensam identitets- och tillitsplattform kan möta behovet.

---

## 6. Plattformar och tjänsteerbjudanden

I detta steg identifieras kandidater. Detaljerade plattformsdokument skapas separat senare eller tidigare vid konkret behov.

| Erbjudande | Syfte | Lämpligt för | Status |
|---|---|---|---|
| Workforce Identity | Identitet och autentisering för interna användare | interna verksamhetsstöd | Kandidat |
| External Identity / Federation | Identitet för externa användare och organisationer | e-tjänster och samverkanslösningar | Kandidat |
| Service Identity | Identitet för system och workloads | system-till-system-kommunikation | Kandidat |
| Authorization Service | Gemensamma auktorisationsbeslut | delade tekniska accesspolicyer | Kandidat |
| PKI / Certificate Service | Certifikat och teknisk trust | TLS, mTLS och externa relationer | Kandidat |
| Secrets Management | Säker lagring och distribution av secrets | applikationer, pipelines och plattformar | Kandidat |
| Privileged Access Management | Kontrollerad administrativ åtkomst | känsliga plattformar och system | Kandidat |
| Identity Lifecycle Service | Provisionering och avveckling av identiteter | konton och behörigheter | Kandidat |

---

## 7. Standarder och teknikval

| Standard/teknikval | Status | Tillämpning |
|---|---|---|
| OAuth 2.x | Kandidat | delegerad åtkomst och API-auktorisation |
| OpenID Connect | Kandidat | autentisering och federation |
| SAML 2.0 | Kandidat/befintligt beroende att verifiera | federation mot äldre eller externa miljöer |
| X.509 | Kandidat | certifikat och teknisk trust |
| mTLS-standard | Kandidat | ömsesidig tjänsteautentisering |
| JWT-standard | Kandidat | tokenformat där lämpligt |
| Gemensam claims-/attributstandard | Kandidat | identitetsinformation mellan tjänster |
| Service identity-standard | Kandidat | workload- och tjänsteidentiteter |
| Secrets-standard | Kandidat | lagring, rotation och åtkomst |
| Privileged access-standard | Kandidat | administrativ åtkomst |

Exakta produkter och versioner dokumenteras separat.

---

## 8. Relaterade artefakter och kvalitetsdimensioner

### 8.1 Relevanta kvalitetsdimensioner

Särskilt viktiga dimensioner är:

- **Säkerhet och informationsskydd** – identitet och tillit är centrala säkerhetsmekanismer.
- **Tillgänglighet** – gemensamma identitetstjänster kan vara kritiska beroenden.
- **Kontinuitet och återställningsförmåga** – autentisering och certifikattjänster måste fungera även vid störningar.
- **Prestanda** – tokenvalidering och auktorisationsbeslut kan ligga i varje requestflöde.
- **Spårbarhet och verifierbarhet** – identitet är grund för audit.
- **Regelefterlevnad** – identitets- och behörighetsdata kan omfattas av särskilda krav.
- **Förvaltningsbarhet och förändringsbarhet** – identitetslivscykel och policyer förändras över tid.
- **Interoperabilitet och portabilitet** – standardiserade federations- och tokenprotokoll är viktiga.
- **Livscykel och hållbarhet** – PKI, federation och identitetsplattformar är långlivade beroenden.

### 8.2 Lösningsmönster

Identifierade kandidater:

- Single Sign-On
- Federated Identity
- Service Identity
- Token-based Authentication
- Delegated Authorization
- Centralized Authorization
- Attribute-Based Access Control
- Role-Based Access Control
- Mutual TLS
- Secret Injection
- Short-lived Credentials
- Privileged Access
- Identity Propagation

### 8.3 Plattformar

Identifierade kandidater:

- Workforce Identity
- External Identity / Federation
- Service Identity
- Authorization Service
- PKI / Certificate Service
- Secrets Management
- Privileged Access Management
- Identity Lifecycle Service

### 8.4 Tekniska standarder

Identifierade kandidater:

- OAuth 2.x
- OpenID Connect
- SAML 2.0
- X.509
- mTLS
- JWT
- claims-/attributstandard
- service identity-standard
- secrets-standard
- privileged access-standard

### 8.5 Kandidater till referensarkitekturer

Följande kandidater stärks eller identifieras:

- **Internt handläggningsstöd**
- **Publik e-tjänst**
- **Informationsutbyte med annan myndighet**
- **Extern samverkanslösning med federation**
- **Containerbaserad mikrotjänstelösning med tjänsteidentiteter**
- **Privilegierad administrationsmiljö**
- **AI-baserat verksamhetsstöd med kontrollerad åtkomst till data och verktyg**

### 8.6 Teknisk dokumentation

När konkreta identitets- och tillitsplattformar dokumenteras bör teknisk referens exempelvis omfatta:

- klientregistrering
- federation
- tokenformat
- claims
- certifikat
- nyckelrotation
- secrets
- tjänsteidentiteter
- autentiseringsflöden
- auktorisationspolicyer
- audit och loggning
- HA och failover
- tekniska begränsningar

---

## Arbetsanteckningar

### Identifierade kandidater

**Lösningsmönster**
- Single Sign-On
- Federated Identity
- Service Identity
- Token-based Authentication
- Delegated Authorization
- Centralized Authorization
- Attribute-Based Access Control
- Role-Based Access Control
- Mutual TLS
- Secret Injection
- Short-lived Credentials
- Privileged Access
- Identity Propagation

**Plattformar/tjänster**
- Workforce Identity
- External Identity / Federation
- Service Identity
- Authorization Service
- PKI / Certificate Service
- Secrets Management
- Privileged Access Management
- Identity Lifecycle Service

**Tekniska standarder**
- OAuth 2.x
- OpenID Connect
- SAML 2.0
- X.509
- mTLS
- JWT
- claims-/attributstandard
- service identity-standard
- secrets-standard
- privileged access-standard

**Referensarkitekturer**
- internt handläggningsstöd
- publik e-tjänst
- informationsutbyte med annan myndighet
- extern samverkanslösning med federation
- containerbaserad mikrotjänstelösning med tjänsteidentiteter
- privilegierad administrationsmiljö
- AI-baserat verksamhetsstöd med kontrollerad åtkomst

**Gränsdragningsfrågor**
- hur centralt auktorisationsbeslut ska beskrivas i förhållande till verksamhetsregler
- var gränsen går mellan identity lifecycle och HR-/organisationsdata
- hur extern e-legitimation och federation ska klassificeras när faktiska tjänster identifieras
- hur service identity relaterar till OpenShift och andra runtimeplattformar
- hur PKI- och certifikatansvar ska delas mellan denna förmåga och Integration/kommunikation
