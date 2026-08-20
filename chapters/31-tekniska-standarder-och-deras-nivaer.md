# 31. Tekniska standarder och deras nivåer

Gemensam IT-arkitektur behöver mer än principer, mönster och plattformstjänster. Den behöver också ett sätt att uttrycka vilka tekniska val som ska vara gemensamma, vilka som bara rekommenderas och vilka som kan lämnas helt till den enskilda lösningen.

Det är standardernas uppgift.

Men ordet standard används ofta så brett att det tappar precision. En organisation kan kalla allt från ett API-format till en specifik produktversion, en krypteringsinställning eller ett rekommenderat utvecklingsverktyg för ”standard”. Resultatet blir lätt en katalog där beslut med helt olika syfte, stabilitet och bindningsgrad blandas ihop.

En fungerande standardmodell behöver därför svara på flera frågor samtidigt:

- Vad är det som standardiseras?
- Varför behöver just detta vara gemensamt?
- På vilken nivå ligger beslutet?
- Är det ett krav, ett rekommenderat förstahandsval eller bara ett godkänt alternativ?
- Hur länge förväntas beslutet vara stabilt?
- Var hanteras produktversioner och detaljerad konfiguration?
- Hur hanteras undantag och förändring?

Det centrala är inte att maximera antalet standarder. Det är att standardisera där gemensam variation skapar mer kostnad, risk eller friktion än nytta.

## Standardisering är ett medel, inte ett mål

Standardisering kan skapa stora fördelar:

- interoperabilitet,
- återanvändning,
- lägre förvaltningskostnad,
- enklare kompetensförsörjning,
- bättre säkerhets- och kvalitetskontroll,
- snabbare onboarding,
- enklare plattformsstöd,
- mer reproducerbara leveranser.

Men samma mekanism kan också skapa problem om den används för brett. En standard kan låsa fast teknik i onödan, skapa långsamma beslutsvägar, försvåra innovation eller tvinga in olika problem i samma lösning.

Därför bör utgångspunkten inte vara:

> Vad kan vi standardisera?

utan:

> Vilken variation behöver organisationen faktiskt kontrollera – och varför?

Det knyter tillbaka till kapitel 9. Något bör vara gemensamt när konsekvenserna av lokal variation spiller över på andra delar av organisationen. Standarder är ett av verktygen för att hantera just denna typ av gemensamma konsekvenser.

## Fem olika nivåer som ofta blandas ihop

I den här boken skiljer vi mellan fem nivåer av tekniska beslut:

1. arkitektur- och teknikstandard,
2. produktstandard,
3. versions- och supportstandard,
4. konfigurationsstandard,
5. lokalt lösningsval.

De hänger ihop men bör inte dokumenteras som om de vore samma sak.

```text
Arkitektur-/teknikstandard
          ↓
    Produktstandard
          ↓
Versions-/supportstandard
          ↓
 Konfigurationsstandard
          ↓
   Lokal realisering
```

Ju längre ned i kedjan man kommer, desto snabbare förändras ofta informationen.

Det är en viktig orsak till att nivåerna bör separeras.

## Arkitektur- och teknikstandard

En arkitektur- och teknikstandard uttrycker relativt stabila regler eller konventioner för hur en teknisk förmåga ska realiseras eller hur lösningar ska samverka.

Exempel kan vara:

- hur API-kontrakt utformas,
- hur tjänster identifieras,
- hur meddelanden korreleras,
- hur observerbarhet ska exponeras,
- hur containeriserade workloads paketeras,
- vilka principer som gäller för secrets,
- hur releaseidentifiering sker.

Denna typ av standard bör helst överleva ett produktbyte.

En API-standard som bara fungerar så länge organisationen använder en viss gatewayprodukt ligger sannolikt för nära produkt- eller konfigurationsnivån.

En bra arkitekturstandard beskriver i stället vilka egenskaper och kontrakt som ska vara gemensamma.

Det gör standarden stabil och låter plattformar och produkter utvecklas bakom den.

## Produktstandard

En produktstandard anger vilken produktfamilj, tjänst eller teknisk realisering som organisationen rekommenderar eller godkänner för ett visst behov.

Exempel:

- en viss containerplattform,
- en viss relationsdatabasfamilj,
- ett visst CI/CD-system,
- en viss produktivitetssvit,
- ett visst BI-verktyg.

Produktstandarder kan vara rationella när gemensam produktanvändning ger tydliga fördelar:

- samlad kompetens,
- gemensam drift,
- licens- eller avtalsfördelar,
- säkerhetsgranskning,
- standardiserad integration,
- gemensam support,
- färdiga golden paths.

Men produktstandarden ska inte förväxlas med förmågan eller tjänsten.

Om organisationen säger:

> Vår integrationsförmåga är produkt X.

har abstraktionsnivåerna blandats ihop.

Ett bättre sätt är:

```text
Förmåga: Integration och kommunikation
      ↓
Tjänst: Enterprise Messaging
      ↓
Produktstandard: vald produktfamilj
      ↓
Supportmatris: godkända versioner
```

Då kan produkten senare bytas utan att förmågan eller tjänstekontraktet måste omdefinieras från grunden.

## Versions- och supportstandard

En versions- och supportstandard anger vilka konkreta versioner som är tillåtna, rekommenderade eller på väg att avvecklas.

Det är mer dynamisk information än en stabil arkitekturstandard.

Den kan innehålla:

- rekommenderad version,
- minsta stödda version,
- senaste godkända huvudversion,
- supportslut,
- avvecklingsdatum,
- migreringsmål,
- ansvarig för uppgradering.

Den typen av information bör normalt ligga i en separat support- eller livscykelmatris i stället för i själva standarddokumentet.

Annars uppstår ett välkänt problem: varje mindre produktrelease tvingar fram ändring av dokument som egentligen beskriver långsiktiga arkitekturbeslut.

Kapitel 32 fördjupar denna livscykelmodell.

## Konfigurationsstandard

En konfigurationsstandard ligger ännu närmare den tekniska realiseringen.

Exempel:

- cipher suites,
- base images,
- pluginversioner,
- portinställningar,
- exakta retentionvärden,
- CPU- och minnesprofiler,
- kö- och topicnamn,
- timeoutvärden,
- produktens installationsparametrar.

Sådana beslut kan vara mycket viktiga. De är inte mindre styrande bara för att de ligger nära implementationen.

Men de förändras ofta snabbare och behöver därför hanteras i andra artefakter:

- tekniska referenser,
- baselines,
- policy-as-code,
- konfigurationsrepositoryn,
- plattformsprofiler,
- automation.

Ju mer detaljerad en standard är, desto större är också möjligheten att göra den exekverbar i stället för att bara dokumentera den.

En konfigurationsregel som kan valideras automatiskt bör ofta flytta närmare pipeline eller plattform än ett manuellt dokument.

## Lokalt lösningsval

Allt behöver inte standardiseras.

Ett lokalt lösningsval är ett tekniskt beslut vars konsekvenser främst bärs av den lösning eller produkt som fattar beslutet.

Exempel kan vara:

- intern kodstruktur,
- ett mindre bibliotek,
- vissa testverktyg,
- lokala implementationstekniker,
- ett algoritmval utan breda beroenden.

Det betyder inte att valet är oviktigt. Det betyder att organisationen inte behöver skapa en gemensam standard för varje tekniskt beslut.

Detta är en central balanspunkt.

Om allt standardiseras skapas en central beslutsapparat för frågor som lokala team hade kunnat hantera bättre själva.

## Standard, krav och rekommendation är olika saker

En annan vanlig sammanblandning är att själva ordet standard får beskriva både innehållet och bindningsgraden.

Det är bättre att skilja dem åt.

En standard kan exempelvis vara:

- obligatorisk,
- rekommenderad,
- godkänd, men inte förstahandsval,
- under utvärdering,
- på väg att avvecklas.

Detta gör det möjligt att uttrycka en mer nyanserad teknikstyrning.

Anta att organisationen har två databastekniker.

Den ena kan vara:

> Rekommenderad för nya lösningar.

Den andra:

> Godkänd för befintliga lösningar men inte rekommenderad för nyutveckling.

Det är betydligt mer informativt än att båda bara märks ”standard”.

## Bindningsgrad bör följa konsekvens

Hur hårt en standard bör vara styrande bör bero på vad variationen kan orsaka. Lokal variation med liten konsekvens kan lämnas fri, medan variation i exempelvis identitetsprotokoll, meddelandekontrakt eller säkerhetsmekanismer kan skapa gemensam risk och integrationskostnad.

Det är samma logik som tidigare i boken: beslut bör fattas på den lägsta nivå som fortfarande kan bära hela konsekvensen.

Interoperabilitet är därför ett särskilt starkt standardiseringsskäl. När flera system måste kommunicera behöver de dela vissa antaganden om exempelvis protokoll, kontrakt, identifierare, semantik, felbeteende, säkerhetsmekanismer och versionsprinciper. Däremot behöver deras interna implementation inte standardiseras.

En användbar tumregel är:

> Standardisera gränsen före insidan.

Det ger gemensamhet där den behövs utan att låsa hela teknikstacken. Samma princip gör det möjligt att ha flera tekniska realiseringar bakom ett gemensamt kontrakt när deras interna skillnader inte påverkar omgivningen.

## Compliance och verifierbarhet

En standard som inte går att förstå eller verifiera blir svår att styra med.

Varje viktig standard bör därför kunna besvara:

- Vad omfattas?
- Vad krävs?
- Vad rekommenderas?
- Vad är förbjudet?
- Hur verifieras efterlevnad?
- Vem ansvarar för kontrollen?
- Hur hanteras undantag?

Det innebär inte att varje standard behöver hundra kontrollpunkter.

Men en formulering som:

> Lösningen ska ha god observerbarhet.

är för vag för att vara en effektiv teknisk standard.

En bättre standard kan uttrycka vilka signaler, metadata och korrelationsmekanismer som ska finnas och därefter låta en plattformsprofil eller policy kontrollera dem automatiskt. Verifieringen behöver inte alltid vara helt automatiserad, men det bör vara tydligt vilken evidens som visar att kravet är uppfyllt och var kontrollen sker.

Det knyter direkt till kapitel 30: en mogen paved road gör många standarder inbyggda i konsumtionsvägen.

## Standarder behöver stöd i plattformar och andra arkitekturartefakter

En standard blir betydligt lättare att följa när plattformen och de rekommenderade vägarna stödjer den. Om varje team manuellt måste implementera krav på tjänsteidentitet, observerbarhet, containerpaketering, CI/CD och secrets blir standarderna en belastning. Om en golden path i stället etablerar workload identity, logg- och tracekonfiguration, standardpipeline, godkänd base image och secrets-integration blir samma regler en del av den enklaste vägen.

Det är därför ofta bättre att realisera gemensamma standarder genom tjänster, automation och policy-as-code än att lämna dem som dokument som varje team tolkar separat.

Samtidigt har standarder, mönster och principer olika roller. Ett mönster beskriver ett återkommande sätt att hantera ett problem och dess avvägningar. En standard uttrycker vilket beteende eller val organisationen har beslutat att stödja eller kräva gemensamt. En princip är mer generell och hjälper organisationen att fatta nya beslut.

Exempel:

- **Princip:** behov före teknik.
- **Mönster:** *Backend for Frontend*.
- **Standard:** API-kontrakt ska följa organisationens API-konventioner.

Separationen gör att varje artefakt kan förändras i rätt takt. Om standardkatalogen fylls med principer blir den svår att verifiera; om principkatalogen fylls med produktnamn blir den snabbt inaktuell.

## Produktstandarder bör kopplas till tjänster

En produktstandard är mest begriplig när det är tydligt vilken tjänst eller vilket behov produkten realiserar.

I stället för:

> Produkt X är standard.

bör man kunna läsa:

```text
Tjänst: Container Application Platform
      ↓
Produktstandard: produktfamilj X
      ↓
Supportmatris: versioner A och B
      ↓
Plattformsprofil: standard / high availability
```

Detta skapar spårbarhet tillbaka till förmågan och behovet. Det blir också tydligare när två produktstandarder faktiskt realiserar samma tjänst men för olika användningsfall eller kvalitetsprofiler; då kan organisationen formulera valkriterier i stället för att behandla båda som likvärdiga standardprodukter.

Det gör också produktportföljen lättare att ifrågasätta.

Om en produkt inte längre realiserar ett relevant tjänsteerbjudande finns det ett tydligt skäl att avveckla den i stället för att behålla den för att den ”alltid har varit standard”.

## Ett standarddokument behöver en tydlig struktur

En praktisk standardbeskrivning kan exempelvis innehålla:

### Syfte

Vilket problem eller vilken gemensam risk ska standarden hantera?

### Omfattning

Vilka lösningar, tjänster eller scenarier omfattas?

### Standardnivå

Är detta:

- arkitektur-/teknikstandard,
- produktstandard,
- versions-/supportstandard,
- konfigurationsstandard?

### Bindningsgrad

Är den:

- obligatorisk,
- rekommenderad,
- godkänd,
- under utvärdering,
- under avveckling?

### Styrande regler

Vilka beteenden eller val gäller?

### Rationale

Varför finns standarden?

### Verifiering

Hur avgör man om en lösning följer standarden?

### Relationer

Vilka:

- förmågor,
- plattformstjänster,
- mönster,
- referensarkitekturer

berörs?

### Undantag

Vilken process gäller när standarden inte passar?

### Livscykel

Vem äger standarden och när ska den omprövas?

Denna struktur gör standarden användbar både för människor och för framtida automation. Den hjälper också läsaren att skilja själva standardbeslutet från den supportmatris, konfiguration eller produktdokumentation som förändras snabbare.

## Undantag är en del av modellen – och en källa till feedback

Ingen genomtänkt standardmodell bör utgå från att undantag aldrig behövs. Legitima orsaker kan vara ett verksamhetskrav som standardlösningen inte kan möta, ett legacysystem, ett externt krav, ett experiment eller en övergångsperiod under migrering.

Ett undantag bör vara ett synligt och tidsbegränsat beslut som anger vilken standard som frångås, varför, vilka risker som accepteras, vem som beslutat, hur länge undantaget gäller och vad som krävs för omprövning eller migration.

Undantagen ger samtidigt återkoppling till standardägaren. Om många lösningar behöver samma avsteg kan standarden vara för snäv, en legitim variant saknas, plattformen inte möta behovet eller tekniklandskapet ha förändrats. Många liknande undantag ska därför behandlas som en signal om att den gemensamma modellen behöver prövas, inte bara som lokala avvikelser.

## Standardisering får inte bli produktlåsning av gammal vana

En särskild risk uppstår när standardkatalogen blir en historisk lista över produkter som någon gång godkänts.

Då kan standardisering byta karaktär från:

> Vi kontrollerar viktig variation.

Till:

> Vi bevarar befintlig teknik.

För att motverka detta behöver varje standard ha ett synligt rationale och en livscykel.

En produktstandard bör exempelvis kunna motiveras med:

- vilken tjänst den stödjer,
- vilken gemensam nytta den ger,
- vilka alternativ som finns,
- vilka kostnader ett byte skulle medföra,
- när beslutet ska omprövas.

Det är inte samma sak som att ständigt byta teknik. Stabilitet har ett värde. Men stabilitet bör vara ett medvetet arkitekturval, inte resultatet av att ingen längre vet varför standarden finns.

## Experiment behöver en egen väg

Om standarder är för absoluta riskerar all teknisk förnyelse att bli ett avsteg.

Det är en dålig modell.

En mogen organisation bör kunna skilja mellan:

- produktion inom etablerad standard,
- kontrollerad pilot,
- teknisk utvärdering,
- sandboxexperiment.

Ett experiment kan få andra krav än en produktionstjänst, men behöver samtidigt ha tydliga gränser:

- vilken data får användas?
- vilka miljöer får nås?
- hur länge pågår försöket?
- vad krävs för att tekniken ska gå vidare?
- vem ansvarar för städning om försöket avslutas?

På så sätt kan organisationen både standardisera produktion och skapa en kontrollerad väg för lärande. Ett lyckat experiment ska inte automatiskt bli ny standard; det behöver först bedömas mot behov, kvalitetskrav, supportbarhet och konsekvenser för resten av tekniklandskapet.

Detta leder naturligt till nästa kapitel om tekniklivscykel.

## Ansvar på tre nivåer

Standardisering följer samma ansvarmodell som resten av boken. Den gemensamma arkitekturnivån definierar standardmodell, bindningsgrader, undantagsprinciper och tvärgående regler. Förmågenivån äger områdesspecifika standarder, exempelvis API-, identitets- eller CI/CD-standarder, och följer hur de fungerar i praktiken. Lösnings-/produktnivån tillämpar standarderna, dokumenterar lokala val och begär undantag när det finns sakliga skäl.

På så sätt blir standardisering ett federerat ansvar inom gemensamma ramar snarare än en central katalog som försöker detaljstyra alla tekniska beslut.

## En praktisk analysordning

När organisationen överväger att skapa eller ändra en teknisk standard kan följande frågor användas:

1. Vilken variation försöker vi kontrollera och vilken gemensam konsekvens orsakar den?
2. Är det gränssnittet, produkten, versionen eller konfigurationen som behöver standardiseras?
3. Vilken bindningsgrad är proportionerlig?
4. Kan standarden överleva ett produktbyte?
5. Vilken plattform, golden path eller automation hjälper konsumenten att följa den?
6. Hur verifieras efterlevnad och hur hanteras legitima undantag?
7. Vem äger standarden?
8. Vilken signal säger att den bör omprövas eller avvecklas?

Om frågorna inte går att besvara är det ofta för tidigt att kalla beslutet en gemensam standard.

## Från standardkatalog till kontrollerad variation

Det viktigaste skiftet är att se standarder som ett sätt att styra variation, inte som ett sätt att maximera likformighet.

En bra standardmodell gör därför tre saker samtidigt:

```text
Skyddar det som måste vara gemensamt
              +
Gör standardfallet enkelt att följa
              +
Lämnar utrymme där variation är legitim
```

Detta är också varför standarder fungerar bäst tillsammans med resten av bokens modell:

- principer förklarar riktningen,
- kvalitetskrav förklarar vad som måste uppnås,
- mönster återanvänder beslutserfarenhet,
- plattformstjänster erbjuder gemensamma mekanismer,
- golden paths gör rekommenderade vägar enkla,
- standarder styr den variation som behöver vara gemensam,
- livscykelmodellen låter allt detta förändras kontrollerat.

Nästa kapitel tar just det sista steget: hur teknik går från introduktion och utvärdering till rekommendation, deprecation och slutlig avveckling utan att organisationen antingen fryser fast eller förändras okontrollerat.
