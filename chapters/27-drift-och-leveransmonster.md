# 27. Drift- och leveransmönster

En lösning är inte färdig när koden fungerar på en utvecklares dator. Den måste kunna byggas reproducerbart, förflyttas mellan miljöer utan att ändra identitet, observeras när den körs och återställas när något går fel. Det är först då leverans och drift blir delar av arkitekturen i stället för aktiviteter som läggs på i slutet.

Här fokuserar vi på tre återanvändbara mönster och på de beroenden som uppstår när leverans och drift kombineras.

I det här kapitlet fördjupar vi tre lösningsmönster från bokens mönsterbibliotek:

- *Build once, promote many*,
- *Observerbarhet för distribuerade tjänster*,
- *Backup och verifierad återställning*.

De tre mönstren angriper olika problem. Build once, promote many skapar förtroende för att den artefakt som når produktion är samma artefakt som testades. Observerbarhet gör det möjligt att förstå en körande lösnings beteende över tjänste- och plattformsgränser. Backup och verifierad återställning gör det möjligt att återfå data och nödvändig konfiguration efter förlust eller korruption.

Tillsammans binder de ihop tre delar av livscykeln:

```text
Bygga och verifiera
        ↓
Promovera och driftsätta
        ↓
Observera och förstå
        ↓
Återställa när något går fel
        ↓
Lära och förbättra nästa leverans
```

Det är viktigt att hålla ansvaren isär. En reproducerbar artefakt skapar inte observerbarhet. Bra tracing ersätter inte backup. En lyckad backup säger inte att återställning fungerar. Mönstren blir starka när de kombineras, inte när ett av dem förväntas lösa allt.

## Drift och leverans börjar före produktion

Ett vanligt anti-pattern är att behandla driftbarhet som en fråga som uppstår först vid produktionssättning. Då har flera avgörande arkitekturval redan gjorts:

- hur artefakter byggs,
- var konfiguration ligger,
- hur versioner identifieras,
- hur loggar och mätvärden produceras,
- hur korrelation fungerar,
- vilka data som måste skyddas,
- hur återställning kan genomföras,
- vilka beroenden som krävs för att systemet ska fungera.

Om dessa frågor inte hanteras under design och utveckling blir de ofta dyra att lägga till i efterhand.

Det är därför mer träffsäkert att se leverans och drift som egenskaper hos lösningen än som separata processer runt lösningen.

En tjänst som inte kan koppla en produktionsversion till ett källkodscommit har ett arkitekturproblem. En tjänst som inte kan korrelera en användaroperation över sina beroenden har ett arkitekturproblem. Ett system som har backup men saknar verifierad återställningsförmåga har också ett arkitekturproblem.

Mönstren i kapitlet gör sådana egenskaper explicita och återanvändbara.

## Mönster 1: Build once, promote many

### Problemet

Anta att en applikation byggs separat i varje miljö:

```text
Källkod
 ├─ build för test
 ├─ build för acceptans
 └─ build för produktion
```

Även om alla builds utgår från samma kod finns flera möjliga skillnader:

- beroenden kan ha förändrats,
- byggverktygets miljö kan skilja sig,
- externa paket kan ha fått nya versioner,
- byggargument kan variera,
- tid eller miljövariabler kan påverka resultatet,
- någon kan ha ändrat konfiguration som bakas in i artefakten.

Därmed uppstår en obehaglig fråga:

> Är det faktiskt den testade programvaran som körs i produktion?

Om svaret inte kan styrkas har testkedjan en bruten tillitslänk.

### Mönstret

Build once, promote many separerar byggandet av programvaran från förflyttningen av samma artefakt mellan miljöer.

```text
Källkod
   ↓
Build + verifiering
   ↓
Versionsmärkt, immutable artefakt
   ↓
Artefaktregister
   ├─ promoveras till test
   ├─ promoveras till acceptans
   └─ promoveras till produktion
```

Nyckelordet är inte bara *build once*. Det är att artefakten har en stabil identitet genom hela leveranskedjan.

Om en containerimage exempelvis har testats bör produktionssättningen referera samma imageidentitet, inte skapa en ny image från samma Dockerfile.

### Vad måste separeras från artefakten?

Mönstret fungerar bara om miljöspecifika egenskaper inte kräver en ny build.

Typiska exempel på sådant som bör hanteras utanför den byggda artefakten är:

- endpointadresser,
- databaskopplingar,
- funktionsflaggor,
- resursprofiler,
- miljöspecifik loggingnivå,
- credentials och secrets,
- vissa policyvärden.

Det betyder inte att all konfiguration ska kunna förändras fritt. Det betyder att miljöskillnader ska uttryckas som kontrollerad konfiguration, inte genom att programvaran kompileras eller paketeras på nytt.

Det ger en tydligare separation:

```text
Artefakt = vad vi byggde och testade
Konfiguration = hur artefakten körs i denna miljö
Secret = känsligt värde som behövs vid körning
```

### Immutable betyder inte oföränderlig för alltid

En immutable artefakt ska inte modifieras efter publicering under samma identitet. Om innehållet ändras ska en ny artefakt med ny identitet skapas.

Det är en viktig skillnad mot att artefakten aldrig får ersättas. Tvärtom förväntas nya versioner byggas kontinuerligt. Men varje version måste kunna behandlas som en stabil enhet.

Det gör spårbarhet möjlig:

```text
Källkodscommit
      ↓
Build
      ↓
Artefakt A
      ↓
Tester och kontroller
      ↓
Produktion: Artefakt A
```

### Promotion är ett beslut, inte en ny build

När en artefakt går från test till acceptans eller produktion bör leveransflödet främst svara på frågor som:

- Har rätt kontroller passerats?
- Har artefakten rätt provenance och signatur där det krävs?
- Är den godkänd för denna miljö?
- Finns rätt konfiguration?
- Är beroenden och migreringar kompatibla?
- Är releasefönster eller manuellt godkännande relevant?

Själva artefakten behöver däremot inte byggas om.

### Databasmigreringar komplicerar bilden

Applikationsartefakten kan vara immutable, men en release kan ändå förändra persistent tillstånd genom databasmigreringar.

Därför behöver mönstret kompletteras med en tydlig strategi för:

- schemaevolution,
- framåt- och bakåtkompatibilitet,
- migreringsordning,
- rollback eller roll-forward,
- samtidiga gamla och nya applikationsversioner.

Build once, promote many löser alltså artefaktidentiteten, inte hela releaseproblemet.

### När mönstret passar

Mönstret passar särskilt väl när:

- samma programvara går genom flera miljöer,
- spårbarhet mellan test och produktion är viktig,
- leveransen automatiseras,
- artefakter kan lagras i ett kontrollerat register,
- miljöspecifik konfiguration kan separeras från programvaran.

Det är ofta ett starkt grundmönster för både containerbaserade och traditionellt paketerade applikationer.

### När mönstret behöver anpassas

Det kan kräva variationer när själva resultatet måste produceras specifikt för en viss målmiljö, exempelvis:

- plattformsspecifik native-kompilering,
- vissa firmwareflöden,
- hårdvarubundna artefakter,
- kundspecifika paket där innehållet faktiskt skiljer sig.

Principen bör ändå bevaras så långt det går: det som testas och godkänns ska ha en entydig identitet och inte förändras på vägen till målmiljön.

## Mönster 2: Observerbarhet för distribuerade tjänster

### Problemet

I en monolitisk applikation kan en lokal logg ibland ge en stor del av felsökningsbilden. I en distribuerad lösning kan samma användaroperation passera:

- webbgränssnitt,
- BFF,
- API gateway,
- flera domäntjänster,
- meddelandekö,
- databas,
- extern tjänst.

Ett fel kan därför vara synligt i en komponent men orsakat i en annan.

```text
Användare
   ↓
BFF
   ↓
Tjänst A → Tjänst B → Databas
   │
   └→ Meddelande → Tjänst C → Externt API
```

Lokala loggfiler svarar då dåligt på frågor som:

- Vilken väg tog den misslyckade operationen?
- Var uppstod fördröjningen?
- Vilken version av en tjänst deltog?
- Berör problemet alla användare eller bara ett visst flöde?
- Är felet tekniskt eller verksamhetsmässigt?

### Mönstret

Observerbarhetmönstret kombinerar flera typer av signaler:

- strukturerade loggar,
- mätvärden,
- distributed tracing,
- korrelationsinformation,
- central eller federerad insamling,
- instrumentpaneler,
- åtgärdsbara larm.

Poängen är inte mängden telemetri. Poängen är att kunna ställa relevanta frågor om systemets tillstånd utan att i förväg känna till exakt vilket fel som kommer att inträffa.

### Tre signaltyper med olika styrkor

### Loggar

Loggar är händelseorienterade och kan ge rik kontext:

```text
order_id=4711
operation=confirm
result=failed
reason=credit_check_timeout
service=order-service
version=3.8.2
```

Strukturerade loggar gör informationen sökbar och möjlig att korrelera.

### mätvärden

mätvärden passar för aggregerade tidsserier:

- latens,
- throughput,
- felkvot,
- ködjup,
- CPU- och minnesanvändning,
- antal lyckade verksamhetsoperationer.

De är effektiva för trender, SLI:er och larm.

### spår

Distributed tracing visar en operations väg över flera komponenter. Det är särskilt värdefullt för att förstå latens och beroenden i distribuerade flöden.

Ingen av signalerna ersätter de andra. En trace kan visa *var* tiden försvann, en logg kan visa *varför* ett anrop misslyckades och mätvärden kan visa *hur ofta* problemet uppstår.

### Korrelation måste designas

Observerbarhet över flera tjänster kräver att relationer mellan händelser kan följas.

Det kan finnas flera relevanta identiteter:

- trace-id,
- span-id,
- request-id,
- meddelande-id,
- verksamhetskorrelation som ärende-id eller order-id.

De bör inte blandas ihop.

Ett tekniskt trace-id har annan livslängd och mening än ett verksamhetsärende. Ett meddelande kan dessutom behandlas senare i ett nytt tekniskt trace men fortfarande höra till samma verksamhetsflöde.

Mönstret behöver därför beskriva vilka korrelationer som ska följa med över vilka gränser.

### Observerbarhet bör följa driftsättningen

När en ny version promoveras till produktion bör telemetri göra det möjligt att koppla observerat beteende till just den versionen.

Det ger en viktig länk till build once, promote many:

```text
Artefaktversion
      ↓
Driftsättning
      ↓
Telemetri märkt med version
      ↓
Jämförelse före/efter release
```

Då kan man exempelvis se om version 3.8.2 förändrade:

- felkvot,
- p95-latens,
- minnesanvändning,
- antal misslyckade verksamhetsoperationer.

Observerbarhet blir därmed en del av releaseverifieringen, inte bara felsökning efter incident.

### SLI och SLO ger riktning

Telemetri blir mest värdefull när den kopplas till kvalitetskrav.

En lösning kan samla tusentals mätvärden utan att veta vilka som faktiskt avgör om tjänsten fungerar för konsumenten.

En Service Level Indicator (SLI) uttrycker en mätbar egenskap, exempelvis andelen lyckade begäranden eller latens för en viss operation. Ett Service Level Objective (SLO) anger den nivå som eftersträvas.

Exempel:

```text
SLI: andel lyckade registreringar
SLO: minst 99,9 % under rullande 30 dagar
```

Det gör observerbarhet användbar för arkitekturella beslut. Om en release försämrar den indikator som faktiskt representerar tjänstens nytta är det mer betydelsefullt än att en enskild intern metric förändras.

### Åtgärdsbara larm

Ett larm bör inte bara säga att ett mätvärde passerat ett tröskelvärde. Det bör representera en situation som någon kan och bör agera på.

Bra larmdesign kräver frågor som:

- Vilken konsekvens indikerar larmet?
- Vem är mottagare?
- Finns en förväntad första åtgärd?
- Är problemet redan självläkande?
- Är signalen tillräckligt stabil för att undvika brus?

Ett system med hundratals lågkvalitativa larm kan vara sämre observerbart än ett system med få men relevanta signaler.

### När mönstret passar

Mönstret är särskilt viktigt för:

- distribuerade tjänster,
- integrationsintensiva lösningar,
- asynkrona flöden,
- lösningar över flera plattformar,
- system med höga krav på felsökning, spårbarhet eller tillgänglighet.

Även mindre system tjänar dock på en gemensam miniminivå för strukturerad logging, mätvärden och korrelation.

## Mönster 3: Backup och verifierad återställning

### Problemet

Det finns en farlig men vanlig likställning:

> Backupjobbet lyckades, alltså kan systemet återställas.

Det följer inte.

En backup kan vara:

- ofullständig,
- korrupt,
- beroende av metadata som inte säkerhetskopierats,
- oförenlig med aktuell programversion,
- för långsam att återställa,
- lagrad i samma fel- eller hotdomän som originalet,
- omöjlig att använda utan credentials som försvann i incidenten.

Därför är den verkliga förmågan inte backup utan återställning.

Backup är bara en av mekanismerna.

### Mönstret

Ett robust backup-/restore-mönster kan uttryckas i sex steg:

1. identifiera skyddsvärda data och konfiguration,
2. härled återställningsbehov från verksamhetskonsekvens,
3. skapa backup enligt lämplig profil,
4. separera backup från primär fel- och hotdomän där behovet kräver det,
5. genomför återkommande restore-test,
6. dokumentera faktisk återställningstid, databortfall och avvikelser.

Det viktiga är återkopplingen mellan krav och verifiering.

### Börja med vad som faktiskt måste återställas

Ett system består av mer än en databas.

Återställningsinventeringen kan behöva omfatta:

- verksamhetsdata,
- dokument och objekt,
- konfiguration,
- kryptografiskt material där det är lämpligt och möjligt,
- infrastrukturdefinitioner,
- versionsinformation,
- scheman och migreringshistorik,
- externa beroenden eller instruktioner för att återansluta dem.

Samtidigt behöver inte allt säkerhetskopieras.

En sökindexkopia kan exempelvis vara fullt återbyggbar från auktoritativ data. En containerimage kan redan finnas i ett artefaktregister. Temporär cache bör normalt inte behöva restaureras alls.

En central fråga blir därför:

> Vad är oersättligt, och vad kan reproduceras?

Det kopplar återställningsmönstret direkt till bokens tidigare skillnad mellan auktoritativt och härlett tillstånd.

### RPO och RTO måste kopplas till mekanismen

Två vanligt använda återställningsmått är:

- RPO – hur mycket dataförlust i tid som kan tolereras,
- RTO – hur lång återställningstid som kan tolereras.

Mönstret blir först meningsfullt när backup- och återställningsdesignen faktiskt kan möta dessa mål.

Om RPO är 15 minuter men backup görs en gång per dygn finns en uppenbar konflikt. Om RTO är en timme men den senaste realistiska restore-övningen tog sju timmar är det den observerade återställningsförmågan som bör styra riskbilden.

### Restore-test är en del av produkten

Ett restore-test bör inte reduceras till att någon visar att en fil kan läsas ur backupen.

En relevant testkedja kan vara:

```text
Välj backupversion
      ↓
Återställ data och nödvändig konfiguration
      ↓
Starta eller anslut rätt applikationsversion
      ↓
Verifiera dataintegritet
      ↓
Verifiera kritiska verksamhetsflöden
      ↓
Mät faktisk RPO/RTO
      ↓
Dokumentera avvikelser
```

Det gör återställning till en verifierbar egenskap.

### Replikering är inte backup

Replikering förbättrar ofta tillgänglighet och kan minska återställningstid vid vissa typer av fel. Men den kan också snabbt replikera:

- felaktig radering,
- korruption,
- logiska applikationsfel,
- skadliga ändringar.

Backup och replikering löser därför olika problem och kan behöva kombineras.

### Återställning måste omfatta beroenden

En databasrestore hjälper inte om systemet därefter saknar:

- kompatibel applikationsartefakt,
- rätt schema- eller migreringsnivå,
- nödvändiga secrets,
- routing eller DNS,
- identitetsintegration,
- konfiguration för externa beroenden.

Här möts alla tre kapitlets mönster.

Build once, promote many gör gamla applikationsartefakter reproducerbart identifierbara. Observerbarhet gör det möjligt att verifiera att den återställda tjänsten faktiskt fungerar. Backup-/restore-mönstret återför det tillstånd som inte kan återskapas på annat sätt.

## Tre mönster – en sammanhängande kedja

Det är lätt att implementera de tre mönstren i separata organisatoriska silor:

- utvecklingsplattformen äger CI/CD,
- driftteamet äger övervakning,
- infrastrukturteamet äger backup.

Tekniskt kan allt då se korrekt ut samtidigt som den sammanhängande återställnings- och leveranskedjan är svag.

En bättre modell är att se dem som tre länkar i samma tillitskedja.

### Före release

Build once, promote many svarar på:

> Vilken exakt programvara är det vi tänker sätta i produktion?

### Efter release

Observerbarhet svarar på:

> Beter sig den produktionssatta versionen som vi förväntar oss?

### Vid allvarligt fel

Backup och verifierad återställning svarar på:

> Kan vi återfå nödvändigt tillstånd och återetablera en fungerande tjänst inom accepterad tid och dataförlust?

Tillsammans ger de en kedja:

```text
Källkod
  ↓
Identifierbar artefakt
  ↓
Kontrollerad promotion
  ↓
Observerad produktion
  ↓
Incident eller dataförlust
  ↓
Verifierad återställning
  ↓
Observerad funktion efter restore
```

Det är en starkare arkitekturmodell än tre isolerade teknikfunktioner.

## Releasebeslut bör använda driftdata

En mogen leveransprocess slutar inte när driftsättningsverktyget rapporterar ”success”.

En driftsättning kan tekniskt lyckas samtidigt som:

- latensen stiger kraftigt,
- en viss verksamhetsoperation börjar misslyckas,
- meddelandeköer byggs upp,
- minnesanvändningen driver,
- fel endast uppstår för en viss användargrupp.

Därför kan releaseflödet använda observerbarhet som verifieringssteg.

Exempel:

```text
Deploy version 4.2
      ↓
Tekniska health checks
      ↓
Kontroll av centrala SLI:er
      ↓
Jämför med baseline
      ↓
Promote / fortsätt / stoppa / roll-forward
```

Det behöver inte innebära att alla beslut automatiseras. Poängen är att produktionsbeteende blir en explicit del av leveransbeslutet.

## Rollback är inte alltid samma sak som återställning

Begreppen blandas ibland ihop.

Rollback av applikation innebär att gå tillbaka till en tidigare programversion.

Restore av data innebär att återskapa persistent tillstånd från en tidigare eller skyddad kopia.

De kan ha helt olika konsekvenser.

Anta att version 4.2 har genomfört en irreversibel datamigrering. Då kanske applikationen inte kan rullas tillbaka till 4.1 trots att den gamla artefakten finns kvar.

Eller anta att användare hunnit skapa giltig verksamhetsdata efter releasen. Att återställa databasen till en äldre tidpunkt skulle då förlora dessa förändringar.

Därför behöver lösningen skilja mellan:

- application rollback,
- configuration rollback,
- roll-forward,
- data restore,
- point-in-time recovery,
- kompensation av verksamhetseffekter.

Mönstren måste kombineras med en explicit release- och återställningsstrategi.

## Felgränser och separata kontrollplan

En robust design bör fråga vad som händer om stödmekanismerna själva går sönder.

Exempel:

- Vad händer om artefaktregistret är otillgängligt under återställning?
- Kan loggingplattformen falla utan att applikationen slutar fungera?
- Vad händer om tracingexport blockeras?
- Kan backupkatalogen nås om den primära identitetsplattformen ligger nere?
- Finns restoreinstruktioner tillgängliga under en större incident?

Det är lätt att skapa cirkulära beroenden.

```text
Systemet kräver identitetstjänst för att återställas
Identitetstjänsten kräver samma system för sin återställning
```

eller:

```text
Restoreproceduren ligger endast i samarbetsplattformen
Samarbetsplattformen är själv otillgänglig i incidenten
```

Återställningsarkitektur behöver därför analysera kontrollplan, credentials och dokumentation som egna beroenden.

## Hur ansvar bör fördelas

Ansvarsfördelningen följer samma princip som i tidigare kapitel. Den gemensamma arkitekturnivån sätter spelregler där inkonsistens skapar organisationsövergripande risk, exempelvis krav på spårbar artefaktidentitet, miniminivå för telemetri och korrelation, backup-/recoveryprofiler och återställningstest för vissa riskklasser.

Förmågenivån omsätter dessa krav i konsumerbara erbjudanden som CI/CD-plattform, artefaktregister, pipelinekomponenter, observerbarhetstjänster, backup- och recoverytjänster samt standardprofiler och golden paths. Lösnings-/produktnivån avgör däremot vilka SLI:er som representerar tjänstens funktion, vilka data som är skyddsvärda, vilket RPO/RTO som gäller och vilka release-, rollback- och återställningsstrategier som är realistiska.

Det gemensamma stödet minskar mängden uppfinning, men kan inte avgöra lösningens verksamhetskonsekvens.

## Vanliga anti-patterns

Några återkommande fel är särskilt värda att känna igen:

- **Build per miljö:** samma källkod byggs om inför varje miljö och test–produktionskedjan får olika artefaktidentitet.
- **Mutable latest:** samma versionsnamn pekar på olika innehåll över tid, vilket förstör spårbarheten.
- **Miljökonfiguration i artefakten:** en ny build krävs för miljöspecifika värden som borde vara kontrollerad körkonfiguration.
- **Telemetri utan frågor:** stora mängder signaler produceras utan att någon definierat vilka frågor de ska besvara.
- **Instrumentpaneler eller larm som mål:** instrumentpaneler och tekniska tröskellarm blir ett självändamål i stället för stöd för tjänstens SLI:er och verksamhetskonsekvenser.
- **Backup equals done:** ett grönt backupjobb ses som bevis på återställningsförmåga utan verifierat restore-test.
- **Replikering kallas backup:** hög tillgänglighet blandas ihop med skydd mot logisk korruption, radering eller angrepp.
- **Ofullständig restorekedja:** data kan återställas men rätt applikationsversion, credentials, instruktioner eller kontrollverktyg saknas eller ligger i samma felgräns som den havererade miljön.

## Ett genomgående exempel

Anta en containerbaserad verksamhetstjänst som hanterar ansökningar.

### Leverans

Pipeline bygger version `2.7.0` en gång, genomför tester och publicerar en immutable containerimage i artefaktregistret.

Samma image promoveras genom test och acceptans till produktion. Databasadress och andra miljövärden tillförs som extern konfiguration. Secrets levereras vid runtime.

### Produktion

Tjänsten producerar:

- strukturerade loggar,
- tekniska mätvärden,
- verksamhetsnära SLI:er,
- spår över anrop till regel- och integrationstjänster.

All telemetri innehåller tjänstenamn och artefaktversion. Därmed kan driftorganisationen se om just version 2.7.0 påverkar exempelvis andelen lyckade registreringar.

### Data

Ansökningsdatabasen är auktoritativ verksamhetsdata och omfattas av en backup-/recoveryprofil. Ett separat sökindex är härlett och behöver inte återställas från backup eftersom det kan byggas om.

RPO är 15 minuter och RTO två timmar.

### Incident

En felaktig administrativ operation skadar verksamhetsdata. Replikeringen har redan spridit felet, vilket visar varför repliker inte ersätter backup.

Restoreproceduren väljer en lämplig återställningspunkt, återskapar databasen och kopplar den till en kompatibel applikationsversion från artefaktregistret.

Efter restore verifieras:

- dataintegritet,
- kritiska verksamhetsflöden,
- centrala SLI:er,
- faktisk återställningstid,
- faktiskt databortfall.

Resultatet visar RTO på 1 timme och 34 minuter och RPO på 11 minuter.

Därmed har organisationen inte bara en backup – den har evidens för sin återställningsförmåga.

## En praktisk analysordning

När drift- och leveransmönster ska appliceras kan följande ordning användas.

### 1. Identifiera releaseenheten

Vad är den immutable artefakt som ska testas och promoveras?

### 2. Separera artefakt, konfiguration och secrets

Vilka skillnader mellan miljöer kräver verkligen olika programvara, och vilka är körkonfiguration?

### 3. Etablera spårbar identitet

Kan produktion kopplas till exakt artefakt, build, källkod och relevanta kontroller?

### 4. Definiera tjänstens viktigaste observerbara beteenden

Vilka tekniska och verksamhetsnära signaler visar att tjänsten fungerar?

### 5. Designa korrelation

Hur följs en operation över tjänste-, meddelande- och plattformsgränser?

### 6. Koppla telemetri till SLI/SLO

Vilka mätvärden representerar den kvalitet konsumenten faktiskt upplever?

### 7. Identifiera oersättligt tillstånd

Vilka data och konfigurationer kan inte enkelt reproduceras?

### 8. Härled RPO och RTO

Vilken dataförlust och återställningstid kan verksamheten tolerera?

### 9. Designa fullständig restorekedja

Vilka artefakter, data, credentials, konfigurationer och beroenden krävs för att tjänsten ska fungera igen?

### 10. Testa hela kedjan

Verifiera inte bara enskilda mekanismer. Testa promotion, observation och återställning som faktiska systemegenskaper.

## Det viktigaste att bära med sig

Drift- och leveransmönster handlar ytterst om förtroende för förändring och återhämtning.

Build once, promote many gör det möjligt att veta vilken programvara som testades och vilken som körs. Observerbarhet gör det möjligt att förstå hur den programvaran faktiskt beter sig i en distribuerad lösning. Backup och verifierad återställning gör det möjligt att återskapa det tillstånd som inte kan reproduceras när ett allvarligt fel inträffar.

De tre mönstren kan sammanfattas med tre frågor:

1. Kan vi bevisa exakt vad vi satte i produktion?
2. Kan vi förstå om det fungerar och varför det inte gör det?
3. Kan vi återetablera en fungerande tjänst när data eller miljö går förlorad?

Om någon av frågorna saknar ett verifierbart svar är leverans- och driftförmågan ofullständig, även om enskilda verktyg finns på plats.

Med detta avslutas bokens del om lösningsmönster. I nästa del flyttar vi fokus från återanvändbara lösningsbeslut till plattformstjänster. Först undersöker vi vad som egentligen krävs för att ett tekniskt byggblock ska bli ett konsumerbart gemensamt erbjudande – och varför central infrastruktur inte automatiskt är en plattform.
