# 5. Arkitekturbeslut och avvägningar

Arkitektur handlar sällan om att hitta ett alternativ som är bäst i alla avseenden. Ofta finns flera lösningar som skulle fungera, men de fungerar bra på olika sätt. En lösning kan ge hög förändringstakt men större operativ komplexitet. En annan kan vara enklare att drifta men ge svagare isolering mellan verksamhetsdelar. En tredje kan vara billigast att införa men svårare att lämna senare.

Det arkitektoniska arbetet består därför inte bara i att beskriva en målbild. Det består också i att göra medvetna val mellan konkurrerande egenskaper, tydliggöra varför valet gjordes och göra det möjligt att ompröva beslutet när förutsättningarna förändras.

Ett arkitekturbeslut behöver kunna besvara åtminstone fyra frågor:

1. Vilket problem eller behov försöker vi lösa?
2. Vilka realistiska alternativ övervägde vi?
3. Vilka konsekvenser och avvägningar innebär alternativen?
4. Varför är det valda alternativet rimligt i just denna kontext?

Det är först när dessa frågor är synliga som arkitekturen blir spårbar som beslutslogik, inte bara som ett tillstånd i ett diagram.

Detta kapitel behandlar hur arkitekturbeslut kan göras explicita, jämförbara och omprövningsbara. Fokus ligger på själva beslutets form och resonemang. Hur organisationen ger mandat, hanterar avsteg och förvaltar styrningen över tid behandlas senare i boken.

## Arkitektur är val under begränsningar

Vi har skilt mellan behov, begränsningar och teknikval och sett hur kvalitetsattribut gör vissa egenskaper arkitekturdrivande. Tillsammans skapar de beslutsrymmet.

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

Det viktiga ordet är realistiska. Arkitekturval görs aldrig i ett vakuum. Organisationen kan redan ha investerat i plattformar, kompetens, avtal, driftsmodeller och säkerhetsmekanismer. Lagstiftning, informationsklassning eller externa integrationskrav kan begränsa möjliga alternativ. Tid, budget och tillgång till kompetens gör detsamma.

Men begränsningar ska avgränsa beslutsrymmet – inte ersätta beslutsanalysen.

Om organisationen redan har en *containerplattform* är det ett relevant faktum. Det betyder däremot inte automatiskt att varje ny applikation bör köras där. Frågan är fortfarande om plattformens egenskaper möter lösningens behov bättre än alternativen, givet kostnad, risk och långsiktiga konsekvenser.

## Ett arkitekturbeslut är mer än ett teknikval

Uttrycket arkitekturbeslut associeras lätt med val som:

- PostgreSQL eller en annan databas,
- synkron API-kommunikation eller asynkrona meddelanden,
- container eller virtuell maskin,
- centralt workflow eller egen processlogik.

Sådana beslut kan vara arkitekturella, men tekniken i sig avgör inte om beslutet är ett arkitekturbeslut.

Ett beslut är arkitekturellt när det har betydande och svårreversibla konsekvenser för struktur, kvaliteter, ansvar, beroenden eller framtida handlingsutrymme.

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

- räckvidd – hur många lösningar eller team påverkas,
- livslängd – hur länge beslutet förväntas gälla,
- reversibilitet – hur dyrt eller svårt det är att ändra,
- kvalitetspåverkan – vilka viktiga kvalitetsattribut som påverkas,
- beroenden – vilka organisatoriska eller tekniska låsningar som skapas,
- risk – vad konsekvensen blir om antagandet bakom beslutet visar sig felaktigt.

Ju högre dessa faktorer är, desto större värde finns i att göra beslutet explicit.

## Det finns nästan alltid flera dimensioner samtidigt

Ett vanligt misstag är att jämföra alternativ längs en enda axel. En integrationsström kan exempelvis byggas med synkrona API-anrop eller asynkron meddelandehantering. Frågan är då inte bara vilket alternativ som är mest robust.

Valet påverkar samtidigt bland annat svarstid, koppling i tid, felhantering, observerbarhet, dataordning, testbarhet, kompetensbehov och driftansvar. Asynkron kommunikation kan tåla att mottagaren tillfälligt är nere, men introducerar frågor om exempelvis idempotens, ordering och korrelation. Synkron kommunikation kan vara enklare att förstå men skapar hårdare tillgänglighetsberoenden.

Arkitektens uppgift är därför att bedöma kombinationen av egenskaper mot den prioriterade kravbilden, inte att hitta den dimension där ett alternativ råkar vara starkast.

## Avvägning betyder inte kompromiss i negativ mening

En avvägning innebär att en förbättring i en egenskap kan medföra kostnader eller konsekvenser i en annan. Mer isolering kan ge högre operativ komplexitet. Mer återanvändning kan ge starkare koppling. Strikt standardisering kan minska variationskostnaden men också begränsa lokalt handlingsutrymme. Hög portabilitet kan minska leverantörslåsning men göra värdefulla plattformsspecifika funktioner svårare att använda.

Det finns därför sällan en arkitektur som maximerar alla kvaliteter samtidigt. Prioriteringen från föregående kapitel blir avgörande: utan tydliga prioriteringar riskerar avvägningen att reduceras till personliga teknikpreferenser.

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

Ett vanligt sätt att dokumentera arkitekturbeslut är ett Architecture Decision Record, ofta förkortat ADR.

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

Den andra texten gör två saker som den första saknar: den beskriver varför valet gjordes och vilka konsekvenser som accepterades.

## ADR är beslutshistorik, inte dokumentationsritual

ADR ger störst värde för beslut som är betydelsefulla, svåra att förstå i efterhand, innehåller tydliga avvägningar, bygger på osäkra antaganden eller är kostsamma att reversera. För mindre beslut kan kod, konfiguration eller vanlig teknisk dokumentation räcka.

En bra tumregel är:

> Dokumentera beslut där förlusten av beslutslogiken skulle vara kostsam.

Beslutet bör också ha en begriplig livscykel. En enkel statusmodell – exempelvis Föreslaget, Accepterat, Ersatt och Utgånget – gör det möjligt att bevara historiken utan att äldre beslut ser ut att fortfarande gälla. Det är värdefullt eftersom ett äldre beslut kan ha varit helt rimligt under dåvarande förutsättningar.

Konsekvenserna ska beskrivas öppet, även de negativa. Om en gemensam managed LLM-tjänst exempelvis ger gemensam säkerhetsmodell, kostnadsuppföljning och loggning kan samma beslut samtidigt skapa beroende av plattformens prioriteringar eller bromsa tillgången till leverantörsspecifika funktioner. Att dokumentera nackdelarna försvagar inte beslutet; det gör det möjligt att följa upp det.

Riskacceptans och medveten teknisk skuld är på samma sätt beslut, inte undantag från beslutsprocessen. Om en första version exempelvis accepteras utan full redundans eller med en temporär punkt-till-punkt-integration bör det framgå varför, vilken konsekvens som accepteras, vilka kompensatoriska åtgärder som finns och när frågan ska tas upp igen. Då blir framtida kostnad och risk synliga i stället för att döljas i lösningen.

För beslut som bygger på tydliga antaganden är det också värdefullt att skriva ned själva antagandet. Om ett plattformsval exempelvis bara är rimligt under en viss lastnivå eller så länge en viss leverantörsfunktion finns kvar kan den informationen vara viktigare för framtida omprövning än en lång beskrivning av mötet där beslutet fattades.

## Beslut behöver omprövningsvillkor

En av de mest värdefulla uppgifterna i en beslutsnotering är ofta när beslutet inte längre ska betraktas som självklart.

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

Det innebär att beslutsprocessen bör vara proportionerlig mot konsekvensen av att ha fel.

Det är särskilt viktigt i gemensam IT-arkitektur. Ett beslut som bara påverkar en lösning kan vara relativt enkelt att korrigera. Ett gemensamt plattformsbeslut som hundra system bygger på kan skapa mycket stor framtida tröghet.

## Beslut på olika nivåer

Bokens tre ansvarsnivåer hjälper också till att placera beslut rätt.

På **gemensam arkitekturnivå** hör beslut hemma som behöver vara konsekventa över flera förmågor eller lösningar, exempelvis övergripande identitetsmodell eller gemensamma kvalitetsdimensioner.

På **förmågenivå** fattas beslut om hur ett visst område ska fungera och vilka erbjudanden det ska tillhandahålla, exempelvis vilka integrationsstilar eller kontraktsregler som stöds inom *Integration och kommunikation*.

På **lösnings-/produktnivå** fattas beslut för ett specifikt verksamhetsbehov, exempelvis om en viss integration ska vara synkron eller asynkron eller hur en tjänst partitionerar sin data.

Beslut bör inte lyftas högre än nödvändigt, men inte heller döljas som lokala implementationer om de skapar beroenden för många team.

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

Avvägningsanalysen gör alltså inte beslutet automatiskt. Den gör orsakerna till beslutet synliga.

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

En beslutsmatris bör därför användas som samtals- och analysverktyg, inte som en maskin som fattar beslutet.

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

kan en begränsad proof of concept, spike eller teknisk prototyp vara billigare än lång argumentation.

Syftet bör då vara att testa en konkret hypotes.

Svagt mål:

> Testa produkt X.

Starkare mål:

> Verifiera om produkt X kan hantera den definierade meddelandevolymen med accepterad latenstid och om plattformsorganisationen kan observera och felsöka flödet med befintliga verktyg.

En prototyp utan beslutskriterier riskerar bara att visa att tekniken går att starta. En prototyp kopplad till en osäkerhet kan däremot minska beslutsrisken. Resultatet bör därför återföras till beslutet som evidens: vilken hypotes testades, vad observerades och hur påverkade det jämförelsen mellan alternativen? På så sätt blir prototypen en del av beslutsunderlaget i stället för ett parallellt teknikexperiment.

## Beslutslogg och arkitekturdiagram fyller olika funktioner

Ett arkitekturdiagram visar ofta vad lösningen består av och hur delar relaterar.

En beslutslogg visar varför strukturen blev sådan.

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

Ett lokalt arkitekturbeslut är inte automatiskt en teknisk standard. För att generaliseras behöver beslutet motsvara ett återkommande behov, ha tillräckligt likartade kvalitetskrav i flera sammanhang och ge en tydlig gemensam nytta, exempelvis skalfördelar eller riskreduktion.

Det behöver också finnas förvaltningskapacitet och förståelse för konsekvenserna för andra team. Lösningsmönster, plattformstjänster och standarder bör därför växa fram ur återkommande beslutssituationer, inte ur önskan att katalogisera teknik.

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

Ett bra arkitekturbeslut behöver inte vara perfekt eller bygga på fullständig konsensus. Det behöver vara rimligt och spårbart.

Det innebär att problemet är rätt formulerat, de viktigaste drivarna och alternativen är kända, avvägningar och risker är synliga och beslutet går att förstå och ompröva när förutsättningarna ändras.

Den viktigaste frågan är därför inte:

> Valde vi den bästa tekniken?

utan:

> Fattade vi ett rimligt beslut utifrån den information och de prioriteringar vi hade?

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

Nästa kapitel behandlar arkitekturprinciper – ett sätt att uttrycka återkommande beslutsriktning på en mer generell nivå. Principer ska inte ersätta beslut och avvägningsanalys, men de kan göra organisationens viktigaste utgångspunkter tydliga innan varje enskild beslutssituation uppstår.
