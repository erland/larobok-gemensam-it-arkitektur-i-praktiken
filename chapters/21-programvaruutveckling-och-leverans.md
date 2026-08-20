# 21. Programvaruutveckling och leverans

Programvara blir inte verksamhetsnytta när koden är skriven. Den blir verksamhetsnytta först när organisationen på ett kontrollerat sätt kan förvandla förändrad källkod till en verifierad, spårbar och driftsatt version som går att förstå, återskapa och vid behov återställa eller ersätta. Därför är *programvaruutveckling och leverans* en egen gemensam IT-förmåga.

Förmågan omfattar inte all teknik som utvecklare råkar använda. Den handlar om den gemensamma vägen från källkod och ändringsförslag till byggda artefakter, verifierade releaser och kontrollerad produktionssättning. Applikationens exekveringsmiljö samt driftbarhet och motståndskraft behandlas som separata förmågor. Här ligger fokus i stället på själva förändringsflödet.

Det centrala arkitekturproblemet är att leveransflödet både måste ge hög förändringstakt och hög kontroll. En organisation som försöker skapa kontroll genom manuella steg får ofta långsamma, svårreproducerade och personberoende leveranser. En organisation som försöker skapa hastighet genom att ta bort kontroller riskerar i stället att göra produktion till testmiljö. Den gemensamma förmågan behöver därför göra den säkra och reproducerbara vägen till den enklaste vägen.

## Från kod till körande förändring är en sammanhängande kedja

Ett modernt leveransflöde kan förenklat beskrivas som:

```text
Ändring
  ↓
Källkod och versionshistorik
  ↓
Build
  ↓
Automatiserade kontroller
  ↓
Versionerad artefakt
  ↓
Artefaktregister
  ↓
Promotion
  ↓
Driftsättning
  ↓
Verifiering i målmiljö
```

Varje steg lämnar efter sig information som nästa steg behöver kunna lita på. Om länkarna i kedjan är svaga försvinner spårbarheten.

Det räcker exempelvis inte att veta att version `2.8.4` är driftsatt. Organisationen bör kunna svara på frågor som:

- Vilken källkod byggdes?
- Vilket bygge producerade artefakten?
- Vilka beroenden ingick?
- Vilka tester och kontroller kördes?
- Vilken artefakt godkändes?
- Har samma artefakt som testades också satts i produktion?
- Vem eller vilken teknisk identitet initierade produktionssättningen?
- Vilken konfiguration kombinerades med artefakten i målmiljön?
- Vilken release behöver återställas eller ersättas om ett fel upptäcks?

Det gör leveranskedjan till en arkitekturfråga, inte bara till ett verktygsval för utvecklingsteamet.

## Versionshantering är förändringens system of record

Källkod bör versionshanteras på ett sätt som gör förändringar granskningsbara och historiskt spårbara. Det gäller inte bara applikationskod. Även sådant som har direkt påverkan på bygg och leverans bör behandlas som versionshanterad förändring, exempelvis:

- pipeline-definitioner,
- infrastrukturdefinitioner,
- byggskript,
- dependencyfiler,
- policy-as-code,
- driftsättningsspecifikationer,
- databasmigreringar,
- centrala konfigurationsmallar.

Det viktiga är inte att allt ligger i samma repository. Det viktiga är att den förändring som påverkar en release kan identifieras, granskas och kopplas till den levererade versionen.

Branchstrategin är däremot sällan ett självändamål. GitFlow, trunk-based development eller andra modeller är medel för att kontrollera förändring, inte arkitekturmål i sig. En gemensam arkitektur bör därför vara försiktig med att göra en specifik branchmodell till universell regel om organisationens produkter har olika behov.

Det mer stabila kravet är att förändringar ska kunna granskas, integreras och spåras på ett kontrollerat sätt.

## Från build till versionerad artefakt

### Reproducerbara builds minskar osäkerheten

Ett bygge bör i möjligaste mån vara deterministiskt eller åtminstone reproducerbart nog för att organisationen ska kunna förstå hur en artefakt skapades.

Det innebär inte att varje bit i alla byggmiljöer alltid måste vara matematiskt identisk. Det innebär att byggprocessen ska vara så definierad att resultatet inte beror på en enskild utvecklares dator, manuella steg eller oregistrerade lokala beroenden.

Några centrala egenskaper är:

- versionshanterad byggdefinition,
- definierade verktygs- och runtimeversioner där det behövs,
- kontrollerade externa beroenden,
- automatiserad byggprocess,
- spårbart byggresultat,
- reproducerbarhet över tid på en nivå som motsvarar risk och livscykel.

En klassisk varningssignal är formuleringen:

> ”Den går bara att bygga på Johans dator.”

Det betyder inte bara att utvecklarupplevelsen är dålig. Det betyder att organisationen saknar en tillräckligt robust leveransförmåga.

### Build once, promote many

En av de viktigaste principerna i ett kontrollerat leveransflöde är att bygga artefakten en gång och föra samma artefakt vidare mellan miljöerna.

En vanlig men riskfylld modell är:

```text
Källkod → build för test
Källkod → nytt build för acceptans
Källkod → nytt build för produktion
```

Även om samma commit används kan de tre byggena skilja sig. Beroenden kan ha förändrats, byggmiljön kan vara annorlunda eller externa resurser kan ha gett olika resultat.

En starkare modell är:

```text
Källkod
  ↓
Build
  ↓
Versionerad artefakt
  ├─→ test
  ├─→ acceptans
  └─→ produktion
```

Det som promoveras är alltså det redan byggda objekt som har passerat kontrollerna.

Miljöspecifik information – exempelvis endpoint-adresser, skalningsparametrar och secrets – behöver därför normalt hållas separerad från själva byggartefakten. Annars tvingas organisationen bygga om för varje miljö och förlorar en del av spårbarheten.

### Artefakten är leveransens kontrakt

En deploybar artefakt kan vara exempelvis:

- ett containerimage,
- ett Java-paket,
- ett frontendpaket,
- ett operativsystemspaket,
- en serverless-bundle,
- en Helm chart eller annan distributionsartefakt,
- en sammansatt release med flera komponenter.

Artefakten bör ha en stabil identitet. Versionsnummer, digest eller annan oföränderlig identifierare gör det möjligt att veta exakt vilket objekt som har verifierats och satts i drift.

Det är en annan sak än en flytande etikett som `latest`. En sådan etikett kan vara praktisk för människor eller vissa flöden, men bör inte vara den enda identiteten för en produktionsrelease. Om samma namn kan peka på olika innehåll över tid försvagas spårbarheten.

Ett artefaktregister är därför mer än lagringsplats. Det är en del av leveransens kontrollplan och bör kunna stödja:

- versionering,
- åtkomstkontroll,
- retention,
- metadata,
- spårbarhet,
- sårbarhets- och livscykelhantering där det är relevant.

## Pipeline som reproducerbar kontroll

### CI är snabb återkoppling – inte bara en byggserver

Continuous Integration handlar principiellt om att förändringar integreras ofta och verifieras snabbt. CI-plattformen är mekanismen som automatiserar delar av denna återkoppling.

Ett typiskt CI-flöde kan innehålla:

```text
Checkout
  ↓
Build
  ↓
Enhetstest
  ↓
Statisk analys
  ↓
Dependencykontroll
  ↓
Paketering
  ↓
Integrationstest
  ↓
Publicering av artefakt
```

Alla projekt behöver inte exakt samma steg. Risk, tekniktyp och ändringstakt avgör vilka kontroller som är proportionerliga.

Det viktiga är att pipeline inte bara blir en lång lista av obligatoriska kontroller som ingen längre förstår. Varje spärr bör svara mot ett faktiskt kvalitets-, säkerhets- eller leveransbehov.

En kontroll som alltid ignoreras eller rutinmässigt kringgås skapar inte säkerhet. Den skapar bara friktion.

### CD kan betyda två olika saker

Förkortningen CD används både för continuous delivery och continuous driftsättning.

Continuous delivery innebär normalt att programvaran hålls i ett tillstånd där en verifierad version kan produktionssättas genom ett kontrollerat beslut.

Continuous driftsättning går längre: förändringar som passerar de automatiserade kontrollerna kan också sättas i produktion automatiskt.

Skillnaden är viktig eftersom organisationer annars kan prata om ”CI/CD” utan att egentligen ha bestämt vilken grad av automatisering de avser.

Det finns inget universellt krav att all produktion måste använda continuous driftsättning. För vissa system kan en automatiserad pipeline med en explicit produktionsgrind vara rätt balans mellan kontroll och hastighet. För andra kan full automatisering vara lämplig.

Arkitekturfrågan är därför inte:

> Har vi continuous driftsättning?

utan:

> Vilken grad av automatisering och kontroll kräver denna förändringsrisk?

### Pipeline as code gör leveranslogiken granskningsbar

Pipelines påverkar hur programvara byggs, testas och levereras. De är därför en del av den tekniska lösningen och bör behandlas med motsvarande förändringsdisciplin.

När pipeline-definitionen versionshanteras kan organisationen:

- granska förändringar,
- förstå historik,
- reproducera äldre flöden,
- koppla pipelineversion till build,
- återanvända gemensamma komponenter,
- testa leveranslogiken innan den används skarpt.

Pipeline as code innebär däremot inte att varje team bör kopiera hundratals rader YAML till sitt repository. Det skapar bara distribuerad duplicering.

En bättre gemensam modell kan vara:

```text
Gemensamma pipelinekomponenter
          ↓
Standardiserade mallar
          ↓
Projektets deklarativa konfiguration
          ↓
Projektunika tillägg där det behövs
```

Det gör standardvägen enkel samtidigt som avvikande behov fortfarande kan hanteras explicit.

### Automatisering gör kontroll reproducerbar

Manuell kontroll uppfattas ibland som säkrare eftersom en människa ”tittar på” förändringen. I praktiken är många manuella steg både svårgranskade och svårreproducerade.

Exempel:

> ”Kopiera filen till servern och ändra sedan tre värden manuellt.”

Det kan fungera hundra gånger. Men processen har då inget starkt svar på frågor som:

- exakt vad ändrades?
- vilken version användes?
- utfördes alla steg?
- blev de likadana i alla miljöer?
- vem kan reproducera dem efter sex månader?

Automatisering ersätter inte ansvar eller granskning. Den gör den beslutade processen reproducerbar.

Därför är målet inte ”automation till varje pris”, utan att automatisera återkommande mekanik och reservera mänskligt omdöme för de beslut där det faktiskt tillför värde.

### Kvalitetssäkring längs hela flödet

Kvalitet kan inte reduceras till ett stort teststeg precis före produktion. Ju senare ett problem upptäcks, desto större är normalt konsekvensytan och kostnaden för återkoppling.

Kontroller kan därför placeras på flera nivåer:

- lokal utveckling,
- pull request/merge request,
- CI-build,
- integrationsmiljö,
- releasegrind,
- driftsättningsverifiering,
- observation efter produktionssättning.

Exempel på kontroller är:

- kompilering och linting,
- enhetstest,
- kontraktstest,
- integrationstest,
- end-to-end-test,
- statisk kodanalys,
- dependencykontroll,
- licenskontroll,
- container- eller paketanalys,
- policykontroll,
- driftsättning smoke tests.

Det avgörande är inte maximalt antal kontroller utan rätt kontroll på rätt plats, med snabb återkoppling när något misslyckas.

## Software supply chain som tillitskedja

En modern applikation består sällan bara av den kod organisationen själv skriver. Den bygger på:

- open source-bibliotek,
- externa paketregister,
- basimages,
- byggverktyg,
- plugins,
- CI-runners,
- pipelinekomponenter,
- publicerade artefakter.

Därför är leveranskedjan också en software supply chain.

Det räcker inte att applikationskoden är korrekt om en angripare kan manipulera ett beroende, byggmiljön eller artefakten efter byggning.

NIST:s Secure Software Development Framework, SSDF, beskriver säkra utvecklingspraktiker som kan integreras i olika utvecklingslivscykler.[K1] SLSA[K2] fokuserar särskilt på integriteten i programvarans supply chain och på verifierbar provenance – information om varifrån en artefakt kommer och hur den byggdes.

För bokens modell är den viktiga principen:

> Tilliten till en release bör kunna härledas genom leveranskedjan, inte bara antas därför att artefakten ligger i ett internt register.

### Beroenden är både produktivitet och risk

Återanvändning av externa komponenter är en grundläggande del av modern utveckling. Att undvika alla externa beroenden skulle i de flesta fall vara både dyrt och riskfyllt.

Men beroenden skapar livscykelfrågor:

- Vilka komponenter använder vi?
- Vilka versioner?
- Vilka licenser gäller?
- Finns kända sårbarheter?
- Är komponenten fortfarande underhållen?
- Är beroendet direkt eller transitivt?
- Kan versionen uppdateras utan orimlig påverkan?

Dependency management bör därför vara integrerat i leveransförmågan, inte en inventering som görs manuellt någon gång per år.

Samtidigt är sårbarhetsskanning inte ett binärt sanningsmaskineri. En träff behöver bedömas i sitt sammanhang. En komponent kan vara tekniskt närvarande men den sårbara funktionen kanske inte används; omvänt kan frånvaro av kända CVE:er aldrig bevisa att programvaran är säker.

Automatiska fynd är beslutsunderlag, inte färdiga riskbeslut.

### SBOM gör innehållet synligare

En Software Bill of Materials, SBOM, beskriver vilka programvarukomponenter som ingår i en produkt eller artefakt. Standardiserade format som SPDX[K3] gör sådan information maskinläsbar och möjlig att utbyta mellan verktyg och organisationer.

En SBOM löser inte supply-chain-säkerheten på egen hand; den ger synlighet. Värdet uppstår först när informationen används för exempelvis sårbarhets- och licensanalys, incidenter, leverantörsuppföljning och livscykelhantering. En SBOM som bara genereras är dokumentation, inte kontroll.

### Provenance beskriver hur artefakten kom till

SBOM svarar i grova drag på frågan:

> Vad ingår?

Provenance svarar snarare på:

> Hur och var skapades artefakten?

Det kan omfatta information om källa, byggprocess, byggmiljö och de steg som producerade resultatet.

Detta är viktigt eftersom två artefakter med samma deklarerade komponenter ändå kan ha producerats på olika sätt. Provenance stärker möjligheten att verifiera att organisationens avsedda byggkedja verkligen användes.

SLSA:s build track formaliserar delar av detta resonemang genom krav på hur build provenance produceras och vilka egenskaper byggplattformen behöver ha på olika nivåer.

Boken behöver dock inte göra en viss SLSA-nivå till universellt krav. Det relevanta är att supply-chain-kontrollerna anpassas efter konsekvens, hotbild och krav på verifierbarhet.

### Signering kräver verifiering

Digital signering av artefakter kan användas för att knyta en artefakt till en betrodd identitet eller byggprocess och upptäcka manipulation efter signering.

Men signering ger inte värde bara för att signaturen existerar.

Det krävs även en verifieringsmodell:

```text
Artefakt
  ↓
Signatur/attestation
  ↓
Betrodd identitet eller rot
  ↓
Policy för vad som accepteras
  ↓
Verifiering före användning
```

Om organisationen signerar alla containerimages men produktionsplattformen aldrig verifierar signaturen blir kontrollen huvudsakligen kosmetisk.

Sigstore[K4]-ekosystemet är ett exempel på moderna mekanismer för signering och verifiering av programvaruarterfakter. Det viktiga arkitekturbegreppet är dock inte ett specifikt verktyg utan kedjan producera bevis → skydda beviset → verifiera beviset → verkställ policy.

### Pipelineidentiteter och secrets

Leveransflöden behöver ofta autentisera mot:

- artefaktregister,
- målplattformar,
- moln- eller infrastrukturtjänster,
- testresurser,
- kod- och analysverktyg.

Dessa credentials bör inte lagras som klartext i repository eller hårdkodas i pipelinefiler.

Kapitlet om identitet och tillit visade varför tekniska identiteter bör vara separata från personliga användarkonton. Samma princip gäller här: en pipeline som behöver produktionsåtkomst bör använda en dedikerad identitet med tydligt avgränsat mandat.

När plattformen stödjer kortlivade credentials eller workload identity kan det dessutom minska behovet av långlivade statiska hemligheter.

Detta är ett bra exempel på hur förmågorna samverkar: leveransförmågan konsumerar identitetsförmågan i stället för att uppfinna en egen säkerhetsmodell.

## Från promotion till säker driftsättning

### Promotion är ett beslut om samma artefakt

En vanlig missuppfattning är att en release ”flyttas” mellan miljöer. Egentligen är det ofta bättre att tänka att samma artefakt får tillåtelse att användas i en ny miljö.

Exempel:

```text
artifact: sha256:abc...
     ↓
Verifierad i test
     ↓
Godkänd för acceptans
     ↓
Godkänd för produktion
```

Promotion kan vara helt automatisk eller innehålla explicita beslutspunkter. Det viktiga är att organisationen inte tappar kopplingen mellan den testade och den produktionssatta artefakten.

Miljöspecifik konfiguration behöver däremot fortfarande hanteras. ”Samma artefakt” betyder inte ”identisk miljö”.

### Driftsättningsstrategin är en del av förändringsrisken

Produktionssättning är inte bara ett kommando som startar en ny version. Strategin påverkar hur fel kan upptäckas och begränsas.

Exempel på angreppssätt är:

- rolling driftsättning,
- blue/green,
- canary,
- trafikstyrd gradvis utrullning,
- kontrollerad aktivering med funktionsflaggor.

Vilken strategi som passar beror på bland annat:

- systemets arkitektur,
- datamodellens kompatibilitet,
- trafikmönster,
- möjlighet att köra flera versioner parallellt,
- konsekvensen av fel,
- hur snabbt fel kan detekteras.

Det är alltså inte självklart att den mest avancerade driftsättningsstrategin är bäst. En liten intern batchtjänst kan behöva en mycket enklare modell än en publik tjänst med kontinuerlig trafik.

### Rollback och roll-forward

Att kunna gå tillbaka till föregående version låter som en självklar säkerhetsmekanism. Men rollback kan vara komplicerat när releasen har förändrat:

- databasschema,
- externa kontrakt,
- meddelandeformat,
- tillstånd,
- irreversible data.

Därför behöver leveransstrategin ibland utformas för roll-forward snarare än ren rollback.

Ett enkelt exempel är en bakåtkompatibel databasmigrering där den gamla och nya applikationsversionen kan köras under en övergångsperiod. Om ett fel upptäcks kan en korrigerad applikationsversion då levereras utan att databasen först måste återställas.

Förmågan behöver alltså stödja säkra förändringsmönster, inte bara en ”rollback-knapp”.

### Funktionsflaggor separerar driftsättning från aktivering

Funktionsflaggor kan göra det möjligt att sätta kod i produktion utan att omedelbart aktivera funktionen för alla användare.

Det kan minska risk genom:

- gradvis aktivering,
- begränsning till testgrupper,
- snabb avstängning av en funktion,
- separation mellan teknisk driftsättning och verksamhetsmässig lansering.

Men flags skapar också tillstånd och kombinationer som behöver hanteras. Gamla flags som aldrig tas bort blir teknisk skuld och kan göra testmatrisen svår att förstå.

Funktionsflaggor bör därför ha ägarskap och livscykel, inte behandlas som permanent konfiguration.

## Standardvägen som plattformserbjudande

### Utvecklarupplevelse är en arkitekturfråga

Om den gemensamma leveransvägen är svår att använda kommer team att skapa egna genvägar.

Det betyder att utvecklarupplevelse (*Developer Experience*, DevEx) inte bara är bekvämlighet. Den påverkar:

- följsamhet till standarder,
- ledtid,
- felrisk,
- onboarding,
- kognitiv belastning,
- möjlighet att uppgradera gemensamma arbetssätt.

En stark plattforms- och leveransförmåga bör därför erbjuda en paved road eller golden path: ett välstött standardflöde som är lättare att använda än att bygga motsvarande mekanismer själv.

Exempel kan vara:

- starter projects,
- gemensamma pipeline-mallar,
- standardiserad artefaktpublicering,
- färdiga säkerhetskontroller,
- dokumenterade driftsättningsmönster,
- självservice för nya projekt,
- tydliga felmeddelanden och feedback.

Detta är en viktig gräns mot central detaljstyrning. En golden path bör göra rätt sak enkel, inte göra alla andra lösningar omöjliga.

### Standardisering på rätt abstraktionsnivå

Det är lätt att standardisera för långt ner i verktygsstacken:

> ”Alla ska använda Jenkins.”

Men det långsiktiga behovet är snarare:

> ”Organisationen behöver en CI/CD-förmåga med reproducerbara builds, spårbara artefakter, säkra pipeline-identiteter, gemensamma kontroller och kontrollerad förflyttning.”

Jenkins, GitHub Actions, GitLab CI eller andra produkter kan vara realiseringar av detta behov. Produkten kan vara standardiserad under en period, men bör inte förväxlas med själva förmågan.

På samma sätt är IntelliJ IDEA, Visual Studio Code och liknande utvecklarverktyg delar av developer tooling – inte arkitekturförmågan i sig.

Detta följer bokens genomgående modell:

```text
Förmåga
  ↓
Plattformstjänst / standardväg
  ↓
Tekniska byggblock
  ↓
Produkt och version
```

### Gemensamma tjänster inom förmågan

**Source Code Management.**

En gemensam källkodstjänst kan ge:

- repositoryhosting,
- autentisering och åtkomstkontroll,
- reviewflöden,
- branch policies,
- audit,
- integration med CI/CD.

Den bör däremot inte kräva att alla produkter har identisk repositorystruktur eller branchmodell om behoven skiljer sig.

**CI/CD Platform.**

En gemensam CI/CD-plattform kan erbjuda:

- runners/agents,
- pipelineexekvering,
- gemensamma mallar,
- secretsintegration,
- artefaktintegration,
- policykontroller,
- driftsättningsintegration,
- loggning och support.

Plattformen bör leverera ett kontrakt och en standardväg snarare än bara en installerad byggserver.

**Artifact Repository.**

Artefakttjänsten bör kunna lagra och förvalta deploybara objekt och beroenden med tydlig identitet, åtkomstkontroll och livscykel.

**Developer Tooling.**

Developer tooling kan omfatta gemensamma IDE-standarder, plugins, lokala utvecklingsverktyg, projektskapande, SDK:er och diagnostik. Värdet ligger i reducerad friktion och kompatibilitet med den gemensamma leveransvägen.

## Ansvar på tre nivåer

Den gemensamma arkitekturnivån bör ange de stabila kraven: spårbar och reproducerbar leverans, miniminivåer för supply-chain-integritet, artefaktidentitet, pipelineidentiteter och hur avsteg hanteras. Den bör inte göra varje teams pipeline identisk.

Förmågenivån utvecklar den praktiska standardvägen genom exempelvis källkodstjänst, CI/CD-plattform, artefaktregister, gemensamma pipelinekomponenter, relevanta kontroller, dokumentation, självservice och support. Återkommande lokala workarounds är en signal om att det gemensamma erbjudandet behöver utvecklas.

Produktteamet ansvarar fortfarande för sin källkod, relevanta tester, kompatibla kontrakts- och databasförändringar, driftsättningsstrategi, beroenden och att den egna pipelinen faktiskt ger rätt produktbeteende. En central plattform kan automatisera mekaniken, men inte avgöra om verksamhetslogiken är korrekt.

## Vanliga anti-patterns

Några återkommande felsätt är:

- **CI/CD som verktygsnamn:** en installerad byggserver förväxlas med en faktisk leveransförmåga.
- **Pipeline-kopiering:** projekt duplicerar stora pipelinefiler i stället för att återanvända versionerade komponenter.
- **Bygg om per miljö:** test och produktion får inte nödvändigtvis samma artefakt.
- **Manuell produktionssättning:** personberoende kommandon gör leveransen svår att reproducera och auditera.
- **Personliga pipelinecredentials:** leveransflödet binds till en individs konto i stället för en avgränsad teknisk identitet.
- **Kontroller utan beslutsmodell:** sårbarhetsfynd behandlas antingen som absoluta sanningar eller ignoreras helt.
- **Bevis som aldrig används:** SBOM produceras utan att konsumeras, eller artefakter signeras utan att signaturen verifieras.
- **Golden path som golden cage:** standardvägen gör legitima avsteg så svåra att team bygger parallella flöden utanför plattformen.

## En praktisk analysordning

När ett utvecklingsområde ska etablera eller förbättra sin leveransväg kan följande ordning användas:

1. Identifiera vad som ska levereras. Vilka typer av artefakter och målmiljöer finns?
2. Kartlägg förändringskedjan. Från commit till produktion: vilka steg finns och vilka är manuella?
3. Definiera spårbarhetsbehovet. Vad måste kunna kopplas från körande version tillbaka till källa och build?
4. Bestäm byggprincipen. Hur görs bygget reproducerbart och hur separeras miljökonfiguration?
5. Definiera kvalitetsgrindar. Vilka tester och kontroller behövs utifrån risk?
6. Analysera supply chain. Vilka externa beroenden, byggverktyg och register behöver kunna betros och följas upp?
7. Definiera artefaktflödet. Hur versionssätts, lagras och promoveras artefakter?
8. Bestäm identitets- och secretsmodell. Vilka tekniska identiteter får göra vad?
9. Välj driftsättning- och återställningsstrategi. Hur begränsas förändringsrisk och hur hanteras fel?
10. Skapa standardvägen. Vilka delar kan plattformiseras och återanvändas för flera team?
11. Mät friktion och effekt. Var väntar teamen, var sker manuella ingrepp och vilka kontroller ger verkligt värde?
12. Förbättra gemensamma byggstenar utifrån användningen. Återkommande speciallösningar är signaler om att standardvägen behöver utvecklas.

Denna ordning gör att CI/CD inte börjar som en verktygsupphandling. Den börjar i vad organisationen faktiskt behöver kunna leverera och kontrollera.

## Leveransförmågan är bryggan mellan förändring och drift

Tidigare har vi behandlat var applikationen körs och hur den går att förstå, övervaka och återställa. Här har fokus varit hur en förändring tar sig från källkod till den körande miljön.

De tre förmågorna behöver därför fungera som ett sammanhängande system:

```text
Programvaruutveckling och leverans
              ↓
      versionerad artefakt
              ↓
Applikationsexekvering och runtime
              ↓
      körande workload
              ↓
Driftbarhet och motståndskraft
              ↓
     operativ återkoppling
              ↺
```

Återkopplingen är viktig. Incidenter, prestandaproblem och återställningssvårigheter bör påverka både applikationens arkitektur och leveransvägens kontroller.

En stark leveransförmåga gör alltså mer än att flytta kod snabbt. Den gör förändring spårbar, reproducerbar, verifierbar och säker nog för den verksamhetsrisk som förändringen innebär.

I nästa kapitel lämnar vi den tekniska leveranskedjan och går till den elfte och sista gemensamma IT-förmågan: Arbetsplats, samarbete och produktivitet. Där blir arkitekturfrågan annorlunda. Fokus ligger mindre på egenutvecklad programvara och mer på hur en gemensam digital arbetsmiljö kan standardiseras, styras och utvecklas utan att skapa informationsrisker eller kväva lokal produktivitet.

## Källor och vidare läsning

**[K1]** NIST, *SP 800-218: Secure Software Development Framework (SSDF) Version 1.1*. https://csrc.nist.gov/pubs/sp/800/218/final

**[K2]** SLSA, *SLSA Specification v1.2*. https://slsa.dev/spec/v1.2/

**[K3]** SPDX, *SPDX Specifications*, aktuell stabil 3.0 vid granskningsdatumet. https://spdx.dev/use/specifications/

**[K4]** Sigstore, *Cosign – Signing and Verifying*. https://docs.sigstore.dev/cosign/signing/overview/ och https://docs.sigstore.dev/cosign/verifying/verify/
