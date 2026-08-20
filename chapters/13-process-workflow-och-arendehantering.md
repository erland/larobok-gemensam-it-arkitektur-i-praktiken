# 13. Process, workflow och ärendehantering

Många verksamhetssystem innehåller någon form av flöde. Ett ärende skapas, information kompletteras, någon granskar, ett beslut fattas och resultatet expedieras. En beställning tas emot, kontrolleras, skickas vidare och avslutas. Ett automatiserat flöde väntar på svar från ett annat system innan nästa steg kan börja.

Det betyder inte att varje sådant flöde behöver en processmotor.

En av de viktigaste arkitekturfrågorna inom denna förmåga är därför inte *hur* en workflowplattform används, utan när process, workflow eller ärendehantering bör behandlas som en explicit förmåga i lösningen och när vanlig domänlogik är ett bättre val.

Det är först när svaret på den frågan är tydligt som tekniska val blir meningsfulla.

Förmågan *Process, workflow och ärendehantering* handlar om att stödja verksamhetsförlopp som behöver hållas ihop över tid, ofta över flera aktiviteter, aktörer och system. Den blir särskilt relevant när tillståndet i ett flöde måste vara synligt, återupptagningsbart, spårbart eller möjligt att förändra som en sammanhängande process.

Typiska behov är att:

- hålla ihop ett ärende under timmar, dagar, månader eller längre,
- kombinera automatiserade steg med mänskliga arbetsuppgifter,
- vänta på externa svar eller händelser utan att hålla en teknisk session öppen,
- hantera deadlines, timers, påminnelser och eskaleringar,
- fördela arbete mellan roller eller organisatoriska enheter,
- visa var i ett verksamhetsförlopp ett ärende befinner sig,
- återuppta ett flöde efter tekniska avbrott,
- hantera redan startade processinstanser när processdefinitionen förändras,
- samordna aktiviteter i flera system utan att göra processmotorn till generell integrationsplattform.

Förmågan ligger därmed i gränslandet mellan verksamhetslogik, mänskligt arbete, integration, data och driftbarhet. Just därför behöver dess ansvar avgränsas noggrant.

## När processen behöver bli explicit

All programvara innehåller kontrollflöde, men det gör inte lösningen till ett workflow. Det är användbart att skilja mellan lokalt kontrollflöde i kod, domänens tillstånd och livscykel samt ett explicit verksamhetsflöde som koordinerar aktiviteter över tid.

En ansökan som registreras, valideras och accepteras eller avvisas inom samma domän kan ofta hanteras med vanlig applikationskod eller en enkel tillståndsmaskin. Om samma ansökan däremot ska kunna vänta på komplettering, tilldelas en handläggare, eskaleras efter en tidsfrist, återupptas efter flera releaser och följas av verksamheten har själva förloppet blivit ett arkitekturproblem.

Det avgörande är alltså inte antalet steg utan vilka egenskaper förloppet behöver ha. Processens tillstånd behöver bli explicit när verksamhet, support eller revision måste kunna svara på frågor som vilka ärenden som väntar, vilka deadlines som passerats, var ett flöde stannade eller vilken processversion en pågående instans använder.

Statusen behöver inte ligga i en särskild processmotor, men arkitekturen måste behandla processens livscykel som något mer än dold kontrolllogik. En användbar tumregel är:

> Ju viktigare det är att kunna observera, återuppta och förvalta själva förloppet oberoende av en enskild kodväg, desto starkare är skälet att modellera processen explicit.

## Långlivade processer förändrar arkitekturproblemet

En vanlig HTTP-förfrågan lever kanske några hundra millisekunder eller sekunder. En affärstransaktion i en databas bör normalt vara ännu kortare.

Ett verksamhetsförlopp kan däremot leva i månader.

Det innebär att en långlivad process inte kan byggas som om den vore en lång teknisk transaktion. Den måste kunna vänta utan att hålla resurser låsta.

Anta ett flöde:

1. ett ärende registreras,
2. en extern part får en begäran om komplettering,
3. processen väntar på svar,
4. efter 14 dagar skickas en påminnelse,
5. efter 30 dagar sker eskalering,
6. när svaret kommer fortsätter handläggningen.

Mellan steg 2 och 6 ska ingen applikationstråd, nätverksanslutning eller databastransaktion behöva vara aktiv. Det som behöver överleva är i stället processens tillstånd och den information som krävs för att återuppta den.

Detta leder till en central princip för förmågan:

Verksamhetsprocessens livslängd får inte kopplas till livslängden hos en enskild teknisk exekvering.

Det ställer krav på bland annat:

- persistens av processstatus,
- robust hantering av timers,
- korrelation mellan externa händelser och rätt processinstans,
- idempotens när steg kan behöva göras om,
- hantering av delvisa fel,
- versionshantering av processdefinitioner,
- observerbarhet och felsökning över lång tid.

Här möter processförmågan andra förmågor. Meddelanden och events hör hemma i *Integration och kommunikation*. Lagring av verksamhetsinformation hör hemma i Data- och informationshantering. Återstart, övervakning och felhantering berör Driftbarhet och motståndskraft. Processförmågan använder dessa mekanismer för att hålla ihop verksamhetsförloppet.

## Workflow och mänskliga arbetsuppgifter

Workflow blir särskilt relevant när människor är aktiva deltagare i processen.

En mänsklig arbetsuppgift är mer än att visa en knapp i ett användargränssnitt. Den kan behöva innehålla information om:

- vad som ska göras,
- vem eller vilken roll som får göra det,
- när uppgiften skapades,
- prioritet,
- deadline,
- eventuell kö eller organisatorisk tillhörighet,
- vilka uppgifter som krävs för att utföra arbetet,
- vilket resultat som ska lämnas tillbaka,
- vad som händer om ingen agerar.

Därmed uppstår arkitekturfrågor kring arbetsfördelning.

Ska uppgiften tilldelas en namngiven person, en roll eller en gemensam kö? Kan en handläggare plocka nästa uppgift själv? Ska en arbetsledare kunna omfördela? Hur påverkas uppgiften om en användare byter organisatorisk enhet? Hur hanteras frånvaro? Behöver vissa uppgifter göras av två olika personer enligt fyrögonsprincip?

Sådana frågor ska inte lösas av workflowplattformen ensam. De är ofta en kombination av:

- processlogik,
- identitets- och behörighetsregler,
- organisatoriska regler,
- verksamhetsregler,
- användargränssnitt.

Processförmågan behöver däremot erbjuda mekanismer som gör dessa samband möjliga att uttrycka utan att varje lösning bygger en ny arbetskömodell från grunden.

## Process, workflow och case management är inte samma sak

Begreppen används ibland som synonymer, men de representerar olika tyngdpunkter.

### Process

En process betonar normalt ett förlopp med aktiviteter och övergångar. Det finns någon form av struktur för hur arbetet rör sig från start mot ett eller flera möjliga slut.

Vissa processer är strikt sekventiella. Andra innehåller parallella grenar, väntelägen, loopar och alternativa vägar.

### Workflow

Workflow används ofta när fokus ligger på arbetsflödet och koordineringen av aktiviteter, inte minst mänskliga uppgifter. I praktiken överlappar workflow och processautomation mycket.

### Case management

Case management blir relevant när arbetet i mindre grad kan beskrivas som en förutbestämd sekvens.

Ett ärende kan i stället fungera som en sammanhållande kontext där olika aktiviteter blir möjliga beroende på:

- vilken information som finns,
- vilka händelser som inträffat,
- professionell bedömning,
- regler,
- ärendets aktuella situation.

I ett sådant fall kan det vara viktigare att beskriva vilka aktiviteter som är möjliga och under vilka villkor än att ange en komplett väg genom processen i förväg.

Skillnaden kan illustreras förenklat:

**Processorienterat:**

> Gör A, därefter B. Om villkor X gäller, gör C, annars D.

**Case-orienterat:**

> I detta ärende kan A, B och C behöva göras. Vilken aktivitet som är lämplig beror på ärendets information, händelser och handläggarens bedömning.

I verkligheten innehåller många verksamhetssystem båda formerna. Ett ärende kan ha ett övergripande livscykelflöde men samtidigt ge handläggaren frihet inom vissa delar.

Arkitekturen bör därför inte försöka pressa allt arbete in i ett strikt processdiagram bara för att verktyget stödjer det.

## Standardiserade notationer kan hjälpa – men är inte arkitekturen

För verksamhetsprocesser finns etablerade modelleringsnotationer. BPMN, Business Process Model and Notation, är en standardiserad grafisk notation för att beskriva verksamhetsprocesser. För case management finns CMMN, Case Management Model and Notation, som fokuserar på modellering av cases och mer situationsstyrt arbete.[K1][K2]

Notationerna kan bidra med ett gemensamt språk mellan verksamhets- och teknikroller. De kan också göra processmodeller mer portabla mellan verktyg än helt leverantörsspecifika diagram.

Men tre saker behöver hållas isär:

1. en notation för att beskriva ett flöde,
2. en exekverbar processdefinition,
3. den faktiska lösningsarkitekturen.

Ett BPMN-diagram är inte automatiskt en bra exekverbar process, och en exekverbar processmodell är inte automatiskt en bra domänarkitektur.

Det är därför riskabelt att utgå från frågan:

> Hur modellerar vi hela verksamheten i processmotorn?

Bättre är:

> Vilka delar av verksamhetsförloppet tjänar på att vara explicita och exekverbara, och vilka delar bör ligga kvar i domäntjänster, regeltjänster eller mänsklig bedömning?

## Två viktiga gränser för processplattformen

En process behöver ofta avgöra vad som ska hända härnäst, men den bör inte därför absorbera all verksamhetslogik. Flödet kan exempelvis uttrycka att ett godkänt resultat leder vidare till registrering, medan logiken som avgör *om* resultatet är godkänt hör hemma i en domäntjänst eller i förmågan *Regler och beslut*.

Processen bör främst äga ordning, väntan, koordinering, övergångar, deadlines, arbetsuppgifter och återupptagning. Domän- och regeltjänster bör äga verksamhetsinvarianter, beräkningar, beslutskriterier och auktoritativa förändringar av verksamhetsobjekt. Gränsen är inte absolut, men stora mängder skript och leverantörsspecifik kod i processmodellen gör den snabbt till en verksamhetsmonolit.

På samma sätt ska processmotorn inte bli generell integrationsplattform. En process kan uttrycka *begär registerkontroll och vänta på resultat*, men autentisering, kontrakt, routing och teknisk övervakning av registerkontrollen hör främst hemma i *Integration och kommunikation*.

Processplattformen bör därför konsumera standardiserade integrationsmekanismer snarare än ersätta dem. Det gör både processen och integrationerna lättare att återanvända, testa och förvalta.

## Orkestrering och koreografi

När flera tjänster deltar i ett verksamhetsförlopp finns två vanliga sätt att koordinera dem.

### Orkestrering

Vid orkestrering finns en komponent som explicit håller ihop flödet och avgör vilka aktiviteter som ska ske.

Förenklat:

```text
Process
   ├── anropa tjänst A
   ├── vänta på resultat
   ├── anropa tjänst B
   └── skapa arbetsuppgift
```

Fördelen är att det blir tydligt var helhetsflödet finns och hur dess status följs.

Nackdelen är att orkestratorn kan bli starkt kopplad till många domäner och gradvis samla på sig verksamhetslogik som egentligen borde ligga någon annanstans.

### Koreografi

Vid koreografi reagerar deltagarna i stället på händelser utan att en central komponent behöver känna till hela sekvensen.

Förenklat:

```text
Tjänst A publicerar händelse
        ↓
Tjänst B reagerar och publicerar ny händelse
        ↓
Tjänst C reagerar
```

Det kan minska central koppling och passa väl när domäner är självständiga.

Samtidigt kan ett långt koreograferat verksamhetsförlopp bli svårt att observera och förstå. Helheten finns då utspridd över flera tjänsters beteenden.

Valet är därför inte ideologiskt. Frågan är vilken egenskap som behöver optimeras.

Om verksamheten behöver ett explicit sammanhållet processläge, mänskliga uppgifter, deadlines och tydlig återupptagning talar mycket för någon form av orkestrering. Om självständiga domäner främst behöver reagera på varandras händelser kan koreografi vara lämpligare.

Ofta används båda i samma arkitektur.

## Ärendestatus och verksamhetsdata måste hållas isär

En workflowplattform behöver lagra data för att veta vad den väntar på och vilket steg som är aktivt.

Det skapar en klassisk risk: processmotorns interna datalager börjar gradvis användas som verksamhetens databas.

Anta ett handläggningsärende. Processmotorn kan behöva känna till:

- ärende-id,
- aktuell processversion,
- aktiv aktivitet,
- väntande timer,
- korrelations-id,
- tilldelad arbetskö.

Men själva verksamhetsobjektet kan innehålla:

- sökandens uppgifter,
- materiella bedömningar,
- registrerade dokument,
- ekonomiska belopp,
- rättsliga grunder,
- beslutsinformation.

Det senare bör normalt ha ett tydligt informationsägarskap utanför processmotorns interna tillstånd.

Poängen är inte att processmotorn aldrig får bära verksamhetsdata. Den behöver ofta ett arbetsunderlag och variabler för att styra flödet. Men arkitekturen bör kunna svara på:

> Om processplattformen byts ut, var finns den auktoritativa verksamhetsinformationen då?

Om svaret är ”bara inne i processmotorn” kan en teknisk stödplattform oavsiktligt ha blivit system of record för en verksamhetsdomän.

Det är just den sammanblandningen kapitel 11 varnade för ur informationsperspektiv och som kapitel 15 senare fördjupar ur tekniskt datahanteringsperspektiv.

## Livscykel, versionering och återhämtning

Långlivade processer kan överleva många applikationsreleaser. En instans som har pågått i månader kan därför fortfarande följa en äldre processdefinition när en ny version driftsätts. Organisationen behöver då ta ställning till om pågående instanser ska fortsätta på sin gamla version, migreras kontrollerat eller stödjas parallellt under en övergångstid. Valet beror på processens semantik, livslängd och risk; någon universell strategi finns inte.

Samma långlivade karaktär gör att processen inte kan förlita sig på en enda ACID-transaktion över alla deltagande system. Om ett flöde har lyckats i system A och B men misslyckas i C kan återhämtningen behöva bestå av återförsök, väntan på manuell åtgärd, kompensation eller eskalering. En kompensation är dessutom ofta en ny verksamhetshändelse, till exempel en avbokning, snarare än en teknisk återställning som låtsas att det första steget aldrig skedde.

Processmotorn kan hålla reda på läget och koordinera återhämtningen, men den skapar inte atomiska transaktioner mellan självständiga verksamhetssystem.

För ärendehantering tillkommer behovet av ett tydligt livscykelbegrepp. Ärendets verksamhetsstatus, processens exekveringsstatus, arbetsuppgifternas status, dokumentens status och beslutens status representerar olika saker. Ett ärende kan exempelvis vara *Under handläggning* samtidigt som processen väntar på en timer och en arbetsuppgift ännu inte är tilldelad.

Därför bör ärendelivscykeln definieras i domän- och informationsmodellen, medan workflowmotorns tekniska status hålls separat. Det minskar risken att ett enda statusfält får bära flera oförenliga betydelser.

## När räcker vanlig domänlogik?

Den kanske viktigaste kompetensen inom processförmågan är att kunna säga nej till processmotorn.

En workflowplattform innebär alltid kostnader:

- ytterligare runtime och drift,
- nytt modellerings- och programmeringsparadigm,
- kompetensbehov,
- felsökning över flera lager,
- processversionshantering,
- koppling till en produkt eller exekveringsmodell,
- risk för dubblering mellan processkod och domänkod.

En vanlig applikation är därför ofta bättre när:

- flödet är kortlivat,
- processen sker inom en tydlig domän,
- ingen mänsklig arbetskö behöver hanteras,
- ingen lång väntan behöver persistenteras,
- processstatus inte behöver vara ett eget verksamhetsobjekt,
- ingen särskild processuppföljning krävs,
- förändringstakten för flödet följer vanlig kodrelease,
- robust återupptagning kan lösas enklare med applikationens vanliga mekanismer.

Exempelvis behöver inte en vanlig beställnings-API-metod som validerar indata, sparar ett objekt och returnerar ett svar modelleras som en process bara för att aktiviteterna råkar ske i en viss ordning.

Det centrala kriteriet är nytta i förhållande till den extra abstraktionen.

## När en gemensam workflow- eller processplattform är motiverad

Kapitel 9 visade att ett gemensamt ansvar bör motiveras av återkommande behov, risk, specialistkompetens, interoperabilitet och standardiserbarhet.

Samma resonemang gäller här.

En gemensam workflow-/processplattform är särskilt intressant när många lösningar behöver liknande mekanismer för:

- långlivad processpersistens,
- timers och deadlines,
- human tasks,
- arbetsköer,
- processhistorik,
- versionshantering,
- korrelation av externa händelser,
- återupptagning efter fel,
- gemensam drift och observerbarhet.

Då kan det vara ineffektivt att varje team bygger sin egen enklare workflowmotor ovanpå databas, schemaläggare och messaging.

Men plattformen bör erbjudas som en konsumerbar tjänst för ett tydligt behov, inte som obligatorisk standard för all applikationslogik.

Ett moget erbjudande behöver därför beskriva både:

- när plattformen bör användas,
- när den inte bör användas.

Det senare är minst lika viktigt.

## Förmågan på de tre ansvarsnivåerna

Den gemensamma arkitekturen bör ange gränserna mot integration, regler, data och identitet samt gemensamma krav på exempelvis säkerhet, spårbarhet och driftbarhet. Den bör däremot normalt inte modellera verksamhetens konkreta processer.

Förmågeområdet bör utveckla kriterier för när workflowplattform ska användas, återanvändbara process- och case management-mönster, plattformserbjudanden, stöd för human tasks, versionering, återupptagning och observerbarhet samt golden paths för robust användning.

Lösnings- eller produktnivån äger den konkreta verksamhetsprocessen: domänens tillstånd och regler, vilka delar som behöver modelleras explicit, informationsbehovet och hur fel, deadlines, kompensation och processversioner hanteras i den aktuella kontexten.

Ansvarsfördelningen gör att den gemensamma förmågan kan minska lokal specialutveckling utan att flytta verksamhetskunskapen in i en central processplattform.

## Typiska kvalitetsattribut för förmågan

Processförmågan berör många av bokens kvalitetsdimensioner, men några blir särskilt tydliga.

### Tillgänglighet och kontinuitet

En processplattform kan vara otillgänglig utan att verksamhetsprocessen får förlora sitt läge. Kravet är därför ofta mindre ”varje exekvering måste alltid lyckas omedelbart” och mer ”processen ska kunna fortsätta korrekt när tjänsten åter är tillgänglig”.

### Korrekthet och spårbarhet

Det måste gå att förstå vilka steg som faktiskt utförts, vilka beslut eller resultat som styrt vägen och vad som återstår.

### Förvaltningsbarhet

Processdefinitioner, connectors, formulärkopplingar och regler får inte bilda ett leverantörsspecifikt nät av beroenden som ingen kan förändra säkert.

### Säkerhet

Arbetsuppgifter, processdata och historik kan innehålla skyddsvärd information. Behörighet behöver därför gälla både vem som får se ett ärende och vem som får utföra en viss aktivitet.

### Interoperabilitet

Processen behöver ofta samverka med många andra tjänster. Det gör tydliga kontrakt och standardiserade integrationsmekanismer centrala.

### Livscykel

Processinstanser kan leva längre än en applikationsversion. Det ställer ovanligt tydliga krav på bakåtkompatibilitet och versionsstrategi.

## Vanliga anti-patterns

Några återkommande problem är särskilt värda att känna igen.

### Allt blir workflow

Eftersom plattformen finns börjar även trivial applikationslogik modelleras som processer. Resultatet blir mer komplexitet utan motsvarande nytta.

### Processmotorn blir verksamhetsmonolit

Regler, beräkningar, integration, formulärlogik och verksamhetsdata samlas i samma processmodell. Plattformen blir då svår att ersätta och processerna svåra att testa.

### Processmotorn blir system of record

Processvariabler börjar användas som primär lagring av verksamhetsinformation trots att informationen har en egen livscykel och ägare.

### Processmotorn blir integrationsnav

Alla externa anrop byggs som leverantörsspecifika connectors inne i workflowplattformen, vilket skapar dold integration och stark koppling.

### Ingen strategi för pågående instanser

En ny processversion driftsätts utan att någon har bestämt vad som händer med de hundratals instanser som redan kör den gamla modellen.

### Processdiagrammet förväxlas med verkligheten

Modellen blir mer detaljerad än den verksamhet den försöker beskriva. Människor börjar arbeta runt processen eftersom modellen inte rymmer verkliga undantag.

### Human tasks blir bara tekniska köposter

Arbetsfördelning implementeras utan tydligt ansvar för prioritering, roll, organisatorisk kontext och verksamhetsregler.

## En praktisk analysordning

När ett utvecklingsområde överväger workflow, processmotor eller case management kan följande ordning användas.

### 1. Beskriv verksamhetsförloppet utan att välja teknik

Vilket resultat ska uppnås? Vilka aktörer och domäner deltar? Var finns väntan, manuella steg och externa beroenden?

### 2. Identifiera det som behöver överleva över tid

Vilket tillstånd måste finnas kvar efter omstart, driftsättning eller lång väntan?

### 3. Avgör om processen behöver vara explicit

Behöver verksamheten kunna se, styra, analysera eller förändra själva förloppet som en sammanhängande enhet?

### 4. Separera process, domän och regler

Vad är koordinering och ordning? Vad är verksamhetslogik? Vad är ett självständigt beslut eller regelverk?

### 5. Identifiera mänskligt arbete

Finns arbetsköer, roller, tilldelning, deadlines eller eskalering som behöver gemensamt stöd?

### 6. Analysera fel och väntan

Vad händer om externa tjänster är nere i minuter, timmar eller dagar? Hur återupptas processen? Krävs återförsök, kompensation eller manuell hantering?

### 7. Definiera informationsägarskap

Vilken information är bara processstatus och vilken är auktoritativ verksamhetsinformation?

### 8. Planera versionshanteringen

Vad händer med redan startade instanser när modellen ändras?

### 9. Jämför med enklare lösning

Vilka problem skulle faktiskt bli svårare om flödet implementerades i vanlig applikationskod? Om svaret är ”inga”, behövs sannolikt ingen processmotor.

### 10. Välj gemensamt erbjudande först när behovet motiverar det

Om en etablerad plattform möter kraven bör den normalt återanvändas. Men plattformens existens är inte i sig ett behov.

## Förmågan som konsumerbart stöd

Ett välutvecklat förmågeområde bör inte bara kunna säga ”vi har en workflowmotor”.

Det bör kunna erbjuda ett sammanhängande stöd som exempelvis omfattar:

- vägledning för när processplattform ska användas,
- gemensam runtime för långlivade processer,
- stöd för timers och väntelägen,
- human task- och arbetsköfunktioner,
- standardiserad integration mot identitet och behörighet,
- observerbarhet för processinstanser,
- versions- och deploystrategier,
- exempel och golden paths,
- stöd för robust korrelation och återupptagning,
- tydliga gränser för vad konsumenten själv ansvarar för.

Det är först då det finns ett plattformserbjudande snarare än bara en installerad produkt.

Den underliggande tekniken kan bytas över tid. Förmågan består så länge organisationen återkommande behöver kunna hålla ihop långlivade verksamhetsförlopp, mänskligt arbete och återupptagningsbar koordinering.

## Sammanfattning

Process, workflow och ärendehantering blir en egen arkitekturförmåga när själva verksamhetsförloppet behöver vara explicit, långlivat, observerbart, återupptagningsbart eller samordnat över flera aktörer och system.

Det behöver inte innebära att varje sekvens i ett system ska modelleras i en processmotor. Vanlig domänlogik är ofta enklare och bättre för kortlivade lokala flöden.

Den viktigaste gränsdragningen är därför:

- processen håller ihop ordning, väntan, övergångar och arbetsuppgifter,
- domäntjänster äger verksamhetsbeteende och auktoritativa tillståndsförändringar,
- Regler och beslut kan äga beslut som behöver uttryckas och förvaltas oberoende av processen,
- Integration och kommunikation tillhandahåller mekanismerna för kommunikation mellan system,
- Data- och informationshantering äger de tekniska mekanismerna för verksamhetsinformationens beständighet,
- Identitet och tillit avgör vem eller vad som får utföra aktiviteter.

När dessa ansvar hålls isär kan en workflowplattform ge stor nytta: gemensam hantering av långlivat tillstånd, human tasks, timers, processhistorik och återupptagning. När gränserna suddas ut riskerar samma plattform i stället att bli en ny verksamhetsmonolit.

Nästa kapitel går vidare till en av de viktigaste gränserna: Regler och beslut. Där flyttas fokus från *vilket steg som ska ske härnäst* till *hur ett beslut eller en regel uttrycks, versionshanteras, förklaras och kan användas oberoende av ett enskilt processflöde*.

## Källor och vidare läsning

**[K1]** Object Management Group (OMG), *Business Process Model and Notation (BPMN) 2.0.2*. https://www.omg.org/spec/BPMN/2.0.2

**[K2]** Object Management Group (OMG), *Case Management Model and Notation (CMMN) 1.1*. https://www.omg.org/spec/CMMN/1.1
