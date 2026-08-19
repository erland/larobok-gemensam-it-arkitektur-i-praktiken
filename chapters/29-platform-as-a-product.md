# 29. Platform as a Product

När ett tekniskt byggblock har fått ett tydligt tjänstekontrakt, definierat ansvar, en konsumtionsmodell och en livscykel har det blivit möjligt att tala om en plattformstjänst. Men det betyder fortfarande inte att tjänsten automatiskt blir användbar, attraktiv eller värdeskapande för sina konsumenter.

En plattform kan vara tekniskt stabil och välförvaltad men ändå misslyckas därför att den löser fel problem, kräver för mycket specialkunskap, har långsam onboarding, erbjuder fel abstraheringsnivå eller utvecklas utifrån plattformsteamets interna teknikintressen snarare än konsumenternas vardag.

Platform as a Product[K1] är ett sätt att angripa detta problem. Grundidén är att en intern plattform bör utvecklas med samma typ av produktorientering som andra produkter: tydliga målgrupper, förstådda behov, prioriterade problem, mätbara utfall, kontinuerlig återkoppling och en färdplan som styrs av värde snarare än enbart teknisk önskelista.

Det betyder inte att en intern plattform är en kommersiell produkt eller att varje teknisk komponent behöver en produktchef. Det betyder att den som ansvarar för en viktig gemensam plattform måste behandla konsumenternas förmåga att lyckas som ett centralt resultat av plattformsarbetet.

## Från teknisk förvaltning till produktansvar

Traditionell teknisk förvaltning fokuserar ofta på frågor som:

- Är plattformen tillgänglig?
- Är den patchad?
- Är kapaciteten tillräcklig?
- Har vi en supportmodell?
- Är underliggande produkter inom support?

Alla dessa frågor är viktiga. Men de säger inte om plattformen är bra att konsumera.

En produktorienterad plattform behöver också kunna svara på frågor som:

- Vilka interna kunder använder plattformen?
- Vilka problem försöker de lösa?
- Vilka delar av deras arbete skapar mest friktion?
- Hur lång tid tar det från behov till första fungerande användning?
- Vilka plattformsfunktioner används faktiskt?
- Vilka funktioner kringgås eller ersätts lokalt?
- Varför väljer team andra lösningar?
- Vilka kvaliteter är viktigast för konsumenterna?
- Vilka förändringar ger störst effekt på utvecklingsflöde, risk eller driftsäkerhet?

Skillnaden kan sammanfattas så här:

```text
Teknisk förvaltning
    ↓
"Håller plattformen?"

Produktorientering
    ↓
"Hjälper plattformen konsumenterna att lyckas?"
```

De två perspektiven konkurrerar inte. En fungerande plattform behöver båda.

## Plattformens användare är interna kunder

Ordet *kund* kan kännas märkligt i en intern IT-organisation. Teamen kan kanske inte fritt välja leverantör, och plattformen finansieras inte genom en traditionell marknadstransaktion. Men kundperspektivet är ändå användbart eftersom det förskjuter uppmärksamheten från vad plattformen producerar till vilket resultat konsumenten får.

För en *Container Application Platform* kan konsumenten exempelvis vara ett utvecklingsteam som behöver:

- få en ny tjänst körbar,
- kunna göra säkra releaser,
- få loggar och mätvärden,
- hantera konfiguration och secrets,
- skala workloaden,
- förstå kostnad och resursförbrukning,
- felsöka incidenter.

Det viktiga är inte att plattformen har Kubernetes, OpenShift eller någon annan viss teknik. Det viktiga är hur väl plattformen minskar den återkommande friktionen runt dessa behov.

Samma resonemang gäller för en databastjänst. Konsumenten behöver sällan ”en PostgreSQL-instans” som slutmål. Teamet behöver snarare en säker och förvaltad plats för relationell data med förutsägbara egenskaper.

Produktperspektivet börjar därför med användningssituationen.

## Alla konsumenter är inte samma målgrupp

Ett vanligt problem är att interna plattformar försöker erbjuda samma upplevelse till alla. Men konsumenterna kan ha mycket olika förutsättningar.

Exempel på konsumentsegment kan vara:

- produktteam med hög teknisk autonomi,
- mindre utvecklingsteam med begränsad plattformskompetens,
- integrationsspecialister,
- data- och analysteam,
- leverantörsdrivna utvecklingsteam,
- team som förvaltar äldre applikationer,
- experiment- och innovationsinitiativ.

Dessa grupper kan behöva samma underliggande kapacitet men olika konsumtionsvägar, dokumentation och abstraheringsnivåer.

En plattform kan därför behöva formulera explicita målgrupper:

> Primär målgrupp: team som bygger containeriserade stateless tjänster och vill ha standardiserad driftsättning, observerbarhet och identitetsintegration.

> Sekundär målgrupp: team som kör schemalagda batch-workloads med liknande operativa behov.

Det är bättre än att formulera plattformen som ”lösningen för alla applikationer”.

## Börja med problem, inte features

Plattformsfärdplans blir lätt featurelistor:

- stöd för ny runtime,
- nytt dashboardverktyg,
- ytterligare databasmotor,
- ny portal,
- fler driftsättningsalternativ.

En produktorienterad färdplan bör i stället börja med problem och önskade utfall.

Exempel:

```text
Problem:
Det tar i median tio arbetsdagar för ett nytt team
att få en första godkänd databasinstans.

Önskat utfall:
Standardprofilen ska kunna tas i bruk samma dag
utan manuell handläggning.

Möjliga lösningar:
- självservice
- automatiserad policykontroll
- standardiserade profiler
- bättre dokumentation
```

Detta lämnar utrymme att välja den mest effektiva lösningen. Om man börjar med ”bygg en portal” har man redan låst lösningen innan problemet är förstått.

Principen behov före teknik gäller alltså lika mycket för plattformsteam som för lösningsarkitektur.

## utvecklarupplevelse är ett arkitekturellt resultat

För plattformar som riktar sig till utvecklingsteam är utvecklarupplevelse, ofta förkortat DX, en central del av produkten.

DX handlar inte bara om att gränssnittet är snyggt. Det handlar om hur mycket kognitiv och administrativ belastning teamet behöver bära för att åstadkomma ett resultat.

Frågor som påverkar DX är exempelvis:

- Hur lätt är det att förstå vad plattformen erbjuder?
- Hur många steg krävs för att komma igång?
- Hur många specialbegrepp måste konsumenten lära sig?
- Hur snabbt får teamet återkoppling när något blir fel?
- Är felmeddelanden begripliga?
- Är dokumentationen kopplad till verkliga arbetsflöden?
- Är standardvägen automatiserad?
- Kan teamet testa lokalt eller i en säker miljö?
- Är plattformens API:er och verktyg konsekventa?
- Behöver samma metadata anges flera gånger i olika system?

En plattform kan därför vara tekniskt kraftfull men ha låg produktkvalitet om användningen kräver omfattande koordinering och specialistkunskap.

## Kognitiv last är en kostnad

När varje team behöver förstå detaljer om nätverk, certifikat, driftsättning, observerbarhet, backup, identiteter och underliggande klusterarkitektur används utvecklingskapacitet på frågor som kanske inte är verksamhetsdifferentierande.

En bra plattform tar inte bort allt ansvar. Den reducerar onödig kognitiv last genom att skapa rimliga standarder och abstrahera sådant som bäst hanteras gemensamt.

Det kan uttryckas som:

```text
Total teknisk komplexitet
        ↓
Plattformen äger återkommande komplexitet
        ↓
Teamet ser relevant komplexitet
        ↓
Mer fokus på domän och verksamhetsvärde
```

Men abstractionen får inte bli ogenomskinlig. Ett team måste fortfarande kunna förstå exempelvis vilka tillgänglighetsgarantier som finns, var data lagras och vilka begränsningar en tjänst har.

Produktkvaliteten ligger alltså i balansen mellan enkel konsumtion och tillräcklig transparens.

## Adoption är ett utfall, inte ett självändamål

En intern plattform vill ofta mäta adoption. Det är rimligt, men antal användare eller workloads säger inte hela sanningen.

Hög adoption kan bero på att plattformen är bra. Men den kan också bero på att användningen är obligatorisk.

Låg adoption kan betyda att plattformen är dålig. Men den kan också betyda att målgruppen är liten eller att tjänsten löser ett smalt problem.

Adoption behöver därför tolkas tillsammans med andra signaler.

Exempel på användbara mätetal är:

- andel relevanta team som använder erbjudandet,
- tid till första fungerande konsumtion,
- tid till vanlig förändring,
- antal manuella handoffs,
- supportärenden per konsument,
- återkommande avsteg eller lokala ersättningslösningar,
- användning av rekommenderad standardväg,
- konsumenternas upplevda friktion,
- stabilitet och SLO-uppfyllelse,
- ledtid för att införa plattformsförbättringar.

Mätetalen bör hjälpa teamet förstå både produktnytta och teknisk kvalitet.

## Plattformens SLO är nödvändigt men inte tillräckligt

En plattform kan uppfylla sitt SLO och ändå ge en dålig användarupplevelse.

Anta att en CI/CD-plattform har 99,9 procents tillgänglighet. Det säger lite om:

- hur lång en vanlig pipeline tar,
- hur snabbt köade jobb startar,
- om fel går att felsöka,
- om nya projekt kan onboardas automatiskt,
- om standardtemplates är begripliga,
- hur lätt det är att uppgradera pipelinekomponenter.

Därför bör produktmätningen kombinera två perspektiv:

```text
Tjänstens tekniska hälsa
          +
Konsumentens förmåga att få arbete gjort
          ↓
Plattformens faktiska produktvärde
```

Tekniska SLO:er är fortfarande centrala. Men de bör kompletteras med mätetal för de viktigaste användarresorna.

## Mät användarresor

Ett kraftfullt sätt att tänka är att beskriva de återkommande användarresor som plattformen ska stödja.

För en databastjänst kan det vara:

1. hitta rätt tjänst,
2. välja kvalitetsprofil,
3. skapa instans,
4. ansluta applikation,
5. få observerbarhet,
6. skala kapacitet,
7. återställa data,
8. uppgradera,
9. avveckla.

För varje steg kan teamet fråga:

- hur lång tid tar detta?
- hur många manuella handoffs krävs?
- hur ofta misslyckas flödet?
- vilka supportärenden uppstår?
- vilken specialistkunskap krävs?

Då blir förbättringsarbetet konkret.

## Feedback måste vara en del av produktloopen

En intern plattform riskerar att utvecklas långt från sina konsumenter eftersom teamet ofta är upptaget med drift, patchning och teknisk evolution.

Produktmodellen kräver därför en aktiv feedbackloop.

Feedback kan komma från:

- intervjuer med konsumentteam,
- supportärenden,
- incidenter,
- onboardingobservationer,
- plattformstelemetri,
- avsteg och undantagsansökningar,
- interna communities of practice,
- användningsdata,
- retrospektiv efter större migrationer.

Det viktiga är inte bara att samla feedback utan att kunna koppla den till prioritering.

Ett återkommande avsteg kan exempelvis vara ett tecken på att konsumenterna inte följer standarden. Men det kan också vara bevis för att plattformen saknar en relevant förmåga.

```text
Konsumentbeteende
       ↓
Feedback och telemetri
       ↓
Produktinsikt
       ↓
Prioritering
       ↓
Förbättrat erbjudande
       ↺
```

## Färdplanen behöver balansera flera typer av arbete

Ett plattformsteam kan inte bara utveckla nya funktioner. Det behöver samtidigt bära teknisk och operativ hållbarhet.

En realistisk färdplan behöver därför balansera åtminstone:

- konsumentdrivna förbättringar,
- säkerhets- och compliancekrav,
- kapacitet och tillgänglighet,
- produkt- och versionsuppgraderingar,
- teknisk skuld,
- avveckling av gammal funktionalitet,
- förbättrad självservice,
- support- och drifterfarenheter.

Om färdplanen bara innehåller nya features kan plattformen bli svår att förvalta. Om den bara innehåller uppgraderingar och patchning utvecklas den till en intern infrastrukturfunktion utan tydlig produktutveckling.

## Plattformsteamet behöver produktkompetens

Ett produktorienterat plattformsteam behöver vanligtvis fler perspektiv än ren teknikförvaltning.

Det behöver förmåga att:

- förstå användarbehov,
- prioritera mellan olika konsumentgrupper,
- formulera produktmål,
- mäta användning och utfall,
- designa konsumtionsupplevelser,
- förvalta tekniken,
- driva säkerhet och tillgänglighet,
- kommunicera förändringar och färdplan.

Det innebär inte att varje plattform behöver samma organisatoriska roller. Produktansvar kan ligga hos en produktägare, produktchef, teknisk produktledare eller annan tydligt utsedd funktion. Det viktiga är att ansvaret finns och inte reduceras till backlogadministration.

## Produktansvar och förmågeansvar är inte samma sak

I bokens ansvarmodell behöver man skilja mellan förmågeområde och enskild plattformsprodukt.

Förmågan *Data- och informationshantering* kan exempelvis omfatta flera erbjudanden:

- *relationell databastjänst*,
- objektlagring,
- cache,
- kanske andra framtida datatjänster.

Förmågeansvaret handlar då om den övergripande riktningen:

- vilka återkommande behov som ska stödjas,
- gemensamma principer,
- relevanta mönster,
- relationer mellan tjänster,
- kvalitetskrav och standarder.

Produktansvaret för databastjänsten handlar mer konkret om:

- målgrupp,
- tjänstekontrakt,
- färdplan,
- adoption,
- supportupplevelse,
- teknisk realisering,
- livscykel och förbättring.

Det ger en viktig separation:

```text
Förmågeområde
    ↓
Vad behöver organisationen kunna erbjuda?
    ↓
Plattformsprodukt
    ↓
Hur gör vi detta erbjudande användbart och hållbart?
```

## En plattform är inte lyckad bara för att den är obligatorisk

I stora organisationer finns en särskild risk: plattformen kan få hög användning genom styrning snarare än genom kvalitet.

Om ett team måste använda en viss tjänst men samtidigt behöver:

- bygga egna kringlösningar,
- öppna många manuella ärenden,
- vänta länge på förändringar,
- skapa lokala verktyg för att kompensera,
- använda odokumenterade genvägar,

är hög adoption inte ett bevis på en bra produkt.

Detta är ett skäl att mäta friktion och workaround-beteenden, inte bara antal konsumenter.

En gemensam standard kan vara obligatorisk av goda skäl. Men plattformsteamet bör ändå försöka göra den rekommenderade vägen till den enklaste rimliga vägen.

## Plattformen ska ha ett tydligt värdelöfte

Ett plattformserbjudande bör kunna beskrivas med ett enkelt värdelöfte.

Exempel:

> Container Application Platform gör det möjligt för produktteam att driftsätta och operera standardiserade containeriserade tjänster utan att själva bygga klusterdrift, grundläggande observerbarhet, identitetsintegration och grundläggande driftsättningsmekanismer.

Värdelöftet hjälper till att avgränsa produkten.

Om plattformen försöker lösa allt för alla blir både teknik och konsumtionsmodell snabbt komplexa.

## Kostnad är en del av produktbeslutet

Interna plattformar verkar inte på en fri marknad, men de har fortfarande en kostnad.

Produktteamet behöver därför förstå åtminstone:

- fasta plattformskostnader,
- kostnad per ytterligare konsument eller workload,
- kostnadsdrivare,
- dyr specialfunktionalitet,
- kostnad för parallella realiseringar,
- kostnad för support och manuell hantering,
- kostnad för att behålla gammal funktionalitet.

Poängen är inte att all intern konsumtion måste faktureras. Men kostnadstransparens hjälper både plattformsteam och konsumenter att göra rationella val.

En kvalitetsprofil med extremt hög tillgänglighet och mycket låg RPO kan exempelvis vara tekniskt möjlig men avsevärt dyrare. Produktmodellen behöver göra sådana samband begripliga.

## När en plattform bör säga nej

Produktorientering betyder inte att plattformsteamet ska implementera varje önskemål.

En bra produkt behöver en tydlig riktning och kan därför behöva säga nej till:

- mycket smala behov som bara ett team har,
- funktioner som bryter plattformens säkerhetsmodell,
- variationer som skapar oproportionerlig operativ komplexitet,
- requests som egentligen hör hemma i domänlösningen,
- äldre funktionalitet som bör avvecklas.

Ett nej bör däremot kunna förklaras utifrån produktens mål, målgrupp, kvaliteter och kostnader – inte bara genom att ”plattformen inte stödjer det”.

## Escape hatches är en produktfråga

Ingen gemensam plattform kommer att täcka alla legitima behov. Därför behöver organisationen ha ett förhållningssätt till avvikelser.

I produktperspektivet är en *escape hatch* inte bara ett governanceundantag. Det är också en signal om produktens gräns.

Om ett fåtal specialiserade workloads behöver en annan runtime kan det vara rimligt att hantera dem utanför standardplattformen. Om däremot många team använder samma escape hatch kan det betyda att produktstrategin behöver ändras.

Kapitel 30 återkommer till hur sådana vägar kan kombineras med golden paths och guardrails.

## Plattformens livscykel är en produktlivscykel

En plattformstjänst behöver kunna introduceras, växa, förändras och avvecklas på ett sätt som konsumenterna kan planera kring.

Det omfattar exempelvis:

- preview eller pilot,
- generell tillgänglighet,
- stöd för nya profiler,
- deprecation,
- migrationsstöd,
- retirement.

En produktorienterad plattform lämnar inte konsumenterna ensamma vid stora förändringar. Migration blir en del av produktarbetet.

Det kan innebära:

- automatiserade konverteringsverktyg,
- kompatibilitetslager,
- dokumenterade migrationsvägar,
- mätning av återstående konsumenter,
- aktiv hjälp till särskilt svåra migreringar.

## Tre ansvarsnivåer

Platform as a Product passar in i bokens tredelade ansvarmodell.

### Gemensam nivå

Den gemensamma arkitekturen bör sätta spelregler för exempelvis:

- vad ett plattformserbjudande behöver beskriva,
- övergripande kvalitetsdimensioner,
- principer för interoperabilitet och säkerhet,
- hur gemensamma tjänster relaterar till förmågekartan,
- gemensamma livscykelprinciper.

Den bör däremot inte detaljprioritera varje plattforms backlog.

### Förmåge- och plattformsnivå

Här ligger produktansvaret:

- målgrupp,
- värdelöfte,
- tjänstekontrakt,
- färdplan,
- användarresor,
- kvalitetsprofiler,
- adoption,
- feedback,
- teknisk realisering,
- livscykel.

### Lösnings-/produktnivå

Konsumentteamet ansvarar för att:

- välja erbjudandet när det passar behovet,
- förstå kontrakt och begränsningar,
- använda standardvägen där den är lämplig,
- ge återkoppling,
- bära sitt kvarvarande lösnings- och domänansvar.

Den här separationen gör att plattformen kan vara produktorienterad utan att bli central lösningsarkitekt för alla team.

## Vanliga anti-patterns

### Tekniken är produkten

Färdplanen drivs av produktuppgraderingar och features i underliggande teknik snarare än konsumentproblem.

### Captive customers tolkas som nöjda kunder

Hög användning antas betyda att plattformen är framgångsrik trots omfattande friktion och workarounds.

### Backlogen är strategin

Hundratals enskilda önskemål prioriteras utan tydliga produktmål eller målgrupper.

### Plattformsteamet bygger för sig självt

Interna teknikbehov får högre prioritet än de användarresor plattformen faktiskt finns för att stödja.

### Feature accumulation

Varje nytt behov leder till en ny variant tills plattformen blir svår att förstå och dyr att operera.

### DX reduceras till en portal

En portal byggs, men de underliggande arbetsflödena är fortfarande manuella, inkonsekventa eller långsamma.

### Mätning utan produktinsikt

Hundratals tekniska mätvärden samlas in men teamet vet fortfarande inte hur lång tid onboarding tar eller varför konsumenterna bygger egna lösningar.

## En praktisk analysordning

När en organisation vill arbeta med Platform as a Product kan följande ordning användas:

1. Identifiera plattformens primära konsumenter.
2. Beskriv deras viktigaste användningssituationer och problem.
3. Formulera ett tydligt värdelöfte.
4. Kartlägg de viktigaste användarresorna.
5. Identifiera var friktion och manuella handoffs finns.
6. Mät både teknisk hälsa och konsumentutfall.
7. Prioritera problem före features.
8. Balansera ny funktionalitet mot säkerhet, livscykel och teknisk hållbarhet.
9. Skapa kontinuerliga feedbackloopar.
10. Tolka avsteg, workarounds och låg adoption som data.
11. Gör färdplan och avvecklingsplan synliga för konsumenterna.
12. Ompröva målgrupp och produktgräns när behoven förändras.

Det är inte en universell produktmetod. Det är ett praktiskt arbetssätt för att flytta en intern plattform från teknik som tillhandahålls till en tjänst som aktivt utvecklas för att hjälpa andra team att lyckas.

## Från produktstrategi till standardväg

Platform as a Product ger ett svar på hur plattformsteamet bör tänka kring konsumenter, behov, värde och utveckling. Men produktstrategin behöver också omsättas i den dagliga användningen.

Om plattformens bästa arbetssätt bara finns i dokumentation är friktionen fortfarande hög. Nästa steg är därför att göra den rekommenderade vägen konkret genom automation, templates, portals, policy-as-code och andra former av självservice.

Det är ämnet för nästa kapitel: golden paths, paved roads och självservice.

## Källor och vidare läsning

**[K1]** CNCF TAG App Delivery, *CNCF Platforms White Paper* och *Platform Engineering Maturity Model*, om plattformens användarbehov, roadmap, feedback och självservice. https://tag-app-delivery.cncf.io/whitepapers/platforms/ och https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/
