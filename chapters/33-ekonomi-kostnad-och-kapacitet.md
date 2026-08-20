# 33. Ekonomi, kostnad och kapacitet

Arkitekturval kostar pengar. Det är självklart, men ekonomin behandlas ändå ofta som något som kommer efter arkitekturen: först utformas lösningen, sedan försöker någon förstå vad den kostar och därefter startar ett separat optimeringsarbete.

Det är ett svagt arbetssätt. Kostnad är inte bara en följd av arkitektur. Kostnadsstruktur är en del av arkitekturen. Val av redundans, datalagring, integrationsform, kapacitetsmarginal, licensmodell, plattform, återställningsnivå och graden av standardisering formar både den direkta kostnaden och organisationens långsiktiga förändringskostnad.

Samtidigt blir ekonomisk styrning farlig om den reduceras till att minimera utgifter. Den billigaste lösningen per månad kan ge högre risk, sämre användbarhet, längre ledtid eller större framtida migreringskostnad. Ett arkitekturbeslut behöver därför väga kostnad tillsammans med övriga kvalitetsattribut.

Detta kapitel handlar om hur ekonomi och kapacitet kan bli arkitekturella styrsignaler utan att de tar över besluten. FinOps används som ett relevant inspirationsområde, men kapitlets modell är bredare än publik molnekonomi. Samma grundfrågor finns för datacenter, SaaS, licenser, AI-tjänster och interna plattformar.

## Kostnad är ett kvalitetsattribut – men inte ett ensamt mål

Kostnadseffektivitet är en av bokens tvärgående kvalitetsdimensioner. Det är en viktig placering. Kostnad konkurrerar ibland med andra kvaliteter och samverkar ibland med dem.

Högre tillgänglighet kan kräva:

- fler instanser,
- redundanta zoner eller datacenter,
- mer avancerad datalagring,
- reserverad kapacitet,
- större operativ beredskap.

Men samma investering kan samtidigt minska kostnaden för avbrott. På motsvarande sätt kan en dyr gemensam plattform bli ekonomiskt rimlig om den reducerar duplicerat arbete, förkortar ledtider och gör specialistkompetens återanvändbar.

Kostnadsfrågan bör därför formuleras som:

> Vilken kostnadsprofil är rimlig för den nytta, risk och kvalitet som lösningen behöver bära?

inte:

> Hur får vi lägsta möjliga månadskostnad?

Det första är en arkitekturfråga. Det andra riskerar att bli lokal optimering.

## Från kostnadsdrivare till ekonomisk återkoppling

En totalsumma säger väldigt lite om varför en tjänst kostar det den gör.

Anta att en plattform kostar tio miljoner kronor per år. Det säger inte om kostnaden drivs av:

- många användare,
- hög transaktionsvolym,
- stora datamängder,
- höga krav på tillgänglighet,
- lång retention,
- dyr licensiering,
- låg resursutnyttjandegrad,
- omfattande manuell drift,
- stor överkapacitet,
- specialistbemanning,
- leverantörsbundna avgifter.

För arkitekturarbete är kostnadsdrivaren ofta viktigare än totalsumman.

En användbar kostnadsmodell bör därför försöka besvara två frågor:

1. Vilka egenskaper hos konsumtionen skapar kostnad?
2. Vilka av dessa egenskaper kan arkitekturen faktiskt påverka?

Det går att beskriva sambandet så här:

```text
Verksamhetsbehov
      ↓
Kvalitetsprofil och användningsmönster
      ↓
Tekniska designval
      ↓
Resurs- och tjänstekonsumtion
      ↓
Kostnadsdrivare
      ↓
Total kostnad och enhetskostnad
```

Om sambandet saknas blir ekonomirapporteringen svår att använda som arkitekturell återkoppling.

**Enhetskostnad ger bättre signal än total kostnad.**

Total kostnad växer ofta när verksamheten växer. Det behöver inte innebära att arkitekturen blivit mindre effektiv.

Anta att kostnaden för en digital tjänst ökar från 1 miljon till 1,5 miljoner kronor samtidigt som antalet genomförda ärenden fördubblas. Den totala kostnaden har ökat med 50 procent, men kostnaden per ärende har minskat.

Därför behövs enhetskostnader.

Exempel kan vara:

- kostnad per behandlat ärende,
- kostnad per aktiv användare,
- kostnad per API-anrop,
- kostnad per meddelande,
- kostnad per lagrad terabyte och månad,
- kostnad per byggpipeline,
- kostnad per modellinferens,
- kostnad per plattformskonsument,
- kostnad per återställd tjänstprofil.

En bra enhet ska helst ha koppling till faktisk konsumtion eller verksamhetsvärde. Enheten behöver också vara tillräckligt stabil för att kunna följas över tid.

Enhetskostnad kan uttryckas enkelt:

```text
Enhetskostnad = relevant total kostnad / relevant konsumtionsenhet
```

Det svåra är inte divisionen. Det svåra är att avgöra:

- vilken kostnad som ska ingå,
- vilken konsumtionsenhet som är meningsfull,
- hur gemensamma kostnader ska fördelas,
- hur kvalitetsskillnader ska vägas in.

Två lösningar kan ha samma kostnad per transaktion men helt olika tillgänglighet, säkerhetsnivå eller lagringstid. Enhetskostnaden är därför ett beslutsunderlag, inte ett facit.

**Kostnadsallokering skapar synlighet.**

För att kunna förstå kostnadsdrivare behöver kostnader kunna kopplas till något ansvarsbärande objekt.

Det kan exempelvis vara:

- produkt,
- tjänst,
- system,
- team,
- verksamhetsområde,
- plattformskonsument,
- miljö,
- kostnadsställe.

I molnmiljöer används ofta metadata, kontostrukturer eller resursrelationer för sådan allokering. I andra miljöer kan licensregister, CMDB, tjänstekataloger och ekonomisystem behöva kombineras.

En central princip är att kostnadsallokering inte bara är en ekonomifråga. Om arkitekturen inte skapar tydliga ansvarsgränser blir kostnaden också svår att fördela.

Det finns därmed en relation:

```text
Tydligt ägarskap
      ↓
Tydlig konsumtion
      ↓
Tydligare kostnadsallokering
      ↓
Bättre återkoppling till beslut
```

Otydliga delade resurser, gemensamma databaser och tekniska plattformar utan konsumtionsmodell gör ekonomisk transparens svårare.

**Showback före chargeback.**

Två återkommande begrepp är showback och chargeback.

I bokens användning betyder showback att konsumtion och kostnader synliggörs för den ansvariga parten utan att kostnaden nödvändigtvis bokförs vidare internt. Chargeback innebär att kostnaden också fördelas ekonomiskt till konsumenten enligt en intern modell.

Skillnaden är viktig.

Showback kan ge:

- medvetenhet,
- jämförbarhet,
- möjlighet att upptäcka avvikelser,
- underlag för planering,
- diskussion om effektivitet.

Chargeback skapar dessutom ett ekonomiskt incitament, men också mer komplexitet. En dåligt utformad internprismodell kan exempelvis få team att:

- undvika gemensamma tjänster trots att de är bättre för helheten,
- optimera för den debiterade mätaren snarare än verklig nytta,
- flytta kostnader mellan kategorier,
- minska redundans eller säkerhetsnivå för att nå lokala budgetmål.

Därför bör chargeback införas först när kostnadsmodellen är tillräckligt begriplig och incitamenten har analyserats.

Ekonomisk transparens kräver inte automatiskt intern fakturering.

## Gemensamma plattformar har både fasta och rörliga kostnader

Ett plattformserbjudande har sällan en rent konsumtionsbaserad kostnadsbild. Det finns ofta en grundkostnad för:

- plattformsteam,
- support,
- säkerhetsarbete,
- automation,
- grundinfrastruktur,
- licenser,
- observerbarhet,
- backup,
- dokumentation,
- kompetensutveckling.

Därtill kan rörliga kostnader uppstå genom exempelvis:

- CPU och minne,
- lagring,
- nätverk,
- antal användare,
- transaktioner,
- API-anrop,
- AI-tokens,
- externa tjänsteanrop.

Det gör principen ”varje team betalar exakt vad det förbrukar” svår att tillämpa. En plattform kan i stället finansieras genom en kombination av:

```text
Gemensam grundinvestering
        +
Synliggjord rörlig konsumtion
        +
Eventuell intern fördelningsmodell
```

Den exakta modellen är en organisationsfråga. Arkitekturen behöver däremot göra konsumtionen mätbar och kostnadsdrivarna begripliga.

## Gemensam investering kan vara rationell även utan direkt återbetalning

Vissa investeringar ger värde genom att minska kostnader som aldrig syns som fakturor.

Exempel:

- gemensam CI/CD minskar tiden varje team lägger på pipelinebygge,
- central identitetsfederation minskar lokala integrationer,
- en standardiserad *containerplattform* minskar variation i drift,
- gemensam observerbarhet minskar felsökningstid,
- golden paths minskar ledtid och felkonfigurationer.

Om man enbart mäter den direkta plattformskostnaden kan dessa tjänster framstå som dyra. En bättre ekonomisk bedömning inkluderar undviket duplicerat arbete och reducerad koordinationskostnad.

Det innebär inte att alla gemensamma investeringar är lönsamma. En plattform som få använder kan tvärtom bli en dyr central speciallösning. Poängen är att kostnadsanalysen måste jämföra med ett realistiskt alternativ.

Frågan är inte:

> Vad kostar plattformsteamet?

utan snarare:

> Vad kostar organisationen med respektive utan den gemensamma förmågan, givet samma kvalitetsbehov?

## Kapacitet, marginal, elasticitet och prognos

Kapacitet handlar om hur mycket belastning en lösning eller plattform kan bära under givna kvalitetskrav.

Exempel på kapacitetsdimensioner är:

- samtidiga användare,
- transaktioner per sekund,
- meddelanden per sekund,
- datavolym,
- lagringstillväxt,
- batchfönster,
- CPU/GPU-tid,
- modellinferenser,
- samtidiga pipelines.

Kapacitet kan inte planeras isolerat från prestanda och tillgänglighet. En tjänst som tekniskt klarar 10 000 anrop per sekund men får oacceptabel svarstid vid 6 000 har en annan praktisk kapacitet än den nominella maxnivån.

Det är därför användbart att formulera kapacitet som:

> den belastning som kan hanteras inom överenskommen kvalitetsprofil.

Detta knyter kapacitetsplanering till kvalitetskraven och drifttelemetrin.

**Överkapacitet kan vara både slöseri och försäkring.**

En vanlig optimeringsidé är att eliminera överkapacitet. Men all överkapacitet är inte dålig.

Marginal kan behövas för:

- belastningstoppar,
- nodfel,
- underhåll,
- disaster recovery,
- plötsliga verksamhetshändelser,
- osäker prognos,
- skalningsfördröjning.

Det ekonomiska problemet uppstår när marginalen är omedveten eller större än den risk den ska hantera.

Man kan tänka i tre lager:

1. Normal kapacitet – förväntad löpande belastning.
2. Planerad reserv – marginal för variation och fel.
3. Exceptionell beredskap – kapacitet för särskilda scenarier.

Dessa bör inte blandas ihop.

Om all kapacitet dimensioneras efter ett extremt scenario som inträffar vart femte år kan kostnaden bli orimlig. Om ingen reserv finns alls kan ett mindre avvikande beteende skapa incident.

Arkitekturen behöver därför göra riskaptit och kapacitetsmarginal explicita.

**Elasticitet förändrar frågan – men tar inte bort den.**

Dynamisk skalning gör att kapacitet kan anpassas snabbare till faktisk belastning. Det är värdefullt, men elasticitet löser inte automatiskt ekonomin.

Automatisk skalning kan också skala upp:

- ineffektiv kod,
- okontrollerade återförsök,
- bottrafik,
- felaktiga batchjobb,
- AI-anrop med oväntat hög tokenförbrukning.

En elastisk plattform behöver därför både tekniska och ekonomiska guardrails.

Det kan exempelvis vara:

- resursgränser,
- quotas,
- budgets,
- anomalidetektion,
- rate limiting,
- skalningsgränser,
- cost alerts.

Principen är densamma som för annan självservice: den fungerar bäst när ramarna är automatiserade och begripliga.

**Prognoser behöver uttrycka osäkerhet.**

Kostnads- och kapacitetsprognoser är modeller av framtiden, inte fakta.

En prognos påverkas av exempelvis:

- verksamhetstillväxt,
- nya funktioner,
- migreringar,
- ändrade användningsmönster,
- prisförändringar,
- licensvillkor,
- prestandaförbättringar,
- nya regulatoriska krav.

Därför är scenarioanalys ofta mer användbart än ett enda exakt tal.

Exempel:

```text
Scenario A – normal tillväxt
Scenario B – fördubblad användning
Scenario C – ny hög tillgänglighetsprofil
Scenario D – större migrering eller datatillväxt
```

För varje scenario kan organisationen uppskatta:

- resursbehov,
- kostnad,
- flaskhalsar,
- ledtid för utökning,
- vilka arkitekturbeslut som måste omprövas.

Det gör prognosen till ett arkitekturstöd i stället för en ren budgetövning.

## Kostnadsprofiler kan vara en del av plattformserbjudandet

Kvalitetsprofiler och tjänstekontrakt ger också en modell som ekonomin kan knytas till.

En databastjänst skulle exempelvis kunna erbjuda:

- standardprofil,
- hög tillgänglighetsprofil,
- hög prestandaprofil,
- arkivprofil.

Varje profil kan ha olika:

- resursmodell,
- replikeringsnivå,
- backupfrekvens,
- retention,
- återställningsmål,
- ungefärlig kostnadsprofil.

Detta gör avvägningen synlig för konsumenten.

I stället för att säga:

> Hög tillgänglighet är dyrt.

kan tjänsten förklara:

> Den här profilen ger högre redundans och kortare återställningsmål, vilket innebär ungefär denna typ av kostnadsökning.

Det blir bättre beslutsstöd.

## FinOps som tvärfunktionell disciplin

FinOps har vuxit fram som ett sätt att föra samman teknik, ekonomi och verksamhet kring variabel teknikförbrukning. Den aktuella FinOps Framework[K1] beskriver bland annat arbete med kostnads- och användningsförståelse, värde, optimering, forecast, unit economics och arkitektur-/workload placement.

För den här boken är den viktigaste lärdomen inte ett specifikt FinOps-processflöde. Det är principen att ekonomiska data måste komma till de personer som kan påverka de tekniska besluten.

Det kräver samarbete mellan exempelvis:

- ekonomi,
- plattformsteam,
- produktteam,
- arkitekter,
- inköp/licensansvariga,
- verksamhetsansvariga.

Ekonomistyrning som enbart sker centralt efter att konsumtionen redan uppstått kommer för sent.

## Kostnadsdata behöver standardiserbar semantik

När organisationen använder flera leverantörer, SaaS-tjänster eller interna plattformar uppstår samma problem som för annan information: olika begrepp och format gör jämförelser svåra.

Det kan vara värdefullt att standardisera exempelvis:

- kostnadsobjekt,
- ägare,
- produkt-/*tjänsteidentitet*,
- konsumtionsenheter,
- miljö,
- kostnadstyp,
- tidsperiod,
- allokeringsprincip.

Inom FinOps finns exempelvis FOCUS[K2], en öppen specifikation som standardiserar faktureringsdata och relaterade kostnads- och användningsbegrepp över olika datakällor. Poängen här är inte att varje organisation måste använda just den specifikationen, utan att ekonomiska data behöver ett eget informationskontrakt om de ska kunna användas tvärs över tekniska miljöer.

## Kostnadsoptimering har flera nivåer

Det är användbart att skilja mellan fyra typer av optimering.

### Resursoptimering

Exempel:

- minska överdimensionerade instanser,
- stäng oanvända resurser,
- rätta ineffektiva lagringsnivåer.

### Avtals- och prisoptimering

Exempel:

- reservationsmodeller,
- volymavtal,
- licensnivåer,
- leverantörsrabatter.

### Arkitekturoptimering

Exempel:

- minska onödig dataöverföring,
- förändra retention,
- använda cache där det är motiverat,
- ändra synkronitet,
- välja annan lagrings- eller exekveringsprofil.

### Produkt- och verksamhetsoptimering

Exempel:

- ta bort funktioner som kostar mycket men används lite,
- ändra en användarresa,
- minska dyr AI-användning där enklare mekanismer räcker,
- styra efter faktisk affärs- eller verksamhetsnytta.

De två sista nivåerna kräver arkitektur- och produktbeslut; ett centralt kostnadsverktyg räcker därför inte för verklig kostnadseffektivitet.

## Billig teknik kan skapa dyr organisation

En kostnadsmodell bör också fånga sådant som inte syns på leverantörsfakturan.

Exempel:

- tid för manuell provisionering,
- specialistberoende,
- incidentarbete,
- duplicerad automation,
- lång onboarding,
- svår migrering,
- teknisk variation,
- många unika supportmodeller.

Detta kan beskrivas som organisatorisk och operativ kostnad.

En teknisk komponent med låg licenskostnad kan bli dyr om varje team måste bygga egen automation, egen observerbarhet och egen supportkompetens. En dyrare plattformstjänst kan därför ge lägre total kostnad om den reducerar friktionen tillräckligt mycket.

Total Cost of Ownership, TCO, är ett användbart tankesätt här, men även TCO behöver avgränsas. Om analysen försöker räkna in varje tänkbar indirekt effekt blir modellen snabbt svår att använda. Det viktiga är att de största relevanta kostnadsdrivarna finns med.

## Incitament formar arkitekturbeteende

Ekonomiska modeller påverkar hur team agerar.

Om en plattform är gratis för konsumenten kan konsumtionen sakna återhållsamhet. Om varje resurs debiteras hårt kan team i stället undvika gemensamma tjänster eller sänka kvalitet för att skydda sin lokala budget.

Därför bör en finansieringsmodell testas mot frågan:

> Vilket beteende belönar den här modellen?

Ett exempel är gemensam säkerhetsinfrastruktur. Om varje team måste bära hela den marginala kostnaden för att använda den gemensamma säkra vägen, medan en lokal genväg uppfattas som gratis, har organisationen skapat fel incitament.

Vissa kostnader bör därför medvetet bäras gemensamt eftersom organisationen vill att ett visst beteende ska vara standardvägen.

Det knyter tillbaka till paved roads: den rekommenderade vägen bör inte bara vara tekniskt enklare – den behöver också vara ekonomiskt rimlig att välja.

## Kostnad och kapacitet som delat ansvar

Bokens ansvarmodell gäller även här. På gemensam nivå behövs jämförbara kostnadsbegrepp, principer för allokering och showback/chargeback samt minimikrav på vilka kostnads- och kapacitetsdata som ska kunna följas.

Förmåge- och plattformsnivån behöver göra kostnadsdrivare, konsumtionsenheter, tjänste- och kvalitetsprofiler samt kapacitetsgränser begripliga. Plattformsteamet behöver kunna förklara både vad tjänsten kostar och vilket arbete eller vilken risk den hjälper organisationen att undvika.

På lösnings- och produktnivå ligger ansvaret för den faktiska konsumtionen: välja rimlig kvalitetsprofil, dimensionera workloaden, följa kostnadsavvikelser och ompröva design när kostnadsprofilen förändras väsentligt.

Ingen nivå kan ensam skapa kostnadseffektivitet. Gemensamma spelregler, begripliga plattformserbjudanden och lokala designval behöver ge återkoppling till varandra.

## Vanliga anti-patterns

- **Cost cutting efter design:** ekonomin analyseras först när kostnaden blivit ett problem, vilket gör grundläggande designval dyra att ändra.
- **Allt mäts i total spend:** tillväxt och ineffektivitet blandas ihop.
- **Chargeback utan begriplig kostnadsmodell:** team optimerar mot en internprislista snarare än faktisk nytta.
- **Gemensamt betyder gratis:** centralt finansierad konsumtion blir osynlig och överkonsumtion svår att upptäcka.
- **Billigast vinner:** direkt kostnad tränger undan risk, kvalitet och förändringskostnad.
- **Kapacitet utan verksamhetsscenario:** tekniska maxvärden styr dimensioneringen i stället för faktisk efterfrågan och kvalitetsmål.

## En praktisk analysordning

När kostnad och kapacitet ska vägas in i ett arkitekturbeslut kan följande ordning användas:

1. Identifiera verksamhetsnytta, kvalitetsprofil och förväntad efterfrågan.
2. Identifiera de viktigaste kostnadsdrivarna och relevanta konsumtionsenheterna.
3. Säkerställ att kostnaden går att koppla till tydliga ägare och konsumtionsgränser.
4. Bedöm kapacitetsmarginal och jämför realistiska alternativ, inklusive större indirekta kostnader.
5. Granska vilket beteende finansierings- och debiteringsmodellen belönar.
6. Gör kostnad och kapacitet synliga nära de tekniska besluten.
7. Ompröva när efterfrågan, enhetskostnaden eller kvalitetsprofilen förändras väsentligt.

Detta är inte en separat ekonomiprocess vid sidan av arkitekturen. Det är ett sätt att göra arkitekturbeslut mer fullständiga.

## Ekonomisk transparens är en arkitekturell förmåga

En mogen gemensam IT-arkitektur gör inte bara teknik återanvändbar. Den gör också konsekvenserna av teknikval begripliga.

Det innebär att en plattformskonsument kan förstå:

- vilken kvalitet en tjänsteprofil ger,
- vilka resurser den använder,
- vilka kostnadsdrivare som påverkas,
- vilken kapacitetsmarginal som ingår,
- hur konsumtionen förändras över tid.

Plattforms- och arkitekturansvariga kan samtidigt se när ett mönster, en standard eller en tjänst skapar orimlig kostnad i större skala. Kostnadsdata blir då feedback till arkitekturen, inte ett kontrollsystem vid sidan av den.

Kapitlets viktigaste princip är därför:

> Kostnad ska vara synlig där tekniska beslut fattas, men alltid tolkas tillsammans med värde, risk och övriga kvalitetskrav.

Med detta är bokens del om plattformar, standarder och teknikstyrning komplett. Nästa del flyttar perspektivet från enskilda artefakter till hur de kombineras i referensarkitekturer och konkreta lösningsarkitekturer.

## Källor och vidare läsning

**[K1]** FinOps Foundation, *FinOps Framework*. https://www.finops.org/framework/

**[K2]** FinOps Foundation, *FOCUS Specification 1.4*, ratificerad 4 juni 2026. https://focus.finops.org/focus-specification/
