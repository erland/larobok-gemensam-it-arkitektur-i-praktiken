# Förmåga: Process, workflow och ärendehantering

> **Status:** Utkast  
> **Ansvarig:** Gemensam IT-arkitektur / stödjande IT-område  
> **Senast reviderad:** 2026-08-18

## 1. Syfte, omfattning och relationer

### 1.1 Syfte

Förmågan ska ge utvecklingsområden stöd för att utforma, automatisera och följa upp verksamhetsprocesser, arbetsflöden, ärenden och arbetsuppgifter som sträcker sig över tid eller involverar flera aktörer, system eller steg.

Syftet är att gemensamma behov kring processorkestrering, ärendehantering och arbetsköer ska kunna lösas på ett enhetligt och förvaltningsbart sätt utan att varje IT-stöd behöver bygga motsvarande mekanismer från grunden.

### 1.2 Omfattning

Förmågan omfattar bland annat:

- verksamhetsprocesser och arbetsflöden
- processorkestrering
- långlivade processinstanser
- ärendehantering och case management
- arbetsuppgifter och human tasks
- arbetsköer och fördelning av arbete
- status- och livscykelhantering för ärenden
- väntelägen, timers och deadlines
- eskalering och påminnelser
- processhistorik och spårbarhet
- koordinering av flera tjänster eller aktiviteter
- kompensation och återupptagning i långlivade flöden
- stöd för manuella och automatiserade processteg

### 1.3 Utanför förmågan

Följande hör primärt hemma i andra förmågor:

- verksamhetsregler och beslut som kan uttryckas oberoende av processflödet – **Regler och beslut**
- tekniska API:er, messaging och events – **Integration och kommunikation**
- presentation av arbetsuppgifter och ärenden för användaren – **Interaktion, presentation och kanaler**
- persistens av verksamhetsdata och dokument – **Data- och informationshantering**
- identitet, autentisering och auktorisation – **Identitet och tillit**
- exekveringsmiljöer för processmotorer och applikationer – **Applikationsexekvering och runtime**
- vanlig domänlogik som naturligt hör hemma i en applikations kodbas

Förmågan ska inte användas som generell behållare för all verksamhetslogik.

### 1.4 Relation till andra förmågor

**Regler och beslut** används när ett beslut eller en regel behöver kunna uttryckas, förvaltas eller exekveras oberoende av själva processflödet.

**Integration och kommunikation** tillhandahåller de mekanismer som processer använder för att kommunicera med andra system och tjänster.

**Interaktion, presentation och kanaler** tillhandahåller gränssnitt för handläggare, andra användare och externa aktörer.

**Data- och informationshantering** hanterar den information och de dokument som processer och ärenden använder eller producerar.

**Identitet och tillit** ger underlag för att avgöra vem eller vad som får utföra aktiviteter.

**Driftbarhet och motståndskraft** är särskilt viktig för långlivade processer som måste kunna återupptas efter fel eller störningar.

---

## 2. Behov och användningsområden

### 2.1 Typiska behov

Ett utvecklingsområde kan behöva stöd när ett IT-stöd ska:

- hålla ihop ett ärende genom flera steg och över lång tid
- fördela arbetsuppgifter mellan individer, roller eller organisatoriska enheter
- kombinera automatiska aktiviteter med manuell handläggning
- vänta på externa händelser eller svar utan att hålla tekniska resurser låsta
- hantera deadlines, påminnelser och eskaleringar
- följa upp var i processen ett ärende befinner sig
- återuppta en process efter tekniska fel eller planerade stopp
- koordinera aktiviteter i flera bakomliggande system
- hantera alternativa vägar beroende på beslut eller verksamhetshändelser
- ge verksamheten insyn i processutfall och ledtider

### 2.2 Typiska användningsfall

#### Handläggningsärende

Ett ärende skapas, tilldelas en handläggare, kompletteras vid behov, passerar ett eller flera beslutssteg och avslutas eller överlämnas.

#### Automatisk process med manuella kontrollpunkter

Merparten av flödet är automatiserat men vissa händelser kräver manuell granskning eller beslut.

#### Långlivad samverkansprocess

Ett flöde väntar på svar från externa parter eller andra myndigheter och behöver kunna återupptas när nya händelser anländer.

#### Koordinering mellan flera system

Ett verksamhetsflöde kräver aktiviteter i flera system där status, fel och kompensation behöver hanteras sammanhållet.

#### Arbetskö

Arbetsuppgifter behöver prioriteras och fördelas till rätt roll eller organisatorisk enhet utifrån verksamhetsregler och belastning.

### 2.3 Centrala arkitekturfrågor

Utvecklingsområdet bör bland annat ta ställning till:

- Är behovet ett verkligt långlivat process-/ärendeflöde eller vanlig applikationslogik?
- Behöver processens tillstånd vara explicit, synligt och återupptagningsbart?
- Finns manuella aktiviteter eller överlämningar mellan roller?
- Behöver verksamheten kunna följa och analysera processens status eller ledtider?
- Behöver processdefinitionen förändras oberoende av övrig applikationskod?
- Vilken information tillhör processen och vilken tillhör verksamhetsobjektet?
- Vilka regler bör ligga i en separat besluts-/regelförmåga?
- Hur ska integration med andra system ske och hur hanteras fel?
- Vilka krav finns på spårbarhet, historik och arkivering?
- Hur hanteras versionsförändringar för redan pågående processer?
- Vad händer om en extern tjänst eller aktivitet är otillgänglig under lång tid?
- När är en central workflow-/ärendeplattform motiverad jämfört med lokal implementation?

---

## 3. Förmågespecifika arkitekturprinciper

Gemensamma principer finns i `../styrning/gemensamma-arkitekturprinciper.md`.

### P-PWÄ-01 Processlogik ska vara explicit när den behöver förvaltas som process

**Princip:**  
Processflöden som behöver kunna följas, återupptas, analyseras eller förändras som en sammanhängande verksamhetsprocess bör modelleras explicit i stället för att döljas i spridd applikationskod.

**Motivering:**  
Explicit processhantering förbättrar spårbarhet, förståelse och möjlighet till långsiktig förvaltning.

**Konsekvens:**  
Det ska samtidigt undvikas att trivial kontrolllogik flyttas till en processmotor utan tydligt behov.

### P-PWÄ-02 Processorkestrering och domänlogik ska hållas isär

**Princip:**  
Processen ska beskriva ordning, koordinering och övergångar mellan aktiviteter medan verksamhetslogik så långt som möjligt ligger i domäntjänster eller regeltjänster.

**Motivering:**  
Det minskar kopplingen mellan processmotor och verksamhetsfunktionalitet och gör båda enklare att förändra.

**Konsekvens:**  
Processdefinitioner bör normalt anropa tydliga tjänster i stället för att innehålla omfattande domänlogik.

### P-PWÄ-03 Långlivade processer ska tåla väntan och återstart

**Princip:**  
Processer som kan pågå under längre tid ska kunna persistenteras och återupptas utan beroende av en kontinuerligt aktiv teknisk session eller process.

**Motivering:**  
Verksamhetsprocessens livslängd är ofta längre än livslängden för en applikationsinstans, anslutning eller transaktion.

**Konsekvens:**  
Timers, väntelägen och externa svar ska hanteras med mekanismer som stödjer robust återupptagning.

### P-PWÄ-04 Processen ska inte bli integrationsplattform

**Princip:**  
Processmotorer ska inte användas som generell ersättning för API management, messaging eller annan integrationsinfrastruktur.

**Motivering:**  
Orkestrering av verksamhetsflöde och teknisk integration är närliggande men olika ansvar.

**Konsekvens:**  
Processen använder standardiserade integrationsförmågor där sådana finns.

### P-PWÄ-05 Ärendeinformation ska ha tydligt informationsägarskap

**Princip:**  
Det ska vara tydligt vilken information som utgör process-/ärendestatus och vilken som är verksamhetsinformation med egen livscykel.

**Motivering:**  
Processmotorns interna datalagring bör inte oavsiktligt bli system of record för verksamhetsinformation.

**Konsekvens:**  
Väsentliga verksamhetsdata ska hanteras enligt principerna för Data- och informationshantering.

### P-PWÄ-06 Processmodellering ska motiveras av faktisk nytta

**Princip:**  
Workflow- eller ärendeplattform ska användas när dess egenskaper ger tydlig nytta för behovet, inte enbart för att en sådan plattform finns.

**Motivering:**  
Överanvändning kan skapa onödig komplexitet och stark koppling till en plattform.

**Konsekvens:**  
Enklare sekvenser och kortlivad kontrolllogik kan med fördel implementeras i vanlig applikationskod.

---

## 4. Krav och styrande riktlinjer

### KR-PWÄ-01 Tydligt ansvar för process och verksamhetsdata

**Krav:**  
IT-stöd som använder gemensam process- eller ärendeplattform ska dokumentera vilka data som ägs av processen respektive av bakomliggande verksamhetstjänster.

**Motivering/källa:**  
Minskar otydligt informationsägarskap och beroende av processmotorns interna lagring.

**Tillämpningsområde:**  
Lösningar med central workflow-, process- eller ärendeplattform.

### KR-PWÄ-02 Återupptagningsbarhet för långlivade flöden

**Krav:**  
Långlivade processer ska utformas så att de kan återupptas efter omstart eller tillfälligt fel utan att verksamhetsstatus går förlorad.

**Motivering/källa:**  
Härleds från behov av kontinuitet, korrekthet och driftbarhet.

**Tillämpningsområde:**  
Processer som kan vänta på användare, timer, extern part eller systemhändelse.

### KR-PWÄ-03 Versionshantering av processdefinitioner

**Krav:**  
Förändring av en processdefinition ska hantera redan startade processinstanser på ett definierat sätt.

**Motivering/källa:**  
Pågående ärenden kan ha längre livslängd än en enskild release.

**Tillämpningsområde:**  
Versionerade process- och workflowdefinitioner.

### KR-PWÄ-04 Behörighetskontroll för arbetsuppgifter

**Krav:**  
Tilldelning, visning och utförande av manuella arbetsuppgifter ska följa organisationens gemensamma principer och tjänster för identitet och behörighet.

**Motivering/källa:**  
Härleds från säkerhet och informationsskydd.

**Tillämpningsområde:**  
Human tasks, ärenden och arbetsköer.

### KR-PWÄ-05 Spårbar processhistorik

**Krav:**  
När verksamhetsbehov eller regelkrav kräver det ska processens betydelsefulla statusövergångar och aktiviteter kunna följas i efterhand.

**Motivering/källa:**  
Härleds från spårbarhet och verifierbarhet; nivån ska anpassas till behovet.

**Tillämpningsområde:**  
Processer och ärenden med uttryckligt behov av audit eller historik.

### KR-PWÄ-06 Ingen känslig information i tekniska processfält utan behov

**Krav:**  
Processvariabler, korrelationsnycklar och tekniska loggar ska inte innehålla mer skyddsvärd verksamhetsinformation än vad som krävs för funktionen.

**Motivering/källa:**  
Säkerhet, dataminimering och minskad spridning av känslig information.

**Tillämpningsområde:**  
Alla process- och workflowlösningar.

### KR-PWÄ-07 Externa beroenden ska ha definierat felbeteende

**Krav:**  
Processteg som beror på externa system eller tjänster ska ha definierad hantering för timeout, avbrott, retry och verksamhetsmässigt fel där det är relevant.

**Motivering/källa:**  
Kontinuitet, driftbarhet och korrekthet.

**Tillämpningsområde:**  
Processer som koordinerar externa tjänster eller system.

---

## 5. Guidelines och vägledning

### När bör en workflowmotor användas?

Överväg workflowmotor när flera av följande gäller:

- processen är långlivad
- manuella och automatiska steg kombineras
- processen behöver kunna följas och visualiseras
- status behöver persistenteras mellan aktiviteter
- timers, väntelägen eller eskaleringar är centrala
- processen koordinerar flera tjänster
- processdefinitionen behöver kunna förändras och versionshanteras separat
- verksamheten behöver analys av flöden och ledtider

Undvik workflowmotor när behovet huvudsakligen är en enkel, kortlivad sekvens av anrop inom en applikation.

### Workflow eller vanlig applikationslogik?

Fråga i första hand om flödet har ett **eget verksamhetsmässigt tillstånd** som behöver förstås eller hanteras över tid.

Om svaret är nej är vanlig applikationslogik ofta enklare och mer ändamålsenlig.

### Workflow eller ärendehantering?

Workflow fokuserar på aktiviteter och flöde. Ärendehantering fokuserar ofta mer på ett verksamhetsobjekt med historik, dokument, ansvar och varierande handläggningsväg.

Ett ärende kan innehålla ett eller flera workflows, men alla workflows behöver inte representera ärenden.

### Process eller integration?

Använd processförmågan för **verksamhetsmässig koordinering**.

Använd integrationsförmågan för exempelvis:

- transport
- protokoll
- routing
- messaging
- API-exponering
- teknisk transformation

En process kan använda integrationstjänster utan att själv implementera deras tekniska ansvar.

### När bör verksamhetsregler externaliseras?

Överväg separat regel-/beslutstjänst när:

- samma regel används i flera processer
- regeln förändras oftare än processflödet
- verksamheten behöver kunna förstå eller granska regeln separat
- beslut behöver kunna spåras oberoende av processen

Små villkor som endast styr ett lokalt processflöde kan ligga kvar i processdefinitionen.

### Hur bör arbetsköer hanteras?

Arbetsköer bör utformas utifrån verksamhetens behov av:

- prioritering
- roller och kompetenser
- organisatorisk tillhörighet
- belastningsfördelning
- tidsfrister
- eskalering
- spårbarhet

Tekniska kömekanismer ska inte i sig definiera hur verksamheten organiserar arbetet.

### Hur hanteras processer som ändras över tid?

Bestäm innan förändring:

1. om pågående instanser fortsätter på gammal version
2. om de migreras
3. om migration kräver verksamhetsbeslut eller datatransformation
4. hur historik och spårbarhet påverkas

Det bör inte antas att alla pågående processer automatiskt kan flyttas till en ny processdefinition.

### När standardlösningen inte passar

Om ett utvecklingsområde har behov som inte möts av gemensamt workflow-/ärendeerbjudande bör behovet dokumenteras i termer av exempelvis:

- processlivslängd
- antal instanser
- antal användare
- human tasks
- integrationsbehov
- processförändringstakt
- spårbarhetskrav
- kontinuitetskrav
- prestanda

Därefter bedöms om lösningen bör anpassas, plattformserbjudandet utvecklas eller en alternativ realisering väljas.

---

## 6. Plattformar och tjänsteerbjudanden

I detta steg identifieras kandidater. Detaljerade plattformsdokument skapas separat när plattformskatalogen konsolideras eller tidigare om behov uppstår.

| Erbjudande | Syfte | Lämpligt för | Status |
|---|---|---|---|
| Workflow/Process Platform | Exekvera och följa långlivade processer | processorkestrering, timers, väntelägen, human tasks | Kandidat |
| Case Management Platform | Hantera ärenden, arbetsuppgifter och historik | handläggningsintensiva verksamhetsflöden | Kandidat |
| Work Queue Service | Gemensam hantering och fördelning av arbetsuppgifter | roller, prioritering och arbetsköer | Kandidat |
| Process Monitoring | Ge insyn i processstatus och tekniska/processnära fel | drift och uppföljning av processer | Kandidat |

Det bör under fortsatt arbete avgöras om workflow och case management bör vara separata erbjudanden eller olika profiler på samma plattform.

---

## 7. Standarder och teknikval

Följande standarder eller teknikval är identifierade som kandidater. De ska inte betraktas som beslutade enbart genom detta dokument.

| Standard/teknikval | Status | Tillämpning |
|---|---|---|
| BPMN 2.x | Kandidat | Modellering av exekverbara eller dokumenterande processer |
| DMN | Kandidat | Beslut som bör externaliseras från processflödet |
| Gemensam process-ID/korrelationsstandard | Kandidat | Spårbarhet mellan process, integration och loggning |
| Standard för human task-metadata | Kandidat | Roller, prioritet, deadline och status |
| Processversionsprincip | Kandidat | Hantering av pågående instanser vid release |

Ett framtida teknikval av exempelvis en specifik processmotor ska dokumenteras separat från själva förmågan.

---

## 8. Relaterade artefakter och kvalitetsdimensioner

### 8.1 Relevanta kvalitetsdimensioner

Särskilt viktiga dimensioner från `../styrning/krav-och-kvalitetsdimensioner.md` är:

- **Säkerhet och informationsskydd** – processer och ärenden kan innehålla eller referera till skyddsvärd information.
- **Tillgänglighet** – kritiska verksamhetsprocesser kan vara beroende av processplattformens tillgänglighet.
- **Kontinuitet och återställningsförmåga** – långlivade processer måste kunna återupptas korrekt.
- **Prestanda** – särskilt relevant för högvolymprocesser och arbetsköer.
- **Skalbarhet och kapacitet** – antal processinstanser, timers och historik kan växa kraftigt.
- **Spårbarhet och verifierbarhet** – centralt för ärenden och processer där det finns behov av efterhandsgranskning.
- **Regelefterlevnad** – processhistorik, information och arbetsfördelning kan omfattas av externa eller interna krav.
- **Förvaltningsbarhet och förändringsbarhet** – processer förändras och kan ha instanser som lever över flera releaser.
- **Livscykel och hållbarhet** – val av processplattform kan skapa betydande långsiktiga beroenden.

### 8.2 Lösningsmönster

Identifierade kandidater:

- Human Workflow
- Long-running Process
- Process Manager / Orchestration
- Saga / kompensationsmönster
- Externaliserade verksamhetsregler
- Event-driven Process
- Arbetskö och rollbaserad tilldelning

Mönstren ska senare bedömas mot hela förmågebildens behov innan separata dokument skapas.

### 8.3 Plattformar

Identifierade kandidater:

- Workflow/Process Platform
- Case Management Platform
- Work Queue Service
- Process Monitoring

### 8.4 Tekniska standarder

Identifierade kandidater:

- BPMN
- DMN
- processkorrelationsstandard
- processversionsprincip
- metadata för human tasks

### 8.5 Kandidater till referensarkitekturer

Följande tvärgående referensarkitekturer har identifierats eller stärkts:

- **Internt handläggningsstöd** – kandidat sedan steg 1; denna förmåga är central.
- **Publik e-tjänst med bakomliggande handläggning** – kombinerar interaktion, process, regler, data, integration och identitet.
- **Integrationsintensivt verksamhetssystem** – processorkestrering kan vara relevant tillsammans med integration och messaging.
- **Långlivad myndighetsöverskridande process** – kandidat där externa svar, SGSI/SHS eller andra samverkansformer kan ingå.

### 8.6 Teknisk dokumentation

När konkreta process-/ärendeplattformar väljs bör teknisk dokumentation ligga separat och exempelvis omfatta:

- processdeployment
- versionshantering
- klientbibliotek
- autentisering
- API:er
- drift och övervakning
- backup och återställning
- skalningsmodell
- tekniska begränsningar

---

## Arbetsanteckningar

### Identifierade kandidater

**Lösningsmönster**
- Human Workflow
- Long-running Process
- Process Manager / Orchestration
- Saga / kompensation
- Externaliserade verksamhetsregler
- Event-driven Process
- Arbetskö och rollbaserad tilldelning

**Plattformar/tjänster**
- Workflow/Process Platform
- Case Management Platform
- Work Queue Service
- Process Monitoring

**Tekniska standarder**
- BPMN
- DMN
- processkorrelationsstandard
- processversionsprincip
- human task-metadata

**Referensarkitekturer**
- internt handläggningsstöd
- publik e-tjänst med handläggning
- integrationsintensivt verksamhetssystem
- långlivad myndighetsöverskridande process

**Gränsdragningsfrågor**
- hur mycket processtillstånd som bör lagras i processmotor respektive verksamhetssystem
- var gränsen mellan processvillkor och externa verksamhetsregler bör gå
- när workflow och case management bör vara separata plattformserbjudanden
- hur processhistorik förhåller sig till verksamhetsmässig arkivering
