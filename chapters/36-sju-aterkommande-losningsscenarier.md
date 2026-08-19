# 36. Sju återkommande lösningsscenarier

En arkitekturmodell blir inte särskilt värdefull om den bara fungerar som taxonomi. Den måste hjälpa ett konkret initiativ att göra bättre val. I föregående kapitel beskrevs därför ett arbetsflöde från behov och kvalitetsprofil till förmågor, referensarkitektur, mönster, plattformar, standarder och lokala arkitekturbeslut. I detta kapitel används samma arbetsflöde på sju återkommande lösningsscenarier.

Syftet är inte att presentera sju färdiga lösningar. Två system som båda är publika e-tjänster kan behöva mycket olika arkitektur beroende på informationsklassning, transaktionsvolym, tillgänglighetskrav och integrationer. På samma sätt kan två handläggningsstöd skilja sig radikalt i hur mycket explicit workflow, regelhantering och dokumenthantering de behöver.

Scenarierna ska i stället läsas som arkitekturella startpunkter. De visar vilka frågor som ofta blir viktiga, vilka förmågor som typiskt aktiveras och vilka mönster eller plattformstjänster som brukar vara relevanta. Varje konkret lösning måste fortfarande verifiera sina egna behov och dokumentera sina egna beslut.

## Samma analysram för alla scenarier

För att scenarierna ska gå att jämföra används samma sex frågor:

1. Vad driver lösningen? Vilket behov eller vilken situation gör scenariot särskilt?
2. Vilka kvalitetsattribut dominerar? Vad måste lösningen vara särskilt bra på?
3. Vilka förmågor blir centrala? Vilka gemensamma IT-förmågor behöver kunna stödja lösningen?
4. Vilka mönster och plattformstjänster blir typiska? Vilka återanvändbara beslut är sannolika kandidater?
5. Vilka val måste fortfarande göras lokalt? Vad kan referensarkitekturen inte avgöra?
6. Vilket är det vanligaste felgreppet? Var finns risken att en bra startpunkt förvandlas till ett dåligt recept?

Den gemensamma ramen gör också en annan sak tydlig: samma komponent kan vara central i ett scenario och perifer i ett annat. En workflowmotor är till exempel ofta viktig i ett handläggningsstöd men normalt ointressant i en enkel containerbaserad teknisk tjänst. En containerplattform kan däremot vara central som runtime i båda fallen utan att därmed definiera lösningens verksamhetsarkitektur.

## Scenario 1: Internt handläggningsstöd

Ett internt handläggningsstöd används av medarbetare som arbetar med ärenden, uppgifter, beslut, dokument och informationsutbyte över tid. Det karakteristiska är inte att det finns ett webbgränssnitt, utan att verksamhetsarbetet ofta har lång livslängd, explicit status, ansvarsförflyttning och krav på historik.

### Drivande behov

Typiska behov är arbetsköer, uppgifter, ärendestatus, dokument och bilagor, verksamhetsregler, rollstyrd åtkomst och integration med flera källsystem. Handläggningen kan sträcka sig över dagar eller månader och fortsätta trots omstarter, versionsbyten eller tillfälligt otillgängliga integrationer.

### Dominerande kvaliteter

Spårbarhet, säkerhet, användbarhet, kontinuitet och förändringsbarhet brukar väga tungt. Det behöver gå att förstå vem som gjorde vad, på vilket underlag och enligt vilken regelversion. Samtidigt måste arbetet kunna återupptas efter fel utan att ärendets verksamhetsmässiga tillstånd blir oklart.

### Centrala förmågor

De primära förmågorna är ofta Interaktion, Process/workflow, Regler och beslut samt Data- och informationshantering. Integration och kommunikation, Identitet och tillit, Runtime och Driftbarhet fungerar som stödjande förmågor.

### Typiska mönster och plattformar

Human workflow är relevant när processen verkligen behöver explicit och beständigt processtillstånd. Externaliserade verksamhetsregler kan vara motiverade när regler ändras oberoende av övrig applikationslogik eller behöver särskild spårbarhet. System of record med härledda kopior hjälper till att skilja auktoritativ ärendedata från index, rapportkopior och cache.

Typiska plattformstjänster kan vara webb-/designsystem, workflow- eller case management-plattform, databastjänst, objektlagring, identitet, API/messaging, runtime, logging/monitoring och backup/recovery.

### Lokala val

Den viktigaste lokala frågan är ofta hur mycket av processen som behöver modelleras explicit. Ett vanligt ärendeflöde kan ibland hanteras bättre med vanlig domänlogik än med en processmotor. Samma prövning gäller regelmotor, dokumentlagring och graden av asynkron integration.

### Vanligt felgrepp

Det vanligaste felgreppet är att göra plattformen till verksamhetsmodell. Workflowmotorn får då äga ärendets affärsstatus, regelmotorn börjar bära processlogik och dokumentplattformen blir system of record utan att det varit ett medvetet beslut. Referensarkitekturen bör i stället hjälpa till att hålla ansvaren tydliga.

## Scenario 2: Publik e-tjänst

En publik e-tjänst möter externa användare över internet. Det gör användarupplevelse, identitet, exponeringsyta och skydd av information särskilt viktiga. Samtidigt är e-tjänsten ofta bara den publika delen av en längre verksamhetsprocess.

### Drivande behov

Lösningen behöver typiskt presentera information, samla in uppgifter, ta emot dokument och ibland låta användaren följa ett pågående ärende. Vissa tjänster kräver stark identifiering; andra bör medvetet kunna användas anonymt.

### Dominerande kvaliteter

Tillgänglighet i betydelsen användbar och åtkomlig tjänst, säkerhet, prestanda, skalbarhet och spårbarhet blir centrala. Internetexponering gör också att felaktiga antaganden om klienten får större konsekvens. Känsliga uppgifter bör inte lagras i klienten bara för att det tekniskt är möjligt.

### Centrala förmågor

Interaktion, Identitet, Integration och Data är vanligen primära. Process och Regler tillkommer när e-tjänsten initierar eller deltar i formell handläggning. Runtime och Driftbarhet är nödvändiga realiseringsförmågor men definierar inte själva scenariot.

### Typiska mönster och plattformar

Backend for Frontend kan vara relevant när den publika kanalens behov skiljer sig tydligt från bakomliggande domäntjänster. Tjänsteidentitet används mellan interna komponenter. Human workflow kan aktiveras när en inskickad ansökan går vidare till handläggning.

Typiska plattformstjänster är webbframework, design system, extern identitet/federation där det behövs, API Management, databastjänster, objektlagring, containerplattform, observerbarhet och CI/CD.

### Lokala val

Identifiering ska alltid härledas från verksamhetsbehovet. En tjänst ska inte kräva inloggning bara för att gemensam autentisering finns. Andra viktiga val är sessionsmodell, edge-/gatewaylösning, uppladdningsflöden, DDoS-skydd, cache och hur den publika tjänsten kopplas till intern handläggning.

### Vanligt felgrepp

Ett vanligt fel är att behandla ”publik e-tjänst” som ett färdigt produktpaket. Resultatet blir att samma autentiseringskrav, samma komponentuppsättning och samma driftprofil appliceras på allt från enkel informationsinhämtning till samhällskritisk transaktion. Scenariot ska standardisera analysen, inte resultatet.

## Scenario 3: Integrationsintensivt verksamhetssystem

I ett integrationsintensivt verksamhetssystem är kommunikation med andra system inte perifer infrastruktur utan en dominerande del av lösningens beteende. Systemet kan ha många API-beroenden, meddelandeflöden, event, filer och externa beroenden.

### Drivande behov

Det centrala behovet är att utbyta information med många parter utan att varje förändring kräver samtidiga releaser över hela landskapet. Robust felhantering, kontraktslivscykel och felsökning blir därför förstklassiga arkitekturfrågor.

### Dominerande kvaliteter

Interoperabilitet, förändringsbarhet, spårbarhet, kontinuitet och prestanda står ofta högst. Lösningen behöver kunna hantera att externa parter är långsamma, temporärt otillgängliga eller ligger på en annan kontraktsversion.

### Centrala förmågor

Integration och kommunikation är primär, tillsammans med Data och Driftbarhet. Identitet och tillit behövs för säkra tjänsterelationer. Process kan vara relevant när ett integrationsflöde faktiskt representerar en långlivad verksamhetsprocess, men bör inte införas bara för att ett meddelande passerar flera steg.

### Typiska mönster och plattformar

Asynkron meddelandekommunikation och publicera/prenumerera blir ofta centrala. Tjänsteidentitet, observerbarhet och system of record/härledda kopior stödjer dem. API Management och Enterprise Messaging är typiska gemensamma erbjudanden, kompletterade med data integration/ETL eller strukturerade utbytestjänster där det finns sådana behov.

### Lokala val

Varje integration måste fortfarande avgöra om kommunikationen ska vara synkron eller asynkron, kommando eller event, API eller fil, direkt eller via plattform. Ordering, idempotens, återförsök, dead-letter-hantering och kontraktskompatibilitet måste relateras till faktisk verksamhetseffekt.

### Vanligt felgrepp

Det klassiska felgreppet är att integrationsplattformen blir ett centralt lager för verksamhetslogik. Transformationer växer till affärsregler, routing blir processmotor och ett gemensamt canonical data model försöker ersätta domänägda begrepp. Då minskar inte kopplingen; den flyttas bara till en ny central flaskhals.

## Scenario 4: Informationsutbyte med annan myndighet eller extern organisation

Detta scenario liknar det integrationsintensiva systemet men har en viktig extra dimension: ansvar och tillit korsar organisationsgränsen. Tekniska kontrakt behöver därför kombineras med tydliga överenskommelser om ansvar, kvittens, felhantering och förändring.

### Drivande behov

Strukturerat informationsutbyte, säker kommunikation, certifikat/trust, kvittenser och spårbarhet är typiska behov. Parterna kan ha olika förändringstakt och olika driftorganisationer.

### Dominerande kvaliteter

Säkerhet, interoperabilitet, spårbarhet, regelefterlevnad och kontinuitet dominerar. Ett tekniskt lyckat anrop räcker inte alltid som bevis på att motparten faktiskt tagit ansvar för informationen; kvittensens semantik måste vara definierad.

### Centrala förmågor

Integration och Identitet/tillit är primära. Data och Driftbarhet är stödjande och Process kan bli relevant när utbytet är en del av ett formellt flöde med tidsgränser och ansvarsskiften.

### Typiska mönster och plattformar

Asynkron meddelandekommunikation är ofta attraktiv när parterna inte kan förutsättas vara tillgängliga samtidigt. Tjänsteidentitet, PKI och observerbarhet blir viktiga. Gemensamma tjänster för säker myndighetskommunikation, strukturerat utbyte, managed file transfer eller messaging kan minska mängden lokal säkerhets- och protokollimplementation.

### Lokala val

API, message eller fil måste fortfarande väljas utifrån informationsmängd, tidskrav och motpartens kapacitet. Kötid, återförsök, kvittenstyper, ordering, certifikatlivscykel och incidentansvar behöver definieras explicit.

### Vanligt felgrepp

Ett vanligt fel är att anta att en gemensam transporttjänst också definierar verksamhetskontraktet. Den kan ge säker transport och teknisk kvittens men kan inte automatiskt avgöra vad informationen betyder, när mottagaren juridiskt eller verksamhetsmässigt har accepterat den eller vem som ansvarar för felaktigt innehåll.

## Scenario 5: Containerbaserad tjänst

En containerbaserad tjänst är annorlunda än de föregående scenarierna eftersom den framför allt beskriver en teknisk realiseringsklass, inte en verksamhetslösningstyp. Den är därför ett bra test på att arkitekturmodellen klarar olika abstraktionsnivåer.

### Drivande behov

Typiska behov är reproducerbar paketering, automatiserad driftsättning, skalning, standardiserad runtime, isolering, observerbarhet, secrets och snabb återstart.

### Dominerande kvaliteter

Förvaltningsbarhet, förändringsbarhet, tillgänglighet, skalbarhet, säkerhet och spårbarhet dominerar. Dessa kvaliteter påverkar hur workloaden utformas, men säger fortfarande inget om vilken verksamhetslogik tjänsten ska bära.

### Centrala förmågor

Runtime, Programvaruutveckling och leverans samt Driftbarhet är primära. Identitet, Integration och Data tillkommer beroende på tjänstens verkliga uppgift.

### Typiska mönster och plattformar

Containeriserad stateless tjänst, build once/promote many, tjänsteidentitet och observerbarhet är typiska mönster. Source Code Management, CI/CD, Artifact Repository, Container Application Platform, Secrets Management och observerbarhetstjänster bildar ofta en paved road.

### Lokala val

Stateless eller stateful är ett faktiskt arkitekturbeslut, inte en etikett som följer automatiskt av containerformatet. Resursprofil, autoscaling, exponeringsmodell, health checks, shutdownbeteende, persistent data och rollback/roll-forward behöver avgöras per workload.

### Vanligt felgrepp

Det vanligaste felgreppet är att containerisering blir ett mål i sig. Workloads med OS-nära beroenden, hårda licensvillkor eller leverantörskrav kan passa bättre på annan runtime. En gemensam plattform ska göra ett vanligt bra val enkelt, inte göra alternativa legitima val omöjliga.

## Scenario 6: AI-baserat verksamhetsstöd

AI-baserat verksamhetsstöd kan sammanfatta, klassificera, söka, rekommendera eller stödja beslut. Det som skiljer scenariot från traditionell regel- och analysfunktionalitet är att delar av beteendet kan vara probabilistiska och svårare att verifiera med klassiska exempelbaserade tester.

### Drivande behov

Behovet kan vara snabbare informationsinhämtning, bättre sökning, stöd vid klassificering eller ett assistentgränssnitt över godkända informationskällor. Det är viktigt att formulera detta behov utan att börja med ”vi behöver en LLM”.

### Dominerande kvaliteter

Spårbarhet, verifierbarhet, informationsskydd, regelefterlevnad, kvalitet och kostnad blir centrala. I många fall är frågan om hur fel får lösningen ha viktigare än modellens nominella kapacitet.

### Centrala förmågor

Analys/sökning/AI, Data och Identitet är primära. Integration, Regler, Process och Driftbarhet tillkommer beroende på om AI-funktionen får läsa källor, använda verktyg eller påverka ett verksamhetsflöde.

### Typiska mönster och plattformar

RAG är relevant när svar behöver grundas i kontrollerade källor. AI med mänsklig kontroll är relevant när resultatet kan få betydande konsekvens. Tjänsteidentitet behövs när AI-tjänsten anropar andra system. System of record/härledda kopior hjälper till att hålla index och embeddings separerade från auktoritativa källor.

Managed LLM, RAG/Knowledge Service, Search/Indexing, API Management och observerbarhet kan vara gemensamma erbjudanden.

### Lokala val

Viktigast är att avgöra om problemet alls kräver AI. Deterministisk regel kan vara bättre när beslutet ska vara reproducerbart och fullständigt specificerbart. Om AI används måste informationskällor, behörighetsfiltrering, utvärderingsmått, modell-/promptversioner, mänsklig kontroll och tillåtna verktyg definieras.

### Vanligt felgrepp

Det farligaste felgreppet är att ge modellen högre tillit än den samlade evidensen motiverar. Ett snyggt svar är inte samma sak som ett korrekt svar. RAG eliminerar inte fel, mänsklig kontroll fungerar bara om människan har information och tid att faktiskt granska, och en agent med breda rättigheter skapar en större konsekvensyta än en ren läsassistent.

## Scenario 7: Digital arbetsplats

Den digitala arbetsplatsen omfattar generell produktivitet, samarbetsytor, dokument, möten, chatt, extern samverkan och allt oftare produktivitets-AI. Den är särskild därför att användningen är bred och decentraliserad samtidigt som informationen ofta är verksamhetskritisk.

### Drivande behov

Medarbetare behöver snabbt kunna skapa, dela och samproducera information. Team och projekt behöver arbetsytor utan lång beställningsprocess. Samtidigt måste organisationen kunna hantera åtkomst, extern delning, livscykel och informationsskydd.

### Dominerande kvaliteter

Användbarhet, säkerhet, regelefterlevnad, tillgänglighet, livscykel och kostnad är centrala. Portabilitet kan bli viktig eftersom stora mängder arbetsmaterial lätt binds till en specifik svit eller informationsstruktur.

### Centrala förmågor

Arbetsplats/samarbete/produktivitet är primär. Identitet, Data, AI och Integration är stödjande.

### Typiska mönster och plattformar

Kontrollerad samarbetsyta är ett centralt mönster. System of record/härledda kopior hjälper till att förklara varför samarbetsytan inte automatiskt ska vara långtidsarkiv eller verksamhetssystem. AI med mänsklig kontroll blir relevant när produktivitets-AI används för underlag med betydande konsekvens.

Typiska plattformstjänster är Productivity Suite, Collaboration Workspace, Productivity AI Assistant och avgränsade low-code-tjänster.

### Lokala val

Personlig eller gemensam yta, intern eller extern delning, arbetsmaterial eller formell information, retention, informationsklassning och vem som äger ytan är centrala frågor. Low-code-lösningar behöver omprövas när de går från individuell produktivitet till gemensamt verksamhetsberoende.

### Vanligt felgrepp

Det vanligaste felgreppet är att låta bekvämlighet bestämma informationsarkitekturen. E-postlådor blir register, teamsytor blir permanenta system of record och low-code-appar blir verksamhetssystem utan motsvarande förvaltningsmodell. Produktivitetsplattformen ska sänka tröskeln för arbete, inte eliminera behovet av ansvar.

## Vad scenarierna visar tillsammans

De sju scenarierna delar många byggstenar men skiljer sig i vad som driver arkitekturen. Det är själva poängen med modellen.

| Scenario | Primär arkitekturdrivare | Särskilt viktig avvägning |
|---|---|---|
| Internt handläggningsstöd | långlivat verksamhetsarbete | explicit workflow kontra vanlig domänlogik |
| Publik e-tjänst | extern kanal och internetexponering | gemensam kanalplattform kontra behovsanpassad riskprofil |
| Integrationsintensivt system | många beroenden och kontrakt | lös koppling kontra operativ komplexitet |
| Externt myndighetsutbyte | organisationsöverskridande trust | teknisk kvittens kontra verksamhetsmässigt ansvar |
| Containerbaserad tjänst | standardiserad exekvering och leverans | paved road kontra olämplig teknikstandardisering |
| AI-baserat verksamhetsstöd | probabilistisk funktion och kunskapsåtkomst | nytta/autonomi kontra verifierbarhet och konsekvens |
| Digital arbetsplats | bred decentraliserad produktivitet | låg friktion kontra informationsstyrning |

Flera slutsatser återkommer.

För det första är en plattform aldrig hela arkitekturen. Containerplattformen löser exekveringsfrågan men inte verksamhetsgränserna. Produktivitetssviten löser samarbetsbehov men inte system-of-record-frågan. AI-plattformen löser modellåtkomst men inte tillitsfrågan.

För det andra är samma mönster olika viktigt i olika sammanhang. Tjänsteidentitet och observerbarhet förekommer i många scenarier eftersom de är tvärgående mekanismer. Human workflow är däremot starkt situationsberoende. Att något finns i en referensarkitektur betyder därför inte att det ska användas i varje instans.

För det tredje blir kvalitetsprofilen den viktigaste differentieraren mellan två lösningar inom samma scenario. Två publika e-tjänster kan se lika ut funktionellt men behöva olika identitetsnivå, tillgänglighet, redundans och loggning. Två AI-stöd kan använda samma modell men kräva helt olika mänsklig kontroll beroende på konsekvensen av ett fel.

För det fjärde visar scenarierna varför ansvar behöver ligga på flera nivåer. Den gemensamma arkitekturen definierar språk, principer, standarder och återanvändbara startpunkter. Förmåge- och plattformsansvariga utvecklar de tjänster och mönster som återkommer. Lösningsteamet bär ansvaret för den konkreta kvalitetsprofilen och för att välja, kombinera eller avvika medvetet.

## Referensarkitektur som hypotes, inte facit

Det är lockande att se en välskriven referensarkitektur som ett svar. En mer användbar syn är att se den som en förkvalificerad hypotes:

> För den här typen av behov brukar dessa förmågor, ansvar, mönster och plattformar vara relevanta. Verifiera dem mot den konkreta situationen.

Det gör två typer av återkoppling viktiga. Om många lösningar av samma typ gör samma avsteg kan referensarkitekturen vara fel eller ofullständig. Om nästan ingen använder en rekommenderad byggsten kan det bero på dålig dokumentation, låg plattformskvalitet eller att rekommendationen inte längre motsvarar behovet.

En levande referensarkitektur bör därför mätas mot verklig användning. Den ska kunna förändras när tekniken, verksamhetsbehoven eller de gemensamma plattformarna förändras. Den ska också kunna förlora delar när en tidigare komplicerad fråga blivit en självklar plattformsförmåga.

Detta leder direkt till bokens avslutande kapitel. När förmågekarta, principer, mönster, plattformstjänster, standarder och referensarkitekturer väl finns är huvudfrågan inte hur de produceras en gång. Huvudfrågan är hur hela systemet hålls levande, relevant och användbart utan att governance blir en flaskhals.
