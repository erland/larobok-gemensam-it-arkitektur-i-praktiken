# 8. Vad är en IT-förmåga?

I de första kapitlen har gemensam IT-förmåga använts som ett av de centrala begreppen i bokens arkitekturmodell. Hittills har det räckt att förstå förmågan som något relativt stabilt som ett stödjande IT-område behöver kunna erbjuda över tid. När förmågekartan nu ska bli utgångspunkt för resten av boken behöver begreppet bli mer precist.

Det är nödvändigt eftersom ordet *förmåga* används på många sätt. En verksamhetsarkitekt kan tala om verksamhetsförmågan att handlägga ärenden. Ett plattformsteam kan säga att organisationen behöver en containerförmåga. En leverantör kan beskriva en produkt som en AI-förmåga. Ett utvecklingsteam kan tala om sin förmåga att leverera ofta. Alla användningarna kan vara begripliga i sitt sammanhang, men de betyder inte samma sak.

I den här boken används därför en avgränsad arbetsdefinition:

> En gemensam IT-förmåga är något ett stödjande IT-område varaktigt behöver kunna erbjuda stöd inom för att flera verksamhetslösningar ska kunna utvecklas, integreras, köras, förvaltas eller användas på ett ändamålsenligt sätt.

Definitionen är medvetet oberoende av dagens produkter och organisationsschema. Förmågan *Integration och kommunikation* finns exempelvis kvar även om en meddelandeprodukt byts ut, ett API-team omorganiseras eller vissa integrationsmekanismer flyttas till en annan teknisk plattform. Det som ska vara stabilt är behovsområdet och det ansvar organisationen behöver kunna bära – inte den aktuella realiseringen.

Detta kapitel förklarar vad som gör en sådan förmåga användbar som arkitekturbegrepp, hur den skiljer sig från närliggande begrepp och hur en förmågekarta kan användas utan att bli ännu en katalog över organisationens teknik.

## Förmåga beskriver vad organisationen behöver kunna åstadkomma

En förmåga uttrycker i första hand ett vad, inte ett hur.

Om organisationen behöver kunna autentisera användare, etablera tillit mellan tekniska tjänster och hantera autentiseringsuppgifter finns ett varaktigt behov inom området identitet och tillit. Den konkreta lösningen kan däremot förändras: identitetsleverantör, certifikatlösning, protokoll, nyckelhantering och driftmodell kan bytas över tid.

På motsvarande sätt beskriver *Applikationsexekvering och runtime* behovet av att kunna köra applikationer under definierade tekniska och operativa villkor. Förmågan är inte samma sak som Kubernetes, OpenShift, en JVM, en viss Linuxdistribution eller en virtuell maskin. Dessa kan vara byggblock eller produkter som realiserar delar av förmågan.

Denna separation ger två viktiga egenskaper.

För det första kan arkitekturen tala om långsiktigt ansvar utan att låsa sig till en produktgeneration. För det andra blir det möjligt att bedöma om dagens realisering faktiskt möter behovet. Om förmågan definieras som ”vår API gateway” blir frågan nästan självrefererande: så länge gatewayen finns har vi förmågan. Om förmågan i stället beskriver säker, spårbar och förändringsbar integration kan organisationen fråga om dess nuvarande API-, meddelande- och informationsutbyteslösningar tillsammans ger det stöd som behövs.

Förmågan fungerar därmed som ett lager mellan behov och realisering:

```text
Återkommande behov
        ↓
Gemensam IT-förmåga
        ↓
Mönster, plattformstjänster och standarder
        ↓
Tekniska byggblock och produkter
```

Den säger inte exakt hur problemet ska lösas. Den säger vilket område organisationen behöver kunna ta ett uthålligt ansvar för.

## Verksamhetsförmåga och gemensam IT-förmåga är inte samma sak

Den viktigaste distinktionen är mot verksamhetsförmåga.

En verksamhetsförmåga beskriver något verksamheten behöver kunna göra för att fullgöra sitt uppdrag eller skapa värde. I en myndighet kan exempel vara att genomföra kontroll, fatta beslut, hantera tillstånd, ge service eller utbyta information med andra aktörer. I ett företag kan motsvarande förmågor handla om försäljning, orderhantering, produktutveckling eller kundservice.

En gemensam IT-förmåga beskriver i stället ett stöd som IT-området behöver kunna tillhandahålla till flera sådana verksamhetsförmågor och deras digitala lösningar.

Relationen är därför ofta många-till-många:

```text
Verksamhetsförmåga A ─┐
Verksamhetsförmåga B ─┼─→ flera gemensamma IT-förmågor
Verksamhetsförmåga C ─┘

Gemensam IT-förmåga X ─→ stödjer flera verksamhetsförmågor
```

Ett digitalt handläggningsstöd kan exempelvis behöva interaktion, workflow, regler, data, integration, identitet, runtime och driftbarhet. Samtidigt kan identitetsförmågan användas av ett stort antal verksamhetsområden som i övrigt har mycket lite gemensamt.

Det gör att en gemensam IT-förmågekarta inte bör läsas som en karta över vad organisationen *gör*. Den beskriver vad ett stödjande IT-område behöver kunna erbjuda stöd inom.

Distinktionen har praktisk betydelse. Om IT-förmågorna utformas genom att spegla verksamhetsorganisationens avdelningar finns risk för att samma tekniska problem löses flera gånger. Om verksamhetsförmågorna i stället ersätts av en teknisk förmågekarta förlorar man verksamhetens ansvar och mening. De två kartorna kan kopplas till varandra, men de har olika syften.

## Förmåga är inte en tjänst

En annan vanlig sammanblandning uppstår mellan förmåga och tjänst.

Förmågan beskriver ett område organisationen behöver kunna stödja. En tjänst är ett mer konkret erbjudande som en konsument kan använda.

Förmågan *Data- och informationshantering* kan exempelvis realiseras genom flera tjänster:

- relationell databastjänst,
- objektlagring,
- cachetjänst,
- backup- och återställningstjänst,
- eventuellt andra lagrings- eller datahanteringserbjudanden.

Ingen av tjänsterna är ensam lika med förmågan. Förmågan är bredare och kan bestå även om vissa tjänster läggs till, delas upp eller avvecklas.

Skillnaden blir särskilt viktig när organisationen vill identifiera luckor. En förmåga kan vara nödvändig utan att det ännu finns ett bra gemensamt tjänsteerbjudande. Om begreppen görs identiska blir ett sådant tillstånd svårt att beskriva. Antingen måste man låtsas att tjänsten finns eller säga att förmågan saknas helt.

Med separationen kan man i stället säga:

> Organisationen behöver förmågan, men den nuvarande realiseringen är ofullständig och vissa behov lämnas fortfarande till lösningsteamen.

Det är ett betydligt mer användbart arkitekturläge.

## Förmåga är inte en produkt eller plattform

Samma resonemang gäller produkter och plattformar.

En produkt är en konkret realisering med version, leverantör, konfiguration, supportmodell och livscykel. En plattformstjänst är ett konsumerbart erbjudande som ofta realiseras av flera sådana produkter och tekniska byggblock. Förmågan ligger ovanför båda.

Exempelvis kan *Programvaruutveckling och leverans* stödjas av tjänster för källkodshantering, CI/CD, artifact repositories och utvecklarverktyg. Dessa tjänster kan i sin tur realiseras med specifika produkter. När en Git-plattform eller CI-produkt byts ut ska inte organisationen behöva rita om sin övergripande förmågekarta.

Detta är en av orsakerna till att förmågor är användbara som relativt stabil struktur. Produkter har ofta kortare livscykel än de problem de löser.

Samtidigt får produktoberoendet inte drivas så långt att förmågan blir innehållslös. ”Teknisk möjliggörande förmåga” är stabilt men säger nästan ingenting. En bra förmåga behöver vara tillräckligt konkret för att man ska kunna beskriva:

- vilka behov den stödjer,
- vilka kvaliteter som är viktiga,
- vad som ligger inom och utanför området,
- vilka andra förmågor den beror på,
- vilka typer av erbjudanden som kan behövas,
- vem som har ansvar för att området utvecklas.

Stabilitet kommer alltså inte av maximal abstraktion utan av att välja en nivå som överlever normala teknikbyten utan att förlora sin mening.

## Förmåga är inte ett team eller en organisatorisk funktion

En förmågekarta bör inte heller vara en kopia av organisationsschemat.

Det är möjligt att ett team i praktiken ansvarar för en hel förmåga, men det är inte ett krav. Ett team kan ansvara för flera förmågor och en förmåga kan kräva samarbete mellan flera organisatoriska enheter.

Detta är särskilt tydligt för tvärgående områden. *Driftbarhet och motståndskraft* kan involvera plattformsteam, säkerhetsfunktioner, driftorganisation, utvecklingsteam och kontinuitetsansvariga. Förmågan behöver ändå kunna beskrivas som ett sammanhängande arkitekturområde med tydliga ansvarssnitt.

Om förmågan definieras efter dagens team uppstår två problem.

Det första är att arkitekturmodellen blir instabil vid varje omorganisation. Det andra är att organisatoriska glapp riskerar att döljas. Om två team delar ansvar för en fråga kan en förmågekarta som bara speglar teamen göra det svårt att se att det egentligen finns ett gemensamt behov som ingen håller ihop.

Förmågekartan bör därför kunna användas för att utmana organisationen, inte bara avbilda den.

Ett bra kontrolltest är:

> Om teamen organiserades om i morgon, skulle detta fortfarande vara något IT-området behöver kunna erbjuda stöd inom?

Om svaret är ja talar det för att man beskriver en förmåga snarare än en organisatorisk funktion.

## Förmåga är inte samma sak som kompetens eller kapacitet

Orden ligger nära varandra men bör hållas isär.

Kompetens handlar om människors eller gruppers kunskap och färdighet. En organisation kan behöva kompetens inom databasteknik, informationsmodellering, nätverk eller UX för att realisera olika förmågor. Kompetensen är en förutsättning men inte själva förmågan.

Kapacitet beskriver hur mycket som kan hanteras inom en viss tid eller belastning: antal transaktioner, mängd lagring, antal samtidiga användare, leveransvolym eller tillgänglig bemanning. Två organisationer kan i princip ha samma förmåga men mycket olika kapacitet.

En gemensam IT-förmåga beskriver däremot att organisationen kan erbjuda ett visst slags stöd med en kombination av ansvar, kompetens, processer, tjänster, teknik och styrning.

Det är därför möjligt att säga:

- vi har identifierat förmågan men saknar tillräcklig kompetens,
- vi erbjuder förmågan men kapaciteten är otillräcklig,
- vi har tekniska produkter men saknar ett sammanhållet förmågeansvar,
- vi har hög lokal kompetens men inget gemensamt tjänsteerbjudande.

Sådana utsagor är viktiga eftersom de gör olika typer av brister synliga.

## Förmågan är ett ansvarssystem – inte bara en rubrik

En ruta i en capability map har inget egenvärde. Förmågan blir användbar först när den kopplas till ett ansvarssystem.

För en gemensam IT-förmåga behöver organisationen över tid kunna svara på frågor som:

- vilka återkommande konsumentbehov finns inom området?
- vilka kvalitetsattribut är särskilt viktiga?
- vilka problem ska lösas gemensamt och vilka bör lämnas lokala?
- vilka lösningsmönster rekommenderas?
- vilka plattformstjänster erbjuds eller saknas?
- vilka standarder behövs?
- vilka beroenden finns till andra förmågor?
- vilka teknik- och produktlivscykler påverkar området?
- hur vet vi om erbjudandena faktiskt används och skapar värde?
- vem ansvarar för att dessa frågor hålls samman?

Detta betyder inte att allt måste dokumenteras från början. Kapitel 7 betonade tvärtom en iterativ etablering. Men frågorna visar vad som skiljer en förmåga från en etikett.

Förmågan är ett sätt att samla ett relativt stabilt problemområde så att behov, ansvar, arkitekturbeslut och återanvändbara erbjudanden kan utvecklas sammanhängande över tid.

## Hur grov bör en förmåga vara?

En av de svåraste praktiska frågorna är granulariteten.

Om kartan är för grov blir den svår att använda. En enda förmåga som heter ”Teknisk plattform” kan rymma runtime, integration, identitet, data, observerbarhet och leverans. Nästan alla frågor hamnar då i samma ruta och kartan hjälper inte till att fördela ansvar eller analysera behov.

Om kartan är för detaljerad uppstår motsatt problem. Om varje protokoll, databasfunktion, utvecklingsverktyg och driftmekanism blir en egen förmåga får organisationen i praktiken en teknik- eller tjänstekatalog med ett nytt namn.

En användbar nivå ligger däremellan. Förmågan bör vara stor nog att:

- vara stabil över normala produkt- och teknikbyten,
- samla problem som har ett meningsfullt gemensamt ansvar,
- kunna bära en långsiktig utvecklingsriktning.

Men den bör också vara avgränsad nog att:

- konsumenterna förstår vilket slags stöd som hör dit,
- gränser och beroenden kan beskrivas,
- ansvar kan tilldelas,
- relevanta mönster, tjänster och standarder går att identifiera.

Bokens elva förmågor är ett exempel på en sådan indelning, inte ett påstående om att exakt elva är rätt för varje organisation. En annan organisation kan slå samman, dela upp eller lägga till områden beroende på uppdrag, storlek, sourcingmodell och teknisk kontext.

Det viktiga är att indelningen följer samma logik.

## Ett praktiskt test för en kandidatförmåga

När ett nytt område föreslås som gemensam IT-förmåga kan det prövas med några frågor.

### 1. Beskriver namnet ett varaktigt behovsområde?

”Integration och kommunikation” klarar testet bättre än ”Kafka” eller ”API Gateway”. Det första beskriver ett problemområde. De andra beskriver möjliga realiseringar.

### 2. Finns behovet i flera lösningar eller verksamhetsområden?

Förmågan behöver inte användas av exakt alla, men den bör vara relevant bortom ett enskilt system. Ett helt unikt verksamhetsproblem hör ofta bättre hemma i en domän- eller lösningsarkitektur.

### 3. Finns ett meningsfullt gemensamt ansvar?

Kan någon utveckla vägledning, mönster, erbjudanden eller standarder som faktiskt hjälper flera konsumenter? Om svaret är nej kan området vara för lokalt eller för abstrakt.

### 4. Överlever förmågan ett produktbyte?

Om namnet och innehållet behöver ändras så snart en leverantör eller produkt ersätts ligger beskrivningen sannolikt för nära realiseringen.

### 5. Går gränsen mot närliggande förmågor att förklara?

Gränser behöver inte vara knivskarpa, men det ska gå att beskriva varför exempelvis tjänsteidentitet primärt hör hemma inom Identitet och tillit medan dess loggning beror på Driftbarhet och motståndskraft.

### 6. Kan förmågan utvecklas utan att detaljdesigna varje lösning?

Om förmågeansvaret kräver kontroll över varje applikations interna design är avgränsningen sannolikt fel eller styrmodellen för centraliserad.

Frågorna är inte en formell certifiering. De hjälper till att upptäcka när en förmågekarta håller på att glida mot produktkatalog, organisationsschema eller lösningsdesign.

## Capability map – karta, inte inventarielista

En capability map, eller förmågekarta, visar vilka förmågor som finns och ofta hur de grupperas eller relaterar till varandra. För den gemensamma IT-arkitekturen fungerar kartan främst som en orienteringsyta.

Den kan användas för att:

- skapa ett gemensamt språk mellan arkitektur-, plattforms- och lösningsteam,
- fördela och synliggöra ansvar,
- koppla behov och kvalitetskrav till rätt område,
- visa var gemensamma tjänster och standarder hör hemma,
- identifiera överlapp, tomrum och beroenden,
- prioritera investeringar och fördjupning,
- analysera effekten av teknik- och produktförändringar.

Men kartan bör inte försöka bära all information själv. Om varje ruta fylls med produkter, versioner, standarder, ägare, projekt, mognadsnivåer och tekniska beroenden blir den snart oläslig.

Bättre är att behandla kartan som ett index till en rikare modell. För varje förmåga kan det finnas en separat beskrivning med syfte, omfattning, kvaliteter, mönster, plattformstjänster, standarder och relationer. Kartan visar strukturen; underliggande artefakter ger detaljerna.

Det är samma princip som i kapitel 2: olika frågor behöver olika artefakter på rätt abstraktionsnivå.

## Stabil betyder inte oföränderlig

Att förmågor ska vara stabilare än produkter betyder inte att förmågekartan ska frysas.

Nya verksamhetsbehov kan göra att ett område blir viktigt nog att få ett eget ansvar. Teknikutveckling kan förändra vilka problem som naturligt hör ihop. En organisations sourcingmodell kan göra att en tidigare intern förmåga huvudsakligen konsumeras externt. Flera förmågor kan visa sig ha så stora beroenden att en gräns behöver flyttas.

En förändring av förmågekartan bör dock normalt ha en annan tyngd än ett produktbyte. Om kartan ändras varje kvartal är den förmodligen för nära teknik- eller organisationsstrukturen. Om den aldrig omprövas trots stora förändringar riskerar den att bli historisk dokumentation.

En användbar förmågekarta är därför trögrörlig men lärande.

Den ska ge kontinuitet samtidigt som erfarenheter från förmågeområden och lösningar kan förändra modellen när det finns goda skäl.

## Förmågemognad är flerdimensionell

När organisationen väl har en förmågekarta uppstår ofta önskemålet att bedöma ”mognad”. Det kan vara användbart, men ett enda mognadstal kan dölja mer än det förklarar.

En förmåga kan exempelvis ha:

- tydligt ansvar men svaga tjänsteerbjudanden,
- god teknik men dålig utvecklarupplevelse,
- etablerade standarder men låg faktisk användning,
- hög tillgänglighet men svag kostnadstransparens,
- god kompetens men produkter nära end-of-life,
- hög användning men otillräcklig kapacitet.

Det är därför ofta mer informativt att bedöma flera dimensioner, till exempel:

- ansvar och ägarskap,
- behovsförståelse,
- arkitektur och vägledning,
- tjänsteutbud,
- standardisering och automatisering,
- kvalitet och driftbarhet,
- användbarhet för konsumenter,
- livscykel och förvaltningsförmåga,
- faktisk användning och upplevt värde.

Syftet bör inte vara att ge varje ruta en dekorativ färg utan att identifiera var nästa investering ger störst effekt.

Även här gäller principen behov före teknik. En tekniskt avancerad plattform gör inte automatiskt förmågan mogen om konsumenterna inte kan eller vill använda den.

## Exempel: integration som förmåga, tjänst och produkt

Ett konkret exempel visar skillnaderna mellan nivåerna.

Anta att en större organisation har många system som behöver utbyta information. Den gemensamma IT-förmågan kan beskrivas som Integration och kommunikation.

Förmågan omfattar frågor som:

- när synkron respektive asynkron kommunikation är lämplig,
- hur kontrakt ska hanteras,
- hur koppling mellan system begränsas,
- hur meddelanden och API-anrop säkras och observeras,
- hur externa informationsutbyten hanteras,
- vilka gemensamma erbjudanden som behöver finnas.

Inom förmågan kan organisationen definiera lösningsmönster för exempelvis asynkron meddelandekommunikation och publicera/prenumerera.

Den kan erbjuda plattformstjänster som API Management och Enterprise Messaging.

Dessa tjänster realiseras i sin tur med tekniska produkter, konfigurationer, runtime-miljöer och nätverkskomponenter.

Ett lösningsteam som behöver publicera information väljer därefter en lämplig struktur utifrån sitt behov och sina kvalitetskrav. Förmågeansvaret ska ge teamet bra alternativ och tydliga ramar, men inte på förhand bestämma att alla integrationsproblem ska lösas med samma produkt eller kommunikationsstil.

Det är just denna kedja som gör förmågebegreppet användbart:

```text
Behov av informationsutbyte
          ↓
Integration och kommunikation
          ↓
Lösningsmönster + plattformstjänster + standarder
          ↓
Konkreta tekniska produkter och konfigurationer
          ↓
Lösningsarkitektur för det specifika systemet
```

Varje nivå svarar på en annan fråga. När nivåerna blandas ihop blir både styrning och förändring svårare.

## De elva förmågorna är en arbetshypotes som ska kunna prövas

Bokens fortsatta fördjupning utgår från elva gemensamma IT-förmågor:

1. *Interaktion, presentation och kanaler*,
2. *Process, workflow och ärendehantering*,
3. Regler och beslut,
4. Data- och informationshantering,
5. Analys, sökning och AI,
6. Integration och kommunikation,
7. Identitet och tillit,
8. Applikationsexekvering och runtime,
9. Driftbarhet och motståndskraft,
10. *Programvaruutveckling och leverans*,
11. Arbetsplats, samarbete och produktivitet.

Indelningen ska läsas som ett sammanhängande förslag för ett stödjande IT-område, inte som en universell taxonomi.

Det är möjligt att en organisation behöver dela upp analys och AI i flera förmågor, lägga till nätverks- eller säkerhetsrelaterade områden, slå samman runtime och driftbarhet eller organisera digital arbetsplats på ett helt annat sätt. Poängen är inte att kopiera elva rubriker. Poängen är att använda ett stabilt förmågeperspektiv för att skapa ansvar och återanvändning utan att börja i produkter.

Det leder direkt till nästa fråga. Även om något kan beskrivas som en IT-förmåga betyder det inte att hela förmågan eller alla dess realiseringar bör centraliseras.

Nästa kapitel behandlar därför när något faktiskt bör vara gemensamt – och när federation, lokal variation eller domänspecifikt ansvar är ett bättre val.
