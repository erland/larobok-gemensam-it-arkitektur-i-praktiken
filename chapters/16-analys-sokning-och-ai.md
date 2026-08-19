# 16. Analys, sökning och AI

Samma information kan användas på helt olika sätt. En handläggare kan vilja hitta ett dokument. En chef kan vilja se hur ärendevolymer utvecklas över tid. Ett verksamhetssystem kan behöva klassificera inkommande material. En användare kan vilja ställa en fråga med naturligt språk och få ett sammanfattat svar grundat i interna källor.

Alla dessa behov använder data, men de är inte samma arkitekturproblem.

Det är därför missvisande att samla allt som kallas ”data och AI” i en enda teknisk lösning. Fulltextsökning, rapportering, statistisk analys, maskininlärning och generativ AI har olika syften, olika kvalitetsmått, olika risker och olika sätt att förvaltas. En gemensam förmåga för **Analys, sökning och AI** behöver kunna stödja flera sådana arbetssätt utan att sudda ut deras skillnader.

Kärnfrågan i kapitlet är:

> **Vilken typ av informationsbearbetning behöver vi – sökning, analys, prediktion eller generering – och vilka krav följer av just den typen?**

Detta kapitel bygger vidare på kapitel 11 om informationens betydelse och ägarskap samt kapitel 15 om teknisk datahantering. Här ligger fokus inte på var primär data lagras, utan på hur information **indexeras, sammanställs, analyseras och används för inferens eller generering**.

## Fyra olika problem som ofta blandas ihop

En användbar första uppdelning är att skilja mellan fyra huvudtyper av behov.

**Sökning** svarar huvudsakligen på frågan:

> Var finns relevant information?

**Business Intelligence och analys** svarar exempelvis på:

> Vad har hänt, hur ser nuläget ut och vilka mönster kan vi se i data?

**Maskininlärning** används bland annat för:

> Vilken klass, sannolikhet eller prognos är rimlig utifrån observerade mönster?

**Generativ AI** används när behovet exempelvis är:

> Skapa, omformulera, sammanfatta eller resonera kring innehåll utifrån en instruktion och ett givet sammanhang.

Dessa kategorier kan kombineras. En söktjänst kan använda maskininlärning för rankning. En BI-lösning kan kompletteras med prediktiva modeller. En generativ AI-assistent kan använda sökning för att hämta aktuellt underlag innan svaret genereras.

Men kombination betyder inte att kategorierna bör behandlas som samma sak.

Ett vanligt arkitekturfel är att börja i den mest uppmärksammade tekniken. Om användaren säger ”jag vill kunna fråga på naturligt språk” kan lösningen snabbt formuleras som ”vi behöver en LLM”. Men det verkliga behovet kan vara ett väl avgränsat sökproblem där en bättre sökmodell, bra metadata och ett tydligt gränssnitt ger högre precision och lägre komplexitet.

Principen från kapitel 3 gäller alltså fullt ut även här:

> **AI är ett möjligt lösningsval, inte ett behov.**

## Sökning – en sekundär representation för att hitta information

Sökning fungerar ofta genom att data från en eller flera källor transformeras till ett särskilt **sökindex**. Indexet optimeras för att hitta information, inte för att vara verksamhetens primära register.

Det kan exempelvis innehålla:

- text från dokument,
- utvalda metadata,
- normaliserade fält,
- tokeniserade textrepresentationer,
- behörighetsinformation för filtrering,
- vektorrepresentationer för semantisk sökning.

Detta gör sökindexet till ännu ett exempel på en **härledd kopia**, enligt modellen i kapitel 15.

För en söklösning behöver man därför kunna svara på frågor som:

1. Vilken källa är auktoritativ?
2. Vilken information indexeras?
3. Hur snabbt måste indexet uppdateras?
4. Hur återskapas indexet om det går förlorat?
5. Hur hanteras behörigheter när informationen kopieras till indexet?
6. Vad betyder ett relevant sökresultat för användaren?

Den sista frågan är lätt att underskatta. Sökning är inte bara ett lagringsproblem. Den är också ett **relevansproblem**.

### Lexikal och semantisk sökning

Traditionell fulltextsökning bygger i stor utsträckning på ord och textstrukturer. Den är ofta mycket stark när användaren vet vilka begrepp som förekommer i materialet och när exakta termer är viktiga.

Semantisk sökning försöker i stället hitta innehåll utifrån betydelse eller likhet i en representation. Moderna lösningar använder ofta så kallade embeddings, där text eller andra objekt representeras som numeriska vektorer som kan jämföras.

Det betyder inte att semantisk sökning alltid är bättre. Exakta identifierare, diarienummer, artikelnummer, juridiska termer och namn kan kräva mycket precis lexikal matchning. I praktiken kan därför en **hybridmodell** vara värdefull, där flera söksignaler kombineras.

Arkitekturfrågan är inte vilken metod som låter mest avancerad, utan:

> **Vilken definition av relevans motsvarar användningsfallet?**

### Behörighet måste följa med till söklagret

Ett sökindex kan skapa en ny säkerhetsrisk. Information som var korrekt skyddad i källsystemet kan bli sökbar från en gemensam tjänst.

Det räcker därför inte att säkra indexets administrativa gränssnitt. Lösningen måste även säkerställa att användaren bara kan hitta och läsa sådant som användaren är behörig att få tillgång till.

Några möjliga modeller är:

- behörighetsfiltrering redan vid indexering,
- lagring av åtkomstmetadata i indexet,
- kontroll mot källsystem eller auktorisationstjänst vid läsning,
- kombinationer av dessa.

Valet påverkar både prestanda, aktualitet och säkerhet. Om en användares behörighet tas bort måste söklösningen exempelvis veta hur snabbt detta ska slå igenom.

## BI och analys – från transaktioner till beslutsunderlag

Operativa system är normalt utformade för att genomföra verksamhetstransaktioner: registrera ett ärende, ändra status, fatta ett beslut eller lagra ett dokument.

Analysbehov ser ofta annorlunda ut. Verksamheten vill kanske:

- summera stora datamängder,
- jämföra perioder,
- följa nyckeltal,
- identifiera avvikelser,
- kombinera information från flera källor,
- analysera historiska utvecklingsmönster.

Det kan motivera särskilda analytiska representationer, exempelvis datamarts eller andra analyslager.

Även dessa är härledda kopior. Deras kvalitet beror därför på:

- källornas kvalitet,
- transformationslogiken,
- uppdateringsfrekvensen,
- gemensamma definitioner av mått och dimensioner,
- hur historik hanteras.

### Ett diagram är inte mer sant än sin definition

En instrumentpanel kan se exakt och övertygande ut även när begreppen bakom den är otydliga.

Ta ett enkelt nyckeltal som **genomsnittlig handläggningstid**. För att måttet ska vara meningsfullt måste man bland annat veta:

- när tiden börjar räknas,
- när den slutar,
- om väntetid på extern part räknas med,
- hur återöppnade ärenden hanteras,
- vilka ärendetyper som ingår,
- vilken tidsperiod som används.

Analysförmågan kan erbjuda teknik för visualisering och databehandling, men den kan inte ensam avgöra vad verksamhetsbegreppet betyder. Därför behöver analysplattformen kopplas tillbaka till informationsägarskapet från kapitel 11.

En central princip är:

> **Gemensam analysinfrastruktur får inte skapa en illusion av gemensam semantik.**

Semantiken måste ägas och förvaltas lika medvetet som tekniken.

## Maskininlärning – inferens i stället för explicit regel

I kapitel 14 skilde vi mellan explicita verksamhetsregler och AI-baserad inferens. Skillnaden är grundläggande.

En deterministisk regel kan exempelvis uttryckas:

```text
OM belopp > 100 000 OCH riskklass = hög
SÅ krävs fördjupad kontroll
```

En maskininlärningsmodell kan i stället producera något i stil med:

```text
sannolikhet för kategori A = 0,82
```

Resultatet kommer då inte från en explicit regel som någon har skrivit. Det är modellens inferens utifrån de mönster den har lärt sig eller representerar.

Det förändrar arkitekturfrågorna.

Man behöver exempelvis förstå:

- vilka data modellen utvecklades eller tränades med,
- vilka egenskaper som används som input,
- hur kvalitet mäts,
- hur osäkerhet representeras,
- hur modellen beter sig på nya typer av data,
- hur förändringar i data över tid påverkar resultatet,
- hur modellen versioneras och återställs,
- vilka verksamhetskonsekvenser ett felaktigt resultat får.

### Precision är inte ett universellt kvalitetsmått

Det finns ingen enda siffra som beskriver om en modell är ”bra”.

För en klassificeringsmodell kan exempelvis falska positiva och falska negativa utfall ha helt olika verksamhetskonsekvenser. En modell som flaggar misstänkta händelser kan behöva optimeras annorlunda beroende på om det värsta felet är att missa ett verkligt riskfall eller att skapa för många onödiga kontroller.

Kvalitetsmåttet måste därför härledas från användningen, precis som andra kvalitetsattribut i kapitel 4.

Det är också viktigt att skilja mellan:

- **modellkvalitet i ett testdataset**,
- **kvalitet i den verkliga produktionsmiljön**,
- **verksamhetsnytta av hela arbetsflödet där modellen ingår**.

En modell kan vara statistiskt stark men ändå skapa dålig verksamhetsnytta om dess resultat presenteras vid fel tidpunkt, inte går att agera på eller leder till en ineffektiv arbetsprocess.

## Generativ AI – resultatet är en generering, inte ett facit

Generativa språkmodeller skiljer sig från klassiska söktjänster och regelmotorer genom att de producerar nytt innehåll utifrån en instruktion och den kontext de får.

Det gör dem användbara för exempelvis:

- sammanfattning,
- omformulering,
- språkstöd,
- informationsutvinning,
- assistentfunktioner,
- interaktion med stora informationsmängder,
- utkast och förslag.

Samtidigt skapar generering en särskild kvalitetsfråga: ett språkligt övertygande svar är inte nödvändigtvis ett verifierat korrekt svar.

Detta är inte bara ett användargränssnittsproblem. Det påverkar hela lösningsarkitekturen.

Man behöver bland annat ta ställning till:

- vilket underlag modellen får,
- vilka instruktioner som styr den,
- om användaren behöver kunna se källor,
- hur svar kvalitetssäkras,
- vilka typer av output som är tillåtna,
- hur känslig information hanteras,
- om svaret bara är rådgivande eller får utlösa en åtgärd,
- vilken fallback som finns när modellen eller tjänsten inte är tillgänglig.

### Modell, prompt och kontext är delar av lösningen

I traditionell applikationsutveckling är det naturligt att versionera källkod. För generativ AI kan verksamhetsbeteendet dessutom påverkas av:

- modell och modellversion,
- systeminstruktioner och promptmallar,
- retrieval-konfiguration,
- embeddingmodell,
- kunskapskällor,
- verktyg som modellen får anropa,
- parametrar och guardrails.

Dessa behöver därför behandlas som **förvaltningsbara artefakter** när de påverkar viktiga verksamhetsutfall.

Det räcker inte att säga ”applikationskoden ändrades inte” om modellversionen eller den centrala prompten byttes ut och systemets beteende därmed förändrades.

## RAG – sökning plus generering

Retrieval-Augmented Generation, RAG, är ett mönster där en språkmodell kompletteras med information som hämtas från en extern kunskapskälla vid frågetillfället.[K1]

En förenklad struktur är:

```text
Fråga
  ↓
Sökning / retrieval
  ↓
Utvalda källpassager
  ↓
Prompt + kontext
  ↓
Språkmodell
  ↓
Genererat svar
```

Mönstret är attraktivt eftersom kunskapen inte enbart behöver finnas i modellens parametrar. En organisation kan koppla språkmodellen till interna eller mer aktuella informationskällor och ofta även göra källorna synliga för användaren.

Men RAG bör förstås som **en kedja av komponenter**, inte som en garanti för korrekta svar.

Fel kan uppstå i flera steg:

1. relevant dokument finns inte i kunskapsbasen,
2. dokumentet är inaktuellt,
3. indexeringen har tappat viktig struktur,
4. frågan omformuleras olämpligt,
5. retrievern väljer fel passager,
6. relevant information ryms inte i den kontext som skickas vidare,
7. språkmodellen tolkar underlaget fel,
8. modellen genererar ett påstående som inte stöds av källorna.

Det betyder att en RAG-lösning behöver utvärderas på mer än bara slutsvaret.

### Retrievalkvalitet och svarskvalitet är olika saker

En mycket viktig diagnosfråga är:

> **Hittade systemet rätt underlag?**

Om svaret är nej ligger problemet inte primärt i genereringen. Då kan förbättringen i stället handla om:

- bättre chunkning,
- metadata,
- indexering,
- filter,
- frågeexpansion,
- hybrid sökning,
- rankning,
- bättre källmaterial.

Om rätt underlag hämtades men svaret ändå blev fel ligger problemet längre ned i kedjan.

Den separationen är viktig både för kvalitet och för ansvar. Annars riskerar varje fel att mötas med ”vi behöver en bättre modell”, även när felet egentligen finns i dokumentkvalitet eller sökning.

### Källhänvisning hjälper – men löser inte allt

Att visa vilka källor som användes kan göra ett svar lättare att verifiera. Men en källhänvisning är inte i sig bevis för att påståendet stöds av källan.

Lösningen kan därför behöva mäta exempelvis:

- om rätt källor hämtades,
- om svaret faktiskt stöds av underlaget,
- om källhänvisningen pekar på relevant passage,
- om svaret innehåller påståenden som går utanför underlaget.

Det är särskilt viktigt när användningsfallet kräver hög verifierbarhet.

## Human-in-the-loop – mänsklig kontroll måste ha en funktion

Uttrycket **human-in-the-loop** används ofta som en generell riskreducerande åtgärd.[K2] Men att en människa finns någonstans i processen innebär inte automatiskt att kontrollen är meningsfull.

För mänsklig kontroll behöver man veta:

- vad människan förväntas kontrollera,
- vilken information personen får som stöd,
- om personen har mandat att avvisa resultatet,
- hur mycket tid kontrollen får ta,
- om systemet presenterar osäkerhet eller källor,
- hur automatiseringsbias motverkas,
- vad som händer när människa och modell bedömer olika.

En kontroll där en handläggare förväntas klicka ”godkänn” på hundratals AI-genererade förslag utan realistisk möjlighet att verifiera dem är inte stark mänsklig kontroll. Den är främst en extra interaktionspunkt.

Mänsklig kontroll bör därför dimensioneras efter **konsekvensen av fel** och den faktiska möjligheten att upptäcka felet.

### Human-on-the-loop och efterhandskontroll

Inte alla användningsfall kräver att en människa godkänner varje enskilt resultat. I vissa situationer kan en bättre modell vara att:

- automatisera lågkonsekvensfall,
- övervaka kvalitetsmått,
- stickprovsgranska resultat,
- eskalera osäkra eller avvikande fall,
- ha möjlighet att snabbt stoppa eller rulla tillbaka funktionen.

Det viktiga är inte etiketten på kontrollformen, utan att kontrollmekanismen är proportionerlig och verifierbar.

## Agentbaserade lösningar ökar konsekvensytan

En generativ AI-funktion som bara formulerar ett textförslag har en begränsad direkt konsekvensyta. En agent som kan anropa verktyg, läsa flera system och utföra åtgärder har en större.

Om en AI-komponent får möjlighet att exempelvis:

- söka i interna informationskällor,
- skapa eller ändra ärenden,
- skicka meddelanden,
- anropa externa API:er,
- generera och köra arbetssteg,

blir frågor om identitet, auktorisation, transaktionsgränser, loggning och återställning centrala.

Agenten bör inte få ett obegränsat tekniskt mandat bara för att den behöver kunna utföra flera steg. Samma principer som gäller för andra tekniska komponenter gäller även här:

- minsta nödvändiga behörighet,
- tydliga verktygsgränser,
- validerade in- och utdata,
- observerbara åtgärder,
- definierade fel- och fallbacklägen,
- möjlighet att stoppa eller återkalla handlingar där det är relevant.

Det gör agentfrågan till en kombination av flera förmågor. AI-förmågan hanterar modell- och inferensdelen, men **Identitet och tillit**, **Integration och kommunikation**, **Process och workflow** samt **Driftbarhet och motståndskraft** är fortfarande ansvariga för sina respektive mekanismer.

## Informationsgrundning börjar före modellen

Kvaliteten i en analys- eller AI-lösning kan aldrig separeras från kvaliteten i dess informationsunderlag.

Det gäller både klassiska modeller och generativ AI.

Några centrala frågor är:

- Är källan auktoritativ för det påstående vi vill göra?
- Är informationen tillräckligt aktuell?
- Är den komplett för användningsfallet?
- Har begreppen samma betydelse i de kombinerade källorna?
- Får informationen användas för detta ändamål?
- Kan vi spåra vilket underlag som användes?

Detta är en direkt koppling till kapitel 11 och 15.

En AI-plattform kan göra det enkelt att anropa en modell, men den kan inte automatiskt skapa korrekt informationsägarskap, bra dokument eller tydlig semantik.

Därför är ett vanligt anti-pattern att lägga stora resurser på modellval och promptar men mycket mindre på den kunskapsbas som modellen faktiskt ska använda.

## Utvärdering måste ske på systemnivå

En AI-lösning bör inte bedömas enbart genom att någon provar ett antal frågor och tycker att svaren ”ser bra ut”.

Utvärderingen behöver vara kopplad till användningsfallet och göras reproducerbar där detta är möjligt.

För ett RAG-baserat kunskapsstöd kan man exempelvis behöva bedöma:

- retrieval recall – hittas relevant underlag?
- precision eller relevans i de hämtade passagerna,
- om svaret stöds av källorna,
- om viktiga frågor besvaras korrekt,
- om systemet avstår när underlaget saknas,
- svarstid,
- kostnad per förfrågan,
- förekomst av olämpliga eller otillåtna svar,
- användarens möjlighet att verifiera resultatet.

För en klassificeringsmodell kan andra mått vara relevanta. För en sammanfattningsfunktion ytterligare andra.

Poängen är:

> **AI-kvalitet måste definieras per användningsfall – inte per modellfamilj.**

### Testmängden är en förvaltningsartefakt

Om ett AI-system är verksamhetsmässigt viktigt behöver organisationen ofta en uppsättning representativa testfall som kan köras om när modellen, prompten, retrievalkedjan eller källmaterialet ändras.

Testmängden kan innehålla:

- typiska fall,
- svåra fall,
- kända riskfall,
- gränsfall,
- frågor där systemet bör avstå,
- säkerhetsrelaterade prov,
- fall som tidigare gett fel.

Den blir då en del av förvaltningen, på samma sätt som regressionstester är en del av traditionell programvaruförvaltning.

Men testdata behöver också livscykelhanteras. Om verkligheten förändras kan en gammal testmängd ge en falsk bild av kvaliteten.

## Drift, förändring och modellbeteende

Traditionell observerbarhet fokuserar ofta på tekniska signaler som svarstid, felprocent och resursanvändning. Dessa är viktiga även för analys- och AI-tjänster, men räcker inte alltid.

En lösning kan tekniskt svara med HTTP 200 och samtidigt producera undermåliga resultat.

Därför kan man behöva följa ytterligare signaler som:

- kvalitetsmått över tid,
- förändringar i inputdata,
- förändringar i svarsmönster,
- andel eskalerade eller avvisade resultat,
- retrievalkvalitet,
- kostnadsutveckling,
- modell- och promptversion,
- vilken kunskapsbas som användes.

För klassiska ML-system brukar förändringar i datadistribution eller samband beskrivas som olika former av drift. Oavsett terminologi behöver verksamheten kunna upptäcka när förutsättningarna för modellens tidigare kvalitet inte längre gäller.

### En extern modell kan förändra förvaltningsmodellen

Om en organisation konsumerar en hanterad modell som tjänst kan leverantören kontrollera delar av modellens livscykel. Då behöver konsumenten förstå bland annat:

- om en bestämd modellversion kan låsas,
- hur länge versionen stöds,
- hur förändringar annonseras,
- om beteendet kan förändras utan egen driftsättning,
- hur data behandlas,
- vilka loggar och mätvärden som är tillgängliga,
- hur exit eller byte av leverantör kan genomföras.

Detta är ett exempel på hur en enkel API-integration kan bära betydande arkitektoniska konsekvenser.

## Kvalitetskrav för analys-, sök- och AI-förmågan

De generella kvalitetsdimensionerna från kapitel 4 får särskilda uttryck här.

### Korrekthet och verifierbarhet

För sökning handlar kvalitet om att relevanta resultat hittas och rankas användbart. För analys handlar den bland annat om korrekt data, transformation och semantik. För ML handlar den om modellens förmåga i den aktuella användningen. För generativ AI behöver även graden av stöd i källunderlaget bedömas.

### Spårbarhet

För verksamhetsmässigt betydelsefulla resultat kan man behöva kunna identifiera:

- källdata,
- modellversion,
- prompt eller konfiguration,
- relevanta retrievalresultat,
- tidpunkt,
- användare eller anropande tjänst,
- efterföljande mänsklig bedömning.

Spårbarhetens omfattning ska vara proportionerlig mot konsekvensen.

### Informationsskydd

Data som används i analys eller AI upphör inte att vara skyddsvärd bara för att den skickas till en modell- eller analystjänst. Informationsklassning och regler för behandling gäller genom hela kedjan.

Detta omfattar även:

- prompts,
- kontext,
- embeddings där dessa kan innebära informationsrisk,
- mellanlagring,
- loggar,
- tränings- och utvärderingsdata,
- genererade svar.

### Tillgänglighet och fallback

En AI-funktion kan vara användbar utan att vara verksamhetskritisk. I andra lösningar kan den ligga i en central arbetsprocess.

Arkitekturen behöver därför definiera vad som händer om tjänsten är:

- otillgänglig,
- långsam,
- för dyr att använda i normal omfattning,
- osäker på svaret,
- blockerad av en säkerhetskontroll.

Fallback kan exempelvis vara manuell handläggning, traditionell sökning, en förenklad regelbaserad funktion eller att funktionen tillfälligt inte erbjuds.

### Kostnad och kapacitet

AI-tjänster kan ha en kostnadsprofil som skiljer sig från traditionell applikationsdrift. Kostnaden kan exempelvis bero på användningsvolym, mängd behandlad text, modellval och antalet steg i en agent- eller retrievalkedja.

Därför behöver kostnad kunna följas per relevant användningsfall och inte bara som en total plattformsfaktura.

## Ansvar på tre nivåer

Den tredelade ansvarmodellen från kapitel 7 är särskilt viktig i ett område med hög teknisk förändringstakt.

### Gemensam arkitekturnivå

På den gemensamma nivån bör organisationen bland annat kunna etablera:

- gemensamma principer för användning av AI och sekundära analyslager,
- övergripande krav på informationsskydd och spårbarhet,
- gemensam terminologi för deterministiska och probabilistiska resultat,
- riskbaserade principer för mänsklig kontroll,
- gemensamma regler för livscykel och utvärdering,
- gränser mot identitet, data, integration och andra förmågor.

Den gemensamma nivån behöver däremot inte välja exakt modell eller sökalgoritm för varje verksamhetsfall.

### Förmågenivå

De som ansvarar för Analys, sökning och AI kan exempelvis ansvara för:

- sök- och indexeringserbjudanden,
- BI- och rapporteringstjänster,
- gemensam åtkomst till modeller,
- RAG-/kunskapstjänster där återanvändning är motiverad,
- mallar för modell- och promptversionering,
- utvärderingsramverk,
- observerbarhet för AI-specifika signaler,
- guardrails och godkända integrationsmönster,
- vägledning för kostnad och kapacitet.

Förmågeansvaret bör göra det lättare att använda tekniken kontrollerat, inte ta över verksamhetens ansvar för information och konsekvenser.

### Lösnings-/produktnivå

Den konkreta lösningen behöver fortfarande avgöra:

- vilket problem som faktiskt ska lösas,
- om AI behövs,
- vilka källor som får användas,
- vilka kvalitetsmått som är relevanta,
- hur resultatet används i arbetsprocessen,
- vilka konsekvenser ett fel får,
- om mänsklig kontroll behövs,
- vilken fallback som krävs,
- hur lösningen följs upp i produktion.

Det är alltså inte den gemensamma AI-plattformen som äger verksamhetsbeslutet om hur ett modellresultat får användas.

## Vanliga anti-patterns

### AI först, problem sedan

Organisationen börjar med en vald modell eller plattform och letar därefter efter användningsfall. Resultatet blir lätt hög komplexitet med oklar nytta.

### RAG som sanningsmotor

Ett RAG-system antas ge korrekta svar bara för att det använder interna dokument. Retrieval- och genereringsfel, inaktuella källor och bristande semantik ignoreras.

### Modellen äger verksamhetsbeslutet

Ett sannolikhetsvärde används som om det vore ett explicit verksamhetsbeslut utan att gräns, ansvar och konsekvens har definierats.

### Human-in-the-loop som dekor

En människa placeras formellt i processen men saknar tid, underlag eller mandat för verklig kontroll.

### Gemensam AI-plattform som central verksamhetslogik

Plattformsteamet börjar förvalta verksamhetsspecifika prompts, kunskapskällor och beslutskriterier för många domäner. Ägarskapet blir otydligt och plattformen växer till en central verksamhetskomponent.

### En modell för alla behov

Sökning, klassificering, sammanfattning och regelstyrning försöker lösas med samma generativa modell trots att enklare och mer förutsägbara tekniker passar vissa behov bättre.

### Demo som acceptanstest

Några imponerande manuella exempel används som bevis för produktionskvalitet. Representativa testfall, negativa test och löpande uppföljning saknas.

### Ospårade förändringar

Modell, prompt, retrievalkonfiguration eller kunskapskälla ändras utan att organisationen kan koppla förändringen till ändrat beteende i produktion.

## En praktisk analysordning

När ett nytt behov inom analys, sökning eller AI uppstår kan följande ordning användas.

### 1. Formulera informationsuppgiften

Är uppgiften att hitta, sammanställa, analysera, klassificera, förutsäga eller generera?

Undvik att formulera behovet som en produkt eller modell.

### 2. Identifiera informationskällorna

Vilka källor behövs, vem äger dem och hur aktuella måste de vara?

### 3. Avgör om resultatet måste vara deterministiskt

Om samma villkor alltid måste ge samma normativt definierade beslut är en explicit regel- eller beslutslösning ofta mer naturlig än AI.

### 4. Beskriv konsekvensen av fel

Vad händer om ett relevant dokument inte hittas, ett nyckeltal är fel, modellen klassificerar fel eller ett genererat svar innehåller ett felaktigt påstående?

### 5. Välj den enklaste lämpliga mekanismen

Pröva om behovet kan lösas med exempelvis:

- strukturerad fråga,
- fulltextsökning,
- semantisk eller hybrid sökning,
- BI/analys,
- explicit regel,
- ML,
- generativ AI,
- en kombination.

### 6. Definiera kvalitetsmått innan produktionssättning

Bestäm hur lösningen ska bedömas och vilka testfall som krävs.

### 7. Definiera spårbarhet och mänsklig kontroll

Avgör vilka artefakter som måste versioneras och om resultat behöver granskas, godkännas eller kunna följas upp i efterhand.

### 8. Definiera fallback och stoppmekanism

Bestäm vad som händer när tjänsten är otillgänglig eller kvaliteten inte är tillräcklig.

### 9. Följ upp faktisk verksamhetsnytta

Mät inte bara teknisk modellkvalitet. Följ upp om lösningen faktiskt förbättrar det verksamhetsproblem som motiverade den.

Den sista punkten sluter cirkeln tillbaka till bokens första delar: en gemensam förmåga är värdefull när den hjälper lösningar att möta verkliga behov, inte när den bara gör ny teknik tillgänglig.

## Förmågan som konsumerbart stöd

Ett stödjande IT-område bör inte beskriva Analys, sökning och AI som ”vi har produkt X” eller ”vi erbjuder en LLM”. Ett konsumerbart erbjudande behöver beskriva vad utvecklingsområdet faktiskt kan få hjälp med.

Exempel på sådana erbjudanden kan vara:

- **Search & Indexing Service** – indexering, sökning, relevansmekanismer och standardiserade driftfunktioner,
- **BI & Reporting Service** – gemensam plattform för analys och rapportering,
- **Managed LLM Service** – kontrollerad åtkomst till godkända språkmodeller,
- **RAG/Knowledge Service** – gemensamma mekanismer för retrieval, indexering och generering över godkända kunskapskällor,
- **Model Evaluation Support** – gemensamma verktyg och arbetssätt för utvärdering och regressionstest.

Men varje erbjudande behöver fortfarande tydliggöra:

- vad plattformen ansvarar för,
- vad konsumenten ansvarar för,
- vilka informationsklasser som stöds,
- vilka kvalitets- och tillgänglighetsnivåer som erbjuds,
- hur kostnader fördelas eller synliggörs,
- hur modeller och andra beroenden livscykelhanteras,
- hur en konsument kan lämna tjänsten.

Det är denna tjänstemässiga form som gör förmågan återanvändbar utan att göra alla lösningar identiska.

## Sammanfattning

Analys, sökning och AI är en gemensam IT-förmåga eftersom många utvecklingsområden behöver liknande tekniska mekanismer för att hitta, sammanställa och härleda information. Men förmågan blir användbar först när skillnaderna mellan mekanismerna bevaras.

Sökning handlar om att hitta relevant information i sekundära representationer. BI och analys handlar om att skapa förståelse och uppföljning ur data. Maskininlärning producerar probabilistisk inferens utifrån modeller. Generativ AI skapar nytt innehåll och behöver därför hanteras med särskild uppmärksamhet på grundning, verifierbarhet och beteende över tid.

RAG kombinerar retrieval och generering men eliminerar inte felkällor. Human-in-the-loop är värdefullt bara när den mänskliga kontrollen är faktiskt genomförbar. Agentbaserade lösningar måste följa samma principer för identitet, behörighet, integration och återställning som andra tekniska komponenter.

Det mest stabila arkitekturvalet är därför inte att standardisera en viss AI-modell. Det är att standardisera **ansvar, kvalitetskrav, informationsskydd, spårbarhet, utvärdering och konsumerbara plattformsmekanismer**, samtidigt som den konkreta lösningen får välja den enklaste teknik som möter behovet.

I nästa kapitel flyttas fokus från bearbetning av information till hur system och domäner kommunicerar med varandra: **Integration och kommunikation**.

## Källor och vidare läsning

**[K1]** Patrick Lewis m.fl., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (2020). https://arxiv.org/abs/2005.11401

**[K2]** NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)* samt *NIST AI 600-1: Generative Artificial Intelligence Profile*. https://www.nist.gov/itl/ai-risk-management-framework och https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
