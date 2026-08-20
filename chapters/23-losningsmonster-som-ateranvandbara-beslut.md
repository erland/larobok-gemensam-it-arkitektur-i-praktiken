# 23. Lösningsmönster som återanvändbara beslut

När flera utvecklingsteam möter samma slags arkitekturproblem uppstår nästan alltid återkommande lösningar. Ett team placerar ett kanalnära lager mellan webbklienten och domäntjänsterna. Ett annat låter meddelanden bära arbete över en tidsgräns. Ett tredje separerar den auktoritativa databasen från ett sökindex. Ett fjärde bygger samma releaseartefakt en gång och promoverar den genom flera miljöer.

Efter ett tag kan organisationen känna igen formerna. Då uppstår en möjlighet: i stället för att varje lösningsteam återupptäcker samma resonemang kan erfarenheten beskrivas som ett lösningsmönster.

Ett mönster är dock inte värdefullt bara för att en viss struktur förekommer ofta. Det måste fånga varför strukturen är användbar, i vilken kontext den fungerar, vilka krafter som behöver balanseras och vilka konsekvenser som följer av valet.

Det är därför missvisande att se ett lösningsmönster som en ritning som ska kopieras. Ett användbart mönster är snarare ett återanvändbart stycke arkitekturellt beslutsstöd.

Den centrala frågan i detta kapitel är:

> Hur beskriver vi återkommande lösningar på ett sätt som hjälper arkitekter att fatta bättre beslut utan att förvandla mönstret till ett recept?

## Från enskilt beslut till återanvändbar erfarenhet

Arkitekturbeslut är val mellan realistiska alternativ under givna drivkrafter och begränsningar. Ett lösningsmönster kan ses som nästa steg när samma typ av beslut återkommer i flera lösningar.

Förenklat kan utvecklingen beskrivas så här:

```text
Återkommande problem
        ↓
Flera lösningars erfarenheter
        ↓
Gemensamma krafter och avvägningar
        ↓
Återkommande lösningsstruktur
        ↓
Dokumenterat lösningsmönster
```

Det viktiga är att generaliseringen inte börjar i tekniken. Om tre system råkar använda samma produkt är det inte automatiskt ett mönster. Det kan bara vara en produktstandard eller en historisk likhet.

Ett mönster bör i stället svara på ett stabilare problem.

Backend for Frontend är exempelvis inte intressant därför att vissa lösningar råkar ha en viss sorts serverkomponent. Det är intressant därför att olika klienter kan ha olika behov av aggregering, sessionshantering, säkerhetsanpassning och dataformat, samtidigt som organisationen vill undvika att exponera interna tjänstegränser direkt mot klienten.

Det återanvändbara ligger alltså i relationen mellan problem, kontext, krafter och struktur.

## Ett mönster är inte ett recept

Ett recept säger i princip:

> Gör A, sedan B, sedan C.

Ett arkitekturmönster bör i stället säga:

> I denna typ av situation uppstår dessa motstridiga behov. En återkommande struktur som ofta balanserar dem är denna. Den ger vissa fördelar, men introducerar också dessa kostnader och risker.

Skillnaden är avgörande.

Om ett mönster blir ett recept uppstår lätt två problem.

Det första är överanvändning. Organisationen börjar applicera mönstret även när problemet inte finns. Om Backend for Frontend blir en regel kan varje frontend få ett eget backendlager, även när klienten utan problem kan använda ett stabilt API direkt. Då har mönstret skapat en extra komponent utan att lösa ett verkligt problem.

Det andra är falsk trygghet. Teamet kan tro att arkitekturen är korrekt bara för att ett känt mönster används. Men mönstret garanterar inte att lösningens kvalitetskrav, informationsgränser, säkerhet eller domänmodell är riktiga.

Ett mönster minskar alltså inte behovet av arkitekturtänkande. Det koncentrerar tidigare arkitekturtänkande så att nästa beslut kan börja på en högre nivå.

## Mönstrets kärna: kontext, problem och krafter

Ett starkt mönster börjar inte med lösningen. Det börjar med kontexten.

Kontexten beskriver den situation där problemet brukar uppstå. För ett mönster för *asynkron meddelandekommunikation* kan kontexten exempelvis vara att två delar av ett system behöver utbyta arbete men inte bör vara tidsmässigt beroende av att båda är tillgängliga samtidigt.

Därefter behöver problemet formuleras. Problemet är inte ”vi behöver en meddelandekö”. Det är snarare något i stil med:

> Hur kan en producent lämna över arbete utan att behöva vänta på att konsumenten är tillgänglig och klar just nu?

Sedan kommer krafterna – ibland kallade forces. Det är de drivkrafter och spänningar som gör problemet arkitekturellt intressant.

För asynkron kommunikation kan sådana krafter vara:

- behov av lös tidskoppling,
- krav på genomströmning,
- tolerans för fördröjning,
- krav på leveranssäkerhet,
- behov av ordering,
- felhantering,
- spårbarhet,
- komplexitet i felsökning,
- krav på omedelbart svar till användaren.

Det är just eftersom dessa krafter drar åt olika håll som ett mönster behövs. Om det bara fanns ett självklart tekniskt svar skulle problemet sällan vara värt ett eget arkitekturmönster.

## Strukturen är svaret – men inte hela svaret

När kontext, problem och krafter är tydliga kan mönstret beskriva en återkommande lösningsstruktur.

Exempelvis:

```text
Producent
   ↓
Meddelande
   ↓
Förmedlande infrastruktur
   ↓
Konsument
```

Denna struktur är medvetet abstrakt. Ett lösningsmönster bör normalt inte behöva ange:

- produktnamn,
- exakt protokollversion,
- operativsystem,
- specifik molntjänst,
- exakt konfigurationsparameter.

Sådant hör hemma längre ned i arkitekturmodellen – i plattformstjänster, tekniska standarder, byggblock och produktval.

Men abstraktion får inte bli vaghet. Ett mönster som bara säger ”använd asynkron kommunikation när asynkron kommunikation är lämplig” ger inget beslutsstöd.

Ett bra mönster behöver därför vara teknikoberoende men mekanismtydligt.

Det ska vara möjligt att förstå:

- vilka roller eller komponenttyper som ingår,
- hur de samverkar,
- var ansvar ligger,
- vilka beroenden som minskar eller ökar,
- vilket beteende som förändras jämfört med alternativen.

## Konsekvenser hör till själva mönstret

Varje mönster har en kostnad.

Det är en av de viktigaste principerna i hela mönsterarbetet.

Om dokumentationen bara beskriver fördelarna har organisationen inte skapat ett mönster. Den har skapat marknadsföring.

Backend for Frontend kan exempelvis ge:

- tydligare kanalansvar,
- mindre koppling mellan klient och interna tjänster,
- enklare anpassning per kanal.

Men samma mönster kan också ge:

- ytterligare komponenter att utveckla och drifta,
- duplicerad logik mellan flera BFF:er,
- risk att kanalnära lager börjar bära verksamhetslogik,
- fler nätverksgränser och fler felmoder.

Asynkron meddelandekommunikation kan minska tidskoppling men samtidigt göra:

- felsökning mer distribuerad,
- konsistens mer fördröjd,
- felhantering mer explicit,
- idempotens och dubbletter till centrala designfrågor.

Mönstret är alltså inte ”bra” eller ”dåligt”. Det förändrar lösningens egenskaper.

Detta knyter direkt tillbaka till kvalitetsattributen. Ett lösningsmönster är i praktiken ett återkommande sätt att påverka en viss uppsättning kvaliteter och avvägningar.

## När mönstret passar – och när det inte passar

En av de mest värdefulla delarna i ett mönster är avsnittet När mönstret inte passar.

Det tvingar författaren att formulera mönstrets gräns.

För Human workflow kan mönstret vara lämpligt när:

- processen innehåller manuella arbetsuppgifter,
- tillstånd behöver bevaras över timmar eller dagar,
- uppgifter ska fördelas till personer, roller eller köer,
- deadlines och eskalering behöver hanteras,
- processen måste kunna återupptas efter avbrott.

Det är däremot sannolikt onödigt när:

- hela flödet är kortlivat och automatiskt,
- ett fåtal lokala UI-steg kan hanteras enklare i applikationen,
- det inte finns något verkligt behov av persistent processtillstånd.

Det negativa användningsområdet skyddar mot pattern fever – tendensen att använda ett känt mönster därför att det är känt.

Ett mönsterbibliotek blir därför starkare om varje mönster tydligt beskriver minst tre saker:

1. när det passar,
2. när det inte passar,
3. vilka tecken som visar att problemet håller på att förändras så att mönstret behöver omprövas.

## Variationer är en del av mönstret

Verkliga arkitekturer är sällan identiska. Därför behöver mönster kunna beskriva variation points.

Ta *publicera/prenumerera* som exempel. Grundidén är att producenter publicerar information utan att känna alla konsumenter. Men lösningen kan variera i exempelvis:

- hur många typer av konsumenter som finns,
- om prenumerationer är statiska eller dynamiska,
- hur händelser lagras,
- om replay behövs,
- vilken ordning som garanteras,
- hur schemautveckling hanteras,
- hur åtkomst till olika händelsetyper styrs.

Om mönstret försöker bestämma alla dessa val slutar det vara ett mönster och blir en specifik referenslösning eller standardprofil.

Om det inte nämner dem alls kan det bli för abstrakt för att hjälpa.

En bra mönsterbeskrivning visar därför både den stabila kärnan och de viktigaste variationspunkterna.

## Pattern language – mönster som hänger ihop

Ett enskilt mönster är sällan tillräckligt för en verklig lösning.

En intern e-tjänst kan exempelvis kombinera:

```text
Backend for Frontend
        ↓
Tjänsteidentitet
        ↓
Asynkron meddelandekommunikation
        ↓
System of record och härledda kopior
        ↓
Observerbarhet för distribuerade tjänster
```

Det betyder inte att mönstren bildar en strikt kedja. Poängen är att de adresserar olika problem i samma lösning.

När mönster beskrivs med relationer till andra mönster börjar ett pattern language växa fram: ett språk där arkitekter kan resonera om återkommande strukturer och hur de kombineras.

Ett sådant språk kan bland annat uttrycka relationer som:

- kompletterar – två mönster löser olika delar av samma problem,
- förutsätter – ett mönster kräver att en annan mekanism eller struktur redan finns,
- alternativ till – två mönster hanterar samma kraft på olika sätt,
- förstärker – kombinationen ökar en viss kvalitet,
- står i spänning med – mönstren kan kombineras men skapar nya avvägningar,
- specialiserar – ett mer specifikt mönster förfinar ett bredare.

Detta är mer användbart än en lång alfabetisk lista över mönsternamn. Mönsterbibliotekets verkliga värde uppstår när läsaren kan förstå landskapet mellan mönstren.

## Mönstrets plats i arkitekturmodellen

Ett lösningsmönster behöver kunna skiljas från andra arkitekturartefakter. Annars blir katalogen snabbt en blandning av principer, standarder, plattformar och lösningsskisser med olika syften.

**Princip och mönster.** En princip uttrycker beslutsriktning, exempelvis *Behov före teknik*. Ett mönster beskriver i stället en återkommande lösningsstruktur för en viss problemklass, exempelvis *Build once, promote many*. Principer hjälper oss bedöma vad som är önskvärt; mönster hjälper oss strukturera hur ett återkommande problem kan lösas.

**Mönster och standard.** En teknisk standard minskar variation genom att ange vad som ska eller bör användas och under vilka villkor. Mönstret *Asynkron meddelandekommunikation* kan vara stabilt även när organisationens standard för protokoll, säkerhetsprofil eller produkt förändras.

**Mönster och plattformstjänst.** Ett mönster är beslutsstöd, inte ett erbjudande som konsumeras. Mönstret *Tjänsteidentitet* kan beskriva struktur och ansvar, medan en Service Identity Platform realiserar delar av mönstret genom identitetsutfärdande, rotation, policyintegration och livscykelhantering. Frågan "vilket mönster passar?" bör därför hållas isär från frågan "vilket gemensamt erbjudande hjälper oss att realisera det?".

**Mönster och referensarkitektur.** En referensarkitektur är bredare och kombinerar flera mönster, förmågor, kvalitetskrav och variationspunkter för en klass av lösningar. Mönstren är återanvändbara byggstenar i resonemanget; referensarkitekturen visar hur de kan samverka i en större struktur.

Distinktionerna är praktiskt viktiga eftersom samma arkitekturidé annars lätt råkar beskrivas fyra gånger med olika status. Ett mönster ska inte göras obligatoriskt bara för att det ligger i mönsterbiblioteket, och en produkt ska inte få mönsterstatus bara för att den används ofta. Den stabila problem- och lösningsstrukturen behöver kunna överleva när standarder, plattformar och produkter förändras.

Samma noggrannhet behövs för anti-patterns. Ett anti-pattern är en återkommande lösningsform som ofta verkar rimlig men tenderar att ge oönskade konsekvenser i en viss kontext. Delad databas mellan självständiga domäner, backup som aldrig återställningstestas eller en gemensam plattform som börjar äga verksamhetslogik kan vara sådana exempel. Men etiketten är inte universell: samma mekanism kan vara fullt rimlig i en annan kontext.

## Från kandidat till förvaltat mönster

Ett mönsterbibliotek behöver vara återhållsamt. Varje teknikidé, kodkonvention eller favoritlösning ska inte bli ett eget mönster. Ett kandidatobjekt bör åtminstone svara ja på frågor som:

- Återkommer problemet i flera lösningar eller förmågor?
- Är problemet arkitekturellt snarare än en lokal implementeringsdetalj?
- Är lösningsidén tillräckligt stabil för att överleva produktbyten?
- Finns verkliga avvägningar och tydliga situationer där mönstret passar respektive inte passar?
- Kan flera team använda beskrivningen som beslutsstöd?
- Är detta verkligen ett mönster och inte en standard, plattformstjänst eller instruktion?

Ett mindre bibliotek med tydliga inträdeskrav är oftast mer användbart än hundratals nästan överlappande poster.

En praktisk mönsterbeskrivning behöver inte vara lång, men bör innehålla:

### Namn och syfte

Ett stabilt namn och den övergripande effekt mönstret försöker åstadkomma.

### Kontext, problem och krafter

I vilka situationer problemet uppstår, vilket problem som ska lösas och vilka kvalitetskrav, begränsningar och motstridiga behov som påverkar valet.

### Struktur

Vilka roller eller komponenttyper som ingår och hur de relaterar.

### Passform och konsekvenser

När mönstret passar, när det inte passar samt både positiva och negativa effekter.

### Variationer och relationer

Vad som normalt behöver anpassas lokalt och vilka andra mönster som kompletterar, konkurrerar med eller förutsätts av detta.

### Förmågor och realisering

Vilka förmågor som berörs och vilka plattformstjänster eller standarder som kan hjälpa till att realisera mönstret utan att blandas ihop med själva mönstret.

Mönster behöver dessutom evidens från verkliga lösningar. En enkel livscykel kan vara:

```text
Kandidat
   ↓
Prövad i en eller flera lösningar
   ↓
Rekommenderat mönster
   ↓
Etablerad erfarenhet
   ↓
Omprövas, ersätts eller avvecklas
```

Statusnamnen är mindre viktiga än återkopplingen. Om återkommande avsteg visar att ett mönster är svårt att använda kan kontexten vara för bred, viktiga krafter saknas, plattformsstödet vara otillräckligt eller förutsättningarna ha förändrats. Då ska mönstret förbättras, delas upp eller avvecklas – inte försvaras därför att det redan finns i katalogen.

Evidens behöver inte innebära att alla lösningar ser likadana ut. Tvärtom är det ofta variationerna som visar om mönstrets kärna är rätt formulerad. Om flera team använder samma grundstruktur men gör olika lokala val kring exempelvis protokoll, skalning eller felhantering kan det vara ett tecken på att mönstret ligger på rätt abstraktionsnivå. Om varje användning kräver undantag från själva kärnstrukturen är mönstret sannolikt för brett eller fel avgränsat.

Ansvar följer samma modell som i övriga boken. Den gemensamma arkitekturnivån sätter form, katalogstruktur och livscykelregler. Förmågenivån identifierar kandidater, samlar erfarenhet och förvaltar mönster inom sitt problemområde. Lösningsteamet bedömer om mönstret faktiskt passar den aktuella kontexten och dokumenterar varför det används eller väljs bort. Ett välmotiverat avsteg är därför inte bara ett lokalt undantag utan kan vara viktig återkoppling till biblioteket.

Mönster som spänner över flera förmågor behöver ett explicit ägarskap även om förvaltningen är gemensam. Annars uppstår lätt samma problem som med andra gemensamma artefakter: alla förväntar sig att någon annan håller konsekvenser, relationer och status aktuella.

## Mönster som gemensamt språk och beslutstöd

Ett av de största värdena med mönster är språket de skapar. Om arkitekter, utvecklare och plattformsteam delar betydelsen av uttryck som Backend for Frontend, Human workflow, System of record och härledda kopior eller Build once, promote many kan diskussionen börja på en högre abstraktionsnivå.

Mönsternamnet ersätter dock inte analysen. En diskussion kan exempelvis börja med:

> Här verkar vi behöva en härledd sökrepresentation från system of record, men vi måste diskutera hur färsk kopian behöver vara.

Då har mönstret gjort analysen effektivare utan att avgöra svaret. Därför måste namnen också användas konsekvent; om samma namn betyder olika saker i olika delar av organisationen skapas bara en ny begreppsförvirring.

Ett bra mönster ska dessutom göra det lättare att säga nej till onödig komplexitet. Om ett team föreslår Cache-aside bör mönstret tvinga fram frågor om vilket problem cachen löser, hur gammal informationen får bli, hur invalidation fungerar och vad som händer vid cachemiss eller otillgänglighet. Om frågorna inte kan besvaras kan den bästa arkitekturen vara att inte införa cachen alls.

## Från mönster till konkret lösning

När ett lösningsteam använder ett mönster behöver det fortfarande göra flera lokala val.

Exempelvis kan mönstret Build once, promote many ge den stabila idén:

```text
Källkod
   ↓
Build + verifiering
   ↓
Versionsmärkt artefakt
   ├─ test
   ├─ acceptans
   └─ produktion
```

Men lösningen behöver fortfarande avgöra:

- vilken artefakttyp som används,
- var den lagras,
- hur provenance verifieras,
- hur miljökonfiguration separeras,
- vilka kontroller som krävs före promotion,
- vilken driftsättningsstrategi som används,
- hur rollback eller roll-forward hanteras.

En del av dessa val kan styras av plattformstjänster och tekniska standarder. Andra hör hemma i den konkreta lösningsarkitekturen.

Det är därför kedjan i bokens metamodell är viktig:

```text
Förmåga
   ↓
Lösningsmönster
   ↓
Plattformstjänst och/eller standard
   ↓
Tekniska byggblock
   ↓
Konkret lösning
```

Mönstret är ett lager i resonemanget – inte slutpunkten. Det innebär också att två lösningar kan använda samma mönster och ändå få olika teknisk realisering. Det viktiga är att den stabila strukturen och de relevanta avvägningarna är gemensamma, inte att varje detalj blir identisk.

## När ett mönster bör delas, delas upp eller tas bort

Mönsterbiblioteket behöver också kunna förenklas.

Ett mönster kan vara för brett om:

- det innehåller flera problem som kan uppstå oberoende av varandra,
- olika delar har helt olika krafter,
- ”när det passar” blir så brett att nästan allt inkluderas,
- variationerna är större än den gemensamma kärnan.

Då kan det behöva delas upp.

Två mönster kan tvärtom behöva slås ihop om:

- de i praktiken löser samma problem,
- skillnaden bara är produktspecifik,
- läsaren måste förstå båda för att kunna använda något av dem,
- samma avvägningar upprepas nästan ordagrant.

Ett mönster kan behöva tas bort om:

- problemet inte längre förekommer,
- lösningsformen har blivit en självklar mekanism på en lägre abstraktionsnivå,
- en plattform helt har absorberat variationen så att arkitekturbeslutet i praktiken försvunnit,
- erfarenheten visar att mönstret konsekvent leder fel.

Att ta bort ett mönster är alltså inte ett misslyckande. Det är ett tecken på att arkitekturkunskapen förvaltas.

## De femton mönstren i boken

Boken använder femton lösningsmönster:

- Backend for Frontend,
- Asynkron meddelandekommunikation,
- Publicera/prenumerera,
- Human workflow,
- Externaliserade verksamhetsregler,
- System of record och härledda kopior,
- Cache-aside,
- Retrieval-Augmented Generation,
- AI med mänsklig kontroll,
- Tjänsteidentitet,
- Containeriserad stateless tjänst,
- Build once, promote many,
- Observerbarhet för distribuerade tjänster,
- Backup och verifierad återställning,
- Kontrollerad samarbetsyta.

Urvalet är inte tänkt som ett komplett katalogverk över alla arkitekturmönster. Det speglar de återkommande beslut som blev särskilt relevanta när de elva gemensamma IT-förmågorna analyserades.

Detta illustrerar en viktig princip:

> Ett organisationsgemensamt mönsterbibliotek bör växa ur de problem organisationen faktiskt behöver lösa – inte ur ambitionen att katalogisera hela IT-branschens mönsterkunskap.

I de kommande kapitlen fördjupar vi dessa mönster i grupper. Syftet är inte att göra katalogposterna längre för sakens skull, utan att visa hur de påverkar verkliga arkitekturbeslut och hur flera mönster kan kombineras utan att ansvar och avvägningar försvinner.

## En praktisk analysordning

När ett team överväger ett lösningsmönster kan följande ordning användas:

1. Formulera problemet utan mönsternamn. Vad försöker vi faktiskt lösa?
2. Beskriv kontexten. Vilka domäner, användare, systemgränser och tekniska begränsningar finns?
3. Identifiera krafterna. Vilka kvalitetskrav och motstridiga behov driver beslutet?
4. Jämför realistiska alternativ. Är mönstret ett av flera möjliga svar?
5. Kontrollera passform och antipassform. Finns förutsättningarna som mönstret bygger på?
6. Analysera konsekvenserna. Vilken komplexitet och vilka nya felmoder introduceras?
7. Identifiera variationerna. Vad behöver anpassas lokalt?
8. Koppla till gemensamma erbjudanden och standarder. Finns plattformsstöd eller guardrails?
9. Dokumentera varför mönstret används. Mönsternamnet ersätter inte beslutets rationale.
10. Återför erfarenheten. Om mönstret inte fungerar som väntat ska biblioteket förbättras.

Denna ordning gör det svårare att börja med formuleringen ”vi ska använda mönster X” och först därefter leta efter problemet.

## Sammanfattning

Lösningsmönster är ett sätt att göra arkitekturerfarenhet återanvändbar utan att göra alla lösningar likadana.

Ett bra mönster beskriver kontext, problem, krafter, lösningsstruktur, passform, konsekvenser, variationer och relationer till andra arkitekturartefakter.

Mönster är inte produkter, inte standarder, inte plattformstjänster och inte kompletta referensarkitekturer. De är återanvändbara beslutserfarenheter.

När de används rätt skapar de ett gemensamt språk och gör det möjligt för lösningsteam att börja med tidigare erfarenhet i stället för från ett tomt papper. När de används fel blir de recept, obligatoriska rutor i diagram eller nya former av central detaljstyrning.

Det är därför mönsterbibliotekets viktigaste kvalitet inte är storleken. Det är hur väl varje mönster hjälper läsaren att förstå när en viss struktur är ett bra svar – och när den inte är det.

I nästa kapitel går vi från mönsterbegreppet till den första gruppen konkreta mönster: integrations- och kommunikationsmönster, där tidskoppling, leveransbeteende, idempotens, ordering och kontraktsutveckling blir centrala delar av analysen.
