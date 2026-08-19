# 34. Vad en referensarkitektur är – och inte är

När en organisation har definierat gemensamma förmågor, lösningsmönster, plattformstjänster och standarder uppstår en naturlig fråga: hur ska allt detta sättas samman när en viss typ av lösning återkommer gång på gång?

Det är här referensarkitekturen får sin roll.

En referensarkitektur ska göra mer än att lista vilka tekniker som är godkända. Den ska samtidigt göra mindre än att designa ett konkret system. Dess värde ligger i mellanrummet: den återanvänder arkitekturerfarenhet för en klass av lösningar och ger ett gemensamt utgångsläge utan att låsa varje implementation till samma detaljdesign.

I den här boken används därför följande arbetsdefinition:

> En referensarkitektur är en förvaltad, återanvändbar arkitekturbeskrivning för en avgränsad klass av lösningar. Den beskriver relevanta concerns, strukturer, ansvar, obligatoriska begränsningar, rekommenderade mönster, gemensamma tjänster och explicita variation points, så att en konkret lösningsarkitektur kan härledas snabbare och mer konsekvent.

Definitionen är avsiktligt praktisk. Begreppet *referensarkitektur* används på olika sätt i olika organisationer och ramverk. Det viktiga är därför inte att hitta en enda universell definition, utan att organisationen är tydlig med vilket problem artefakten ska lösa, vilken abstraktionsnivå den har och hur den relaterar till andra arkitekturartefakter.

Detta kapitel etablerar den rollen. Nästa kapitel visar sedan hur ett konkret initiativ går från behov till faktisk lösningsarkitektur med referensarkitekturen som ett av flera beslutsunderlag.

## Varför behövs en referensarkitektur?

Anta att en organisation under några år bygger flera publika e-tjänster. De skiljer sig åt i verksamhetslogik, användargrupper och data, men återkommer till samma frågor:

- hur användaren autentiseras,
- hur frontend och backend separeras,
- hur API:er exponeras,
- hur verksamhetsdata lagras,
- hur dokument hanteras,
- hur integrationer sker,
- hur loggning och tracing byggs in,
- hur tjänsten levereras och körs,
- hur återställning hanteras,
- vilka standarder och gemensamma plattformar som ska användas.

Om varje projekt börjar från noll kommer organisationen att fatta samma typer av beslut om och om igen. Resultatet blir inte bara högre kostnad. Det skapar också variation som senare måste förvaltas.

Motsatsen är inte att skapa en enda obligatorisk lösningsdesign för alla e-tjänster. Det skulle göra arkitekturen oförmögen att hantera verkliga skillnader.

Referensarkitekturen försöker i stället fånga det som rimligen bör återanvändas.

```text
Återkommande lösningsklass
          ↓
Gemensamma concerns och kvalitetsbehov
          ↓
Återanvändbara arkitekturbeslut
          ↓
Referensarkitektur
          ↓
Konkret initiativ
          ↓
Lösningsarkitektur med explicita variationer
```

Värdet är alltså inte att alla lösningar blir identiska. Värdet är att variation blir medveten, lokaliserad och motiverad.

## En referensarkitektur beskriver en klass av lösningar

Den viktigaste gränsdragningen är att en referensarkitektur inte beskriver *ett specifikt system*.

Den beskriver exempelvis:

- publik e-tjänst,
- internt handläggningsstöd,
- integrationsintensivt verksamhetssystem,
- informationsutbyte med extern part,
- containerbaserad tjänst,
- AI-baserat verksamhetsstöd,
- digital arbetsplats.

Det är lösningsklasser där tillräckligt många arkitekturfrågor återkommer för att gemensam vägledning ska ge värde.

En referensarkitektur för publik e-tjänst kan därför beskriva att lösningen typiskt behöver:

```text
Användare
   ↓
Publikt webbgränssnitt
   ↓
API-/BFF-lager
   ↓
Domäntjänster
   ├─ identitet och behörighet
   ├─ verksamhetsdata
   ├─ dokument
   ├─ integrationer
   └─ observerbarhet
```

Men den behöver inte bestämma:

- exakt antal tjänster,
- exakt domänindelning,
- tabellstruktur,
- URL-struktur,
- antal repliker,
- exakt produktversion,
- vilka verksamhetsregler den konkreta tjänsten innehåller.

Dessa frågor hör normalt hemma i den faktiska lösningsarkitekturen och implementationen.

Referensarkitekturen måste därför befinna sig på en abstraktionsnivå där den är tillräckligt konkret för att styra återkommande beslut men tillräckligt generell för att återanvändas.

## Referensarkitektur är inte lösningsarkitektur

Det vanligaste missförståndet är att referensarkitekturen ses som en färdig lösningsarkitektur som bara ska kopieras.

Skillnaden kan beskrivas så här:

| Referensarkitektur | Lösningsarkitektur |
|---|---|
| Gäller en klass av lösningar | Gäller ett konkret initiativ eller system |
| Återanvändbar | Situationsspecifik |
| Beskriver typiska strukturer och ansvar | Beskriver faktisk struktur och faktiska beslut |
| Har explicita variation points | Väljer en konkret variant |
| Pekar på gemensamma mönster och tjänster | Väljer vilka som faktiskt används |
| Beskriver begränsningar som gäller lösningsklassen | Hanterar även lokala begränsningar |
| Förvaltas över flera initiativ | Förvaltas med den konkreta lösningen |

Sambandet är inte:

```text
Referensarkitektur = lösningsarkitektur
```

utan snarare:

```text
Referensarkitektur
      +
konkreta behov
      +
kvalitetsprofil
      +
lokala begränsningar
      +
arkitekturbeslut
      ↓
Lösningsarkitektur
```

Detta gör också att avsteg från en referensarkitektur inte automatiskt är fel. Ett avsteg kan vara helt korrekt om den konkreta lösningen har andra kvalitetsdrivare eller begränsningar.

Det viktiga är att avvikelsen blir synlig och motiverad.

## Referensarkitektur är inte ett lösningsmönster

Ett lösningsmönster fokuserar på ett återkommande designproblem.

Exempel från tidigare kapitel är:

- Backend for Frontend,
- asynkron meddelandekommunikation,
- human workflow,
- externaliserade verksamhetsregler,
- cache-aside,
- RAG,
- tjänsteidentitet,
- build once, promote many.

Referensarkitekturen har bredare scope. Den kan kombinera flera mönster för en viss lösningsklass.

En referensarkitektur för AI-baserat verksamhetsstöd kan exempelvis använda:

- RAG,
- AI med mänsklig kontroll,
- tjänsteidentitet,
- stateless runtime,
- observerbarhet,
- auktoritativ informationskälla.

Mönstret svarar alltså ungefär på:

> Hur kan ett återkommande arkitekturproblem struktureras?

Referensarkitekturen svarar snarare på:

> Hur ser en rimlig sammanhängande arkitektur ut för den här typen av lösning, och vilka beslut bör återanvändas?

Referensarkitekturen bör därför referera till mönster i stället för att kopiera hela mönsterbeskrivningen in i varje dokument.

## Referensarkitektur är inte en standard

En standard beskriver sådant organisationen vill göra konsekvent.

Den kan exempelvis ange:

- godkänd API-profil,
- identitetsprotokoll,
- observerbarhetskrav,
- containerkrav,
- produktstandard,
- supportversioner,
- konfigurationsstandard.

Referensarkitekturen kan hänvisa till dessa standarder, men standarden och referensarkitekturen har olika roller.

```text
Standard
  → vad som ska vara konsekvent

Referensarkitektur
  → hur flera återanvändbara delar hänger ihop i en lösningsklass
```

Om alla standarder kopieras in i referensarkitekturen uppstår dubbel dokumentation och livscykelproblem. När en standard ändras riskerar flera referensarkitekturer att bli inaktuella samtidigt.

Bättre är att referensarkitekturen uttrycker beroendet:

> Externa API:er ska följa organisationens aktuella API-standard.

inte:

> Här är en kopia av alla regler i API-standarden.

Detta följer samma princip som boken använt genomgående: stabila artefakter ska referera till mer föränderliga artefakter i stället för att duplicera dem.

## Referensarkitektur är inte en plattform

En annan sammanblandning sker när en organisation säger att den har en ”referensarkitektur” men dokumentet egentligen bara visar en plattformsprodukt.

Exempel:

```text
Ingress
  ↓
Containerplattform
  ↓
Databastjänst
```

Det kan vara en värdefull plattformsbild, men är inte automatiskt en referensarkitektur.

En referensarkitektur behöver utgå från lösningens concerns och kvalitetsbehov, inte från vilka produkter plattformsteamet råkar erbjuda.

Den kan däremot beskriva att en viss lösningsklass normalt realiseras genom organisationens containerplattform, databastjänst, identitetstjänst och observerbarhetstjänster.

Skillnaden är viktig:

- plattformen beskriver ett gemensamt erbjudande,
- referensarkitekturen beskriver hur flera erbjudanden och mönster kan kombineras i en lösningsklass.

Plattformskatalogen svarar på *vad som går att konsumera*. Referensarkitekturen hjälper till att svara på *hur det kan sättas samman*.

## Referensarkitektur är inte en template eller starter kit

En template är exekverbar eller kopierbar utgångspunkt.

Det kan vara:

- Git-repository,
- kodskelett,
- pipeline,
- infrastructure-as-code-modul,
- Helm chart,
- konfigurationspaket.

Templates är mycket konkreta och ofta starkt knutna till teknikversioner.

Referensarkitekturen är mer långlivad och kan ligga bakom flera olika templates.

```text
Referensarkitektur
       ↓
Golden path / paved road
       ↓
Templates och automation
       ↓
Konkret lösning
```

Detta gör att referensarkitekturen kan överleva när ett repository byter byggverktyg eller när plattformen byter produktversion.

Samtidigt är kopplingen viktig. En referensarkitektur som aldrig påverkar golden paths, templates eller lösningsbeslut riskerar att bli rent presentationsmaterial.

## Scope är referensarkitekturens första beslut

En användbar referensarkitektur börjar med scope.

Det behöver vara tydligt:

- vilken lösningsklass den gäller,
- vilka typer av behov som omfattas,
- vilka närliggande områden som inte omfattas,
- vilka kvalitetsprofiler den är avsedd för,
- vilka organisatoriska eller regulatoriska förutsättningar som antas.

Ett för brett scope ger lätt en generisk bild som säger nästan ingenting.

Ett för smalt scope gör artefakten så situationsspecifik att den lika gärna kunde vara en lösningsarkitektur.

Ett praktiskt test är att fråga:

> Finns det flera verkliga eller sannolika lösningar som kan använda samma arkitekturvägledning utan att deras viktigaste skillnader försvinner?

Om svaret är nej är referensarkitekturens scope sannolikt fel.

## Concerns och viewpoints gör dokumentet användbart för fler än en läsare

En arkitektur har flera intressenter och flera typer av frågor. En enda komponentbild kan därför sällan bära hela referensarkitekturen.

ISO/IEC/IEEE 42010 skiljer mellan arkitekturen och den beskrivning som uttrycker den[K1], och använder bland annat *viewpoints* och *views* för att strukturera arkitekturbeskrivningar. Boken behöver inte göra varje referensarkitektur formellt konform med standarden för att använda samma grundidé: olika concerns behöver ofta olika vyer.

För en publik e-tjänst kan relevanta viewpoints exempelvis vara:

- logisk struktur,
- informationsflöden,
- integrationer,
- identitet och tillit,
- driftsättning/runtime,
- observerbarhet och drift,
- kontinuitet,
- ansvar och ägarskap.

Ett viewpoint kan ses som en återanvändbar regel för vilka frågor en viss vy ska besvara.

Exempel:

> Driftsättning-vyn ska visa exekveringsmiljöer, externa beroenden, zon-/miljögränser och de plattformstjänster som är relevanta för tillgänglighet och drift.

Den konkreta vyn visar sedan dessa aspekter för referensarkitekturen.

Det viktiga är inte att maximera antalet diagram. Det viktiga är att varje vy har ett tydligt syfte.

## Variation points är en kärndel – inte ett tecken på ofullständighet

En svag referensarkitektur försöker ofta dölja variation. Den visar en lösning och kallar den ”referens”.

En stark referensarkitektur beskriver i stället explicit var variation är förväntad och vilka drivkrafter som avgör valet.

Exempel för en publik e-tjänst:

### Autentisering

Variation kan bero på:

- anonym åtkomst,
- privatperson,
- organisation,
- medarbetare,
- federerad extern identitet.

Referensarkitekturen bör inte nödvändigtvis välja en enda variant. Den bör beskriva hur valet ska göras och vilka gemensamma identitetstjänster som finns.

### Integrationsform

Variation kan vara:

- synkront API,
- asynkront meddelande,
- event,
- filbaserat utbyte.

Valet beror på bland annat tidskoppling, volym, leveranssemantik och den externa partens förutsättningar.

### Runtime

Variation kan exempelvis bero på:

- containeriserad stateless workload,
- stateful komponent,
- legacy begränsning,
- särskilt hårdvarubehov.

Att dokumentera dessa variation points gör referensarkitekturen mer användbar eftersom den visar var arkitekturarbetet fortfarande måste fatta ett lokalt beslut.

## Begränsningar ska vara få, tydliga och motiverade

Allt i en referensarkitektur bör inte vara valbart.

Det finns ofta begränsningar som gäller hela lösningsklassen.

Exempel:

- externa API:er ska exponeras genom den gemensamma API-hanteringen,
- tjänsteidentiteter ska användas för workload-till-workload-kommunikation,
- produktionslösningar ska producera definierad telemetri för observerbarhet,
- secrets ska hanteras genom den gemensamma secrets-tjänsten,
- publika gränssnitt ska följa organisationens tillgänglighetskrav.

Men varje begränsning behöver ha ett skäl.

En begränsning kan motiveras av:

- säkerhet,
- interoperabilitet,
- regelefterlevnad,
- operativ förmåga,
- gemensamt plattformskontrakt,
- tydlig riskreduktion.

Om referensarkitekturen består av mycket detaljerade obligatoriska val riskerar den att bli en dold produktstandard eller en frusen lösningsdesign.

Obligatoriskt där konsekvensen kräver det; varierbart där lokala behov skiljer sig.

## Kvalitetsprofiler påverkar referensarkitekturen

Två lösningar kan tillhöra samma lösningsklass men ha olika kvalitetsbehov.

Ett internt handläggningsstöd kan exempelvis ha en normal tillgänglighetsprofil. Ett annat stöd kan vara kritiskt för en operativ verksamhet och kräva betydligt kortare RTO, högre tillgänglighet och andra redundansmönster.

Därför bör referensarkitekturen antingen:

1. tydligt ange vilken kvalitetsprofil den är avsedd för, eller
2. beskriva hur arkitekturen varierar mellan definierade kvalitetsprofiler.

Exempel:

```text
Grundprofil
  → standard runtime
  → normal backup/recovery
  → normal kapacitetsmarginal

Förstärkt kontinuitetsprofil
  → zonredundans
  → kortare RPO/RTO
  → utökad recovery-verifiering
  → högre kapacitetsmarginal
```

På så sätt blir referensarkitekturen kopplad till kapitel 4:s kvalitetsmodell i stället för att bara vara en komponentbild.

## En referensarkitektur behöver beskriva ansvar – inte bara komponenter

Arkitekturproblem uppstår ofta i gränserna mellan delar.

Därför bör referensarkitekturen visa ansvar för exempelvis:

- verksamhetslogik,
- processläge,
- auktoritativ data,
- identitet,
- integration,
- dokument,
- observerbarhet,
- plattformsdrift.

Det gör det möjligt att skilja mellan:

```text
Vad lösningen äger
        och
Vad en gemensam plattform äger
```

En referensarkitektur för containerbaserad tjänst bör exempelvis inte bara visa containerplattformen. Den bör också ange att applikationsteamet ansvarar för sådant som:

- korrekt health behavior,
- resursdeklarationer,
- applikationsloggning,
- data- och transaktionsdesign,
- säker användning av credentials.

Plattformsteamet kan samtidigt ansvara för:

- exekveringsmiljön,
- klustrets tillgänglighet,
- gemensamma policyer,
- plattformstelemetri,
- plattformens supportfönster.

Detta gör referensarkitekturen till ett ansvarskontrakt lika mycket som en teknisk bild.

## Traceability gör referensarkitekturen begriplig

Varje viktig del av referensarkitekturen bör kunna härledas till ett behov, kvalitetsattribut, mönster, standard eller gemensamt erbjudande.

Exempel:

```text
Behov: extern part ska kunna skicka ärenden
       ↓
Kvalitet: lös koppling och robust felhantering
       ↓
Mönster: asynkron meddelandekommunikation
       ↓
Plattform: Enterprise Messaging
       ↓
Standard: messaging/event-standard
       ↓
Referensarkitektur: asynkron integrationsväg
```

Spårbarheten gör två saker.

För det första blir arkitekturen lättare att förstå. Ett element finns inte bara därför att ”det alltid finns på bilden”.

För det andra blir förändring lättare. Om plattformen eller standarden ändras går det att se vilka referensarkitekturer som påverkas.

## Referensarkitekturen bör bestå av mer än ett diagram

Ett vanligt anti-pattern är att referensarkitekturen reduceras till en enda PowerPoint-bild.

En bild kan vara ett bra navigationslager, men den räcker sällan för att bära beslutsinformationen.

En praktisk referensarkitektur kan exempelvis innehålla:

1. Syfte och scope
2. Antaganden och avgränsningar
3. Relevanta kvalitetsprofiler
4. Logisk översiktsvy
5. Viktiga informations-/integrationsflöden
6. Identitets- och tillitsmodell
7. Driftsättning/runtime-vy där relevant
8. Ansvarsgränser
9. Obligatoriska begränsningar
10. Variation points och beslutsregler
11. Rekommenderade lösningsmönster
12. Relevanta plattformstjänster
13. Relevanta standarder
14. Kända avvägningar och risker
15. Exempel på tillämpning
16. Livscykel, ägare och ändringshistorik

Alla referensarkitekturer behöver inte alla dessa delar. Modellen bör anpassas till scope och konsekvens.

## En referensarkitektur ska vara normativ på rätt ställen

Det finns en frestelse att göra referensarkitekturen antingen helt normativ eller helt informativ.

Båda ytterligheterna är problematiska.

Om allt är normativt blir artefakten stel och svår att återanvända.

Om inget är normativt blir det oklart om arkitekturen faktiskt påverkar några beslut.

En bättre modell är att markera innehållets status.

Exempel:

| Typ | Betydelse |
|---|---|
| Begränsning | Ska följas om inte godkänt avsteg finns |
| Rekommenderad struktur | Bör vara förstahandsval när angivna förutsättningar gäller |
| Variation point | Lokalt beslut krävs enligt angivna drivkrafter |
| Exempel | Illustrerar möjlig realisering men är inte normerande |
| Referens | Pekar på separat standard, mönster eller tjänstekontrakt |

Detta gör artefakten mer precis utan att varje detalj blir regel.

## Avsteg är del av användningen

Om ett konkret initiativ inte kan följa referensarkitekturen bör frågan inte vara:

> Hur tvingar vi lösningen tillbaka till bilden?

utan:

> Vilken skillnad i behov, kvalitet eller begränsning gör att referensarkitekturen inte passar här?

Det finns åtminstone tre möjliga utfall:

1. Lokalt motiverat avsteg – referensarkitekturen är fortfarande rätt för sin målklass.
2. Ny variation point – flera lösningar visar att referensarkitekturen behöver uttrycka ett legitimt alternativ.
3. Referensarkitekturen är fel eller föråldrad – återkommande avsteg visar att den gemensamma modellen behöver ändras.

Avsteg blir därmed en feedbackmekanism.

```text
Referensarkitektur
      ↓
Tillämpning
      ↓
Avsteg / friktion / erfarenhet
      ↓
Analys
      ↓
Förbättrad referensarkitektur
```

Detta är samma lärloop som boken tidigare använt för principer, standarder och plattformar.

## Förvaltning är nödvändig för att referensen ska förbli trovärdig

En referensarkitektur som inte förvaltas blir snabbt farligare än ingen referensarkitektur alls. Den ser auktoritativ ut men pekar på gamla produkter, utgångna standarder eller borttagna plattformstjänster.

Varje referensarkitektur behöver därför åtminstone:

- namngiven ägare,
- tydligt scope,
- versions- eller revisionshistorik,
- kända beroenden,
- regelbunden kontroll av refererade standarder och tjänster,
- kanal för feedback från lösningar,
- status, exempelvis aktiv, under revidering eller avvecklad.

Förvaltningen behöver dock inte innebära att hela dokumentet skrivs om när en produktversion ändras. Om artefakten är korrekt separerad från produkt- och versionsstandarder räcker det ofta att dess referenser fortsätter peka på aktuella artefakter.

Det är ytterligare ett skäl att undvika duplicering.

## Referensarkitektur och de tre ansvarsnivåerna

Bokens tredelade ansvarmodell gäller även här.

### Gemensam nivå

Den gemensamma nivån bör definiera:

- vad organisationen menar med referensarkitektur,
- gemensam dokumentationsstruktur,
- minsta metadata och statusmodell,
- hur begränsningar och variation points markeras,
- hur relationer till principer, mönster, standarder och plattformar uttrycks,
- vilka lösningsklasser som motiverar gemensamma referensarkitekturer.

### Förmåge-/plattformnivå

Förmåge- och plattformsansvariga bidrar med:

- aktuella mönster,
- plattformstjänster,
- tjänstekontrakt,
- standarder,
- kvalitetsprofiler,
- kända begränsningar och variationer inom sina områden.

De behöver inte ensamma äga en tvärgående referensarkitektur, men deras erbjudanden måste kunna användas i den.

### Lösnings-/produktnivå

Den konkreta lösningen ska:

- välja relevant referensarkitektur,
- verifiera att scope och antaganden passar,
- välja variationer,
- komplettera med lokala behov och begränsningar,
- dokumentera faktiska beslut,
- registrera motiverade avsteg,
- ge återkoppling när referensen inte fungerar.

Referensarkitekturen ersätter alltså inte lokal arkitekturkompetens. Den gör den mer fokuserad.

## Hur vet man om en referensarkitektur är bra?

En referensarkitektur bör bedömas utifrån om den förbättrar faktiska lösningsbeslut.

Några praktiska frågor är:

- Kan ett nytt initiativ snabbare identifiera relevanta arkitekturfrågor?
- Blir återkommande beslut mer konsekventa?
- Är det tydligt vad som är obligatoriskt och vad som får variera?
- Kan lösningen härleda varför en viss struktur rekommenderas?
- Är aktuella plattformar och standarder lätta att hitta?
- Minskar mängden lokalt uppfunna speciallösningar?
- Är avsteg tydliga och lärande?
- Kan referensarkitekturen överleva teknikbyten utan total omskrivning?

Det går också att följa mer kvantitativa signaler:

- antal initiativ som använder referensarkitekturen,
- ledtid till första arkitekturförslag,
- antal återkommande avsteg,
- antal lokala lösningar för redan lösta gemensamma problem,
- andel referenser till inaktuella standarder eller tjänster,
- tid mellan upptäckt förändring och uppdaterad referens.

Adoption i sig är dock inte ett tillräckligt kvalitetsmått. En dålig referensarkitektur kan användas därför att den är obligatorisk.

Den bättre frågan är:

> Gör referensarkitekturen bättre beslut lättare att fatta?

## Vanliga anti-patterns

### Den frusna lösningen

Ett konkret systems arkitektur döps om till referensarkitektur och förväntas passa alla framtida lösningar.

### Produktkatalogen som referensarkitektur

Dokumentet visar endast vilka plattformsprodukter som finns och saknar lösningsklass, concerns och variation points.

### Den universella referensarkitekturen

En enda arkitektur försöker täcka e-tjänster, batch, integration, AI, arbetsplats och handläggning samtidigt. Resultatet blir så generellt att det inte vägleder några verkliga beslut.

### Den normlösa bilden

Diagrammet ser pedagogiskt ut men det går inte att avgöra vad som är begränsning, rekommendation eller exempel.

### Den odokumenterade variationen

Alla lösningar gör undantag på olika sätt eftersom referensarkitekturen bara visar ett happy path.

### Den duplicerade standarden

Referensarkitekturen kopierar standardtexter och produktversioner och blir snabbt inaktuell.

### Referens utan ägare

Artefakten publiceras en gång men saknar ansvarig för återkoppling, revidering och avveckling.

## En praktisk analysordning

När en organisation vill skapa eller revidera en referensarkitektur kan arbetet göras i följande ordning.

### 1. Identifiera lösningsklassen

Vilka återkommande lösningar delar tillräckligt många arkitekturfrågor?

### 2. Avgränsa scope

Vad omfattas och vad omfattas inte?

### 3. Identifiera concerns och kvalitetsdrivare

Vilka frågor återkommer oavsett konkret implementation?

### 4. Välj relevanta viewpoints

Vilka vyer behövs för att besvara dessa concerns?

### 5. Identifiera återanvändbara beslut

Vilka principer, mönster, standarder och plattformserbjudanden är relevanta?

### 6. Separera begränsningar från rekommendationer

Vad måste vara gemensamt och vad är bara ett bra standardval?

### 7. Dokumentera variation points

Var måste lösningsarkitekturen göra ett lokalt val och vilka drivkrafter styr valet?

### 8. Beskriv ansvarssnitt

Vad äger lösningen, plattformen och andra gemensamma förmågor?

### 9. Skapa spårbarhet

Varför finns varje viktig del och vilka andra artefakter är den beroende av?

### 10. Testa mot flera verkliga scenarier

Om referensarkitekturen bara passar det system den skapades från är den ännu inte tillräckligt generell.

### 11. Publicera med ägarskap och feedbackkanal

En referensarkitektur är en förvaltad produkt av arkitekturarbetet, inte en avslutad ritning.

## Referensarkitekturen som brygga

Bokens arkitekturmodell har hittills gått från behov och kvaliteter via förmågor till mönster, plattformar och standarder. Referensarkitekturen är den artefakt som kombinerar flera av dessa perspektiv för en återkommande lösningsklass.

```text
Förmågor
   │
Mönster ──────────┐
   │              │
Plattformar ──────┼─→ Referensarkitektur
   │              │
Standarder ───────┤
   │              │
Kvalitetsprofiler ┘
                  ↓
          Lösningsarkitektur
```

Det gör den till en brygga mellan den gemensamma arkitekturen och det konkreta initiativet.

Men bron fungerar bara om båda sidorna förblir tydliga.

Referensarkitekturen ska inte absorbera lösningsarkitekturen. Den ska inte heller bli ännu en katalog över gemensamma artefakter. Dess uppgift är att visa hur organisationens gemensamma arkitekturerfarenhet kan sättas samman för en viss typ av lösning, var den är normerande och var den lämnar plats för lokala beslut.

I nästa kapitel används denna idé praktiskt. Då följer vi ett konkret initiativ från verksamhetsbehov och kvalitetsprofil genom förmågor, mönster, plattformar, standarder och referensarkitektur till en dokumenterad lösningsarkitektur.

## Källor och vidare läsning

**[K1]** ISO/IEC/IEEE 42010:2022, *Software, systems and enterprise — Architecture description*. https://www.iso.org/standard/74393.html
