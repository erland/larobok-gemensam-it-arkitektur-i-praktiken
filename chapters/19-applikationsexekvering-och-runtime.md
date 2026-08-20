# 19. Applikationsexekvering och runtime

När en applikation är byggd behöver den någonstans att köras. Det kan låta som en ren infrastruktursfråga, men valet av exekveringsmiljö påverkar nästan allt annat: hur applikationen skalas, uppgraderas, isoleras, övervakas, patchas, återstartas och förvaltas. Runtime är därför inte bara ”servern där koden körs”. Det är en gemensam IT-förmåga med egna ansvar, kontrakt och livscykler.

I en liten miljö kan varje utvecklingsteam självt välja operativsystem, applikationsserver, containerlösning och driftsättningsmodell. I en större organisation leder samma arbetssätt snabbt till en flora av kombinationer som alla behöver patchas, övervakas och hållas säkra. Samtidigt är det lika problematiskt att tvinga alla workloads in i exakt samma tekniska form. En äldre applikation med operativsystemsnära beroenden har andra behov än en stateless backend-tjänst eller ett kortlivat batchjobb.

Kärnfrågan i kapitlet är därför:

> Vad behöver en organisation erbjuda för att applikationer och andra workloads ska kunna köras standardiserat, säkert och förvaltningsbart utan att onödigt låsa lösningarna till en viss produkt eller exekveringsmodell?

Kapitlet behandlar den gemensamma IT-förmågan *Applikationsexekvering och runtime*. Fokus ligger på exekveringsmodeller, isolering, resursprofiler, konfiguration, stateless/stateful, portabilitet och relationen mellan applikation och plattform. Bygg, test och release hör primärt till programvaruutveckling och leverans. Observerbarhet, backup, recovery och operativ motståndskraft hör primärt till driftbarhet och motståndskraft.

## Workloaden är utgångspunkten

En runtimeplattform bör inte väljas därför att organisationen råkar ha en viss produkt. Den bör väljas därför att workloadens egenskaper gör den lämplig.

Det är samma grundprincip som tidigare: behov före teknik.

För runtime innebär det att lösningen först behöver förstå sådant som:

- Är workloaden långlivad eller kortlivad?
- Är den stateless eller behöver den lokalt tillstånd?
- Behöver den särskilda operativsystemsfunktioner?
- Kräver den en viss språk- eller applikationsruntime?
- Vilka CPU- och minnesprofiler har den?
- Behöver den horisontell eller vertikal skalning?
- Hur snabbt behöver nya instanser kunna startas?
- Kan en instans ersättas utan att data eller arbete går förlorat?
- Finns native-bibliotek eller andra hårda teknikberoenden?
- Behövs GPU eller annan specialiserad hårdvara?
- Vilka säkerhets- och isoleringskrav finns?
- Vilken livslängd har applikationen och dess tekniska beroenden?

När dessa frågor är besvarade kan man börja bedöma vilken exekveringsmodell som passar bäst.

Om organisationen börjar i produktnamnet riskerar tekniska egenskaper att omvandlas till falska behov.

Exempel:

> ”Applikationen måste köras på containerplattformen.”

är inte samma sak som:

> ”Applikationen behöver horisontell skalning, automatiserad ersättning av instanser, standardiserad nätverksanslutning och en driftsättningsmodell där instanser kan startas och stoppas utan lokal dataförlust.”

Den andra formuleringen går att pröva mot flera möjliga realiseringar och överlever sannolikt längre än den första.

## Runtime är ett kontrakt mellan applikation och plattform

En gemensam runtime bör betraktas som ett tjänsteerbjudande med ett tydligt kontrakt mellan konsument och plattformsansvarig.

Konsumenten behöver veta vad plattformen erbjuder och vilka antaganden applikationen får göra. Plattformen behöver i sin tur kunna ställa krav på workloaden för att automatisering och standardisering ska fungera.

Ett sådant kontrakt kan omfatta exempelvis:

- hur applikationen paketeras,
- vilka runtimeversioner som stöds,
- hur resurser deklareras,
- hur konfiguration tillförs,
- hur secrets tillförs,
- hur health checks fungerar,
- hur applikationen ska reagera på nedstängning,
- hur nätverksanslutning erhålls,
- hur persistent data ska hanteras,
- vilka miljöer och säkerhetszoner som finns,
- hur patchning och runtimeuppgraderingar sker,
- vilket ansvar konsumenten har för kompatibilitet.

Det är här runtimeförmågan börjar bli mer än infrastruktur. Den skapar ett standardiserat sätt för utvecklingsområden att konsumera exekvering.

En bra runtimetjänst gör mycket av den underliggande infrastrukturen ointressant för applikationsteamet. Teamet behöver inte känna till varje nod, operativsystemspatch eller intern nätverksdetalj. Men abstraktionen får inte bli så opak att viktiga kvalitets- och kostnadsegenskaper försvinner.

## Containers är ett exekveringssätt – inte en arkitekturprincip

Containerisering har blivit en vanlig form för att paketera och köra applikationer. Den ger ofta goda förutsättningar för standardiserad distribution, isolering och portabilitet mellan kompatibla miljöer.[K1]

Men ”allt ska köras i containers” är sällan en bra generell arkitekturprincip.

Containers passar särskilt väl när workloaden:

- kan paketeras med tydliga beroenden,
- inte kräver omfattande direkt kontroll över värdoperativsystemet,
- kan startas och ersättas automatiskt,
- kan uttrycka resursbehov deklarativt,
- kan hantera att instanser är förgängliga,
- vinner på horisontell skalning eller standardiserad driftsättning.

De passar sämre när applikationen har hårda beroenden till ett visst operativsystem, kräver specialdrivrutiner, är starkt bunden till lokal maskinstate eller är en äldre produkt där containerisering skulle skapa mer risk än nytta.

Det viktiga är därför inte containerformatet i sig utan vilka egenskaper det möjliggör och vilka krav det ställer på applikationen.

## Virtuella maskiner är inte automatiskt ett misslyckande

När containerplattformar etableras uppstår ibland en förenklad bild där virtuella maskiner betraktas som något som alltid bör avvecklas.

Det är en dålig utgångspunkt.

En virtuell maskin kan vara rätt exekveringsmodell när workloaden exempelvis:

- kräver full kontroll över operativsystemsmiljön,
- använder programvara som inte stöds i containerform,
- har native-komponenter eller drivrutinsberoenden,
- behöver en tydlig maskinlik isoleringsgräns,
- är en äldre applikation där modernisering inte är motiverad ännu.

Problemet är inte att virtuella maskiner existerar. Problemet uppstår när varje VM blir ett unikt husdjur med egen handpåläggning, oklar patchnivå och avvikande driftmodell.

Även VM-baserad runtime kan standardiseras genom:

- godkända operativsystemsprofiler,
- automatiserad provisionering,
- gemensam konfigurationshantering,
- standardiserad patchning,
- definierade nät- och säkerhetsprofiler,
- tydlig livscykel och avveckling.

En organisation kan därför ha flera runtimeerbjudanden utan att ge upp standardisering.

## Språk- och applikationsruntime som separat lager

Mellan applikationskoden och den underliggande exekveringsmiljön finns ofta ytterligare en runtime: exempelvis en JVM, en managed runtime eller en applikationsserver.

Det skapar ytterligare en livscykel att hantera.

En Java-applikation kan exempelvis bero på:

```text
Applikationskod
      ↓
Ramverk / bibliotek
      ↓
Java-runtime / applikationsserver
      ↓
Container eller VM
      ↓
Operativsystem / infrastruktur
```

Varje lager kan ha egen supportperiod, säkerhetsuppdatering och kompatibilitetsgräns.

Det gör det viktigt att skilja mellan:

- vilket språk eller vilken runtime applikationen behöver,
- vilken version organisationen stödjer,
- vem som ansvarar för uppgradering,
- hur länge äldre versioner får finnas,
- hur beroendet påverkar portabilitet och framtida förändring.

En gemensam runtimeförmåga kan därför erbjuda standardiserade profiler, exempelvis en förvaltad Java-runtime, utan att varje applikation behöver bygga och förvalta hela kedjan själv.

Det innebär inte centralstyrning av programmeringsspråk, men en brett använd runtime behöver en synlig gemensam livscykel.

## Stateless och förgängliga instanser

Stateless är ett användbart designideal för många backend-tjänster eftersom en instans utan unik persistent verksamhetsdata är enklare att ersätta, skala och återstarta.

Förenklat:

```text
Begäran
   ↓
Valfri tjänsteinstans
   ↓
Gemensam persistent datatjänst
```

En tjänst kan samtidigt ha temporärt tillstånd i minne, cache eller tekniska buffertar. Det avgörande är om en viss instans bär unik information som måste bevaras för att verksamheten ska fungera. Stateful workloads som databaser och vissa kökomponenter är därför fullt legitima; deras tillstånd behöver bara behandlas som en medveten del av arkitekturen.

I en automatiserad runtimeplattform måste applikationen dessutom kunna leva med att instanser försvinner vid exempelvis plattformsuppgradering, autoskalning, driftsättning eller maskinvarufel. En långlivad tjänst bör därför kunna signalera readiness och hälsa, hantera kontrollerad nedstängning och starta om utan manuell rekonstruktion av lokalt tillstånd.[K2]

Arkitekturfrågorna blir då:

- Vilket tillstånd finns och var är det auktoritativt?
- Vad får vara lokalt och förgängligt?
- Hur bevaras pågående arbete när en instans ersätts?
- Hur påverkar tillståndet skalning och återställning?
- Vilket ansvar ligger på runtimeplattformen respektive datatjänsten?

För vanliga verksamhetstjänster är en bra grundregel att persistent verksamhetsdata inte ska ligga på en lokal ephemeral disk som försvinner med instansen.

## Resurser och skalning ska uttryckas som behov

CPU, minne, lagring och specialiserad hårdvara är begränsade resurser. Workloads behöver därför beskriva resursprofil och belastningsmönster i stället för att bara begära stora marginaler ”för säkerhets skull”. För stora reservationer ger låg nyttjandegrad; för små skapar instabilitet och oförutsägbara svarstider.

Runtimeförmågan behöver stödja en återkopplingsloop:

```text
Initial uppskattning
      ↓
Resursprofil
      ↓
Produktion
      ↓
Mätning
      ↓
Justering
```

Skalningsmodellen är en del av samma fråga. Vertikal skalning ger en instans mer CPU eller minne. Horisontell skalning fördelar arbetet över flera instanser och fungerar bäst när workloaden kan parallelliseras utan konflikt.

Horisontell skalning kräver därför svar på frågor som:

- Kan flera instanser arbeta samtidigt utan konflikt?
- Finns sessionsstate som måste delas?
- Hur fördelas trafik eller jobb?
- Hur hanteras samtidighet mot databasen?
- Finns externa beroenden som inte skalar lika snabbt?

Autoskalning är alltså inte ett substitut för kapacitetsdesign. Plattformen tillhandahåller mekanismer för resursallokering och skalning, medan observerbarhet ger underlag för att justera profilen utifrån verkligt beteende.

## Isolering är flerdimensionell

När flera workloads delar samma plattform uppstår frågan om isolering.

Isolering kan behövas på flera nivåer:

- process,
- container,
- virtuell maskin,
- nod eller fysisk värd,
- nätverk,
- identitet,
- resurser,
- administrativt ansvar.

Olika workloads kan kräva olika nivåer beroende på risk, informationsklassning, tekniska beroenden och störningskänslighet.

Det betyder att ”delad plattform” inte behöver betyda ”allt delar allt”. En gemensam plattform kan erbjuda olika profiler eller zoner med olika isoleringsgrad.

Isoleringskravet bör uttryckas som en konsekvens av risk och kvalitetsbehov, inte som ett direkt krav på ett visst tekniskt lager. Två workloads kan exempelvis få tillräcklig separation genom identitet, nätverkspolicy och resursgränser, medan en annan behöver egen nodpool eller separat miljö därför att konsekvensen av störning eller administrativ åtkomst är större.

Varje extra isoleringsnivå har samtidigt en kostnad. Separata kluster, noder eller maskiner kan förbättra separationen men minska resurseffektiviteten och öka driftbördan. Beslutet behöver därför baseras på avvägningar snarare än på generella slogans.

## Konfiguration ska skiljas från artefakten

En central princip för modern runtime är att applikationsartefakten och den miljöspecifika konfigurationen ska kunna förändras oberoende.

Samma byggda artefakt bör så långt möjligt kunna användas genom flera miljöer:

```text
Samma artefakt
    ├─ utveckling + utvecklingskonfiguration
    ├─ test + testkonfiguration
    └─ produktion + produktionskonfiguration
```

Detta minskar risken att en ny binär byggs bara för att ett endpointnamn eller en runtimeparameter skiljer sig.

Secrets ska samtidigt inte blandas ihop med vanlig konfiguration. Lösenord, nycklar, tokens och certifikatmaterial behöver hanteras genom de mekanismer som etablerats inom förmågan Identitet och tillit.

Runtimeplattformen kan stå för injicering och teknisk distribution, men den bör inte bli ursprunglig ägare till identitets- eller behörighetsinformationen.

## Runtime och applikation behöver separata livscykler

En av de viktigaste egenskaperna i en förvaltbar runtimearkitektur är att applikationen inte binds onödigt hårt till plattformens interna implementation.

Plattformsteamet behöver kunna:

- patcha operativsystem,
- uppgradera orkestreringslager,
- byta underliggande noder,
- förnya basimages eller runtimekomponenter,
- förändra intern infrastruktur.

Applikationsteamet behöver samtidigt kunna:

- releasa applikationskod,
- uppgradera egna bibliotek,
- ändra resursbehov,
- justera konfiguration,
- migrera mellan stödda runtime-profiler.

Om varje plattformsuppgradering kräver omfattande kodändring i alla applikationer blir den gemensamma plattformen en källa till systemisk förändringsrisk.

Omvänt kan plattformsteamet inte lova full kompatibilitet med alla historiska applikationsberoenden för all framtid.

Det behövs därför ett kontrakt med:

- supportperioder,
- kompatibilitetsprofiler,
- deprecation,
- migreringsvägar,
- ansvar för uppgradering.

Detta blir särskilt viktigt när organisationen har hundratals applikationer och flera generationer av teknik.

## Portabilitet betyder inte identisk körning överallt

Portabilitet används ofta som argument för containers eller andra abstraherande tekniker. Begreppet behöver dock nyanseras.

En applikation kan vara portabel på en nivå men fortfarande bero på omgivande plattformstjänster.

En containerimage kan exempelvis gå att starta i flera miljöer men applikationen kan samtidigt vara beroende av:

- en viss identitetsmodell,
- specifik logg- och metrikhantering,
- en viss typ av persistent lagring,
- interna nätverkstjänster,
- särskilda secretsmekanismer,
- leverantörsspecifika managed services.

Portabilitet är därför bättre att analysera som en uppsättning beroenden än som en binär egenskap.

Frågan bör vara:

> Vilka delar av lösningen är portabla, vilka är medvetet plattformsbundna och vad kostar ett framtida byte?

Det är ofta fullt rimligt att acceptera ett plattformsberoende om nyttan är stor och beroendet är synligt. Problemet uppstår när beroendet upptäcks först när en migrering blir nödvändig.

## Legacykrav är begränsningar – inte framtida standarder

Äldre applikationer kan kräva:

- utgångna operativsystem,
- specifika applikationsservrar,
- äldre runtimeversioner,
- native-bibliotek,
- statiska servernamn,
- lokalt filsystem,
- särskilda installationsmodeller.

Dessa krav behöver hanteras som faktiska begränsningar så länge applikationen finns kvar.

Men de bör inte utan vidare omvandlas till generella plattformsprinciper.

Om en äldre applikation kräver en viss VM-konfiguration är slutsatsen inte att alla nya applikationer bör använda samma konfiguration. I stället bör organisationen dokumentera:

- vilket beroende som finns,
- varför det finns,
- vilken risk det skapar,
- hur länge det behöver stödjas,
- vilken avvecklings- eller moderniseringsplan som finns.

På så sätt undviker man att teknisk skuld institutionaliseras som standard.

## Batch och schemalagda workloads behöver egen behandling

All exekvering är inte en långlivad webbtjänst.

Batchjobb och schemalagda workloads har andra egenskaper:

- de startar vid en viss tid eller händelse,
- de kan behandla stora datamängder,
- de behöver ofta tydlig exitstatus,
- återförsök kan vara relevant på jobbnivå,
- parallellisering kan vara viktig,
- missade körningar kan ha verksamhetskonsekvenser,
- ett jobb kan behöva återupptas från checkpoint.

Runtimeplattformen bör därför kunna uttrycka dessa workloads som förstaklassobjekt i stället för att tvinga dem att imitera en permanent tjänst.

Samtidigt behöver processansvaret vara tydligt. Om ett batchjobb är ett steg i en verksamhetsprocess hör processens tillstånd och verksamhetsmässiga återupptagning hemma i process- eller domänlagret. Runtimeplattformen ansvarar för att exekvera jobbet, inte för att förstå dess verksamhetsbetydelse.

## Serverless och funktionsliknande exekvering

En del plattformar erbjuder exekveringsformer där konsumenten i ännu högre grad abstraheras från underliggande runtime. En funktion eller kortlivad workload startas på begäran och plattformen hanterar mer av kapacitet, instansiering och skalning.

Det kan vara attraktivt för:

- händelsedrivna små workloads,
- sporadisk exekvering,
- kortlivad bearbetning,
- funktioner där snabb leverans är viktigare än kontroll över runtime.

Men samma modell kan skapa nya begränsningar kring:

- exekveringstid,
- startup-latens,
- tillstånd,
- felsökning,
- lokala beroenden,
- portabilitet,
- kostnadsprofil.

Serverless bör därför behandlas som ännu en möjlig runtime-profil, inte som ett mål i sig.

## Specialiserad hårdvara förändrar plattformskontraktet

AI, avancerad analys, bildbehandling och vissa beräkningsintensiva workloads kan behöva GPU eller annan accelerator.

Det gör resursmodellen mer komplex eftersom sådan hårdvara ofta är:

- dyr,
- begränsad,
- beroende av särskilda drivrutiner,
- kopplad till specifika runtimeversioner,
- svårare att dela effektivt.

Ett gemensamt erbjudande behöver därför göra dessa beroenden explicita. Konsumenten bör uttrycka behov i termer av beräkningsprofil och kvalitetskrav snarare än att själv välja fysisk maskin eller intern infrastruktur.

Plattformen bör alltså abstrahera onödig infrastruktur utan att dölja egenskaper som påverkar arkitekturen.

## Runtimeplattformen ska inte bli en ny monolit

När en containerplattform eller annan exekveringsplattform blir central finns en risk att organisationen börjar placera allt möjligt ansvar där.

Plattformen får då ansvar för:

- identitet,
- integration,
- databaser,
- CI/CD,
- observerbarhet,
- verksamhetsregler,
- driftsättning,
- säkerhet,
- nätverk,
- backup.

Tekniskt kan flera av dessa mekanismer vara integrerade med runtime-plattformen. Arkitekturellt behöver ansvaret ändå hållas isär.

Exempelvis kan runtime-plattformen injicera en secret, men identitetsförmågan äger principerna för hur secreten skapas och roteras. Plattformen kan exponera mätvärden, men driftbarhetsförmågan äger modellen för observerbarhet och operativ uppföljning.

Detta följer bokens metamodell: en fysisk eller teknisk produkt kan realisera flera förmågor utan att förmågorna behöver slås ihop begreppsligt.

## Ett gemensamt runtimeerbjudande behöver profiler

I en större organisation är det ofta bättre att erbjuda ett begränsat antal tydliga runtime-profiler än en enda universell miljö eller helt fria teknikval.

Exempelvis kan katalogen innehålla:

- *Container Application Platform* för containeriserade workloads,
- *Java Application Runtime* för förvaltad Java-exekvering,
- Virtual Machine Runtime för workloads som behöver fullare operativsystemsmiljö,
- särskilda batch- eller funktionsprofiler när behovet motiverar det.

Varje erbjudande bör beskriva:

- vilka behov det är avsett för,
- vilka kvalitetsnivåer som stöds,
- vilka tekniska begränsningar som finns,
- vilket ansvar konsumenten har,
- vilket ansvar plattformen har,
- vilka standarder som gäller,
- hur livscykel och support fungerar.

Profilerna bör dessutom ha tydliga valkriterier. Om två erbjudanden kan köra samma typ av applikation behöver läsaren kunna förstå varför det ena är förstahandsval och vilka egenskaper som motiverar det andra. Annars flyttas bara produktvalet från teamet till en otydlig plattformskatalog.

Detta gör valet mer meningsfullt än ett rent produktval och knyter runtimeerbjudandet tillbaka till workloadens faktiska behov.

## Ansvar på tre nivåer

Runtimefrågorna följer samma ansvarmodell som övriga förmågor, men med olika fokus:

- **Gemensam arkitekturnivå** sätter principer för produktberoenden, kvalitetskrav, livscykel och gränser mot identitet, integration, data och driftbarhet.
- **Förmågenivån** utvecklar runtimeerbjudanden, konsumentkontrakt, standardprofiler, supportfönster, migreringsvägar och golden paths samt följer upp kapacitet, kostnad och användning.
- **Lösnings-/produktnivån** beskriver workloadens egenskaper, väljer lämplig profil, anger resursbehov och uppfyller kontrakt för exempelvis health checks, graceful shutdown, konfiguration och kompatibilitet.

Det gör det möjligt att standardisera exekveringen utan att göra plattformsteamet ansvarigt för applikationernas verksamhetsarkitektur.

## Vanliga anti-patterns

Några återkommande problem är särskilt värda att känna igen.

### Produktnamnet blir behovet

”Alla Java-applikationer ska köras på produkt X.”

Det kan vara en produktstandard, men det är inte en bra formulering av själva runtimebehovet. När produktstandarden senare ändras riskerar arkitekturen att vara full av gamla produktantaganden.

### En runtime för allt

En enda plattform försöker lösa både moderna stateless tjänster, legacyprodukter, batch, databaser och specialiserade workloads. Resultatet blir ofta många undantag och en alltmer komplex plattform.

### Varje team bygger sin egen runtime

Motsatsen är att varje team själv installerar operativsystem, runtime, reverse proxy, certifikathantering och övervakning. Det ger lokal frihet men multiplicerar drift- och livscykelansvaret.

### Lokal disk behandlas som permanent data

Applikationen fungerar så länge samma instans lever men tappar information när den flyttas eller ersätts.

### Plattformen döljer alla kostnader

Om teamen inte ser resursförbrukning finns få incitament att dimensionera rimligt. En självserviceplattform behöver därför kombinera enkel konsumtion med synlighet i faktisk resursanvändning.

### Uppgraderingar skjuts på framtiden

En applikation binds till en gammal runtimeversion utan definierad avvecklingsplan. När säkerhets- eller supportläget tvingar fram en uppgradering blir förändringen akut och dyr.

## En praktisk analysordning

När en ny workload ska placeras i en runtime kan följande ordning användas:

1. Beskriv workloaden. Är den långlivad, batch, händelsedriven eller specialiserad?
2. Identifiera tillstånd. Vilket tillstånd finns och var behöver det bevaras?
3. Beskriv resursprofilen. CPU, minne, lagring, GPU och belastningsmönster.
4. Identifiera tekniska begränsningar. Runtimeversion, native-bibliotek, OS-beroenden och särskild hårdvara.
5. Härled kvalitetskraven. Tillgänglighet, skalning, återstartstid, isolering och livscykel.
6. Pröva mot gemensamma runtimeerbjudanden. Välj det enklaste erbjudande som uppfyller behoven.
7. Dokumentera avvikelser. Om inget erbjudande passar ska gapet beskrivas som behov, inte omedelbart som ett nytt produktkrav.
8. Definiera konsumentansvaret. Health, shutdown, konfiguration, resurser och kompatibilitet.
9. Planera livscykeln. Hur uppgraderas både applikation och runtime över tid?
10. Mät i verklig drift. Justera resursprofil och plattformsval utifrån observerat beteende.

Arbetssättet gör runtimevalet till ett arkitekturbeslut som kan motiveras, följas upp och omprövas.

## Från exekvering till driftbarhet

Runtimeförmågan svarar på frågan var och under vilka tekniska villkor en workload körs.

Men att en applikation går att starta innebär inte att den går att drifta väl.

Organisationen behöver också kunna svara på:

- Hur vet vi att tjänsten fungerar?
- Hur upptäcker vi degradering?
- Hur följer vi en transaktion genom flera tjänster?
- Hur återställer vi efter fel?
- Hur verifierar vi backup?
- Hur arbetar vi med SLO och operativ återkoppling?
- Hur designar vi för att fel faktiskt kommer att inträffa?

Det är nästa förmåga.

Därefter flyttas fokus från exekveringsmiljön till förmågan att förstå, återställa och hålla systemen fungerande över tid.

## Källor och vidare läsning

**[K1]** Open Container Initiative, *OCI Image Specification* och *OCI Runtime Specification*. https://specs.opencontainers.org/image-spec/ och https://github.com/opencontainers/runtime-spec

**[K2]** Kubernetes, *Liveness, Readiness, and Startup Probes*. https://kubernetes.io/docs/concepts/workloads/pods/probes/
