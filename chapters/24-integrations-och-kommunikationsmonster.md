# 24. Integrations- och kommunikationsmönster

Integration är sällan svårt därför att två system inte kan utbyta bytes. Det svåra är att låta två självständiga delar samarbeta utan att deras livscykler, fel, belastning och interna modeller växer ihop mer än nödvändigt. Därför är integrationsmönster i första hand mönster för beroenden. De hjälper oss att bestämma vem som känner till vem, när parterna måste vara tillgängliga samtidigt, vilket ansvar som ligger i kontraktet och vad som händer när något går fel.

Kapitel 17 beskrev integrations- och kommunikationsförmågan och valen mellan exempelvis API, messaging, events, filutbyte och dataförflyttning. Här ligger fokus på en annan nivå. Vi ska se hur återkommande lösningsstrukturer kan användas för att hantera dessa behov. Mönstren är inte konkurrerande tekniker som man väljer en gång för hela organisationen. De är svar på olika krafter och kombineras ofta i samma lösning.

Fokus ligger därför på mönstrens struktur, krafter, konsekvenser och kombinationer, inte på att återupprepa kommunikationsformerna från kapitel 17.

Tre mönster står i centrum:

- *Backend for Frontend*,
- *asynkron meddelandekommunikation*,
- *publicera/prenumerera*.

Runt dem behöver vi dessutom förstå sådant som idempotens, ordering, återförsök, dead-letter-hantering, korrelation och kontraktsutveckling. Dessa är inte alltid egna lösningsmönster, men de är återkommande designmekanismer som avgör om mönstren fungerar robust i praktiken.

## Börja med den koppling du är beredd att acceptera

Ett integrationsval skapar alltid någon form av koppling. Målet är därför inte ”ingen koppling”, utan medveten och kontrollerad koppling.

Parter kan bland annat kopplas genom:

- tid – måste båda vara tillgängliga samtidigt?
- identitet – måste producenten känna till en viss konsument?
- kontrakt – hur starkt är parterna bundna till samma format och semantik?
- sekvens – måste saker inträffa i en viss ordning?
- tillgänglighet – sprids ett fel i den ena parten direkt till den andra?
- kapacitet – måste båda kunna hantera samma belastningstopp samtidigt?
- förändring – behöver en ändring hos den ena samordnas med den andra?

Detta ger en bättre utgångspunkt än frågor som ”ska vi använda REST eller Kafka?”. Tekniken kan realisera ett valt mönster, men den avgör inte vilket beroende verksamheten faktiskt behöver.

En synkron begäran kan vara rätt när den som anropar inte kan fortsätta utan ett omedelbart svar. Asynkron messaging kan vara rätt när arbete får utföras senare och tillgänglighetstoppar behöver absorberas. Publicera/prenumerera kan vara rätt när producenten ska uttrycka ett faktum utan att styra vilka andra delar som reagerar på det.

Mönstret bör alltså väljas efter önskad relation mellan parterna, inte efter vilken plattform organisationen råkar ha.

## Backend for Frontend – ett kanalnära ansvarslager

Backend for Frontend, ofta förkortat BFF, används när en klient eller kanal har behov som inte bör läggas vare sig i klienten eller i generiska domäntjänster.

Grundstrukturen är enkel:

```text
Klient
  ↓
Backend for Frontend
  ↓
Domän- och plattformstjänster
```

BFF-lagret kan exempelvis:

- aggregera data från flera backend-tjänster,
- anpassa dataformat för en viss klienttyp,
- minska antalet nätverksanrop från klienten,
- hantera klientnära sessions- eller autentiseringsflöden,
- isolera klienten från interna tjänstegränser,
- ge webb, mobil och andra kanaler olika kontrakt när deras behov faktiskt skiljer sig.

Mönstrets kärna är inte att varje frontend ska få en egen backendkomponent. Kärnan är att kanalspecifika behov får ett tydligt hem när ett generiskt backendgränssnitt annars skulle bli för brett eller klienten skulle behöva förstå för mycket av backendlandskapet.

### Krafter som BFF balanserar

Ett gemensamt API kan verka attraktivt eftersom det minskar antalet komponenter. Men om flera klienttyper har olika interaktionsmönster kan samma API behöva bära många specialfall. Alternativt tvingas varje klient göra egen aggregering och orkestrering.

BFF flyttar en del av denna komplexitet till ett separat serversidelager. Vinsten är större kanalautonomi och mindre kunskap om interna tjänster i klienten. Kostnaden är ytterligare en komponent att utveckla, testa, drifta och versionera.

Mönstret passar därför sämre om lagret enbart vidarebefordrar varje anrop utan egen kanalrelevant funktion. Ett sådant BFF blir lätt ett extra nätverkshopp utan arkitektoniskt värde.

### BFF får inte bli en ny monolit

Ett vanligt misslyckande är att lägga all ”bekväm” logik i BFF-lagret. Då kan lagret successivt börja innehålla:

- verksamhetsregler,
- gemensam domänlogik,
- integrationslogik som egentligen tillhör backend,
- datalagring som blir auktoritativ,
- orkestrering som flera kanaler är beroende av.

Då har kanalgränsen blivit en oavsiktlig domängräns.

En användbar tumregel är att fråga om logiken finns därför att just denna klient eller kanal behöver den. Om samma regel måste gälla oavsett kanal hör den normalt hemma längre in i lösningen.

### Ett BFF per behov – inte per organisationsruta

Mönstrets namn kan locka till mekanisk tillämpning: ett BFF per frontend. Det är sällan en bra regel. Två klienter med i princip samma behov kan dela ett kontrakt. En enda komplex klient kan tvärtom ha skäl att separera olika ansvarsytor.

Det viktiga är inte antalet BFF-komponenter utan att gränsen följer verkliga variationsbehov.

## Asynkron meddelandekommunikation – bryt tidskopplingen

Asynkron meddelandekommunikation används när producenten kan lämna över ett arbete eller meddelande utan att mottagaren måste utföra det inom samma anropskedja.

En förenklad struktur är:

```text
Producent
   ↓
Meddelandetjänst
   ↓
Konsument
```

Meddelandetjänsten kan buffra när konsumenten är långsammare eller tillfälligt otillgänglig. Producent och konsument kan därmed skalas och återstartas mer oberoende än vid ett direkt synkront anrop.

Detta innebär dock inte att beroendet försvinner. Tidskopplingen minskar, men parterna delar fortfarande ett kontrakt och en förväntan om vad meddelandet betyder.

### När mönstret passar

Asynkron kommunikation är särskilt användbar när:

- mottagaren inte behöver ge ett omedelbart verksamhetssvar,
- arbetet kan köas,
- belastning behöver jämnas ut,
- tillfällig otillgänglighet inte ska slå tillbaka direkt på producenten,
- arbetet kan återförsökas senare,
- producent och konsument behöver skalas oberoende.

Det passar sämre när användarens nästa steg verkligen kräver ett svar här och nu. Att göra en naturligt synkron interaktion asynkron flyttar då ofta bara komplexiteten till statuspollning, callbacks eller långlivad processhantering.

### Asynkront betyder inte automatiskt robust

En kö gör inte en lösning robust av sig själv. Tvärtom introducerar mönstret nya frågor:

- Kan samma meddelande levereras mer än en gång?
- Vad händer efter fem misslyckade försök?
- Kan meddelanden behandlas i annan ordning än de skapades?
- Hur upptäcks meddelanden som fastnar?
- Hur kopplar man ihop ett senare resultat med det ursprungliga sammanhanget?
- Hur länge får ett meddelande ligga kvar innan det saknar verksamhetsvärde?

Därför hör leveransbeteende och felhantering till mönstret, inte till en senare driftfråga.

## Leveranssemantik och felhantering

Asynkrona mönster minskar tidskoppling men gör leveransbeteendet till en del av arkitekturen. Robustheten avgörs därför inte av att en kö eller broker finns, utan av hur lösningen hanterar dubbletter, tillfälliga och permanenta fel, ordning, upprepade försök och fel som inte kan lösas automatiskt.

**Idempotens – designa för att samma sak kan hända igen.**

I distribuerade system är det ofta svårt att veta om ett försök misslyckades före eller efter att mottagaren hann genomföra operationen. Ett timeoutfel kan exempelvis betyda att mottagaren aldrig fick meddelandet, men också att operationen lyckades och bara svaret försvann.

Det gör idempotens central för många integrationsmönster.

En operation är idempotent i praktisk integrationsmening när samma logiska begäran kan behandlas igen utan att den avsedda verksamhetseffekten upprepas felaktigt.

Om kommandot ”Registrera betalning” levereras två gånger ska det exempelvis inte automatiskt skapa två betalningar. Lösningen kan behöva ett stabilt meddelande- eller operations-id och en mekanism som känner igen redan behandlade operationer.

Idempotens är inte detsamma som att ignorera alla dubbletter. I vissa domäner kan två till synes identiska händelser vara två verkliga verksamhetshändelser. Det är därför den logiska identiteten för operationen som behöver modelleras, inte bara dess payload.

**Återförsök – bara när felet kan lyckas senare.**

Återförsök är en mekanism, inte en universell felhantering.

Ett återförsök är meningsfullt när felet sannolikt är tillfälligt, exempelvis:

- ett kort nätverksavbrott,
- tillfällig överbelastning,
- en beroendetjänst som håller på att starta om.

Återförsök hjälper inte när felet är permanent:

- kontraktet är ogiltigt,
- obligatoriska data saknas,
- operationen bryter mot en verksamhetsregel,
- mottagaren stöder inte meddelandeversionen.

Oreflekterade återförsök kan tvärtom förstärka en incident. Om hundratals konsumenter omedelbart försöker igen mot en överbelastad tjänst ökar belastningen precis när kapaciteten är som lägst.

Robust återförsök behöver därför normalt ta ställning till:

- vilka fel som är återförsökningsbara,
- hur många försök som får göras,
- hur väntetiden mellan försök utvecklas,
- hur samtidiga återförsök sprids över tid,
- hur operationens idempotens säkerställs,
- vad som händer när försöken är slut.

**Dead-letter – början på ett arbetsflöde, inte slutförvaring.**

När ett meddelande inte kan behandlas efter tillåtna försök behöver det ofta flyttas åt sidan så att resten av flödet kan fortsätta. Detta beskrivs ofta som dead-letter-hantering.

Det viktiga är inte den tekniska dead-letter-kön i sig. Det viktiga är vad organisationen gör med misslyckade meddelanden.

En dead-letter-mekanism behöver därför kopplas till frågor som:

- Vem äger felet?
- Hur upptäcks det?
- Vilken information behövs för felsökning?
- Kan meddelandet korrigeras och återföras säkert?
- Finns risk att det då behandlas dubbelt?
- Hur länge ska det sparas?
- Hur ser man att mängden fel växer?

En dead-letter-kö som ingen övervakar är inte en felhanteringsstrategi. Den är ett arkiv över ouppklarade problem.

**Ordering – betala bara för ordning när den betyder något.**

Ordering är en typisk integrationsfråga där ett generellt ”starkare” beteende kan vara dyrare än verksamheten behöver.

I vissa flöden är ordningen central. Om en statusövergång från `Skapad` till `Godkänd` måste behandlas före `Avslutad` kan omkastning ge ett semantiskt fel.

I andra flöden är ordningen ointressant. Hundra oberoende analysuppgifter kan kanske behandlas i vilken sekvens som helst.

Det finns dessutom flera nivåer av ordering:

- global ordning för alla meddelanden,
- ordning inom ett visst ärende eller aggregat,
- ordning per producent,
- ingen garanterad ordning.

Att kräva global ordning när endast per-ärende-ordning behövs kan minska parallellism och skalbarhet. Därför bör ordering formuleras som ett konkret verksamhetskrav och avgränsas till den minsta nödvändiga mängden meddelanden.

**”Exakt en gång” är ofta fel fråga.**

I integrationsdiskussioner dyker ofta önskemålet ”exactly once” upp. Bakom det finns vanligtvis ett legitimt verksamhetskrav: en verksamhetseffekt får inte uppstå dubbelt.

Det är bättre att formulera just det kravet än att börja med en transportegenskap.

En robust lösning kan exempelvis kombinera:

- minst-en-gång-leverans,
- stabilt operations-id,
- idempotent konsument,
- transaktionell lokal hantering,
- tydlig återställningsprocedur.

Ur verksamhetens perspektiv kan detta ge den önskade effekten utan att hela den distribuerade kedjan måste lova ett absolut ”exakt en gång”-beteende.

Poängen är inte att en viss leveranssemantik alltid är rätt, utan att verksamhetseffekten ska beskrivas först och den tekniska mekanismen därefter.

**Fel ska isoleras men inte döljas.**

Asynkrona mönster är bra på att hindra ett tillfälligt fel från att omedelbart spridas bakåt. Det kan göra systemet mer motståndskraftigt. Samtidigt finns en risk att fel blir mindre synliga.

En kö kan fortsätta ta emot meddelanden trots att ingen konsument lyckas behandla dem. Användarens initiala anrop ser kanske lyckat ut samtidigt som den faktiska verksamhetsprocessen står still.

Därför behöver integrationsmönstren kopplas till driftbarhetsmönstren från kapitel 27:

- ködjup behöver kunna observeras,
- återförsök behöver mätas,
- dead-letter-volymer behöver larmas,
- end-to-end-latens behöver följas,
- korrelationsinformation behöver följa flödet,
- verksamhetsnära status behöver kunna skiljas från teknisk transportstatus.

Lös koppling får inte betyda lös ansvarskedja.

## Publicera/prenumerera – uttryck fakta utan att styra mottagarna

Publicera/prenumerera, eller pub/sub, används när en producent publicerar information som flera oberoende konsumenter kan vara intresserade av.

Strukturen kan förenklas till:

```text
                  ┌→ Konsument A
Producent → Event ├→ Konsument B
                  └→ Konsument C
```

Producenten behöver inte känna till alla konsumenter. Nya konsumenter kan tillkomma utan att producenten byggs om för varje mottagare.

Detta är en stark egenskap när händelsen uttrycker ett redan inträffat faktum, exempelvis:

- `ÄrendeRegistrerat`,
- `BeslutFattat`,
- `LeveransMottagen`.

Producenten säger då i princip: ”detta har hänt”. Konsumenterna avgör själva vad det betyder för dem.

### Event är inte ett förklätt kommando

En vanlig feltillämpning är att skapa events som egentligen instruerar en bestämd mottagare:

- `UppdateraSystemB`,
- `SkickaRapportTillAnalysplattform`,
- `SynkroniseraRegisterC`.

Detta ser tekniskt asynkront ut men behåller en stark semantisk koppling. Producenten känner fortfarande till mottagarens ansvar och styr dess beteende.

Ett verkligt domänevent beskriver normalt ett faktum ur producentens eget ansvarsperspektiv. Det gör att producenten kan förbli okunnig om varför andra konsumenter är intresserade.

### Pub/sub flyttar ansvar till kontraktet

När producenten inte känner sina konsumenter blir eventkontraktet ännu viktigare. Ett event som publiceras brett kan få fler beroenden än producenten vet om.

Det innebär att följande behöver vara tydligt:

- vad eventet betyder,
- vilken domän som äger betydelsen,
- när det publiceras,
- om det representerar ett faktum eller en teknisk notifiering,
- vilka fält som är stabila,
- hur förändringar hanteras,
- hur länge konsumenter kan förvänta sig stödet.

Lös koppling på runtime-nivå får alltså inte förväxlas med frånvaro av kontraktsansvar.

## Meddelande, kommando och event behöver hållas isär

Asynkron teknik kan bära flera olika semantiska former. Två särskilt viktiga är kommando och event.

Ett kommando uttrycker ungefär:

> Jag vill att en viss ansvarig part försöker göra något.

Ett event uttrycker ungefär:

> Något har redan hänt inom mitt ansvar.

Skillnaden påverkar ägarskap och felhantering.

Om ett kommando inte kan genomföras finns normalt en avsändare som behöver förstå utfallet. Om en av flera eventkonsumenter misslyckas har producenten inte nödvändigtvis ansvar för konsumentens lokala reaktion.

Detta är ett exempel på varför transportmekanismen inte räcker för att beskriva integrationen. Två meddelanden på samma tekniska plattform kan ha helt olika kontrakts- och ansvarsbeteende.

## Korrelation – bevara sammanhang utan att skapa central kontroll

Asynkrona flöden bryter den direkta anropskedjan. Det gör systemet mindre tidskopplat men svårare att följa.

Korrelation används för att kunna relatera meddelanden och händelser till ett gemensamt sammanhang, exempelvis:

- en användarbegäran,
- ett ärende,
- en order,
- en processinstans,
- en teknisk trace.

Det kan finnas flera relevanta identiteter samtidigt. Ett `correlation-id` för observerbarhet är inte nödvändigtvis samma sak som verksamhetens ärende-id, och ett meddelande-id har ett annat syfte än båda.

En robust lösning skiljer därför mellan:

- meddelandets identitet – vilket enskilt meddelande är detta?
- operationens identitet – vilken logisk begäran representeras?
- verksamhetskorrelation – vilket ärende eller aggregat hör det till?
- teknisk trace-korrelation – hur följs exekveringskedjan i observerbarhetsverktyg?

Om alla dessa pressas in i ett enda fält blir betydelsen snabbt oklar.

## Kontraktsutveckling är en del av mönstret

Integrationer lever längre än den version som först skapade dem. Därför behöver mönstren kunna bära förändring.

Ett kontrakt består inte bara av JSON-, XML- eller meddelandeschema. Det omfattar också:

- semantik,
- obligatoriskt beteende,
- felbeteende,
- timingförväntningar,
- eventuella orderingkrav,
- livscykel och supportperiod.

### Kompatibel förändring först

När det är möjligt bör kontrakt utvecklas genom förändringar som befintliga konsumenter kan tåla. Exempel kan vara att lägga till ny information som äldre konsumenter kan ignorera.

Men ”bakåtkompatibel” är inte bara en schemafråga. Ett nytt fält kan tekniskt vara valfritt men ändå ändra innebörden av hela meddelandet. Semantisk kompatibilitet behöver därför bedömas separat.

### Parallella versioner har en kostnad

Ibland behövs en ny kontraktsversion. Då uppstår frågor om:

- hur länge den gamla stöds,
- hur konsumenter upptäcks,
- vem som driver migrering,
- om producenten behöver publicera flera versioner,
- hur gamla versioner avvecklas.

En versioneringsmodell utan avvecklingsmodell ackumulerar kontraktsskuld.

## Kombinera mönster medvetet

Verkliga lösningar använder ofta flera mönster samtidigt.

En publik e-tjänst kan exempelvis använda:

```text
Webbklient
   ↓
BFF
   ↓
Domäntjänst
   ↓
Asynkront kommando
   ↓
Bearbetning
   ↓
Domänevent
   ↓
Flera prenumeranter
```

Varje övergång har olika syfte:

- BFF isolerar klienten från intern struktur,
- det asynkrona kommandot bryter tidskoppling för ett arbete som får utföras senare,
- eventet informerar oberoende konsumenter om ett inträffat faktum.

Det är viktigt att inte beskriva hela kedjan som ”eventdriven” och därmed förlora skillnaden mellan dessa ansvar.

### Mönsterkombinationer skapar nya krafter

När flera mönster kombineras behöver man analysera helheten:

- Hur får användaren veta att den asynkrona operationen är klar?
- Vem äger statusen under tiden?
- Kan BFF lagra tillstånd eller bara presentera det?
- Vad händer om eventet publiceras men en prenumerant misslyckas?
- Hur korreleras hela flödet?
- Vilken del har auktoritativ information?

Ett korrekt valt mönster lokalt garanterar alltså inte en bra arkitektur globalt.

## Plattformstöd och ansvar

Gemensamma tjänster för API management, messaging, eventdistribution, kontraktsregister, observerbarhet samt identitets- och certifikathantering kan göra rätt integrationsmönster enklare att använda. De bör ge guardrails och standardprofiler, men inte tvinga alla behov in i samma kommunikationsform. En messagingplattform är inte ett argument för att allt ska vara asynkront, och ett API-gateway-erbjudande är inte ett argument för att varje intern metod ska exponeras som API.

Ansvarsfördelningen följer den modell som redan etablerats i boken. Den gemensamma nivån sätter principer, miniminivåer för säkerhet, spårbarhet och kontraktslivscykel. Förmågeansvaret för Integration och kommunikation omsätter detta i mönster, profiler, plattformserbjudanden och stöd. Den konkreta lösningen avgör däremot vilken relation som faktiskt finns mellan parterna, vilket mönster som passar och hur leverans-, ordering-, idempotens- och felbeteende ska realiseras.

Plattformstjänsten realiserar alltså ett behov och ett valt mönster. Den skapar inte behovet.

## Vanliga anti-patterns

Några återkommande fel är särskilt värda att känna igen:

- **Allt blir event.** Tekniska notifieringar publiceras utan tydligt domänansvar. Fråga vilket faktum en oberoende konsument faktiskt behöver reagera på.
- **Asynkront för att slippa hantera fel.** En kö införs utan definierade återförsök, dead-letter, status eller kompensation. Felet flyttas bara i tid.
- **BFF som verksamhetslager.** Kanalnära lagret börjar äga regler och data som ska vara gemensamma över kanaler.
- **Återförsök utan idempotens.** En teknisk återhämtningsmekanism kan då skapa dubbla verksamhetseffekter.
- **Dead-letter som slutförvaring.** Misslyckade meddelanden saknar ägare, larm och säker återföringsprocess.
- **Global ordering som standard.** Allt serialiseras trots att verksamheten bara behöver lokal ordning inom exempelvis ett ärende.
- **Event som dolt RPC.** Ett ”event” instruerar i praktiken en namngiven konsument och döljer den semantiska kopplingen.
- **Eviga kontraktsversioner.** Nya versioner införs utan migrations- och avvecklingsplan.

## En praktisk analysordning

När ett integrationsproblem ska lösas kan följande ordning användas.

### 1. Identifiera ansvariga parter

Vilka domäner eller tjänster äger informationen och beteendet på respektive sida?

### 2. Beskriv önskad relation

Behöver avsändaren ett omedelbart svar? Ska en bestämd mottagare göra något? Eller ska producenten bara uttrycka att ett faktum har inträffat?

### 3. Identifiera acceptabel koppling

Analysera tid, identitet, kontrakt, tillgänglighet, sekvens, kapacitet och förändring.

### 4. Välj grundmönster

Exempelvis synkron request/reply, asynkront kommando, pub/sub eller BFF i klientgränsen.

### 5. Definiera kontraktets semantik

Vad betyder meddelandet eller API-operationen? Vem äger betydelsen? Vad är ett kommando och vad är ett event?

### 6. Definiera leverans- och felbeteende

Behövs återförsök? Hur uppnås idempotens? Finns orderingkrav? Vad händer efter sista försöket?

### 7. Definiera korrelation och observerbarhet

Hur följs flödet tekniskt och verksamhetsmässigt över systemgränser?

### 8. Definiera förändringsmodellen

Vilka kompatibilitetsregler gäller? Hur introduceras och avvecklas kontraktsversioner?

### 9. Välj plattformstjänst och standardprofil

Först nu väljs den gemensamma tekniska realisering som bäst stödjer mönstret och kraven.

### 10. Testa felvägarna

Verifiera inte bara happy path. Testa dubbletter, omkastad ordning, timeout, otillgänglig konsument, överbelastning, ogiltiga meddelanden och återföring från dead-letter-hantering.

## Sammanfattning

Integrations- och kommunikationsmönster handlar om att forma beroenden mellan självständiga delar. Backend for Frontend isolerar kanalnära variationer från domän- och backendstrukturen. Asynkron meddelandekommunikation minskar tidskoppling och kan absorbera variation i tillgänglighet och belastning. Publicera/prenumerera gör det möjligt att uttrycka inträffade fakta till flera oberoende konsumenter utan att producenten behöver styra deras beteende.

Mönstrens värde avgörs dock av detaljerna runt omkring dem. Idempotens, återförsök, dead-letter-hantering, ordering, korrelation och kontraktsutveckling är avgörande för om en lösning blir robust eller bara mer distribuerad.

Det viktigaste är därför inte att standardisera ett enda integrationssätt. Det är att skapa ett gemensamt språk för vilken relation man vill ha, vilka krafter som behöver balanseras och vilka konsekvenser varje mönster medför. När detta kombineras med gemensamma plattformstjänster och guardrails kan lösningsteamen återanvända arkitekturell erfarenhet utan att förlora domänansvar och lokal beslutskraft.
