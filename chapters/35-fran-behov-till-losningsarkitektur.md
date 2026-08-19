# 35. Från behov till lösningsarkitektur

När en organisation har etablerat gemensamma förmågor, lösningsmönster, plattformstjänster, standarder och referensarkitekturer återstår den fråga som avgör om modellen faktiskt fungerar i vardagen:

> Hur använder ett konkret initiativ allt detta utan att arkitekturarbetet blir en mekanisk checklista eller ett parallellt dokumentationsspår?

Det är lätt att tänka att lösningsarkitektur börjar när någon ritar komponenter. I praktiken börjar den tidigare. Den börjar när ett verksamhetsbehov formuleras, när kvalitetskrav görs explicita, när gränser och ansvar identifieras och när organisationen avgör vilka gemensamma delar som kan återanvändas och vilka beslut som faktiskt måste tas lokalt.

Lösningsarkitekturen är därför inte ett fristående lager ovanpå den gemensamma arkitekturen. Den är den konkreta tillämpningen av den.

En förenklad kedja kan beskrivas så här:

```text
Behov och verksamhetskonsekvenser
            ↓
Kvalitetsprofil och begränsningar
            ↓
Berörda förmågor och ansvar
            ↓
Relevant referensarkitektur
            ↓
Mönster, plattformar och standarder
            ↓
Alternativ och arkitekturbeslut
            ↓
Konkret lösningsarkitektur
            ↓
Verifiering, leverans och återkoppling
```

Kedjan ska inte läsas som ett vattenfall där varje steg måste vara fullständigt innan nästa börjar. I verkligheten rör sig arkitekten fram och tillbaka mellan dem. Ett plattformsval kan synliggöra ett kvalitetsproblem. Ett domänbeslut kan förändra vilka integrationer som behövs. Ett proof of concept kan visa att ett antagande var fel.

Det centrala är inte sekventiell perfektion utan **spårbarhet mellan varför, vad och hur**.

## Börja med beslutssituationen, inte med arkitekturartefakten

Ett vanligt arkitekturproblem är att arbetet startar med frågan:

> Vilket arkitekturdokument ska vi ta fram?

Det är nästan alltid fel första fråga.

Bättre är:

> Vilka beslut behöver initiativet fatta, vilka konsekvenser har de och vilka av dem kan organisationens gemensamma arkitektur redan hjälpa oss med?

Ett mindre internt verktyg och en samhällskritisk extern tjänst behöver inte samma mängd analys eller dokumentation. De kan ändå använda samma beslutslogik.

Arkitekturarbetets omfattning bör därför vara proportionerlig mot exempelvis:

- verksamhetskonsekvens,
- informationskänslighet,
- antal konsumenter,
- beroenden till andra system,
- krav på tillgänglighet och kontinuitet,
- förändringstakt,
- juridiska och organisatoriska begränsningar,
- graden av irreversibilitet i de tekniska besluten.

Detta knyter an till principen från kapitel 5: analysens djup ska stå i proportion till beslutets räckvidd och reversibilitet.

Ett initiativ behöver alltså inte producera fler artefakter bara för att det kallas arkitektur. Det behöver skapa **tillräcklig evidens för de beslut som faktiskt spelar roll**.

## Steg 1: formulera behovet utan att gömma lösningen i frågan

Resan börjar med behovet.

Det innebär inte att tekniska idéer är förbjudna. Det innebär att de inte får ersätta problemformuleringen.

Skillnaden är betydande:

> Vi behöver Kafka.

är ett lösningsförslag.

> Flera oberoende konsumenter behöver reagera på samma verksamhetshändelser utan att producenten behöver känna till dem.

är ett behov som kan analyseras.

På samma sätt är:

> Vi behöver ett AI-stöd.

för svagt för att bära arkitekturbeslut.

Bättre är:

> Handläggare behöver snabbare kunna hitta relevant information i ett stort dokumentunderlag, men beslutet ska fortfarande fattas av en ansvarig människa och svaret måste kunna härledas till källmaterial.

Den senare formuleringen börjar samtidigt avslöja kvalitetsdrivare:

- sökkvalitet,
- spårbarhet,
- behörighetskontroll,
- mänsklig kontroll,
- svarstid,
- informationssäkerhet.

Det gör behovet användbart som arkitektoniskt ingångsvärde.

## Steg 2: gör kvalitetsprofilen konkret

När behovet är förstått behöver initiativet fråga vilka kvaliteter som faktiskt styr lösningen.

Det räcker sällan att skriva:

- hög tillgänglighet,
- god prestanda,
- säker lösning,
- skalbar arkitektur.

Sådana formuleringar uttrycker ambition men hjälper inte mycket när två alternativ ska jämföras.

Kvalitetsprofilen bör i stället göra konsekvensen explicit.

Exempel:

```text
Om en extern användare skickar in ett ärende under normal belastning
ska mottagandet bekräftas inom 3 sekunder i minst 99 % av fallen.
```

eller:

```text
Vid total förlust av primär databas ska tjänstens kritiska
verksamhetsfunktion kunna återställas inom 60 minuter och högst
5 minuters accepterad dataförlust får uppstå.
```

Kvalitetsprofilen behöver inte alltid vara omfattande. Men den bör fånga de egenskaper som faktiskt kan ändra arkitekturen.

En praktisk modell är:

```text
Verksamhetskonsekvens
        ↓
Kvalitetsbehov
        ↓
Mätbart eller prövbart krav
        ↓
Arkitekturdrivare
```

Det är dessa arkitekturdrivare som ska användas när mönster, plattformar och alternativ senare bedöms.

## Steg 3: identifiera verkliga begränsningar

Parallellt med kvalitetsprofilen behöver initiativet identifiera begränsningar.

En begränsning är något lösningen måste förhålla sig till även om arkitekten hade föredragit något annat.

Exempel kan vara:

- ett externt system erbjuder endast ett visst protokoll,
- lagstiftning kräver viss informationshantering,
- ett befintligt avtal gäller under en bestämd period,
- lösningen måste fungera i ett frånkopplat nät,
- en kritisk datakälla kan bara förändras vid vissa releasefönster,
- organisationen har beslutat en obligatorisk identitetsstandard.

Det är viktigt att skilja begränsningar från preferenser.

> Vi brukar använda produkt X.

är inte automatiskt en begränsning.

> Organisationens förvaltade plattformstjänst stöder endast produkt X under lösningens planerade livslängd och avsteg skulle kräva separat driftorganisation.

är däremot ett faktiskt beslutsvillkor.

Den skillnaden hjälper initiativet att både respektera verkligheten och undvika att historiska teknikval förkläs till eviga krav.

## Steg 4: hitta berörda förmågor och ansvar

Nästa fråga är inte vilka produkter som behövs utan **vilka typer av IT-stöd lösningen behöver**.

En publik e-tjänst kan exempelvis beröra:

- Interaktion, presentation och kanaler,
- Identitet och tillit,
- Data- och informationshantering,
- Integration och kommunikation,
- Applikationsexekvering och runtime,
- Driftbarhet och motståndskraft,
- Programvaruutveckling och leverans.

Ett AI-baserat handläggarstöd kan dessutom beröra:

- Analys, sökning och AI,
- Process, workflow och ärendehantering,
- Regler och beslut.

Syftet med denna kartläggning är inte att märka lösningen med så många förmågor som möjligt. Syftet är att upptäcka:

- vilka gemensamma erbjudanden som kan återanvändas,
- vilka standarder som kan vara relevanta,
- vilka förmågeansvariga som behöver involveras,
- var ansvarssnitt kan bli otydliga,
- var lösningen riskerar att skapa en ny lokal mekanism trots att en gemensam redan finns.

Här blir förmågekartan ett navigeringsverktyg.

Den säger inte hur systemet ska byggas. Den hjälper initiativet att hitta **rätt frågor och rätt ägare**.

## Steg 5: pröva relevant referensarkitektur

När lösningsklassen är tydlig bör initiativet fråga om det finns en relevant referensarkitektur.

Det kan exempelvis vara:

- publik e-tjänst,
- internt handläggningsstöd,
- integrationsintensivt verksamhetssystem,
- informationsutbyte med extern part,
- containerbaserad tjänst,
- AI-baserat verksamhetsstöd,
- digital arbetsplats.

Referensarkitekturen ska inte kopieras mekaniskt.

Den ska prövas mot initiativets faktiska behov.

En praktisk start är att klassificera innehållet i tre grupper:

1. **Direkt tillämpligt** – delar som passar utan särskild anpassning.
2. **Tillämpligt med variation** – samma arkitekturidé men annan konkret utformning.
3. **Ej tillämpligt eller avvikande** – där initiativets behov eller begränsningar motiverar annan lösning.

Detta gör referensarkitekturen till beslutsunderlag snarare än mall.

Exempel:

```text
Referensarkitektur: Publik e-tjänst

Direkt tillämpligt:
- federerad användaridentitet
- förvaltad API-exponering
- central observerbarhet

Variation:
- dokumentlagring behövs inte
- BFF används endast för mobil kanal

Avsteg:
- extern integrationspart kräver filöverföring i stället för API
```

Redan här uppstår en första spårbarhet mellan gemensam arkitektur och konkret lösning.

## Steg 6: välj mönster utifrån problemet

När de viktiga concerns är kända kan lösningen pröva vilka återanvändbara mönster som hjälper.

Det är viktigt att mönstret väljs för att det passar problemet, inte för att det finns i organisationens katalog.

Exempel:

| Problem | Möjligt mönster |
|---|---|
| Flera konsumenter reagerar på samma händelse | Publicera/prenumerera |
| Mänsklig uppgift väntar i dagar | Human workflow |
| Verksamhetsregler ändras oberoende av processkod | Externaliserade verksamhetsregler |
| Läsintensiv kopia av auktoritativ data behövs | System of record och härledd kopia |
| Genererat AI-svar behöver källgrundas | RAG |
| Tjänst behöver egen maskinidentitet | Tjänsteidentitet |
| Samma artefakt ska gå genom flera miljöer | Build once, promote many |

Mönstret är fortfarande inte hela lösningen.

Det beskriver ett återanvändbart beslut och dess konsekvenser. Den konkreta lösningsarkitekturen behöver fortfarande välja:

- vilka komponenter som får ansvaret,
- vilken data de hanterar,
- vilka kontrakt de använder,
- hur kvalitetskraven realiseras,
- vilka gemensamma tjänster som används.

## Steg 7: pröva gemensamma plattformstjänster

När mönster och ansvar börjar bli tydliga kan initiativet välja vilka gemensamma plattformstjänster som passar.

Detta bör ske som en matchning mellan behov och tjänstekontrakt.

Exempel:

```text
Behov:
Asynkron kommunikation med beständig kö, definierad återförsöksmodell,
central övervakning och stöd för tjänsteidentitet.

Mönster:
Asynkron meddelandekommunikation.

Plattformstjänst:
Enterprise Messaging – om dess tjänstekontrakt uppfyller kvalitetsprofilen.
```

Det centrala uttrycket är *om*.

Principen om standardiserade erbjudanden när de möter behovet innebär inte att den gemensamma tjänsten alltid ska användas. Den innebär att initiativet först ska pröva den och dokumentera orsaken om den inte räcker.

Det ger två möjliga lärdomar:

- lösningen har ett legitimt specialbehov,
- plattformserbjudandet har en lucka som flera konsumenter kan komma att möta.

Båda är värdefulla signaler.

## Steg 8: applicera relevanta standarder och guardrails

Standarderna beskriver sådant som organisationen vill hålla konsekvent.

När lösningen har valt sina centrala strukturer blir det därför möjligt att identifiera vilka standarder som är relevanta.

Exempel:

- API-standard,
- identitetsprotokoll,
- containerstandard,
- observerbarhetsstandard,
- backup/recovery-standard,
- produktstandarder,
- versions-/supportstandarder.

Här är det viktigt att undvika två ytterligheter.

Den ena är att lösningen börjar med hela standardkatalogen och behandlar varje standard som lika relevant.

Den andra är att standarderna kontrolleras först när lösningen redan är färdigdesignad.

Bättre är att koppla standarderna till de faktiska arkitekturdelarna:

```text
Extern API-exponering
    → API-standard

Tjänst-till-tjänst-kommunikation
    → tjänsteidentitetsstandard

Containeriserad workload
    → containerstandard + runtime-profil

Kritisk persistent data
    → backup/recovery-standard + kvalitetsprofil
```

På så sätt blir standarden en del av designen, inte en revisionslista i slutet.

## Steg 9: skapa realistiska alternativ där gemensam arkitektur inte redan avgör frågan

Gemensam arkitektur ska minska mängden lokala beslut, inte eliminera dem.

Ett konkret initiativ kommer fortfarande att möta frågor där flera rimliga alternativ finns.

Exempel:

- synkron API-integration eller asynkron messaging,
- processorkestrering eller eventdriven koreografi,
- relationell lagring eller objektlagring,
- separat BFF eller gemensamt API,
- egen stateless tjänst eller funktionsexekvering,
- lokal sökindexering eller gemensam söktjänst.

Där behöver arkitekten formulera alternativ som är **reellt genomförbara**.

Ett skenalternativ tillför inget.

```text
Alternativ A: organisationens rekommenderade plattform
Alternativ B: tekniskt omöjligt alternativ
```

är inte en analys.

En bättre jämförelse kopplar alternativen till arkitekturdrivarna:

| Drivare | Alternativ A | Alternativ B |
|---|---|---|
| Tillgänglighet | Stark | Stark |
| Latens | Bättre | Sämre |
| Operativ komplexitet | Lägre | Högre |
| Leverantörsberoende | Högre | Lägre |
| Återanvändning | Hög | Medel |
| Lokal specialanpassning | Begränsad | Hög |

Poängen är inte att skapa en matematisk sanning. Poängen är att göra avvägningen synlig.

## Steg 10: dokumentera de beslut som förändrar lösningens konsekvensyta

Alla designval behöver inte en ADR.

Men beslut som påverkar exempelvis:

- ansvar,
- dataägarskap,
- säkerhet,
- interoperabilitet,
- kontinuitet,
- stora framtida migrationskostnader,
- gemensamma beroenden,
- avsteg från standard eller referensarkitektur,

bör normalt dokumenteras på ett sätt som bevarar *varför*.

Ett användbart beslut kan beskriva:

```text
Beslut
Vi använder asynkron messaging mellan ärendetjänsten och dokumenttjänsten.

Drivare
Dokumentgenerering kan ta lång tid och ska inte blockera användarens transaktion.

Alternativ
Synkront API-anrop; schemalagd batch; asynkron messaging.

Konsekvenser
Eventual consistency, behov av idempotens, återförsök och operativ köövervakning.

Gemensam arkitektur
Enterprise Messaging används enligt organisationens messagingstandard.
```

Då blir lösningsarkitekturen spårbar både bakåt till behovet och uppåt till den gemensamma arkitekturen.

## Avsteg ska vara explicit, inte osynlig variation

En mogen gemensam arkitektur måste tillåta legitima avsteg.

Problemet är inte avsteget i sig. Problemet är när variation uppstår utan att någon vet om den är medveten.

Ett avsteg bör därför minst uttrycka:

- vad lösningen avviker från,
- varför den gemensamma vägen inte räcker,
- vilken risk eller kostnad avsteget skapar,
- vem som accepterar konsekvensen,
- om avsteget är temporärt eller permanent,
- vilket villkor som ska utlösa omprövning.

Exempel:

```text
Avsteg:
Extern integrationspart kan endast ta emot SFTP-baserad filöverföring.

Avviker från:
Referensarkitekturens rekommenderade API-baserade informationsutbyte.

Motivering:
Motpartens tekniska begränsning kan inte påverkas inom initiativets tidsram.

Konsekvens:
Separat filflöde, batchlatens och särskild övervakning krävs.

Omprövning:
När motparten inför nytt integrationsgränssnitt eller senast vid nästa större avtalsperiod.
```

Detta gör avsteget till både lösningsbeslut och återkoppling till den gemensamma arkitekturen.

## Bygg spårbarhet utan att skapa dokumentationsbyråkrati

Spårbarhet betyder inte att varje ruta i ett diagram måste länkas till tio dokument.

Det räcker ofta att kunna följa de viktigaste besluten genom en enkel kedja:

```text
Behov
  ↓
Kvalitetsdrivare / begränsning
  ↓
Arkitekturbeslut
  ↓
Mönster / plattform / standard
  ↓
Konkret lösningsdel
  ↓
Verifiering
```

Anta exempelvis att en tjänst måste kunna återställas inom 30 minuter.

Då kan spårbarheten vara:

```text
Verksamhetskonsekvens:
max 30 minuters avbrott

→ Kvalitetskrav:
RTO ≤ 30 min

→ Arkitekturbeslut:
databasen använder plattformens högre recoveryprofil

→ Gemensam tjänst:
Relationell databastjänst + Backup/Recovery Service

→ Verifiering:
återställningsövning mäter faktisk tid
```

Det är en användbar spårbarhet eftersom den kan svara på två viktiga frågor:

> Varför byggde vi så här?

och:

> Hur vet vi att lösningen uppfyller behovet?

## Lösningsarkitekturen ska beskriva faktisk struktur och faktisk ansvarsfördelning

När analysen mognat behöver lösningsarkitekturen bli konkret.

Den bör inte bara vara ett diagram över produkter. Den behöver uttrycka åtminstone:

- relevanta aktörer och externa parter,
- centrala domäner och ansvar,
- komponenter eller tjänster,
- informationsägarskap och viktiga dataflöden,
- integrationskontrakt,
- identitets- och tillitsgränser,
- runtime och plattformsberoenden,
- kvalitetsdrivande mekanismer,
- observerbarhet och recovery,
- viktiga arkitekturbeslut,
- kända avsteg och risker.

Hur detta dokumenteras kan variera.

Organisationen kan använda:

- diagram,
- text,
- ADR,
- modelleringsverktyg,
- maskinläsbar konfiguration,
- kod och infrastructure-as-code.

Det viktiga är att arkitekturbeskrivningen kan stödja de personer som behöver förstå och förändra lösningen.

Lösningsarkitektur är därför inte liktydigt med en viss diagramnotation.

## Fördela ansvar mellan tre nivåer

Den tredelade ansvarmodellen från kapitel 7 blir särskilt viktig i ett konkret initiativ.

### Gemensam nivå

Den gemensamma nivån bör främst äga:

- principer,
- gemensamma kvalitetsdimensioner,
- förmågekarta,
- tvärgående standarder,
- modell för avsteg,
- referensarkitekturer med bred räckvidd,
- gemensamma regler för spårbarhet och livscykel.

Den ska inte designa varje lösning.

### Förmåge- och plattformsnivå

Förmågeansvariga och plattformsteam bör äga:

- återanvändbara mönster inom området,
- tjänstekontrakt,
- förmågespecifika standarder,
- golden paths,
- tekniklivscykel,
- vägledning och stöd,
- återkoppling från konsumenter.

De ska inte äga verksamhetsdomänens beslut.

### Lösnings-/produktnivå

Det konkreta initiativet behöver äga:

- sin domänmodell,
- sina verksamhetskrav,
- sin kvalitetsprofil,
- sina lokala arkitekturbeslut,
- sin faktiska implementation,
- konsekvenserna av sina avsteg,
- verifiering i den verkliga lösningen.

Den här gränsdragningen skapar autonomi utan att varje lösning behöver uppfinna sin egen teknikplattform.

## Arkitekturgranskning bör kontrollera resonemang, inte estetisk likhet

Om en organisation använder arkitekturgranskning finns en risk att granskningen blir:

> Ser lösningen ut som vår referensbild?

Det är ett för svagt kriterium.

En bättre granskning frågar exempelvis:

- Är behov och kvalitetsdrivare tydliga?
- Är ansvar och dataägarskap begripliga?
- Har relevanta gemensamma tjänster prövats?
- Är viktiga standarder tillämpade?
- Är avsteg explicita och motiverade?
- Är säkerhets- och tillitsgränser synliga?
- Är drift, återställning och livscykel hanterade?
- Finns det oavsiktlig koppling eller otydligt delat ansvar?
- Kan de viktigaste arkitekturbesluten härledas till faktiska behov?

Granskningen blir då en kvalitetskontroll av beslutsprocessen snarare än en jakt på diagramavvikelser.

## Flytta så mycket som möjligt från manuell granskning till gemensamma mekanismer

Ett annat viktigt mål är att arkitekturprocessen inte ska behöva upptäcka samma fel manuellt gång på gång.

Om en viss regel är stabil och maskinellt verifierbar bör den helst flyttas till:

- plattformen,
- CI/CD,
- policy-as-code,
- golden path,
- template,
- automatiserad compliancekontroll.

Exempel:

```text
Manuell arkitekturregel:
"Alla tjänster ska exponera standardiserad health endpoint."

Mognare mekanism:
Golden path genererar endpointen och pipeline verifierar att den finns.
```

Då kan arkitekturen lägga mer tid på frågor som faktiskt kräver omdöme:

- domängränser,
- kvalitetsavvägningar,
- informationsägarskap,
- nya typer av risk,
- legitima avsteg.

Det är samma utveckling som beskrevs i kapitel 30: från dokumenterad rekommendation till förvaltad och exekverbar paved road.

## Verifiera arkitekturen genom de kvaliteter som drev den

En lösningsarkitektur är inte verifierad för att dokumentet är godkänt.

Den måste prövas mot sina drivare.

Exempel:

| Arkitekturdrivare | Möjlig verifiering |
|---|---|
| RTO ≤ 30 min | Återställningsövning |
| Hög belastning | Lasttest |
| Behörighetsseparation | Säkerhetstest och access review |
| Eventual consistency | Test av fördröjning och reconciliation |
| Spårbar AI | Utvärdering av källträff och citering |
| Portabilitet | Reproducerbar driftsättning i alternativ miljö |
| Observerbarhet | Incidentövning med telemetri |

Det är här kedjan sluts:

```text
Behov
  ↓
Arkitekturdrivare
  ↓
Arkitekturval
  ↓
Implementation
  ↓
Verifiering
  ↓
Evidens
```

Utan sista länken vet organisationen egentligen bara att lösningen *designades för* att uppfylla kravet.

Inte att den gör det.

## Återkoppla erfarenheterna uppåt

Den konkreta lösningen är inte bara konsument av gemensam arkitektur. Den är också en viktig källa till lärande.

När flera initiativ gör samma avsteg kan det betyda att:

- standarden är för snäv,
- referensarkitekturen saknar ett variation point,
- en plattformstjänst har otillräcklig funktion,
- ett nytt mönster behöver dokumenteras,
- förmågegränsen är fel,
- ett lokalt behov egentligen har blivit gemensamt.

När samma lokala lösning återkommer kan den röra sig uppåt i modellen:

```text
Lokalt beslut
    ↓
återkommer i flera lösningar
    ↓
dokumenterat lösningsmönster
    ↓
gemensam plattformskapabilitet
    ↓
golden path eller standard
```

Detta är en central del av den iterativa modellen från kapitel 7.

Den gemensamma arkitekturen ska alltså inte bara styra lösningarna. **Lösningarna ska förbättra den gemensamma arkitekturen.**

## Ett sammanhängande exempel: publik e-tjänst

Anta att en myndighet ska skapa en ny publik tjänst där företag kan lämna en ansökan och följa dess status.

### Behov

- företag behöver kunna lämna ansökan digitalt,
- användaren ska kunna återkomma och se status,
- handläggare arbetar vidare i ett internt system,
- bilagor kan vara stora,
- vissa beslut fattas först efter mänsklig granskning.

### Kvalitetsdrivare

- stark användaridentifiering,
- hög spårbarhet,
- god tillgänglighet,
- återställningsbar verksamhetsdata,
- säker dokumenthantering,
- tydlig separation mellan extern och intern zon.

### Berörda förmågor

- Interaktion, presentation och kanaler,
- Identitet och tillit,
- Process, workflow och ärendehantering,
- Data- och informationshantering,
- Integration och kommunikation,
- Applikationsexekvering och runtime,
- Driftbarhet och motståndskraft,
- Programvaruutveckling och leverans.

### Referensarkitektur

*Publik e-tjänst* används som utgångspunkt.

### Mönster

- BFF för den publika kanalen,
- Human workflow för väntande handläggningssteg,
- Tjänsteidentitet mellan interna tjänster,
- System of record med härledda statusvyer,
- Build once, promote many,
- Observerbarhet för distribuerade tjänster.

### Plattformstjänster

- Workforce/external identity enligt organisationens modell,
- Container Application Platform,
- Relationell databastjänst,
- Object Storage Service,
- API Management,
- Monitoring/Tracing Service,
- Backup/Recovery Service.

### Standarder

- API-standard,
- identitetsstandard,
- containerstandard,
- observerbarhetsstandard,
- backup/recoverystandard.

### Lokala arkitekturbeslut

- exakt domänindelning,
- ansökningsmodell,
- vilka statusar som exponeras externt,
- dokumentens metadata,
- integration mot handläggningssystemet,
- val mellan synkront API och messaging i vissa flöden.

### Avsteg

Det äldre handläggningssystemet kan endast ta emot nattlig filimport för en viss del av processen. Avsteget dokumenteras och ges ett omprövningsvillkor kopplat till systemets planerade modernisering.

I detta exempel är lösningsarkitekturen inte en kopia av referensarkitekturen. Den är en **spårbar konkretisering** av den, kombinerad med faktiska behov, kvalitetsdrivare, plattformserbjudanden och lokala beslut.

## En praktisk arbetsordning

För ett konkret initiativ kan arbetsflödet sammanfattas i tolv frågor:

1. Vilket verksamhetsproblem eller vilken möjlighet ska lösas?
2. Vilka kvalitetsattribut och verksamhetskonsekvenser driver arkitekturen?
3. Vilka begränsningar är verkliga?
4. Vilka domäner och gemensamma IT-förmågor berörs?
5. Finns en relevant referensarkitektur?
6. Vilka delar av den är direkt tillämpliga, varierande eller inte tillämpliga?
7. Vilka lösningsmönster passar de återkommande problemen?
8. Vilka gemensamma plattformstjänster uppfyller behoven?
9. Vilka standarder och guardrails gäller?
10. Vilka beslut återstår lokalt och vilka realistiska alternativ finns?
11. Vilka avsteg och risker måste dokumenteras?
12. Hur ska de kvaliteter som drev arkitekturen verifieras i verkligheten?

Ordningen är vägledande, inte mekanisk.

Under arbetet kommer svaren att påverka varandra. Det är förväntat.

## Från arkitekturprocess till arkitekturförmåga

Den viktigaste effekten av modellen uppstår när den används upprepade gånger.

I början kan varje initiativ behöva mycket aktiv hjälp för att navigera:

- förmågor,
- mönster,
- standarder,
- plattformar,
- referensarkitekturer.

När organisationen mognar kan mer av kunskapen flyttas till:

- sökbar arkitekturkatalog,
- automatiserad discovery,
- golden paths,
- plattformsportaler,
- policy-as-code,
- maskinläsbara standarder,
- återanvändbara beslutsmallar.

Då blir arkitekturen mindre beroende av att enskilda personer känner till alla dokument.

Det långsiktiga målet är inte fler arkitekturdokument. Det är att göra **goda arkitekturbeslut lättare att fatta, lättare att återanvända och lättare att verifiera**.

## Sammanfattning

Resan från behov till lösningsarkitektur kan sammanfattas som en kedja av successiv konkretisering:

```text
Behov
  ↓
Kvalitetsprofil och begränsningar
  ↓
Förmågor och ansvar
  ↓
Referensarkitektur
  ↓
Mönster
  ↓
Plattformstjänster
  ↓
Standarder och guardrails
  ↓
Lokala arkitekturbeslut
  ↓
Lösningsarkitektur
  ↓
Verifiering och återkoppling
```

Gemensam arkitektur ska ta bort onödiga lokala beslut, men inte ersätta det omdöme som krävs i en konkret lösning.

Referensarkitekturen ger utgångsläget. Mönstren ger återanvändbar beslutserfarenhet. Plattformarna ger konsumtionsbara gemensamma mekanismer. Standarderna ger konsekventa gränser. Lösningsarkitekturen kombinerar allt detta med initiativets faktiska behov.

Det är först när denna kedja fungerar i praktiken som förmågemodellen blir mer än en katalog.

Nästa kapitel prövar modellen mot sju återkommande lösningsscenarier och visar hur samma arkitekturbyggstenar får olika betydelse beroende på lösningsklass, kvalitetsprofil och verksamhetskonsekvens.
