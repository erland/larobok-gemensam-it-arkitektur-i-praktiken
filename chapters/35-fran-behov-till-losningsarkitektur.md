# 35. Från behov till lösningsarkitektur

När en organisation har etablerat gemensamma förmågor, lösningsmönster, plattformstjänster, standarder och referensarkitekturer återstår den fråga som avgör om modellen fungerar i vardagen:

> Hur använder ett konkret initiativ allt detta för att fatta bättre arkitekturbeslut utan att skapa ett parallellt dokumentationsspår?

Lösningsarkitektur börjar inte när någon ritar komponenter. Den börjar när ett verksamhetsbehov formuleras, när kvalitetsdrivare och begränsningar blir synliga och när initiativet avgör vilka delar av den gemensamma arkitekturen som går att återanvända och vilka beslut som fortfarande måste fattas lokalt.

Lösningsarkitekturen är därför den konkreta tillämpningen av den gemensamma arkitekturen.

En förenklad kedja är:

```text
Behov och verksamhetskonsekvenser
            ↓
Kvalitetsprofil och begränsningar
            ↓
Förmågor och ansvar
            ↓
Referensarkitektur
            ↓
Mönster, plattformar och standarder
            ↓
Lokala alternativ och arkitekturbeslut
            ↓
Konkret lösningsarkitektur
            ↓
Verifiering, leverans och återkoppling
```

Kedjan är inte ett vattenfall. Ett plattformsval kan synliggöra ett nytt kvalitetsproblem och ett proof of concept kan visa att ett tidigare antagande var fel. Det viktiga är att besluten förblir spårbara mellan *varför*, *vad* och *hur*.

## Börja med beslutssituationen

Ett vanligt fel är att starta med frågan:

> Vilket arkitekturdokument ska vi ta fram?

Bättre är:

> Vilka beslut behöver initiativet fatta, vilka konsekvenser har de och vilka av dem kan den gemensamma arkitekturen redan hjälpa oss med?

Ett mindre internt verktyg och en samhällskritisk extern tjänst behöver inte samma analysdjup. Omfattningen bör stå i proportion till exempelvis verksamhetskonsekvens, informationskänslighet, antal beroenden, krav på kontinuitet, förändringstakt och hur svåra besluten är att ändra i efterhand.

Arkitekturarbetet ska alltså skapa tillräcklig evidens för de beslut som faktiskt spelar roll, inte maximera antalet artefakter.

## En sammanhängande process från behov till lösning

### 1. Formulera behovet utan att gömma lösningen i frågan

Resan börjar med behovet. Tekniska idéer får gärna finnas, men de får inte ersätta problemformuleringen.

> Vi behöver Kafka.

är ett lösningsförslag.

> Flera oberoende konsumenter behöver reagera på samma verksamhetshändelser utan att producenten behöver känna till dem.

är ett behov som går att analysera.

På samma sätt är ”vi behöver ett AI-stöd” för svagt. Ett bättre ingångsvärde är att handläggare behöver hitta relevant information snabbare, att svaret måste kunna härledas till källmaterial och att beslutet fortfarande ska fattas av en ansvarig människa. Då syns redan arkitekturdrivare som sökkvalitet, spårbarhet, behörighet, mänsklig kontroll och svarstid.

**Beslutspunkt:** vilket problem ska lösas och vilka verksamhetskonsekvenser är viktigast?

### 2. Gör kvalitetsprofilen konkret

Kvaliteter som ”hög tillgänglighet”, ”god prestanda” och ”säker lösning” uttrycker ambition men hjälper föga när alternativ ska jämföras.

Kvalitetsprofilen bör därför göra konsekvensen prövbar. Exempel:

```text
Om en extern användare skickar in ett ärende under normal belastning
ska mottagandet bekräftas inom 3 sekunder i minst 99 % av fallen.
```

eller:

```text
Vid total förlust av primär databas ska kritisk verksamhetsfunktion
kunna återställas inom 60 minuter och högst 5 minuters dataförlust
accepteras.
```

Kvalitetsprofilen behöver inte vara stor. Den behöver fånga de egenskaper som faktiskt kan ändra arkitekturen.

**Beslutspunkt:** vilka kvalitetskrav är så viktiga att de ska styra arkitekturval och senare verifiering?

### 3. Identifiera verkliga begränsningar

En begränsning är något lösningen måste förhålla sig till även om arkitekten hade föredragit något annat. Det kan vara lagstiftning, ett externt protokoll, ett bindande avtal, ett frånkopplat nät eller en obligatorisk identitetsstandard.

Det är viktigt att skilja begränsning från vana.

> Vi brukar använda produkt X.

är inte automatiskt ett beslutsvillkor.

> Organisationens förvaltade plattformstjänst stöder endast produkt X under lösningens planerade livslängd och avsteg kräver separat driftansvar.

är däremot en verklig begränsning.

**Beslutspunkt:** vilka villkor är faktiskt givna och vilka är bara preferenser eller historiska val?

### 4. Hitta berörda förmågor och ansvar

Nästa fråga är inte vilka produkter som behövs utan vilka typer av IT-stöd lösningen behöver.

En *publik e-tjänst* kan exempelvis beröra Interaktion, Identitet, Data, Integration, Runtime, Driftbarhet samt Programvaruutveckling och leverans. Ett AI-baserat handläggarstöd kan dessutom beröra Analys, sökning och AI samt *Process, workflow och ärendehantering*.

Förmågekartan används här som navigeringsverktyg för att hitta:

- relevanta gemensamma erbjudanden,
- förmågespecifika standarder,
- ansvariga team,
- otydliga ansvarssnitt,
- risk för onödig lokal duplicering.

Den säger inte hur systemet ska byggas.

**Beslutspunkt:** vilka förmågeområden behöver bidra och vilka ansvar ligger fortfarande hos lösningen själv?

### 5. Pröva relevant referensarkitektur

Om lösningsklassen motsvarar en befintlig referensarkitektur ska den användas som utgångspunkt, inte kopieras mekaniskt.

Ett praktiskt sätt är att klassificera dess innehåll som:

1. **Direkt tillämpligt** – kan användas som det är.
2. **Tillämpligt med variation** – samma arkitekturidé men annan konkret utformning.
3. **Avvikande eller ej tillämpligt** – behov eller begränsningar motiverar annan lösning.

Exempel:

```text
Referensarkitektur: Publik e-tjänst

Direkt tillämpligt:
- förvaltad API-exponering
- central observerbarhet

Variation:
- dokumentlagring behövs inte

Avsteg:
- extern part kräver filöverföring i stället för API
```

**Beslutspunkt:** vilka gemensamma arkitekturval kan återanvändas och var behövs medveten variation?

### 6. Välj mönster utifrån problemet

Lösningsmönster ska väljas för att de passar problemet, inte för att de råkar finnas i en katalog.

| Problem | Möjligt mönster |
|---|---|
| Flera konsumenter reagerar på samma händelse | Publicera/prenumerera |
| Mänsklig uppgift väntar i dagar | Human workflow |
| Verksamhetsregler ändras oberoende av processkod | Externaliserade verksamhetsregler |
| Läsintensiv kopia av auktoritativ data behövs | System of record och härledd kopia |
| Genererat AI-svar behöver källgrundas | RAG |
| Tjänst behöver egen maskinidentitet | Tjänsteidentitet |
| Samma artefakt ska gå genom flera miljöer | Build once, promote many |

Mönstret löser inte hela designen. Det återanvänder ett beslut och dess kända konsekvenser.

**Beslutspunkt:** vilka återkommande problem kan lösas med etablerade mönster i stället för nya lokala mekanismer?

### 7. Pröva gemensamma plattformstjänster

När mönster och ansvar är tydligare kan de matchas mot gemensamma tjänstekontrakt.

```text
Behov:
Asynkron kommunikation med beständig kö, återförsök,
central övervakning och tjänsteidentitet.

Mönster:
Asynkron meddelandekommunikation.

Plattformstjänst:
Enterprise Messaging – om tjänstekontraktet möter kvalitetsprofilen.
```

Det centrala ordet är *om*. Standardiserade erbjudanden ska prövas först när de passar behovet, inte användas oavsett konsekvens. Om tjänsten inte räcker kan det antingen vara ett legitimt specialbehov eller en signal om att plattformserbjudandet behöver utvecklas.

**Beslutspunkt:** vilka gemensamma tjänster kan konsumeras direkt och vilka behov återstår utanför erbjudandet?

### 8. Applicera relevanta standarder och guardrails

Standarder ska kopplas till de delar av lösningen där de faktiskt är relevanta.

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

Det undviker både att hela standardkatalogen behandlas som lika relevant och att standarderna granskas först när designen redan är klar.

**Beslutspunkt:** vilka bindande eller rekommenderade gränser gäller för den design som nu växer fram?

### 9. Formulera verkliga lokala alternativ

Gemensam arkitektur ska minska antalet lokala beslut, inte eliminera dem.

När flera rimliga alternativ återstår ska de jämföras mot arkitekturdrivarna. Det kan exempelvis gälla synkront API eller messaging, orkestrering eller koreografi, relationell lagring eller objektlagring, separat BFF eller gemensamt API.

| Drivare | Alternativ A | Alternativ B |
|---|---|---|
| Latens | Bättre | Sämre |
| Operativ komplexitet | Lägre | Högre |
| Leverantörsberoende | Högre | Lägre |
| Återanvändning | Hög | Medel |
| Lokal specialanpassning | Begränsad | Hög |

Poängen är inte matematisk exakthet utan att göra avvägningen synlig.

**Beslutspunkt:** vilka frågor är fortfarande lokala och vilket alternativ ger bäst samlad konsekvens?

### 10. Dokumentera viktiga beslut och avsteg

Alla designval behöver inte en ADR. Beslut som påverkar ansvar, dataägarskap, säkerhet, interoperabilitet, kontinuitet, stora framtida migrationskostnader eller avsteg från gemensam arkitektur bör däremot bevara *varför*.

Ett avsteg bör minst uttrycka:

- vad lösningen avviker från,
- varför den gemensamma vägen inte räcker,
- vilken risk eller kostnad avsteget skapar,
- vem som accepterar konsekvensen,
- om avsteget är temporärt eller permanent,
- när det ska omprövas.

Avsteg är därmed inte ett misslyckande i modellen utan en explicit form av variation och en möjlig källa till lärande.

**Beslutspunkt:** vilka val behöver kunna förstås och omprövas långt efter att projektgruppen har förändrats?

## Lösningsarkitekturens faktiska struktur och ansvar

När analysen mognat behöver lösningsarkitekturen beskriva den faktiska lösningen, inte bara produkter eller tekniklager. Den bör göra det möjligt att förstå åtminstone:

- aktörer och externa parter,
- domäner och ansvar,
- komponenter eller tjänster,
- informationsägarskap och viktiga dataflöden,
- integrationskontrakt,
- identitets- och tillitsgränser,
- runtime- och plattformsberoenden,
- kvalitetsdrivande mekanismer,
- observerbarhet och recovery,
- viktiga arkitekturbeslut,
- avsteg och risker.

Dokumentationen kan bestå av diagram, text, ADR, modeller, kod, infrastructure-as-code och maskinläsbar konfiguration. Det viktiga är att den stödjer dem som behöver förstå, bygga, drifta och förändra lösningen.

De tre ansvarsnivåerna behöver inte definieras på nytt här. I en konkret lösning räcker följande arbetsfördelning:

| Nivå | Beslutar framför allt |
|---|---|
| Gemensam arkitektur | Principer, tvärgående standarder, breda referensarkitekturer och avstegsmodell |
| Förmåge-/plattformsnivå | Tjänstekontrakt, mönster, golden paths, förmågespecifika standarder och tekniklivscykel |
| Lösnings-/produktnivå | Domänmodell, kvalitetsprofil, lokala arkitekturbeslut, implementation, avsteg och faktisk verifiering |

Autonomi uppstår när varje nivå fattar rätt typ av beslut och när lösningen kan återanvända det som redan är avgjort högre upp.

## Spårbarhet med minsta nödvändiga dokumentation

Spårbarhet betyder inte att varje ruta i ett diagram behöver tio länkar. Det räcker ofta att kunna följa de viktigaste besluten genom en enkel kedja:

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

Om en tjänst exempelvis måste kunna återställas inom 30 minuter kan kedjan vara:

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

Det räcker för att kunna svara på två centrala frågor: *varför byggde vi så här?* och *hur vet vi att lösningen uppfyller behovet?*

## Verifiera, leverera och återför lärande

Processen slutar inte när ett arkitekturdokument godkänns. De kvaliteter som drev arkitekturen måste prövas i den verkliga lösningen.

| Arkitekturdrivare | Möjlig verifiering |
|---|---|
| RTO ≤ 30 min | Återställningsövning |
| Hög belastning | Lasttest |
| Behörighetsseparation | Säkerhetstest och access review |
| Eventual consistency | Test av fördröjning och reconciliation |
| Spårbar AI | Utvärdering av källträff och citering |
| Observerbarhet | Incidentövning med telemetri |

Arkitekturgranskning bör därför kontrollera resonemang och evidens snarare än estetisk likhet med en referensbild. Stabilt maskinellt verifierbara regler bör samtidigt flyttas från manuella möten till plattformar, CI/CD, policy-as-code och golden paths.

Det frigör granskningen för frågor som kräver omdöme: domängränser, informationsägarskap, kvalitetsavvägningar, nya risker och legitima avsteg.

När samma avsteg eller lokala lösning återkommer i flera initiativ ska erfarenheten återföras till den gemensamma arkitekturen:

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

Lösningen är alltså både konsument av och lärandekälla för den gemensamma arkitekturen.

## Ett sammanhängande exempel: publik e-tjänst

Anta att en myndighet ska skapa en ny publik tjänst där företag kan lämna en ansökan och följa dess status. Exemplet visar processen; nästa kapitel använder samma typ av scenario mer översiktligt för att stresstesta modellens bredd.

**Behov och kvalitetsprofil.** Företag ska kunna lämna ansökan digitalt och följa status. Bilagor kan vara stora och viss handläggning sker manuellt. Stark användaridentifiering, spårbarhet, säker dokumenthantering, god tillgänglighet och återställningsbar verksamhetsdata blir arkitekturdrivande.

**Förmågor och referensarkitektur.** Lösningen berör bland annat *Interaktion, presentation och kanaler*, Identitet, Process, Data, Integration, Runtime och Driftbarhet. Referensarkitekturen *Publik e-tjänst* används som utgångspunkt och dess delar klassificeras som direkt tillämpliga, varierande eller avvikande.

**Mönster och plattformar.** BFF kan användas för den publika kanalen, Human workflow för väntande handläggningssteg, Tjänsteidentitet mellan interna tjänster och System of record med härledda statusvyer för att skilja auktoritativ data från publik läsmodell. Gemensamma tjänster för identitet, API-exponering, runtime, databas, objektlagring, observerbarhet och recovery prövas mot kvalitetsprofilen.

**Standarder och lokala beslut.** API-, identitets-, container-, observerbarhets- och recovery-standarder appliceras där de är relevanta. Därefter återstår lokala beslut om domänindelning, vilka statusar som får exponeras, dokumentmetadata och hur integrationen mot det interna handläggningssystemet ska ske.

**Avsteg och verifiering.** Om ett äldre system endast kan ta emot en nattlig filimport dokumenteras det som avsteg med omprövningsvillkor. Tillgänglighet och recovery verifieras sedan genom test och återställningsövning, inte enbart genom att designen ser rimlig ut.

Lösningsarkitekturen blir därmed inte en kopia av referensarkitekturen utan en spårbar konkretisering av den.

## Kort checklista

Checklistan speglar samma process och är tänkt som ett stöd, inte som en alternativ arbetsordning:

1. Är behov och verksamhetskonsekvenser tydliga?
2. Vilka kvalitetsdrivare och verkliga begränsningar styr lösningen?
3. Vilka förmågor och ansvar berörs?
4. Vilken referensarkitektur, vilka mönster och vilka plattformstjänster kan återanvändas?
5. Vilka standarder och guardrails gäller?
6. Vilka lokala alternativ och arkitekturbeslut återstår?
7. Finns explicita och motiverade avsteg?
8. Kan viktiga beslut spåras från behov till lösningsdel?
9. Hur verifieras de kvaliteter som drev arkitekturen?
10. Vilket lärande ska återföras till den gemensamma arkitekturen?

## Sammanfattning

Från behov till lösningsarkitektur handlar om successiv konkretisering, inte om att fylla i en mall.

Gemensam arkitektur tar bort onödiga lokala beslut. Referensarkitekturen ger utgångsläget. Mönstren återanvänder beslutserfarenhet. Plattformarna ger konsumtionsbara mekanismer. Standarderna sätter konsekventa gränser. Lösningsarkitekturen kombinerar allt detta med initiativets faktiska behov och bevarar de lokala beslut som fortfarande behöver fattas.

Kedjan är inte färdig förrän lösningen har verifierats och erfarenheterna återförts. Först då blir den gemensamma arkitekturen en lärande förmåga snarare än en katalog.

Nästa kapitel prövar modellen mot sju återkommande lösningsscenarier. Där ligger fokus inte på den fullständiga arbetsprocessen utan på hur samma arkitekturbyggstenar får olika betydelse beroende på lösningsklass, kvalitetsprofil och verksamhetskonsekvens.
