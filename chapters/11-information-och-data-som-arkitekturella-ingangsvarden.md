# 11. Information och data som arkitekturella ingångsvärden

Arkitektur börjar ofta prata om data för sent.

Först väljs en applikationsstruktur, sedan en integrationsmodell och därefter en lagringsmekanism. När dessa beslut väl är fattade upptäcker man att flera lösningar använder samma begrepp på olika sätt, att samma uppgift finns i flera varianter och att ingen riktigt vet vilken källa som är auktoritativ. Då försöker man lösa problemet tekniskt: med synkronisering, datalager, API:er, masterdataplattformar eller nya integrationsflöden.

Men problemet är ofta inte i första hand tekniskt.

Det handlar om att informationens mening, ansvar och livscykel inte har behandlats som arkitekturella ingångsvärden.

Detta kapitel flyttar därför fokus ett steg tillbaka. Innan vi frågar vilken databas, sökmotor eller lagringsmodell som ska användas behöver vi förstå:

- vilken information verksamheten behöver,
- vad centrala begrepp betyder,
- vem som äger betydelsen och kvaliteten,
- vilken källa som är auktoritativ,
- vilka kopior som får finnas och varför,
- hur information får delas mellan domäner,
- vilka uppgifter som behöver vara gemensamma,
- vilka som legitimt får ha olika betydelse i olika sammanhang,
- och vilka krav på klassning, retention och livscykel som följer med informationen.

Det är först därefter som den tekniska datahanteringen kan utformas på ett hållbart sätt.

## Information och data är inte samma fråga

Orden *information* och *data* används ofta som synonymer. För arkitekturarbete är det dock användbart att skilja dem åt.

Data är representationen: värden, attribut, dokument, meddelanden, poster och andra strukturer som kan lagras och överföras.

Information är den betydelse som dessa data får i ett sammanhang.

Ett datumfält med värdet `2026-08-18` är data. Om värdet betyder ansökningsdatum, beslutsdatum, giltighetsdatum eller senast verifierad tidpunkt är en informationsfråga.

På samma sätt kan en identifierare tekniskt vara en sträng på tolv tecken men verksamhetsmässigt representera helt olika saker: en person, ett ärende, en organisation, ett fordon eller ett externt avtal.

Skillnaden är viktig eftersom två system kan ha identiskt dataformat men ändå mena olika saker. Det omvända är också möjligt: samma information kan representeras på olika sätt i olika system.

En robust gemensam arkitektur behöver därför arbeta med båda perspektiven:

```text
Verksamhetsbegrepp och informationsbehov
                ↓
       informationsmodell
                ↓
   kontrakt och ansvar mellan domäner
                ↓
       teknisk datamodell
                ↓
 lagring, kopior, index, cache och arkiv
```

Om de tekniska modellerna kommer först riskerar representationen att börja styra betydelsen.

## Informationsbehov före datamodell

Kapitel 3 etablerade principen *behov före teknik*. Samma princip gäller inom dataområdet.

En vanlig men riskabel arbetsordning är:

1. välj databas eller plattform,
2. definiera tabeller och scheman,
3. exponera data via API,
4. försök därefter förklara vad fälten betyder.

En bättre ordning är att först fråga:

- vilka beslut ska kunna fattas med informationen?
- vilka verksamhetsprocesser använder den?
- vilka begrepp behöver vara gemensamt förstådda?
- vilken aktualitet krävs?
- vilken precision krävs?
- vem får ändra informationen?
- vem behöver kunna lita på den?
- hur länge behöver den finnas?
- vilka konsekvenser får felaktig eller gammal information?

Dessa frågor påverkar senare de tekniska valen, men de ska inte formuleras utifrån en viss teknik.

Om verksamheten exempelvis behöver kunna avgöra vilken adress som var gällande vid ett historiskt beslut är behovet inte ”en temporal tabell”. Behovet är att kunna återskapa vilket informationsläge som gällde vid en viss tidpunkt. Temporal modellering kan vara en realisering, men inte utgångspunkten.

På samma sätt är ”vi behöver Kafka-event” inte ett informationsbehov. Det kan finnas ett behov av att flera konsumenter får kännedom om en förändring med låg fördröjning och utan stark tidsmässig koppling till producenten. Eventbaserad kommunikation är då ett möjligt arkitekturval.

## Begrepp är en del av arkitekturen

Begreppsarbete betraktas ibland som dokumentation vid sidan av den tekniska arkitekturen. I själva verket är otydliga begrepp en vanlig källa till teknisk komplexitet.

Anta att tre system använder termen *ärende*.

I det första systemet betyder ärende en formell handläggningsinstans. I det andra betyder det ett inkommande kundärende. I det tredje betyder det en teknisk supportticket.

Om organisationen försöker skapa ett gemensamt API med ett generellt objekt `Case` kan resultatet bli en modell där egenskaper från tre olika betydelser blandas ihop. Modellen blir stor, svårtolkad och fylld av valfria attribut.

Problemet är då inte att API-designen varit dålig. Problemet är att organisationen försökt tvinga fram gemensam semantik där sådan inte fanns.

Begreppsarbete behöver därför svara på två olika frågor:

1. Vilka begrepp måste ha gemensam betydelse över flera domäner?
2. Vilka begrepp får legitimt betyda olika saker i olika bounded contexts?

Det första kan kräva gemensamma definitioner, referensdata eller kontrakt. Det andra kräver tydliga gränser och explicita översättningar.

Målet är inte en enda universell informationsmodell för hela organisationen. Målet är att skapa tillräckligt gemensam semantik där samverkan kräver det och tillräcklig lokal frihet där verksamhetskontexterna faktiskt skiljer sig.

## Informationsmodell och datamodell fyller olika funktioner

En informationsmodell beskriver typiskt verksamhetsmässiga begrepp och relationer utan att binda dem till en viss lagringsteknik.

En datamodell beskriver hur data struktureras i en viss teknisk kontext.

De två kan ligga nära varandra, men de bör inte blandas ihop.

En informationsmodell kan exempelvis uttrycka att:

- en organisation har ett eller flera verksamhetsställen,
- en fullmakt utfärdas av en part till en annan,
- ett beslut avser ett visst ärende,
- och ett tillstånd har en giltighetsperiod.

En teknisk datamodell behöver därefter lösa frågor som:

- hur identifierare representeras,
- hur relationer lagras,
- hur historik hanteras,
- hur null-värden tolkas,
- hur versionering sker,
- och hur indexering optimeras.

Om informationsmodellen och datamodellen hålls isär blir det lättare att förändra den tekniska realiseringen utan att verksamhetsbegreppen måste ändras samtidigt.

Det minskar också risken att en gammal databasstruktur blir organisationens de facto-definition av verksamheten.

## Informationsägarskap handlar om mandat

Kapitel 10 behandlade ägarskap som en del av domängränser. Här behöver vi gå ett steg djupare.

Informationsägarskap betyder inte bara att ett visst system råkar lagra en uppgift. Det handlar om mandat och ansvar för informationens betydelse och kvalitet.

Ett informationsägarskap kan behöva omfatta ansvar för:

- definitionen av informationen,
- regler för hur den skapas och ändras,
- krav på kvalitet och aktualitet,
- livscykel och gallring,
- klassning och åtkomstprinciper,
- vilka externa eller interna kontrakt som får exponera den,
- och hur förändringar i definitionen kommuniceras till konsumenter.

Det tekniska systemet som lagrar informationen kan förvaltas av ett annat team än det verksamhetsområde som äger betydelsen. Detta är inte ett problem så länge ansvarssnittet är tydligt.

Ett vanligt anti-pattern är däremot att informationsägarskap delegeras till den som råkar drifta databasen. Då får tekniska team fatta verksamhetsmässiga beslut om begrepp de inte äger.

Ett annat anti-pattern är att alla anses vara gemensamma ägare. I praktiken betyder det ofta att ingen har mandat att avgöra vad som gäller när definitioner kolliderar.

## System of record och auktoritativ källa

Begreppet *system of record* används för att beskriva ett system som är den auktoritativa källan för viss information.

Det betyder inte nödvändigtvis att:

- informationen bara får finnas där,
- alla läsningar måste gå direkt mot systemet,
- systemet måste ha den bästa sökfunktionen,
- eller systemet måste vara tekniskt centralt.

Det betyder att det finns en utsedd källa vars uppgift betraktas som normerande när flera representationer skiljer sig åt.

Det är därför användbart att skilja mellan:

- auktoritativ källa – den källa som äger sanningen för ett visst informationsområde,
- härledd kopia – data som replikerats eller transformerats för ett annat användningsfall,
- cache – temporär kopia för prestanda eller tillgänglighet,
- analytisk kopia – data som anpassats för rapportering eller analys,
- sökindex – representation optimerad för sökning,
- arkiv – representation som bevaras för historik eller regelkrav.

Arkitekturen behöver vara tydlig med vilken roll varje representation har.

Om en sökplattform exempelvis innehåller en kopia av kundinformation för att möjliggöra snabb fritextsökning bör den inte automatiskt bli den plats där kundinformationen ändras. Sökindexet är en härledd representation, inte den auktoritativa källan.

Detta låter enkelt men blir snabbt svårt i stora systemlandskap där data flyttats och kopierats under många år. Där kan ett viktigt arkitekturarbete vara att återetablera tydligt ägarskap och auktoritet, inte att försöka eliminera alla kopior.

## En uppgift kan ha flera legitima sanningar

Begreppet *single source of truth* används ofta som ideal. Det kan vara användbart, men det blir missvisande om det tolkas som att hela organisationen alltid ska ha exakt en fysisk representation av varje uppgift.

I verkligheten kan olika domäner behöva äga olika sidor av samma verklighet.

En personaldomän kan exempelvis vara auktoritativ för anställningsförhållandet. En identitetsplattform kan vara auktoritativ för tekniska identiteter och autentiseringsattribut. En behörighetsdomän kan vara auktoritativ för tilldelade roller. Dessa objekt kan vara relaterade till samma person men representerar olika ansvar.

Arkitekturen behöver därför fråga mer precist:

> För vilken information, i vilket sammanhang och vid vilken tidpunkt är denna källa auktoritativ?

Den precisionen är viktigare än sloganen att det bara ska finnas ”en sanning”.

## Masterdata och referensdata

Två informationskategorier som ofta blir gemensamma är masterdata och referensdata.

Masterdata beskriver relativt stabila kärnobjekt som används av flera processer eller system, exempelvis organisationer, personer, produkter, platser eller avtal – beroende på verksamhetens natur.

Referensdata beskriver i stället ofta tillåtna värdemängder eller klassifikationer, exempelvis landkoder, statuskoder, valuta, kategorier eller andra kodverk.

Gränsen är inte universell. Det viktiga är därför inte att klassificera varje informationsobjekt perfekt, utan att förstå när gemensam styrning behövs.

Frågor som kan motivera gemensamt ansvar är exempelvis:

- används samma information av många domäner?
- behöver betydelsen vara konsekvent mellan dem?
- uppstår kostsamma fel när olika kopior divergerar?
- finns en tydlig auktoritativ källa?
- finns krav på gemensam klassifikation eller rapportering?
- behöver förändringar distribueras kontrollerat?

Ett vanligt misstag är att skapa en central masterdataplattform innan ansvar och semantik är tydliga. Plattformen kan då bara centralisera den tidigare otydligheten.

Teknik kan inte ersätta informationsgovernance.

## Data contracts – gränssnitt för information

När information passerar en domängräns behövs ett explicit kontrakt.

Ett datakontrakt kan beskrivas som en överenskommelse mellan producent och konsument om hur data exponeras och vilka egenskaper konsumenten får förlita sig på.

Kontraktet kan omfatta mer än bara schema.

Det kan exempelvis beskriva:

- semantik och definitioner,
- fälttyper och format,
- obligatoriska och valfria attribut,
- identifierare,
- versionshantering,
- kompatibilitetsregler,
- aktualitet och uppdateringsfrekvens,
- kvalitetsnivåer,
- klassning och åtkomstbegränsningar,
- ägarskap och kontaktvägar,
- samt hur förändringar och avveckling kommuniceras.

Det gör datakontrakt till en nära släkting till API-kontrakt och eventkontrakt, men med tydligare fokus på den information som konsumeras.

Poängen är inte att varje intern tabell ska bli ett formellt avtal. Poängen är att information som används över en ansvargräns inte bör vara beroende av outtalade antaganden.

Ett dåligt kontrakt kan exempelvis säga:

> `status` är en sträng.

Ett användbart kontrakt behöver också klargöra vad status betyder, vilka värden som kan förekomma, vem som bestämmer dem, om nya värden kan läggas till och hur konsumenten förväntas reagera på okända värden.

Det är där semantik möter tekniskt gränssnitt.

## Informationsklassning påverkar arkitektur tidigt

Informationens egenskaper påverkar vilka tekniska lösningar som är möjliga och lämpliga.

Därför behöver informationsklassning ske tidigt nog för att påverka arkitekturen.

Beroende på organisation och regelverk kan klassningen exempelvis behöva bedöma konsekvenser för:

- konfidentialitet,
- riktighet,
- tillgänglighet,
- spårbarhet,
- personuppgiftshantering,
- sekretess,
- bevarande,
- eller andra rättsliga och verksamhetsmässiga krav.

Klassningen ska inte ses som en etikett som läggs på i slutet av projektet. Den kan påverka:

- var information får lagras,
- vilka tjänster som får behandla den,
- hur åtkomst kontrolleras,
- vilka loggar som får innehålla den,
- hur säkerhetskopior hanteras,
- om information får lämna en viss miljö,
- och vilka krav som ställs på återställning och incidenthantering.

Samma plattformstjänst kan därför behöva erbjuda olika profiler beroende på vilken information som behandlas.

Detta är ett tydligt exempel på varför kvalitetskrav och informationsbehov måste komma före teknikvalet.

## Information har en livscykel

Data betraktas ofta som något som bara ackumuleras. Men information har en livscykel.

Den kan:

1. skapas eller tas emot,
2. verifieras,
3. ändras,
4. användas i operativa processer,
5. delas med andra,
6. ersättas av nyare information,
7. arkiveras,
8. gallras eller raderas,
9. och i vissa fall behöva kunna återskapas som den såg ut vid en tidigare tidpunkt.

Dessa steg är inte bara lagringsfrågor.

De påverkas av verksamhetsregler, rättsliga krav, informationsägarskap och behov av spårbarhet.

Om ett beslut exempelvis baserades på en viss uppgift behöver organisationen ibland kunna förstå vilken version av uppgiften som användes. Det kan kräva historik även om den aktuella verksamhetsprocessen bara behöver dagens värde.

På motsvarande sätt kan ”spara allt för säkerhets skull” vara lika problematiskt som att radera för tidigt. Onödig information ökar kostnader, komplexitet, säkerhetsrisk och ansvar.

Retention bör därför vara ett medvetet informationsbeslut som sedan realiseras tekniskt, inte en bieffekt av att lagringsutrymmet är billigt.

## Kopior är inte automatiskt ett arkitekturfel

I distribuerade system är det ofta nödvändigt att kopiera data.

Kopior kan behövas för:

- analys,
- sökning,
- cache,
- lokal autonomi,
- motståndskraft,
- integration,
- rapportering,
- historik,
- eller för att minska belastningen på en auktoritativ källa.

Problemet är därför inte att kopior finns.

Problemet uppstår när organisationen inte vet:

- vilken kopia som är auktoritativ,
- hur färsk en kopia förväntas vara,
- hur den uppdateras,
- om den får ändras lokalt,
- vilka konsumenter som använder den,
- och vad som händer när den avviker från källan.

En användbar arkitektur gör dessa egenskaper explicita.

```text
Auktoritativ källa
       │
       ├── operativ kopia
       ├── sökindex
       ├── analytisk kopia
       └── arkiv/historik
```

Varje gren har ett syfte och ett ansvar.

Kapitel 15 kommer att fördjupa hur sådana kopior, cachemekanismer, historik och konsistensmodeller kan realiseras tekniskt. Här räcker det att etablera att beslutet om varför en kopia finns och vilken roll den har måste tas innan tekniken väljs.

## Gemensam informationsmodell eller federerad semantik?

En central fråga för större organisationer är hur långt den gemensamma informationsmodellen bör sträcka sig.

Det finns två ytterligheter.

Den ena är att varje system definierar sina begrepp själv. Det ger lokal frihet men skapar hög integrationskostnad och risk för semantisk fragmentering.

Den andra är att försöka skapa en enda fullständig organisationsgemensam modell som alla måste följa. Det kan skapa konsistens men riskerar att bli tungstyrt, långsamt och dåligt anpassat till domänspecifika behov.

Mellan dessa ytterligheter finns en mer praktisk modell: federerad semantik.

Den innebär att:

- vissa kärnbegrepp och kodverk styrs gemensamt,
- domäner äger sin lokala modell,
- betydande skillnader mellan kontexter görs explicita,
- integration sker via tydliga kontrakt,
- och gemensamma definitioner skapas där faktisk interoperabilitet kräver dem.

Det ligger nära bokens övergripande ansvarmodell.

Gemensam nivå bör inte försöka äga all information. Den bör äga de spelregler, gemensamma begrepp och kontraktsprinciper som krävs för att flera domäner ska kunna samverka.

Domänerna bör äga sin verksamhetsnära semantik.

Lösningar och produkter realiserar dessa modeller tekniskt.

## De tre ansvarsnivåerna i informationsarkitekturen

Bokens tredelade ansvarmodell kan tillämpas direkt på information och data.

### Gemensam nivå

Den gemensamma nivån bör normalt hantera sådant som behöver vara konsekvent över flera domäner, exempelvis:

- övergripande informationsprinciper,
- gemensamma klassningsprinciper,
- gemensamma identifieringsprinciper där det behövs,
- gemensamma referensdata och kodverk,
- kontraktsprinciper för datautbyte,
- gemensamma krav på metadata, spårbarhet och livscykel,
- samt metoder för att beskriva auktoritativa källor och ägarskap.

Den bör däremot vara försiktig med att skapa en enda detaljerad datamodell för hela organisationen.

### Förmågenivå

Förmågeansvariga behöver omsätta de gemensamma principerna till återanvändbara mekanismer och tjänster.

Det kan exempelvis innebära:

- plattformstjänster för relationsdata, objektlagring eller sökning,
- mönster för system of record och härledda kopior,
- standarder för schema- och kontraktshantering,
- tjänster för master- eller referensdata där sådana faktiskt behövs,
- datakataloger och metadatafunktioner,
- eller vägledning för retention och historik.

Förmågeområdet ska dock inte ta över verksamhetsdomänens ansvar för vad informationen betyder.

### Lösnings-/produktnivå

Lösningsteamet behöver:

- identifiera vilka informationsobjekt lösningen använder,
- följa domänens begrepp och ägarskap,
- definiera konkreta datamodeller,
- använda rätt gemensamma kontrakt och plattformstjänster,
- dokumentera lokala kopior och deras roll,
- och säkerställa att klassning och livscykel realiseras i den tekniska lösningen.

Det är här informationsarkitektur blir konkret systemdesign.

## Vanliga anti-patterns

Flera återkommande mönster tyder på att information inte behandlats som ett arkitekturellt ingångsvärde.

### Databasen definierar verksamheten

Gamla tabellnamn och kolumner används som organisationsgemensamma begrepp eftersom databasen råkar vara äldst.

Konsekvensen blir att teknisk historik styr verksamhetens språk.

### Gemensam modell utan gemensam mening

Organisationen skapar ett centralt kanoniskt informationsobjekt som försöker rymma alla domäners varianter.

Resultatet blir ofta hundratals attribut, komplexa regler och otydliga ansvar.

### Alla kopior blir nya sanningar

En lokal kopia skapas för analys eller prestanda men börjar senare uppdateras lokalt. Efter några år vet ingen längre vilken källa som gäller.

### Ägarskap följer lagringsplats

Det team som driver databasen förväntas avgöra verksamhetsmässiga definitioner eftersom informationen tekniskt ligger där.

### Klassning sker efter implementation

Först efter att systemet är byggt upptäcks att viss information inte får hanteras på den valda plattformen eller i den valda loggningen.

### ”Single source of truth” blir ”single point of dependency”

Alla konsumenter tvingas läsa synkront från samma system även när deras behov gäller sökning, analys eller lokal tillgänglighet. Ett informationsprincipbeslut förväxlas med en teknisk distributionsmodell.

### Data lake som semantisk lösning

Data samlas centralt men utan tydligt ansvar, gemensamma definitioner eller kvalitetskrav. Resultatet blir fler kopior men inte bättre förståelse.

Gemensamt för dessa anti-patterns är att teknik används för att maskera otydligt ansvar och otydlig mening.

## En praktisk analysordning

När ett nytt lösningsområde analyseras kan informationsfrågorna hanteras i en ungefärlig ordning.

### 1. Identifiera centrala informationsobjekt

Vilka objekt, dokument, händelser och begrepp är avgörande för verksamhetsbehovet?

### 2. Beskriv mening och kontext

Vad betyder varje begrepp och inom vilket sammanhang gäller definitionen?

### 3. Identifiera ägarskap

Vem har mandat att definiera och förändra informationen?

### 4. Identifiera auktoritativ källa

Var skapas eller fastställs den normerande versionen?

### 5. Identifiera konsumenter och gränser

Vilka andra domäner behöver informationen och genom vilka kontrakt bör den delas?

### 6. Fastställ kvalitets- och klassningskrav

Vilken aktualitet, riktighet, spårbarhet, konfidentialitet och tillgänglighet krävs?

### 7. Beskriv livscykeln

Hur skapas, ändras, historiseras, arkiveras och gallras informationen?

### 8. Först därefter – välj tekniska mekanismer

När dessa frågor är tydliga kan lösningen bedöma relationsdatabas, dokumentlagring, objektlagring, event, cache, sökindex, analytiska kopior och andra mekanismer.

Denna ordning är inte ett vattenfall. Informationens tekniska realisering kan ge ny förståelse som gör att tidigare antaganden behöver justeras. Men den hjälper organisationen att undvika att börja i fel ände.

## Från informationsproblem till förmågebehov

När återkommande informationsproblem analyseras på detta sätt börjar också behov av gemensamma IT-förmågor bli synliga.

Om många domäner exempelvis behöver:

- hantera stora dokument,
- söka över härledda kopior,
- lagra relationsdata med backup och återställning,
- hantera gemensamma kodverk,
- distribuera förändringar som events,
- eller lagra historik med tydlig retention,

är det inte nödvändigtvis ett tecken på att alla ska använda samma applikation.

Det kan i stället vara ett tecken på att organisationen behöver gemensamma data- och informationshanteringsförmågor, integrationsförmågor och plattformstjänster.

Här möts del II och del III i boken.

Domän- och informationsanalysen beskriver vad som behöver vara sant om informationen. Förmågemodellen beskriver vilket återanvändbart stöd organisationen behöver kunna erbjuda för att göra detta möjligt.

## Sammanfattning

Information och data är inte bara något som lagras efter att arkitekturen redan har bestämts. De är ingångsvärden till arkitekturen.

Ett hållbart arbetssätt börjar med att förstå:

- informationens mening,
- begrepp och kontext,
- ägarskap,
- auktoritativ källa,
- kontrakt mellan domäner,
- klassning,
- kvalitet,
- och livscykel.

Först därefter bör tekniska beslut om lagring, kopior, cache, historik och konsistens tas.

Det innebär också att en organisation inte behöver välja mellan full centralisering och total lokal frihet. Gemensamma begrepp och referensdata kan styras där gemensam semantik faktiskt behövs, samtidigt som domäner behåller ansvar för sin lokala modell. Explicita datakontrakt kan därefter göra informationsutbyte begripligt och förändringsbart.

Det centrala arkitekturbudskapet är därför:

> Data ska inte först göras gemensamma och sedan ges en mening. Mening, ansvar och livscykel behöver vara tydliga innan data delas, lagras och tekniskt standardiseras.

Med denna grund på plats kan boken nu gå vidare från de övergripande frågorna om förmågor, domäner och information till de konkreta gemensamma IT-förmågor som ett stödjande IT-område behöver kunna erbjuda.
