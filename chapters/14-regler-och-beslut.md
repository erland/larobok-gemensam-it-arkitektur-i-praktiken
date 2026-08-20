# 14. Regler och beslut

Ett verksamhetssystem fattar ständigt beslut. Ett ärende ska kanske godkännas eller avslås. En avgift ska beräknas. Ett objekt ska klassificeras. En ansökan ska styras till en viss handläggningsväg. En kontroll ska avgöra om vissa villkor är uppfyllda.

Det betyder inte att varje `if`-sats är en verksamhetsregel som bör externaliseras.

Förmågan *Regler och beslut* blir relevant när själva regeln eller beslutet har en egen betydelse som behöver kunna förstås, förändras, testas, återanvändas eller spåras oberoende av den applikation som råkar exekvera det. Arkitekturfrågan är därför inte i första hand vilken regelmotor organisationen ska använda, utan vilken beslutslogik som bör behandlas som en egen förvaltningsbar artefakt och vilken logik som bör stanna i vanlig domänkod.

Det är en viktig gränsdragning. För lite explicit regelhantering kan ge duplicerade regler, svår spårbarhet och långsam förändring. För mycket explicit regelhantering kan i stället skapa en central regelmonolit, indirekt kod och ett nytt plattformsberoende för logik som hade varit enklare att förstå nära domänen.

## Från villkor i kod till verksamhetsbeslut

All programvara innehåller villkor. Ett fält får inte vara tomt. En användare måste vara autentiserad. Ett API får inte ta emot mer än en viss mängd trafik. En order får inte avslutas innan alla obligatoriska uppgifter finns.

Dessa villkor är inte nödvändigtvis samma typ av regel.

Det är användbart att skilja mellan åtminstone fyra kategorier:

1. lokal programlogik – tekniska och domännära villkor som hör ihop med komponentens implementation,
2. verksamhetsregler – explicita villkor med verksamhetsbetydelse,
3. verksamhetsbeslut – ett resultat som härleds från ett eller flera fakta och regler,
4. tekniska policyer – styrning av exempelvis access, routing, resursanvändning eller säkerhet.

Anta att ett system innehåller följande logik:

```text
om sökanden är under 18 år
och samtycke saknas
så krävs komplettering
```

Om detta är ett centralt verksamhetsvillkor, återkommer i flera flöden och behöver kunna knytas till en viss regelversion är det rimligt att behandla det som en explicit verksamhetsregel.

Ett annat villkor kan vara:

```text
om HTTP-anropet misslyckas med 503
så försök igen enligt återförsökspolicy
```

Det är också en regel i vardagligt språk, men den hör inte hemma i förmågan Regler och beslut. Det är teknisk resilienslogik.

Det första steget är alltså att klassificera vilken sorts logik det faktiskt är.

## Ett beslut är mer än en regel

En regel uttrycker ofta ett samband eller villkor. Ett beslut är resultatet av att använda fakta, regler och ibland beräkningar för att komma fram till ett utfall.

Det kan till exempel uttryckas som:

```text
Indata
  ↓
Fakta och härledda värden
  ↓
Regler / beslutstabell / beräkning
  ↓
Beslut
  ↓
Motivering och metadata
```

Det är en viktig skillnad eftersom en fungerande beslutsförmåga behöver hantera mer än själva uttrycket som returnerar `ja` eller `nej`.

För vissa beslut behöver organisationen också veta:

- vilka indata som användes,
- vilken regel- eller modellversion som gällde,
- när beslutet fattades,
- vilket utfall som returnerades,
- vilka regler som bidrog till utfallet,
- vilken giltighetsperiod reglerna hade,
- vem som ägde eller godkände regelverket,
- om beslutet senare har ersatts eller omprövats.

Ju större verksamhetsmässig eller rättslig betydelse beslutet har, desto mindre rimligt är det att behandla beslutslogiken som en anonym kodrad utan egen livscykel.

## När regler bör göras explicita

Externalisering innebär att regel- eller beslutslogik lyfts ut ur vanlig applikationskod till en tydligare representerad och separat förvaltad artefakt. Det kan vara en beslutstabell, en beslutsmodell, en regeluppsättning eller en beslutstjänst.

Det bör finnas ett konkret skäl till detta.

Externalisering blir särskilt intressant när flera av följande gäller:

- samma regel behöver användas i flera system eller processer,
- regeln förändras i en annan takt än applikationen,
- verksamheten behöver kunna granska regeln explicit,
- beslut måste kunna förklaras i efterhand,
- regelversionen behöver kunna kopplas till ett historiskt beslut,
- regelverket består av många kombinationer som är svåra att överblicka i vanlig kod,
- verksamheten behöver simulera framtida regeländringar,
- regler behöver testas oberoende av hela applikationen,
- flera organisatoriska delar behöver tillämpa samma beslut konsekvent.

Det viktiga är inte att regler *kan* externaliseras, utan att externaliseringen förbättrar förståelighet, förändringsbarhet, återanvändning eller spårbarhet.

En enkel lokal regel som endast används i en domänkomponent och förändras tillsammans med resten av koden vinner ofta inget på att flyttas ut.

## Externalisering är inte samma sak som centralisering

En vanlig missuppfattning är att explicit regelhantering betyder att alla verksamhetsregler bör läggas i en gemensam central regelmotor.

Det är normalt en dålig slutsats.

Verksamhetslogik har ett domänansvar. Att en gemensam plattform kan exekvera regler innebär inte att plattformen bör äga deras mening.

En mer hållbar struktur kan vara:

```text
Gemensam regel-/beslutsplattform
            │
            ├── Regelområde A – ägs av domän A
            ├── Regelområde B – ägs av domän B
            └── Regelområde C – ägs av domän C
```

Det gemensamma kan då vara:

- exekveringsmiljö,
- modellformat,
- versionshantering,
- test- och simulationsstöd,
- driftsättningsmekanism,
- audit och observerbarhet,
- API-principer,
- verktygsstöd.

Det verksamhetsmässiga ägarskapet för respektive regelverk förblir däremot där regeln hör hemma.

Detta följer samma princip som för andra gemensamma IT-förmågor: gemensam mekanism behöver inte innebära centraliserad verksamhetslogik.

## Gränsen mot processvillkor och domänlogik

Regler och beslut behöver avgränsas både mot processlogik och mot vanlig domänkod. En användbar fråga är om logiken har en egen verksamhetsmässig livscykel som motiverar att den kan förstås, testas och förändras separat från det som använder den.

Anta ett workflow där ett ärende efter registrering går till automatisk handläggning eller manuell granskning. Om villkoret bara är ett lokalt vägval i just processen kan det ligga i processmodellen. Om samma klassificering däremot används i flera processer, har en egen verksamhetsdefinition, förändras oberoende av flödet eller måste kunna förklaras i efterhand bör den behandlas som ett eget beslut.

```text
Workflow
   ↓
"Vilken handläggningskategori gäller?"
   ↓
Beslutstjänst
   ↓
AUTOMATISK | MANUELL | SÄRSKILD_KONTROLL
```

Processen äger vad som händer efter resultatet. Beslutet äger hur kategorin avgörs. Det gör att process och beslutslogik kan förändras i olika takt.

Vanlig domänkod är samtidigt ofta bäst när logiken bara används i en komponent, är nära kopplad till domänmodellens beteende och förändras tillsammans med övrig funktionalitet. Explicit regelhantering blir starkare när regelverket i sig är en förvaltningsvärd artefakt – exempelvis ett avgiftsregelverk med giltighetsperioder och historisk spårbarhet – snarare än ett enkelt villkor som skyddar ett lokalt domäninvariant.

Gränsen är alltså inte teknisk. Samma slags villkor kan ligga i vanlig kod i ett sammanhang och vara ett explicit beslut i ett annat. Avgörande är behovet av separat begriplighet, återanvändning, ändringstakt, spårbarhet och förvaltning.

## Beslutstabeller som verktyg för begriplighet

Många verksamhetsbeslut består av kombinationer av villkor.

Anta att en kontrollnivå bestäms av tre faktorer:

- typ av aktör,
- värdeintervall,
- tidigare avvikelser.

Om detta implementeras som en lång kedja av nästlade villkor blir det snabbt svårt att avgöra om alla kombinationer är täckta.

En beslutstabell kan göra samma logik mer överskådlig:

| Aktör | Värde | Tidigare avvikelse | Resultat |
|---|---|---|---|
| Låg risk | Lågt | Nej | Normal kontroll |
| Låg risk | Högt | Nej | Utökad kontroll |
| Valfri | Valfritt | Ja | Särskild kontroll |

Poängen är inte tabellen i sig. Poängen är att representationen passar den typ av beslut som ska förstås och förvaltas.

För vissa beslut passar ett beslutsträd bättre. För andra en beräkning, en sammansatt beslutsmodell eller vanlig kod.

En arkitekt bör därför inte fråga ”kan detta göras i en beslutstabell?” utan ”vilken representation gör beslutets logik mest korrekt, begriplig och förvaltningsbar?”.

## DMN – en standardiserad beslutsnotation

Decision Model and Notation, DMN, är en OMG-standard för modellering av beslut. Standarden ger dels en grafisk notation för att beskriva beroenden mellan beslut och deras indata, dels ett uttrycksspråk för beslutslogik.

DMN kan vara särskilt användbart när en organisation vill skapa ett gemensamt språk mellan verksamhetsanalys och teknisk exekvering av beslut.

En beslutsmodell kan exempelvis visa:

```text
Aktörsinformation ─┐
                   ├──> Riskklass ──┐
Transaktionsdata ──┘                ├──> Kontrollnivå
Historik ───────────────────────────┘
```

Det gör beroenden synliga på ett annat sätt än om hela logiken bara ligger i kod.

DMN ska däremot inte uppfattas som ett krav för all regelhantering. En organisation kan ha fullt legitima beslut som implementeras på andra sätt. Standarden löser inte heller ägarskap, informationskvalitet, versionsstrategi eller governance automatiskt.

Vid faktagranskningen den 19 augusti 2026 är DMN 1.5 den senaste formellt antagna versionen hos OMG; 1.6 och 1.7 finns som betaversioner.[K1] Versionsuppgifter är tidskänsliga och bör därför verifieras igen om publiceringen sker vid ett senare tillfälle.

## En beslutstjänst som arkitekturmönster

När samma beslut behöver användas från flera lösningar kan det exponeras som en beslutstjänst.

```text
Konsument
   ↓
Besluts-API
   ↓
Beslutsmodell / regelverk
   ↓
Resultat + beslutsmetadata
```

Det kan ge flera fördelar:

- en gemensam exekveringspunkt,
- konsekvent användning av samma regelversion,
- separat release av beslutet,
- gemensam observerbarhet,
- tydlig mätning av användning och fel,
- möjlighet att centralisera vissa test- och auditfunktioner.

Men det skapar också ett distribuerat beroende.

Om varje lokal beräkning måste göra ett synkront nätverksanrop till en central beslutstjänst uppstår frågor om:

- latens,
- tillgänglighet,
- skalbarhet,
- felhantering,
- versionering av kontrakt,
- driftsättningsberoenden,
- geografiska eller säkerhetsmässiga begränsningar.

Återanvändning genom tjänsteanrop är alltså inte automatiskt bättre än återanvändning genom gemensam modell, bibliotek eller distribuerad regelartefakt. En central tjänst kan vara rätt när konsekvent exekvering och gemensam förvaltning väger tungt; lokal exekvering kan vara bättre när latens, robusthet eller isolering dominerar.

Det rätta mönstret beror på kvalitetskraven och på vilken nivå av återanvändning som faktiskt behövs.

## Versionering, förklarbarhet och testning

För verksamhetskritiska eller rättsligt betydelsefulla beslut räcker det sällan att veta vilken applikationsversion som körde. Arkitekturen kan behöva skilja mellan modellversion, verksamhetsmässig giltighetsperiod, driftsättningstidpunkt och den tidpunkt då det konkreta beslutet fattades. Ett ärende som kom in före en regeländring men avgörs efter den kan exempelvis behöva bedömas enligt den äldre regeln. Ett beslut kan annars inte säkert reproduceras i efterhand.

Det är därför viktigt att inte låta teknisk versionshantering ensam representera verksamhetsmässig giltighet. En modellversion kan vara driftsatt men ännu inte gälla för alla typer av beslut, och en äldre version kan behöva finnas kvar för historiska eller pågående ärenden.

```text
beslut_id
regelmodell = AVGIFT
regelversion = 2027.1
regel_giltig_fran = 2027-01-01
beslutstidpunkt = 2027-01-14T10:32
indata_referens = ...
resultat = ...
```

Förklarbarhet behöver samtidigt utgå från mottagaren. En utvecklare kan behöva en detaljerad exekveringslogg, en handläggare vilka kriterier som gav utfallet, en extern part en begriplig motivering och en revisor möjlighet att återskapa beslutet från historiska indata och regelversion. En teknisk trace är därför inte automatiskt en verksamhetsförklaring.

Det kan också vara viktigt att skilja mellan att förklara *vilken regel som slog till* och att förklara *varför regeln finns*. Den första frågan hör till exekveringsspåret, den andra till regelverkets verksamhetsmässiga källa och motivering. Båda kan behövas, men de kräver olika metadata.

När regler externaliseras bör de också kunna testas som egna artefakter. Det kan omfatta gränsvärden, kombinationer och överlapp, luckor där inget utfall blir giltigt, historiska regressionsfall och simulering mot representativa data. Testningen bör alltså inte bara visa att regelmotorn tekniskt fungerar, utan att regelverket ger rätt utfall för relevanta kombinationer och att oavsiktliga förändringar upptäcks.

Särskilt värdefullt är att kunna jämföra gammal och ny regelversion före driftsättning. Organisationen kan då fråga: hur många historiska beslut hade fått ett annat utfall, vilka grupper hade påverkats och beror skillnaden på en avsedd regeländring eller ett oväntat sidoresultat? Då blir beslutsförmågan också ett stöd för konsekvensanalys.

Externaliserade regler behöver dessutom tydligt sakägarskap och tekniskt förvaltningsansvar. Sakägaren ansvarar för verksamhetsmässig innebörd, tolkning av styrande regelverk, prioritering och godkännande av förändringar. Det tekniska ansvaret omfattar bland annat modellformat, implementation, testautomatisering, driftsättning, prestanda, audit och versionshantering.

Det viktiga är inte att samma organisatoriska enhet äger båda perspektiven, utan att förändringsprocessen gör dem beroende av varandra på ett kontrollerat sätt. En tekniskt korrekt driftsättning av en verksamhetsmässigt felaktig regel är inte en lyckad förändring, och ett verksamhetsmässigt korrekt regelbeslut är inte produktionssäkert förrän det har testats och driftsatts kontrollerat.

## Deterministiska regler och AI är olika saker

Ett explicit regelverk kan exempelvis säga:

```text
om A och B gäller → resultat X
```

Givet samma indata och samma regelversion ska resultatet då vara förutsebart.

En maskininlärningsmodell kan i stället ge en sannolikhet, klassificering eller genererad bedömning. Den har andra egenskaper kring testning, förklarbarhet, förändring och risk.

De två bör därför hållas konceptuellt isär även när de kombineras.

Ett möjligt upplägg är:

```text
AI/ML-modell
    ↓
Bedömningssignal
    ↓
Explicit regelbaserat beslut
    ↓
Utfall
```

Exempelvis kan en modell beräkna en risksignal medan explicita regler avgör vilka åtgärder som får följa av signalen.

Det innebär inte att denna struktur alltid är rätt. Men den gör ansvarsfördelningen tydlig: modellen producerar en bedömning; beslutslagret tillämpar explicita regler.

AI-specifika kvalitets- och styrningsfrågor behandlas senare.

## Beslutsdata måste ha tydlig betydelse

Regler är bara så bra som de data de använder.

Ett beslut kan vara fullständigt deterministiskt men ändå fel om indata:

- är inaktuell,
- kommer från fel källa,
- har annan semantik än modellen förutsätter,
- saknar nödvändig historik,
- har förändrats mellan beslut och senare granskning.

Här möter förmågan *Data- och informationshantering*.

För beslut med höga spårbarhetskrav behöver man ibland kunna återskapa inte bara regeln utan även vilket beslutsunderlag som faktiskt fanns vid beslutstidpunkten.

Det kan kräva exempelvis:

- snapshot av relevanta indata,
- referens till versionshanterad information,
- historiserad källa,
- tydlig dokumentation av vilka externa uppgifter som användes.

Att bara köra om dagens regel mot dagens data är inte nödvändigtvis att reproducera gårdagens beslut.

## Kvalitetskrav för beslutsförmågan

Olika beslut ställer mycket olika krav.

En rekommendation som visas för en intern användare och kan ignoreras har en annan riskprofil än ett automatiserat beslut som påverkar en extern part.

Några återkommande kvalitetsfrågor är:

### Korrekthet

Vilken tolerans finns för felaktiga utfall? Hur verifieras regelverket före driftsättning?

### Spårbarhet

Behöver det gå att avgöra vilken modell, indata och giltighetsperiod som låg bakom ett historiskt beslut?

### Förklarbarhet

Vem behöver förstå varför utfallet blev som det blev och på vilken detaljnivå?

### Prestanda

Är det fråga om några få komplexa beslut per dag eller tusentals enkla beslut per sekund?

### Tillgänglighet

Kan konsumenten fortsätta om beslutstjänsten är otillgänglig? Finns fallback eller lokal exekvering?

### Förändringsbarhet

Hur ofta ändras reglerna? Måste de kunna driftsättas separat från konsumerande system?

### Säkerhet och informationsskydd

Använder beslutet känsliga uppgifter? Vilka användare får se eller förändra regler och beslutsspår?

### Regelefterlevnad

Finns krav på dokumentation, attest, giltighetsperiod eller bevarande?

Kvalitetsprofilen bör avgöra realiseringen – inte det faktum att organisationen redan äger en viss regelmotor.

## Ansvar på tre nivåer

Bokens tredelade ansvarmodell kan här användas utan att introduceras på nytt. Den gemensamma arkitekturnivån bör definiera sådant som behöver vara konsekvent mellan regelområden – exempelvis principer för spårbarhet, versionshantering, audit, modell- eller API-format och gränsen mot process och AI. Den ska inte äga innehållet i varje verksamhetsregel.

Förmågeområdet kan erbjuda vägledning för externalisering, lösningsmönster, plattformstöd, test och simulering, versionshantering, beslutsmetadata och golden paths. Lösnings- eller produktnivån äger däremot de domänspecifika besluten, informationsmodellen, testfallen och hur resultatet används i den konkreta lösningen.

Gemensamt stöd ska alltså minska återkommande teknikarbete utan att flytta bort domänansvaret.

## Vanliga anti-patterns

### Varje `if` blir en regel

Små lokala villkor flyttas ut ur koden bara för att en regelplattform finns. Logiken blir mer indirekt och svårare att förstå.

### Den centrala regelmonoliten

Regler från många orelaterade domäner samlas i samma globala regelverk. Ägarskap, release och felsökning blir sammanflätade.

### Verksamheten redigerar produktion direkt

Målet ”verksamheten ska kunna ändra regler utan IT” leder till att förändringar kan göras utan versionshantering, test, granskning eller kontrollerad driftsättning.

### Regeln dupliceras överallt

Samma regel kopieras till flera system. Efter några år finns flera nästan likadana tolkningar utan tydlig auktoritativ version.

### Processen innehåller hela regelverket

Beslutstabeller och omfattande verksamhetsregler bäddas in i processdefinitioner trots att de har egen livscykel och används på flera ställen.

### Regelmotorn blir integrationsplattform

Regler börjar göra omfattande nätverksanrop och koordinera externa system. Beslutslogiken får då dolda beroenden och blandas ihop med integration.

### Teknisk trace förväxlas med verksamhetsförklaring

Systemet kan visa exakt vilka interna noder som exekverades men kan ändå inte ge en begriplig motivering till beslutet.

### Ingen koppling mellan beslut och regelversion

Regler versionshanteras men historiska beslut sparar inte vilken version som användes. Versionshanteringen ger då mindre spårbarhet än man tror.

### AI-resultat behandlas som deterministisk regel

En probabilistisk modell får samma semantik som ett explicit regelverk utan att osäkerhet, modellversion eller risk hanteras.

## En praktisk analysordning

När ett utvecklingsområde överväger explicit regel- eller beslutshantering kan följande ordning användas.

### 1. Beskriv beslutet utan teknik

Vilken fråga ska besvaras? Vilket verksamhetsutfall produceras?

### 2. Identifiera beslutets ägare

Vem bestämmer vad regeln betyder och vem får godkänna förändringar?

### 3. Beskriv indata och informationskällor

Vilka fakta behövs? Vilken källa är auktoritativ? Behöver historiska indata kunna återskapas?

### 4. Avgör om logiken har egen livscykel

Förändras regeln oberoende av applikationen? Behöver den förstås, testas eller versioneras separat?

### 5. Separera regel, process och teknisk policy

Är detta ett verksamhetsbeslut, ett lokalt processvillkor, domänlogik eller teknisk styrning?

### 6. Bedöm återanvändningsbehovet

Ska flera processer eller system använda samma beslut? Krävs en gemensam tjänst eller räcker gemensam modell/artefakt?

### 7. Definiera spårbarhetsnivån

Vilken information måste kunna visas eller reproduceras i efterhand?

### 8. Välj representation

Vanlig kod, beslutstabell, beslutsmodell, regelmotor eller annan form – välj den enklaste som uppfyller kraven.

### 9. Definiera test- och simulationsstrategi

Hur upptäcks konflikter, luckor och oönskade effekter före driftsättning?

### 10. Planera version och giltighet

Vad betyder det att en regelversion ”gäller” och hur kopplas ett konkret beslut till rätt version?

### 11. Analysera driftsegenskaper

Vilka krav finns på latens, tillgänglighet, volym, säkerhet och observerbarhet?

### 12. Jämför med vanlig kod igen

Har externaliseringen ett tydligt värde? Om svaret fortfarande är oklart bör den enklare lösningen väga tungt.

## Förmågan som konsumerbart stöd

Ett moget förmågeområde bör kunna erbjuda mer än en installerad regelmotor.

Ett konsumerbart stöd kan exempelvis bestå av:

- kriterier för när externalisering är lämplig,
- stöd för beslutstabeller och beslutsmodeller,
- en eller flera exekveringsprofiler,
- beslutstjänster med definierade kontrakt,
- versions- och giltighetsmodell,
- test- och simulationsverktyg,
- audit och beslutsmetadata,
- observerbarhet,
- säker driftsättning,
- exempel och golden paths,
- integration mot workflow och API-plattform,
- tydligt konsumentansvar för domänregler och informationskvalitet.

Tekniken kan förändras över tid. Förmågan består så länge organisationen återkommande behöver kunna uttrycka, exekvera och förvalta verksamhetsbeslut på ett begripligt och spårbart sätt.

## Sammanfattning

Regler och beslut bör behandlas som en egen IT-förmåga när beslutslogiken har ett värde och en livscykel som motiverar att den kan förstås, testas, förändras, återanvändas eller spåras oberoende av en enskild applikations implementation.

Det innebär inte att all villkorslogik ska externaliseras.

Den centrala gränsdragningen är:

- domänlogik äger beteenden som naturligt hör ihop med domänens modell,
- Regler och beslut äger explicita verksamhetsbeslut som vinner på separat representation och förvaltning,
- *Process, workflow och ärendehantering* äger ordning, väntan och koordinering,
- Integration och kommunikation äger mekanismerna för kommunikation mellan system,
- Data- och informationshantering äger de tekniska mekanismerna för information och historik,
- Analys, sökning och AI äger probabilistisk inferens och modeller som inte bör förväxlas med deterministiska regler.

Externalisering ska därför vara ett medvetet arkitekturbeslut, inte en reflex. En regelmotor skapar värde först när den gör regelverket lättare att äga, förstå och förändra än motsvarande kodlösning.

Nästa kapitel flyttar fokus från hur beslut uttrycks till hur data och information lagras, historiseras, kopieras och görs tillgängliga utifrån sina kvalitetskrav.

## Källor och vidare läsning

**[K1]** Object Management Group (OMG), *Decision Model and Notation (DMN) 1.5*. Versionsstatus kontrollerad 2026-08-19 mot OMG:s specifikationsregister. https://www.omg.org/spec/DMN/1.5
