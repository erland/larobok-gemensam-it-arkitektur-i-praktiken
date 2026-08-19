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

Hur hårt en standard bör vara styrande bör bero på vad variationen kan orsaka.

Om olika team väljer olika färger på lokala utvecklingsverktyg är konsekvensen liten.

Om olika team däremot använder inkompatibla identitetsprotokoll eller meddelandekontrakt kan variationen skapa:

- säkerhetsrisk,
- integrationskostnad,
- svårförvaltade beroenden,
- dubbel infrastruktur,
- låg återanvändbarhet.

Ju större gemensam konsekvens, desto starkare är argumentet för bindande standardisering.

Man kan förenklat tänka:

```text
Lokal konsekvens
      ↓
Mer lokal frihet

Gemensam konsekvens
      ↓
Starkare standardisering
```

Det är samma logik som ansvarsfördelningen tidigare i boken: beslut bör fattas på den lägsta nivå som fortfarande kan bära hela konsekvensen.

## Interoperabilitet är ett särskilt starkt standardiseringsskäl

Interoperabilitet är ett område där standarder ofta skapar mycket stor nytta.

När flera system måste kommunicera behöver de kunna dela vissa antaganden:

- protokoll,
- kontrakt,
- identifierare,
- semantik,
- felbeteende,
- säkerhetsmekanismer,
- versionsprinciper.

Det är inte nödvändigt att standardisera systemens interna implementation för att uppnå interoperabilitet.

Tvärtom är en viktig arkitekturprincip att standardisera gränssnittet där gemensamhet krävs och lämna intern implementation friare där variation inte skadar helheten.

Detta kan sammanfattas som:

> Standardisera gränsen före insidan.

Det är ofta en bättre strategi än att försöka standardisera hela teknikstacken.

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

En bättre standard kan uttrycka vilka signaler, metadata och korrelationsmekanismer som ska finnas och därefter låta en plattformsprofil eller policy kontrollera dem automatiskt.

Det knyter direkt till kapitel 30: en mogen paved road gör många standarder inbyggda i konsumtionsvägen.

## Standarder och plattformar måste stödja varandra

En standard blir betydligt lättare att följa när plattformen stödjer den.

Anta att organisationen har en standard för:

- tjänsteidentitet,
- observerbarhet,
- containerpaketering,
- CI/CD,
- secrets.

Om varje team manuellt måste implementera alla dessa regler är standarderna en belastning.

Om en golden path däremot automatiskt etablerar:

- workload identity,
- logg- och tracekonfiguration,
- standardpipeline,
- godkänd base image,
- secrets-integration,

blir samma standarder en del av den enklaste vägen.

Det är en viktig princip:

> Gemensamma standarder bör så långt det är rimligt realiseras genom gemensamma tjänster och automation.

Annars riskerar organisationen att skapa ett stort dokumentbibliotek som varje produktteam förväntas implementera separat.

## Standarder och lösningsmönster har olika roller

Ett mönster beskriver ett återkommande sätt att hantera ett problem och dess avvägningar.

En standard uttrycker vilket beteende eller val organisationen har beslutat att gemensamt stödja eller kräva.

Exempel:

- **Mönster:** Backend for Frontend.
- **Standard:** API-kontrakt ska följa organisationens API-konventioner.

Mönstret svarar på:

> När är denna struktur lämplig och vilka konsekvenser får den?

Standarden svarar på:

> När vi exponerar ett API, vilka gemensamma regler gäller?

En organisation kan alltså ha flera godkända mönster som alla måste följa samma standard i sina gränssnitt.

## Standarder och principer har olika abstraktionsnivå

En princip är ännu mer generell.

Exempel:

> Behov före teknik.

En relaterad standard kan säga:

> Nya synkrona tjänstegränssnitt ska använda organisationens fastställda API-kontrakt.

Principen hjälper organisationen att fatta nya beslut. Standarden konkretiserar ett redan etablerat gemensamt beslut.

Om standardkatalogen fylls med formuleringar som egentligen är principer blir den svår att verifiera.

Om principkatalogen fylls med produktnamn blir den snabbt inaktuell.

Separationen behövs för att varje artefakt ska kunna förändras i rätt takt.

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

Detta skapar spårbarhet tillbaka till förmågan och behovet.

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

Denna struktur gör standarden användbar både för människor och för framtida automation.

## Undantag är en del av modellen

Ingen genomtänkt standardmodell bör utgå från att undantag aldrig behövs.

Tvärtom finns det flera legitima orsaker:

- ett verksamhetskrav som standardlösningen inte kan möta,
- ett legacysystem med särskilda begränsningar,
- ett experiment som behöver pröva ny teknik,
- ett externt krav,
- en övergångsperiod under migrering.

Men undantag bör vara medvetna beslut, inte osynliga avvikelser.

Ett undantag bör därför normalt innehålla:

- vilken standard som avviks från,
- varför,
- vilka risker som accepteras,
- vem som beslutat,
- hur länge undantaget gäller,
- när det ska omprövas,
- eventuell migreringsplan.

Det är särskilt viktigt att undantag inte automatiskt blir permanenta.

Tidsbegränsning är ofta ett effektivt sätt att skilja en verklig transition från en ny oavsiktlig standard.

## Många undantag är feedback

Om ett fåtal lösningar behöver avvika kan problemet vara lokalt.

Om många lösningar begär samma undantag bör standardägaren fråga:

> Är standarden fel – eller saknas en legitim variant?

Återkommande avsteg kan indikera att:

- standarden är för snäv,
- plattformen inte möter behovet,
- en ny kvalitetsprofil behövs,
- tekniklandskapet har förändrats,
- standardens rationale inte längre gäller.

Undantag är därför också telemetri för arkitekturstyrningen.

Samma tanke har återkommit genom boken: lokal erfarenhet ska kunna förbättra den gemensamma modellen.

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

På så sätt kan organisationen både standardisera produktion och skapa en kontrollerad väg för lärande.

Detta leder naturligt till nästa kapitel om tekniklivscykel.

## Ansvar på tre nivåer

Bokens tredelade ansvarmodell fungerar även för standarder.

### Gemensam arkitekturnivå

Den gemensamma nivån bör definiera:

- standardmodell och standardtyper,
- hur bindningsgrad uttrycks,
- regler för undantag,
- principer för livscykel,
- tvärgående standarder som påverkar flera förmågor,
- hur standarder kopplas till referensarkitekturer och gemensamma kvalitetskrav.

Den ska inte behöva äga varje detaljstandard.

### Förmågenivå

Förmågeområdet bör äga de standarder som hör till det egna området.

Exempel:

- Integration och kommunikation äger API- och messagingstandarder.
- Identitet och tillit äger identitets- och tjänsteidentitetsstandarder.
- Programvaruutveckling och leverans äger release-, repository- och CI/CD-relaterade standarder.

Förmågeansvaret bör också följa hur standarderna fungerar i praktiken och identifiera behov av förändring.

### Lösnings-/produktnivå

Den lokala lösningen ska:

- förstå vilka standarder som gäller,
- använda rekommenderade vägar när de passar,
- dokumentera lokala beslut som inte behöver standardiseras,
- begära undantag när det finns verkliga skäl,
- ge återkoppling när standarden skapar onödig friktion.

Detta gör standardisering till ett federerat ansvar inom gemensamma ramar snarare än en central lista som en liten grupp försöker detaljförvalta.

## En praktisk analysordning

När organisationen överväger att skapa eller ändra en teknisk standard kan följande frågor användas:

1. Vilken variation försöker vi kontrollera?
2. Vilken gemensam konsekvens orsakar variationen?
3. Behöver vi standardisera gränssnittet, produkten, versionen eller konfigurationen?
4. Vilken bindningsgrad är proportionerlig?
5. Kan standarden överleva ett produktbyte?
6. Vilken plattform eller golden path hjälper konsumenten att följa den?
7. Hur verifieras efterlevnad?
8. Hur hanteras legitima undantag?
9. Vem äger standarden?
10. Vilken signal säger att den bör omprövas eller avvecklas?

Om dessa frågor inte går att besvara är det ofta för tidigt att kalla beslutet en gemensam standard.

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
