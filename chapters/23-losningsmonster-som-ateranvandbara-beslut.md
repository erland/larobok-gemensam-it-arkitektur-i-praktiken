# 23. Lösningsmönster som återanvändbara beslut

När flera utvecklingsteam möter samma slags arkitekturproblem uppstår nästan alltid återkommande lösningar. Ett team placerar ett kanalnära lager mellan webbklienten och domäntjänsterna. Ett annat låter meddelanden bära arbete över en tidsgräns. Ett tredje separerar den auktoritativa databasen från ett sökindex. Ett fjärde bygger samma releaseartefakt en gång och promoverar den genom flera miljöer.

Efter ett tag kan organisationen känna igen formerna. Då uppstår en möjlighet: i stället för att varje lösningsteam återupptäcker samma resonemang kan erfarenheten beskrivas som ett **lösningsmönster**.

Ett mönster är dock inte värdefullt bara för att en viss struktur förekommer ofta. Det måste fånga **varför** strukturen är användbar, **i vilken kontext** den fungerar, **vilka krafter som behöver balanseras** och **vilka konsekvenser som följer av valet**.

Det är därför missvisande att se ett lösningsmönster som en ritning som ska kopieras. Ett användbart mönster är snarare ett återanvändbart stycke arkitekturellt beslutsstöd.

Den centrala frågan i detta kapitel är:

> Hur beskriver vi återkommande lösningar på ett sätt som hjälper arkitekter att fatta bättre beslut utan att förvandla mönstret till ett recept?

## Från enskilt beslut till återanvändbar erfarenhet

I kapitel 5 beskrev vi arkitekturbeslut som val mellan realistiska alternativ under givna drivkrafter och begränsningar. Ett lösningsmönster kan ses som ett nästa steg när samma typ av beslut återkommer i flera lösningar.

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

**Backend for Frontend** är exempelvis inte intressant därför att vissa lösningar råkar ha en viss sorts serverkomponent. Det är intressant därför att olika klienter kan ha olika behov av aggregering, sessionshantering, säkerhetsanpassning och dataformat, samtidigt som organisationen vill undvika att exponera interna tjänstegränser direkt mot klienten.

Det återanvändbara ligger alltså i relationen mellan **problem, kontext, krafter och struktur**.

## Ett mönster är inte ett recept

Ett recept säger i princip:

> Gör A, sedan B, sedan C.

Ett arkitekturmönster bör i stället säga:

> I denna typ av situation uppstår dessa motstridiga behov. En återkommande struktur som ofta balanserar dem är denna. Den ger vissa fördelar, men introducerar också dessa kostnader och risker.

Skillnaden är avgörande.

Om ett mönster blir ett recept uppstår lätt två problem.

Det första är **överanvändning**. Organisationen börjar applicera mönstret även när problemet inte finns. Om Backend for Frontend blir en regel kan varje frontend få ett eget backendlager, även när klienten utan problem kan använda ett stabilt API direkt. Då har mönstret skapat en extra komponent utan att lösa ett verkligt problem.

Det andra är **falsk trygghet**. Teamet kan tro att arkitekturen är korrekt bara för att ett känt mönster används. Men mönstret garanterar inte att lösningens kvalitetskrav, informationsgränser, säkerhet eller domänmodell är riktiga.

Ett mönster minskar alltså inte behovet av arkitekturtänkande. Det koncentrerar tidigare arkitekturtänkande så att nästa beslut kan börja på en högre nivå.

## Mönstrets kärna: kontext, problem och krafter

Ett starkt mönster börjar inte med lösningen. Det börjar med **kontexten**.

Kontexten beskriver den situation där problemet brukar uppstå. För ett mönster för asynkron meddelandekommunikation kan kontexten exempelvis vara att två delar av ett system behöver utbyta arbete men inte bör vara tidsmässigt beroende av att båda är tillgängliga samtidigt.

Därefter behöver problemet formuleras. Problemet är inte ”vi behöver en meddelandekö”. Det är snarare något i stil med:

> Hur kan en producent lämna över arbete utan att behöva vänta på att konsumenten är tillgänglig och klar just nu?

Sedan kommer **krafterna** – ibland kallade forces. Det är de drivkrafter och spänningar som gör problemet arkitekturellt intressant.

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

Ett bra mönster behöver därför vara **teknikoberoende men mekanismtydligt**.

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

Detta knyter direkt tillbaka till kvalitetsattributen i kapitel 4. Ett lösningsmönster är i praktiken ett återkommande sätt att påverka en viss uppsättning kvaliteter och avvägningar.

## När mönstret passar – och när det inte passar

En av de mest värdefulla delarna i ett mönster är avsnittet **När mönstret inte passar**.

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

Det negativa användningsområdet skyddar mot **pattern fever** – tendensen att använda ett känt mönster därför att det är känt.

Ett mönsterbibliotek blir därför starkare om varje mönster tydligt beskriver minst tre saker:

1. när det passar,
2. när det inte passar,
3. vilka tecken som visar att problemet håller på att förändras så att mönstret behöver omprövas.

## Variationer är en del av mönstret

Verkliga arkitekturer är sällan identiska. Därför behöver mönster kunna beskriva **variation points**.

Ta publicera/prenumerera som exempel. Grundidén är att producenter publicerar information utan att känna alla konsumenter. Men lösningen kan variera i exempelvis:

- hur många typer av konsumenter som finns,
- om prenumerationer är statiska eller dynamiska,
- hur händelser lagras,
- om replay behövs,
- vilken ordning som garanteras,
- hur schemautveckling hanteras,
- hur åtkomst till olika händelsetyper styrs.

Om mönstret försöker bestämma alla dessa val slutar det vara ett mönster och blir en specifik referenslösning eller standardprofil.

Om det inte nämner dem alls kan det bli för abstrakt för att hjälpa.

En bra mönsterbeskrivning visar därför både **den stabila kärnan** och **de viktigaste variationspunkterna**.

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

När mönster beskrivs med relationer till andra mönster börjar ett **pattern language** växa fram: ett språk där arkitekter kan resonera om återkommande strukturer och hur de kombineras.

Ett sådant språk kan bland annat uttrycka relationer som:

- **kompletterar** – två mönster löser olika delar av samma problem,
- **förutsätter** – ett mönster kräver att en annan mekanism eller struktur redan finns,
- **alternativ till** – två mönster hanterar samma kraft på olika sätt,
- **förstärker** – kombinationen ökar en viss kvalitet,
- **står i spänning med** – mönstren kan kombineras men skapar nya avvägningar,
- **specialiserar** – ett mer specifikt mönster förfinar ett bredare.

Detta är mer användbart än en lång alfabetisk lista över mönsternamn. Mönsterbibliotekets verkliga värde uppstår när läsaren kan förstå **landskapet mellan mönstren**.

## Mönster och anti-patterns

Ett anti-pattern är inte bara ”en dålig lösning”. Det är en återkommande lösningsform som ofta verkar rimlig men tenderar att skapa oönskade konsekvenser i den aktuella kontexten.

Exempel som återkommit tidigare i boken är:

- delad databas som integrationsmodell mellan självständiga domäner,
- processmotor för kort och enkel lokal kontrolllogik,
- gemensamt generiskt API som tvingar alla klienter till samma behovsbild,
- omskrivning eller ny build av artefakten för varje miljö,
- backup som aldrig återställningstestas,
- gemensam plattform som gradvis börjar äga verksamhetslogik.

Anti-patterns är användbara därför att de synliggör **varför en till synes enkel lösning blir problematisk**.

Men även här behövs försiktighet. En lösning som är problematisk i en kontext kan vara fullt rimlig i en annan. En delad databas mellan två små moduler i samma applikation är inte samma arkitekturproblem som en delad databas mellan två organisatoriskt och livscykelmässigt självständiga domäner.

Anti-patterns bör alltså beskrivas med samma respekt för kontext som vanliga mönster.

## Skillnaden mellan princip och mönster

Arkitekturprinciper och lösningsmönster kan låta lika eftersom båda återanvänder erfarenhet.

Men de fyller olika roller.

En princip uttrycker **beslutsriktning**.

> Behov före teknik.

> Standardiserade erbjudanden när de möter behovet.

> Bygg in driftbarhet från början.

Ett mönster beskriver däremot **en återkommande lösningsstruktur för en viss typ av problem**.

> Build once, promote many.

> Backend for Frontend.

> Cache-aside.

Principen hjälper oss bedöma vad som är önskvärt. Mönstret hjälper oss strukturera hur ett återkommande problem kan lösas.

En princip kan därför motivera flera olika mönster, och ett mönster kan stödja flera principer.

## Skillnaden mellan mönster och standard

En teknisk standard minskar variation genom att ange vad som ska eller bör användas och under vilka villkor.

Ett lösningsmönster beskriver i stället ett återkommande sätt att strukturera en lösning.

Exempel:

```text
Mönster:
Asynkron meddelandekommunikation

Standard:
Vilka protokoll, kontraktsregler, säkerhetskrav och
leveransprofiler organisationen tillåter för messaging
```

Mönstret kan vara stabilt även när standarden förändras.

Organisationen kan byta produkt, protokollprofil eller versionskrav utan att den arkitekturella idén om asynkron kommunikation upphör att vara relevant.

Detta är samma separation mellan stabil arkitektur och föränderlig teknik som boken återkommande har betonat.

## Skillnaden mellan mönster och plattformstjänst

Ett mönster är inte något som konsumeras via ett beställningsgränssnitt.

En plattformstjänst är däremot ett faktiskt erbjudande.

Mönstret **Tjänsteidentitet** kan beskriva att workloads bör använda separata, maskinhanterade identiteter i stället för delade användarkonton eller hårdkodade credentials.

En **Service Identity Platform** kan sedan tillhandahålla:

- identitetsutfärdande,
- credential rotation,
- policyintegration,
- certifikat eller tokens,
- observerbarhet och livscykelhantering.

Mönstret beskriver struktur och ansvar. Plattformen gör en viss realisering enkel att konsumera.

Ett viktigt arkitekturarbete består därför i att skilja frågorna:

> Vilket mönster är lämpligt?

från:

> Vilket gemensamt erbjudande hjälper oss att realisera mönstret?

## Skillnaden mellan mönster och referensarkitektur

En referensarkitektur är normalt bredare än ett mönster.

Den kombinerar flera mönster, förmågor, kvalitetskrav och variationspunkter för en **klass av lösningar**.

Ett internt handläggningsstöd kan exempelvis använda:

- Backend for Frontend,
- Human workflow,
- Externaliserade verksamhetsregler,
- System of record och härledda kopior,
- Tjänsteidentitet,
- Observerbarhet för distribuerade tjänster.

Mönstren är byggstenar i resonemanget. Referensarkitekturen visar hur de kan kombineras i en större sammanhängande struktur.

Det betyder också att en referensarkitektur inte bör skapa nya namngivna mönster bara för att varje ruta i diagrammet behöver en etikett. Mönster bör finnas därför att problemet återkommer och erfarenheten är återanvändbar.

## Ett mönsterbibliotek behöver inträdeskrav

När en organisation börjar arbeta med mönster finns en risk att katalogen växer snabbt.

Varje teknikidé, kodkonvention eller favoritlösning får ett eget dokument. Då tappar mönsterbegreppet sin betydelse.

Ett kandidatobjekt bör därför prövas mot frågor som:

- Återkommer problemet i flera lösningar eller förmågor?
- Är problemet arkitekturellt snarare än bara implementeringsnära?
- Är lösningsidén tillräckligt stabil för att överleva produktbyten?
- Finns tydliga situationer där mönstret passar och inte passar?
- Finns verkliga avvägningar att förstå?
- Kan flera team använda beskrivningen som beslutsstöd?
- Är detta verkligen ett mönster och inte en standard, plattformstjänst eller teknisk instruktion?

Det ursprungliga underlaget till denna bok använder just denna typ av urval och har valt att inte skapa separata mönster för exempelvis varje återförsöksvariant, varje driftsättningsstrategi eller varje specifik åtkomstkontrollmodell.

Det är en sund återhållsamhet.

Ett litet och begripligt mönsterbibliotek är ofta mer användbart än en katalog med hundratals nästan överlappande poster.

## En praktisk mall för mönster

En mönsterbeskrivning behöver inte vara lång, men den bör innehålla tillräckligt mycket för att stödja ett verkligt beslut.

En användbar struktur kan vara:

### Namn

Ett kort och stabilt namn som fungerar i arkitekturdiskussioner.

### Syfte

Vilken övergripande effekt mönstret försöker åstadkomma.

### Kontext

I vilka situationer problemet brukar uppstå.

### Problem

Vilket återkommande problem som behöver lösas.

### Krafter

Vilka kvalitetskrav, begränsningar och motstridiga behov som påverkar valet.

### Struktur

Vilka roller eller komponenttyper som ingår och hur de relaterar.

### När det passar

Typiska indikatorer på att mönstret är relevant.

### När det inte passar

Situationer där mönstret sannolikt skapar mer kostnad än värde.

### Konsekvenser

Både positiva och negativa effekter.

### Variationer

Vilka delar som normalt måste anpassas till lokal kontext.

### Relaterade mönster

Vilka andra mönster som kompletterar, konkurrerar med eller förutsätts av detta.

### Berörda förmågor

Vilka gemensamma IT-förmågor som huvudsakligen påverkas.

### Realisering

Eventuella plattformstjänster eller standarder som kan hjälpa till att realisera mönstret, utan att blanda ihop dem med själva mönstret.

Denna struktur gör mönsterdokumentet till en **beslutsartefakt**, inte bara en teknisk beskrivning.

## Mönster behöver evidens från verkliga lösningar

Ett mönster bör helst inte uppstå enbart genom central arkitekturdesign.

Om ingen har använt lösningsformen finns ännu begränsad erfarenhet av dess konsekvenser.

Det innebär inte att organisationen aldrig kan dokumentera ett mönster proaktivt. Men mognadsgraden bör vara synlig.

En enkel livscykel kan vara:

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

Poängen är inte de exakta statusnamnen. Poängen är att mönsterbiblioteket ska **lära från verklig användning**.

Om återkommande avsteg visar att ett mönster är svårt att använda kan orsaken vara:

- att kontexten är för brett beskriven,
- att viktiga krafter saknas,
- att plattformsstödet är otillräckligt,
- att mönstret egentligen bara passar en smalare problemklass,
- att tekniska eller organisatoriska förutsättningar har förändrats.

Mönstret ska då förbättras, inte försvaras därför att det redan finns i katalogen.

## Mönster på de tre ansvarsnivåerna

Bokens tredelade ansvarmodell hjälper även här.

### Gemensam arkitekturnivå

Den gemensamma nivån bör främst äga **formen för mönsterarbetet**:

- definitionen av vad som räknas som lösningsmönster,
- gemensam dokumentationsstruktur,
- relationen till principer, standarder, plattformar och referensarkitekturer,
- katalogisering och sökbarhet,
- övergripande livscykelregler.

Den behöver inte detaljäga varje mönster.

### Förmågenivå

Förmågeansvariga är normalt bäst placerade att äga mönster inom sitt område eftersom de ser återkommande behov över flera lösningar.

De kan:

- identifiera kandidater,
- samla erfarenhet från användning,
- beskriva avvägningar,
- koppla mönster till plattformstjänster och standarder,
- förvalta variationer och rekommendationer.

Ett mönster som spänner över flera förmågor kan få gemensamt ägarskap, men ansvaret bör ändå vara explicit.

### Lösnings-/produktnivå

Lösningsteamet ansvarar för att bedöma om mönstret faktiskt passar den aktuella kontexten.

Teamet behöver kunna säga:

> Vi använder detta mönster därför att dessa krafter finns i vår lösning.

eller:

> Vi använder inte standardmönstret därför att vår kontext skiljer sig på följande sätt.

Det senare är inte automatiskt ett avsteg som måste stoppas. Det kan vara viktig återkoppling till mönsterbiblioteket.

## Mönster som gemensamt språk

Ett av de största värdena med mönster är inte dokumentationen i sig utan **språket** den skapar.

Om arkitekter, utvecklare och plattformsteam delar betydelsen av uttryck som:

- Backend for Frontend,
- Human workflow,
- System of record och härledda kopior,
- Cache-aside,
- Tjänsteidentitet,
- Build once, promote many,

kan en diskussion börja på en högre abstraktionsnivå.

I stället för att beskriva hela strukturen från början kan någon säga:

> Här verkar vi behöva en härledd sökrepresentation från system of record, men vi måste diskutera hur färsk kopian behöver vara.

Då har mönstret inte ersatt analysen. Det har gjort analysen effektivare.

Det är också därför mönsternamn måste användas konsekvent. Om samma namn betyder olika saker i olika delar av organisationen skapas bara en ny typ av begreppsförvirring.

## Mönster ska göra det lättare att säga nej

Ett väl beskrivet mönster hjälper inte bara till att välja en lösning. Det hjälper också till att **avstå**.

Om ett team föreslår en cache kan mönsterbeskrivningen för Cache-aside tvinga fram frågor som:

- Vilket problem löser cachen?
- Hur gammal får informationen bli?
- Vad händer vid cachemiss?
- Vem invalidaterar?
- Vad händer när cachen är otillgänglig?
- Är komplexiteten motiverad av ett faktiskt prestandabehov?

Om teamet inte kan besvara frågorna kan den bästa arkitekturen vara att inte införa cachen alls.

Detta är en viktig egenskap hos bra arkitekturstöd: det ska inte bara göra vissa lösningar enkla att välja. Det ska göra onödig komplexitet lättare att upptäcka.

## Från mönster till konkret lösning

När ett lösningsteam använder ett mönster behöver det fortfarande göra flera lokala val.

Exempelvis kan mönstret **Build once, promote many** ge den stabila idén:

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

Mönstret är ett lager i resonemanget – inte slutpunkten.

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

## De femton mönstren i bokens underlag

Det ursprungliga arkitekturmaterialet identifierar femton lösningsmönster:

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

1. **Formulera problemet utan mönsternamn.** Vad försöker vi faktiskt lösa?
2. **Beskriv kontexten.** Vilka domäner, användare, systemgränser och tekniska begränsningar finns?
3. **Identifiera krafterna.** Vilka kvalitetskrav och motstridiga behov driver beslutet?
4. **Jämför realistiska alternativ.** Är mönstret ett av flera möjliga svar?
5. **Kontrollera passform och antipassform.** Finns förutsättningarna som mönstret bygger på?
6. **Analysera konsekvenserna.** Vilken komplexitet och vilka nya felmoder introduceras?
7. **Identifiera variationerna.** Vad behöver anpassas lokalt?
8. **Koppla till gemensamma erbjudanden och standarder.** Finns plattformsstöd eller guardrails?
9. **Dokumentera varför mönstret används.** Mönsternamnet ersätter inte beslutets rationale.
10. **Återför erfarenheten.** Om mönstret inte fungerar som väntat ska biblioteket förbättras.

Denna ordning gör det svårare att börja med formuleringen ”vi ska använda mönster X” och först därefter leta efter problemet.

## Sammanfattning

Lösningsmönster är ett sätt att göra arkitekturerfarenhet återanvändbar utan att göra alla lösningar likadana.

Ett bra mönster beskriver:

- en återkommande kontext,
- ett verkligt arkitekturproblem,
- de krafter som behöver balanseras,
- en stabil lösningsstruktur,
- situationer där mönstret passar och inte passar,
- positiva och negativa konsekvenser,
- viktiga variationer,
- relationer till andra mönster, förmågor, plattformar och standarder.

Mönster är inte produkter, inte standarder, inte plattformstjänster och inte kompletta referensarkitekturer. De är **återanvändbara beslutserfarenheter**.

När de används rätt skapar de ett gemensamt språk och gör det möjligt för lösningsteam att börja med tidigare erfarenhet i stället för från ett tomt papper. När de används fel blir de recept, obligatoriska rutor i diagram eller nya former av central detaljstyrning.

Det är därför mönsterbibliotekets viktigaste kvalitet inte är storleken. Det är hur väl varje mönster hjälper läsaren att förstå **när en viss struktur är ett bra svar – och när den inte är det**.

I nästa kapitel går vi från mönsterbegreppet till den första gruppen konkreta mönster: **integrations- och kommunikationsmönster**, där tidskoppling, leveransbeteende, idempotens, ordering och kontraktsutveckling blir centrala delar av analysen.
