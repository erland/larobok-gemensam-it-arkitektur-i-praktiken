# 28. När ett byggblock blir en plattformstjänst

Det är lätt att kalla något för en plattform därför att det är centralt installerat, tekniskt avancerat eller används av flera team. Men central infrastruktur är inte automatiskt en plattformstjänst. Ett kluster, en databasmotor, en meddelandebroker eller ett identitetssystem kan vara viktiga tekniska byggblock utan att vara ett konsumtionsbart erbjudande.

Skillnaden uppstår först när organisationen kan svara tydligt på frågor som: Vad får konsumenten? Vilket problem löser tjänsten? Hur ansluter man sig? Vilka kvaliteter kan man räkna med? Vad ansvarar konsumenten själv för? Vad händer när något går fel? Hur utvecklas och avvecklas tjänsten?

Det här kapitlet handlar om övergången från tekniskt byggblock till ett förvaltat, begripligt och återanvändbart tjänsteerbjudande.

## Från teknisk komponent till konsumerbart erbjudande

Ett tekniskt byggblock är något en lösning kan byggas av. Ett plattformserbjudande är något ett team kan konsumera med förutsägbart ansvar och förutsägbara egenskaper.

```text
Tekniskt byggblock
    ↓
Paketerad funktion
    ↓
Definierat tjänstekontrakt
    ↓
Reproducerbar konsumtion
    ↓
Drift, support och livscykel
    ↓
Plattformstjänst
```

Anta att en organisation har ett OpenShift-kluster. Det betyder inte automatiskt att organisationen erbjuder en *Container Application Platform*. För att det ska vara ett verkligt tjänsteerbjudande behöver det exempelvis vara tydligt vilka workload-typer som stöds, hur team får tillgång, vilka nätverks- och identitetsintegrationer som ingår, vilken observerbarhet som finns, hur uppgraderingar hanteras och var gränsen går mellan plattformens och konsumentens ansvar.

Utan detta har man främst central infrastruktur med lokala integrationsproblem.

## Ett plattformserbjudande behöver ha ett tydligt syfte

Det första kravet är att tjänsten löser ett återkommande problem som flera konsumenter faktiskt har.

Det är inte tillräckligt att säga:

> Vi har en Kubernetesmiljö.

Ett tjänsteerbjudande behöver snarare uttrycka något i stil med:

> Vi erbjuder en förvaltad exekveringsmiljö för containeriserade applikationer med standardiserad driftsättning, grundläggande observerbarhet, nätverksintegration, identitetsintegration och definierade resursprofiler.

Den första formuleringen börjar med produkten. Den andra börjar med konsumentens behov och den kapacitet som erbjuds.

```text
Förmåga
  ↓
Behov hos konsumenter
  ↓
Plattformstjänst
  ↓
Tekniska byggblock
  ↓
Produkt / version / konfiguration
```

Produkten är en realisering. Tjänsten är det stabilare kontraktet mot konsumenten.

## Tjänstekontrakt, ansvar och konsumtion

När en teknisk komponent blir en tjänst uppstår ett kontrakt mellan den som tillhandahåller tjänsten och den som konsumerar den. Det behöver inte vara ett juridiskt dokument eller ett formellt SLA, men det måste vara tillräckligt tydligt för att två team ska kunna samarbeta utan att bygga sitt arbete på antaganden.

Ett användbart kontrakt behöver åtminstone ange:

1. vilket behov och vilka användningsfall tjänsten stöder,
2. vilka användningsfall som ligger utanför erbjudandet,
3. vad plattformsområdet respektive konsumenten ansvarar för,
4. vilka kvaliteter och begränsningar som gäller,
5. hur tjänsten beställs, provisioneras, ändras och avvecklas,
6. hur support, incidenter och eskalering fungerar,
7. hur förändringar och livscykel kommuniceras,
8. vilka kostnader, kvoter eller kapacitetsgränser som är relevanta.

Ta en API Management-tjänst som exempel. Plattformen kan ansvara för gatewayfunktion, teknisk exponering, policy enforcement, grundläggande autentiseringsintegration, throttling och teknisk loggning. Konsumenten behöver fortfarande ansvara för API-kontraktets semantik, verksamhetsägarskap, versionsstrategi, korrekt auktorisationslogik och datakvalitet.

Om plattformen börjar ta ansvar för dessa delar flyttar den sig in i domänansvar. Om konsumenten däremot måste bygga egen gateway, egen throttling, egen certifikathantering och egen loggning har plattformen inte abstraherat tillräckligt mycket av den återkommande tekniska friktionen.

Konsumtionsmodellen är en del av samma kontrakt. Den kan bygga på API, portal, CLI, GitOps, infrastructure-as-code, service request eller en kombination. Det viktiga är att konsumtionen är reproducerbar och går att förstå över tid. Om en enskild specialist måste göra manuella ändringar på konsumentens vägnar är plattformen organisatoriskt svår att skala även om tekniken skalar utmärkt.

Support hör också till kontraktet. Konsumenten behöver veta vad som räknas som plattformsfel, vilket felsökningsansvar som ligger lokalt, vilka signaler båda sidor kan se och hur återkommande problem återförs till tjänstens utveckling. Supportärenden är därför inte bara en kostnad utan också data om plattformens användbarhet.

Ett tydligt ansvarssnitt blir särskilt viktigt under incidenter. Om tjänsten fungerar tekniskt men konsumenten använder den utanför sin avsedda profil behöver det gå att avgöra var analysen börjar och vem som fattar beslut om korrigerande åtgärder. Om samma typ av incident återkommer hos flera konsumenter är det däremot ofta ett tecken på att plattformens kontrakt, defaultvärden eller automation behöver förbättras.

Detta gör tjänstekontraktet till mer än dokumentation. Det är den praktiska gränsen mellan gemensamt ansvar och lösningsansvar och bör kunna användas både vid arkitekturval, onboarding, drift och incidenthantering.

## Plattformen ska abstrahera återkommande komplexitet

En viktig anledning att skapa en plattformstjänst är att ta bort komplexitet som inte ger konsumentteamet verksamhetsfördelar.

Ett team som bygger ett handläggningssystem behöver förstå sin domänmodell, sina processer och sina kvalitetskrav. Det bör däremot inte behöva bli expert på hur databasservern patchas, certifikat roteras, meddelandekluster uppgraderas eller underliggande noder livscykelhanteras.

Plattformens uppgift är inte att dölja all teknisk komplexitet. Det skulle kunna skapa farliga abstraktioner. Uppgiften är att äga den komplexitet som med fördel kan bäras gemensamt och exponera ett kontrakt som är enkelt nog att konsumera men transparent nog för välgrundade arkitekturbeslut.

```text
Underliggande komplexitet
        ↓
Plattformsansvar
        ↓
Stabilt konsumtionsgränssnitt
        ↓
Konsumentens lösningsansvar
```

## Onboarding och självservice

Onboarding är inte dokumentation runt tjänsten; för konsumenten är den en del av själva erbjudandet. En tekniskt avancerad plattform med dålig onboarding kan därför ge lägre värde än en enklare plattform som är lätt att förstå och börja använda.

En fungerande onboarding behöver hjälpa konsumenten att:

- **förstå** om tjänsten passar behovet och vilka begränsningar som gäller,
- **ansluta** genom en tydlig och reproducerbar väg,
- **operera** tjänsten genom synlig status, kända supportvägar och tydliga förändrings- och avvecklingsprocesser.

Självservice är ofta ett mognadstecken, men betyder inte att allt måste vara öppet och omedelbart. Den normala konsumtionsvägen ska vara förutsägbar, dokumenterad och så automatiserad som riskbilden tillåter.[K1]

Exempel kan vara att skapa en databas från en godkänd profil, registrera ett API, skapa ett meddelandetopic, begära en workload-identitet eller skapa ett projekt i en containerplattform. Guardrails kan fortfarande kräva exempelvis informationsklassning, kostnadsställe eller återställningsprofil.

Kapitel 30 fördjupar hur denna konsumtionsväg kan utvecklas till golden paths, paved roads och mer omfattande självservice. Här räcker det att konstatera att ett erbjudande som bara kan konsumeras genom personberoende specialistarbete fortfarande har en svag tjänsteform, även om den underliggande tekniken är gemensam.

## Kvalitetsprofiler och tjänstenivåer

Ett plattformserbjudande bör inte bara lista funktioner. Det behöver beskriva vilka kvaliteter konsumenten kan bygga sin lösning på.

För en databastjänst kan det exempelvis vara relevant att beskriva profiler för tillgänglighet, backup, återställningstid, kapacitet, kryptering och supporthorisont. För en containerplattform kan motsvarande egenskaper vara resursgränser, autoskalning, nodspridning, nätverksprofil, loggretention och persistent storage.

Standardiserade kvalitetsprofiler är ofta bättre än individuella överenskommelser:

| Profil | Tillgänglighet | Backup/recovery | Support | Typisk användning |
|---|---|---|---|---|
| Bas | normal kontorstidskritikalitet | standard | kontorstid | interna stödverktyg |
| Kritisk | högre redundans | förstärkt | utökad | centrala verksamhetssystem |
| Experiment | lägre garanti | begränsad | best effort | prototyp och utvärdering |

Tabellen är illustrativ. Poängen är att kvalitetsnivån blir en del av erbjudandet i stället för något som varje lösning förhandlar fram i efterhand.

SLO och SLA ska samtidigt bara beskriva sådant plattformen faktiskt kan påverka och mäta. Plattformens service level, konsumentens applikations-SLO och verksamhetens end-to-end-behov hänger ihop men är inte samma sak.

Det betyder exempelvis att en databastjänst kan ange tillgänglighet, backupfrekvens och återställningsmål för själva databastjänsten, men inte garantera hela verksamhetssystemets tillgänglighet. Applikationsfel, felaktig konfiguration eller beroenden till andra tjänster ligger utanför plattformens direkta kontroll. Kvalitetsprofilen behöver därför vara tillräckligt konkret för att kunna användas i lösningens end-to-end-analys utan att ge sken av ett bredare ansvar än plattformen faktiskt har.

## Plattformens livscykel är större än produktens

Ett plattformserbjudande behöver överleva enskilda produktversioner och ibland även produktbyten.

Om en *relationell databastjänst* i dag realiseras med en viss produkt bör konsumenterna även efter ett framtida produktbyte känna igen centrala begrepp som databasinstans, kapacitetsprofil, backup-policy, restoreprocess, säkerhetsprofil och supporthorisont.

Allt kan inte göras produktoberoende. Produktbyte kan kräva migrering och skapa kompatibilitetsproblem. Men ju bättre tjänstekontraktet är separerat från realiseringen, desto mindre risk att organisationens gemensamma arkitektur blir en katalog över tillfälliga produktnamn.

Kapitel 32 fördjupar den kontrollerade förändringen, migrationen och avvecklingen över tid. På tjänstenivå behöver kapitel 28 bara etablera att förändring måste kommuniceras i termer som konsumenten förstår: vilka profiler som ändras, när stöd upphör, vilken migreringsväg som finns och vilka delar av kontraktet som består även när tekniken under byts ut.

## En gemensam tjänst behöver inte ha en enda realisering

Ett erbjudande motsvarar inte nödvändigtvis en enda produktinstallation.

En Relationell databastjänst kan ha flera realiseringar för olika workload-typer. Ett identitetserbjudande kan kombinera katalog, federation, PKI och secrets management. Ett observerbarhetserbjudande kan bestå av flera byggblock för loggar, mätvärden och tracing.

Det omvända gäller också: en stor produkt kan realisera flera tjänsteerbjudanden. Produktgränsen är därför inte automatiskt rätt tjänstegräns.

## När bör man inte skapa en plattformstjänst?

Att paketera något som tjänst skapar kostnader för ägarskap, dokumentation, support, livscykel och automation. Ett byggblock bör därför inte göras till gemensamt erbjudande bara för att det är tekniskt möjligt.

Varningssignaler är exempelvis att:

- behovet bara finns hos ett enskilt team,
- användningsfallen är så olika att ett gemensamt kontrakt blir artificiellt,
- tekniken förändras så snabbt att erbjudandet saknar stabil kärna,
- inget team har mandat eller kapacitet att bära supportansvaret,
- konsumenterna ändå måste förstå och förvalta nästan hela den underliggande tekniken,
- samordningskostnaden blir större än den friktion tjänsten tar bort.

I sådana fall kan en standard, ett rekommenderat mönster eller ett referensbyggblock vara bättre än en full plattformstjänst.

Detta är en viktig motvikt till plattformstänkandet. En organisation kan vinna mycket på gemensamma krav, arkitekturmönster, automation eller dokumenterade produktprofiler utan att skapa ett centralt operativt beroende. Frågan är därför inte om återanvändning är önskvärd, utan vilken nivå av gemensamhet som bäst motsvarar behov, kvalitetskrav och organisatorisk förmåga att bära ansvaret.

## Plattformskatalogen ska beskriva erbjudanden

En plattformskatalog blir lätt en inventarielista över OpenShift, Oracle, IBM MQ, Jenkins, Elasticsearch eller Microsoft 365. Det är användbart för asset management men inte samma sak som en tjänstekatalog.

En arkitektonisk plattformskatalog bör i första hand uttrycka erbjudanden som Container Application Platform, Relationell databastjänst, Enterprise Messaging, CI/CD Platform, *Search and Indexing Service* och Productivity Suite. Produkten kan anges som aktuell realisering under erbjudandet.

Det gör katalogen mer robust över tid och hjälper konsumenten att börja med behovet i stället för produktnamnet. Katalogposten bör därför kunna visa vilket behov erbjudandet möter, vilka förmågor det bidrar till, målgrupp, profiler, ansvarssnitt och aktuell realisering. Produktinventeringen kan fortfarande finnas, men den fyller ett annat syfte.

## Konkreta exempel

### Databasserver kontra relationell databastjänst

Ett centralt databaskluster där team får ett schema genom ett manuellt ärende är ett gemensamt tekniskt byggblock. För att bli Relationell databastjänst behöver organisationen dessutom definiera stödda profiler, ansvar, provisioning, backup/restore, kapacitet, support, relevanta tjänstenivåer och livscykel.

Tekniken kan vara densamma före och efter. Skillnaden är att relationen till konsumenten har blivit en tjänst. Ett team kan då fatta ett arkitekturbeslut utifrån en beskriven profil i stället för att först behöva förhandla med en driftgrupp om hur den centrala databasen råkar vara uppsatt.

### Meddelandebroker kontra Enterprise Messaging

En centralt förvaltad broker kan ta emot meddelanden. Ett plattformserbjudande behöver dessutom beskriva vilka kommunikationsmönster som stöds, hur queues/topics provisioneras, kvoter, retention, säkerhetsmodell, protokoll, observerbarhet, dead-letter-hantering och support.

Plattformen ska däremot inte bestämma meddelandenas verksamhetssemantik. Det ansvaret ligger hos de domäner som publicerar och konsumerar informationen. Erbjudandet blir därmed gemensamt på den tekniska nivån utan att skapa en central verksamhetsmodell.

### Containerkluster kontra Container Application Platform

Ett containerkluster blir ett erbjudande först när team kan behandla det som en definierad exekveringstjänst. Konsumenten kan exempelvis ansvara för image, health checks, resursbehov och applikationskonfiguration, medan plattformen ansvarar för kluster, noder, uppgraderingar, nätverks- och identitetsintegration samt grundläggande observerbarhet.

Det är ansvarskontraktet och konsumtionsvägen, inte förekomsten av Kubernetes eller OpenShift i sig, som gör detta till en plattformstjänst. Om olika workload-typer kräver olika isolering, tillgänglighet eller driftsmodell kan samma tjänst dessutom behöva flera profiler eller realiseringar i stället för att alla applikationer pressas in i en universell plattform.

## En praktisk mognadstrappa

Övergången från byggblock till tjänst kan beskrivas kompakt:

1. **Gemensam teknik** – central teknik finns men användning och ansvar är personberoende.
2. **Paketerat erbjudande** – syfte, målgrupp, ansvar och begränsningar är dokumenterade.
3. **Reproducerbar konsumtion** – onboarding, provisioning och standardkonfiguration är dokumenterade och i hög grad automatiserade.
4. **Operativ tjänst** – support, observerbarhet, incidenthantering och livscykel ingår i erbjudandet.
5. **Produktliknande plattform** – tjänsten utvecklas aktivt utifrån konsumentbehov, adoption och återkommande friktion.

Den sista nivån leder vidare till nästa kapitel om Platform as a Product. Mognadstrappan ska inte läsas som ett krav på att alla byggblock måste nå nivå 5. Vissa tekniska komponenter bör stanna som gemensamma byggblock eller standardiserade realiseringar. Trappan är främst ett sätt att synliggöra vilket ansvar organisationen faktiskt tar på sig när den kallar något för plattformstjänst.

## Ansvar på tre nivåer

Den gemensamma nivån bör definiera vad som menas med plattformstjänst och vilka minimikrav som gäller för erbjudanden. Förmåge- eller plattformsansvaret definierar tjänsten, dess kontrakt, kvalitetsprofiler, konsumtionsväg och realisering. Konsumentteamet bedömer om tjänsten möter lösningens behov, väljer relevant profil och uppfyller sitt konsumentansvar.

Poängen är att ansvar följer tjänstens räckvidd utan att varje plattform behöver detaljstyras centralt. Den gemensamma nivån sätter spelreglerna, plattformsnivån formar erbjudandet och lösningsnivån avgör om erbjudandet faktiskt passar den aktuella användningen.

## Vanliga anti-patterns

- **Produktnamnet är tjänsten.** Erbjudandet beskriver inte vilket konsumentproblem det löser.
- **Plattform som central ticket-kö.** All konsumtion kräver manuella specialistanpassningar.
- **Obegränsat plattformsansvar.** Plattformsteamet förväntas bära konsumentens domän- och applikationsansvar.
- **Obegränsat konsumentansvar.** Plattformen levererar rå teknik men ingen återanvändbar konsumtionsmodell.
- **Falsk standardisering.** Alla användningsfall pressas in i samma profil trots olika kvalitetsbehov.
- **Ingen avvecklingsväg.** Tjänsten kan beställas men saknar definierad väg för migrering och avregistrering.
- **Tjänstenivåer utan mätbarhet.** Löften ges utan telemetri eller faktisk kontroll över kvaliteten.

## Praktisk analysordning

När ett tekniskt byggblock övervägs som gemensam plattformstjänst kan följande ordning användas:

1. Identifiera det återkommande konsumentbehovet.
2. Definiera avsedda användningsfall och tydliga icke-mål.
3. Dra gränsen mellan plattforms- och konsumentansvar.
4. Definiera tjänstekontrakt och kvalitetsprofiler.
5. Utforma reproducerbar onboarding och konsumtion.
6. Designa support, observerbarhet och incidentmodell.
7. Separera tjänstekontraktet från dagens tekniska realisering.
8. Definiera förändring och avveckling på tjänstenivå.
9. Mät ledtid, användning, fel, supportärenden och återkommande avsteg.
10. Ompröva om tjänsten fortfarande bör vara gemensam.

## Centrala fakta

- Ett tekniskt byggblock blir inte en plattformstjänst bara genom central installation eller gemensam drift.
- En plattformstjänst behöver ett tydligt konsumentproblem, ett tjänstekontrakt och ett explicit ansvarssnitt.
- Onboarding, support, observerbarhet och livscykel är delar av erbjudandet, inte sidoaktiviteter.
- Självservice handlar främst om reproducerbar och förutsägbar konsumtion[K1], inte om frånvaro av styrning.
- Kvalitetsprofiler gör erbjudandet mer användbart än individuella och ad hoc-baserade överenskommelser.
- Produkt och plattformstjänst bör hållas isär: produkten är en realisering av tjänsten.
- En plattformstjänst kan bestå av flera tekniska byggblock, och en produkt kan realisera flera tjänster.
- Det är inte alltid rätt att skapa en plattformstjänst; ibland är en standard, ett mönster eller ett referensbyggblock tillräckligt.
- När ett erbjudande utvecklas aktivt utifrån konsumentbehov och användningsdata närmar det sig Platform as a Product.

## Källor och vidare läsning

**[K1]** CNCF TAG App Delivery, *CNCF Platforms White Paper*, om plattformar som självbetjänade, användarorienterade erbjudanden. https://tag-app-delivery.cncf.io/whitepapers/platforms/
