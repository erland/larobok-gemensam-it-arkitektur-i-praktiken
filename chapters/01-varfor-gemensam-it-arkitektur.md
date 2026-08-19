# 1. Varför gemensam IT-arkitektur?

När en organisation är liten kan många tekniska beslut fattas nära den enskilda lösningen. Ett utvecklingsteam väljer hur användare ska autentiseras, hur data lagras, hur loggar samlas in, hur integrationer byggs och hur programvaran ska driftsättas. Så länge antalet system är få och beroendena begränsade kan detta fungera väl. Teamet har korta beslutsvägar, kan optimera för sitt eget behov och behöver sällan ta hänsyn till ett större tekniskt landskap.

I en större organisation förändras problemet. Samma typer av behov återkommer i många verksamhetsområden: identitet, integration, datalagring, dokumenthantering, loggning, övervakning, leverans, återställning, analys, användargränssnitt och informationsutbyte. Om varje team löser dessa behov från grunden uppstår inte bara många lösningar. Det uppstår också många sätt att förstå samma problem, många ansvarssnitt och många tekniska beroenden som måste förvaltas under lång tid.

Gemensam IT-arkitektur handlar därför inte i första hand om att göra systemen lika. Den handlar om att avgöra **vilka problem organisationen bör lösa gemensamt, på vilken nivå de bör lösas och vilka delar som fortsatt bör lämnas till lokala lösningar och domäner**.

Det är en viktig skillnad. En gemensam arkitektur som försöker bestämma allt blir snabbt en central kontrollapparat. En gemensam arkitektur som inte ger någon konkret vägledning lämnar däremot organisationen med samma fragmentering som tidigare. Utmaningen är att hitta den nivå där gemensamma beslut minskar onödig variation utan att ta bort den variation som faktiskt behövs.

Detta kapitel beskriver varför den balansen är nödvändig, vilka problem den gemensamma arkitekturen försöker lösa och vilka risker som uppstår när den själv blir en del av problemet.

## Lokal optimering skapar inte automatiskt en bra helhet

Det finns goda skäl att låta beslut fattas nära den verksamhet och den lösning som berörs. Ett team som känner sin domän kan ofta fatta snabbare och bättre beslut än en central funktion som saknar detaljkunskap. Lokal autonomi kan öka utvecklingstakten, göra ansvar tydligare och ge utrymme för innovation.

Problemet uppstår när ett beslut som är rationellt för ett enskilt team får kostnader någon annanstans i organisationen.

Anta att tre utvecklingsteam behöver kommunicera med externa parter. Det första bygger en egen filöverföringslösning, det andra inför en meddelandeplattform och det tredje exponerar ett API via en lokalt vald gateway. Varje lösning kan vara tekniskt rimlig. Men organisationen behöver därefter hantera tre olika säkerhetsmodeller, tre sätt att övervaka trafiken, tre kompetensprofiler, tre livscykler och tre uppsättningar incidentrutiner.

Det som såg enkelt ut inom varje projekt har blivit komplext på organisationsnivå.

Samma effekt kan uppstå inom nästan alla teknikområden. Om tio systemteam väljer egna mekanismer för secrets-hantering får säkerhetsorganisationen tio olika angreppssätt att granska. Om varje applikation bygger sin egen logginsamling blir central felsökning och spårbarhet svårare. Om varje projekt väljer sin egen CI/CD-modell måste organisationen förvalta många vägar från källkod till produktion. Om varje system gör egna tolkningar av autentisering och auktorisation ökar både risk och kostnad.

Det betyder inte att variation alltid är fel. Olika verksamhetsbehov kan kräva olika lösningar. Det viktiga är att skilja mellan **motiverad variation** och **variation som bara uppstår därför att samma problem har lösts flera gånger utan gemensam riktning**.

Den skillnaden är en av gemensam IT-arkitekturs viktigaste arbetsuppgifter.

## Fragmentering har flera former

När man talar om fragmentering är det lätt att tänka på ett stort antal produkter och tekniker. Produktflora är bara en del av problemet. Fragmentering kan uppstå på flera nivåer samtidigt.

### Teknisk fragmentering

Organisationen använder flera tekniker för samma grundproblem utan att skillnaderna motsvarar olika behov. Resultatet kan bli fler produktversioner, fler integrationsvarianter, fler plattformar och fler specialkonfigurationer att hantera.

Teknisk variation är inte nödvändigtvis negativ. Två olika databastyper kan vara helt motiverade om de löser olika informations- och kvalitetsbehov. Fragmentering uppstår när variationen saknar en tydlig anledning eller när kostnaden för den inte längre är synlig för den som fattar beslutet.

### Operativ fragmentering

Två system kan vara byggda med liknande teknik men ändå förvaltas på helt olika sätt. De kan ha olika modeller för driftsättning, loggning, övervakning, backup, incidenthantering och återställning. Då blir organisationens driftförmåga beroende av lokal kunskap och manuella rutiner.

Operativ fragmentering är ofta mindre synlig än produktfragmentering, men kan vara minst lika dyr. Den märks först när något ska förändras, uppgraderas, felsökas eller återställas.

### Informationsmässig fragmentering

Samma begrepp kan tolkas olika i olika lösningar. Samma information kan kopieras utan tydligt ägarskap. Ett system kan betrakta en viss datakälla som auktoritativ medan ett annat använder en lokal kopia som i praktiken blivit ett eget original.

Detta är inte främst ett plattformsproblem. Men en gemensam IT-arkitektur behöver kunna synliggöra var tekniska lösningar förstärker eller försvårar informationsmässig sammanhållning.

### Säkerhetsmässig fragmentering

Om säkerhetsmekanismer varierar kraftigt mellan lösningar blir det svårt att veta vilka skydd som faktiskt gäller. Autentisering, tjänsteidentiteter, certifikat, secrets, loggning och åtkomstkontroll kan då behöva bedömas separat i varje system.

Gemensamma säkerhetsmekanismer kan minska denna variation, men bara om de bygger på tydliga behov och ansvar. Att införa en gemensam produkt utan en gemensam säkerhetsmodell löser inte problemet.

### Kunskapsmässig fragmentering

Varje unik teknik och lokal speciallösning kräver människor som förstår den. När kunnandet finns hos ett fåtal personer ökar sårbarheten. Ny personal behöver lära sig fler varianter, och team får svårare att hjälpa varandra.

Denna typ av fragmentering gör också organisationen långsammare. Ett problem som redan är löst på ett ställe behöver analyseras igen på ett annat, eftersom lösningen inte är paketerad på ett återanvändbart sätt.

Gemensam IT-arkitektur försöker inte eliminera alla dessa former av variation. Den försöker göra dem **avsiktliga, begripliga och proportionerliga**.

## Återanvändning handlar om mer än kod

När ordet återanvändning används inom IT går tanken ofta till kodbibliotek eller gemensamma komponenter. I en större arkitektur är det bara en del av bilden.

Det som kan återanvändas är även:

- ett sätt att formulera ett återkommande problem,
- ett lösningsmönster,
- en säkerhetsmodell,
- ett tjänstekontrakt,
- en plattformstjänst,
- en standard,
- en teststrategi,
- en kvalitetsprofil,
- en referensarkitektur,
- erfarenhet av vilka avvägningar som brukar vara viktiga.

Detta är ofta mer värdefullt än att återanvända en viss kodbas. Om ett team kan använda en etablerad modell för tjänsteidentitet behöver det inte börja med frågan ”hur brukar vi lösa detta?”. Om det finns en gemensam databastjänst med tydliga ansvar och kvalitetsnivåer behöver varje projekt inte designa drift, backup och övervakning från grunden. Om det finns ett väl beskrivet mönster för asynkron kommunikation kan nya lösningar börja med kända frågor om idempotens, ordering, återförsök och felhantering i stället för att upptäcka dem sent.

Gemensam IT-arkitektur skapar därför värde när den förvandlar återkommande problem till **återanvändbar kunskap och återanvändbara erbjudanden**.

Det innebär också att återanvändning måste bedömas utifrån mer än teknisk möjlighet. En gemensam lösning som är svår att konsumera, har otydligt ansvar eller inte möter viktiga kvalitetskrav kommer att kringgås. Då finns återanvändningen bara på papperet.

## En produktkatalog är inte en arkitektur

Många organisationer har redan listor över godkända produkter, plattformar och tekniker. Sådana kataloger kan vara nödvändiga, men de svarar inte på den viktigaste frågan: **varför finns tekniken och vilket behov är den avsedd att lösa?**

Om den gemensamma arkitekturen börjar i en produktlista blir resonemanget lätt bakvänt.

I stället för att fråga:

> Vilket behov har lösningen och vilka egenskaper måste den uppfylla?

börjar man fråga:

> Vilken av våra befintliga produkter ska användas?

Det kan leda till att produktens egenskaper och begränsningar gradvis omvandlas till generella krav. En plattform råkar exempelvis stödja ett visst sätt att distribuera applikationer, och efter en tid beskrivs detta som om alla verksamhetsbehov naturligt leder till just den modellen. Då har medlet blivit mål.

En mer hållbar gemensam arkitektur behöver skilja mellan relativt stabila frågor och mer föränderliga tekniska svar.

Behov som säker integration, spårbar identitet, robust lagring eller reproducerbar leverans kan finnas under många år. Produkterna som används för att realisera dem kommer däremot att förändras. Om arkitekturens översta nivå binds direkt till produktnamn måste modellen göras om vid varje större teknikskifte.

Bokens fortsatta modell utgår därför från en annan ordning: behov och kvalitetskrav leder till gemensamma IT-förmågor, som kan realiseras genom mönster, plattformstjänster, standarder och tekniska byggblock. Produkter och versioner ligger längre ned och kan förändras snabbare.

Den fullständiga modellen introduceras i nästa kapitel. Här räcker det att konstatera att **stabil arkitektur och föränderlig teknik behöver kunna röra sig i olika takt**.

## Varför tänka i förmågor?

Förmågetänkandet ger ett sätt att beskriva vad organisationen behöver kunna stödja utan att omedelbart låsa sig vid en viss teknisk realisering.

En organisation kan exempelvis behöva kunna:

- hantera identitet och tillit,
- integrera system och utbyta information,
- köra applikationer,
- lagra och hantera data,
- leverera programvara på ett kontrollerat sätt,
- övervaka och återställa tjänster.

Dessa behov finns oberoende av om den aktuella lösningen råkar vara byggd med en viss produkt, köras på en viss plattform eller ägas av ett visst organisatoriskt team.

Det gör förmågan användbar som en relativt stabil navigationspunkt. När tekniken förändras kan organisationen fortfarande fråga: Vad behöver vi kunna erbjuda inom identitet? Vilka typer av integrationsbehov måste vi stödja? Vilka kvaliteter behöver vår exekveringsmiljö kunna leverera?

Förmågor löser dock inte allt. De ersätter inte domänarkitektur, verksamhetsmodellering eller konkreta lösningsbeslut. En förmågekarta säger inte automatiskt hur två verksamhetsdomäner bör avgränsas, vilket system som ska äga en viss informationsmängd eller hur en specifik applikation ska designas.

Det är därför viktigt att använda förmågor som **struktur för gemensamt IT-stöd**, inte som en universell modell för hela organisationens arkitektur.

Vad en IT-förmåga betyder mer exakt, hur den skiljer sig från verksamhetsförmåga, tjänst och produkt samt hur förmågor bör avgränsas behandlas senare i boken.

## Gemensamt betyder inte centraliserat

En vanlig missuppfattning är att allt som är gemensamt också måste ägas och implementeras centralt.

Det behöver inte vara så.

En gemensam standard kan beslutas gemensamt men implementeras av många team. Ett gemensamt mönster kan användas lokalt utan en central plattform. En plattformstjänst kan ha ett gemensamt tjänstekontrakt men drivas federerat. En referensarkitektur kan ge en gemensam utgångspunkt utan att varje lösning blir identisk.

Begreppet gemensam bör därför förstås som att något **behöver fungera sammanhängande över flera delar av organisationen**, inte att alla beslut måste flyttas till en central grupp.

Detta öppnar för flera former av gemensamhet:

- gemensamma principer men lokal implementation,
- gemensamma protokoll och kontrakt,
- gemensamma plattformstjänster,
- gemensamma kvalitetskrav,
- gemensamma lösningsmönster,
- gemensam terminologi och dokumentationsstruktur,
- gemensam livscykelstyrning för utvalda teknikområden.

Vilken form som är lämplig beror på problemet.

Om tio team behöver samma specialiserade infrastruktur kan en gemensam plattform ge tydliga skalfördelar. Om behoven däremot skiljer sig kraftigt kan en gemensam plattform skapa mer friktion än nytta. I vissa fall är det viktigaste bara att systemen använder kompatibla protokoll eller delar samma informationskontrakt.

En mogen gemensam arkitektur behöver därför kunna säga både **”detta bör vi lösa tillsammans”** och **”detta bör få vara lokalt”**.

## Standardisering ska köpa något

Standardisering har en kostnad. Den begränsar valfrihet, kräver förvaltning och kan skapa tröghet om den utformas dåligt. Därför behöver varje standardisering kunna motiveras med vilket värde den skapar.

Det kan exempelvis vara:

- lägre säkerhetsrisk,
- enklare interoperabilitet,
- snabbare onboarding,
- lägre drift- och supportkostnad,
- bättre möjlighet att automatisera,
- mindre beroende av enskilda personer,
- enklare uppgraderingar,
- högre återanvändning,
- bättre spårbarhet och regelefterlevnad.

Om en standard inte längre ger tillräckligt värde behöver den kunna omprövas. Detsamma gäller en gemensam plattform. Den ska inte användas bara för att den är gemensam; den ska användas när den på ett ändamålsenligt sätt möter lösningens behov och kvalitetskrav.

Detta skapar en viktig princip för resten av boken:

> **Gemensamma lösningar är medel för kvalitet, effektivitet och sammanhang – inte mål i sig.**

Det gör också avsteg till en naturlig del av en fungerande arkitektur. Om ett standarderbjudande inte möter ett legitimt behov ska det gå att välja något annat, under tydligt ansvar. Återkommande avsteg är dessutom värdefull information: de kan visa att standarden eller plattformen behöver förändras.

Själva besluts- och avstegsmodellen behandlas längre fram. Här är poängen att en arkitektur som aldrig kan avvikas från lätt blir en källa till lokal kringgång i stället för verklig standardisering.

## Gemensam arkitektur som möjliggörare

Den mest användbara gemensamma arkitekturen märks inte främst genom hur många dokument den producerar. Den märks genom vilka frågor ett team **slipper lösa från början**.

Ett utvecklingsteam bör exempelvis kunna komma in i ett projekt och redan ha svar eller etablerade alternativ för frågor som:

- Hur autentiserar sig användare och tjänster?
- Hur publicerar vi ett API?
- Hur skickar vi meddelanden asynkront?
- Hur hanteras secrets?
- Hur samlas loggar och mätvärden in?
- Hur tar vi applikationen från källkod till produktion?
- Vilka återställningsmekanismer finns?
- Vilka kvalitetsnivåer kan de gemensamma tjänsterna leverera?

Det innebär inte att arkitekturen ska ge ett enda svar på varje fråga. Ibland behövs flera godkända alternativ. Men alternativen bör vara begripliga, deras avvägningar kända och deras ansvar tydliga.

När detta fungerar kan gemensam arkitektur faktiskt **öka teamens autonomi**. Teamet behöver inte vänta på en central arkitekt för varje detaljbeslut, eftersom spelplanen redan är tydlig. Det kan välja inom etablerade ramar och fokusera sin energi på det som är unikt för verksamhetsproblemet.

Det är en annan syn på styrning än att varje projekt ska passera en serie centrala godkännanden. Målet är inte att centralisera beslutsfattandet, utan att göra fler beslut säkra att fatta nära lösningen.

## När gemensam arkitektur blir ett hinder

Samma mekanismer som kan skapa sammanhang kan också skapa problem.

### När standarden blir viktigare än behovet

Om frågan ”följer ni standarden?” kommer före frågan ”vilket behov försöker ni lösa?” har styrningen vänt på orsak och verkan. Team kan då tvingas in i lösningar som formellt är korrekta men funktionellt olämpliga.

### När gemensamma plattformar blir obligatoriska monopol

En gemensam plattform kan vara värdefull så länge den erbjuder en konkurrenskraftig väg att lösa återkommande behov. Om den i stället skyddas från jämförelse med faktiska behov kan den utvecklas till ett hinder. Då får konsumenterna bära plattformens begränsningar utan att plattformsområdet behöver förbättra erbjudandet.

### När abstraktionen blir för grov

Om allt sorteras under ett fåtal breda rubriker kan viktiga skillnader försvinna. ”Integration” är exempelvis inte ett enda problem. Realtids-API:er, eventdriven kommunikation, batchöverföring och myndighetsöverskridande informationsutbyte kan ha helt olika kvalitetskrav.

Gemensam arkitektur måste därför vara tillräckligt stabil för att skapa sammanhang men tillräckligt detaljerad för att leda till meningsfulla beslut.

### När dokumentationen ersätter tjänsten

Att dokumentera att en organisation har en viss förmåga betyder inte att förmågan faktiskt fungerar. Om det finns ett dokument om CI/CD men varje team ändå måste bygga sin egen leveranskedja från grunden är det gemensamma stödet svagt. Om API Management finns som rubrik men saknar tydlig onboarding, support och ansvar är det mer en teknisk komponent än ett fungerande tjänsteerbjudande.

Det är därför boken senare skiljer mellan förmåga, lösningsmönster, plattformstjänst, standard och tekniskt byggblock. De beskriver olika saker och kan inte ersätta varandra.

### När arkitekturen inte kan förändras

Tekniklandskap, verksamhetsbehov och externa krav förändras. En gemensam arkitektur som inte kan ompröva sina standarder och erbjudanden kommer förr eller senare att skydda historiska beslut i stället för att stödja organisationens behov.

Stabilitet betyder därför inte oföränderlighet. Det betyder att olika delar av arkitekturen får förändras i olika takt och att förändring sker med förståelse för konsekvenserna.

## Ett konkret exempel: tre team, samma återkommande problem

Tänk dig en större organisation med tre utvecklingsinitiativ:

1. ett internt handläggningsstöd,
2. en publik e-tjänst,
3. ett system för informationsutbyte med en extern organisation.

Verksamhetsbehoven skiljer sig. Det första behöver stödja handläggare och långlivade ärenden. Det andra behöver vara tillgängligt för externa användare och hantera varierande belastning. Det tredje behöver säkra och spårbara informationsflöden över en organisatorisk gräns.

Trots skillnaderna finns återkommande tekniska frågor.

Alla tre behöver identitet, loggning, övervakning, leverans och någon form av datalagring. Två av dem behöver sannolikt API-hantering. Minst två behöver tjänsteidentiteter. Alla behöver kunna återställas efter fel. De behöver kanske olika integrationsmönster, men de behöver gemensamma principer för hur kontrakt, säkerhet och spårbarhet hanteras.

Utan gemensam arkitektur kan varje initiativ börja om från början. Det ger hög lokal frihet men också stor risk för dubbelarbete och inkompatibla lösningar.

Med en alltför centraliserad arkitektur kan de i stället tvingas in i samma tekniska modell trots att behoven skiljer sig.

En mer balanserad modell gör något annat. Den identifierar vilka **förmågor och kvaliteter** som återkommer, erbjuder gemensamma mönster och tjänster där de ger värde och lämnar lösningsspecifika beslut till respektive team.

Handläggningsstödet kan exempelvis använda ett gemensamt workflow-erbjudande medan e-tjänsten inte gör det. Båda kan använda samma identitets- och loggningstjänster. Informationsutbytet kan behöva en särskild kommunikationslösning men ändå följa gemensamma principer för identitet, spårbarhet och förvaltning.

Det är denna kombination av **gemensam grund och motiverad lokal variation** som boken kommer att utveckla vidare.

## Tre nivåer behöver kunna samspela

Redan här är det användbart att skilja mellan tre nivåer, även om ansvarsfördelningen fördjupas senare.

På en **gemensam arkitekturnivå** behöver organisationen hålla ihop sådant som måste vara konsekvent över flera områden: grundläggande begrepp, övergripande principer, kvalitetsdimensioner och ramen för vilka gemensamma förmågor som finns.

På **förmågenivå** kan ansvariga för exempelvis integration, identitet eller applikationsexekvering utveckla relevanta lösningsmönster, tjänsteerbjudanden, standarder och vägledning.

På **lösnings- och produktnivå** kombinerar team dessa byggstenar med domänspecifika komponenter för att lösa ett konkret verksamhetsbehov.

Ingen av nivåerna kan ersätta de andra.

Om den gemensamma nivån försöker detaljdesigna varje lösning blir den en flaskhals. Om förmågeområdena saknar mandat att utveckla sina erbjudanden blir arkitekturen statisk. Om lösningsteamen ignorerar gemensamma byggstenar försvinner skalfördelarna och sammanhanget.

Den praktiska frågan blir därför inte ”centralt eller lokalt?” utan **vilka beslut hör hemma på vilken nivå?**

Boken återkommer till detta genomgående.

## Hur vet man att den gemensamma arkitekturen fungerar?

Det går att producera många arkitekturdokument utan att förbättra organisationens förmåga att utveckla och förvalta IT-stöd. En bättre fråga är vilka beteenden och effekter man vill se.

Tecken på en fungerande gemensam arkitektur kan vara att:

- team snabbare hittar etablerade sätt att lösa återkommande problem,
- samma säkerhets- och driftfrågor inte behöver återuppfinnas i varje projekt,
- gemensamma tjänster har tydliga ansvar och är möjliga att konsumera utan omfattande specialhjälp,
- tekniska avvikelser är motiverade av verkliga behov snarare än okunskap om befintliga alternativ,
- det går att förstå varför en viss standard eller plattform finns,
- återkommande avsteg leder till förbättring av gemensamma erbjudanden,
- teknik kan bytas utan att hela den övergripande arkitekturmodellen måste ritas om,
- lösningsteam har frihet inom tydliga ramar i stället för frihet genom frånvaro av ramar.

Detta är i grunden tecken på **minskad onödig komplexitet och bättre beslutsförmåga**.

Gemensam IT-arkitektur är alltså inte framgångsrik för att många system använder samma produkt. Den är framgångsrik när organisationen kan hantera återkommande problem konsekvent, göra avvägningar medvetet och ändå låta verkliga skillnader i behov få påverka lösningen.

## Från problembild till modell

Vi har nu etablerat varför en större organisation behöver något mer än en samling lokala lösningar och en katalog över godkända produkter.

Gemensam IT-arkitektur behövs för att:

- minska onödig variation,
- återanvända kunskap och tekniska erbjudanden,
- göra ansvar och gränssnitt tydligare,
- hantera tvärgående kvaliteter konsekvent,
- skilja långlivade behov från kortlivade teknikval,
- skapa autonomi inom begripliga ramar.

Men detta säger ännu inte **hur arkitekturen ska struktureras**.

Om behov, förmågor, mönster, plattformar, standarder, byggblock och produkter blandas ihop blir dokumentationen svår att navigera och styrningen svår att förändra. Nästa steg är därför att skapa en modell där varje typ av arkitekturinnehåll har en tydlig roll och en lämplig förändringstakt.

Det är ämnet för nästa kapitel: **En arkitektur av flera lager**.

## Centrala fakta

- Gemensam IT-arkitektur ska minska onödig variation, inte all variation.
- Lokal optimering kan skapa kostnader och risker på organisationsnivå även när varje enskilt teknikval är rimligt.
- Fragmentering kan vara teknisk, operativ, informationsmässig, säkerhetsmässig och kunskapsmässig.
- Återanvändning omfattar inte bara kod utan även mönster, kunskap, tjänstekontrakt, standarder och kvalitetsprofiler.
- En produktkatalog beskriver tekniska val men förklarar inte i sig vilka behov eller förmågor de ska stödja.
- Förmågor ger en stabilare ingång än produkter, men ersätter inte domänarkitektur eller konkreta lösningsbeslut.
- Gemensamt är inte synonymt med centraliserat. Gemensamma principer och kontrakt kan kombineras med lokal eller federerad implementation.
- Standardisering ska ge ett tydligt värde. Om den inte längre gör det behöver standarden kunna omprövas.
- En bra gemensam arkitektur gör fler beslut möjliga att fatta nära lösningen eftersom spelplan, alternativ och ansvar är tydliga.
- Boken skiljer mellan gemensam arkitekturnivå, förmågenivå och lösnings-/produktnivå. De tre nivåerna behöver samspela utan att detaljstyra varandra.

## Begrepp att känna till

**Gemensam IT-arkitektur**  
En sammanhängande modell av principer, förmågor, mönster, tjänster, standarder och andra arkitekturartefakter som används för problem och behov som berör flera delar av organisationens IT-landskap.

**Lokal optimering**  
När ett beslut förbättrar situationen för ett enskilt team, system eller område men samtidigt kan skapa kostnader, risker eller komplexitet för helheten.

**Motiverad variation**  
Skillnader i lösning som kan härledas till verkliga skillnader i behov, kvalitetskrav, risk eller andra relevanta förutsättningar.

**Fragmentering**  
När likartade behov hanteras på många sinsemellan olika sätt utan att variationen ger motsvarande verksamhets- eller kvalitetsvärde.

**Återanvändning**  
Att använda tidigare etablerad kunskap, mönster, komponenter, plattformstjänster, standarder eller andra byggstenar för att slippa lösa samma problem från grunden.
