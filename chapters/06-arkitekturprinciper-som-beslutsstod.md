# 6. Arkitekturprinciper som beslutsstöd

Ett enskilt arkitekturbeslut kan dokumenteras i en ADR, motiveras med kvalitetskrav och omprövas när förutsättningarna ändras. Men i en större organisation återkommer många beslutssituationer gång på gång.

Ska ett team använda ett gemensamt plattformserbjudande eller bygga en egen lösning? Ska ett behov uttryckas produktoberoende eller direkt i termer av den teknik som redan finns? Ska säkerhet och driftbarhet hanteras i efterhand eller byggas in från början? När är återanvändning önskvärd, och när är en lokal speciallösning motiverad?

Om varje team behöver börja om från noll i sådana frågor blir beslutsfattandet dyrt och inkonsekvent. Samtidigt är det sällan klokt att ersätta bedömning med detaljerade regler för varje tänkbar situation.

Här fyller **arkitekturprinciper** en viktig funktion.

En arkitekturprincip uttrycker en relativt stabil beslutsriktning. Den säger inte exakt vilken produkt eller konfiguration som ska väljas, men den gör organisationens viktigaste utgångspunkter tydliga innan det konkreta beslutet behöver fattas.

Principer kan därmed fungera som en brygga mellan strategi och vardagliga arkitekturval:

```text
Mål, behov och återkommande erfarenheter
                 ↓
        Arkitekturprinciper
                 ↓
        Konkreta beslut
                 ↓
  Mönster, standarder och plattformar
                 ↓
        Tekniska lösningar
```

En bra princip reducerar alltså inte arkitektur till lydnad. Den hjälper människor att fatta mer konsekventa beslut utan att varje situation måste regleras i detalj.

## Principer är inte regler med finare namn

Det är lätt att blanda ihop principer med krav, standarder och policies.

Jämför följande formuleringar:

> Kommunikation mellan tjänster ska ske med HTTPS och minst den TLS-version som anges i organisationens säkerhetsstandard.

Detta är i första hand ett tekniskt krav eller en standardregel. Det är konkret, verifierbart och relativt nära realiseringen.

Jämför med:

> Säkerhet och andra relevanta kvaliteter ska byggas in i lösningen från början.

Det är en princip. Den säger något om *hur organisationen bör tänka*, men inte exakt vilka protokoll eller mekanismer som ska användas i varje situation.

En tredje formulering kan vara:

> Använd organisationens API Management-tjänst för exponerade API:er enligt tjänstekontraktet.

Det är snarare en styrning mot ett specifikt gemensamt erbjudande.

Skillnaden kan förenklas så här:

| Typ | Huvudfråga | Exempel |
|---|---|---|
| Princip | Vilken generell beslutsriktning ska vi ha? | Behov före teknik. |
| Mönster | Hur kan ett återkommande lösningsproblem struktureras? | Backend for Frontend. |
| Standard | Vilken gemensam teknisk regel eller rekommendation gäller? | API-standard. |
| Plattformserbjudande | Vilken gemensam tjänst kan konsumeras? | API Management. |
| Lokalt beslut | Vad väljer vi i just denna lösning? | Använd erbjudandet för dessa API:er. |

En princip som försöker innehålla produktnamn, versionsnummer och detaljerade implementationer blir därför ofta för kortlivad. Omvänt blir en princip som bara säger att organisationen ska ”bygga bra och säkra lösningar” så allmän att den inte hjälper någon att välja.

Den användbara nivån ligger mellan dessa ytterligheter.

## Vad en användbar princip behöver åstadkomma

En princip är värdefull först när den påverkar verkliga beslut.

Det räcker inte att den låter klok på en presentationsbild.

En användbar arkitekturprincip bör normalt ha flera egenskaper.

### Den ska uttrycka en verklig prioritering

En princip bör säga något som faktiskt kan påverka ett val.

”Vi ska använda lämplig teknik” är nästan omöjlig att invända mot, men hjälper inte när två alternativ konkurrerar.

”Behov före teknik” uttrycker däremot en verklig prioritering: behov och kvalitetskrav ska styra formuleringen av problemet före dagens produktlandskap.

Det betyder inte att befintlig teknik ignoreras. Kapitel 3 visade att installerad teknik kan vara en verklig begränsning eller ett ekonomiskt relevant alternativ. Principen säger däremot att tekniken inte automatiskt får definiera behovet.

### Den ska vara tillräckligt stabil

En gemensam princip bör normalt överleva fler produktgenerationer än en teknisk standard.

Om organisationen byter containerplattform behöver principen ”separera stabil arkitektur från föränderlig teknik” fortfarande vara meningsfull. En princip som säger ”alla tjänster ska köras i produkt X” gör det inte.

Detta hänger ihop med metamodellen i kapitel 2. Ju högre upp ett artefaktslag ligger i abstraktionskedjan, desto större skäl finns att hålla det relativt oberoende av dagens realisering.

### Den ska kunna få konsekvenser

En princip bör göra det möjligt att fråga:

> Om vi tar den här principen på allvar, vad förändras då i vårt beslut?

Om svaret är ”ingenting” är formuleringen sannolikt för vag.

Principen ”livscykel och förvaltning beaktas vid beslut” kan exempelvis innebära att ett tekniskt alternativ med snabbare initial utveckling ändå väljs bort om det medför oproportionerligt hög förvaltningskostnad, svår uppgradering eller oacceptabel leverantörsrisk.

### Den ska kunna användas tillsammans med andra principer

Principer verkar sällan ensamma.

”Återanvändning före lokal speciallösning” kan tala för ett gemensamt erbjudande. ”Standardiserade erbjudanden när de möter behovet” lägger samtidigt in ett viktigt villkor: återanvändning är inte ett självändamål.

Om standarderbjudandet inte klarar lösningens centrala kvalitetskrav kan ett avsteg vara rationellt.

Principer ska därför inte behandlas som absoluta lagar som alltid ger ett entydigt svar. De är beslutsdrivare som behöver vägas mot behov, kvaliteter och andra principer.

## Tio principer som exempel på en sammanhängande principuppsättning

Det arkitekturunderlag som ligger till grund för denna bok innehåller tio gemensamma principer. De är användbara som exempel därför att de tillsammans täcker flera återkommande beslutssituationer utan att gå hela vägen ner till specifika produkter.

De är inte universella regler som varje organisation måste använda ordagrant. De visar snarare hur en principuppsättning kan byggas för att stödja den modell som boken beskriver.

## 1. Behov före teknik

Principen säger i korthet att tekniska lösningar och tekniska krav ska härledas från identifierade behov, kvalitetskrav och verkliga begränsningar.

Den motverkar ett vanligt mönster:

```text
Befintlig produkt
      ↓
Produktens egenskaper och begränsningar
      ↓
Formuleras om till "krav"
      ↓
Alla lösningar anpassas efter samma antagande
```

I stället eftersträvas:

```text
Verksamhetsbehov och kvalitetskrav
              ↓
      Relevanta begränsningar
              ↓
        Arkitekturalternativ
              ↓
        Teknisk realisering
```

Principen är central eftersom den skyddar skillnaden mellan *mål* och *medel*. Den gör också framtida teknikbyten lättare: om behovsbilden är formulerad oberoende av en viss produkt kan nya realiseringar utvärderas mot samma behov.

Kapitel 3 behandlade denna princip i detalj. I principuppsättningen fungerar den som ett återkommande kontrollfrågetecken: har vi formulerat problemet före lösningen?

## 2. Standardiserade erbjudanden när de möter behovet

En organisation investerar ofta betydande resurser i gemensamma plattformar, tjänster och standarder. Om varje team ändå bygger egna varianter går skalfördelar, säkerhetsarbete och samlad kompetens förlorade.

Det innebär inte att det gemensamma alltid ska användas.

Den avgörande delen av principen är **när de möter behovet**.

Detta skapar en balanserad grundregel:

> Återanvänd det gemensamma där det är ändamålsenligt, men gör inte standardisering till ett mål i sig.

Principen hjälper till att undvika två motsatta problem.

Det ena är **lokal uppfinningslust**: varje team väljer egen teknik även när ett gemensamt erbjudande löser samma problem tillräckligt väl.

Det andra är **central tvångsstandardisering**: alla tvingas in i samma lösning även när viktiga behov eller kvalitetskrav faktiskt skiljer sig.

Det är först när standarderbjudandets tjänstekontrakt, egenskaper och begränsningar är synliga som principen kan användas på ett seriöst sätt. Därför leder den senare naturligt vidare till bokens delar om plattformar som produkter och standarder som guardrails.

## 3. Problem löses på lämplig arkitekturnivå

Många tekniska landskap blir onödigt komplexa därför att problem löses på fel nivå.

Ett applikationsproblem kan exempelvis kompenseras med speciallogik i nätverket. Ett plattformsproblem kan lösas separat i varje applikation. Ett informationsproblem kan döljas bakom ytterligare integrationslager.

Principen säger att problemet så långt som möjligt bör lösas där det naturligt hör hemma.

Det innebär bland annat att fråga:

- Är detta ett organisationsgemensamt problem?
- Är det ett problem inom en viss IT-förmåga?
- Är det ett lokalt lösningsproblem?
- Är det egentligen ett informations- eller domänproblem?
- Är det en egenskap som plattformen bör erbjuda en gång i stället för att varje applikation implementerar den?

Principen är nära kopplad till den ansvarsfördelning som introduceras i kapitel 7. Den motverkar både övercentralisering och onödig duplicering.

Ett problem som endast finns i en viss verksamhetsdomän behöver inte automatiskt bli en central plattformsfunktion. Omvänt bör exempelvis en generell mekanism för hemlighetshantering normalt inte uppfinnas på nytt av varje applikation.

## 4. Ansvar och gränssnitt ska vara tydliga

Återanvändning fungerar dåligt när det är oklart vem som ansvarar för vad.

En gemensam tjänst som bara beskrivs med tekniknamn lämnar ofta många frågor obesvarade:

- Vad lovar tjänsten konsumenten?
- Vilka kvalitetsnivåer ingår?
- Vad måste konsumenten själv konfigurera och övervaka?
- Vem hanterar incidenter?
- Vem ansvarar för uppgraderingar?
- Vad händer när tjänsten förändras eller avvecklas?

Principen gör därför **tjänstekontrakt och ansvarssnitt** till en arkitekturfråga, inte bara en organisatorisk detalj.

Den underliggande tekniska komplexiteten bör abstraheras där det är ändamålsenligt, men abstraktionen får inte dölja ansvar.

Ett bra plattformserbjudande reducerar det som varje konsument måste förstå. Det innebär inte att konsumenten saknar ansvar. Tvärtom blir gränsen tydligare: plattformsområdet ansvarar för vissa egenskaper och mekanismer, medan lösnings- eller produktteamet ansvarar för hur tjänsten används i den konkreta lösningen.

## 5. Säkerhet och andra kvaliteter byggs in

Kapitel 4 visade att kvalitetsattribut ofta är arkitekturdrivande. Denna princip gör samma insikt till en återkommande beslutsriktning.

Säkerhet, tillgänglighet, kontinuitet, spårbarhet, användbarhet och andra relevanta kvaliteter ska inte behandlas som efterkontroller som läggs ovanpå en färdig funktionell lösning.

De behöver påverka arkitekturen från början.

Detta är särskilt viktigt för kvaliteter som skär genom flera lager. Om säkerhet behandlas som ett separat teknikområde riskerar den att reduceras till komponenter vid sidan av den egentliga lösningen. Samma sak gäller driftbarhet: loggning, mätvärden, tracing, larm och återställningsförmåga blir betydligt dyrare att lägga till när systemets struktur redan är låst.

Principen betyder inte att alla lösningar ska ha samma säkerhets- eller tillgänglighetsnivå. Nivån ska fortfarande härledas från behov och konsekvens. Det som ska vara gemensamt är att relevanta kvaliteter beaktas som en del av designen.

## 6. Separation mellan stabil arkitektur och föränderlig teknik

Denna princip skyddar själva arkitekturmodellens livslängd.

Förmågor, behov och principer förändras vanligtvis långsammare än produkter, versioner och konfigurationer. Om de blandas ihop blir varje teknikbyte ett arkitekturprojekt.

Anta att en organisation beskriver en förmåga som:

> Förmåga att köra OpenShift-baserade applikationer.

Då har en viss produkt byggts in i förmågedefinitionen.

En stabilare formulering är:

> Förmåga att exekvera och drifta applikationer med definierade egenskaper för isolering, skalning, driftsättning och driftbarhet.

OpenShift kan vara dagens realisering, men förmågan kan bestå även om produkten ersätts.

Principen är inte ett argument för maximal abstraktion. På realiseringsnivån måste produkter och versioner naturligtvis vara explicita. Poängen är att varje begrepp ska leva på rätt nivå i modellen.

## 7. Återanvändning före lokal speciallösning

Återanvändning är en av de huvudsakliga anledningarna till att etablera gemensam IT-arkitektur över huvud taget.

När flera team behöver liknande funktioner kan gemensamma komponenter, tjänster och mönster ge:

- mindre duplicerat arbete,
- samlad kompetens,
- mer konsekvent säkerhet,
- enklare support,
- snabbare onboarding,
- bättre möjligheter till automatisering.

Men principen behöver läsas tillsammans med behovsprincipen och principen om standardiserade erbjudanden.

Återanvändning är rationell när det återanvända faktiskt möter behovet. En lokal speciallösning kan vara berättigad när verksamhetsbehov, kvalitetskrav, juridiska förutsättningar eller andra begränsningar avviker på ett sätt som det gemensamma erbjudandet inte stödjer.

Det viktiga är att skillnaden är verklig och synlig, inte bara uttryck för lokal vana eller preferens.

## 8. Automatisering och reproducerbarhet eftersträvas

Gemensam arkitektur handlar inte bara om strukturdiagram och komponentval. Hur lösningar byggs, testas, konfigureras och driftsätts påverkar kvalitet, risk och förvaltningsbarhet.

Principen säger därför att återkommande tekniska processer bör automatiseras där det är praktiskt och proportionerligt.

Reproducerbarhet innebär att samma definierade indata så långt som möjligt kan ge samma förväntade resultat utan beroende av en enskild persons manuella steg.

Det kan gälla:

- byggprocesser,
- test,
- driftsättning,
- infrastruktur,
- konfiguration,
- policykontroller,
- säkerhetskontroller,
- återställningsprocedurer.

Automatisering är dock inte ett självändamål. Att automatisera en sällsynt och enkel engångsaktivitet kan kosta mer än det ger. Principen behöver därför alltid läsas med proportionalitet i åtanke.

Senare kapitel om programvaruutveckling och leverans fördjupar hur denna princip kan realiseras.

## 9. Livscykel och förvaltning beaktas vid beslut

Teknikval bedöms ofta i det ögonblick de införs. Den kortaste vägen till första leverans får då oproportionerligt stor vikt.

Men en lösning ska därefter:

- drivas,
- övervakas,
- supporteras,
- förändras,
- uppgraderas,
- kompetensförsörjas,
- kostnadsstyras,
- till slut avvecklas.

Principen gör därför hela livscykeln till en del av beslutet.

Ett alternativ som ser billigt ut under projektets första sex månader kan bli dyrt under fem års drift. Ett populärt bibliotek kan vara snabbt att börja med men ha en livscykel som inte passar organisationens supportmodell. En egenbyggd komponent kan lösa ett lokalt problem elegant men skapa ett långsiktigt ägaransvar som ingen planerat för.

Principen kopplar därmed direkt tillbaka till kapitel 5: konsekvenser och teknisk skuld ska inte döljas bara för att den första implementationen går fort.

## 10. Avsteg ska kunna motiveras

En principuppsättning utan möjlighet till välgrundade avsteg riskerar att bli dogmatisk.

Samtidigt förlorar principer och standarder sitt värde om varje team fritt kan ignorera dem utan att göra skälen synliga.

Den balanserade ståndpunkten är därför att avsteg ska kunna motiveras.

Det innebär att organisationen behöver kunna se:

- vilket behov eller kvalitetskrav standardvägen inte möter,
- vilket alternativ som väljs,
- vilka konsekvenser och risker som accepteras,
- vem som äger den extra komplexiteten,
- om avsteget är tillfälligt eller långsiktigt.

Minst lika viktigt är vad som händer när samma avsteg återkommer.

Om fem team oberoende av varandra behöver göra samma undantag är det inte längre bara ett lokalt problem. Det kan vara evidens för att:

- standarden är fel utformad,
- plattformserbjudandet saknar en viktig funktion,
- tjänstekontraktet är för snävt,
- förmågekartan behöver justeras,
- ett nytt lösningsmönster behövs.

Avsteg kan därmed fungera som återkoppling till den gemensamma arkitekturen.

Den organisatoriska processen för mandat, godkännande och förvaltning av avsteg behandlas först i kapitel 37. Här är poängen principiell: ett undantag ska vara ett synligt arkitekturbeslut, inte en dold genväg.

## Principer måste kunna stå i spänning med varandra

En principuppsättning blir missvisande om den presenteras som om alla principer alltid pekar åt samma håll.

Anta att ett team behöver en ny funktion för mycket hög meddelandevolym. Organisationen har redan ett gemensamt messaging-erbjudande.

Flera principer blir relevanta:

- standardiserade erbjudanden när de möter behovet,
- återanvändning före lokal speciallösning,
- behov före teknik,
- livscykel och förvaltning beaktas,
- avsteg ska kunna motiveras.

Om det gemensamma erbjudandet klarar volym, latens, leveransgarantier och driftkrav är återanvändning sannolikt det starkaste alternativet.

Om det inte gör det kan samma principuppsättning stödja ett avsteg. Behovet och kvalitetskraven väger då tyngre än återanvändning för återanvändningens skull.

Detta är viktigt: **principerna ska göra resonemanget mer konsekvent, inte eliminera avvägningar**.

Kapitel 5 behövs fortfarande. En principuppsättning är inte en beslutsmotor som automatiskt producerar rätt svar.

## Hierarki eller jämbördiga principer?

Organisationer frestas ibland att numrera principer och sedan anta att P1 alltid är viktigare än P2, P2 viktigare än P3 och så vidare.

Det kan vara praktiskt i vissa mycket specifika sammanhang, men en generell rangordning blir ofta konstgjord.

Behov före teknik är exempelvis grundläggande, men det betyder inte att kostnad, regulatoriska begränsningar eller befintliga strategiska investeringar saknar betydelse. Säkerhet som inbyggd kvalitet är viktig, men den konkreta säkerhetsnivån måste fortfarande stå i proportion till information, hot och konsekvens.

Det är därför ofta bättre att se principerna som **gemensamma utgångspunkter med tydlig motivering**, inte som en mekanisk prioriteringslista.

När två principer drar åt olika håll behöver det konkreta beslutet återgå till:

1. behovet,
2. kvalitetskraven,
3. begränsningar,
4. riskerna,
5. beslutets konsekvenser.

Principerna hjälper då till att strukturera analysen.

## Princip, motivering och konsekvens

En kort principformulering blir starkare om den kompletteras med varför den finns och vilka konsekvenser den normalt får.

Ett enkelt format är:

### Princip

En kort, minnesvärd formulering.

### Motivering

Vilket återkommande problem eller vilken strategisk riktning principen adresserar.

### Konsekvenser

Vad principen typiskt betyder för beslut, ansvar och arbetssätt.

Exempel:

**Princip:** Behov före teknik.

**Motivering:** Om dagens produktlandskap får definiera morgondagens krav cementeras historiska begränsningar och alternativa realiseringar blir svåra att utvärdera.

**Konsekvenser:** Behov och kvalitetskrav ska formuleras innan produktval. Produktbegränsningar får behandlas som begränsningar när de verkligen är bindande, men ska inte automatiskt generaliseras till alla lösningar.

Detta format gör principen lättare att använda än enbart ett slagord.

I vissa organisationer läggs även exempel, implikationer, ägare eller relaterade standarder till. Det kan vara värdefullt, men då bör man vara försiktig så att principdokumentet inte sväller till en blandning av princip, policy och teknisk katalog.

## För många principer är nästan lika illa som inga

Om en organisation har femtio eller hundra ”principer” uppstår ett praktiskt problem: nästan ingen kan minnas eller använda dem i vardagliga beslut.

Det är ofta ett tecken på att flera olika artefakttyper har blandats ihop.

Vissa formuleringar kanske egentligen är:

- tekniska standarder,
- säkerhetskrav,
- kodningsregler,
- plattformsinstruktioner,
- processkrav,
- rekommendationer.

En liten uppsättning starka arkitekturprinciper kan vara mer styrande än en stor lista av detaljregler eftersom de är lättare att internalisera och använda i nya situationer.

Poängen är inte att organisationen ska ha få tekniska regler. Det betyder att de tekniska reglerna bör ligga där de hör hemma – exempelvis i standarder och tjänstekontrakt – i stället för att kallas principer.

## Principer på olika nivåer

Bokens tredelning mellan gemensam nivå, förmågenivå och lösnings-/produktnivå är användbar även här.

### Gemensam nivå

Här hör principer hemma som behöver vara relativt stabila och gälla över flera förmågor, exempelvis:

- behov före teknik,
- kvaliteter byggs in,
- ansvar ska vara tydliga,
- livscykeln beaktas.

De skapar en gemensam beslutslogik.

### Förmågenivå

Ett förmågeområde kan behöva mer specifika principer som fortfarande är teknikoberoende.

Integration och kommunikation kan exempelvis behöva principer om kontraktsägarskap, koppling eller när synkron respektive asynkron interaktion är lämplig.

Dataområdet kan behöva principer om informationsägarskap, härledda kopior eller livscykel.

Sådana principer bör vara förenliga med de gemensamma principerna men får vara mer domänspecifika.

### Lösnings-/produktnivå

Här behövs normalt färre långlivade ”principer” och fler konkreta arkitekturbeslut.

Ett produktteam kan naturligtvis ha lokala designprinciper, men de ska inte automatiskt upphöjas till organisationsgemensam arkitektur. Det som är optimalt för en lösning är inte nödvändigtvis ett generellt mönster.

Denna nivåskillnad minskar risken att lokal erfarenhet generaliseras för snabbt.

## Från återkommande beslut till princip

Hur uppstår då en bra princip?

En sund väg är ofta att börja i verkliga beslut och återkommande problem.

Anta att flera team under några år har haft problem med plattformsspecifika krav som läckt in i verksamhetskrav. Organisationen ser samma typ av teknisk inlåsning och svårigheter vid modernisering.

Efter flera sådana erfarenheter finns underlag för en stabilare riktning:

> Behov före teknik.

På samma sätt kan återkommande problem med egenbyggda driftmekanismer ge stöd för principen att gemensamma erbjudanden ska återanvändas när de möter behovet.

En princip bör alltså helst inte uppstå bara därför att den låter modern eller hämtats från en extern trendrapport. Den bör ha en tydlig koppling till organisationens mål, risker eller återkommande beslutsmönster.

Det skapar också bättre förutsättningar för acceptans. Människor förstår varför principen finns.

## Från princip till konkret styrsignal

En princip blir verkligt användbar först när den kan realiseras genom andra artefakter.

Exempel:

```text
Princip: Återanvändning före lokal speciallösning
                     ↓
           Lösningsmönster
                     ↓
        Plattformserbjudanden
                     ↓
         Tekniska standarder
                     ↓
        Golden paths / automation
                     ↓
        Konkreta lösningsbeslut
```

Principen i sig tillhandahåller inte återanvändning. Den behöver stödjas av erbjudanden som faktiskt är användbara.

Om organisationen säger ”använd gemensamma plattformar” men plattformarna är svåra att beställa, saknar dokumentation eller inte uppfyller rimliga kvalitetskrav kommer principen att uppfattas som administrativ styrning snarare än stöd.

Detta leder till en viktig slutsats:

> En arkitekturprincip skapar en förväntan även på den organisation som formulerar den.

Om team förväntas återanvända gemensamma erbjudanden måste de gemensamma områdena erbjuda något som är värt att återanvända.

Om team förväntas automatisera och arbeta reproducerbart behöver plattformar och verktyg stödja det.

Om kvaliteter ska byggas in från början behöver kvalitetskrav, mönster och plattformsförmågor vara tillgängliga tidigt i utvecklingen.

Principer är därför inte bara krav nedåt i organisationen. De kan också uttrycka vad den gemensamma arkitekturen och plattformsorganisationen behöver möjliggöra.

## När en princip bör omprövas

Principer är avsiktligt stabila, men stabilitet är inte samma sak som evighet.

En princip bör kunna omprövas när:

- organisationens mål förändras,
- lagstiftning eller riskbild förändras,
- återkommande avsteg visar att principen inte fungerar,
- teknikutveckling ändrar grundläggande förutsättningar,
- principen inte längre påverkar beslut,
- två principer skapar systematiska konflikter,
- formuleringen är så vag att olika grupper tolkar den helt olika.

Det är dock viktigt att skilja på att **principen** behöver ändras och att **realiseringen** förändras.

När en produkt går ur support är det normalt produktstandarden eller plattformens tekniska realisering som ska ändras, inte principen om exempelvis återanvändning eller livscykelhantering.

Det är ännu ett exempel på varför separationen mellan stabil arkitektur och föränderlig teknik är så central.

## Ett praktiskt test av en principuppsättning

Innan en organisation beslutar eller reviderar sina principer kan varje princip prövas med några enkla frågor:

1. **Vilket återkommande problem eller vilken strategisk riktning adresserar principen?**
2. **Vilken typ av beslut ska den påverka?**
3. **Kan två rimliga alternativ faktiskt bedömas olika med hjälp av principen?**
4. **Är formuleringen tillräckligt teknikoberoende för att överleva flera realiseringar?**
5. **Finns innebörden redan bättre uttryckt som standard, policy eller krav?**
6. **Vilka konsekvenser får principen för gemensam nivå, förmågeområden och lösningsteam?**
7. **Hur märker vi att principen inte längre fungerar?**

Om svaren är otydliga är principen sannolikt inte färdig.

## Principer som gemensamt språk

Den kanske viktigaste effekten av en bra principuppsättning är inte formell styrning utan ett gemensamt språk.

När någon säger:

> Vi verkar göra dagens plattformsbegränsning till ett generellt krav. Hur stämmer det med behov före teknik?

kan diskussionen snabbt flyttas från personliga preferenser till en känd beslutsgrund.

När ett team vill bygga en egen lösning kan frågan bli:

> Vilket behov möter inte standarderbjudandet?

När en ny plattform föreslås kan man fråga:

> Hur ser hela livscykeln ut, inte bara införandet?

När observerbarhet planeras sent kan någon påminna om att driftbarhet ska byggas in från början.

Principerna blir då inte skyltar på väggen utan **frågor organisationen har lärt sig att ställa återkommande**.

Det är en mycket starkare form av arkitekturstyrning än att bara kontrollera efterlevnad i slutet av ett projekt.

## Från principer till etablering

De första sex kapitlen har nu byggt upp flera delar av samma logik:

- kapitel 1 beskrev varför gemensam IT-arkitektur behövs,
- kapitel 2 etablerade arkitekturens olika lager,
- kapitel 3 separerade behov från teknik,
- kapitel 4 gjorde kvalitetsattribut till explicita arkitekturdrivare,
- kapitel 5 visade hur konkreta beslut och avvägningar kan göras spårbara,
- detta kapitel har visat hur återkommande beslutsriktning kan uttryckas som relativt stabila principer.

Nästa fråga är praktisk:

> I vilken ordning etablerar man allt detta i en verklig organisation, och vem bör egentligen ansvara för vad?

Det är ämnet för nästa kapitel. Där introduceras bokens tredelning mellan **gemensam arkitekturnivå**, **förmågeområde** och **lösnings-/produktnivå**, tillsammans med en iterativ etableringsordning för den gemensamma IT-arkitekturen.
