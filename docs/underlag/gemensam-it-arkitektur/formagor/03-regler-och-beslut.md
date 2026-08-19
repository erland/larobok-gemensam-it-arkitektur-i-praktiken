# Förmåga: Regler och beslut

> **Status:** Utkast  
> **Ansvarig:** Gemensam IT-arkitektur / stödjande IT-område  
> **Senast reviderad:** 2026-08-18

## 1. Syfte, omfattning och relationer

### 1.1 Syfte

Förmågan ska ge utvecklingsområden stöd för att uttrycka, exekvera, förvalta och följa upp verksamhetsregler och beslut som behöver vara tydliga, förändringsbara, spårbara eller återanvändbara oberoende av en enskild applikations implementation.

Syftet är att skilja sådana regler och beslut från vanlig programlogik, processlogik och tekniska policyer så att rätt typ av logik hanteras på rätt arkitekturnivå.

### 1.2 Omfattning

Förmågan omfattar bland annat:

- verksamhetsregler
- beslutstabeller
- beslutsträd
- deklarativa regelverk
- beslutsmodeller
- beräkningar med tydlig verksamhetsbetydelse
- regelmotorer
- beslutstjänster
- regelversionering
- regelspårbarhet
- beslutsförklaring
- simulering och test av regelverk
- gemensamma eller återanvändbara beslutsregler
- policyer som styr verksamhetsbeslut

### 1.3 Utanför förmågan

Följande hör primärt hemma i andra förmågor eller lager:

- vanlig domänlogik som endast är relevant inom en applikations kodbas
- ordning och koordinering av aktiviteter – **Process, workflow och ärendehantering**
- tekniska access- och säkerhetspolicyer – främst **Identitet och tillit** samt säkerhet som kvalitetsdimension
- tekniska routing- och integrationsregler – **Integration och kommunikation**
- statistiska modeller, maskininlärning och generativ AI – **Analys, sökning och AI**
- presentationslogik – **Interaktion, presentation och kanaler**

Förmågan ska inte bli en generell behållare för all logik bara för att logiken kan uttryckas som ett villkor.

### 1.4 Relation till andra förmågor

**Process, workflow och ärendehantering** kan anropa en beslutstjänst eller regelmotor för att fatta ett beslut, men själva flödet och beslutet bör hållas isär när de har olika livscykel.

**Data- och informationshantering** tillhandahåller de data som regler och beslut använder och hanterar även historik eller beslutsunderlag som behöver bevaras.

**Integration och kommunikation** används när beslutstjänster exponeras eller anropas av andra system.

**Analys, sökning och AI** används när beslutet baseras på statistisk inferens, ML eller generativ AI snarare än på explicita deklarativa regler.

**Identitet och tillit** kan tillhandahålla attribut och behörighetsinformation som påverkar beslut, men accesskontroll ska inte sammanblandas med verksamhetsbeslut.

---

## 2. Behov och användningsområden

### 2.1 Typiska behov

Ett utvecklingsområde kan behöva stöd när:

- samma verksamhetsregel används i flera IT-stöd
- regelverket förändras oftare än övrig applikationskod
- verksamheten behöver kunna granska eller förstå regeln explicit
- regler behöver kunna testas och simuleras separat
- beslut måste kunna förklaras i efterhand
- regelversionen behöver kunna kopplas till ett visst beslut
- stora kombinationer av villkor gör vanlig kod svår att förvalta
- beslut behöver exekveras som en gemensam tjänst
- flera processer behöver använda samma beslutslogik
- en extern eller intern policy ska omsättas konsekvent i flera lösningar

### 2.2 Typiska användningsfall

#### Behörighetsnära verksamhetsbeslut

Ett system behöver avgöra om en användare eller aktör får genomföra en verksamhetsåtgärd utifrån flera verksamhetsvillkor. Själva autentiseringen och den tekniska auktorisationen ligger fortfarande i Identitet och tillit.

#### Klassificering eller kategorisering

Ett objekt eller ärende behöver klassificeras i en kategori utifrån deklarativa regler.

#### Beräkning av avgift eller nivå

Ett värde beräknas utifrån regler som förändras över tid och behöver vara spårbara till beslutad version.

#### Routing av ärende

Ett workflow behöver besluta vilken väg ett ärende ska ta utifrån verksamhetsregler som används även i andra sammanhang.

#### Automatisk kontroll

En regelmotor kontrollerar om data uppfyller ett antal explicita kriterier och returnerar resultat samt eventuella avvikelser.

### 2.3 Centrala arkitekturfrågor

Utvecklingsområdet bör bland annat ta ställning till:

- Är regeln så viktig eller förändringsbar att den bör hanteras explicit?
- Behöver regeln kunna förstås av andra än utvecklare?
- Behöver flera system använda samma regel?
- Krävs spårbarhet till vilken regelversion som användes?
- Är beslutet deterministiskt eller bygger det på statistisk/AI-baserad inferens?
- Behöver regler kunna simuleras eller testas på historiska data?
- Är regeln egentligen ett processvillkor eller en teknisk policy?
- Behöver beslutet kunna förklaras för användare eller granskare?
- Hur hanteras beroenden till data och externa tjänster?
- Vilken förändringstakt och releaseprocess ska gälla för regelverket?

---

## 3. Förmågespecifika arkitekturprinciper

Gemensamma principer finns i `../styrning/gemensamma-arkitekturprinciper.md`.

### P-RB-01 Externalisera endast regler som vinner på det

**Princip:**  
Verksamhetsregler bör externaliseras från applikationskod när det finns ett tydligt behov av återanvändning, separat förändring, förståelig representation, spårbarhet eller särskild förvaltning.

**Motivering:**  
En regelmotor tillför värde först när förvaltningen blir bättre än motsvarande kodlösning.

**Konsekvens:**  
Enkla och lokala villkor ska inte flyttas till en gemensam regelplattform utan tydlig nytta.

### P-RB-02 Beslutslogik och processflöde ska hållas isär när deras livscykler skiljer sig

**Princip:**  
Regler som har egen verksamhetsbetydelse eller återanvänds i flera processer bör hanteras separat från processdefinitionen.

**Motivering:**  
Det minskar koppling och gör det möjligt att förändra beslut utan att förändra hela processflödet.

### P-RB-03 Beslut ska vara spårbara när behovet kräver det

**Princip:**  
När verksamhet, tillsyn eller rättssäkerhet kräver det ska ett beslut kunna kopplas till relevant regelversion och indata.

**Motivering:**  
Det gör beslut möjliga att verifiera och förklara i efterhand.

**Konsekvens:**  
Regel- och beslutstjänster behöver stöd för versionering och relevant auditinformation.

### P-RB-04 Deterministiska regler och probabilistiska modeller ska hållas konceptuellt isär

**Princip:**  
Explicita regelbaserade beslut ska skiljas från ML- eller AI-baserade bedömningar.

**Motivering:**  
De har olika egenskaper kring förklarbarhet, testning, ändring, risk och styrning.

**Konsekvens:**  
En AI-modell kan ge input till ett beslut, men ska inte otydligt behandlas som om den vore samma sak som ett deklarativt regelverk.

### P-RB-05 Regler ska ha tydligt ägarskap

**Princip:**  
Verksamhetsregler som hanteras explicit ska ha identifierat sakägarskap och tekniskt förvaltningsansvar.

**Motivering:**  
Oklart regelägarskap leder till svårigheter vid förändring och konflikt mellan system.

### P-RB-06 Regler ska testas som verksamhetsartefakter

**Princip:**  
Regler med egen livscykel ska kunna testas och verifieras separat från den applikation som konsumerar dem.

**Motivering:**  
Det minskar risken att förändringar i regelverk endast upptäcks genom systemtest av hela lösningen.

---

## 4. Krav och styrande riktlinjer

### KR-RB-01 Regelägarskap

**Krav:**  
Explicit externaliserade verksamhetsregler ska ha dokumenterat verksamhetsmässigt ägarskap och tekniskt förvaltningsansvar.

**Motivering/källa:**  
Förvaltningsbarhet, förändringsbarhet och ansvar.

**Tillämpningsområde:**  
Gemensamma regelverk, beslutstjänster och regler som används av flera lösningar.

### KR-RB-02 Versionshantering

**Krav:**  
Regler och beslutsmodeller som kan påverka ett verksamhetsutfall ska versionshanteras så att det går att avgöra vilken version som gällde vid ett visst beslut när behovet kräver det.

**Motivering/källa:**  
Spårbarhet och verifierbarhet.

### KR-RB-03 Testbarhet

**Krav:**  
Regelverk som externaliseras ska kunna verifieras med automatiserade eller strukturerade testfall på en nivå som är proportionerlig mot deras betydelse.

**Motivering/källa:**  
Korrekthet och förändringsbarhet.

### KR-RB-04 Ingen dold kritisk logik i klienten

**Krav:**  
Verksamhetskritiska beslut får inte enbart implementeras i användargränssnitt eller annan klientkod.

**Motivering/källa:**  
Säkerhet, korrekthet och återanvändbarhet.

### KR-RB-05 Tydliga beslutsgränssnitt

**Krav:**  
Gemensamma beslutstjänster ska ha tydligt definierade kontrakt för indata, utdata, fel och versionshantering.

**Motivering/källa:**  
Interoperabilitet och förvaltningsbarhet.

### KR-RB-06 Förklarbarhet när verksamhetsbehov finns

**Krav:**  
När ett beslut behöver kunna motiveras eller granskas ska lösningen bevara tillräcklig information för att förklara utfallet.

**Motivering/källa:**  
Spårbarhet, verifierbarhet och regelefterlevnad.

### KR-RB-07 Regler ska inte dupliceras utan motivering

**Krav:**  
När samma verksamhetsregel behöver tillämpas i flera IT-stöd ska utvecklingsområdet bedöma om regeln bör återanvändas genom gemensam regel-/beslutstjänst eller annat gemensamt mönster.

**Motivering/källa:**  
Konsistens och förvaltningsbarhet.

---

## 5. Guidelines och vägledning

### När bör en regelmotor användas?

Överväg en regelmotor när flera av följande gäller:

- regelverket är omfattande
- regler förändras relativt ofta
- regler behöver kunna förstås eller granskas explicit
- flera system använder samma regler
- beslutstabeller eller deklarativa modeller passar bättre än programkod
- historik och regelversioner behöver kunna följas
- verksamheten behöver simulera förändringar i regelverket

Undvik regelmotor när logiken är liten, lokal och starkt kopplad till en enskild domänfunktion.

### Regelmotor eller vanlig kod?

Vanlig kod är ofta bäst när:

- logiken endast används i en komponent
- förändringstakten följer övrig kod
- reglerna är nära kopplade till domänmodellens implementation
- det inte finns behov av separat förvaltning eller förståelse

Regelmotor är mer motiverad när regeln själv är en förvaltningsvärd artefakt.

### Regel eller processvillkor?

Ett lokalt villkor som endast avgör nästa steg i ett processflöde kan ligga i processen.

En regel som har egen verksamhetsbetydelse, återanvänds eller förändras oberoende bör hellre hanteras inom Regler och beslut.

### Regel eller AI?

Använd explicita regler när beslutet kan uttryckas deterministiskt och verksamheten behöver förutsebart beteende.

Överväg AI/ML när uppgiften kräver exempelvis klassificering, mönsterigenkänning eller probabilistisk bedömning som inte rimligen kan uttryckas som fasta regler.

Kombinationer är möjliga, exempelvis:

```text
AI-modell → bedömningssignal
              ↓
         regelbaserat beslut
```

### Hur bör regler versioneras?

Minst följande bör övervägas:

- unik regel-/modellversion
- giltighetsperiod
- vem som godkänt förändringen
- testresultat
- möjlighet att koppla ett historiskt beslut till rätt version

### Hur undviker man en central regelmonolit?

Gemensam återanvändning betyder inte att alla regler ska ligga i en enda global regelmotor.

Gruppera regler efter verksamhetsansvar och förändringsbehov. En gemensam plattform kan stödja flera separata regelområden.

### När standardlösningen inte passar

Beskriv behovet i termer av:

- antal regler
- förändringstakt
- återanvändning
- krav på spårbarhet
- prestanda
- beslut per tidsenhet
- förklarbarhet
- testbarhet
- koppling till processer eller AI

Bedöm därefter om vanlig kod, beslutstjänst, regelmotor eller annan realisering är mest ändamålsenlig.

---

## 6. Plattformar och tjänsteerbjudanden

I detta steg identifieras kandidater. Detaljerade dokument skapas separat vid konsolidering eller när ett konkret behov uppstår.

| Erbjudande | Syfte | Lämpligt för | Status |
|---|---|---|---|
| Business Rules Platform | Exekvera och förvalta deklarativa verksamhetsregler | regelverk med egen livscykel | Kandidat |
| Decision Service | Exponera återanvändbara beslut via tjänstegränssnitt | beslut som används av flera system/processer | Kandidat |
| Decision Table Service | Förvalta och exekvera beslutstabeller | tabellbaserade regelverk | Kandidat |
| Rule Simulation/Test Support | Simulera och verifiera regeländringar | regelverk med hög förändringstakt eller höga korrekthetskrav | Kandidat |

Det bör senare avgöras om dessa är separata tjänster eller profiler på en gemensam plattform.

---

## 7. Standarder och teknikval

| Standard/teknikval | Status | Tillämpning |
|---|---|---|
| DMN | Kandidat | Deklarativ modellering av beslut |
| Standard för besluts-API | Kandidat | Gemensamma kontrakt för beslutstjänster |
| Regelversionsstandard | Kandidat | Spårbarhet och historik |
| Regeltestformat | Kandidat | Strukturerad verifiering av regler |
| Beslutsmetadata | Kandidat | Version, källa, giltighet och eventuell förklaring |

BPMN hör primärt hemma i Process, workflow och ärendehantering men kan länka till DMN-baserade beslut.

---

## 8. Relaterade artefakter och kvalitetsdimensioner

### 8.1 Relevanta kvalitetsdimensioner

Särskilt viktiga dimensioner är:

- **Säkerhet och informationsskydd** – beslut kan baseras på skyddsvärda data.
- **Prestanda** – vissa beslut kan exekveras i mycket hög volym.
- **Spårbarhet och verifierbarhet** – centralt när beslut behöver kunna granskas.
- **Regelefterlevnad** – regler kan vara härledda från lag, föreskrift eller intern styrning.
- **Förvaltningsbarhet och förändringsbarhet** – själva kärnan i att externalisera regler.
- **Interoperabilitet och portabilitet** – viktigt om beslutstjänster konsumeras av flera lösningar.
- **Livscykel och hållbarhet** – regelplattformen kan bli ett centralt beroende.

### 8.2 Lösningsmönster

Identifierade kandidater:

- Externaliserade verksamhetsregler
- Decision Service
- Decision Table
- Rules as a Service
- AI-assisted Decision with Rule Guardrails
- Policy/Rule Separation
- Versioned Decision Logic

### 8.3 Plattformar

Identifierade kandidater:

- Business Rules Platform
- Decision Service
- Decision Table Service
- Rule Simulation/Test Support

### 8.4 Tekniska standarder

Identifierade kandidater:

- DMN
- besluts-API-standard
- regelversionsstandard
- regeltestformat
- beslutsmetadata

### 8.5 Kandidater till referensarkitekturer

Följande kandidater stärks eller identifieras:

- **Internt handläggningsstöd** – process och beslut samverkar ofta.
- **Publik e-tjänst med automatiserade beslut** – kombinerar interaktion, regler, data, identitet och process.
- **AI-baserat verksamhetsstöd med regelbaserade guardrails** – kandidat för senare steg.
- **Regelintensivt verksamhetssystem** – kandidat där stora explicita regelverk är centrala.

### 8.6 Teknisk dokumentation

När konkret regel-/beslutsplattform väljs bör teknisk dokumentation exempelvis omfatta:

- modell- och regeldeployment
- versionering
- API:er
- test- och simulationsstöd
- autentisering och auktorisation
- prestanda och skalning
- audit och loggning
- backup/restore
- tekniska begränsningar

---

## Arbetsanteckningar

### Identifierade kandidater

**Lösningsmönster**
- Externaliserade verksamhetsregler
- Decision Service
- Decision Table
- Rules as a Service
- AI-assisted Decision with Rule Guardrails
- Policy/Rule Separation
- Versioned Decision Logic

**Plattformar/tjänster**
- Business Rules Platform
- Decision Service
- Decision Table Service
- Rule Simulation/Test Support

**Tekniska standarder**
- DMN
- besluts-API-standard
- regelversionsstandard
- regeltestformat
- beslutsmetadata

**Referensarkitekturer**
- internt handläggningsstöd
- publik e-tjänst med automatiserade beslut
- AI-baserat verksamhetsstöd med regelbaserade guardrails
- regelintensivt verksamhetssystem

**Gränsdragningsfrågor**
- var gränsen mellan vanlig domänlogik och externaliserade verksamhetsregler går
- hur tekniska policy engines ska klassificeras i förhållande till verksamhetsregler
- hur regelbaserade och AI-baserade beslut kombineras utan otydligt ansvar
- när beslut bör centraliseras och när de bör ligga nära respektive domän
