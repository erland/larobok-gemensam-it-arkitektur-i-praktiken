# 26. AI-, identitets- och runtime-mönster

AI-lösningar diskuteras ofta som om den stora arkitekturfrågan vore vilken modell man ska välja. I praktiken uppstår många av de svåraste problemen runt modellen: vilket underlag den får använda, vilka handlingar den får utföra, hur osäkra resultat hanteras, vilken identitet en tjänst använder och hur själva workloaden körs, skalas och ersätts.

Det gör AI till ett bra exempel på varför lösningsmönster behöver kombineras över flera förmågor.

I det här kapitlet fördjupar vi fyra mönster från bokens mönsterbibliotek:

- *Retrieval-Augmented Generation (RAG)*,
- *AI med mänsklig kontroll*,
- tjänsteidentitet,
- *containeriserad stateless tjänst*.

Mönstren löser inte samma problem. RAG minskar kunskapsrisken genom att grunda generering i explicit informationsunderlag. Mänsklig kontroll begränsar konsekvensen av osäkra eller betydelsefulla AI-resultat. Tjänsteidentitet gör teknisk tillit och privilegier explicita. En containeriserad stateless tjänst gör exekveringen reproducerbar, skalbar och utbytbar utan att persistent verksamhetsstate binds till instansen.

Det är först när dessa ansvar hålls isär som de kan kombineras på ett robust sätt.

## Fyra risktyper – fyra olika mönster

En typisk AI-tjänst kan beskrivas ungefär så här:

```text
Användare
   ↓
Applikation
   ↓
AI-tjänst
   ├─ hämtar relevant information
   ├─ anropar modell
   ├─ presenterar resultat
   └─ kan eventuellt initiera en åtgärd
```

Bakom den enkla bilden finns flera frågor:

- Hur vet vi vilket underlag modellen använde?
- Hur säkerställer vi att användaren får se just det underlaget?
- När får ett AI-resultat leda direkt till en åtgärd?
- Vilken teknisk identitet använder AI-tjänsten mot sökindex, API:er eller andra tjänster?
- Vilka privilegier ska den identiteten ha?
- Vad händer när en instans kraschar mitt i ett anrop?
- Hur skalar vi tjänsten utan att sessions- eller verksamhetsstate fastnar lokalt?

Det är olika problem. Ett mönster som förbättrar ett område löser inte automatiskt de andra.

En användbar tumregel är därför:

> Separera kunskapsrisk, beslutskonsekvens, tillit och exekvering innan tekniken väljs.

Det minskar risken att en AI-plattform får ett otydligt helhetsansvar som egentligen borde vara fördelat mellan information, identitet, process, beslut och runtime.

## RAG – när modellen behöver ett explicit kunskapsunderlag

Retrieval-Augmented Generation används när en generativ modell behöver svara med stöd av information som hämtas från externa källor vid frågetillfället.

En förenklad struktur är:

```text
Fråga
  ↓
Retrieval
  ↓
Relevant källmaterial
  ↓
Språkmodell
  ↓
Svar + källreferenser
```

Det centrala är inte att systemet använder embeddings eller en vektordatabas. Det arkitektoniska mönstret är kombinationen av informationssökning och generering.

Modellen behöver alltså inte bära hela kunskapen i sina parametrar. Den får i stället ett explicit underlag som en del av kontexten.

Det passar särskilt när:

- informationen förändras oftare än modellens grundträning,
- verksamheten behöver använda organisationsspecifika källor,
- svar bör kunna spåras till underlag,
- informationsmängden är för stor för en statisk prompt,
- olika användare har rätt till olika informationsmängder.

### RAG skapar inte en ny sanningskälla

Ett vanligt tankefel är att betrakta RAG-systemet som den nya kunskapsdatabasen.

Men ett RAG-flöde innehåller normalt flera representationer:

```text
Auktoritativ källa
      ↓
extraktion / bearbetning
      ↓
index / chunks / embeddings
      ↓
retrieval
      ↓
modellkontext
      ↓
genererat svar
```

De nedre lagren är härledda representationer. De kan vara gamla, ofullständiga eller felaktigt segmenterade även om originalkällan är korrekt.

Därför behöver lösningen kunna svara på frågor som:

- Vilken källa är auktoritativ?
- När hämtades eller indexerades innehållet?
- Hur upptäcks ändringar och borttagningar?
- Hur hanteras dokument som inte längre får användas?
- Hur återskapas indexet?
- Hur verifieras att rätt dokument faktiskt hittas?

RAG är alltså lika mycket ett informationslivscykelmönster som ett AI-mönster.

### Retrieval och generering har separata felgränser

Anta att ett genererat svar är felaktigt. Felet kan ha uppstått på flera ställen:

1. relevant information fanns inte i källorna,
2. den fanns i källan men inte i indexet,
3. indexet innehöll informationen men retrieval hittade fel material,
4. rätt material hittades men modellen misstolkade det,
5. modellen formulerade ett svar som gick längre än underlaget,
6. presentationen gav användaren ett överdrivet intryck av säkerhet.

Det innebär att kvalitet inte kan mätas med ett enda mått på slutsvaret.

Ett välkonstruerat RAG-system behöver kunna utvärdera åtminstone:

- retrievalkvalitet – hittar systemet relevant underlag?
- grundning – stöds svaret av det hämtade underlaget?
- svarskvalitet – är svaret användbart för den avsedda uppgiften?
- källspårbarhet – kan användaren eller granskaren kontrollera underlaget?

### Behörighet måste följa med in i retrieval

RAG gör också identitetsfrågan central.

Det räcker inte att användaren är behörig att använda AI-tjänsten. Tjänsten måste säkerställa att retrieval inte hämtar information som användaren saknar rätt att se.

Det kan hanteras på olika sätt, exempelvis genom:

- behörighetsmetadata i indexet,
- filtrering vid retrieval,
- separerade index för olika informationsdomäner,
- åtkomstkontroller mot källsystemet,
- kombinationer av dessa.

Det viktiga är principen:

> AI-lagret får inte göra en informationsmängd mer åtkomlig än den var i källsystemet.

Här möts RAG och tjänsteidentitet. AI-tjänsten behöver ofta en egen teknisk identitet för att nå källor och söktjänster, men den identiteten får inte ge användaren indirekt tillgång till allt som tjänsten tekniskt kan läsa.

## AI med mänsklig kontroll – när konsekvensen kräver ett stopp

Mänsklig kontroll används när ett AI-resultat inte bör få gå direkt från modell till betydelsefull åtgärd.

En enkel struktur är:

```text
AI-resultat
    ↓
underlag + osäkerhet
    ↓
mänsklig granskning
    ↓
beslut eller åtgärd
```

Det är frestande att beskriva detta som att ”en människa tittar på svaret”. Men då blir mönstret för vagt för att ge verkligt skydd.

Mänsklig kontroll behöver ha en definierad funktion.

Granskaren måste exempelvis kunna:

- förstå vad AI:n föreslår,
- se relevant underlag,
- upptäcka rimliga fel,
- avvisa eller ändra förslaget,
- ha tid och kompetens att göra bedömningen,
- förstå vilket ansvar den mänskliga bedömningen innebär.

Om människan i praktiken bara klickar ”Godkänn” på hundratals förslag är det inte säkert att mönstret reducerar risk.

### Kontrollpunkten ska placeras efter konsekvensen

Det är ofta bättre att fråga:

> Vilken konsekvens behöver stoppas innan den blir verklig?

än:

> Var i AI-flödet ska vi lägga en granskningsskärm?

Anta att AI används för att:

- sammanfatta ett dokument,
- prioritera inkommande ärenden,
- föreslå beslut,
- fatta beslut,
- skapa och skicka ett externt meddelande,
- anropa ett API som ändrar verksamhetsdata.

Konsekvensen stiger inte nödvändigtvis linjärt med hur ”avancerad” modellen är. Ett enkelt klassificeringssystem kan få hög konsekvens om dess resultat automatiskt styr vem som får en förmån eller vilken incident som ignoreras.

Mänsklig kontroll bör därför kopplas till åtgärdens betydelse och återställbarhet, inte till en generell regel om att ”AI alltid ska granskas”.

### Mänsklig kontroll är ett processmönster också

När mänsklig granskning är obligatorisk blir den en del av verksamhetsprocessen.

Då behöver lösningen hantera exempelvis:

- arbetsköer,
- ansvarig roll,
- väntetid,
- eskalering,
- vilka underlag som presenterades,
- vilket AI-resultat som fanns,
- om förslaget ändrades,
- vilket slutligt beslut som togs.

Det betyder att mönstret ofta behöver kombineras med Human workflow från kapitel 25.

AI med mänsklig kontroll är alltså inte bara en UI-funktion. Vid betydelsefulla processer kan det vara en beständig och spårbar del av processarkitekturen.

### Feedback är inte samma sak som automatisk träning

En mänsklig rättning kan ge värdefull återkoppling, men den ska inte automatiskt behandlas som ny träningsdata.

En rättning kan bero på:

- modellfel,
- bristfälligt underlag,
- förändrad regel,
- individuellt undantag,
- missförstånd hos granskaren,
- ny information som inte fanns när AI-resultatet skapades.

Feedback behöver därför klassificeras och förvaltas innan den används för att ändra modell, prompt, retrieval eller annan logik.

## Tjänsteidentitet – gör den tekniska aktören explicit

När en applikation anropar en annan tjänst behöver mottagaren kunna svara på frågan:

> Vem eller vad är det som anropar mig?

För system-till-system-kommunikation bör svaret normalt inte vara ”ett delat servicekonto” eller ”utvecklarens personliga konto”.

Mönstret tjänsteidentitet ger i stället varje relevant workload eller tjänst en egen teknisk identitet.

En förenklad struktur är:

```text
Workload A
   │ teknisk identitet A
   ↓
Tjänst / API / datakälla
   ↑
policy: A får utföra X
```

Det möjliggör:

- tydligare spårbarhet,
- minsta privilegium,
- separat livscykel,
- automatiserad credentialrotation,
- återkallelse utan att andra tjänster påverkas.

### Identiteten ska följa ansvar, inte bara driftsättning

Det är möjligt att göra identiteter för grova eller för detaljerade.

En enda identitet för en hel plattform ger enkel administration men mycket stora privilegier. En separat identitet för varje kortlivad process kan ge onödig komplexitet om alla instanser har samma ansvar.

Identitetsgränsen bör i stället följa den säkerhets- och ansvarsgräns som behöver kunna styras och spåras separat.

Exempelvis kan två workloads som körs i samma containerplattform behöva olika identiteter därför att:

- den ena får läsa sekretesskyddad information,
- den andra endast får anropa ett publikt API,
- de förvaltas av olika team,
- deras credentials behöver kunna återkallas oberoende.

### Kortlivade credentials passar dynamiska workloads

Containeriserade och autoskalande workloads gör långlivade, manuellt skapade hemligheter särskilt problematiska.

Om en tjänst skalas från två till femtio instanser bör man helst inte behöva kopiera samma statiska lösenord till varje instans och sedan hålla reda på var det finns.

En modern tjänsteidentitetsmodell strävar därför ofta efter:

- automatiskt utfärdade credentials,
- kort livslängd,
- automatisk förnyelse,
- begränsad målgrupp och scope,
- central policy men distribuerad användning.

Det minskar både den administrativa kostnaden och konsekvensen om en credential exponeras.

### Tjänsteidentitet är inte användarens identitet

Anta att en AI-tjänst anropas av en handläggare och därefter hämtar information från ett dokument-API.

Två identitetsfrågor finns samtidigt:

1. Vilken tjänst gör anropet?
2. För vems räkning gör tjänsten det?

De får inte blandas ihop.

Tjänsteidentiteten kan exempelvis svara ”AI-assistenten”, medan användarkontexten svarar ”handläggare X med behörighet Y”.

Mottagande system kan behöva båda för att fatta rätt beslut.

Detta är särskilt viktigt när AI-lösningar får tillgång till verktyg eller agentliknande funktioner. Tjänsten bör inte kunna använda sin egen breda tekniska behörighet för att kringgå användarens begränsningar.

## Containeriserad stateless tjänst – gör exekveringen utbytbar

Mönstret containeriserad stateless tjänst används när en applikation kan paketeras som en reproducerbar containerartefakt och köras utan att persistent verksamhetsstate binds till den lokala instansen.

En förenklad struktur är:

```text
Request
   ↓
Containerinstans
   ├─ kod + runtime
   ├─ externaliserad konfiguration
   ├─ tjänsteidentitet
   └─ tillfälligt lokalt tillstånd
         ↓
Externa persistenta tjänster
```

Instansen ska kunna:

- startas,
- ersättas,
- skalas ut,
- stoppas,

utan att verksamhetsdata försvinner.

### Stateless betyder inte att systemet saknar tillstånd

Detta är en viktig distinktion.

Nästan alla verksamhetssystem har tillstånd. Det kan finnas i:

- databas,
- dokumentlager,
- meddelandekö,
- workflowmotor,
- cache,
- sessionslager.

Stateless-mönstret betyder att den enskilda exekveringsinstansen inte är den enda ägaren till persistent tillstånd som behövs för att systemet ska fortsätta fungera.

Det gör instansen utbytbar.

### AI-tjänster passar ofta – men inte alltid

Många AI-komponenter lämpar sig väl för detta mönster.

En RAG-baserad frågetjänst kan exempelvis:

1. ta emot en fråga,
2. hämta kontext från ett sökindex,
3. anropa en modell,
4. returnera ett svar.

Om beständiga konversationer, användardata och index ligger i externa tjänster kan själva AI-orchestratorn vara stateless.

Det förenklar skalning och driftsättning.

Men vissa workloads passar sämre, exempelvis:

- långlivade GPU-sessioner med dyr modellinitiering,
- lokal modellstate som är kostsam att återskapa,
- strömmande bearbetning med lokal checkpointstate,
- specialiserade modeller som binds hårt till viss acceleratorhårdvara.

Mönstret ska därför väljas utifrån workloadens egenskaper, inte för att containers är organisationens standardplattform.

### Health checks behöver mäta rätt sak

En container som svarar på en enkel health endpoint kan fortfarande vara oanvändbar om:

- modellen inte går att nå,
- söktjänsten är nere,
- credentials har gått ut,
- nödvändig konfiguration saknas.

Samtidigt kan det vara farligt att göra liveness beroende av alla externa system. En tillfällig störning i en beroendetjänst kan annars få plattformen att starta om friska instanser i onödan.

Det behövs därför en genomtänkt skillnad mellan exempelvis:

- liveness – processen kan fortsätta exekvera,
- readiness – instansen är redo att ta trafik,
- tjänstefunktion – hela beroendekedjan kan leverera den avsedda funktionen.

Den sista hör ofta hemma i monitorering och syntetiska tester snarare än i containerplattformens omstartslogik.

## När de fyra mönstren kombineras

Anta att en organisation bygger ett AI-baserat handläggarstöd som ska kunna svara på frågor om interna styrande dokument och föreslå nästa åtgärd i ett ärende.

En möjlig struktur är:

```text
Handläggare
    ↓
Webbgränssnitt
    ↓ användaridentitet
AI-assistent
    │
    ├─ tjänsteidentitet
    │      ↓
    ├─ retrieval → behörighetsfiltrerat index
    │
    ├─ språkmodell
    │
    └─ förslag
          ↓
   mänsklig kontroll
          ↓
   verksamhetsåtgärd
```

AI-assistenten kan köras som en containeriserad stateless tjänst. Den använder en egen tjänsteidentitet för tekniska anrop. Retrieval begränsas dessutom utifrån användarens behörighet. RAG ger explicit underlag till språkmodellen. Om förslaget kan få betydande konsekvenser krävs mänsklig kontroll innan verksamhetsåtgärden utförs.

Varje mönster svarar på en separat fråga:

| Mönster | Huvudfråga |
|---|---|
| RAG | Vilket underlag ska AI:n använda och hur kan det spåras? |
| AI med mänsklig kontroll | Vilken konsekvens får inte automatiseras utan granskning? |
| Tjänsteidentitet | Vilken teknisk aktör får åtkomst till vad? |
| Containeriserad stateless tjänst | Hur gör vi exekveringsinstansen reproducerbar och utbytbar? |

Det är en viktig arkitekturell egenskap: kombinationen fungerar eftersom mönstren delar upp ansvar, inte därför att de tillsammans bildar en viss produktstack.

## Behörighetskedjan är viktigare än modellens API-nyckel

I AI-lösningar hamnar säkerhetsdiskussionen lätt på hur API-nyckeln till modellen ska lagras.

Det är viktigt, men otillräckligt.

Den verkliga kedjan kan vara:

```text
Användare
  ↓
Frontend
  ↓
AI-tjänst
  ↓
Söktjänst
  ↓
Dokumentkälla
  ↓
Eventuellt verktyg / verksamhets-API
```

För varje steg behöver arkitekturen förstå:

- vem som autentiseras,
- vilken identitet som används,
- vilket mandat som delegeras,
- vilka privilegier som gäller,
- vad som loggas,
- vad som händer när behörigheter ändras.

En agentliknande AI-lösning med bred tjänsteidentitet kan annars bli en privilegieförstärkare. Användaren ställer en fråga, men AI-tjänsten utför anrop med en betydligt bredare teknisk behörighet än användaren själv har.

Det är därför farligt att utgå från:

> Tjänsten är intern, alltså kan den läsa allt den kan behöva.

Bättre är:

> Varje anrop ska ha den minsta behörighet som krävs för den aktuella uppgiften och kunna kopplas till rätt teknisk och, där relevant, mänsklig aktör.

## Stateless exekvering förenklar inte bort konversationsstate

AI-assistenter har ofta samtalshistorik. Det kan låta som ett argument mot stateless tjänster.

Men konversationsstate behöver inte lagras i själva containerinstansen.

En struktur kan vara:

```text
Request + conversation-id
        ↓
Stateless AI-tjänst
        ↓
Konversationslager
```

Tjänsten hämtar relevant historik, utför sin behandling och skriver tillbaka det som behöver bevaras.

Det ger flera fördelar:

- vilken instans som helst kan ta nästa request,
- instanser kan ersättas utan att samtal försvinner,
- retention kan styras centralt,
- åtkomstkontroll kan appliceras på konversationsdata,
- historik kan raderas utan att containerimages påverkas.

Samtidigt uppstår nya frågor:

- Vad behöver egentligen sparas?
- Hur länge?
- Är all historik lämplig att skicka tillbaka till modellen?
- Kan tidigare promptinnehåll påverka senare anrop på oväntade sätt?
- Hur hanteras klassning och personuppgifter?

Stateless runtime löser alltså exekveringsproblemet. Den löser inte informationsförvaltningen.

## Modellåtkomst som ett separat beroende

En AI-tjänst kan använda:

- en intern modellplattform,
- en extern modellerbjudare,
- flera modeller beroende på uppgift,
- en lokalt driftad modell för vissa informationsklasser.

Det är klokt att behandla modellåtkomst som ett explicit beroende med eget kontrakt.

Det innebär exempelvis att dokumentera:

- vilka modeller eller modellklasser som får användas,
- vilken information som får skickas,
- timeout- och återförsöksbeteende,
- kostnadsgränser,
- fallback,
- versions- eller förändringspolicy,
- observerbarhet,
- hur credentials hanteras.

Då blir inte modellleverantörens SDK själva arkitekturen.

## Felgränser behöver designas mellan mönstren

När fyra mönster kombineras får lösningen flera oberoende felkällor.

Anta att:

- retrieval fungerar,
- modellen svarar,
- människan godkänner,
- men verksamhets-API:t misslyckas.

Då måste systemet veta att ett mänskligt godkännande skedde men att åtgärden inte genomfördes.

Eller:

- retrieval returnerar inget relevant underlag,
- modellen kan fortfarande formulera ett flytande svar.

Då behöver lösningen kunna avstå från att svara eller tydligt indikera bristande grundning.

Eller:

- tjänsteidentiteten har förlorat en behörighet,
- containerplattformen ser processen som frisk,
- men AI-tjänsten kan inte längre läsa den informationskälla som krävs.

Då behövs operativ observerbarhet som skiljer teknisk processhälsa från faktisk tjänstefunktion.

Det illustrerar varför mönsterkombinationer måste analyseras genom felgränser, inte bara genom happy-path-diagram.

## Quality gates före autonomi

När en AI-lösning går från rekommendation till automatisk handling förändras arkitekturrisken.

Det kan vara användbart att se autonomi som en progression:

```text
Generera → Visa → Rekommendera → Förbereda → Utföra med godkännande → Utföra autonomt
```

Varje steg ökar konsekvensytan.

Innan ett högre steg tillåts bör lösningen kunna visa att relevanta kvaliteter är tillräckligt väl hanterade, exempelvis:

- utvärderad resultatkvalitet,
- tydligt underlag och spårbarhet,
- korrekt behörighetskedja,
- begränsade privilegier,
- observerbarhet,
- rollback eller kompensation där det är möjligt,
- hantering av modell- och promptförändringar,
- tydliga stoppmekanismer.

Det är inte en universell mognadsmodell. Poängen är att autonomi är ett arkitekturbeslut med ökande konsekvens, inte en funktion som bör slås på enbart därför att tekniken stödjer den.

## Plattformar ska stödja mönstren – inte blanda ihop dem

En organisation kan erbjuda gemensamma plattformstjänster för flera delar av denna arkitektur:

- AI Platform / Model Gateway,
- Search & Retrieval Platform,
- Service Identity,
- Secrets Management,
- Container Application Platform,
- Logging, Monitoring & Tracing.

Det kan ge stor återanvändning.

Men det betyder inte att en enda ”AI-plattform” bör äga:

- informationsbehörighet,
- verksamhetsbeslut,
- processansvar,
- tjänsteidentiteter,
- persistent verksamhetsdata.

Plattformar bör erbjuda mekanismer och väl definierade kontrakt. Mönstren hjälper lösningen att placera ansvar mellan dessa mekanismer.

## Ansvar på tre nivåer

De fyra mönstren visar tydligt varför bokens tredelade ansvarmodell behövs.

### Gemensam arkitekturnivå

Den gemensamma nivån bör bland annat kunna definiera:

- principer för AI-användning och konsekvensbaserad kontroll,
- gemensamma krav på identitet, spårbarhet och informationsskydd,
- tillåtna trust- och delegeringsmodeller,
- gemensamma runtime-profiler,
- övergripande regler för informationsklassning och extern modellåtkomst,
- hur mönster och standarder ska beskrivas och förvaltas.

Den bör däremot normalt inte besluta vilken prompt eller vilken modell varje lösning ska använda.

### Förmågenivå

Förmågeområdena behöver tillsammans förvalta mönstrens konkreta stöd.

Analys, sökning och AI kan exempelvis ansvara för:

- RAG-vägledning,
- utvärderingsramverk,
- modellåtkomst,
- AI-observerbarhet.

Identitet och tillit kan ansvara för:

- tjänsteidentitet,
- credentiallivscykel,
- trustmodeller,
- delegeringsprofiler.

Runtimeförmågan kan ansvara för:

- containerprofiler,
- resursmodeller,
- health-check-konventioner,
- isolering och skalningsmekanismer.

Ingen av förmågorna bör ensam äga hela AI-lösningen.

### Lösnings-/produktnivå

Den konkreta lösningen behöver besluta:

- om RAG faktiskt behövs,
- vilka källor som är tillåtna,
- hur retrieval filtreras per användare,
- var mänsklig kontroll behövs,
- vilken handling som får automatiseras,
- vilken tjänsteidentitet varje workload använder,
- vilka scopes och privilegier som krävs,
- om stateless exekvering passar workloaden,
- hur persistent konversations- och verksamhetsstate hanteras,
- hur fel mellan retrieval, modell, identitet och downstream-system hanteras.

Det är lösningen som bär konsekvensen av kombinationen.

## Vanliga anti-patterns

### RAG som universell sanningsmotor

Ett sökindex och en språkmodell behandlas som om de tillsammans skapar en auktoritativ kunskapskälla. Originalkällor, aktualitet och livscykel blir otydliga.

### Human-in-the-loop som dekor

En människa måste klicka ”godkänn”, men har varken tid, underlag eller realistisk möjlighet att upptäcka fel.

### AI-tjänsten får en superidentitet

AI-komponenten ges bred åtkomst till många system ”för flexibilitetens skull” och kan därmed agera med större privilegier än användaren.

### Delade servicekonton

Flera workloads använder samma tekniska identitet, vilket gör spårbarhet, återkallelse och minsta privilegium svårare.

### Container = stateless

En applikation körs i container men lagrar ändå nödvändigt persistent tillstånd på lokal disk och blir därmed inte utbytbar.

### Modell-SDK som arkitekturgräns

Lösningen binds direkt till en leverantörs SDK utan separat kontrakt för modellåtkomst, vilket gör observerbarhet, fallback och förändringskontroll svårare.

### All konversationshistorik skickas alltid tillbaka

Hela historiken sparas och skickas till modellen utan tydligt behov, retention, klassning eller analys av informationsläckage.

### Autonomi utan ny riskbedömning

En funktion som tidigare gav rekommendationer får börja utföra åtgärder automatiskt utan att behörigheter, rollback, observerbarhet och kvalitetskrav omprövas.

## En praktisk analysordning

När AI, identitet och runtime möts kan följande ordning vara användbar.

### 1. Definiera uppgiften och konsekvensen

Vad ska AI-komponenten faktiskt göra, och vad händer om resultatet är fel?

### 2. Identifiera auktoritativa informationskällor

Vilket underlag får användas, vem äger det och hur aktuellt måste det vara?

### 3. Avgör om retrieval behövs

Behöver modellen dynamiskt och spårbart underlag, eller räcker en enklare lösning?

### 4. Definiera mänskliga kontrollpunkter

Vilken konsekvens behöver stoppas före genomförande, och kan en människa realistiskt göra kontrollen?

### 5. Kartlägg identitetskedjan

Vilka användare, workloads och tjänster agerar, och för vems räkning?

### 6. Minimera privilegier

Vilken åtkomst behöver varje tjänsteidentitet för just sin uppgift?

### 7. Beskriv workloadens runtimeegenskaper

Kan tjänsten vara stateless? Vilket tillstånd måste ligga externt? Vilka resurs- och skalningskrav finns?

### 8. Definiera felgränser

Vad händer när retrieval, modell, credentialutfärdare eller downstream-API misslyckas var för sig?

### 9. Definiera observerbarhet och spårbarhet

Kan en operation kopplas från användare och tjänsteidentitet via hämtat underlag och modellresultat till slutlig åtgärd?

### 10. Öka autonomi först efter verifierad kvalitet

Automatisera mer först när kvalitetsmått, privilegier, felhantering och återställning stödjer den ökade konsekvensen.

## Det viktigaste att bära med sig

AI-, identitets- och runtime-mönster blir särskilt värdefulla när de hjälper oss att begränsa olika typer av risk var för sig.

RAG gör kunskapsunderlaget explicit och uppdateringsbart, men skapar inte en ny sanningskälla. AI med mänsklig kontroll kan begränsa konsekvensen av osäker inferens, men bara om kontrollen är verklig och placerad före den betydelsefulla åtgärden. Tjänsteidentitet gör tekniska aktörer, privilegier och livscykler explicita. En containeriserad stateless tjänst gör exekveringsinstanser reproducerbara och utbytbara utan att persistent verksamhetsstate binds till dem.

Kombinationen kan sammanfattas med fyra frågor:

1. Vilket underlag får AI:n använda?
2. Vilken konsekvens får AI:n orsaka utan mänsklig kontroll?
3. Vilken identitet och vilka privilegier används för varje anrop?
4. Vilket tillstånd måste överleva den enskilda exekveringsinstansen?

När svaren är tydliga kan AI-lösningen förändras – modell, index, runtime och tjänster kan bytas – utan att ansvar och tillit behöver uppfinnas på nytt varje gång.

I nästa kapitel flyttar vi fokus från AI och runtime till den operativa livscykeln. Då fördjupar vi mönstren build once, promote many, observerbarhet för distribuerade tjänster och backup med verifierad återställning – tre mönster som gör leverans och drift till en del av arkitekturen redan innan produktionssättning.
