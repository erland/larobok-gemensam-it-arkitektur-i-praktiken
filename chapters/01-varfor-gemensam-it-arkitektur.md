# 1. Varför gemensam IT-arkitektur?

När en organisation är liten kan många tekniska beslut fattas nära den enskilda lösningen. Ett utvecklingsteam väljer hur användare autentiseras, hur data lagras, hur loggar samlas in, hur integrationer byggs och hur programvaran driftsätts. Så länge antalet system är få och beroendena begränsade kan det fungera väl.

I en större organisation förändras problemet. Samma behov återkommer i många verksamhetsområden: identitet, integration, datalagring, dokumenthantering, loggning, övervakning, leverans, återställning, analys, användargränssnitt och informationsutbyte. Om varje team löser dem från grunden uppstår inte bara många tekniska lösningar, utan också många ansvarssnitt, arbetssätt och beroenden som måste förvaltas under lång tid.

Gemensam IT-arkitektur handlar därför inte främst om att göra systemen lika. Den handlar om att avgöra vilka problem organisationen bör lösa gemensamt, på vilken nivå det ska ske och vilken variation som fortsatt behöver finnas lokalt.

Balansen är central. En gemensam arkitektur som försöker bestämma allt blir en kontrollapparat. En arkitektur som inte ger konkret vägledning lämnar däremot organisationen med samma fragmentering som tidigare. Målet är att minska onödig variation utan att ta bort den variation som verkliga behov kräver.

## Lokal optimering skapar inte automatiskt en bra helhet

Det finns goda skäl att låta beslut fattas nära den verksamhet och lösning som berörs. Ett team som känner sin domän kan ofta fatta snabbare och bättre beslut än en central funktion som saknar detaljkunskap. Lokal autonomi kan öka utvecklingstakten, göra ansvar tydligare och skapa utrymme för innovation.

Problemet uppstår när ett beslut som är rationellt för ett enskilt team får kostnader någon annanstans i organisationen.

Anta att tre utvecklingsteam behöver kommunicera med externa parter. Det första bygger en egen filöverföringslösning, det andra inför en meddelandeplattform och det tredje exponerar ett API via en lokalt vald gateway. Varje lösning kan vara tekniskt rimlig. Men organisationen behöver därefter hantera tre säkerhetsmodeller, tre sätt att övervaka trafiken, tre kompetensprofiler, tre livscykler och tre uppsättningar incidentrutiner.

Det som såg enkelt ut inom varje projekt har blivit komplext på organisationsnivå.

Samma effekt kan uppstå inom nästan alla teknikområden. Om tio systemteam väljer egna mekanismer för secrets-hantering får säkerhetsorganisationen tio angreppssätt att granska. Om varje applikation bygger sin egen logginsamling blir central felsökning och spårbarhet svårare. Om varje projekt väljer sin egen CI/CD-modell måste organisationen förvalta många vägar från källkod till produktion.

Det betyder inte att variation alltid är fel. Olika verksamhetsbehov kan kräva olika lösningar. Den viktiga frågan är om variationen är motiverad eller bara har uppstått därför att samma problem har lösts flera gånger utan gemensam riktning.

## Fragmentering har flera former

Produktflora är bara en del av problemet. Fragmentering kan uppstå på flera nivåer samtidigt.

### Teknisk fragmentering

Organisationen använder flera tekniker för samma grundproblem utan att skillnaderna motsvarar olika behov. Resultatet kan bli fler produktversioner, integrationsvarianter, plattformar och specialkonfigurationer att hantera.

Teknisk variation är inte i sig negativ. Två databastyper kan vara fullt motiverade om de möter olika informations- och kvalitetsbehov. Fragmentering uppstår när variationen saknar en tydlig anledning eller när kostnaden för den inte längre är synlig för den som fattar beslutet.

### Operativ fragmentering

Två system kan vara byggda med liknande teknik men ändå förvaltas på helt olika sätt. De kan ha olika modeller för driftsättning, loggning, övervakning, backup, incidenthantering och återställning. Då blir organisationens driftförmåga beroende av lokal kunskap och manuella rutiner.

Operativ fragmentering är ofta mindre synlig än produktfragmentering men märks tydligt när något ska förändras, uppgraderas, felsökas eller återställas.

### Informationsmässig fragmentering

Samma begrepp kan tolkas olika i olika lösningar. Samma information kan kopieras utan tydligt ägarskap. Ett system kan betrakta en viss datakälla som auktoritativ medan ett annat använder en lokal kopia som i praktiken blivit ett eget original.

Detta är inte främst ett plattformsproblem, men den gemensamma arkitekturen behöver synliggöra när tekniska lösningar förstärker eller försvårar informationsmässig sammanhållning.

### Säkerhetsmässig fragmentering

Om säkerhetsmekanismer varierar kraftigt mellan lösningar blir det svårt att veta vilka skydd som faktiskt gäller. Autentisering, *tjänsteidentitet*er, certifikat, secrets, loggning och åtkomstkontroll kan då behöva bedömas separat i varje system.

Gemensamma säkerhetsmekanismer kan minska variationen, men en gemensam produkt utan en gemensam säkerhetsmodell löser inte problemet.

### Kunskapsmässig fragmentering

Varje unik teknik och lokal speciallösning kräver människor som förstår den. När kunnandet finns hos ett fåtal personer ökar sårbarheten. Ny personal behöver lära sig fler varianter och team får svårare att hjälpa varandra.

Samma problem behöver dessutom analyseras på nytt på flera ställen om kunskapen inte är paketerad för återanvändning.

Gemensam IT-arkitektur försöker inte eliminera all variation. Den försöker göra den avsiktlig, begriplig och proportionerlig. Det kräver också att organisationen kan se kostnaden för variation över tid. Ett teknikval kan vara billigt i projektet men dyrt i förvaltningen om det kräver separat kompetens, särskilda övervakningsrutiner eller en egen livscykel. På motsvarande sätt kan en gemensam lösning vara dyrare att etablera men billigare när många team kan använda samma säkerhets-, drift- och supportmodell. Arkitekturen behöver därför göra konsekvenserna synliga på en större yta än det enskilda projektet.

## Återanvändning handlar om mer än kod

Återanvändning inom IT förknippas ofta med kodbibliotek och gemensamma komponenter. I en större arkitektur är det bara en del av bilden. Det som kan återanvändas är också exempelvis lösningsmönster, säkerhetsmodeller, tjänstekontrakt, plattformstjänster, standarder, kvalitetsprofiler och erfarenhet av återkommande avvägningar.

Det kan vara mer värdefullt än att återanvända en viss kodbas. Om ett team kan använda en etablerad modell för tjänsteidentitet behöver det inte börja med frågan ”hur brukar vi lösa detta?”. Om en gemensam databastjänst redan har tydliga ansvar och kvalitetsnivåer behöver varje projekt inte designa drift, backup och övervakning från grunden.

Gemensam IT-arkitektur skapar därför värde när återkommande problem omvandlas till återanvändbar kunskap och användbara erbjudanden. Det minskar inte bara arbetet i nästa projekt. Det gör också att organisationen kan förbättra samma lösning för många konsumenter samtidigt, exempelvis genom bättre säkerhet, automatisering eller återställning.

För att det ska fungera måste erbjudandena vara möjliga att konsumera och möta relevanta kvalitetskrav. En gemensam komponent som kräver omfattande specialkunskap, har otydligt ansvar eller inte går att använda i teamens normala leveransflöde kommer att kringgås. Då finns återanvändningen bara på papperet.

## En produktkatalog är inte en arkitektur

Många organisationer har listor över godkända produkter, plattformar och tekniker. Sådana kataloger kan vara nödvändiga, men de svarar inte på den viktigaste frågan: varför finns tekniken och vilket behov är den avsedd att lösa?

Om den gemensamma arkitekturen börjar i en produktlista blir resonemanget lätt bakvänt. I stället för att fråga vilket behov lösningen har och vilka egenskaper den måste uppfylla börjar man fråga vilken av de befintliga produkterna som ska användas.

Då finns en risk att produktens egenskaper och begränsningar gradvis omvandlas till generella krav. Medlet blir mål.

En mer hållbar arkitektur behöver skilja mellan relativt stabila behov och mer föränderliga tekniska svar. Behov som säker integration, spårbar identitet, robust lagring eller reproducerbar leverans kan bestå under lång tid även när produkterna som realiserar dem byts ut.

Bokens modell utgår därför från att behov och kvalitetskrav leder vidare till gemensamma IT-förmågor, som i sin tur kan realiseras genom mönster, plattformstjänster, standarder och tekniska byggblock. Produkter och versioner ligger längre ned och kan förändras snabbare. Den modellen utvecklas i nästa kapitel.

## Varför tänka i förmågor?

Förmågor ger ett sätt att beskriva vad organisationen behöver kunna stödja utan att direkt låsa beskrivningen vid en viss teknisk realisering.

Organisationen kan exempelvis behöva kunna hantera *identitet och tillit*, integrera system, köra applikationer, lagra data, leverera programvara och återställa tjänster. Behoven finns oberoende av vilken produkt som råkar användas eller vilket team som äger realiseringen.

Det gör förmågan användbar som en relativt stabil navigationspunkt när tekniken förändras. Förmågor ersätter däremot inte domänarkitektur, verksamhetsmodellering eller konkreta lösningsbeslut. De används här som struktur för gemensamt IT-stöd. Begreppet fördjupas i Del II.

## Gemensamt betyder inte centraliserat

Att något är gemensamt betyder inte att det måste ägas och implementeras centralt.

En standard kan beslutas gemensamt men implementeras av många team. Ett lösningsmönster kan användas lokalt utan en central plattform. En plattformstjänst kan ha gemensamma kontrakt men drivas federerat. En referensarkitektur kan ge en gemensam utgångspunkt utan att varje lösning blir identisk.

Gemensamt bör därför förstås som att något behöver fungera sammanhängande över flera delar av organisationen, inte att alla beslut ska flyttas till en central grupp. Vad som behöver vara gemensamt kan alltså vara själva tjänsten, men det kan lika gärna vara kontraktet, säkerhetskravet, informationsmodellen eller sättet att fatta beslut.

Den skillnaden är viktig eftersom centralisering och standardisering löser olika problem. Centralisering samlar ansvar eller realisering. Standardisering skapar en gemensam form. Ibland behövs båda, ibland bara den ena.

I vissa fall ger en gemensam plattform tydliga skalfördelar. I andra räcker gemensamma protokoll, kontrakt, kvalitetskrav eller principer. En fungerande arkitektur behöver kunna säga både ”detta bör vi lösa tillsammans” och ”detta bör få vara lokalt”.

## Standardisering ska köpa något

Standardisering har en kostnad. Den begränsar valfrihet, kräver förvaltning och kan skapa tröghet. Därför behöver den kunna motiveras med vilket värde den skapar, exempelvis lägre säkerhetsrisk, enklare interoperabilitet, snabbare onboarding, lägre driftkostnad eller bättre automatisering.

Gemensamma lösningar är medel för kvalitet, effektivitet och sammanhang – inte mål i sig.

Om ett standarderbjudande inte möter ett legitimt behov behöver det gå att välja något annat under tydligt ansvar. Återkommande avsteg är dessutom information om att standarden eller plattformen kan behöva förändras. Hur sådana beslut och avvägningar bör hanteras behandlas senare i Del I.

## Gemensam arkitektur som möjliggörare

Den mest användbara gemensamma arkitekturen märks inte främst genom hur många dokument den producerar. Den märks genom vilka frågor ett team slipper lösa från början.

Ett utvecklingsteam bör exempelvis kunna hitta etablerade svar eller alternativ för frågor som autentisering, API-publicering, asynkron kommunikation, secrets-hantering, loggning, leverans, återställning och kvalitetsnivåer.

Det innebär inte att arkitekturen måste ge ett enda svar på varje fråga. Ibland behövs flera etablerade alternativ. Men alternativen bör vara begripliga, deras avvägningar kända och deras ansvar tydliga.

När detta fungerar kan gemensam arkitektur öka teamens autonomi. Teamet behöver inte vänta på en central arkitekt för varje detaljbeslut eftersom spelplanen redan är tydlig. Det kan fokusera på det som är unikt för verksamhetsproblemet och fatta fler beslut nära lösningen.

Det är också ett viktigt test på om arkitekturen verkligen fungerar som möjliggörare. Om varje användning av ett gemensamt erbjudande kräver en individuell dispens, omfattande samordning eller muntlig kunskap från ett fåtal personer har organisationen inte skapat en fungerande gemensam väg, även om dokumentationen säger något annat.

## När gemensam arkitektur blir ett hinder

Samma mekanismer som skapar sammanhang kan bli problem om de används fel.

### När standarden blir viktigare än behovet

Om frågan ”följer ni standarden?” kommer före frågan ”vilket behov försöker ni lösa?” har styrningen vänt på orsak och verkan. Team kan då tvingas in i lösningar som är formellt korrekta men funktionellt olämpliga.

### När gemensamma plattformar blir obligatoriska monopol

En gemensam plattform är värdefull så länge den erbjuder en bra väg att lösa återkommande behov. Om den skyddas från jämförelse med faktiska behov riskerar konsumenterna i stället att få bära dess begränsningar.

### När abstraktionen blir för grov

Om allt sorteras under ett fåtal breda rubriker kan viktiga skillnader försvinna. ”Integration” är exempelvis inte ett enda problem. Realtids-API:er, eventdriven kommunikation, batchöverföring och organisationsöverskridande informationsutbyte kan ha helt olika kvalitetskrav.

### När dokumentationen ersätter tjänsten

Att dokumentera att en organisation har en viss förmåga betyder inte att den fungerar i praktiken. Ett gemensamt erbjudande behöver vara möjligt att använda, ha tydligt ansvar och ge faktiskt stöd – inte bara finnas som rubrik i en arkitekturbeskrivning.

### När arkitekturen inte kan förändras

Tekniklandskap, verksamhetsbehov och externa krav förändras. En gemensam arkitektur som inte kan ompröva sina standarder och erbjudanden kommer förr eller senare att skydda historiska beslut i stället för att stödja aktuella behov.

Gemensam arkitektur behöver alltså vara stabil nog för att skapa sammanhang men föränderlig nog för att fortsätta vara relevant. Det är därför styrningen inte bara behöver kunna besluta om nya gemensamma lösningar, utan också kunna ändra och avveckla dem när förutsättningarna förändras.

## Ett konkret exempel: tre team, samma återkommande problem

Tänk dig en större organisation med tre utvecklingsinitiativ:

1. ett *internt handläggningsstöd*,
2. en publik e-tjänst,
3. ett system för informationsutbyte med en extern organisation.

Verksamhetsbehoven skiljer sig. Det första behöver stödja handläggare och långlivade ärenden. Det andra behöver vara tillgängligt för externa användare och hantera varierande belastning. Det tredje behöver säkra och spårbara informationsflöden över en organisatorisk gräns.

Trots skillnaderna återkommer många tekniska frågor. Alla tre behöver identitet, loggning, övervakning, leverans och någon form av datalagring. Flera behöver API-hantering eller tjänsteidentiteter. Alla behöver kunna återställas efter fel.

Utan gemensam arkitektur kan varje initiativ börja om från början. Med en alltför centraliserad arkitektur kan de i stället tvingas in i samma tekniska modell trots att behoven skiljer sig.

En mer balanserad modell identifierar vad som återkommer, erbjuder gemensamma mönster och tjänster där de ger värde och lämnar lösningsspecifika beslut till respektive team.

Handläggningsstödet kan exempelvis använda ett gemensamt workflow-erbjudande medan e-tjänsten inte gör det. Båda kan använda samma identitets- och loggningstjänster. Informationsutbytet kan behöva en särskild kommunikationslösning men ändå följa gemensamma principer för identitet, spårbarhet och förvaltning.

Det är denna kombination av gemensam grund och motiverad lokal variation som resten av boken utvecklar.

## Tre nivåer behöver kunna samspela

För att hålla ihop helheten behöver beslut kunna tas på olika nivåer. På en gemensam arkitekturnivå hålls sådant samman som behöver vara konsekvent över flera områden. På förmågenivå utvecklas exempelvis mönster, tjänsteerbjudanden och standarder inom ett visst område. På lösnings- och produktnivå kombinerar team dessa byggstenar med domänspecifika komponenter för att lösa ett konkret behov.

Den fulla ansvarsfördelningen utvecklas senare. Här är den viktiga poängen att gemensam riktning och lokal autonomi behöver stödja varandra, inte konkurrera. Den gemensamma nivån ska inte detaljdesigna lösningar, och lösningsteamen ska inte behöva uppfinna gemensamma mekanismer på nytt. Mellan dem behövs förmågeområden som kan omsätta gemensam riktning till användbara mönster, tjänster och standarder.

## Hur vet man att den gemensamma arkitekturen fungerar?

Det går att producera många arkitekturdokument utan att förbättra organisationens förmåga att utveckla och förvalta IT-stöd. En bättre fråga är vilka effekter man vill se.

Tecken på en fungerande gemensam arkitektur kan vara att:

- team snabbare hittar etablerade sätt att lösa återkommande problem,
- samma säkerhets- och driftfrågor inte behöver återuppfinnas i varje projekt,
- gemensamma tjänster har tydliga ansvar och är möjliga att konsumera utan omfattande specialhjälp,
- tekniska avvikelser motiveras av verkliga behov,
- det går att förstå varför en viss standard eller plattform finns,
- återkommande avsteg leder till förbättring av gemensamma erbjudanden,
- teknik kan bytas utan att den övergripande arkitekturmodellen måste göras om,
- lösningsteam har frihet inom tydliga ramar.

Gemensam IT-arkitektur är alltså inte framgångsrik för att många system använder samma produkt. Den är framgångsrik när organisationen kan hantera återkommande problem konsekvent, göra avvägningar medvetet och samtidigt låta verkliga skillnader i behov påverka lösningen.

## Från problembild till modell

Gemensam IT-arkitektur behöver alltså minska onödig variation utan att låsa ihop sådant som måste kunna skilja sig. För att göra det behöver behov, förmågor, mönster, plattformar, standarder, byggblock och produkter hållas isär och relateras till varandra.

Nästa kapitel introducerar den lagerindelning som används genom resten av boken.

## Centrala fakta

- Gemensam IT-arkitektur ska minska onödig variation, inte all variation.
- Lokal optimering kan skapa kostnader och risker på organisationsnivå även när varje enskilt teknikval är rimligt.
- Fragmentering kan vara teknisk, operativ, informationsmässig, säkerhetsmässig och kunskapsmässig.
- Återanvändning omfattar inte bara kod utan även mönster, kunskap, tjänstekontrakt, standarder och kvalitetsprofiler.
- En produktkatalog beskriver tekniska val men förklarar inte i sig vilka behov eller förmågor de ska stödja.
- Förmågor ger en stabilare ingång än produkter, men ersätter inte domänarkitektur eller konkreta lösningsbeslut.
- Gemensamt är inte synonymt med centraliserat.
- Standardisering ska skapa ett tydligt värde och kunna omprövas när den inte längre gör det.
- En bra gemensam arkitektur gör fler beslut möjliga att fatta nära lösningen eftersom spelplan, alternativ och ansvar är tydliga.
- Gemensam arkitekturnivå, förmågenivå och lösnings-/produktnivå behöver samspela utan att detaljstyra varandra.

## Begrepp att känna till

Gemensam IT-arkitektur  
En sammanhängande modell av principer, förmågor, mönster, tjänster, standarder och andra arkitekturartefakter som används för problem och behov som berör flera delar av organisationens IT-landskap.

Lokal optimering  
När ett beslut förbättrar situationen för ett enskilt team, system eller område men samtidigt kan skapa kostnader, risker eller komplexitet för helheten.

Motiverad variation  
Skillnader i lösning som kan härledas till verkliga skillnader i behov, kvalitetskrav, risk eller andra relevanta förutsättningar.

Fragmentering  
När likartade behov hanteras på många sinsemellan olika sätt utan att variationen ger motsvarande verksamhets- eller kvalitetsvärde.

Återanvändning  
Att använda tidigare etablerad kunskap, mönster, komponenter, plattformstjänster, standarder eller andra byggstenar för att slippa lösa samma problem från grunden.
