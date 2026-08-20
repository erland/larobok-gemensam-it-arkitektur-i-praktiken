# 36. Sju återkommande lösningsscenarier

En arkitekturmodell blir inte särskilt värdefull om den bara fungerar som taxonomi. Den måste hjälpa ett konkret initiativ att göra bättre val. I föregående kapitel beskrevs därför en sammanhängande väg från behov och kvalitetsprofil till förmågor, referensarkitektur, mönster, plattformstjänster, standarder och lokala arkitekturbeslut. Här används samma modell på sju återkommande lösningsscenarier.

Syftet är inte att presentera sju färdiga lösningar. Två publika e-tjänster kan behöva mycket olika arkitektur beroende på informationsklassning, transaktionsvolym, tillgänglighetskrav och integrationer. Två handläggningsstöd kan på motsvarande sätt skilja sig kraftigt i hur mycket explicit workflow, regelhantering och dokumenthantering de behöver.

Scenarierna ska därför läsas som **arkitekturella startpunkter**. För varje scenario prövas samma sex frågor: vad som driver lösningen, vilka kvalitetsattribut som dominerar, vilka gemensamma IT-förmågor som blir centrala, vilka mönster och plattformstjänster som typiskt är relevanta, vilka val som måste förbli lokala och vilket felgrepp som är särskilt vanligt. Poängen är jämförbarhet — inte att varje scenario ska mynna ut i samma komponentlista.

## Scenario 1: Internt handläggningsstöd

Ett internt handläggningsstöd används av medarbetare som arbetar med ärenden, uppgifter, beslut, dokument och informationsutbyte över tid. Det karakteristiska är inte webbgränssnittet utan det långlivade verksamhetsarbetet: explicit status, ansvarsförflyttning, historik och behov av att kunna återuppta arbetet efter avbrott.

Spårbarhet, säkerhet, användbarhet, kontinuitet och förändringsbarhet väger därför tungt. Interaktion, Process/workflow, Regler och beslut samt Data- och informationshantering är ofta de mest styrande förmågorna, med Integration, Identitet, Runtime och Driftbarhet som stöd. Human workflow kan vara relevant när processen faktiskt behöver beständigt processtillstånd, medan externaliserade verksamhetsregler kan vara motiverade när regler förändras självständigt eller kräver särskild spårbarhet. Databas, objektlagring, identitet, integration, runtime och observerbarhet är typiska plattformstjänster runt lösningen.

Det viktigaste lokala valet är ofta **hur mycket som verkligen ska modelleras explicit**. Ett ärendeflöde kan ibland hanteras bättre med vanlig domänlogik än med en processmotor. Samma prövning gäller regelmotor, dokumentplattform och graden av asynkron integration. Det typiska felgreppet är att göra plattformen till verksamhetsmodell: workflowmotorn får äga affärsstatus, regelmotorn börjar bära processlogik eller dokumentplattformen blir system of record utan ett medvetet beslut.

## Scenario 2: Publik e-tjänst

En *publik e-tjänst* möter externa användare över internet. Därmed blir användarupplevelse, identitet, exponeringsyta, informationsskydd, prestanda och skalbarhet särskilt viktiga. E-tjänsten är samtidigt ofta bara den publika delen av en längre verksamhetsprocess.

Interaktion, Identitet, Integration och Data är vanligen centrala förmågor. Backend for Frontend kan vara relevant när kanalens behov skiljer sig tydligt från bakomliggande domäntjänster, medan gemensamma tjänster för design, identitet, API-hantering, runtime, observerbarhet och leverans ofta utgör startpunkter. Men identifiering, sessionsmodell, edge-/gatewaylösning, uppladdningsflöden, cache, skydd mot överbelastning och kopplingen till intern handläggning måste fortfarande härledas från den konkreta kvalitetsprofilen.

Det typiska felgreppet är att behandla ”publik e-tjänst” som ett färdigt produktpaket och ge alla tjänster samma autentisering, komponentuppsättning och driftprofil. I föregående kapitel användes den publika e-tjänsten som genomgående exempel för hela härledningen från behov till lösningsarkitektur. Här är poängen i stället att visa att samma scenarioklass kan ge olika arkitektur när risk, informationsinnehåll och konsekvens skiljer sig.

## Scenario 3: Integrationsintensivt verksamhetssystem

I ett **integrationsintensivt verksamhetssystem** ligger den arkitekturella tyngdpunkten i mängden systemberoenden och kontrakt inom eller nära den egna lösningsmiljön. Kommunikation är inte perifer infrastruktur utan en dominerande del av applikationens beteende: många API-anrop, meddelandeflöden, event, filer och beroenden behöver kunna förändras utan samtidiga releaser över hela landskapet.

Interoperabilitet, förändringsbarhet, spårbarhet, kontinuitet och prestanda blir därför centrala kvaliteter. Integration och kommunikation är primär förmåga, tillsammans med Data och Driftbarhet. Asynkron meddelandekommunikation, publicera/prenumerera, tjänsteidentitet, observerbarhet och system of record med härledda kopior är återkommande mönster. API Management, Enterprise Messaging och vid behov data integration/ETL kan vara gemensamma plattformstjänster.

De lokala besluten ligger i bland annat synkron kontra asynkron kommunikation, kommando kontra event, API kontra fil, ordering, idempotens, återförsök, dead-letter-hantering och kontraktskompatibilitet. Det klassiska felgreppet är att integrationsplattformen blir ett centralt lager för verksamhetslogik. Då flyttas kopplingen bara till en ny central flaskhals.

## Scenario 4: Informationsutbyte över organisationsgräns

Detta scenario kan tekniskt likna scenario 3, men **det som driver arkitekturen är en annan gräns**: ansvar och tillit korsar en organisationsgräns. Tekniska kontrakt måste därför kombineras med överenskommelser om informationsansvar, identitet, kvittens, incidenter, förändringstakt och interoperabilitet mellan parter som inte styrs av samma organisation.

Säkerhet, interoperabilitet, spårbarhet, regelefterlevnad och kontinuitet dominerar. Integration samt Identitet och tillit är primära förmågor. PKI, tjänsteidentitet, asynkron meddelandekommunikation och observerbarhet är ofta viktiga mönster och mekanismer, medan gemensamma tjänster för säker organisationsöverskridande kommunikation, strukturerat utbyte, managed file transfer eller messaging kan minska mängden lokal implementation.

Lokalt måste bland annat API, message eller fil väljas utifrån informationsmängd, tidskrav och motpartens kapacitet. Kvittenstyper, certifikatlivscykel, återförsök, ordering och incidentansvar behöver vara explicita. Det typiska felgreppet är att anta att en gemensam transporttjänst också definierar verksamhetskontraktet. Säker transport och teknisk kvittens säger inte automatiskt vad informationen betyder, när mottagaren har accepterat ansvar eller vem som hanterar felaktigt innehåll.

## Scenario 5: Containerbaserad tjänst

En containerbaserad tjänst är medvetet en annan typ av scenario. Den beskriver en **tekniskt formulerad startpunkt**, inte en verksamhetslösningsklass. Det gör den till ett stresstest av modellen: även när initiativet börjar med en realiseringsform måste analysen gå tillbaka till behov, kvaliteter och ansvar i stället för att anta att tekniken är arkitekturens mål.

Förvaltningsbarhet, förändringsbarhet, tillgänglighet, skalbarhet, säkerhet och spårbarhet är vanliga drivkrafter. Runtime, Programvaruutveckling och leverans samt Driftbarhet blir centrala förmågor. Containeriserad stateless tjänst, build once/promote many, tjänsteidentitet och observerbarhet är typiska mönster, medan Source Code Management, CI/CD, Artifact Repository, Container Application Platform, Secrets Management och observerbarhet ofta bildar en paved road.

Men containerformatet avgör inte om workloaden ska vara stateless eller stateful, hur persistent data ska hanteras, vilken resursprofil som behövs eller hur autoscaling, health checks, shutdown, exponering och rollback ska fungera. Det typiska felgreppet är att containerisering blir ett mål i sig. En gemensam plattform ska göra ett vanligt bra val enkelt, inte göra legitima alternativa realiseringsformer omöjliga.

## Scenario 6: AI-baserat verksamhetsstöd

AI-baserat verksamhetsstöd kan sammanfatta, klassificera, söka, rekommendera eller stödja beslut. Det som särskiljer scenariot är att delar av beteendet kan vara probabilistiska och svårare att verifiera än deterministisk regel- eller programlogik.

Spårbarhet, verifierbarhet, informationsskydd, regelefterlevnad, kvalitet och kostnad blir centrala kvaliteter. Analys/sökning/AI, Data och Identitet är primära förmågor, medan Integration, Regler, Process och Driftbarhet tillkommer när AI-funktionen får läsa källor, använda verktyg eller påverka ett verksamhetsflöde. RAG kan vara relevant när svar ska grundas i kontrollerade källor, och mänsklig kontroll när fel kan få betydande konsekvens. Managed LLM, RAG/Knowledge Service, Search/Indexing, API Management och observerbarhet kan vara gemensamma erbjudanden.

Det första lokala beslutet är dock om problemet alls kräver AI. Deterministisk regel är ofta bättre när ett beslut ska vara reproducerbart och fullständigt specificerbart. Om AI används måste informationskällor, behörighetsfiltrering, utvärderingsmått, modell- och promptversioner, mänsklig kontroll och tillåtna verktyg definieras. Det farligaste felgreppet är att ge modellen större tillit än evidensen motiverar: ett övertygande svar är inte samma sak som ett korrekt svar, och RAG eller mänsklig kontroll eliminerar inte automatiskt risken.

## Scenario 7: Digital arbetsplats

Den digitala arbetsplatsen omfattar generell produktivitet, samarbetsytor, dokument, möten, chatt, extern samverkan och allt oftare produktivitets-AI. Den arkitekturella utmaningen är kombinationen av mycket bred, decentraliserad användning och information som ändå kan vara verksamhetskritisk.

Användbarhet, säkerhet, regelefterlevnad, tillgänglighet, livscykel och kostnad är centrala kvaliteter. Arbetsplats/samarbete/produktivitet är primär förmåga, med Identitet, Data, AI och Integration som stöd. Kontrollerad samarbetsyta och system of record/härledda kopior är viktiga mönster för att skilja arbetsytan från långtidsarkiv och verksamhetssystem. Productivity Suite, Collaboration Workspace, Productivity AI Assistant och avgränsade low-code-tjänster är typiska gemensamma erbjudanden.

Lokalt måste bland annat personlig kontra gemensam yta, intern kontra extern delning, arbetsmaterial kontra formell information, retention, informationsklassning och ägarskap avgöras. Low-code-lösningar behöver omprövas när de går från individuell produktivitet till gemensamt verksamhetsberoende. Det typiska felgreppet är att låta bekvämlighet bestämma informationsarkitekturen: e-postlådor blir register, samarbetsytor blir permanenta system of record och enkla appar blir verksamhetssystem utan motsvarande förvaltning.

## Jämförelse mellan scenarierna

De sju scenarierna delar många byggstenar men skiljer sig i **vad som driver arkitekturen, vilken gemensam artefakt som betyder mest och vilken frihetsgrad som behöver finnas kvar lokalt**.

| Scenario | Dominerande kvaliteter | Särskilt viktiga förmågor | Mest styrande gemensamma artefakt | Typisk lokal frihetsgrad |
|---|---|---|---|---|
| Internt handläggningsstöd | spårbarhet, kontinuitet, användbarhet | Process, Regler, Data, Interaktion | referensarkitektur för handläggning + workflow-/datamönster | hur mycket process och regler som ska externaliseras |
| Publik e-tjänst | säkerhet, användbarhet, prestanda, skalbarhet | Interaktion, Identitet, Integration, Data | kanal-/e-tjänstreferensarkitektur och gemensamma plattformstjänster | identitetsnivå, sessions- och exponeringsmodell |
| Integrationsintensivt system | interoperabilitet, förändringsbarhet, kontinuitet | Integration, Data, Driftbarhet | integrationsmönster och kontraktsstandarder | synkront/asynkront, kontrakt, leveranssemantik |
| Informationsutbyte över organisationsgräns | säkerhet, interoperabilitet, regelefterlevnad | Integration, Identitet/tillit, Data | gemensamma utbytesmönster och tillits-/säkerhetsstandarder | kvittenssemantik, incidentansvar, partsspecifika avtal |
| Containerbaserad tjänst | förvaltningsbarhet, förändringsbarhet, skalbarhet | Runtime, Leverans, Driftbarhet | paved road/plattformserbjudande | workloadens state, resursprofil och exponeringsmodell |
| AI-baserat verksamhetsstöd | verifierbarhet, informationsskydd, kvalitet, kostnad | AI/analys, Data, Identitet | AI-referensarkitektur, guardrails och gemensamma AI-tjänster | modell, källor, evalueringsnivå, mänsklig kontroll och verktygsåtkomst |
| Digital arbetsplats | användbarhet, informationsskydd, livscykel | Arbetsplats, Identitet, Data, AI | samarbetsprinciper, informationsmönster och produktivitetsplattform | yttyp, delning, retention, informationsklassning och ägarskap |

Matrisen visar varför en gemensam arkitektur inte bör försöka eliminera variation. Den bör i stället göra **rätt typ av variation synlig och hanterbar**.

## Vad som är gemensamt — och vad som varierar

Några slutsatser går igen i alla sju scenarier.

För det första är **en plattform aldrig hela arkitekturen**. Containerplattformen löser exekveringsfrågan men inte verksamhetsgränserna. Produktivitetssviten löser samarbetsbehov men inte system-of-record-frågan. AI-plattformen löser modellåtkomst men inte tillitsfrågan.

För det andra är **samma mönster olika viktigt i olika sammanhang**. Tjänsteidentitet och observerbarhet förekommer i många scenarier eftersom de är tvärgående mekanismer. Human workflow är däremot starkt situationsberoende. Att något finns i en referensarkitektur betyder därför inte att det ska användas i varje instans.

För det tredje är **kvalitetsprofilen den viktigaste differentieraren inom samma scenarioklass**. Två publika e-tjänster kan se lika ut funktionellt men behöva olika identitetsnivå, redundans och loggning. Två AI-stöd kan använda samma modell men kräva helt olika mänsklig kontroll beroende på konsekvensen av ett fel.

För det fjärde finns det ett återkommande mönster i vad som bör standardiseras och vad som bör lämnas öppet. Gemensam arkitektur kan med fördel standardisera språk, kontrakt, guardrails, paved roads och återanvändbara startpunkter. Den konkreta lösningen måste däremot fortfarande äga sin kvalitetsprofil, sina domängränser och sina medvetna avsteg. Det är denna ansvarsfördelning — snarare än en gemensam komponentlista — som gör modellen skalbar över olika scenarier.

## Referensarkitektur som hypotes, inte facit

Det är lockande att se en välskriven referensarkitektur som ett svar. En mer användbar syn är att se den som en förkvalificerad hypotes:

> För den här typen av behov brukar dessa förmågor, ansvar, mönster och plattformar vara relevanta. Verifiera dem mot den konkreta situationen.

Det gör återkopplingen från verkliga lösningar viktig. Om många lösningar av samma typ gör samma avsteg kan referensarkitekturen vara fel eller ofullständig. Om nästan ingen använder en rekommenderad byggsten kan det bero på låg plattformskvalitet, dålig dokumentation eller att rekommendationen inte längre motsvarar behoven.

En levande referensarkitektur bör därför mätas mot faktisk användning och kunna förändras när verksamhetsbehoven, tekniken eller de gemensamma plattformarna förändras. Det leder direkt till bokens avslutande kapitel. När förmågekarta, principer, mönster, plattformstjänster, standarder och referensarkitekturer väl finns är huvudfrågan inte hur de produceras en gång, utan hur hela systemet hålls relevant och användbart över tid utan att governance blir en flaskhals.
