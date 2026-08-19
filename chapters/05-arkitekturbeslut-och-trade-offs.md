# 5. Arkitekturbeslut och avvägningar

Arkitektur handlar sällan om att hitta ett alternativ som är bäst i alla avseenden. Ofta finns flera lösningar som skulle fungera, men de fungerar bra på olika sätt. En lösning kan ge hög förändringstakt men större operativ komplexitet. En annan kan vara enklare att drifta men ge svagare isolering mellan verksamhetsdelar. En tredje kan vara billigast att införa men svårare att lämna senare.

Det arkitektoniska arbetet består därför inte bara i att beskriva en målbild. Det består också i att göra **medvetna val mellan konkurrerande egenskaper**, tydliggöra varför valet gjordes och göra det möjligt att ompröva beslutet när förutsättningarna förändras.

Ett arkitekturbeslut behöver kunna besvara åtminstone fyra frågor:

1. Vilket problem eller behov försöker vi lösa?
2. Vilka realistiska alternativ övervägde vi?
3. Vilka konsekvenser och avvägningar innebär alternativen?
4. Varför är det valda alternativet rimligt i just denna kontext?

Det är först när dessa frågor är synliga som arkitekturen blir spårbar som **beslutslogik**, inte bara som ett tillstånd i ett diagram.

Detta kapitel behandlar hur arkitekturbeslut kan göras explicita, jämförbara och omprövningsbara. Fokus ligger på själva beslutets form och resonemang. Hur organisationen ger mandat, hanterar avsteg och förvaltar styrningen över tid behandlas senare i boken.

## Arkitektur är val under begränsningar

I kapitel 3 skilde vi mellan behov, begränsningar och teknikval. I kapitel 4 såg vi hur kvalitetsattribut gör vissa egenskaper arkitekturdrivande. Tillsammans skapar de beslutsrymmet.

En förenklad bild är:

```text
Behov och mål
      +
Kvalitetskrav
      +
Begränsningar
      ↓
Realistiska alternativ
      ↓
Avvägningar och risker
      ↓
Arkitekturbeslut
      ↓
Konsekvenser och uppföljning
```

Det viktiga ordet är **realistiska**. Arkitekturval görs aldrig i ett vakuum. Organisationen kan redan ha investerat i plattformar, kompetens, avtal, driftsmodeller och säkerhetsmekanismer. Lagstiftning, informationsklassning eller externa integrationskrav kan begränsa möjliga alternativ. Tid, budget och tillgång till kompetens gör detsamma.

Men begränsningar ska avgränsa beslutsrymmet – inte ersätta beslutsanalysen.

Om organisationen redan har en containerplattform är det ett relevant faktum. Det betyder däremot inte automatiskt att varje ny applikation bör köras där. Frågan är fortfarande om plattformens egenskaper möter lösningens behov bättre än alternativen, givet kostnad, risk och långsiktiga konsekvenser.

## Ett arkitekturbeslut är mer än ett teknikval

Uttrycket arkitekturbeslut associeras lätt med val som:

- PostgreSQL eller en annan databas,
- synkron API-kommunikation eller asynkrona meddelanden,
- container eller virtuell maskin,
- centralt workflow eller egen processlogik.

Sådana beslut kan vara arkitekturella, men tekniken i sig avgör inte om beslutet är ett arkitekturbeslut.

Ett beslut är arkitekturellt när det har **betydande och svårreversibla konsekvenser** för struktur, kvaliteter, ansvar, beroenden eller framtida handlingsutrymme.

Exempel kan vara:

- att göra en viss tjänst till system of record för en informationsmängd,
- att låta flera domäner dela samma datamodell,
- att standardisera på händelsedriven integration för en viss klass av flöden,
- att lägga verksamhetsregler i en gemensam regelplattform,
- att kräva att tjänster är stateless i exekveringslagret,
- att centralisera identitetsfederation i ett gemensamt erbjudande,
- att acceptera leverantörsspecifika funktioner för att få högre produktivitet.

Ett litet bibliotek som kan bytas på en eftermiddag behöver sällan ett formellt arkitekturbeslut. Ett val som påverkar ett tiotal system under fem år gör det ofta.

Det är därför praktiskt att bedöma beslut efter bland annat:

- **räckvidd** – hur många lösningar eller team påverkas,
- **livslängd** – hur länge beslutet förväntas gälla,
- **reversibilitet** – hur dyrt eller svårt det är att ändra,
- **kvalitetspåverkan** – vilka viktiga kvalitetsattribut som påverkas,
- **beroenden** – vilka organisatoriska eller tekniska låsningar som skapas,
- **risk** – vad konsekvensen blir om antagandet bakom beslutet visar sig felaktigt.

Ju högre dessa faktorer är, desto större värde finns i att göra beslutet explicit.

## Det finns nästan alltid flera dimensioner samtidigt

Ett vanligt misstag är att jämföra alternativ längs en enda axel.

Anta att en organisation behöver välja hur en ny integrationsström ska byggas. Ett alternativ är synkrona API-anrop och ett annat är asynkron meddelandehantering.

Det är lätt att fråga:

> Vilket alternativ är mest robust?

Men robusthet är bara en dimension. Valet påverkar också:

- svarstider,
- koppling i tid mellan systemen,
- felhantering,
- observerbarhet,
- dataordning,
- utvecklingskomplexitet,
- testbarhet,
- kompetensbehov,
- driftansvar,
- felsökning,
- användarupplevelse.

Den asynkrona lösningen kan tåla att mottagaren tillfälligt är nere, men den introducerar samtidigt frågor om idempotens, ordering, dead-letter-hantering och korrelation. Det synkrona alternativet kan vara enklare att förstå men skapa hårdare beroende mellan tillgängligheten i två tjänster.

Arkitektens uppgift är därför inte att hitta den egenskap där ett alternativ är starkast, utan att förstå **vilken kombination av egenskaper som bäst motsvarar den prioriterade kravbilden**.

## Avvägning betyder inte kompromiss i negativ mening

Ordet kompromiss kan ge intrycket att arkitekturen blir sämre än den borde vara. Avvägning är ett mer precist sätt att tänka.

En avvägning innebär att förbättring av en egenskap kan ha kostnader eller konsekvenser för andra egenskaper.

Exempel:

- mer isolering kan ge högre kostnad och större operativ komplexitet,
- mer återanvändning kan ge starkare koppling mellan konsumenter,
- strikt standardisering kan ge lägre variationskostnad men minska lokalt handlingsutrymme,
- mer cache kan ge bättre svarstid men svårare konsistenshantering,
- fler distribuerade tjänster kan ge självständigare leverans men öka behovet av observerbarhet och robust integration,
- stark portabilitet kan minska leverantörslåsning men hindra användning av värdefulla plattformsspecifika funktioner,
- mer detaljerad auditloggning kan öka spårbarheten men också kostnad, datavolym och integritetsrisk.

Det finns alltså sällan en arkitektur som maximerar alla kvaliteter samtidigt.

Det gör prioriteringen från föregående kapitel central. Om organisationen inte vet vilka kvaliteter som är viktigast blir avvägning-diskussionen lätt en kamp mellan personliga teknikpreferenser.

## Gör beslutskriterierna synliga före valet

Ett effektivt sätt att förbättra beslutsprocessen är att formulera kriterierna innan alternativet väljs.

Anta att tre tekniska realiseringar övervägs för en dokumenttjänst. I stället för att först välja favorit och sedan motivera den kan teamet definiera kriterier som:

- klarar informationsklassningen,
- möter återställningskraven,
- stödjer den förväntade datavolymen,
- kan integreras med organisationens identitetsmodell,
- har en rimlig förvaltningskostnad,
- kan bemannas med tillgänglig kompetens,
- kan införas inom önskad tid,
- ger acceptabel exit-kostnad.

Det går sedan att jämföra alternativen mot samma frågor.

Det betyder inte att arkitektur bör reduceras till ett kalkylblad där det alternativ som får flest poäng automatiskt vinner. Vissa krav är absoluta. Vissa risker är asymmetriska. Vissa kvaliteter är svåra att mäta numeriskt. Och en viktning kan skapa falsk precision.

Men explicita kriterier gör resonemanget synligt och minskar risken att beslutet i praktiken bygger på:

- vana,
- organisatorisk prestige,
- leverantörspresentationer,
- senaste tekniktrenden,
- en stark individs preferens,
- det som råkar vara enklast just denna sprint.

## Skilj på krav, preferenser och hypoteser

När alternativ utvärderas är det användbart att skilja mellan tre typer av påståenden.

### Krav

Ett krav behöver uppfyllas eller hanteras som ett medvetet avsteg eller accepterad risk.

Exempel:

> Lösningen måste kunna återställas inom den fastställda RTO:n.

### Preferens

En preferens är önskvärd men kan vägas mot andra egenskaper.

Exempel:

> Vi föredrar en teknik som redan stöds av befintlig plattformsorganisation.

### Hypotes

En hypotes är ett antagande om framtiden eller om hur ett alternativ kommer att bete sig.

Exempel:

> Vi bedömer att datamängden kommer att tredubblas inom tre år.

Hypoteser är särskilt viktiga eftersom många arkitekturbeslut bygger på dem utan att det sägs högt.

Om ett beslut bygger på att belastningen sannolikt aldrig överstiger en viss nivå bör det dokumenteras. Om den nivån senare förändras vet organisationen då *varför* arkitekturen behöver omprövas.

## Architecture Decision Records

Ett vanligt sätt att dokumentera arkitekturbeslut är ett **Architecture Decision Record**, ofta förkortat ADR.

Grundidén är enkel: varje betydelsefullt beslut får en liten, självständig beslutsnotering som bevarar kontexten och resonemanget.

En ADR kan exempelvis innehålla:

```text
Titel
Status
Kontext/problem
Beslutsdrivare
Övervägda alternativ
Beslut
Konsekvenser
Antaganden och risker
Datum och ansvar
Villkor för omprövning
```

Det finns flera etablerade ADR-format, och organisationen behöver inte låsa sig vid en viss mall. Det viktigaste är att noteringen hjälper en framtida läsare förstå beslutet.

En svag beslutsnotering säger:

> Vi använder produkt X som databas.

En bättre notering förklarar:

> Tjänsten behöver transaktionell konsistens mellan de centrala informationsobjekten, etablerad backup/restore enligt den definierade kontinuitetsprofilen och stöd från befintlig driftorganisation. Tre alternativ utvärderades. Produkt X valdes eftersom den möter de prioriterade kraven och redan erbjuds som förvaltad databastjänst. Beslutet innebär samtidigt beroende av plattformens versionscykel och vissa leverantörsspecifika driftmekanismer.

Den andra texten gör två saker som den första saknar: den beskriver **varför** valet gjordes och **vilka konsekvenser** som accepterades.

## ADR är beslutshistorik, inte dokumentationsritual

Det är lätt att göra ADR till ännu en obligatorisk mall. Då riskerar man att skapa hundratals dokument som ingen använder.

ADR ger störst värde för beslut som är:

- betydelsefulla,
- svåra att förstå i efterhand,
- kontroversiella eller innehåller tydliga avvägningar,
- beroende av antaganden som kan ändras,
- svåra eller kostsamma att reversera,
- viktiga för flera team eller framtida förvaltare.

För mindre beslut kan kod, konfiguration eller vanlig teknisk dokumentation räcka.

Principen bör vara:

> Dokumentera beslut där **förlusten av beslutslogiken** skulle vara kostsam.

Det är en bättre styrsignal än att försöka definiera exakt vilka tekniktyper som alltid måste få en ADR.

## Status gör beslutets livscykel begriplig

Arkitekturbeslut är inte eviga sanningar. En enkel statusmodell hjälper till att skilja aktuella beslut från historik.

Exempel:

- **Föreslaget** – alternativet diskuteras men är inte beslutat.
- **Accepterat** – beslutet gäller.
- **Ersatt** – ett senare beslut har tagit dess plats.
- **Utgånget** – beslutet är inte längre relevant.

I vissa organisationer kan ytterligare statusar behövas, men för många räcker en enkel modell.

Det viktiga är att inte skriva om historiken så att det ser ut som om organisationen alltid tänkte som den gör idag. Ett äldre beslut kan ha varit helt rimligt när det fattades även om det senare ersatts.

Den historiken är värdefull. Den visar vilka antaganden som ändrades och hjälper organisationen undvika att återupprepa samma diskussion utan ny information.

## Konsekvenser måste dokumenteras, även de negativa

En beslutsnotering som bara beskriver fördelar är ofta ett tecken på att beslutet redan var emotionellt taget innan analysen började.

Varje arkitekturbeslut bör försöka synliggöra både positiva och negativa konsekvenser.

Anta att en organisation väljer en gemensam managed LLM-tjänst i stället för att låta varje team integrera direkt med valfri modellleverantör.

Positiva konsekvenser kan vara:

- gemensam säkerhets- och avtalsmodell,
- central kostnadsuppföljning,
- enhetlig loggning,
- lägre integrationskostnad för konsumenterna.

Negativa konsekvenser kan vara:

- långsammare tillgång till vissa nya modellfunktioner,
- beroende av den gemensamma plattformens prioriteringar,
- risk att ett gemensamt API döljer viktiga leverantörsspecifika möjligheter,
- större konsekvens om den gemensamma tjänsten får problem.

Att skriva ned nackdelarna gör inte beslutet svagare. Det gör det ärligare och skapar underlag för framtida uppföljning.

## Riskacceptans är också ett beslut

Ibland finns inget alternativ som uppfyller alla krav inom tillgänglig tid och budget. Organisationen kan då behöva acceptera en risk.

Det viktiga är att riskacceptansen inte blir osynlig.

Exempel:

> Den första versionen saknar automatisk failover mellan två datacenter. Den beräknade återställningstiden kan därför överskrida önskad nivå vid ett fullständigt datacenterbortfall. Risken accepteras för lansering eftersom verksamheten kan använda manuellt reservförfarande under den begränsade införandeperioden. Beslutet ska omprövas före nästa expansionsfas.

Det är bättre än att låta arkitekturdokumentationen ge sken av att kvalitetskravet är uppfyllt.

Riskacceptans bör göra åtminstone följande synligt:

- vilken risk som accepteras,
- varför den accepteras,
- vilken konsekvens den kan få,
- vilka kompensatoriska åtgärder som finns,
- vem som har mandat att acceptera den,
- när den ska omprövas.

Mandatfrågan hör organisatoriskt hemma i governance, som behandlas senare. Men själva riskresonemanget är en del av arkitekturbeslutet.

## Teknisk skuld kan vara medveten

Teknisk skuld beskrivs ofta som något som bara uppstår när utvecklare tar genvägar. Det är för snävt.

En organisation kan medvetet välja en lösning som är billigare eller snabbare idag trots att den skapar en framtida kostnad. Det kan vara rationellt.

Exempel:

- en temporär punkt-till-punkt-integration för att klara en tidskritisk migrering,
- en äldre runtime som behålls tills en större modernisering genomförs,
- manuella driftsmoment under en pilotperiod,
- begränsad redundans i en tjänst som ännu har låg verksamhetskritikalitet.

Problemet uppstår när den framtida kostnaden inte längre är synlig.

En medveten arkitekturell skuld bör därför dokumenteras med:

- varför skulden tas,
- vilken konsekvens den har,
- vilka signaler som visar att den behöver lösas,
- eventuell tidsgräns eller omprövningspunkt.

Då blir skulden en del av den strategiska beslutsportföljen i stället för ett dolt problem.

## Beslut behöver omprövningsvillkor

En av de mest värdefulla uppgifterna i en beslutsnotering är ofta **när beslutet inte längre ska betraktas som självklart**.

Det behöver inte vara ett kalenderdatum. Omprövning kan triggas av händelser.

Exempel:

- när antalet konsumenter överstiger 20,
- när datavolymen passerar en viss nivå,
- när aktuell produktversion lämnar support,
- när ett regulatoriskt krav förändras,
- när plattformen erbjuder en tidigare saknad funktion,
- när kostnaden når en definierad gräns,
- när en ny verksamhetskritikalitet kräver en högre kontinuitetsprofil.

Detta gör arkitekturen adaptiv.

I stället för:

> Detta är vår arkitektur.

blir budskapet:

> Detta är den arkitektur vi bedömer som lämplig under dessa förutsättningar.

Det är en viktig skillnad.

## Reversibilitet bör påverka hur mycket analys som görs

Alla beslut förtjänar inte samma analysinsats.

Ett användbart tankesätt är att skilja mellan beslut som är relativt enkla att ändra och beslut som är dyra att reversera.

För ett lätt reversibelt beslut är det ofta bättre att:

1. göra en rimlig bedömning,
2. välja,
3. mäta resultatet,
4. ändra om utfallet blir dåligt.

För ett svårreversibelt beslut bör organisationen i stället investera mer i:

- alternativanalys,
- prototyper,
- belastningstest,
- säkerhetsanalys,
- migreringsstrategi,
- exit-planering,
- oberoende granskning.

Det innebär att beslutsprocessen bör vara **proportionerlig mot konsekvensen av att ha fel**.

Det är särskilt viktigt i gemensam IT-arkitektur. Ett beslut som bara påverkar en lösning kan vara relativt enkelt att korrigera. Ett gemensamt plattformsbeslut som hundra system bygger på kan skapa mycket stor framtida tröghet.

## Beslut på olika nivåer

Bokens tredelning mellan gemensam nivå, förmågenivå och lösnings-/produktnivå är också användbar för arkitekturbeslut.

### Gemensam arkitekturnivå

Här hör beslut hemma som behöver vara konsekventa över flera förmågor eller lösningar.

Exempel:

- vilken övergripande identitetsmodell organisationen använder,
- hur tekniska standarder klassificeras,
- vilka kvalitetsdimensioner som ska användas gemensamt,
- vilken princip som gäller för produkt kontra stabil arkitektur,
- hur tvärgående informationsutbyte ska hanteras.

Gemensamma beslut bör vara relativt få men ha hög räckvidd.

### Förmågenivå

Här fattas beslut om hur ett visst stödjande område ska fungera och vilka erbjudanden det ska tillhandahålla.

Exempel inom Integration och kommunikation kan vara:

- vilka integrationsstilar plattformen ska stödja,
- när API management ska vara standardvägen,
- vilka messaging-egenskaper som erbjuds,
- vilka kontrakts- och versionsregler som gäller inom området.

Förmågebeslut ska ligga inom de gemensamma ramarna men får vara betydligt mer tekniskt konkreta.

### Lösnings-/produktnivå

Här fattas beslut för ett specifikt verksamhetsbehov.

Exempel:

- om just denna integration ska vara synkron eller asynkron,
- hur just denna tjänst partitionerar sin data,
- vilken kontinuitetsprofil lösningen behöver,
- hur en viss domän delas upp i komponenter.

Det är viktigt att beslut inte lyfts högre än nödvändigt. Ett lokalt val ska inte göras till organisationsstandard bara för att det fungerade i ett projekt.

Det omvända gäller också: ett beslut som skapar beroenden för många team bör inte döljas som ett lokalt implementationsval.

## Ett konkret exempel: delad databas eller separata dataägarskap

Anta att två verksamhetstjänster behöver arbeta med närliggande information.

### Alternativ A: gemensam databas och gemensamt schema

Möjliga fördelar:

- enkel åtkomst till gemensam data,
- transaktioner över flera tabeller är enkla,
- färre integrationsmekanismer,
- lägre initial komplexitet.

Möjliga nackdelar:

- stark koppling mellan tjänsternas datamodeller,
- svårare självständig förändring,
- otydligt dataägarskap,
- risk att direkt databasåtkomst ersätter definierade kontrakt.

### Alternativ B: separata dataägarskap och definierad integration

Möjliga fördelar:

- tydligare ansvar,
- bättre självständig förändringsbarhet,
- explicita kontrakt,
- möjlighet att skala eller lagra data olika.

Möjliga nackdelar:

- distribuerad konsistens måste hanteras,
- mer integrationslogik,
- större observerbarhetsbehov,
- högre initial komplexitet.

Vilket alternativ är rätt?

Det går inte att avgöra utan sammanhang.

Om funktionerna i praktiken tillhör samma sammanhållna domän, förändras tillsammans och kräver stark transaktionell konsistens kan en gemensam datamodell vara rimlig. Om de har olika ägare, olika förändringstakt och tydliga domängränser kan separata dataägarskap vara viktigare.

Avvägning-analysen gör alltså inte beslutet automatiskt. Den gör **orsakerna till beslutet synliga**.

## Undvik falsk precision i beslutsmatriser

Beslutsmatriser kan vara användbara. Ett team kan ge varje alternativ bedömningen låg, medel eller hög mot ett antal kriterier. Man kan även använda viktning.

Men det finns en risk att en tabell med siffror ger sken av objektivitet som egentligen inte finns.

Exempel:

| Kriterium | Vikt | Alternativ A | Alternativ B |
|---|---:|---:|---:|
| Tillgänglighet | 5 | 4 | 5 |
| Förvaltningskostnad | 3 | 5 | 3 |
| Portabilitet | 2 | 2 | 5 |

Att multiplicera och summera dessa siffror kan hjälpa diskussionen, men resultatet är inte en naturvetenskaplig sanning. Både vikter och poäng bygger på bedömningar.

En beslutsmatris bör därför användas som **samtals- och analysverktyg**, inte som en maskin som fattar beslutet.

Särskilt absoluta krav måste hanteras separat. Ett alternativ som inte klarar ett nödvändigt informationsskyddskrav ska inte kunna vinna genom att samla fler poäng på lägre kostnad och bättre utvecklarupplevelse.

## Prototyper kan minska osäkerhet före beslut

Alla frågor kan inte analyseras bort på papper.

När ett beslut bygger på osäkerhet kring exempelvis:

- prestanda,
- integrationskomplexitet,
- utvecklarupplevelse,
- driftbarhet,
- kompatibilitet,
- produktmognad,

kan en begränsad **proof of concept**, spike eller teknisk prototyp vara billigare än lång argumentation.

Syftet bör då vara att testa en konkret hypotes.

Svagt mål:

> Testa produkt X.

Starkare mål:

> Verifiera om produkt X kan hantera den definierade meddelandevolymen med accepterad latenstid och om plattformsorganisationen kan observera och felsöka flödet med befintliga verktyg.

En prototyp utan beslutskriterier riskerar bara att visa att tekniken går att starta. En prototyp kopplad till en osäkerhet kan däremot minska beslutsrisken.

## Beslutslogg och arkitekturdiagram fyller olika funktioner

Ett arkitekturdiagram visar ofta **vad** lösningen består av och hur delar relaterar.

En beslutslogg visar **varför** strukturen blev sådan.

De ersätter inte varandra.

Ett diagram kan visa att en lösning använder en meddelandebroker. Det säger inte om den valdes för att mottagaren måste kunna vara offline, för att belastningstoppar behöver buffras, för att organisationen har en standardplattform eller bara för att teamet föredrog messaging.

När framtida arkitekter ser diagrammet behöver de kunna avgöra vilka delar som är:

- fundamentala för behovet,
- konsekvens av ett kvalitetskrav,
- organisatorisk begränsning,
- lokalt teknikval,
- historiskt arv som kan ändras.

Det är denna förståelse beslutshistoriken ger.

## När ett beslut blir en standard

Ett lokalt arkitekturbeslut och en teknisk standard är inte samma sak.

Om ett team beslutar att använda ett visst mönster eller en viss produkt betyder det inte att hela organisationen bör göra samma sak.

För att ett lokalt beslut ska kunna generaliseras behöver man fråga:

- Är behovet återkommande i flera domäner?
- Är kvalitetskraven tillräckligt lika?
- Finns skalfördelar eller riskreduktion i att göra valet gemensamt?
- Har lösningen bevisats i flera relevanta sammanhang?
- Är konsekvenserna för andra team förstådda?
- Finns förvaltningskapacitet för ett gemensamt erbjudande?

Detta är en viktig koppling till bokens senare delar. Lösningsmönster, plattformstjänster och standarder bör växa fram ur **återkommande beslutssituationer**, inte ur önskan att katalogisera så mycket teknik som möjligt.

## Beslut ska kunna förstås utan mötesminnet

I stora organisationer byter människor roller. Team omorganiseras. Plattformar får nya ägare. Konsulter lämnar. Ett muntligt resonemang som alla känner till idag kan vara helt borta om två år.

Därför är en bra kontrollfråga:

> Kan en kompetent person som inte deltog i beslutet förstå varför det var rimligt?

Om svaret är nej är beslutet för beroende av organisatoriskt minne.

Det innebär inte att varje diskussion måste dokumenteras. Men det som behövs för att rekonstruera kärnlogiken bör finnas kvar:

- kontexten,
- de viktigaste alternativen,
- beslutskriterierna,
- valet,
- konsekvenserna,
- centrala antaganden.

## En enkel beslutsprocess

En praktisk process för större arkitekturbeslut kan sammanfattas i åtta steg.

### 1. Formulera beslutssituationen

Beskriv vad som faktiskt behöver avgöras. Undvik att formulera frågan som ett produktval om det underliggande problemet är bredare.

### 2. Identifiera arkitekturdrivare

Samla relevanta behov, kvalitetskrav, begränsningar och beroenden.

### 3. Skilj krav från preferenser och antaganden

Det minskar risken att historiska vanor får status som absoluta krav.

### 4. Identifiera realistiska alternativ

Ta med status quo när det är ett verkligt alternativ. Att inte förändra något har också konsekvenser.

### 5. Jämför avvägningar

Analysera hur alternativen påverkar de prioriterade kvaliteterna, kostnaderna, riskerna och framtida handlingsutrymmet.

### 6. Minska kritisk osäkerhet

Använd prototyper, mätningar, expertgranskning eller annan evidens där centrala antaganden är osäkra.

### 7. Fatta och dokumentera beslutet

Gör val, konsekvenser, risker och antaganden synliga.

### 8. Definiera när beslutet ska omprövas

Ange datum eller händelser som gör en ny bedömning relevant.

Processen kan vara omfattande för ett organisationsgemensamt beslut och mycket lättviktig för ett lokalt, reversibelt val. Formen ska stå i proportion till beslutets konsekvens.

## Vad ett bra beslut inte behöver vara

Ett bra arkitekturbeslut behöver inte vara perfekt.

Det behöver inte heller innebära fullständig konsensus. Ibland är alternativen genuint jämnstarka och någon med mandat behöver välja.

Ett bra beslut kännetecknas snarare av att:

- problemet är rätt formulerat,
- de viktigaste drivarna är kända,
- relevanta alternativ har övervägts,
- avvägningar är synliga,
- antaganden och risker är ärligt beskrivna,
- beslutet är begripligt för andra,
- det går att ompröva när förutsättningarna ändras.

Detta flyttar fokus från frågan:

> Valde vi den bästa tekniken?

mot en bättre fråga:

> Fattade vi ett rimligt och spårbart beslut utifrån den information och de prioriteringar vi hade?

## Från beslut till gemensam riktning

En organisation som dokumenterar sina viktigaste beslut börjar efter hand se mönster.

Samma frågor återkommer:

- ska vi använda det gemensamma erbjudandet eller bygga själva?
- när ska kommunikationen vara asynkron?
- hur mycket leverantörsspecificitet accepterar vi?
- när behöver data separeras?
- vilka kvaliteter måste alltid beaktas?

När samma beslutslogik återkommer kan det vara ett tecken på att organisationen behöver något mer stabilt än enskilda ADR:er.

Det kan bli:

- en arkitekturprincip,
- ett lösningsmönster,
- en teknisk standard,
- ett plattformserbjudande,
- en referensarkitektur.

Det är så gemensam arkitektur kan växa fram ur verkliga behov utan att reduceras till central teori.

Nästa kapitel behandlar **arkitekturprinciper** – ett sätt att uttrycka återkommande beslutsriktning på en mer generell nivå. Principer ska inte ersätta beslut och avvägning-analys, men de kan göra organisationens viktigaste utgångspunkter tydliga innan varje enskild beslutssituation uppstår.
