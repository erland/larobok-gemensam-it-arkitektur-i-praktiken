# 6. Arkitekturprinciper som beslutsstöd

Ett enskilt arkitekturbeslut kan dokumenteras i en ADR, motiveras med kvalitetskrav och omprövas när förutsättningarna ändras. I en större organisation återkommer samtidigt många beslutssituationer gång på gång.

Ska ett team använda ett gemensamt plattformserbjudande eller bygga en egen lösning? Ska ett behov uttryckas produktoberoende eller direkt i termer av den teknik som redan finns? Ska säkerhet och driftbarhet hanteras i efterhand eller byggas in från början? När är återanvändning önskvärd, och när är en lokal speciallösning motiverad?

Om varje team börjar om från noll blir beslutsfattandet dyrt och inkonsekvent. Samtidigt är det sällan klokt att ersätta bedömning med detaljerade regler för varje tänkbar situation.

Här fyller arkitekturprinciper en viktig funktion.

En arkitekturprincip uttrycker en relativt stabil beslutsriktning. Den säger inte exakt vilken produkt eller konfiguration som ska väljas, men gör organisationens viktigaste utgångspunkter tydliga innan det konkreta beslutet fattas.

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

> Kommunikation mellan tjänster ska ske med HTTPS och minst den TLS-version som anges i organisationens säkerhetsstandard.

Detta är i första hand ett tekniskt krav eller en standardregel. Det är konkret, verifierbart och nära realiseringen.

> Säkerhet och andra relevanta kvaliteter ska byggas in i lösningen från början.

Detta är en princip. Den anger hur organisationen bör tänka, men inte exakt vilka protokoll eller mekanismer som ska användas.

> Använd organisationens API Management-tjänst för exponerade API:er enligt tjänstekontraktet.

Det är i stället styrning mot ett specifikt gemensamt erbjudande.

Skillnaden kan sammanfattas så här:

| Typ | Huvudfråga | Exempel |
|---|---|---|
| Princip | Vilken generell beslutsriktning ska vi ha? | Behov före teknik. |
| Mönster | Hur kan ett återkommande lösningsproblem struktureras? | Backend for Frontend. |
| Standard | Vilken gemensam teknisk regel eller rekommendation gäller? | API-standard. |
| Plattformserbjudande | Vilken gemensam tjänst kan konsumeras? | API Management. |
| Lokalt beslut | Vad väljer vi i just denna lösning? | Använd erbjudandet för dessa API:er. |

En princip som innehåller produktnamn, versionsnummer och detaljerade implementationer blir ofta för kortlivad. En princip som bara säger att organisationen ska ”bygga bra och säkra lösningar” blir i stället så allmän att den inte hjälper någon att välja. Den användbara nivån ligger mellan dessa ytterligheter.

## Vad en användbar princip behöver åstadkomma

En princip är värdefull först när den påverkar verkliga beslut.

### Den ska uttrycka en verklig prioritering

”Vi ska använda lämplig teknik” är svårt att invända mot men hjälper inte när två alternativ konkurrerar. ”Behov före teknik” uttrycker däremot en faktisk prioritering: behov och kvalitetskrav ska styra problemformuleringen innan dagens produktlandskap får styra lösningen.

### Den ska vara tillräckligt stabil

En gemensam princip bör normalt överleva fler produktgenerationer än en teknisk standard. Om organisationen byter containerplattform ska principen om att separera stabil arkitektur från föränderlig teknik fortfarande vara meningsfull.

### Den ska få konsekvenser

En princip bör göra det möjligt att fråga:

> Om vi tar den här principen på allvar, vad förändras då i vårt beslut?

Om svaret är ”ingenting” är formuleringen sannolikt för vag.

### Den ska kunna användas tillsammans med andra principer

Principer verkar sällan ensamma. Återanvändning kan tala för ett gemensamt erbjudande, medan behov och kvalitetskrav kan tala för ett avsteg. Principerna ska därför fungera som beslutsdrivare, inte som absoluta lagar som automatiskt ger ett enda svar.

Det är också en anledning att formulera principer så att de går att diskutera tillsammans. Om en princip alltid trumfar alla andra är den i praktiken snarare ett överordnat krav. Om två principer alltid ger exakt samma slutsats kan de kanske slås ihop. En väl avvägd uppsättning bör i stället belysa olika sidor av beslutet och hjälpa organisationen att göra avvägningen synlig.

### Den ska vara möjlig att känna igen i vardagen

En princip behöver kunna kopplas till situationer som arkitekter, produktteam och plattformsansvariga faktiskt möter. Formuleringen ska därför vara tillräckligt generell för att överleva teknikskiften, men tillräckligt konkret för att någon ska kunna använda den som kontrollfråga i ett designmöte.

Det är en viktig skillnad mellan en princip och ett värdeord. Ett värdeord kan uttrycka en önskad kultur. En arkitekturprincip behöver dessutom ge riktning i ett återkommande val.

## Tio principer som exempel på en sammanhängande uppsättning

Följande tio principer används som exempel på en sammanhängande principuppsättning. De är inte universella regler som varje organisation måste använda ordagrant. Syftet är att visa hur återkommande beslutsriktning kan göras tydlig utan att gå hela vägen ner till produkter och konfigurationer.

### 1. Behov före teknik

Arkitekturval ska utgå från identifierade behov, relevanta kvaliteter och verkliga begränsningar, inte från en på förhand vald produkt.

**Konsekvens:** behov och kvalitetskrav ska kunna beskrivas innan teknikvalet motiveras. Befintlig teknik får behandlas som en begränsning när den faktiskt är bindande, men ska inte automatiskt definiera behovet.

### 2. Standardiserade erbjudanden när de möter behovet

Gemensamma plattformar, tjänster och standarder ska återanvändas när deras tjänstekontrakt och egenskaper är tillräckliga för det aktuella behovet.

**Konsekvens:** lokala lösningar ska inte byggas av vana eller preferens när ett gemensamt erbjudande fungerar, men det gemensamma får inte göras obligatoriskt när centrala behov eller kvalitetskrav faktiskt inte uppfylls.

### 3. Problem löses på lämplig arkitekturnivå

Problem bör så långt som möjligt lösas där de naturligt hör hemma: gemensamt, inom en förmåga eller lokalt i en lösning.

**Konsekvens:** ett generellt plattformsproblem bör inte implementeras separat i varje applikation, samtidigt som ett lokalt domänproblem inte automatiskt ska bli en central plattformsfunktion.

### 4. Ansvar och gränssnitt ska vara tydliga

Gemensamma tjänster och byggblock ska ha tydliga ansvarssnitt och tjänstekontrakt.

**Konsekvens:** det ska gå att förstå vad tjänsten lovar, vilka kvalitetsnivåer som ingår, vad konsumenten ansvarar för och vem som äger drift, förändring och avveckling. Abstraktion ska minska onödig komplexitet utan att dölja ansvar.

### 5. Säkerhet och andra kvaliteter byggs in

Relevanta kvalitetsattribut ska påverka arkitekturen från början och inte behandlas som efterkontroller ovanpå en färdig funktionell lösning.

**Konsekvens:** exempelvis säkerhet, tillgänglighet, kontinuitet, driftbarhet och användbarhet ska få en nivå som motiveras av behov och konsekvens och därefter avspeglas i design, mönster och plattformskrav.

### 6. Stabil arkitektur separeras från föränderlig teknik

Behov, förmågor och principer bör hållas fria från onödiga beroenden till dagens produkter, versioner och konfigurationer.

**Konsekvens:** en förmåga bör beskriva vad organisationen behöver kunna göra, medan en produkt beskriver dagens realisering. Produktnamn hör hemma där den tekniska realiseringen faktiskt beslutas.

### 7. Återanvändning före lokal speciallösning

Återanvändning är förstahandsval när det återanvända objektet möter behovet på ett rimligt sätt.

**Konsekvens:** gemensamma komponenter, tjänster och mönster bör användas när de ger verklig nytta. Lokala speciallösningar är motiverade när skillnaden i behov är verklig och synlig, inte bara uttryck för lokal vana.

### 8. Automatisering och reproducerbarhet eftersträvas

Återkommande tekniska processer bör automatiseras där det är praktiskt och proportionerligt.

**Konsekvens:** bygg, test, driftsättning, infrastruktur, konfiguration och relevanta kontroller ska så långt som möjligt kunna utföras reproducerbart utan beroende av enskilda personers manuella steg. Automatisering är dock inte ett självändamål för sällsynta och enkla aktiviteter.

### 9. Livscykel och förvaltning beaktas vid beslut

Teknikval ska bedömas över hela den förväntade livscykeln, inte bara utifrån snabbaste vägen till första leverans.

**Konsekvens:** drift, support, kompetens, uppgraderingar, kostnader och avveckling ska vägas in tillsammans med införandekostnaden. Ett alternativ som är enkelt att börja med kan ändå vara dyrt att äga.

### 10. Avsteg ska kunna motiveras

Avsteg från gemensamma principer, standarder eller erbjudanden ska vara synliga arkitekturbeslut.

**Konsekvens:** det ska gå att beskriva vilket behov den gemensamma vägen inte möter, vilket alternativ som väljs, vilka konsekvenser som accepteras och vem som äger den extra komplexiteten. Återkommande likartade avsteg ska dessutom kunna användas som återkoppling till den gemensamma arkitekturen.

## När principer drar åt olika håll

En principuppsättning blir missvisande om den presenteras som om alla principer alltid pekar åt samma håll.

Anta att ett team behöver hantera mycket hög meddelandevolym och organisationen redan har ett gemensamt messaging-erbjudande. Återanvändning och standardiserade erbjudanden talar för den gemensamma vägen. Behov före teknik och kvalitetskraven kan samtidigt visa att erbjudandet inte klarar nödvändig volym, latens eller leveransgaranti.

Om erbjudandet möter kraven är återanvändning sannolikt rationell. Om det inte gör det kan samma principuppsättning stödja ett avsteg.

Poängen är att principerna ska göra resonemanget mer konsekvent, inte eliminera avvägningar. När två principer drar åt olika håll måste beslutet återgå till behov, kvalitetskrav, begränsningar, risker och konsekvenser.

En mekanisk rangordning där princip 1 alltid vinner över princip 2 fungerar därför sällan väl. Vissa organisationer kan behöva särskilda överordnade principer, men i normalfallet är det bättre att göra motiveringen bakom varje princip tydlig och låta den konkreta situationen avgöra hur de vägs tillsammans.

I praktiken betyder det att principer bör användas tidigt i beslutsarbetet, inte bara som en kontrollista i efterhand. När alternativen fortfarande är öppna kan de hjälpa till att formulera vilka frågor som behöver besvaras. När beslutet väl är fattat kan samma principer användas för att förklara varför ett alternativ valdes framför ett annat. Därmed blir de både analysstöd och språk för motivering.

## Princip, motivering och konsekvens

En kort principformulering blir starkare om den kompletteras med varför den finns och vad den normalt betyder i praktiken.

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

**Konsekvenser:** Behov och kvalitetskrav formuleras före produktval. Produktbegränsningar behandlas som begränsningar när de verkligen är bindande, men generaliseras inte automatiskt till alla lösningar.

I vissa organisationer läggs även exempel, ägare eller relaterade standarder till. Det kan vara värdefullt, men principdokumentet bör inte svälla till en blandning av princip, policy och teknisk katalog.

Det kan också vara klokt att ange vilka beslutssituationer principen särskilt är avsedd att påverka. En princip om livscykelperspektiv blir exempelvis lättare att använda om det framgår att den ska påverka teknikval, plattformsinföranden och större egenutvecklade komponenter. Då blir principens användningsområde tydligt utan att själva formuleringen behöver fyllas med detaljer.

## För många principer är nästan lika illa som inga

Om en organisation har femtio eller hundra ”principer” uppstår ett praktiskt problem: nästan ingen kan minnas eller använda dem i vardagliga beslut.

Det är ofta ett tecken på att olika artefakttyper har blandats ihop. Vissa formuleringar är egentligen tekniska standarder, säkerhetskrav, kodningsregler, plattformsinstruktioner eller processkrav.

En liten uppsättning starka arkitekturprinciper kan därför vara mer styrande än en stor lista av detaljregler. Det betyder inte att organisationen ska ha få tekniska regler, utan att reglerna bör ligga där de hör hemma i modellen.

En praktisk tumregel är att en gemensam principuppsättning ska vara så liten att de viktigaste principerna går att känna igen utan att slå upp dem. Om människor bara kan använda principerna genom att söka i ett stort dokument har de sannolikt blivit för många eller för detaljerade.

## Principer på olika nivåer

Bokens tredelning mellan gemensam nivå, förmågenivå och lösnings-/produktnivå är användbar även för principer.

**Gemensam nivå** behöver ett litet antal stabila principer som skapar en gemensam beslutslogik över flera områden, exempelvis behov före teknik och livscykelperspektiv.

**Förmågenivån** kan behöva mer specifika principer. Integration och kommunikation kan exempelvis behöva principer om kontraktsägarskap eller när synkron respektive asynkron interaktion är lämplig. Dessa principer ska vara förenliga med de gemensamma men får vara mer domänspecifika.

**Lösnings-/produktnivån** behöver normalt fler konkreta arkitekturbeslut än långlivade principer. Lokala designprinciper kan vara värdefulla men ska inte automatiskt upphöjas till organisationsgemensam arkitektur.

Nivåerna ger också en väg för lärande. En lokal designregel som återkommer i många lösningar kan vara kandidat för ett förmågespecifikt mönster eller en princip. En förmågeprincip som visar sig relevant över flera områden kan på motsvarande sätt bli gemensam. Förflyttningen uppåt bör dock bygga på återkommande behov och erfarenhet, inte på att en enskild lösning vill generalisera sitt arbetssätt.

## Från återkommande beslut till princip

Bra principer uppstår ofta ur verkliga beslut och återkommande problem.

Om flera team exempelvis gång på gång låter plattformsspecifika begränsningar läcka in i verksamhetskrav finns erfarenhet som kan kondenseras till en stabil beslutsriktning: *Behov före teknik*.

Om egenbyggda driftmekanismer återkommer trots att samma problem finns på många håll kan erfarenheten i stället stödja principer om återanvändning och gemensamma erbjudanden.

En princip bör alltså ha tydlig koppling till organisationens mål, risker eller återkommande beslutsmönster. Det skapar också bättre förutsättningar för acceptans: människor förstår varför principen finns.

## Från princip till konkret styrsignal

En princip blir verkligt användbar först när den kan realiseras genom andra artefakter.

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

Principen tillhandahåller inte återanvändning i sig. Den behöver stödjas av erbjudanden som faktiskt är användbara.

Om organisationen säger ”använd gemensamma plattformar” men plattformarna är svåra att beställa, saknar dokumentation eller inte möter rimliga kvalitetskrav kommer principen att uppfattas som administrativ styrning. Om team förväntas automatisera och arbeta reproducerbart måste plattformar och verktyg stödja det. Om kvaliteter ska byggas in tidigt måste relevanta krav, mönster och plattformsförmågor finnas tillgängliga tidigt.

En princip uttrycker därför inte bara vad lösningsteam ska göra. Den skapar också en förväntan på den gemensamma arkitekturen och plattformsorganisationen.

Det är här principer kan kopplas till konkret styrning utan att själva bli detaljregler. En princip om återanvändning kan exempelvis stödjas av en katalog över plattformserbjudanden och golden paths. En princip om reproducerbarhet kan stödjas av standardiserade pipelines och automatiserade policykontroller. En princip om tydliga ansvar kan realiseras genom tjänstekontrakt och dokumenterade ägarskap.

Om det saknas sådana realiseringar bör organisationen vara försiktig med att tolka bristande efterlevnad som ett teamproblem. En princip som inte stöds av praktiska förutsättningar riskerar annars att skapa friktion i stället för riktning.

## När en princip bör omprövas

Principer är avsiktligt stabila, men stabilitet är inte samma sak som evighet.

En princip bör kunna omprövas när exempelvis:

- organisationens mål eller riskbild förändras,
- återkommande avsteg visar att principen inte fungerar,
- teknikutveckling ändrar grundläggande förutsättningar,
- principen inte längre påverkar beslut,
- två principer skapar systematiska konflikter,
- formuleringen tolkas så olika att den förlorar styrverkan.

Det är samtidigt viktigt att skilja på att principen behöver ändras och att dess realisering förändras. När en produkt går ur support är det normalt produktstandarden eller plattformens realisering som ska ändras, inte principen om exempelvis återanvändning eller livscykelhantering.

Förvaltning av principer behöver därför vara återhållsam. Små tekniska förändringar ska inte automatiskt ge nya formuleringar, men återkommande konflikter och systematiska avsteg bör följas upp. På så sätt kan principerna vara stabila utan att bli immuna mot erfarenhet.

## Ett praktiskt test av en principuppsättning

Innan en organisation beslutar eller reviderar sina principer kan varje princip prövas med några frågor:

1. Vilket återkommande problem eller vilken strategisk riktning adresserar principen?
2. Vilken typ av beslut ska den påverka?
3. Kan två rimliga alternativ faktiskt bedömas olika med hjälp av principen?
4. Är formuleringen tillräckligt teknikoberoende för att överleva flera realiseringar?
5. Finns innebörden redan bättre uttryckt som standard, policy eller krav?
6. Vilka konsekvenser får principen på gemensam nivå, förmågenivå och lösningsnivå?
7. Hur märker vi att principen inte längre fungerar?

Om svaren är otydliga är principen sannolikt inte färdig.

## Principer som gemensamt språk

Den kanske viktigaste effekten av en bra principuppsättning är inte formell styrning utan ett gemensamt språk.

När någon säger:

> Vi verkar göra dagens plattformsbegränsning till ett generellt krav. Hur stämmer det med behov före teknik?

kan diskussionen flyttas från personliga preferenser till en känd beslutsgrund.

När ett team vill bygga en egen lösning kan frågan bli:

> Vilket behov möter inte standarderbjudandet?

När en ny plattform föreslås kan man fråga hur hela livscykeln ser ut, inte bara införandet. När observerbarhet planeras sent kan någon påminna om att driftbarhet ska byggas in från början.

Principerna blir då inte skyltar på väggen utan frågor organisationen har lärt sig att ställa återkommande. Det är en starkare form av arkitekturstyrning än att bara kontrollera efterlevnad i slutet av ett projekt.

## Från principer till etablering

Arkitekturprinciperna ger en stabil riktning över många enskilda beslut. Nästa fråga är därför praktisk:

> Hur etablerar man modellen i en verklig organisation, och vem bör ansvara för vad?

Det är ämnet för nästa kapitel.
