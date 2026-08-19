# 20. Driftbarhet och motståndskraft

Ett system kan vara korrekt byggt, korrekt driftsatt och ändå vara svårt att hålla fungerande över tid. Det kan sakna tillräcklig telemetri för att förstå vad som händer, ha larm som ingen kan agera på, innehålla beroenden som gör att små fel sprider sig eller ha säkerhetskopior som aldrig har provats i en verklig återställning.

Driftbarhet och motståndskraft handlar därför inte bara om att ”ha övervakning” eller ”ta backup”. Förmågan handlar om att göra system **begripliga under drift, möjliga att återställa och konstruerade så att fel kan hanteras utan att konsekvenserna blir större än nödvändigt**.

Kärnfrågan i kapitlet är:

> **Hur skapar en organisation gemensamma mekanismer för att förstå, upptäcka, begränsa och återhämta sig från fel – på en nivå som motsvarar verksamhetens faktiska behov?**

Kapitel 4 beskrev hur tillgänglighet, kontinuitet, återställningstid och andra kvalitetskrav härleds från verksamhetskonsekvenser. Det här kapitlet tar nästa steg: vilka tekniska och operativa förmågor behövs för att realisera och verifiera sådana krav?

Runtimefrågor som exekveringsmiljö, scaling och healthmekanismer behandlades i kapitel 19. Bygg, test, release och deployment behandlas i kapitel 21. Fokus här ligger på **observability, monitorering, larm, felisolering, återhämtning, backup, restore, disaster recovery, kapacitetsuppföljning och operativ återkoppling**.

## Driftbarhet är en egenskap hos hela systemet

Driftbarhet kan inte läggas till som ett separat lager efter att lösningen är färdig.

Ett system blir driftbart genom en kombination av sådant som:

- tydliga ansvarsgränser,
- begriplig arkitektur,
- relevant telemetri,
- förutsägbara felbeteenden,
- dokumenterade beroenden,
- återställningsmekanismer,
- testade operativa procedurer,
- rimlig förändringstakt,
- och människor som kan förstå signalerna och agera på dem.

Det innebär att två system med samma observabilityplattform kan ha helt olika driftbarhet. Det ena producerar strukturerade loggar, meningsfulla metrics och korrelerade traces och har tydliga runbooks. Det andra skickar stora mängder ostrukturerad text till samma plattform utan att någon vet vilka signaler som är viktiga.

Den gemensamma plattformen kan ge verktyg och standarder. Den kan inte ensam skapa driftbarheten.

Detta är samma ansvarsmönster som återkommer genom boken: **gemensamma mekanismer reducerar återkommande tekniskt arbete, men lösningen måste fortfarande utformas så att mekanismerna kan ge värde**.

## Utgå från konsekvens – inte maximal robusthet

Det är lockande att formulera generella krav som:

> Alla system ska ha hög tillgänglighet.

> All data ska säkerhetskopieras varje timme.

> Alla tjänster ska ha full tracing.

> Alla miljöer ska ha disaster recovery i en separat region.

Sådana formuleringar verkar försiktiga, men de blandar ihop målet med en viss teknisk ambitionsnivå.

En liten intern stödtjänst som kan vara otillgänglig en arbetsdag har inte samma behov som ett verksamhetskritiskt system där minuter av avbrott får stora konsekvenser. Om samma högsta robusthetsnivå byggs överallt blir kostnaden hög, komplexiteten ökar och organisationen riskerar dessutom att lägga lika mycket operativ uppmärksamhet på oviktiga och kritiska signaler.

Driftbarhet behöver därför härledas från frågor som:

- Vad händer i verksamheten om tjänsten inte fungerar?
- Hur snabbt behöver felet upptäckas?
- Hur snabbt behöver tjänsten återställas?
- Hur mycket dataförlust kan accepteras?
- Vilka delar måste fortsätta fungera även om ett beroende fallerar?
- Vilka fel kan hanteras manuellt och vilka behöver automatiserad återhämtning?
- Hur snabbt behöver orsaken kunna diagnostiseras?
- Hur dyrt är det att bygga och upprätthålla den önskade robusthetsnivån?

Det leder till **kvalitetsprofiler** snarare än ett universellt maximalkrav.

En gemensam plattform kan exempelvis erbjuda flera profiler för backup, retention, redundans eller larmning. Konsumenten väljer inte profil efter tycke, utan utifrån de kvalitetsbehov som härletts tidigare.

## Observability är förmågan att förstå systemets tillstånd

Begreppet *observability* används ofta som synonym till övervakning, men det är mer användbart att skilja dem åt.

**Monitorering** handlar i första hand om att följa kända signaler och upptäcka att ett definierat villkor har inträffat.

**Observability** handlar bredare om att kunna dra slutsatser om ett systems interna beteende utifrån den telemetri systemet exponerar.

Skillnaden blir tydlig i en incident.

Monitorering kan säga:

> Felkvoten för API:t har passerat fem procent.

Observability behöver dessutom hjälpa oss svara på:

- Vilka anrop fallerar?
- När började problemet?
- Berör det alla användare eller en viss grupp?
- Finns sambandet med en release?
- Är databasen långsam eller är det ett externt beroende?
- Uppstår felet i samma del av ett distribuerat flöde?
- Är systemet tekniskt levande men verksamhetsmässigt oanvändbart?

En gemensam observabilityförmåga behöver därför mer än en central loggdatabas. Den behöver en sammanhängande modell för **loggar, metrics, traces, korrelation, dashboards, larm och åtkomst till telemetrin**.

## Loggar berättar vad som hände

Loggar är fortfarande ett centralt verktyg för drift och felsökning, men värdet beror starkt på hur de produceras.

En bra applikationslogg bör göra det möjligt att förstå en händelse utan att först tolka stora mängder fri text. Strukturerade fält gör det exempelvis möjligt att konsekvent söka och gruppera på:

- tidsstämpel,
- tjänst,
- miljö,
- händelsetyp,
- korrelationsidentifierare,
- resultat,
- felkategori,
- relevant teknisk kontext.

Det innebär inte att varje intern variabel ska loggas. Tvärtom är för mycket loggning ett problem. Det ökar kostnad och brus, kan påverka prestanda och kan sprida information som aldrig borde lämna den ursprungliga komponenten.

En viktig princip är därför:

> **Logga det som behövs för drift, felsökning och relevant spårbarhet – inte allt som råkar vara tekniskt möjligt att logga.**

Credentials, secrets och onödiga person- eller skyddsvärda uppgifter ska inte användas som diagnostiskt material. Retention för loggar behöver också styras medvetet. ”Spara allt för säkerhets skull” är sällan en hållbar informationsstrategi.

## Metrics visar beteende över tid

Loggar beskriver enskilda händelser. Metrics gör det lättare att se mönster och förändring över tid.

Exempel på tekniska metrics är:

- svarstid,
- felkvot,
- antal anrop,
- ködjup,
- CPU- och minnesanvändning,
- antal aktiva anslutningar,
- antal lyckade eller misslyckade bakgrundsjobb.

Men endast tekniska resursmått är inte alltid tillräckliga.

Ett system kan ha låg CPU-belastning och samtidigt vara helt oanvändbart för verksamheten. Därför behöver lösningen ibland även **verksamhetsnära operativa signaler**, exempelvis:

- antal ärenden som fastnat i ett visst steg,
- ålder på äldsta obehandlade meddelande,
- antal genomförda kritiska transaktioner,
- andel misslyckade dokumentleveranser,
- tid från inkommen händelse till slutförd behandling.

Dessa signaler ska inte förväxlas med full verksamhetsanalys. Syftet är att förstå om den tekniska tjänsten faktiskt levererar den funktion som behöver hållas i drift.

## Tracing knyter ihop distribuerade flöden

När ett användarflöde passerar flera tjänster, gateways, databaser och meddelandekanaler blir lokala loggar snabbt otillräckliga.

Distributed tracing kan då göra det möjligt att följa ett sammanhängande flöde över flera komponenter.

Det viktiga är inte att alla system alltid måste ha full tracing. Det viktiga är att organisationen har en gemensam mekanism när behovet finns.

Ett typiskt distribuerat flöde kan exempelvis vara:

```text
Klient
  ↓
API-gateway
  ↓
Tjänst A
  ↓
Tjänst B
  ↓
Meddelandekö
  ↓
Tjänst C
```

Om varje komponent bara har sin egen lokala tidsstämpel och sin egen interna identifierare blir incidentanalysen manuellt detektivarbete.

Med gemensam korrelation kan samma logiska transaktion följas genom kedjan.

Detta är särskilt viktigt i integrationsintensiva miljöer. Samtidigt behöver korrelationsinformation designas så att den inte i sig blir en bärare av känslig information.

## Teknisk hälsa är inte samma sak som fungerande tjänst

Ett av de vanligaste misstagen i driftövervakning är att kontrollera att processen lever och sedan anta att tjänsten fungerar.

Det finns flera nivåer av hälsa:

1. **Processhälsa** – processen eller containern kör.
2. **Instanshälsa** – instansen kan ta emot relevant arbete.
3. **Beroendehälsa** – nödvändiga beroenden fungerar tillräckligt väl.
4. **Tjänstehälsa** – den externa tjänsten levererar sitt kontrakt.
5. **Verksamhetsmässig funktion** – det viktiga användar- eller verksamhetsflödet fungerar.

Dessa nivåer ska inte alltid kopplas ihop mekaniskt.

Om en health check exempelvis gör instansen ”ohälsosam” bara för att ett externt beroende är tillfälligt nere kan runtimeplattformen börja starta om fullt fungerande instanser i onödan. Resultatet kan bli större störning än det ursprungliga felet.

Health checks behöver därför ha ett tydligt syfte. En signal som används för automatisk omstart har en annan konsekvens än en signal som används för en dashboard.

Automatisering gör felhantering snabbare – men den förstorar också konsekvensen av en felaktig signal.

## SLI, SLO och SLA fyller olika funktioner

För att driva en tjänst behöver man kunna mäta den egenskap som är viktig.

En **Service Level Indicator, SLI**, är ett mätetal som representerar en relevant aspekt av tjänstens beteende. Det kan exempelvis vara andelen lyckade anrop eller svarstid för ett definierat flöde.

Ett **Service Level Objective, SLO**, uttrycker den önskade nivån för indikatorn under en viss period.

Ett **Service Level Agreement, SLA**, är däremot ett avtal eller en överenskommelse där servicenivåer kan vara kopplade till formella åtaganden och konsekvenser.

Det är därför olämpligt att använda orden som synonymer.

För den gemensamma arkitekturen är framför allt kopplingen viktig:

```text
Verksamhetskonsekvens
        ↓
Kvalitetskrav
        ↓
Mätbar indikator
        ↓
Målnivå
        ↓
Observability och operativ uppföljning
```

SLO bör inte börja i frågan ”vilka metrics kan vår plattform mäta?”. De bör börja i vilket tjänstebeteende som faktiskt är viktigt.

## Larm ska leda till handling

Det är enkelt att skapa larm. Det är svårare att skapa bra larm.

Ett larm är värdefullt när det signalerar ett tillstånd där någon behöver göra något eller där en automatiserad åtgärd behöver initieras.

Ett bra produktionslarm bör därför så långt som möjligt ha:

- ett definierat felvillkor,
- känd betydelse,
- tydligt ansvar,
- en möjlig nästa åtgärd,
- rimlig prioritet,
- tillräcklig kontext för första analysen.

Om ett larm återkommande ignoreras finns i grunden tre möjligheter:

1. tröskeln är fel,
2. signalen är inte åtgärdsbar,
3. organisationen saknar mandat eller kapacitet att agera.

Att lägga ytterligare larm ovanpå problemet förbättrar inte driftbarheten.

**Larmtrötthet** är därför inte bara ett användargränssnittsproblem. Det är ett tecken på att organisationens operativa signalmodell behöver förbättras.

## Dashboards är hypoteser om vad som är viktigt

Dashboards blir lätt stora samlingar av grafer därför att telemetrin finns tillgänglig.

En bättre utgångspunkt är att varje vy ska svara på en fråga.

Exempel:

- Fungerar tjänsten för användarna just nu?
- Är ett beroende på väg att bli en flaskhals?
- Har en ny release förändrat felkvoten?
- Klarar vi beslutad servicenivå?
- Växer kön snabbare än vi kan behandla den?
- Har återkommande incidenter samma tekniska signatur?

Det innebär ofta att olika målgrupper behöver olika vyer. Ett plattformsteam, ett applikationsteam och en tjänsteägare behöver inte samma dashboard.

En gemensam observabilityplattform bör göra data tillgänglig och standardiserad. Den bör inte anta att samma dashboard kan representera alla tjänsters verkliga hälsa.

## Motståndskraft börjar med att fel förväntas

Motståndskraft, eller resilience, handlar inte om att skapa system där inget någonsin går sönder.

Det handlar om att utforma system så att fel:

- upptäcks,
- begränsas,
- hanteras,
- återhämtas från,
- och ger lärande inför nästa händelse.

Det kräver en annan tankemodell än att betrakta fel som exceptionella undantag.

I ett distribuerat system kommer exempelvis nätverksfördröjning, tillfälligt otillgängliga beroenden, överbelastning, processkrascher och misslyckade deploymenter förr eller senare att inträffa.

Arkitekturen behöver därför fråga:

> Vad händer när detta beroende inte svarar?

inte bara:

> Hur anropar vi beroendet när allt fungerar?

## Felisolering begränsar konsekvensytan

Ett litet fel blir allvarligt när det får sprida sig genom hela lösningen.

Felisolering kan skapas på flera sätt:

- tydliga tidsgränser för externa anrop,
- separata resurspooler,
- begränsade köer,
- isolerade exekveringsmiljöer,
- kontroll över samtidighet,
- bulkheads mellan kritiska och mindre kritiska flöden,
- separerade fel- och hotdomäner,
- avgränsade data- och nätverkszoner.

Målet är inte maximal uppdelning. Varje isoleringsgräns har kostnad och komplexitet.

Frågan är i stället vilka beroenden som kan orsaka oproportionerligt stora konsekvenser om de fallerar.

Det är nära kopplat till diskussionen om coupling i kapitel 10. Ett system kan vara logiskt modulärt men fortfarande operativt starkt kopplat om alla delar fallerar tillsammans.

## Timeout är en arkitekturell gräns

Ett synkront anrop utan rimlig timeout är i praktiken ett antagande om att motparten alltid svarar.

Det är sällan ett säkert antagande.

Timeouts begränsar hur länge en komponent väntar på ett beroende och skyddar därmed resurser som trådar, anslutningar och kökapacitet.

Men timeoutvärdet kan inte väljas isolerat.

Om tjänst A anropar B som anropar C behöver tidsbudgeten förstås över hela kedjan. Annars kan den yttre klienten ge upp medan interna tjänster fortsätter arbeta med ett resultat som ingen längre väntar på.

Det gör timeout till mer än en lokal konfigurationsparameter. I kritiska flöden är den en del av lösningens fel- och latensmodell.

## Retry kan både hjälpa och skada

Automatiska retries kan hantera kortvariga fel mycket effektivt.

De kan också förstärka en incident.

Om tusentals klienter omedelbart skickar om misslyckade anrop mot en redan överbelastad tjänst kan retrylogiken skapa en återkopplingsloop som gör problemet större.

Retry behöver därför analyseras tillsammans med:

- idempotens,
- timeout,
- backoff,
- jitter,
- maximal försöksmängd,
- kapacitet hos mottagaren,
- feltyp.

Ett permanent valideringsfel ska normalt inte försöka skickas om på samma sätt som ett tillfälligt nätverksfel.

Detta knyter an till kapitel 17: leveranssemantik och kommunikationsmönster är en del av motståndskraften, men driftbarhetsförmågan behöver ge mekanismer för att **se när retries sker, när de misslyckas och när de skapar belastning**.

## Automatisk återhämtning är värdefull när beteendet är säkert

Automatisk restart, failover och annan självläkning kan kraftigt minska återställningstid.

Men automation bör användas där organisationen förstår konsekvensen.

En stateless instans som inte längre svarar kan ofta ersättas säkert.

En datakomponent med oklar replikeringsstatus kan kräva betydligt försiktigare beslut innan automatisk failover sker.

Principen är därför inte ”automatisera all recovery”, utan:

> **Automatisera återkommande återhämtning när tillståndet kan identifieras pålitligt och åtgärden har förutsägbara konsekvenser.**

Automation ska dessutom vara observerbar. Om en plattform återstartar samma instans hundra gånger utan att någon reagerar har den inte löst problemet; den har bara dolt symptomet.

## Backup är inte samma sak som återställningsförmåga

En lyckad backupkörning bevisar bara att en mekanism har producerat något som bedöms vara en säkerhetskopia.

Den bevisar inte att:

- rätt data ingår,
- datat är konsistent,
- nödvändig konfiguration finns med,
- credentials och nycklar kan återetableras,
- kopian kan läsas,
- återställningen ryms inom önskad tid,
- den återställda tjänsten faktiskt fungerar.

Därför är **verifierad restore** den viktigare förmågan.

En återställningsstrategi behöver börja med att identifiera vad som faktiskt måste kunna återskapas. Det kan omfatta mer än databasen:

- verksamhetsdata,
- objekt och dokument,
- konfiguration,
- infrastrukturbeskrivningar,
- nödvändiga nyckelmaterial,
- externa beroendekonfigurationer,
- metadata som krävs för att tolka datat.

Detta behöver samordnas med dataförmågan i kapitel 15. Informationsägaren avgör vad som behöver skyddas och hur länge. Driftbarhetsförmågan tillhandahåller mekanismerna för backup och återställning.

## Replikering och backup löser olika fel

Replikering kan ge hög tillgänglighet och minska effekten av att en enskild nod eller lagringskomponent fallerar.

Men en replika kan också snabbt kopiera samma problem:

- oavsiktlig radering,
- applikationsfel,
- datakorruption,
- felaktig migrering,
- skadlig förändring.

Därför är replikering inte automatiskt en ersättning för backup.

På motsvarande sätt är backup inte en ersättning för hög tillgänglighet. Om det tar flera timmar att återställa en säkerhetskopia löser den inte ett behov där tjänsten bara får vara nere några minuter.

Det är två olika mekanismer som svarar på olika felbilder.

## RPO och RTO behöver kopplas till verklig recovery

Kapitel 4 introducerade **Recovery Point Objective, RPO**, och **Recovery Time Objective, RTO** som sätt att uttrycka återställningsbehov.

I driftbarhetsförmågan blir frågan om den tekniska lösningen faktiskt kan möta dem.

Ett RPO på exempelvis femton minuter kan påverka:

- backupfrekvens,
- loggning eller journaling,
- replikering,
- point-in-time recovery,
- lagringsarkitektur.

Ett RTO på trettio minuter kan påverka:

- hur snabbt infrastruktur kan provisioneras,
- hur konfiguration återskapas,
- automatiseringsgrad,
- datavolym,
- nätverks- och DNS-ändringar,
- tillgång till personal och behörigheter,
- hur recoveryproceduren är tränad.

Det sista glöms ofta bort. En tekniskt möjlig återställning på trettio minuter är inte samma sak som en organisatoriskt genomförbar återställning på trettio minuter.

## Disaster recovery är en kedja, inte en reservmiljö

Disaster recovery, DR, reduceras ibland till frågan om organisationen har en sekundär miljö.

Det är otillräckligt.

En fungerande DR-förmåga behöver förstå hela kedjan:

```text
Störning
  ↓
Beslut om DR
  ↓
Aktivering av alternativ miljö
  ↓
Återställning av data och konfiguration
  ↓
Återetablering av integrationer och identiteter
  ↓
Verifiering
  ↓
Trafikomläggning
  ↓
Operativ stabilisering
```

Varje steg kan innehålla beroenden som blir den verkliga flaskhalsen.

Det hjälper exempelvis inte att databasen kan återställas snabbt om:

- certifikat saknas,
- DNS-ändringen kräver manuell handläggning,
- externa parter bara accepterar trafik från den primära miljön,
- secrets inte finns i recoverymiljön,
- integrationsköer inte kan återskapas,
- ingen har mandat att initiera växlingen.

DR är därför både arkitektur och operativ förmåga.

## En recoveryplan som aldrig övas är en hypotes

Dokumentation är nödvändig men inte tillräcklig.

En runbook kan vara logiskt korrekt och ändå fallera när den används därför att:

- kommandon har förändrats,
- behörigheter saknas,
- en beroendetjänst har bytt adress,
- backupformatet har ändrats,
- en återställning tar betydligt längre tid än antaget,
- ett manuellt steg bara förstås av en person.

Återställning behöver därför verifieras på en nivå som motsvarar konsekvensen av misslyckande.

Det kan handla om:

- automatiserade restoretester,
- återkommande återläsning i isolerad miljö,
- komponentvisa recoveryövningar,
- fullskaliga DR-övningar,
- tabletop-övningar för besluts- och ansvarskedjan.

Alla system behöver inte samma testfrekvens eller omfattning. Återigen är det kvalitetsbehovet som styr.

## Runbooks gör kunskap operativ

En runbook beskriver hur ett känt operativt tillstånd hanteras.

En bra runbook kan exempelvis svara på:

- Hur identifieras problemet?
- Vilka kontroller ska göras först?
- Vilka åtgärder är säkra att utföra?
- Vilka åtgärder kräver särskilt mandat?
- Hur verifieras att tjänsten återhämtat sig?
- När ska problemet eskaleras?
- Vilken information ska bevaras för efteranalys?

Runbooks är särskilt värdefulla när återkommande incidenter kräver samma kedja av diagnostik och åtgärder.

Men de ska inte bli ett sätt att permanent acceptera manuellt arbete som borde automatiseras. Om samma runbook körs flera gånger i veckan är det ofta ett tecken på att en plattforms- eller produktförbättring bör prioriteras.

På så sätt blir operativt arbete en källa till arkitektoniskt lärande.

## Kapacitet är en del av driftbarheten

Kapacitetsproblem uppstår sällan exakt när en resurs når hundra procent.

De kan visa sig som:

- ökande svarstider,
- växande köer,
- fler timeouts,
- längre garbage collection-pauser,
- ökande databaslåsning,
- slut på anslutningar,
- högre kostnad per transaktion.

Kapacitetsövervakning bör därför kopplas till tjänstens faktiska beteende, inte bara till enskilda servermått.

Det är också viktigt att skilja **kapacitet** från **skalbarhet**.

Skalbarhet beskriver hur lösningen kan förändra kapaciteten när belastningen ändras. Driftbarhet behöver kunna upptäcka när kapaciteten inte längre är tillräcklig och om skalningsmekanismen faktiskt fungerar.

En autoscaler är alltså inte en ersättning för kapacitetsförståelse.

## Operativ återkoppling ska påverka arkitekturen

En av de största vinsterna med en gemensam driftbarhetsförmåga är att incidenter och driftdata kan skapa strukturerad återkoppling.

Återkommande problem kan visa att:

- ett API-kontrakt är för skört,
- en runtimeprofil är fel dimensionerad,
- ett beroende saknar timeout,
- en gemensam plattform inte erbjuder rätt recoveryprofil,
- ett system har otydliga ägargränser,
- en standard ger för mycket larmbrus,
- en manuell rutin borde automatiseras.

Den operativa återkopplingen behöver därför gå tillbaka till rätt nivå.

Ett lokalt kodfel ska inte bli en ny organisationsstandard.

Men om tjugo team har samma problem är det sannolikt inte längre ett lokalt problem.

Det är samma iterativa modell som etablerades i kapitel 7: gemensam arkitektur sätter ramar, lösningar producerar erfarenhet och erfarenheten används för att förbättra den gemensamma modellen.

## Incidenthantering och problemhantering är olika perspektiv

När en tjänst är störd är den första uppgiften normalt att återställa acceptabel funktion.

Det är incidentperspektivet.

Efteråt behöver organisationen förstå varför störningen inträffade, vilka skydd som saknades och vad som bör förändras.

Det är ett mer långsiktigt problem- och förbättringsperspektiv.

De två målen kan stå i konflikt under själva incidenten. Den snabbaste vägen tillbaka till drift är inte alltid den bästa vägen för att bevara full diagnostisk information.

Därför bör arkitekturen redan i förväg stödja båda:

- tillräcklig telemetri för efteranalys,
- säkra recoveryprocedurer,
- möjlighet att ta diagnostiska snapshots där det är relevant,
- spårbarhet mellan incident, förändring och åtgärd.

En mogen driftbarhetsförmåga bedöms alltså inte bara på hur fort larm går, utan också på om organisationen faktiskt lär sig av återkommande fel.

## Gemensamma tjänster inom förmågan

Ett stödjande IT-område kan välja att erbjuda flera gemensamma plattformstjänster inom driftbarhet och motståndskraft.

Typiska exempel är:

### Central Logging Service

Ett gemensamt erbjudande för insamling, retention, sökning och åtkomstkontroll för tekniska loggar.

Plattformen kan standardisera mekanismen. Konsumenten behöver fortfarande producera meningsfulla loggar och avgöra vilken information som får förekomma i dem.

### Metrics, Monitoring and Tracing

Ett erbjudande för metrics, dashboards, teknisk monitorering, tracing och larmfunktioner.

Plattformen kan tillhandahålla insamling och standardiserade integrationer. Konsumenten behöver definiera vilka signaler som visar den egna tjänstens hälsa.

### Backup and Recovery Service

Ett erbjudande för backup, point-in-time recovery, restore och tekniskt stöd för återställning.

Plattformen kan erbjuda profiler. Konsumenten behöver identifiera skyddsvärda data, välja rätt profil och delta i verifieringen av att hela lösningen kan återställas.

Dessa tjänster kan vara separata produkter även om de hör till samma förmåga. Det finns inget egenvärde i att samla observability, backup och DR i en enda teknisk plattform.

## Standardisering ska ske på rätt nivå

Gemensamma standarder kan skapa stor nytta inom driftbarhet eftersom många mekanismer annars implementeras olika i varje produkt.

Exempel på lämpliga standardområden är:

- strukturerad loggning,
- korrelationsmekanism,
- benämning och labels för metrics,
- health checks,
- hur traces propagateras,
- förbud mot secrets i loggar,
- backup- och restoreprofiler,
- krav på återkommande restoretest för kritiska data.

Men en standard bör inte automatiskt föreskriva samma detaljnivå för alla system.

Full distributed tracing kan vara rimligt för en komplex integrationskedja och överdrivet för en enkel intern batchtjänst. En sekundär recoverymiljö kan vara motiverad för ett kritiskt verksamhetssystem och ekonomiskt orimlig för en stödtjänst med lågt kontinuitetskrav.

Standarden bör därför ange **miniminivåer, gemensamma kontrakt och valbara kvalitetsprofiler**, snarare än att göra maximal robusthet obligatorisk överallt.

## Ansvar på tre nivåer

Driftbarhet blir särskilt tydlig när ansvarsfördelningen från kapitel 7 tillämpas.

### Gemensam arkitekturnivå

Den gemensamma nivån bör bland annat:

- definiera kvalitetsdimensioner och övergripande principer,
- ange gemensamma krav för observability och återställningsbarhet,
- definiera hur kvalitetsprofiler uttrycks,
- besluta gemensamma korrelations- och telemetrikontrakt,
- etablera principer för backup, restore och fel-/hotdomäner,
- ange när dokumenterad DR-strategi krävs,
- definiera hur avsteg och gemensamma risker hanteras.

Den gemensamma nivån ska inte välja larmtröskel för varje enskild applikation eller bestämma varje systems exakta recoveryprocedur.

### Förmågenivå

Förmågeansvaret för Driftbarhet och motståndskraft bör bland annat:

- utveckla gemensamma observabilitytjänster,
- erbjuda logging-, monitoring- och tracingmekanismer,
- erbjuda backup- och recoveryprofiler,
- ta fram standarder och golden paths,
- stödja runbooks och operativ integration,
- följa upp återkommande incidentmönster,
- utveckla mekanismer för restoretest och DR-verifiering,
- förvalta retention- och kapacitetsprofiler för telemetri,
- samla återkoppling från konsumenterna.

Förmågeansvaret bör inte bli den operativa ägaren av varje system som använder plattformen.

### Lösnings-/produktnivå

Det konkreta produktområdet behöver bland annat:

- härleda sina kvalitetskrav,
- definiera relevanta SLI:er och operativa signaler,
- producera användbar telemetri,
- definiera åtgärdsbara larm,
- kartlägga kritiska beroenden och felmoder,
- välja backup- och recoveryprofil,
- dokumentera och testa återställning,
- utforma lösningen för felisolering och säker retry,
- äga sina runbooks,
- följa upp incidenter och förbättra både produkt och gemensamma mekanismer.

Denna ansvarsfördelning gör det möjligt att standardisera verktyg och mekanismer utan att centralisera all operativ förståelse.

## Vanliga anti-patterns

### Dashboarden blir målet

Projektet anses ”ha observability” eftersom en dashboard finns, trots att den inte hjälper någon att förstå tjänstens verkliga tillstånd.

### Alla fel blir larm

Varje tekniskt avvikande mätvärde skickas till jour. Resultatet blir brus och larmtrötthet.

### Logga allt

Loggar används som en osorterad datadump. Kostnaden växer, felsökningen blir svårare och skyddsvärd information riskerar att spridas.

### Backup utan restoretest

Backupjobbet rapporterar grönt år efter år, men ingen vet om återställning faktiskt fungerar.

### Replikering betraktas som backup

Samma logiska fel kopieras snabbt till alla repliker och det saknas en separat återställningspunkt.

### DR reduceras till en andra miljö

Teknisk infrastruktur finns på plats men beslutsvägar, integrationer, identiteter och dataåterställning har aldrig verifierats tillsammans.

### Restart ersätter diagnos

Automatiserad självläkning döljer ett återkommande fel utan att grundorsaken hanteras.

### Plattformsteamet blir ansvarigt för applikationens drift

Konsumenten producerar ingen meningsfull telemetri eftersom den antar att observabilityplattformen automatiskt kan förstå verksamhetslogiken.

## En praktisk analysordning

När driftbarhet och motståndskraft ska utformas för ett IT-stöd kan följande ordning användas:

1. **Utgå från konsekvensen.** Återanvänd kvalitetskraven från kapitel 4.
2. **Identifiera kritiska användar- och verksamhetsflöden.** Vad måste faktiskt fungera?
3. **Kartlägg beroenden och felmoder.** Vad kan fallera och hur sprids felet?
4. **Definiera observerbara signaler.** Vilka loggar, metrics, traces och verksamhetsnära indikatorer behövs?
5. **Definiera SLI och relevanta målnivåer.** Hur vet vi om tjänsten håller önskad kvalitet?
6. **Utforma larm.** Vilka tillstånd kräver mänsklig eller automatisk åtgärd?
7. **Planera felisolering och återhämtning.** Timeout, retry, redundans, failover och andra mekanismer där behovet motiverar dem.
8. **Identifiera vad som måste kunna återställas.** Data, konfiguration och övriga beroenden.
9. **Välj backup- och recoveryprofil.** Knyt den till RPO/RTO eller motsvarande behov.
10. **Dokumentera operativa procedurer.** Runbooks, mandat och eskalering.
11. **Verifiera återställningen.** Testa restore och DR i proportion till konsekvensen.
12. **Lär från drift.** Använd incidenter, kapacitetsdata och återkommande manuellt arbete som återkoppling till arkitekturen.

Ordningen gör driftbarheten till en del av lösningsdesignen i stället för ett övervakningsprojekt som startar strax före produktionssättning.

## Från drift till leverans

En driftbar och motståndskraftig applikation behöver mekanismer för att förstå och återhämta sig från fel.

Men varje förändring i systemet kan också skapa nya fel.

Därför behöver organisationen kunna svara på ytterligare frågor:

- Hur vet vi exakt vilken kod och vilka beroenden som byggdes?
- Hur flyttas samma artefakt mellan miljöer?
- Hur verifieras förändringen före produktion?
- Hur skyddas bygg- och leveranskedjan?
- Hur gör vi en release reproducerbar?
- Hur kan en dålig förändring upptäckas och hanteras snabbt?

Det är nästa förmåga.

I **kapitel 21 – Programvaruutveckling och leverans** flyttas fokus från att hålla en körande tjänst begriplig och återställningsbar till den gemensamma vägen från kod till säker och reproducerbar produktion.
