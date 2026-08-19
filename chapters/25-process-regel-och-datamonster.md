# 25. Process-, regel- och datamönster

Processer, regler och data hör nära ihop i nästan varje verksamhetssystem. En process behöver information för att veta var den befinner sig. Ett beslut behöver fakta att bedöma. Data förändras när processen går vidare eller ett beslut fattas. Det är därför frestande att låta en enda komponent bära allt detta ansvar: processmotorn får bli systemets minne, regelmotorn får styra hela flödet och databasen får fungera som både integrationspunkt, cache och historik.

Det är också där många lösningar börjar tappa sina tydliga gränser.

Kapitel 13–15 beskrev förmågorna Process, workflow och ärendehantering, Regler och beslut samt Data- och informationshantering. I det här kapitlet ligger fokus i stället på fyra återkommande lösningsmönster:

- *Human workflow*,
- *externaliserade verksamhetsregler*,
- *system of record och härledda kopior*,
- cache-aside.

Mönstren löser olika problem. Human workflow gör långlivat arbete och mänskliga uppgifter explicita. Externaliserade regler ger vissa beslut en egen livscykel och spårbarhet. System of record med härledda kopior tydliggör vilken representation som är auktoritativ när information behöver finnas på flera ställen. Cache-aside förbättrar läsprestanda genom att låta en återskapbar kopia ligga nära användningen.

Det viktiga är inte att använda alla fyra. Det viktiga är att kunna avgöra vilket ansvar som behöver göras explicit, var det ska ligga och vad som fortfarande måste vara sant när flera mönster kombineras.

## Börja med ansvar, inte motorer

En vanlig diskussion börjar med teknik:

> Behöver vi en workflowmotor, regelmotor och cacheplattform?

Det är oftast för tidigt. En bättre start är att identifiera de olika ansvar som lösningen faktiskt behöver bära.

Exempelvis:

```text
Verksamhetsprocess
  ├─ väntar på mänskligt arbete
  ├─ behöver fatta ett beslut
  ├─ läser auktoritativa fakta
  └─ visar information snabbt i ett användargränssnitt
```

Dessa fyra behov kan motivera fyra olika mekanismer, men inte nödvändigtvis fyra separata produkter. Mönstren beskriver ansvar och struktur. Plattformen är en möjlig realisering.

Det ger också en viktig grundregel:

> En mekanism får gärna hjälpa flera delar av lösningen, men den bör inte oavsiktligt bli ägare till ansvar som hör hemma någon annanstans.

En processmotor bör exempelvis inte bli auktoritativ källa för all verksamhetsinformation bara därför att den behöver processvariabler. En regelmotor bör inte bli en dold databas. En cache bör inte börja behandlas som system of record därför att den råkar svara snabbast.

## Human workflow – när väntan är en del av verksamheten

Human workflow används när en verksamhetsprocess innehåller mänskliga arbetsuppgifter som behöver tilldelas, följas upp och återupptas över tid.

En förenklad struktur är:

```text
Processinstans
   ├─ automatiskt steg
   ├─ human task → arbetskö eller användare
   ├─ väntan
   ├─ beslut
   └─ nästa steg
```

Det centrala är inte att en människa klickar på en knapp. Mänsklig interaktion finns i nästan alla system. Det arkitektoniskt intressanta uppstår när själva väntan och arbetsuppgiften måste vara beständiga verksamhetsobjekt.

Det kan exempelvis krävas att lösningen vet:

- vem eller vilken roll som ansvarar för uppgiften,
- när uppgiften skapades,
- vilken deadline som gäller,
- om den har delegerats,
- när den ska eskaleras,
- vilket underlag som fanns när arbetet startade,
- vad som händer om processen startas om,
- hur processen fortsätter när uppgiften är klar.

Då räcker inte en vanlig HTTP-request som väntar på svar. Processen kan leva i dagar eller månader och måste överleva både användarsessioner och tekniska omstarter.

### Human task är inte samma sak som ärende

Det är viktigt att skilja mellan en arbetsuppgift och det verksamhetsobjekt som arbetet gäller.

Anta att en handläggare ska granska en ansökan. Ansökan är ett verksamhetsobjekt. Arbetsuppgiften ”Granska ansökan” är en aktivitet i en process. Processinstansen beskriver hur arbetet rör sig framåt.

Om dessa begrepp blandas ihop kan processmotorn börja bli den enda plats där verksamhetens tillstånd finns. Det gör senare integration, rapportering, migrering och förändring svårare.

En robustare ansvarsfördelning kan se ut så här:

```text
Verksamhetsdata
   ↑
Domäntjänst
   ↑
Processinstans
   ├─ arbetsuppgift A
   ├─ vänteläge
   └─ arbetsuppgift B
```

Processinstansen behöver referera till verksamhetsobjektet och kan bära processnära metadata, men den behöver inte duplicera hela objektets auktoritativa tillstånd.

### När human workflow passar

Mönstret är särskilt användbart när:

- manuella aktiviteter är en del av ett längre flöde,
- arbete behöver tilldelas roller, grupper eller köer,
- deadlines, påminnelser och eskalering behövs,
- processen måste kunna pausas och återupptas,
- status och historik behöver följas över tid,
- flera mänskliga och automatiserade steg behöver koordineras.

Det passar sämre när flödet är kort, lokalt och helt bundet till ett användargränssnitt. Om en användare fyller i tre formulärsteg under samma session behövs inte nödvändigtvis ett beständigt workflowobjekt.

### Den dolda kostnaden: processversionering

När en processmodell förändras kan redan startade processinstanser fortfarande följa den gamla modellen. Det skapar frågor som inte finns i samma form i vanlig request/response-logik:

- Ska pågående instanser fortsätta på gammal version?
- Kan de migreras till ny modell?
- Vad händer om ett nytt steg införs mitt i processen?
- Hur länge behöver gammal processdefinition kunna exekveras?

Human workflow ger alltså spårbarhet och styrbarhet, men gör också processens livscykel explicit. Den kostnaden är motiverad när processen verkligen behöver leva över tid. Annars kan mönstret bli mer förvaltning än nytta.

## Externaliserade verksamhetsregler – ge rätt logik en egen livscykel

Externaliserade verksamhetsregler används när viss beslutslogik behöver kunna förstås, förändras, versioneras eller återanvändas mer självständigt än applikationens övriga kod.

En förenklad struktur kan vara:

```text
Domän- eller processtjänst
        ↓
      Beslut
        ↓
 Regel-/beslutskomponent
        ↓
  beslut + förklaring
```

Mönstret betyder inte att all `if`-logik ska flyttas ur programkoden. Det handlar om att identifiera regler som har ett självständigt verksamhetsvärde.

Exempel kan vara:

- ett regelverk som ändras oftare än resten av applikationen,
- samma beslut som behöver användas i flera processer,
- ett beslut där den exakta regelversionen måste kunna förklaras i efterhand,
- beslutstabeller som verksamhetsexperter behöver kunna granska,
- regler vars giltighet varierar över tid.

### Externalisering är en ansvarsförflyttning

När regler externaliseras flyttas inte bara kod. Lösningen introducerar ett nytt förvaltningsobjekt.

Det behöver då finnas svar på frågor som:

- Vem äger regelns innebörd?
- Vem får ändra den?
- Hur testas den?
- Hur publiceras den?
- När börjar en ny version gälla?
- Hur kopplas ett historiskt beslut till rätt regelversion?
- Hur hanteras beroenden mellan regler?

Detta är mönstrets verkliga kostnad. Om regeln är liten, lokal och förändras exakt tillsammans med applikationskoden kan externalisering skapa fler livscykler utan att lösa ett faktiskt problem.

### Regelmotorn ska inte äga processen

Workflow och regler kombineras ofta, men de löser olika frågor.

En processmodell svarar främst på:

> Vad händer härnäst och vad väntar vi på?

En regelmodell svarar främst på:

> Vilket beslut följer av dessa fakta och regler?

Det kan illustreras så här:

```text
Process
  ↓
Samla beslutsunderlag
  ↓
Anropa beslut
  ↓
Beslut: godkänn / komplettera / avslå
  ↓
Processen väljer nästa aktivitet
```

Regelkomponenten bör normalt inte behöva känna till hela processens historia för att fatta beslutet. Processen bör i sin tur inte duplicera den verksamhetsregel som beslutstjänsten redan äger.

Detta gör reglerna lättare att återanvända och processen lättare att förstå.

### Regler behöver fakta – inte dold dataägarskap

En regelmotor kan behöva många fakta. Det betyder inte att den bör slå upp godtycklig information över hela IT-landskapet eller bygga en egen dold kopia av verksamhetsdata.

Ett tydligare mönster är att den som begär beslutet levererar ett explicit beslutsunderlag:

```text
Beslutsbegäran
  ├─ fakta A
  ├─ fakta B
  ├─ tidpunkt
  └─ relevant kontext
        ↓
     Regelverk
        ↓
Beslut + regelversion + motivering
```

Det ger bättre spårbarhet. Man kan senare se vilka fakta och vilken regelversion som ledde till beslutet.

Om regelkomponenten själv hämtar data från många källor blir det svårare att återskapa det historiska beslutsögonblicket. Fakta kan ha förändrats sedan dess.

## System of record och härledda kopior – separera sanning från representation

Data behöver ofta finnas på flera platser. Ett system kan ha en transaktionell databas, ett sökindex, ett analyslager, en lokal read model och flera cachelager samtidigt.

Det är inte kopiorna i sig som är problemet. Problemet uppstår när ingen längre vet vilken representation som har tolkningsföreträde.

Mönstret system of record och härledda kopior gör denna relation explicit.

```text
             ┌→ sökindex
System of    ├→ analyslager
record ──────┼→ lokal read model
             └→ cache
```

System of record är den auktoritativa källan för den aktuella informationsmängden. De andra representationerna finns därför att de löser andra behov: snabbare läsning, sökning, rapportering, lokal autonomi eller annan åtkomstform.

### En kopia behöver ett kontrakt mot sin källa

Varje härledd kopia bör kunna beskrivas genom åtminstone fem frågor:

1. Vilken källa är auktoritativ?
2. Hur uppdateras kopian?
3. Hur gammal får informationen vara?
4. Hur upptäcks och hanteras avvikelser?
5. Kan kopian återskapas från sin källa?

Dessa frågor omvandlar ”vi replikerar lite data” till ett medvetet arkitekturval.

Exempel:

```text
Sökindex för ärenden
- källa: Ärendetjänstens verksamhetsdatabas
- uppdatering: event efter relevanta förändringar
- tolererad aktualitet: 30 sekunder
- avvikelsekontroll: periodisk reconciliationskörning
- återbyggnad: full omsynkning från auktoritativ källa
```

Det är en mycket starkare beskrivning än att bara dokumentera vilken sökprodukt som används.

### Härledd betyder inte oviktig

En härledd kopia kan vara kritisk för tjänstens funktion även om den inte är auktoritativ.

Om en publik söktjänst är helt beroende av sitt index kan indexet ha höga krav på tillgänglighet och återställning. Men dess återställningsstrategi kan ändå skilja sig från system of record. Om indexet kan byggas om kanske traditionell backup är mindre viktig än en snabb, verifierad rebuild-process.

Mönstret hjälper därmed inte bara informationsägarskap. Det påverkar även kontinuitetsdesign, observerbarhet och kostnad.

### Kopior får inte bli nya sanningar av bekvämlighet

En vanlig glidning ser ut så här:

1. En lokal kopia skapas för läsprestanda.
2. Någon upptäcker att det är enklast att korrigera data direkt i kopian.
3. Ytterligare funktioner börjar skriva där.
4. Kopian innehåller till slut information som inte kan återskapas från källan.
5. Ingen vet längre vilken källa som gäller.

Då har den härledda representationen bytt ansvar utan att arkitekturen har erkänt det.

Om en kopia behöver bli skrivbar och bära egen information bör det behandlas som ett nytt arkitekturbeslut. Kanske har en ny domängräns eller ett nytt system of record faktiskt uppstått.

## Cache-aside – en specialiserad och medvetet förgänglig kopia

Cache-aside är ett mer specifikt datamönster. Applikationen läser först från en cache. Om värdet saknas hämtas det från den auktoritativa källan och läggs sedan i cachen.

```text
Applikation
   ↓
Läs cache
   ├─ träff → använd värdet
   └─ miss
        ↓
   Läs system of record
        ↓
   Skriv till cache
        ↓
      svar
```

Mönstret är attraktivt eftersom det kan ge stora prestandavinster utan att den auktoritativa datamodellen behöver förändras. Men det fungerar bara om organisationen accepterar att cacheinnehållet är en förgänglig och potentiellt inaktuell representation.

### Den centrala frågan är inte TTL utan tolererad felaktighet

Cache diskuteras ofta tekniskt genom Time To Live, TTL. Men TTL är bara en mekanism. Den egentliga arkitekturfrågan är:

> Hur gammal eller felaktig får informationen vara innan konsekvensen blir oacceptabel?

Om en produktbeskrivning visas med fem minuters fördröjning kan det vara helt acceptabelt. Om samma cache används för ett aktuellt behörighetsbeslut kan fem minuter vara alldeles för länge.

Utgångspunkten bör därför vara verksamhets- och säkerhetskonsekvensen. Därifrån kan en lämplig invalidation- eller TTL-strategi härledas.

### Cache invalidation är en ägarskapsfråga

När källan förändras behöver cachen förr eller senare förstå att den gamla representationen inte längre gäller.

Det finns flera möjliga strategier:

- kort TTL och acceptans av viss stale data,
- explicit invalidation vid förändring,
- uppdatering av cache genom event,
- versions- eller etag-baserad kontroll,
- ingen invalidation alls eftersom värdet bara används inom en mycket kort period.

Ingen strategi är universellt bäst. Valet styrs av:

- förändringsfrekvens,
- läsfrekvens,
- tolererad inaktualitet,
- konsekvens av felaktig data,
- belastning på system of record,
- komplexitet i synkroniseringsmekanismen.

Det är också därför cache-aside bör ses som ett mönster ovanpå system of record och härledda kopior. Cache är en typ av härledd kopia med särskilda prestandaegenskaper.

### Cache stampede och andra sekundära effekter

Om ett populärt cachevärde löper ut samtidigt för många användare kan alla begäranden gå vidare till system of record samtidigt. Belastningen kan då bli större än om ingen cache hade funnits.

Detta brukar beskrivas som cache stampede eller thundering herd. Lösningen kan kräva exempelvis:

- låsning eller single-flight vid återladdning,
- spridning av TTL-värden,
- background refresh,
- stale-while-revalidate-liknande beteende,
- kapacitetsdesign för cachemissar.

Det visar en viktig generell princip: ett prestandamönster förändrar också failure modes. Cache ska därför inte bara dimensioneras för normalfallet utan även för vad som händer när den är tom eller otillgänglig.

### Skyddsvärd data i cache

Cache kan göra information mer spridd än den auktoritativa lagringen. Därför behöver man även ta ställning till:

- om informationen får cachas alls,
- hur länge den får ligga kvar,
- om den måste krypteras,
- vilka identiteter som får läsa den,
- hur tenant- eller användargränser upprätthålls,
- om loggning av cachekeys kan läcka information.

Prestandaoptimering får inte skapa en ny informationssäkerhetsmodell av misstag.

## Fyra mönster – fyra olika typer av tillstånd

När mönstren kombineras blir det särskilt viktigt att förstå att de kan bära olika slags tillstånd.

| Mönster/komponent | Typiskt tillstånd | Ska normalt vara auktoritativt för |
|---|---|---|
| Human workflow | processläge, väntan, arbetsuppgifter | processens exekveringsläge |
| Externaliserade regler | regeldefinitioner, versioner, giltighet | regelverkets innehåll |
| System of record | verksamhetsdata | definierad informationsmängd |
| Härledd kopia/cache | reproducerad eller temporär representation | normalt inget utöver sin egen tekniska status |

Tabellen visar varför ett system kan ha flera ”sanningar” utan motsägelse. De är auktoritativa för olika ansvar.

Processmotorn kan vara auktoritativ för att en viss arbetsuppgift väntar på handläggning samtidigt som verksamhetsdatabasen är auktoritativ för ärendets sakuppgifter. Regelregistret kan vara auktoritativt för vilken regelversion som gäller. Cachen är inte auktoritativ för något av detta.

Problemet uppstår först när gränserna blir otydliga.

## Ett genomgående exempel – från ansökan till beslut

Anta ett verksamhetsstöd där en person skickar in en ansökan. Ansökan ska granskas, vissa villkor bedömas och beslut fattas. Handläggaren behöver dessutom ett snabbt användargränssnitt.

En möjlig kombination är:

```text
                    ┌───────────────┐
                    │ Regelverk     │
                    │ version 12    │
                    └──────▲────────┘
                           │
                           │ beslut
                           │
┌──────────────┐    ┌──────┴───────┐
│ System of    │◄───│ Domäntjänst  │
│ record       │    └──────▲───────┘
└──────▲───────┘           │
       │                   │
       │ fakta             │
       │            ┌──────┴────────┐
       └────────────│ Human workflow│
                    └──────▲────────┘
                           │
                           │ arbetsuppgift
                           │
                    ┌──────┴────────┐
                    │ Handläggare   │
                    └───────────────┘

System of record ──→ cache/read model ──→ handläggarvy
```

Här har varje del ett tydligt ansvar:

- system of record äger ansöknings- och ärendedata,
- workflowinstansen äger processläge och arbetsuppgifter,
- regelkomponenten äger regeldefinition och regelversion,
- cache/read model optimerar läsning,
- domäntjänsten binder samman verksamhetsoperationerna.

När handläggningen når ett beslutsteg hämtas eller sammanställs nödvändiga fakta från den auktoritativa domänen. Dessa skickas tillsammans med relevant kontext till beslutskomponenten. Resultatet kan innehålla:

- beslut,
- regelversion,
- motivering eller träffade regler,
- tidpunkt.

Domäntjänsten registrerar den verksamhetseffekt som beslutet medför. Processen fortsätter därefter till nästa steg.

Detta är medvetet mer explicit än att låta workflowmotorn direkt läsa och skriva i alla tabeller, samtidigt som en regelmotor själv hämtar fakta från samma databas och en cache uppdateras genom specialskriven kod lite överallt.

## Snapshot eller live data – ett viktigt beslut i långlivade processer

Långlivade processer skapar en särskild fråga: ska ett senare steg använda aktuella fakta eller de fakta som gällde när processen startade?

Anta att en ansökan lämnas in den 1 mars men handläggs den 15 mars. Under tiden kan:

- personuppgifter ha ändrats,
- organisationstillhörighet ha förändrats,
- ett regelverk ha fått ny version,
- externa referensdata ha uppdaterats.

Det finns inget generellt rätt svar.

I vissa fall ska beslutet bygga på det aktuella läget. I andra fall behöver man rekonstruera exakt vilket underlag som gällde vid en viss verksamhetstidpunkt. Då kan lösningen behöva lagra ett snapshot, versionsreferenser eller temporal historik.

Det viktiga är att inte låta processmotorns råa processvariabler bli en oplanerad historikmodell. Historik och beslutsspårbarhet behöver utformas medvetet utifrån verksamhetskravet.

## Duplicerat tillstånd är inte automatiskt fel

Mönstren i detta kapitel innebär ofta att samma verksamhetsbegrepp representeras på flera ställen:

- ärende-id finns i processinstansen,
- ärendet finns i system of record,
- vissa fält finns i en read model,
- några attribut finns tillfälligt i cache,
- relevanta fakta kan sparas tillsammans med ett beslut.

Detta är inte nödvändigtvis skadlig duplicering. Tvärtom kan den vara en medveten del av en robust arkitektur.

Frågan är i stället:

> Har varje representation ett tydligt syfte, en definierad källa och en begriplig livscykel?

Duplicering blir problematisk när två representationer samtidigt förväntas vara auktoritativa för samma sak eller när synkroniseringsmodellen är okänd.

## När eventual consistency är en medveten egenskap

Härledda kopior och cache innebär ofta att alla representationer inte uppdateras exakt samtidigt.

Det kan vara helt acceptabelt om verksamheten förstår och accepterar fördröjningen.

Exempel:

```text
Beslut registreras i system of record
        ↓
Event publiceras
        ↓
Read model uppdateras inom några sekunder
        ↓
Handläggarvyn visar nytt tillstånd
```

Under några sekunder kan read model vara äldre än system of record. Arkitekturen behöver då svara på:

- hur lång fördröjning som är acceptabel,
- hur användaren märker att data kan vara på väg att uppdateras,
- hur missade uppdateringar upptäcks,
- hur kopian reconcileras,
- vilka operationer som måste gå direkt mot auktoritativ källa.

Eventual consistency är alltså inte bara en teknisk etikett. Det är ett kvalitets- och verksamhetsbeslut.

## Mönsterkombinationer behöver ha tydliga felgränser

När flera mönster kombineras uppstår nya failure modes.

Anta att workflowmotorn har markerat ett beslutsteg som slutfört men domäntransaktionen misslyckades. Eller att verksamhetsdata har uppdaterats men eventet som skulle uppdatera read model aldrig kom fram.

Då behöver lösningen avgöra var atomaritet faktiskt krävs och var kompensation, återförsök eller reconciliation används.

En användbar analys är att gå igenom varje gräns:

```text
Workflow → Domänoperation
Domänoperation → Beslutstjänst
System of record → Härledd kopia
Applikation → Cache
```

För varje gräns bör man fråga:

- Vad händer om anropet misslyckas före effekt?
- Vad händer om effekten sker men bekräftelsen försvinner?
- Kan operationen upprepas säkert?
- Hur upptäcks ett permanent avvikande tillstånd?
- Vem äger återställningen?

På så sätt kopplas mönstren tillbaka till integrations- och driftmönstren i kapitel 24 och 27 utan att deras ansvar blandas ihop.

## Vanliga anti-patterns

### Processmotorn som verksamhetsdatabas

Alla verksamhetsfält läggs som processvariabler eftersom de är lättåtkomliga där. Resultatet blir ett otydligt system of record och svår dataförvaltning.

### Regelmotorn som universell logikmotor

All villkorslogik externaliseras, även lokal teknisk och domänintern logik. Reglerna blir svåra att förstå och beroendena växer.

### Dold multi-master

Två system eller kopior kan båda uppdatera samma informationsmängd utan tydlig konfliktmodell eller ägarskap.

### Cache som permanent lagring

Lösningen börjar bero på information som bara finns i cache. En tömning blir då dataförlust i stället för ett normalt driftläge.

### TTL som verksamhetskrav

”Cachen har fem minuters TTL” dokumenteras utan att någon har bestämt om fem minuter gammal information faktiskt är acceptabel.

### Snapshot av allt

En långlivad process kopierar stora mängder verksamhetsdata ”för säkerhets skull”. Kopiorna blir snart svåra att klassificera, gallra och förstå.

### Direkt databasåtkomst från workflow och regler

Process- eller regelmotorn får bred åtkomst till domänens interna tabeller. Det skapar stark koppling till intern datamodell och gör domänansvaret svagare.

## Ansvar på tre nivåer

Precis som i tidigare kapitel behöver mönstren kunna användas utan att en central funktion designar varje lösning.

### Gemensam arkitekturnivå

Den gemensamma nivån bör framför allt:

- definiera vad organisationen menar med system of record, härledd kopia och cache,
- ange gemensamma principer för spårbarhet, informationsklassning och historik,
- tydliggöra när process- och regelmodeller får egna livscykler,
- etablera gemensamma krav på identitet, audit, driftbarhet och versionshantering,
- beskriva mönstren och deras gränser,
- säkerställa att gemensamma plattformserbjudanden inte tvingar fram mönster där de inte passar.

### Förmågenivå

Ansvariga för process-, regel- och dataförmågorna bör bland annat:

- förvalta respektive mönster och vägledning,
- erbjuda relevanta plattformstjänster,
- definiera rekommenderade integrations- och livscykelmodeller,
- ge stöd för versionering, migrering och observerbarhet,
- samordna gränssnitt där flera förmågor möts,
- följa upp återkommande problem och avsteg.

### Lösnings-/produktnivå

Den konkreta lösningen behöver besluta:

- om explicit workflow verkligen behövs,
- vilka regler som bör externaliseras,
- vilket system som är auktoritativt för vilken information,
- vilka kopior som behövs och varför,
- vilken aktualitet varje kopia måste ha,
- om cache ger tillräcklig nytta för sin komplexitet,
- hur fel och avvikelser mellan komponenterna hanteras,
- hur beslut och historik ska kunna rekonstrueras.

Den gemensamma arkitekturen ska göra dessa beslut enklare och mer konsekventa, inte fatta dem i förväg för alla system.

## En praktisk analysordning

När process, regler och data behöver kombineras kan följande ordning vara användbar.

### 1. Identifiera verksamhetsobjekten

Vad är det egentligen verksamheten hanterar? Ärende, ansökan, avtal, order, tillstånd eller något annat?

### 2. Bestäm auktoritativt ansvar

Vilken komponent eller domän äger respektive informationsmängd?

### 3. Identifiera väntan och långlivat arbete

Finns mänskliga uppgifter, externa svar eller andra väntelägen som behöver vara beständiga och spårbara?

### 4. Identifiera beslut med egen livscykel

Vilka regler eller beslut behöver versionering, förklarbarhet, återanvändning eller självständig förändring?

### 5. Identifiera läs- och åtkomstbehov

Behövs sökindex, read models, lokala kopior eller cache för att uppnå prestanda, autonomi eller annan åtkomstform?

### 6. Definiera varje kopias roll

För varje representation: källa, synkronisering, aktualitet, reconciliation och återuppbyggnad.

### 7. Definiera historikpunkter

Vilka fakta, regelversioner och processtillstånd måste kunna rekonstrueras i efterhand?

### 8. Analysera felgränser

Vad händer om en del lyckas och nästa misslyckas? Behövs återförsök, idempotens, kompensation eller manuell återställning?

### 9. Först därefter – välj teknisk realisering

Nu kan workflowmotor, regelmotor, databastjänst, cacheplattform och andra produkter bedömas mot de ansvar och kvalitetskrav som redan är tydliga.

## Det viktigaste att bära med sig

Process-, regel- och datamönster hjälper oss att göra olika sorters ansvar och tillstånd explicita.

Human workflow passar när mänskligt arbete och väntan behöver bli beständiga delar av processen. Externaliserade verksamhetsregler passar när vissa beslut behöver egen livscykel, spårbarhet eller återanvändning. System of record med härledda kopior gör det möjligt att duplicera information utan att tappa bort auktoriteten. Cache-aside är ett specialiserat sätt att använda en förgänglig kopia för bättre läsprestanda.

De fyra mönstren fungerar väl tillsammans just därför att de inte behöver äga samma sak.

En hållbar kombination bygger på att man kan svara på fyra frågor:

1. Vem äger processens tillstånd?
2. Vem äger regeln och beslutets betydelse?
3. Vilken källa är auktoritativ för verksamhetsinformationen?
4. Vilka kopior får vara tillfälliga eller inaktuella – och hur mycket?

När svaren är tydliga kan processer, regler och data utvecklas med olika livscykler utan att lösningen tappar sin sammanhållning. När svaren är otydliga hjälper ingen workflowmotor, regelmotor eller cacheplattform i världen till att skapa ordning.

I nästa kapitel flyttar vi samma mönsterperspektiv till ett annat område: AI, identitet och runtime. Där blir frågan inte främst vem som äger verksamhetsdata, utan hur man begränsar osäkerhet, privilegier och exekveringsrisk i återkommande lösningsstrukturer.
