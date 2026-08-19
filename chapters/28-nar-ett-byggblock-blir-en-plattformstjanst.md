# 28. När ett byggblock blir en plattformstjänst

Det är lätt att kalla något för en plattform därför att det är centralt installerat, tekniskt avancerat eller används av flera team. Men central infrastruktur är inte automatiskt en plattformstjänst. Ett kluster, en databasmotor, en meddelandebroker eller ett identitetssystem kan vara viktiga tekniska byggblock utan att vara ett konsumtionsbart erbjudande.

Skillnaden uppstår först när organisationen kan svara tydligt på frågor som: **Vad får konsumenten? Vilket problem löser tjänsten? Hur ansluter man sig? Vilka kvaliteter kan man räkna med? Vad ansvarar konsumenten själv för? Vad händer när något går fel? Hur utvecklas och avvecklas tjänsten?**

Det här kapitlet handlar om den övergången. Det handlar alltså inte i första hand om vilken teknik som ligger under en plattform, utan om vad som krävs för att göra tekniska byggblock till ett förvaltat, begripligt och återanvändbart tjänsteerbjudande.

## Från teknisk komponent till konsumerbart erbjudande

Ett tekniskt byggblock är något en lösning kan byggas av. Det kan vara en databasmotor, en containerorkestrator, ett certifikatsystem, en meddelandebroker eller en loggplattform. Ett plattformserbjudande är däremot något ett team kan **konsumera med förutsägbart ansvar och förutsägbara egenskaper**.

Skillnaden kan beskrivas så här:

```text
Tekniskt byggblock
    ↓
Paketerad funktion
    ↓
Definierat tjänstekontrakt
    ↓
Onboarding och konsumtionsmodell
    ↓
Drift, support och livscykel
    ↓
Plattformstjänst
```

Det centrala är alltså inte bara tekniken, utan den organisatoriska och operativa inramningen runt tekniken.

Anta att en organisation har ett OpenShift-kluster. Det betyder inte automatiskt att organisationen erbjuder en **Container Application Platform**. För att det ska vara ett verkligt tjänsteerbjudande behöver det exempelvis vara tydligt:

- vilka workload-typer plattformen är avsedd för,
- vilka resursprofiler som stöds,
- hur team får tillgång,
- vilka nätverks- och identitetsintegrationer som ingår,
- vilken observability som är tillgänglig,
- hur uppgraderingar hanteras,
- vilka tillgänglighets- och supportnivåer som gäller,
- vilka delar konsumentteamet själv måste bygga och förvalta.

Utan detta har man främst **central infrastruktur med lokala integrationsproblem**.

## Ett plattformserbjudande behöver ha ett tydligt syfte

Det första kravet på en plattformstjänst är att den löser ett återkommande problem som flera konsumenter faktiskt har.

Det är inte tillräckligt att säga:

> Vi har en Kubernetesmiljö.

Ett tjänsteerbjudande behöver snarare säga något i stil med:

> Vi erbjuder en förvaltad exekveringsmiljö för containeriserade applikationer med standardiserad deployment, basobservability, nätverksintegration, identitetsintegration och definierade resursprofiler.

Skillnaden är viktig. Den första formuleringen börjar med produkten. Den andra börjar med **konsumentens behov och den kapacitet som erbjuds**.

Det här följer samma princip som tidigare delar av boken: behov före teknik. Ett erbjudande bör därför kunna beskrivas utan att produktnamnet är dess huvudsakliga identitet.

```text
Förmåga
  ↓
Behov hos konsumenter
  ↓
Plattformstjänst
  ↓
Tekniska byggblock
  ↓
Produkt / version / konfiguration
```

Produkten är en realisering. Tjänsten är det stabilare kontraktet mot konsumenten.

## Tjänstekontraktet är plattformens kärna

När en teknisk komponent blir en tjänst uppstår ett kontrakt mellan den som tillhandahåller tjänsten och den som konsumerar den. Kontraktet behöver inte vara ett juridiskt dokument eller ett formellt SLA, men det måste vara tillräckligt tydligt för att två team ska kunna samarbeta utan att bygga sitt arbete på antaganden.

Ett användbart tjänstekontrakt bör åtminstone svara på följande frågor:

1. **Vilket behov löser tjänsten?**
2. **Vilka användningsfall stöds?**
3. **Vilka användningsfall stöds uttryckligen inte?**
4. **Vad ansvarar plattformsområdet för?**
5. **Vad ansvarar konsumenten för?**
6. **Vilka kvaliteter erbjuds?**
7. **Hur ansluter eller beställer man tjänsten?**
8. **Hur ser support- och incidentvägen ut?**
9. **Hur hanteras förändringar och avveckling?**
10. **Vilka kostnader eller kvoter är relevanta?**

Det är ofta just frånvaron av dessa svar som gör att en central teknisk miljö upplevs som svår att använda.

## Konsumentansvar och plattformsansvar måste mötas

Ett vanligt misslyckande är att plattformsteamet beskriver vad plattformen gör men inte vad den **inte** gör. Då flyttas ansvar i praktiken mellan team under incidenter och förändringar.

Ta en API Management-tjänst som exempel. Plattformen kan ansvara för:

- gatewayfunktion,
- teknisk exponering,
- policy enforcement,
- grundläggande autentiseringsintegration,
- throttlingmekanismer,
- teknisk loggning och analytics.

Konsumenten behöver fortfarande ansvara för:

- API-kontraktets semantik,
- verksamhetsmässigt ägarskap,
- versionsstrategi,
- korrekt auktorisationslogik,
- bakåtkompatibilitet där det krävs,
- datakvalitet och verksamhetsregler.

Om plattformen börjar ta ansvar för dessa delar flyttar den sig från generell plattformsförmåga in i domänansvar. Om konsumentteamet däremot måste bygga egen gateway, egen throttling, egen certifikathantering och egen loggning har plattformen inte abstraherat tillräckligt mycket av den återkommande tekniska friktionen.

Ett bra plattformserbjudande hittar en användbar gräns mellan dessa två ytterligheter.

## Plattformen ska abstrahera återkommande komplexitet

En av de viktigaste anledningarna att skapa en plattformstjänst är att **ta bort komplexitet som inte ger konsumentteamet konkurrens- eller verksamhetsfördelar**.

Ett team som bygger ett handläggningssystem behöver sannolikt förstå sin domänmodell, sina processer och sina kvalitetskrav. Det bör däremot inte behöva bli expert på exempelvis:

- hur databasservern patchas,
- hur certifikat roteras,
- hur meddelandekluster uppgraderas,
- hur backupmedia förvaltas,
- hur observabilitybackend skalas,
- hur underliggande noder livscykelhanteras.

Plattformens uppgift är inte nödvändigtvis att dölja all teknisk komplexitet. Det skulle kunna skapa farliga abstraktioner. Uppgiften är att **äga den komplexitet som med fördel kan bäras gemensamt** och exponera ett kontrakt som är tillräckligt enkelt för konsumenten men tillräckligt transparent för välgrundade arkitekturbeslut.

Det kan beskrivas som:

```text
Underliggande komplexitet
        ↓
Plattformsansvar
        ↓
Stabilt konsumtionsgränssnitt
        ↓
Konsumentens lösningsansvar
```

## Självservice är ofta ett mognadstecken

Om varje anslutning till en plattform kräver ett möte, ett manuellt ärende, handskrivna konfigurationsfiler och flera veckors koordinering finns ett återanvändbart tekniskt erbjudande, men konsumtionsmodellen är fortfarande svag.

Självservice betyder inte att allt måste vara öppet och omedelbart. Det betyder att den normala konsumtionsvägen är **förutsägbar, dokumenterad och så automatiserad som riskbilden tillåter**.

Exempel på självservice kan vara:

- skapa en databasinstans från en godkänd profil,
- registrera ett API,
- skapa ett meddelandetopic,
- begära en workload-identitet,
- skapa ett projekt/namespace i en containerplattform,
- beställa en standardiserad backup-profil,
- ansluta en applikation till central loggning.

Guardrails kan fortfarande finnas. En beställning kan exempelvis kräva informationsklassning, kostnadsställe eller val av återställningsprofil. Skillnaden är att processen är kodifierad och återupprepningsbar i stället för personberoende.

## Onboarding är en del av produkten

Plattformsteam tenderar ibland att se onboarding som dokumentation runt den egentliga tjänsten. För konsumenten är onboarding däremot en del av själva produkten.

En tekniskt mycket bra plattform med dålig onboarding kan i praktiken ha lägre värde än en enklare plattform som är lätt att förstå och börja använda.

En fungerande onboarding behöver normalt hjälpa konsumenten genom tre steg:

### Förstå

Konsumenten behöver snabbt kunna avgöra:

- passar tjänsten mitt behov?
- vilka begränsningar finns?
- vilka kvalitetsprofiler erbjuds?
- vad kommer jag fortfarande att äga själv?

### Ansluta

Det ska finnas en tydlig väg från beslut till fungerande första konsumtion. Det kan vara en portal, ett API, infrastructure-as-code, en pipeline eller en beställningsprocess.

### Operera

Efter onboarding behöver teamet veta:

- var tjänstens status syns,
- hur incidenter rapporteras,
- vilka dashboards eller loggar som finns,
- hur kapacitet justeras,
- hur förändringar kommuniceras,
- hur tjänsten avvecklas.

Om onboarding slutar när kontot skapats har plattformen bara löst en del av konsumtionsproblemet.

## Kvalitetsprofiler gör erbjudandet begripligt

Ett plattformserbjudande bör inte bara lista funktioner. Det behöver också beskriva **vilka kvaliteter konsumenten kan bygga sin lösning på**.

För en databastjänst kan det exempelvis vara relevant att beskriva profiler för:

- tillgänglighet,
- backupfrekvens,
- maximal tolererad dataförlust,
- återställningstid,
- kapacitet,
- kryptering,
- supporthorisont.

För en containerplattform kan andra egenskaper vara centrala:

- resursgränser,
- autoskalning,
- zon-/nodspridning,
- nätverksprofil,
- loggretention,
- support för persistent storage.

Det är inte nödvändigt att varje konsument får ett individuellt SLA. Tvärtom är standardiserade **service tiers eller kvalitetsprofiler** ofta bättre, eftersom de gör kostnad och driftmodell mer förutsägbar.

Exempel:

| Profil | Tillgänglighet | Backup/recovery | Support | Typisk användning |
|---|---|---|---|---|
| Bas | normal kontorstidskritikalitet | standard | kontorstid | interna stödverktyg |
| Kritisk | högre redundans | förstärkt | utökad | centrala verksamhetssystem |
| Experiment | lägre garanti | begränsad | best effort | prototyp och utvärdering |

Tabellen är ett illustrativt exempel, inte en universell profilmodell. Poängen är att kvalitetsnivån blir en **del av erbjudandet**, inte något som varje lösning försöker förhandla fram efteråt.

## Service levels utan falsk precision

SLO och SLA kan vara viktiga, men bara när de beskriver något som plattformen faktiskt kan påverka och mäta.

Ett plattformsteam kan exempelvis lova en viss tillgänglighet för databastjänsten. Det kan däremot inte lova samma tillgänglighet för konsumentens hela verksamhetssystem om applikationen själv har andra felkällor.

Det är därför viktigt att skilja mellan:

- **plattformens service level**,
- **konsumentens applikations-SLO**,
- **verksamhetens end-to-end-behov**.

De hänger ihop men är inte samma sak.

En plattform kan bidra till en högre end-to-end-kvalitet utan att själv ensam kunna garantera den.

## En plattform behöver en tydlig konsumtionsmodell

Konsumtionsmodellen beskriver hur konsumenten faktiskt använder tjänsten. Den kan vara:

- deklarativ konfiguration,
- API,
- CLI,
- portal,
- GitOps/infrastructure-as-code,
- service request,
- SDK eller framework,
- kombinationer av flera vägar.

Det viktiga är inte att välja en viss kanal som standard, utan att konsumtionen är **reproducerbar och går att förstå över tid**.

Om plattformen endast kan användas genom att en enskild specialist gör manuella ändringar på konsumentens vägnar är plattformen svår att skala organisatoriskt, även om den underliggande tekniken skalar utmärkt.

## Supportmodellen måste vara en del av designen

När en tjänst används av många team uppstår nästan alltid supportbehov. Det räcker därför inte att fundera på support efter att plattformen lanserats.

En fungerande supportmodell behöver bland annat tydliggöra:

- vad som räknas som plattformsfel,
- vad som är konsumentens felsökningsansvar,
- vilka signaler båda sidor kan se,
- hur incidenter eskaleras,
- vilka tider och responstider som gäller,
- hur återkommande problem återförs till produktutvecklingen.

Det sista är särskilt viktigt. Support är inte bara en kostnad. Supportärenden är **data om plattformens användbarhet**.

Om många team återkommer med samma fel kan problemet vara:

- dålig dokumentation,
- svagt gränssnitt,
- otydliga defaultvärden,
- för låg automatiseringsgrad,
- ett felaktigt ansvarssnitt,
- ett saknat plattformserbjudande.

## Plattformens livscykel är större än produktens livscykel

Ett plattformserbjudande behöver överleva enskilda produktversioner och ibland även produktbyten.

Anta att en relationell databastjänst i dag realiseras med en viss databasprodukt. Om organisationen senare byter produkt bör konsumenterna i idealfallet fortfarande känna igen de centrala tjänstebegreppen:

- databasinstans,
- kapacitetsprofil,
- backup-policy,
- restoreprocess,
- säkerhetsprofil,
- supporthorisont.

Allt kan inte göras produktoberoende. Produktbyte kan kräva migrering och skapa kompatibilitetsproblem. Men ju bättre tjänstekontraktet är separerat från produktrealiseringen, desto mindre risk att organisationens gemensamma arkitektur blir en katalog över tillfälliga produktnamn.

Livscykeln bör därför hantera minst två nivåer:

```text
Plattformstjänst
    ├─ status och framtida riktning
    ├─ kvalitetsprofiler
    ├─ konsumtionskontrakt
    └─ supportmodell
          ↓
Teknisk realisering
    ├─ produkt
    ├─ version
    ├─ konfiguration
    └─ tekniska byggblock
```

Detta blir särskilt viktigt när standard- och tekniklivscykel fördjupas i senare kapitel.

## En gemensam tjänst behöver inte ha en enda realisering

En vanlig förenkling är att anta att ett tjänsteerbjudande alltid motsvarar en produktinstallation. Så behöver det inte vara.

Ett erbjudande som **Relationell databastjänst** kan exempelvis ha flera profiler eller realiseringar därför att olika workloadtyper har olika constraints. Ett identitetserbjudande kan kombinera katalog, federation, PKI och secrets management. Ett observabilityerbjudande kan bestå av flera byggblock för loggar, metrics och tracing.

Tjänsten är då den stabilare **konsumtions- och ansvarsenheten** ovanpå dessa komponenter.

Det omvända gäller också: en stor produkt kan realisera flera tjänsteerbjudanden. En produktivitetsplattform eller low-code-plattform kan till exempel stödja samarbete, dokumenthantering, automation och applikationsutveckling. Det betyder inte att allt bör beskrivas som ett enda odifferentierat erbjudande.

Produktgränsen är alltså inte automatiskt rätt tjänstegräns.

## När bör man inte skapa en plattformstjänst?

Att paketera något som tjänst skapar också kostnader. Det kräver ägarskap, dokumentation, support, livscykelhantering och ofta automatisering.

Ett byggblock bör därför inte göras till ett gemensamt erbjudande bara för att det är tekniskt möjligt.

Varningssignaler är exempelvis:

- behovet finns bara hos ett enda team,
- användningsfallen är så olika att ett gemensamt kontrakt blir artificiellt,
- tekniken förändras så snabbt att erbjudandet saknar stabil kärna,
- plattformsteamet har inget mandat eller kapacitet att bära supportansvaret,
- konsumenterna behöver ändå förstå och förvalta nästan hela den underliggande tekniken själva,
- den gemensamma lösningen skapar mer samordningskostnad än den tar bort.

I sådana fall kan det vara bättre att ha en standard, ett rekommenderat mönster eller ett referensbyggblock än en full plattformstjänst.

## Plattformskatalogen ska beskriva erbjudanden, inte installationer

En plattformskatalog blir lätt en inventarielista:

- OpenShift,
- Oracle,
- IBM MQ,
- Jenkins,
- Elasticsearch,
- Microsoft 365.

Det är användbart för asset management, men det är inte samma sak som en tjänstekatalog.

En arkitektonisk plattformskatalog bör i första hand uttrycka erbjudanden som:

- Container Application Platform,
- Relationell databastjänst,
- Enterprise Messaging,
- CI/CD Platform,
- Search and Indexing Service,
- Productivity Suite.

Produkten kan anges som aktuell realisering under erbjudandet.

Detta gör katalogen mer robust över tid och hjälper konsumenten att börja med behovet i stället för produktnamnet.

## Konkreta exempel

### Exempel 1: Databasserver kontra relationell databastjänst

En organisation har ett centralt databaskluster. Team kan få ett schema skapat genom att skicka ett ärende till driftorganisationen.

Det finns alltså ett gemensamt tekniskt byggblock. Men konsumenten vet kanske inte:

- vilken tillgänglighet som gäller,
- hur backup fungerar,
- hur restore beställs,
- vilken maxstorlek som stöds,
- hur prestandaproblem felsöks,
- när versionen uppgraderas,
- vem som ansvarar för indexering och schemaförändringar.

För att utveckla detta till **Relationell databastjänst** kan organisationen definiera:

1. stödda databasprofiler,
2. tydliga konsument- och plattformsansvar,
3. standardiserad provisioning,
4. backup-/restoreprofiler,
5. kapacitets- och supportmodell,
6. mätbara service levels där det är relevant,
7. livscykel för produktrealiseringen.

Tekniken kan vara densamma före och efter. Skillnaden är att relationen till konsumenten har blivit en tjänst.

### Exempel 2: Central meddelandebroker kontra Enterprise Messaging

En centralt förvaltad broker kan ta emot meddelanden. Ett plattformserbjudande behöver dessutom beskriva:

- vilka kommunikationsmönster som stöds,
- hur queues/topics provisioneras,
- maxstorlekar och kvoter,
- retention,
- säkerhetsmodell,
- klientbibliotek eller protokoll,
- observability,
- dead-letter-hantering,
- support och versionslivscykel.

Plattformen ska däremot inte bestämma eventens verksamhetssemantik. Det ansvaret ligger kvar hos de domäner som publicerar och konsumerar informationen.

### Exempel 3: Containerkluster kontra Container Application Platform

Ett containerkluster blir ett plattformserbjudande först när team kan behandla det som en definierad exekveringstjänst.

Konsumenten kan exempelvis ansvara för:

- containerimage,
- health checks,
- resursbehov,
- applikationskonfiguration,
- applikationsnära observability.

Plattformen kan ansvara för:

- kluster och noder,
- scheduler,
- plattformsuppgraderingar,
- nätverks- och identitetsintegration,
- basobservability,
- standardiserad deploymentyta.

Det är ansvarskontraktet och konsumtionsvägen, inte förekomsten av Kubernetes eller OpenShift i sig, som gör detta till en plattformstjänst.

## En praktisk mognadstrappa

Övergången från byggblock till tjänst kan ses som en enkel mognadstrappa:

### Nivå 1 – Gemensam teknik

Tekniken finns centralt och flera team kan använda den, men användning och ansvar är starkt personberoende.

### Nivå 2 – Paketerat erbjudande

Syfte, målgrupp, konsumentansvar, plattformsansvar och grundläggande begränsningar är dokumenterade.

### Nivå 3 – Reproducerbar konsumtion

Onboarding, provisioning och standardkonfiguration är dokumenterade och i hög grad automatiserade.

### Nivå 4 – Operativ tjänst

Support, service levels, observability, incidenthantering och livscykel är integrerade delar av erbjudandet.

### Nivå 5 – Produktliknande plattform

Erbjudandet utvecklas aktivt utifrån konsumenternas behov, användningsdata, adoption och återkommande friktion.

Den sista nivån leder direkt vidare till nästa kapitel om **Platform as a Product**.

## Ansvar på tre nivåer

Bokens tredelade ansvarmodell gäller även här.

### Gemensam nivå

Den gemensamma arkitekturen bör definiera:

- vad som menas med plattformstjänst,
- minimikrav på tjänstebeskrivningar,
- gemensamma kvalitetsdimensioner,
- principer för service levels och livscykel,
- hur plattformskatalogen relaterar till förmågor, standarder och referensarkitekturer.

Den bör normalt inte detaljdesigna varje erbjudande.

### Förmågenivå

Förmåge- eller plattformsansvaret bör:

- definiera själva erbjudandet,
- välja relevanta byggblock,
- utforma konsumtionskontrakt,
- skapa onboarding och supportmodell,
- definiera kvalitetsprofiler,
- hantera produktrealisering och teknisk livscykel,
- följa upp användning och friktion.

### Lösnings-/produktnivå

Konsumentteamet bör:

- avgöra om tjänsten faktiskt möter lösningens behov,
- välja rätt profil,
- uppfylla sitt konsumentansvar,
- integrera tjänsten i lösningsarkitekturen,
- eskalera behov som inte täcks av erbjudandet,
- undvika att behandla plattformen som en ursäkt för att hoppa över egen arkitekturanalys.

## Vanliga anti-patterns

### Produktnamnet är tjänsten

Erbjudandet heter enbart efter produkten och beskriver inte vilket konsumentproblem det löser. Resultatet blir att teknikval och tjänstebegrepp blandas ihop.

### Plattform som central ticket-kö

All konsumtion sker genom manuella specialistanpassningar. Plattformsteamet blir flaskhals och självservice uteblir.

### Obegränsat plattformsansvar

Plattformsteamet förväntas felsöka allting som körs på plattformen, inklusive konsumentens domänlogik och applikationskod.

### Obegränsat konsumentansvar

Plattformen tillhandahåller endast rå teknik och förväntar sig att varje konsument själv bygger provisioning, säkerhet, observability och lifecycle automation.

### Falsk standardisering

Alla användningsfall pressas in i samma profil trots tydligt olika kvalitetsbehov.

### Ingen avvecklingsväg

Tjänsten kan beställas men det finns ingen definierad process för migrering, avregistrering, databorttagning eller avveckling.

### Service levels utan mätbarhet

SLA eller SLO skrivs för att tjänsten ska se mogen ut men plattformsteamet saknar telemetry eller kontroll över den kvalitet som lovas.

## Praktisk analysordning

När ett tekniskt byggblock övervägs som gemensam plattformstjänst kan följande ordning användas:

1. **Identifiera det återkommande konsumentbehovet.** Vilken friktion eller risk upprepas i flera lösningar?
2. **Definiera tjänstens avsedda användningsfall.** Vad ska erbjudandet göra lättare?
3. **Avgränsa vad tjänsten inte är.** Vilket ansvar ska ligga kvar hos domänen och konsumenten?
4. **Definiera tjänstekontraktet.** Vad får konsumenten och vad måste konsumenten själv leverera?
5. **Bestäm kvalitetsprofiler.** Vilka nivåer av tillgänglighet, kapacitet, recovery, säkerhet eller support är relevanta?
6. **Utforma konsumtionsvägen.** Hur beställs, provisioneras, ändras och avvecklas tjänsten?
7. **Designa operativ modell.** Support, observability, incidenter, kapacitet och service levels.
8. **Separera tjänst från realisering.** Vilka tekniska byggblock och produkter används i dag, och vilka delar av kontraktet bör överleva ett framtida produktbyte?
9. **Mät faktisk användbarhet.** Användning, ledtid, fel, supportärenden och återkommande avsteg visar om tjänsten fungerar.
10. **Pröva om tjänsten fortfarande bör vara gemensam.** Gemensamt ansvar är ett arkitekturbeslut som kan behöva omprövas.

## Centrala fakta

- Ett tekniskt byggblock blir inte en plattformstjänst bara genom central installation eller gemensam drift.
- En plattformstjänst behöver ett tydligt konsumentproblem, ett tjänstekontrakt och ett explicit ansvarssnitt.
- Onboarding, support, observability och livscykel är delar av erbjudandet, inte sidoaktiviteter.
- Självservice är främst en fråga om reproducerbar och förutsägbar konsumtion, inte om frånvaro av styrning.
- Kvalitetsprofiler gör erbjudandet mer användbart än individuella och ad hoc-baserade överenskommelser.
- Plattformens service level och verksamhetssystemets end-to-end-kvalitet är relaterade men inte identiska.
- Produkt och plattformstjänst bör hållas isär: produkten är en realisering av tjänsten.
- En plattformstjänst kan bestå av flera tekniska byggblock, och en produkt kan realisera flera tjänster.
- Det är inte alltid rätt att skapa en plattformstjänst; ibland är en standard, ett mönster eller ett referensbyggblock tillräckligt.
- När ett erbjudande utvecklas aktivt utifrån konsumentbehov och användningsdata närmar det sig **Platform as a Product**, vilket är nästa steg i modellen.
