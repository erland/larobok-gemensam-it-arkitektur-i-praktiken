# 34. Vad en referensarkitektur är – och inte är

När en organisation har definierat gemensamma förmågor, lösningsmönster, plattformstjänster och standarder uppstår en naturlig fråga: hur ska allt detta sättas samman när en viss typ av lösning återkommer gång på gång?

Det är här referensarkitekturen får sin roll.

En referensarkitektur ska göra mer än att lista vilka tekniker som är godkända. Den ska samtidigt göra mindre än att designa ett konkret system. Dess värde ligger i mellanrummet: den återanvänder arkitekturerfarenhet för en klass av lösningar och ger ett gemensamt utgångsläge utan att låsa varje implementation till samma detaljdesign.

I den här boken används därför följande arbetsdefinition:

> En referensarkitektur är en förvaltad, återanvändbar arkitekturbeskrivning för en avgränsad klass av lösningar. Den beskriver relevanta concerns, strukturer, ansvar, obligatoriska begränsningar, rekommenderade mönster, gemensamma tjänster och explicita variation points, så att en konkret lösningsarkitektur kan härledas snabbare och mer konsekvent.

Begreppet *referensarkitektur* används på olika sätt i olika organisationer och ramverk. Det viktiga är därför inte att hitta en enda universell definition, utan att vara tydlig med vilket problem artefakten ska lösa, vilken abstraktionsnivå den har och hur den relaterar till andra arkitekturartefakter.

Detta kapitel etablerar den rollen. Nästa kapitel visar hur ett konkret initiativ går från behov till faktisk lösningsarkitektur med referensarkitekturen som ett av flera beslutsunderlag.

## Varför behövs en referensarkitektur?

Anta att en organisation under några år bygger flera publika e-tjänster. De skiljer sig åt i verksamhetslogik, användargrupper och data, men återkommer till samma frågor:

- hur användaren autentiseras,
- hur frontend och backend separeras,
- hur API:er exponeras,
- hur verksamhetsdata och dokument hanteras,
- hur integrationer sker,
- hur loggning och tracing byggs in,
- hur tjänsten levereras och körs,
- hur återställning hanteras,
- vilka standarder och gemensamma plattformar som ska användas.

Om varje initiativ börjar från noll fattas samma typer av beslut om och om igen. Resultatet blir inte bara högre kostnad, utan också variation som senare måste förvaltas.

Motsatsen är inte att skapa en enda obligatorisk lösningsdesign för alla e-tjänster. Det skulle göra arkitekturen oförmögen att hantera verkliga skillnader. Referensarkitekturen försöker i stället fånga det som rimligen bör återanvändas.

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

## En arkitektur för en klass av lösningar

Den viktigaste gränsdragningen är att en referensarkitektur inte beskriver *ett specifikt system*. Den beskriver en lösningsklass där tillräckligt många arkitekturfrågor återkommer för att gemensam vägledning ska ge värde, exempelvis:

- publik e-tjänst,
- internt handläggningsstöd,
- integrationsintensivt verksamhetssystem,
- informationsutbyte med extern part,
- *containerbaserad tjänst*,
- *AI-baserat verksamhetsstöd*,
- digital arbetsplats.

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

Men den behöver normalt inte bestämma exakt antal tjänster, domänindelning, tabellstruktur, URL-struktur, antal repliker, produktversion eller vilka verksamhetsregler den konkreta tjänsten innehåller. Sådana beslut hör hemma i lösningsarkitekturen och implementationen.

Referensarkitekturen måste alltså ligga på en nivå där den är tillräckligt konkret för att styra återkommande beslut men tillräckligt generell för att återanvändas.

## Skillnaden mot lösningsarkitektur

Det vanligaste missförståndet är att referensarkitekturen ses som en färdig lösningsarkitektur som bara ska kopieras.

| Referensarkitektur | Lösningsarkitektur |
|---|---|
| Gäller en klass av lösningar | Gäller ett konkret initiativ eller system |
| Återanvändbar | Situationsspecifik |
| Beskriver typiska strukturer och ansvar | Beskriver faktisk struktur och faktiska beslut |
| Har explicita variation points | Väljer en konkret variant |
| Pekar på gemensamma mönster och tjänster | Väljer vilka som faktiskt används |
| Beskriver begränsningar för lösningsklassen | Hanterar även lokala begränsningar |
| Förvaltas över flera initiativ | Förvaltas med den konkreta lösningen |

Sambandet är alltså inte:

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

Ett avsteg från referensarkitekturen är därför inte automatiskt fel. Det kan vara helt korrekt om den konkreta lösningen har andra kvalitetsdrivare eller begränsningar. Det viktiga är att skillnaden blir synlig och motiverad.

## Gränsen mot andra återanvändbara artefakter

Referensarkitekturen arbetar tillsammans med lösningsmönster, standarder, plattformar och templates, men ersätter ingen av dem.

| Artefakt | Primär fråga | Relation till referensarkitekturen |
|---|---|---|
| Lösningsmönster | Hur kan ett återkommande designproblem struktureras? | Referensarkitekturen kombinerar relevanta mönster för en lösningsklass. |
| Standard | Vad ska göras konsekvent? | Referensarkitekturen hänvisar till tillämpliga standarder och begränsningar. |
| Plattformstjänst | Vad kan lösningen konsumera gemensamt? | Referensarkitekturen visar hur erbjudanden kan sättas samman i lösningsklassen. |
| Golden path / paved road | Hur gör vi den rekommenderade vägen enkel att följa? | Operationaliserar delar av referensarkitekturen. |
| Template / starter kit | Vilken konkret startpunkt kan återanvändas? | Realiserar utvalda delar i kod, konfiguration eller automation. |

Ett lösningsmönster har smalare scope. En referensarkitektur för AI-baserat verksamhetsstöd kan till exempel kombinera RAG, AI med mänsklig kontroll, tjänsteidentitet, stateless runtime och observerbarhet. Referensarkitekturen bör då referera till mönstren snarare än att kopiera deras fullständiga beskrivningar.

På samma sätt bör standarder hållas separata. Om referensarkitekturen kopierar hela API-, identitets- eller containerstandarden uppstår dubbla källor och livscykelproblem. Bättre är exempelvis:

> Externa API:er ska följa organisationens aktuella API-standard.

Plattformen är inte heller referensarkitekturen. En bild som bara visar ingress, containerplattform och databastjänst kan vara en värdefull plattformsbild, men säger inte nödvändigtvis något om lösningsklassens concerns, kvalitetsbehov eller variationer.

Slutligen är templates mer konkreta och mer teknikberoende än referensarkitekturen:

```text
Referensarkitektur
       ↓
Golden path / paved road
       ↓
Templates och automation
       ↓
Konkret lösning
```

Det gör att referensarkitekturen kan överleva när ett repository byter byggverktyg eller en plattform byter produktversion. Samtidigt bör den påverka faktiska golden paths, templates och lösningsbeslut; annars riskerar den att bli presentationsmaterial utan praktisk effekt.

## Referensarkitekturens anatomi

En användbar referensarkitektur består av mer än ett diagram. Den behöver beskriva både vad lösningsklassen omfattar och vilka beslut som ska återanvändas.

### Scope och concerns

Scope är det första beslutet. Det behöver vara tydligt:

- vilken lösningsklass arkitekturen gäller,
- vilka typer av behov som omfattas,
- vilka närliggande områden som inte omfattas,
- vilka kvalitetsprofiler den är avsedd för,
- vilka organisatoriska eller regulatoriska förutsättningar som antas.

Ett för brett scope ger en generisk bild som säger nästan ingenting. Ett för smalt scope gör artefakten så situationsspecifik att den lika gärna kunde vara en lösningsarkitektur.

Ett praktiskt test är:

> Finns det flera verkliga eller sannolika lösningar som kan använda samma arkitekturvägledning utan att deras viktigaste skillnader försvinner?

Referensarkitekturen behöver därefter identifiera de concerns som återkommer i lösningsklassen. För en publik e-tjänst kan det handla om identitet, informationsflöden, integration, driftsättning, observerbarhet, kontinuitet och ansvar.

### Viewpoints och vyer

En enda komponentbild kan sällan bära alla dessa frågor. ISO/IEC/IEEE 42010 skiljer mellan arkitekturen och den beskrivning som uttrycker den[K1], och använder bland annat *viewpoints* och *views* för att strukturera arkitekturbeskrivningar. Boken behöver inte göra varje referensarkitektur formellt konform med standarden för att använda samma grundidé: olika concerns behöver ofta olika vyer.

Relevanta viewpoints kan exempelvis vara:

- logisk struktur,
- informations- och integrationsflöden,
- identitet och tillit,
- driftsättning/runtime,
- observerbarhet och drift,
- kontinuitet,
- ansvar och ägarskap.

Det viktiga är inte att maximera antalet diagram. Varje vy ska besvara en tydlig fråga.

### Variation points och begränsningar

En stark referensarkitektur beskriver explicit var variation är förväntad och vilka drivkrafter som avgör valet.

För en publik e-tjänst kan autentisering variera mellan anonym åtkomst, privatperson, organisation, medarbetare och federerad extern identitet. Integrationsformen kan vara synkront API, asynkront meddelande, event eller filbaserat utbyte. Runtime kan variera mellan stateless container workload, stateful komponent eller en lösning med särskilda legacy- eller hårdvarubegränsningar.

Att dokumentera sådana variation points är inte ett tecken på ofullständighet. Det visar var lösningsarkitekturen fortfarande måste fatta ett lokalt beslut.

Samtidigt ska inte allt vara valbart. En lösningsklass kan ha begränsningar, exempelvis att externa API:er går genom gemensam API-hantering, att tjänsteidentiteter används mellan workloads eller att produktion måste leverera definierad telemetri. Men begränsningarna bör vara få, tydliga och motiverade av exempelvis säkerhet, interoperabilitet, regelefterlevnad eller operativ förmåga.

Principen är enkel: obligatoriskt där konsekvensen kräver det; varierbart där lokala behov skiljer sig.

### Kvalitetsprofil

Två lösningar kan tillhöra samma lösningsklass men ha olika kvalitetsbehov. Ett internt handläggningsstöd kan ha normal tillgänglighetsprofil, medan ett operativt kritiskt stöd kräver kortare RTO, högre tillgänglighet och andra redundansmönster.

Referensarkitekturen bör därför antingen ange vilken kvalitetsprofil den är avsedd för eller beskriva hur arkitekturen varierar mellan definierade profiler.

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

Därmed kopplas referensarkitekturen tillbaka till bokens kvalitetsmodell i stället för att reduceras till en komponentbild.

### Ansvar och spårbarhet

Referensarkitekturen behöver visa ansvar i de gränser där lösningar annars lätt gör olika antaganden: verksamhetslogik, processläge, auktoritativ data, identitet, integration, dokument, observerbarhet och plattformsdrift.

För en containerbaserad tjänst kan lösningsteamet exempelvis ansvara för korrekt health behavior, resursdeklarationer, applikationsloggning, data- och transaktionsdesign samt säker användning av credentials. Plattformsteamet ansvarar samtidigt för exekveringsmiljö, plattformens tillgänglighet, gemensamma policyer, plattformstelemetri och supportfönster.

Detta är en tillämpning av bokens tre ansvarsnivåer, inte en ny ansvarmodell. Den generella governance- och förvaltningsmodellen behandlas i det avslutande governancekapitlet.

Viktiga delar bör också kunna härledas till behov, kvalitetsattribut, mönster, standard eller gemensamt erbjudande:

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

Spårbarheten gör både besluten begripliga och förändringspåverkan lättare att analysera.

En praktisk referensarkitektur kan därför innehålla syfte och scope, antaganden, kvalitetsprofiler, relevanta vyer, ansvarsgränser, begränsningar, variation points, rekommenderade mönster, plattformstjänster, standardreferenser, kända avvägningar och exempel på tillämpning. Ägare, status och ändringshistorik behöver också finnas, men den mer generella förvaltningsmekaniken hör hemma i bokens avslutande governancekapitel.

## Normativitet och avsteg

Referensarkitekturen bör vara normativ på rätt ställen. Om allt är normativt blir den stel; om inget är normativt blir det oklart om den faktiskt påverkar några beslut.

| Typ | Betydelse |
|---|---|
| Begränsning | Ska följas om inte godkänt avsteg finns |
| Rekommenderad struktur | Bör vara förstahandsval när angivna förutsättningar gäller |
| Variation point | Lokalt beslut krävs enligt angivna drivkrafter |
| Exempel | Illustrerar möjlig realisering men är inte normerande |
| Referens | Pekar på separat standard, mönster eller tjänstekontrakt |

Avsteg är därför en normal del av användningen. När ett konkret initiativ inte kan följa referensarkitekturen bör frågan vara vilken skillnad i behov, kvalitet eller begränsning som gör att den inte passar.

Det kan leda till tre utfall:

1. **Lokalt motiverat avsteg** – referensarkitekturen är fortfarande rätt för sin målklass.
2. **Ny variation point** – flera lösningar visar att ett legitimt alternativ behöver beskrivas.
3. **Förändrad referensarkitektur** – återkommande avsteg visar att den gemensamma modellen är fel eller föråldrad.

Det räcker här att konstatera att referensarkitekturen behöver ägare, status, revisionshistorik och en avstegsmekanism. Hur denna feedback blir en fungerande governance- och förvaltningsloop behandlas i bokens avslutning.

## Kvalitetskriterier och anti-patterns

En referensarkitektur är bra om den förbättrar faktiska lösningsbeslut. Några praktiska kontrollfrågor är:

- Kan ett nytt initiativ snabbare identifiera relevanta arkitekturfrågor?
- Blir återkommande beslut mer konsekventa?
- Är det tydligt vad som är obligatoriskt och vad som får variera?
- Kan lösningen härleda varför en viss struktur rekommenderas?
- Är aktuella plattformar och standarder lätta att hitta?
- Minskar mängden lokalt uppfunna speciallösningar?
- Är avsteg tydliga och lärande?
- Kan referensarkitekturen överleva teknikbyten utan total omskrivning?

Det går även att följa signaler som användning, ledtid till första arkitekturförslag, återkommande avsteg och inaktuella referenser. Adoption i sig är dock inte ett tillräckligt kvalitetsmått. En dålig referensarkitektur kan användas bara därför att den är obligatorisk.

Den bättre frågan är:

> Gör referensarkitekturen bättre beslut lättare att fatta?

Vanliga anti-patterns är:

- **Den frusna lösningen:** ett konkret systems arkitektur döps om till referensarkitektur och förväntas passa allt.
- **Produktkatalogen som referensarkitektur:** dokumentet visar bara plattformsprodukter och saknar lösningsklass, concerns och variation points.
- **Den universella referensarkitekturen:** en enda modell försöker täcka e-tjänster, batch, integration, AI, arbetsplats och handläggning och blir därför för generell.
- **Den normlösa bilden:** diagrammet är pedagogiskt men det går inte att avgöra vad som är krav, rekommendation eller exempel.
- **Den odokumenterade variationen:** varje lösning gör undantag på olika sätt eftersom bara ett happy path visas.
- **Den duplicerade standarden:** standardtexter och produktversioner kopieras in och blir snabbt inaktuella.
- **Referens utan ägare:** artefakten publiceras en gång men saknar ansvar för revidering och avveckling.

## Checklista för att skapa eller granska en referensarkitektur

För att undvika att denna aktivitet blandas ihop med nästa kapitels process från behov till lösningsarkitektur kan arbetet sammanfattas i sex referensarkitekturspecifika frågor:

1. **Lösningsklass och scope:** finns flera verkliga lösningar som delar tillräckligt många arkitekturfrågor, och är gränsen mot närliggande lösningsklasser tydlig?
2. **Concerns och kvalitetsprofiler:** vilka återkommande frågor och kvalitetsdrivare måste artefakten hjälpa lösningar att hantera?
3. **Återanvändbara beslut:** vilka mönster, plattformstjänster och standarder ska refereras, och vilka vyer behövs för att förklara hur de hänger ihop?
4. **Normativitet och variation:** vad är begränsning, rekommendation respektive variation point, och framgår drivkrafterna för lokala val?
5. **Ansvar och spårbarhet:** är det tydligt vem som äger vad och varför viktiga arkitekturelement finns?
6. **Praktisk användbarhet:** fungerar referensarkitekturen för flera realistiska scenarier, kan den förvaltas utan duplicering och finns ägare samt mekanism för feedback och avsteg?

Om en referensarkitektur bara passar systemet den skapades från är den för specifik. Om den kan passa nästan vilket system som helst utan att påverka några beslut är den för generell.

## Referensarkitekturen som brygga

Bokens arkitekturmodell har hittills gått från behov och kvaliteter via förmågor till mönster, plattformar och standarder. Referensarkitekturen kombinerar flera av dessa perspektiv för en återkommande lösningsklass.

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

Det gör den till en brygga mellan den gemensamma arkitekturen och det konkreta initiativet. Men bron fungerar bara om båda sidorna förblir tydliga.

Referensarkitekturen ska inte absorbera lösningsarkitekturen. Den ska inte heller bli ännu en katalog över gemensamma artefakter. Dess uppgift är att visa hur organisationens gemensamma arkitekturerfarenhet kan sättas samman för en viss typ av lösning, var den är normerande och var den lämnar plats för lokala beslut.

I nästa kapitel följer vi därför ett konkret initiativ från verksamhetsbehov och kvalitetsprofil genom förmågor, mönster, plattformar, standarder och referensarkitektur till en dokumenterad lösningsarkitektur. Där blir referensarkitekturen ett beslutsunderlag i processen, inte processen i sig.

## Källor och vidare läsning

**[K1]** ISO/IEC/IEEE 42010:2022, *Software, systems and enterprise — Architecture description*. https://www.iso.org/standard/74393.html
