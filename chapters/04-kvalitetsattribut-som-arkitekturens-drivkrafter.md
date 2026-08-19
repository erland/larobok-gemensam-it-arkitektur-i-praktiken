# 4. Kvalitetsattribut som arkitekturens drivkrafter

Två system kan erbjuda exakt samma funktion och ändå vara radikalt olika ur arkitektursynpunkt. Det ena kan vara tillgängligt dygnet runt, återhämta sig snabbt efter fel, hantera kraftiga belastningstoppar och vara enkelt att förändra. Det andra kan kräva nattliga driftstopp, ha långa återställningstider, vara svårt att felsöka och bli dyrt att vidareutveckla.

Funktionslistan avslöjar inte den skillnaden.

Arkitektur kan därför inte bara utgå från *vad* ett IT-stöd ska göra, utan också från *hur väl*, *under vilka förutsättningar* och *med vilka konsekvenser*. Sådana egenskaper beskrivs som kvalitetsattribut eller kvalitetskrav, exempelvis tillgänglighet, prestanda, säkerhet, förändringsbarhet och återställningsförmåga. De kan påverka systemets struktur, redundans, teknikval och driftmodell mer än enskilda funktioner.

Kvalitetsattribut fungerar därför som en länk mellan verksamhetskonsekvens och teknisk utformning.

En förenklad kedja är:

```text
Verksamhetskonsekvens
        ↓
Kvalitetsbehov
        ↓
Verifierbart kvalitetskrav
        ↓
Arkitekturdrivare
        ↓
Arkitekturval och tekniska mekanismer
        ↓
Verifiering i test och drift
```

Detta kapitel handlar om hur den kedjan byggs. Senare kapitel visar hur olika förmågor och plattformstjänster realiserar delar av kvalitetsbehoven tekniskt.

## Funktionella krav räcker inte

Funktionella krav svarar typiskt på frågor som:

- vad användaren ska kunna göra,
- vilken information som ska kunna registreras,
- vilka beräkningar som ska utföras,
- vilka händelser som ska hanteras,
- vilket resultat en process ska ge.

De är nödvändiga, men de säger ofta ganska lite om den arkitektur som krävs.

Anta att två lösningar båda uppfyller kravet:

> Handläggaren ska kunna öppna ett ärende och se dess dokument.

Den ena lösningen kanske accepteras om dokumenten ibland tar fem sekunder att visa och tjänsten kan vara otillgänglig någon timme under natten. Den andra kanske används i en verksamhet där dokument måste visas inom en sekund och där ett avbrott efter några minuter får operativa konsekvenser.

Funktionen är densamma. Arkitekturproblemet är det inte.

Det är därför uttryck som ”systemet ska vara snabbt”, ”lösningen ska vara säker” eller ”tjänsten ska ha hög tillgänglighet” är otillräckliga. De anger en önskad riktning men inte vilken nivå som faktiskt behövs.

Arkitekten behöver förstå vad som händer när kvaliteten inte uppnås.

## Börja i konsekvensen

Ett kvalitetskrav blir betydligt starkare när det kan härledas från en konkret verksamhetskonsekvens.

Jämför:

> Systemet ska ha hög tillgänglighet.

med:

> Om tjänsten är otillgänglig under ordinarie handläggning kan arbete tillfälligt köas, men efter 30 minuter uppstår en oacceptabel operativ påverkan.

Den senare formuleringen gör det möjligt att diskutera vilken återställningsförmåga, redundans och övervakning som faktiskt behövs.

Samma princip gäller andra kvaliteter. Ett prestandakrav blir användbart först när svarstid kopplas till belastning och användarprocess. Skalbarhet behöver på motsvarande sätt uttryckas genom exempelvis förväntad topp, hur snabbt belastningen förändras och vad som händer om kapaciteten inte räcker.

Kvalitetskravet blir då ett uttryck för ett verkligt behov, inte en allmän ambition.

## Kvalitetsattribut behöver scenarier

Ett praktiskt sätt att göra kvalitetskrav konkreta är att formulera dem som kvalitetsattributsscenarier.[K1]

Ett sådant scenario beskriver inte bara egenskapen utan också situationen där den blir relevant. En användbar struktur är:

1. källa – vem eller vad utlöser något,
2. stimulus – vilken händelse som inträffar,
3. berörd del – vilken del av systemet eller tjänsten som påverkas,
4. miljö – under vilka omständigheter händelsen sker,
5. respons – hur systemet ska reagera,
6. responsmått – hur man avgör om reaktionen är tillräcklig.

Ett tillgänglighetsscenario kan exempelvis vara:

> Under normal drift slutar en applikationsinstans svara. Plattformen identifierar felet, styr bort trafik från instansen och återställer önskad kapacitet utan att användarnas pågående arbete går förlorat. Tjänsten ska åter vara inom sin definierade kapacitetsnivå inom två minuter.

Ett förändringsbarhetsscenario kan vara:

> När ett externt regelverk ändrar formatet för ett inkommande meddelande ska den nödvändiga anpassningen kunna göras utan förändringar i domänlogik som inte berör formatet och kunna driftsättas inom organisationens normala leveransflöde.

Scenariernas styrka är att de tvingar fram sammanhang och mätbarhet. ”Hög tillgänglighet” kan betyda nästan vad som helst. ”Återställ kapaciteten inom två minuter vid bortfall av en instans under normal drift” går att designa och testa för.

Det betyder inte att varje kvalitetskrav måste dokumenteras med sex rubriker. Strukturen är ett analysverktyg. Det viktiga är att kravbilden fångar situation, förväntad respons och någon form av verifierbar nivå.

## Från konsekvens till arkitekturdrivare

Alla kvalitetskrav är inte lika viktiga för arkitekturen.

Ett krav blir en arkitekturdrivare när det i betydande grad påverkar systemets struktur eller centrala designbeslut.

Exempel:

- mycket kort tolererad avbrottstid kan kräva redundans och automatisk failover,
- mycket stora belastningsvariationer kan påverka hur kapacitet och tillstånd hanteras,
- stark isolering mellan informationsmängder kan påverka nät, identitet och lagringsstruktur,
- höga krav på spårbarhet kan påverka loggning, identitetspropagering och datamodell,
- krav på snabb förändring kan påverka modularitet, gränssnitt och automatisering,
- interoperabilitet med många externa parter kan göra kontrakts- och versionshantering central.

Poängen är inte att maximera varje kvalitet. Poängen är att identifiera vilka kvaliteter som är avgörande i just den aktuella kontexten och låta dem styra de viktigaste arkitekturvalen.

## Tolv kvalitetsdimensioner i bokens modell

Den här boken använder tolv övergripande kvalitetsdimensioner som ett praktiskt arbetsramverk. De är inte avsedda som en ny universell standard eller som en ersättning för etablerade kvalitetsmodeller. De hjälper oss att ställa återkommande frågor över flera förmågor och plattformstjänster.

### Säkerhet och informationsskydd

Handlar om att skydda information, funktioner och tekniska resurser mot obehörig åtkomst, manipulation, läckage och andra oacceptabla händelser.

Frågor kan vara:

- Vilken information behöver skyddas och från vem?
- Vilka aktörer får utföra vilka handlingar?
- Hur upptäcks och utreds missbruk?
- Hur påverkas säkerhetskraven av informationsklassning och trust boundaries?

”Säkert” är inte ett mätbart krav i sig. Det måste brytas ned till hot, skyddsvärden, kontrollbehov och accepterad risk.

### Tillgänglighet

Beskriver när och i vilken utsträckning en tjänst behöver vara fungerande och åtkomlig.

En procentsiffra kan vara relevant, men den räcker sällan ensam. Man behöver också förstå:

- vilka tidsperioder som är kritiska,
- om planerade avbrott är acceptabla,
- hur långa enskilda avbrott får vara,
- vilka funktioner som behöver fortsätta fungera vid degraderat läge.

Två tjänster med samma årsvisa tillgänglighet kan ha helt olika verksamhetseffekt om den ena har många korta avbrott och den andra ett enda långt avbrott under årets mest kritiska timme.

### Kontinuitet och återställningsförmåga

Tillgänglighet handlar om att tjänsten fungerar. Kontinuitet handlar också om vad som händer när den inte gör det.

Här blir frågor om återställning centrala:

- Hur länge kan verksamheten acceptera att resursen är otillgänglig?
- Hur mycket data eller arbete får gå förlorat?
- Vilka beroenden måste återställas först?
- Hur vet vi att backup faktiskt går att återläsa?
- Kan verksamheten arbeta i ett degraderat eller manuellt reservläge?

Begreppen RTO och RPO används ofta här. RTO uttrycker målet för hur snabbt en resurs eller funktion behöver återställas efter ett avbrott. RPO uttrycker hur långt tillbaka i tiden man som mest accepterar att återställd data ligger, alltså den tolererade dataförlusten uttryckt som en tidpunkt eller tidsmängd.

De bör inte sättas av tekniken ensam. De ska härledas från verksamhetskonsekvens och därefter användas för att utforma backup, replikerings- och återställningslösningar.

### Prestanda

Prestanda omfattar mer än ”snabbt”. Beroende på system kan relevanta mått vara:

- svarstid,
- genomströmning,
- bearbetningstid,
- kötid,
- latenstid mellan händelse och effekt,
- tid till första användbara svar.

Ett prestandakrav behöver ange belastning och situation. Ett svarstidsmål utan att säga hur många samtidiga användare, vilken datamängd eller vilken typ av anrop som avses är svårt att använda.

Det är också viktigt att välja percentiler eller andra mått som speglar användarupplevelsen när medelvärden döljer långsamma ytterfall.

### Skalbarhet och kapacitet

Prestanda beskriver hur lösningen beter sig vid en viss belastning. Skalbarhet handlar om hur väl den kan anpassa sig när belastning eller datavolym förändras.

Frågor kan vara:

- Kan kapacitet ökas utan redesign?
- Hur snabbt måste skalan kunna ändras?
- Krävs horisontell eller vertikal skalning?
- Vilka delar skalar oberoende av varandra?
- Finns tillstånd eller externa beroenden som begränsar skalningen?

Kapacitetskrav bör också skilja mellan normal belastning, förutsebara toppar och extrema men möjliga händelser.

### Spårbarhet och verifierbarhet

I många verksamheter måste det i efterhand gå att förstå vad som hände och varför.

Det kan kräva att man kan besvara frågor som:

- Vilken användare eller tjänst utförde handlingen?
- Vilka data och regler låg bakom ett beslut?
- Vilken version av en komponent eller regel användes?
- Hur följde en transaktion genom flera distribuerade tjänster?
- Kan loggar och andra bevis kopplas ihop till en begriplig händelsekedja?

Spårbarhet påverkar därför identitet, loggning, korrelations-id, beslutsdata och livscykel för revisionsinformation.

### Regelefterlevnad

Vissa kvalitetskrav motiveras av lag, föreskrift, avtal eller intern styrning.

Det viktiga arkitekturellt är att inte stanna vid formuleringen ”av compliance-skäl”. Kravet bör så långt möjligt kunna spåras till:

- den faktiska källan,
- organisationens tolkning,
- den konkreta skyldighet som uppstår,
- vilka tekniska eller organisatoriska kontroller som realiserar den.

Det minskar risken att historiska lösningsval lever kvar som falska regelkrav.

### Tillgänglighet för användare och användbarhet

Ett system kan vara tekniskt tillgängligt men praktiskt oanvändbart.

Denna dimension handlar därför om användarens möjlighet att faktiskt genomföra sitt arbete. Det kan omfatta:

- digital tillgänglighet,
- begriplighet,
- felprevention,
- återkoppling,
- effektivitet i återkommande arbetsmoment,
- stöd för olika användarförutsättningar och hjälpmedel.

Arkitekturen påverkas bland annat genom kanalstrategi, *design system*, klientansvar och hur komplexitet fördelas mellan användargränssnitt och bakomliggande tjänster.

### Förvaltningsbarhet och förändringsbarhet

Ett system ska inte bara fungera idag. Det måste kunna förstås, felsökas, uppgraderas och förändras.

Relevanta frågor är:

- Hur isolerad kan en förändring göras?
- Hur många team eller komponenter behöver samordnas?
- Hur snabbt kan ett fel lokaliseras?
- Kan beroenden uppgraderas utan stora följdändringar?
- Hur automatiserad är test och driftsättning?

Denna dimension är central eftersom många långsiktiga kostnader uppstår efter den första leveransen.

### Interoperabilitet och portabilitet

Interoperabilitet beskriver förmågan att samverka med andra lösningar genom begripliga och stabila kontrakt.

Portabilitet handlar i stället om möjligheten att flytta eller realisera funktion och data i andra miljöer där det är relevant.

De bör inte blandas ihop. Ett system kan vara mycket interoperabelt genom väl definierade API:er men ändå starkt bundet till en viss runtime. Ett annat kan vara tekniskt portabelt men använda proprietära dataformat som gör informationsutbyte svårt.

### Livscykel och hållbarhet

Teknik har livscykler. Produkter går ur support, kompetens förändras och beroenden behöver uppgraderas.

Därför behöver arkitekturen även beakta:

- supporthorisonter,
- uppgraderingsbarhet,
- ersättningsbarhet,
- avveckling,
- teknisk skuld,
- beroenden till produkter eller kompetenser med begränsad livslängd.

Detta är inte samma sak som miljömässig hållbarhet, även om resursförbrukning kan vara relevant. I bokens modell används dimensionen främst för lösningens och teknikvalens långsiktiga livskraft.

### Kostnads- och resurseffektivitet

Kostnad är inte ett separat efterhandsproblem. Den är en del av arkitekturens avvägningar.

En lösning kan nästan alltid göras mer redundant, snabbare eller mer isolerad om tillräckligt mycket resurser används. Frågan är om verksamhetsnyttan motiverar nivån.

Kostnad bör därför kopplas till kvalitetsprofilen:

> Vilken kvalitetsnivå behöver vi, vad kostar den och vad händer om vi väljer en lägre nivå?

Det gör det möjligt att undvika både underdimensionering och överarkitektur.

## En kvalitetsmodell är en checklista – inte ett facit

Det finns etablerade standarder och modeller för programvaru- och systemkvalitet. De är värdefulla för att undvika blinda fläckar och skapa gemensamt språk.

Men en kvalitetsmodell säger inte automatiskt vilka egenskaper som är viktigast för en viss lösning.

Två system kan båda bedömas utifrån säkerhet, prestanda och förändringsbarhet men prioritera dem olika. Ett internt analysverktyg kan tolerera avbrott men kräva hög datakvalitet. En publik tidskritisk e-tjänst kan prioritera tillgänglighet och kapacitet mycket högre. Ett långlivat kärnsystem kan behöva lägga särskild vikt vid förändringsbarhet och tekniklivscykel.

Arkitekturarbetet börjar därför inte med att ge alla kvalitetsattribut högsta prioritet. Det börjar med att förstå vilka konsekvenser som är viktigast.

## Konflikter mellan kvaliteter är normala

Kvalitetsattribut drar ofta arkitekturen i olika riktningar. Mer redundans kan öka tillgänglighet men också kostnad och komplexitet. Starkare säkerhetskontroller kan påverka användbarhet eller svarstid. Caching kan förbättra prestanda men försvåra konsistens, och maximal portabilitet kan kräva att värdefulla plattformsspecifika funktioner avstås.

Detta är inte tecken på dålig kravställning utan en normal del av arkitekturarbetet. Här behöver analysen framför allt göra tre saker tydliga:

1. vilka verksamhetskonsekvenser kvaliteterna representerar,
2. vilken miniminivå som faktiskt krävs,
3. vilka konflikter som behöver hanteras som explicita beslut.

Hur sådana beslut dokumenteras, motiveras och omprövas behandlas i nästa kapitel.

## Högsta möjliga kvalitet är sällan rätt mål

Att kräva exempelvis aktiv-aktiv drift, ingen dataförlust, extrem svarstid eller maximal portabilitet överallt kan låta robust men driva stor kostnad och komplexitet utan motsvarande nytta. Kvalitetsnivån behöver i stället vara tillräcklig för verksamhetsbehovet.

Det är särskilt viktigt för gemensamma plattformstjänster. Om varje erbjudande dimensioneras för den mest extrema konsumenten blir det onödigt dyrt för alla andra. Ett bättre arbetssätt kan vara att erbjuda ett fåtal definierade kvalitetsprofiler, exempelvis en basprofil och en kritisk profil med högre redundans, kortare återställningsmål och förstärkt övervakning.

Poängen är inte exakt vilka profiler som används, utan att kvalitetsnivån blir en medveten del av tjänsteerbjudandet i stället för dold i implementationen.

## Kvalitetskrav måste kunna verifieras

Ett krav som inte går att observera eller testa riskerar att bli en ambition snarare än ett styrmedel.

Verifiering kan ske på flera sätt:

- prestandatest,
- last- och stresstest,
- failovertest,
- återläsning av backup,
- chaos- eller felinjektionstest där det är lämpligt,
- säkerhetstest och threat modeling,
- tillgänglighetstest med verkliga hjälpmedel,
- driftsövningar,
- mätning av ledtid för förändringar,
- kontroll av logg- och spårbarhetskedjor.

Vissa egenskaper kan mätas kontinuerligt i drift. Andra behöver verifieras genom återkommande övningar eller analyser.

Det viktiga är att redan när kravet formuleras fråga:

> Hur kommer vi att veta att detta är uppfyllt?

Om svaret saknas behöver kravet sannolikt förtydligas.

## SLO, SLA och arkitekturkrav är inte samma sak

Begrepp om tjänstenivå blandas ibland ihop med kvalitetskrav. Ett SLO, service level objective, är ett mål för en observerbar tjänstenivå, medan ett SLA, service level agreement, är ett avtalat åtagande. Ett arkitekturellt kvalitetskrav kan ligga bakom båda men är bredare; exempelvis förändringsbarhet och återställningsförmåga uttrycks inte alltid bäst som en SLA-metrik.

Det är därför bättre att se relationen som:

```text
Verksamhetsbehov
      ↓
Kvalitetskrav
      ↓
Arkitektur och tjänstedesign
      ↓
Mätbara SLO:er där det är relevant
      ↓
SLA eller andra åtaganden där organisationen behöver dem
```

SLO och SLA är alltså möjliga operationaliseringar av vissa kvaliteter, inte ersättningar för kvalitetsanalysen.

## Kvalitetskrav på tre ansvarsnivåer

Den tredelade ansvarmodellen kan tillämpas direkt på kvalitetskraven.

### Gemensam arkitekturnivå

Den gemensamma nivån bör ange sådant som behöver vara jämförbart över flera förmågor och lösningar: vilka kvalitetsdimensioner som alltid ska bedömas, gemensamma definitioner och mätprinciper samt eventuella bas- eller miniminivåer. Den bör däremot vara försiktig med att sätta samma höga nivå för alla system.

### Förmågenivå

Förmågeansvariga översätter de gemensamma dimensionerna till egenskaper i sina erbjudanden. En databastjänst kan exempelvis behöva beskriva backup, återställning och kapacitet, medan en identitetstjänst behöver tydliggöra bland annat tillgänglighet, säkerhet och spårbarhet.

### Lösnings-/produktnivå

Det konkreta teamet avgör vilken kvalitetsprofil verksamhetsbehovet kräver och analyserar hela lösningskedjan. En plattform med hög tillgänglighet gör inte automatiskt hela systemet högtillgängligt; ett enda svagt beroende kan dominera resultatet. Kvalitet är därför en end-to-end-egenskap.

## Plattformens kvalitet och lösningens kvalitet är olika saker

Detta är en särskilt viktig distinktion i en plattformsorienterad arkitektur.

Anta att en gemensam databastjänst erbjuder automatisk replikeringsmekanism och backup. Det betyder inte att applikationen automatiskt har den återställningsförmåga verksamheten behöver.

Frågor kvarstår:

- Är all nödvändig data med i backupen?
- Kan applikationsversion och databas återställas till kompatibla lägen?
- Hur återställs externa filer eller meddelanden?
- Är återställningsproceduren testad?
- Vet verksamheten hur arbetet återupptas efter avbrottet?

På samma sätt kan en *containerplattform* erbjuda automatisk restart utan att applikationen är motståndskraftig mot fel. En applikation som lagrar kritiskt tillstånd lokalt kan fortfarande förlora arbete när containern ersätts.

Gemensamma plattformar kan alltså möjliggöra kvaliteter, men de kan sällan garantera hela lösningens kvalitet på egen hand.

Detta bör vara tydligt i tjänstekontraktet mellan plattform och konsument:

> Vad garanterar plattformen, vad behöver konsumenten göra och vilka egenskaper uppstår först genom kombinationen?

## Kvaliteter behöver prioriteras tillsammans

Säkerhet, drift, användbarhet, arkitektur och ekonomi bör inte formulera sina kvalitetskrav isolerat. En gemensam analys behöver synliggöra verksamhetskonsekvenser, konflikter och osäkerheter innan lösningen byggs. Resultatet ska vara ett gemensamt beslutsunderlag, inte en stapel av specialistkrav som alla behandlas som absoluta.

## När kraven är osäkra

I tidiga faser finns sällan exakta svar på allt. Det är inte ett skäl att hoppa över kvalitetsanalysen, utan att uttrycka osäkerheten. En osäker belastningsprognos kan exempelvis dokumenteras som ett antagande som ska kapacitetstestas tidigt, och ett preliminärt RTO som något som måste verifieras före produktionssättning.

Det är bättre än falsk precision. Moget arkitekturarbete gör antaganden synliga och ger dem en omprövningspunkt.

## Från kvalitetskrav till arkitekturella taktiker

När kvalitetskravet är tydligt kan arkitekturen börja välja mekanismer som påverkar egenskapen.

Exempel:

| Kvalitetsbehov | Möjliga arkitekturella mekanismer |
|---|---|
| Kort avbrottstid | redundans, health checks, failover, isolering |
| Låg svarstid | caching, indexering, minskad nätverksrundtur, asynkronisering |
| Hög förändringsbarhet | modulära gränser, tydliga kontrakt, automatiserade tester |
| Spårbarhet | korrelations-id, auditlogg, identitetspropagering, versionsinformation |
| Skalbarhet | stateless bearbetning, partitionering, köer, horisontell skalning |
| Stark informationssäkerhet | autentisering, auktorisation, kryptering, segmentering, secrets-hantering |

Listan är medvetet generell. En mekanism är inte automatiskt rätt bara för att den kan förbättra en viss kvalitet. Caching kan förbättra svarstid men skapa konsistensproblem. Redundans kan förbättra tillgänglighet men öka komplexitet. Asynkron kommunikation kan förbättra frikoppling men göra felsökning och konsistens svårare.

Det är därför kvalitetskraven behöver följas av explicita arkitekturbeslut och avvägningar.

## Ett sammanhängande exempel

Anta att en myndighet ska införa en *publik e-tjänst* för en ansökan som har en tydlig sista ansökningsdag.

Det funktionella behovet är enkelt uttryckt:

> En sökande ska kunna lämna in sin ansökan digitalt.

Men verksamhetsanalysen visar flera konsekvenser:

- belastningen ökar kraftigt under de sista timmarna före deadline,
- en misslyckad inlämning kan få rättslig eller ekonomisk betydelse för den sökande,
- känsliga uppgifter behandlas,
- användaren behöver kunna bevisa att ansökan togs emot,
- efter deadline minskar den akuta belastningen kraftigt.

Ur detta kan kvalitetsbehov härledas.

**Kapacitet:** tjänsten behöver hantera en stor men tidsbegränsad topp.

**Tillgänglighet:** avbrott under de sista timmarna är betydligt mer kritiska än under lågtrafik.

**Spårbarhet:** mottagandet behöver kunna bevisas i efterhand.

**Säkerhet:** uppgifter och identiteter behöver skyddas genom hela flödet.

**Återställning:** ett fel får inte leda till att redan mottagna ansökningar försvinner.

Detta leder i sin tur till arkitekturfrågor:

- Behövs elastisk kapacitet?
- Hur hanteras ett beroende som inte klarar samma topp?
- Kan mottagning frikopplas från senare bearbetning?
- Hur skapas ett oberoende kvitto på mottagandet?
- Vilka delar behöver vara synkront tillgängliga vid deadline?
- Vilket RPO är acceptabelt för mottagna ansökningar?
- Hur provar vi scenariot före den kritiska perioden?

Nu driver verksamhetskonsekvenserna arkitekturen. Teknikdiskussionen får en tydlig grund.

Det är skillnaden mellan att säga ”bygg en robust e-tjänst” och att faktiskt kunna motivera vad robust betyder.

## Centrala fakta

- Funktionella krav beskriver vad ett IT-stöd ska göra; kvalitetsattribut beskriver viktiga egenskaper hos hur det ska fungera och förändras.
- Kvalitetsattribut blir arkitekturdrivande när de påverkar systemets struktur eller centrala designbeslut.
- Kvalitetskrav bör så långt möjligt härledas från verksamhetskonsekvenser, inte från generella teknikambitioner.
- Kvalitetsattributsscenarier gör krav konkreta genom att beskriva stimulus, miljö, respons och verifierbart responsmått.
- Bokens tolv kvalitetsdimensioner är ett praktiskt arbetsramverk, inte en ny universell kvalitetsstandard.
- Högsta möjliga nivå på alla kvaliteter är normalt varken ekonomiskt eller arkitekturellt rimlig.
- Konflikter mellan kvaliteter är normala och behöver hanteras som explicita avvägningar.
- RTO och RPO är verksamhetsdrivna återställningsmål och bör inte sättas enbart utifrån vad tekniken råkar erbjuda.
- Ett kvalitetskrav bör redan vid formuleringen kopplas till hur det ska verifieras.
- Gemensamma plattformstjänster kan möjliggöra kvaliteter men garanterar sällan hela lösningens end-to-end-kvalitet.
- Gemensam nivå, förmågenivå och lösnings-/produktnivå har olika ansvar för kvalitetskraven.
- SLO och SLA kan operationalisera vissa kvaliteter men ersätter inte den bredare kvalitetsanalysen.
- Osäkra kvalitetskrav bör uttryckas som antaganden och verifieringsbehov i stället för med falsk precision.

## Begrepp att känna till

Kvalitetsattribut – en egenskap hos ett system eller en tjänst som beskriver hur väl eller under vilka förutsättningar den fungerar, exempelvis tillgänglighet, prestanda eller förändringsbarhet.

Kvalitetskrav – ett krav som preciserar önskad eller nödvändig nivå för ett kvalitetsattribut.

Arkitekturdrivare – ett behov, begränsning eller kvalitetskrav som i betydande grad påverkar arkitekturens struktur och centrala beslut.

Kvalitetsattributsscenario – en konkret situation som beskriver stimulus, miljö, berörd del, förväntad respons och hur responsen mäts.

RTO (Recovery Time Objective) – mål för hur snabbt en funktion eller resurs behöver återställas efter ett avbrott.

RPO (Recovery Point Objective) – mål för hur långt tillbaka återställd data som mest får ligga efter ett avbrott, och därmed vilken dataförlust som kan tolereras.[K2]

SLO (Service Level Objective) – ett mätbart mål för en observerbar tjänstenivå.[K3]

SLA (Service Level Agreement) – ett formellt åtagande om tjänstenivå mellan parter, ofta med definierade ansvar eller konsekvenser.

Avvägning – en avvägning där förbättring av en egenskap påverkar kostnad, komplexitet eller en annan kvalitet.

Arkitekturell taktik – en designmekanism som används för att påverka ett kvalitetsattribut, exempelvis redundans för tillgänglighet eller caching för svarstid.

## Källor och vidare läsning

**[K1]** Carnegie Mellon University, Software Engineering Institute (SEI), *Reasoning About Software Quality Attributes* och material om Quality Attribute Scenarios. https://www.sei.cmu.edu/library/reasoning-about-software-quality-attributes/

**[K2]** NIST, *SP 800-34 Rev. 1: Contingency Planning Guide for Federal Information Systems*. https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final

**[K3]** Google, *Site Reliability Engineering – Service Level Objectives*. https://sre.google/sre-book/service-level-objectives/

Vidare läsning: ISO/IEC 25010:2023, *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*. https://www.iso.org/standard/78176.html
