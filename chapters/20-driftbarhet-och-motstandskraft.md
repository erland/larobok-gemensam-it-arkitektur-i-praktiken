# 20. Driftbarhet och motståndskraft

Ett system kan vara korrekt byggt, korrekt driftsatt och ändå vara svårt att hålla fungerande över tid. Det kan sakna tillräcklig telemetri för att förstå vad som händer, ha larm som ingen kan agera på, innehålla beroenden som gör att små fel sprider sig eller ha säkerhetskopior som aldrig har provats i en verklig återställning.

*Driftbarhet och motståndskraft* handlar därför inte bara om att ”ha övervakning” eller ”ta backup”. Förmågan handlar om att göra system begripliga under drift, möjliga att återställa och konstruerade så att fel kan hanteras utan att konsekvenserna blir större än nödvändigt.

Kärnfrågan i kapitlet är:

> Hur skapar en organisation gemensamma mekanismer för att förstå, upptäcka, begränsa och återhämta sig från fel – på en nivå som motsvarar verksamhetens faktiska behov?

Kapitel 4 beskrev hur tillgänglighet, kontinuitet, återställningstid och andra kvalitetskrav härleds från verksamhetskonsekvenser. Det här kapitlet tar nästa steg: vilka tekniska och operativa förmågor behövs för att realisera och verifiera sådana krav?

Runtimefrågor som exekveringsmiljö, scaling och healthmekanismer behandlades i kapitel 19. Bygg, test, release och driftsättning behandlas i kapitel 21. Fokus här ligger på observerbarhet, monitorering, larm, felisolering, återhämtning, backup, restore, disaster recovery, kapacitetsuppföljning och operativ återkoppling.

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

Två system med samma observerbarhetsplattform kan därför ha helt olika driftbarhet. Plattformen kan ge verktyg och standarder, men lösningen måste fortfarande producera meningsfull telemetri och vara utformad så att signalerna går att använda.

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

Det leder till kvalitetsprofiler snarare än ett universellt maximalkrav.

En gemensam plattform kan exempelvis erbjuda flera profiler för backup, retention, redundans eller larmning. Konsumenten väljer inte profil efter tycke, utan utifrån de kvalitetsbehov som härletts tidigare.

## Observerbarhet och tjänstehälsa

### Observerbarhet (*observability*) är förmågan att förstå systemets tillstånd

Begreppet *observability*, här observerbarhet, används ofta som synonym till övervakning, men det är mer användbart att skilja dem åt.

Monitorering handlar i första hand om att följa kända signaler och upptäcka att ett definierat villkor har inträffat.

Observerbarhet handlar bredare om att kunna dra slutsatser om ett systems interna beteende utifrån den telemetri systemet exponerar.[K1]

Skillnaden blir tydlig i en incident.

Monitorering kan säga:

> Felkvoten för API:t har passerat fem procent.

Observerbarhet behöver dessutom hjälpa oss svara på:

- Vilka anrop fallerar?
- När började problemet?
- Berör det alla användare eller en viss grupp?
- Finns sambandet med en release?
- Är databasen långsam eller är det ett externt beroende?
- Uppstår felet i samma del av ett distribuerat flöde?
- Är systemet tekniskt levande men verksamhetsmässigt oanvändbart?

En gemensam observerbarhetsförmåga behöver därför en sammanhängande modell för loggar, mätvärden, spår, korrelation, larm och åtkomst till telemetrin – inte bara en central loggdatabas.

### Loggar berättar vad som hände

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

För mycket loggning skapar kostnad och brus och kan dessutom sprida information som aldrig borde lämna komponenten. Logga därför det som behövs för drift, felsökning och relevant spårbarhet – inte allt som är tekniskt möjligt. Credentials, secrets och onödiga person- eller skyddsvärda uppgifter hör inte hemma i diagnostiskt material, och retention behöver styras medvetet.

### Mätvärden visar beteende över tid

Loggar beskriver enskilda händelser. mätvärden gör det lättare att se mönster och förändring över tid.

Exempel på tekniska mätvärden är:

- svarstid,
- felkvot,
- antal anrop,
- ködjup,
- CPU- och minnesanvändning,
- antal aktiva anslutningar,
- antal lyckade eller misslyckade bakgrundsjobb.

Tekniska resursmått räcker inte alltid. Ett system kan ha låg CPU-belastning och samtidigt vara oanvändbart för verksamheten. Därför behövs ibland verksamhetsnära operativa signaler, exempelvis:

- antal ärenden som fastnat i ett visst steg,
- ålder på äldsta obehandlade meddelande,
- antal genomförda kritiska transaktioner,
- andel misslyckade dokumentleveranser,
- tid från inkommen händelse till slutförd behandling.

Syftet är inte full verksamhetsanalys, utan att förstå om tjänsten faktiskt levererar den funktion som behöver hållas i drift.

### Tracing knyter ihop distribuerade flöden

När ett användarflöde passerar flera tjänster, gateways, databaser och meddelandekanaler blir lokala loggar snabbt otillräckliga.

Distributed tracing kan då göra det möjligt att följa ett sammanhängande flöde över flera komponenter.

Alla system behöver inte full tracing, men organisationen bör ha en gemensam mekanism när behovet finns.

I ett flöde som passerar exempelvis gateway, flera tjänster och en meddelandekö blir incidentanalysen snabbt manuellt detektivarbete om varje komponent bara har lokala identifierare. Med gemensam korrelation kan samma logiska transaktion följas genom kedjan.

Detta är särskilt viktigt i integrationsintensiva miljöer. Samtidigt behöver korrelationsinformation designas så att den inte i sig blir en bärare av känslig information.

### Teknisk hälsa är inte samma sak som fungerande tjänst

Ett av de vanligaste misstagen i driftövervakning är att kontrollera att processen lever och sedan anta att tjänsten fungerar.

Det finns flera nivåer av hälsa: process, instans, beroenden, tjänstekontrakt och det faktiska användar- eller verksamhetsflödet. De bör inte blandas ihop.

Dessa nivåer ska inte alltid kopplas ihop mekaniskt.

Om en health check exempelvis gör instansen ”ohälsosam” bara för att ett externt beroende är tillfälligt nere kan runtime-plattformen börja starta om fullt fungerande instanser i onödan. Resultatet kan bli större störning än det ursprungliga felet.

Health checks behöver därför ha ett tydligt syfte. En signal för automatisk omstart har större konsekvens än en signal för en instrumentpanel, och felaktig automation kan förstora incidenten.

### SLI, SLO och SLA fyller olika funktioner

För att driva en tjänst behöver man kunna mäta den egenskap som är viktig.

En Service Level Indicator, SLI, är ett mätetal som representerar en relevant aspekt av tjänstens beteende. Det kan exempelvis vara andelen lyckade anrop eller svarstid för ett definierat flöde.

Ett Service Level Objective, SLO, uttrycker den önskade nivån för indikatorn under en viss period.[K2]

Ett Service Level Agreement, SLA, är däremot ett avtal eller en överenskommelse där servicenivåer kan vara kopplade till formella åtaganden och konsekvenser.

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
Observerbarhet och operativ uppföljning
```

SLO bör inte börja i frågan ”vilka mätvärden kan vår plattform mäta?”. De bör börja i vilket tjänstebeteende som faktiskt är viktigt.

### Larm ska leda till handling

Det är enkelt att skapa larm. Det är svårare att skapa bra larm.

Ett larm är värdefullt när det signalerar ett tillstånd som kräver mänsklig eller automatiserad åtgärd.

Ett bra produktionslarm bör ha ett definierat felvillkor, känd betydelse, tydligt ansvar, rimlig prioritet, tillräcklig kontext och en möjlig nästa åtgärd.

Om ett larm återkommande ignoreras finns i grunden tre möjligheter:

1. tröskeln är fel,
2. signalen är inte åtgärdsbar,
3. organisationen saknar mandat eller kapacitet att agera.

Att lägga ytterligare larm ovanpå problemet förbättrar inte driftbarheten.

Larmtrötthet är därför ett tecken på att den operativa signalmodellen behöver förbättras.

### Instrumentpaneler är hypoteser om vad som är viktigt

instrumentpaneler blir lätt stora samlingar av grafer därför att telemetrin finns tillgänglig.

En bättre utgångspunkt är att varje vy ska svara på en fråga.

Exempelvis kan en vy svara på om tjänsten fungerar för användarna, om ett beroende blir en flaskhals, om en release förändrat felkvoten eller om en kö växer snabbare än den behandlas.

Olika målgrupper behöver ofta olika vyer. Plattformen bör standardisera tillgången till data, inte anta att samma instrumentpanel representerar alla tjänsters verkliga hälsa.

## Motståndskraft under pågående drift

### Motståndskraft börjar med att fel förväntas

Motståndskraft, eller resilience, handlar inte om att skapa system där inget någonsin går sönder.

Det handlar om att utforma system så att fel:

- upptäcks,
- begränsas,
- hanteras,
- återhämtas från,
- och ger lärande inför nästa händelse.

I distribuerade system kommer nätverksfördröjning, otillgängliga beroenden, överbelastning, processkrascher och misslyckade driftsättningar förr eller senare att inträffa.

Arkitekturen behöver därför fråga:

> Vad händer när detta beroende inte svarar?

inte bara:

> Hur anropar vi beroendet när allt fungerar?

### Felisolering begränsar konsekvensytan

Ett litet fel blir allvarligt när det får sprida sig genom hela lösningen.

Felisolering kan skapas med exempelvis tidsgränser, separata resurspooler, begränsade köer, isolerade exekveringsmiljöer, bulkheads och avgränsade fel-, data- eller nätverksdomäner.

Varje isoleringsgräns har kostnad. Frågan är därför vilka beroenden som kan orsaka oproportionerligt stora konsekvenser om de fallerar.

Det är nära kopplat till diskussionen om coupling i kapitel 10. Ett system kan vara logiskt modulärt men fortfarande operativt starkt kopplat om alla delar fallerar tillsammans.

### Timeout är en arkitekturell gräns

Ett synkront anrop utan rimlig timeout är i praktiken ett antagande om att motparten alltid svarar.

Det är sällan ett säkert antagande.

Timeouts begränsar hur länge en komponent väntar på ett beroende och skyddar därmed resurser som trådar, anslutningar och kökapacitet.

Men timeoutvärdet kan inte väljas isolerat.

Om tjänst A anropar B som anropar C behöver tidsbudgeten förstås över hela kedjan. Annars kan den yttre klienten ge upp medan interna tjänster fortsätter arbeta med ett resultat som ingen längre väntar på.

I kritiska flöden är timeout därför en del av lösningens fel- och latensmodell, inte bara lokal konfiguration.

### Återförsök kan både hjälpa och skada

Automatiska återförsök kan hantera kortvariga fel mycket effektivt.

De kan också förstärka en incident.

Om tusentals klienter omedelbart skickar om misslyckade anrop mot en redan överbelastad tjänst kan återförsökslogiken skapa en återkopplingsloop som gör problemet större.

Återförsök behöver därför analyseras tillsammans med idempotens, timeout, backoff/jitter, maximal försöksmängd, mottagarens kapacitet och feltyp.

Ett permanent valideringsfel ska normalt inte försöka skickas om på samma sätt som ett tillfälligt nätverksfel.

Leveranssemantik och kommunikationsmönster hör ihop med motståndskraften, men driftbarhetsförmågan behöver framför allt synliggöra när återförsök sker, misslyckas eller skapar belastning.

### Automatisk återhämtning är värdefull när beteendet är säkert

Automatisk restart, failover och annan självläkning kan kraftigt minska återställningstid.

Men automation bör användas där organisationen förstår konsekvensen.

En stateless instans som inte längre svarar kan ofta ersättas säkert.

En datakomponent med oklar replikeringsstatus kan kräva betydligt försiktigare beslut innan automatisk failover sker.

Principen är därför inte ”automatisera all recovery”, utan:

> Automatisera återkommande återhämtning när tillståndet kan identifieras pålitligt och åtgärden har förutsägbara konsekvenser.

Automation ska dessutom vara observerbar. Upprepade automatiska återstarter utan reaktion löser inte grundproblemet utan kan dölja det.

## Återställning efter större fel

### Backup är inte samma sak som återställningsförmåga

En lyckad backupkörning bevisar bara att en mekanism har producerat något som bedöms vara en säkerhetskopia.

Den bevisar inte att:

- rätt data ingår,
- datat är konsistent,
- nödvändig konfiguration finns med,
- credentials och nycklar kan återetableras,
- kopian kan läsas,
- återställningen ryms inom önskad tid,
- den återställda tjänsten faktiskt fungerar.

Därför är verifierad restore viktigare än ett grönt backupjobb.

En återställningsstrategi behöver börja med att identifiera vad som faktiskt måste kunna återskapas. Det kan omfatta mer än databasen: verksamhetsdata, objekt och dokument, konfiguration, infrastrukturbeskrivningar, nyckelmaterial, externa beroendekonfigurationer och metadata som krävs för att tolka datat.

Detta behöver samordnas med dataförmågan i kapitel 15. Informationsägaren avgör vad som behöver skyddas och hur länge. Driftbarhetsförmågan tillhandahåller mekanismerna för backup och återställning.

### Replikering och backup löser olika fel

Replikering kan ge hög tillgänglighet och minska effekten av att en enskild nod eller lagringskomponent fallerar.

Men en replika kan också snabbt kopiera samma problem:

- oavsiktlig radering,
- applikationsfel,
- datakorruption,
- felaktig migrering,
- skadlig förändring.

Därför är replikering inte automatiskt en ersättning för backup.

På motsvarande sätt är backup inte en ersättning för hög tillgänglighet. Om det tar flera timmar att återställa en säkerhetskopia löser den inte ett behov där tjänsten bara får vara nere några minuter.

Mekanismerna svarar alltså på olika felbilder och behöver väljas därefter.

### RPO och RTO behöver kopplas till verklig recovery

Kapitel 4 introducerade Recovery Point Objective, RPO, och Recovery Time Objective, RTO som sätt att uttrycka återställningsbehov.[K3]

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

En tekniskt möjlig återställning på trettio minuter är alltså inte samma sak som en organisatoriskt genomförbar återställning på trettio minuter.

### Disaster recovery är en kedja, inte en reservmiljö

Disaster recovery, DR, reduceras ibland till frågan om organisationen har en sekundär miljö.

Det är otillräckligt.

En fungerande DR-förmåga omfattar hela kedjan från störning och beslut om aktivering till alternativ miljö, återställning av data och konfiguration, återetablerade integrationer och identiteter, verifiering, trafikomläggning och operativ stabilisering. Varje steg kan bli den verkliga flaskhalsen.

Det hjälper exempelvis inte att databasen kan återställas snabbt om:

- certifikat saknas,
- DNS-ändringen kräver manuell handläggning,
- externa parter bara accepterar trafik från den primära miljön,
- secrets inte finns i recoverymiljön,
- integrationsköer inte kan återskapas,
- ingen har mandat att initiera växlingen.

DR är därför en kedja av både arkitektur och operativ förmåga.

### En recoveryplan som aldrig övas är en hypotes

Dokumentation är nödvändig men inte tillräcklig.

En driftinstruktion kan vara logiskt korrekt och ändå fallera när den används därför att:

- kommandon har förändrats,
- behörigheter saknas,
- en beroendetjänst har bytt adress,
- backupformatet har ändrats,
- en återställning tar betydligt längre tid än antaget,
- ett manuellt steg bara förstås av en person.

Återställning behöver därför verifieras på en nivå som motsvarar konsekvensen av misslyckande.

Det kan handla om automatiserade restoretester, återläsning i isolerad miljö, komponentvisa recoveryövningar, fullskaliga DR-övningar eller tabletop-övningar för besluts- och ansvarskedjan.

Testfrekvens och omfattning bör styras av kvalitetsbehovet.

## Operativ förmåga och lärande

### Driftinstruktioner gör kunskap operativ

En driftinstruktion beskriver hur ett känt operativt tillstånd hanteras.

En bra driftinstruktion beskriver hur problemet identifieras, vilka kontroller och åtgärder som är säkra, när särskilt mandat eller eskalering krävs och hur återhämtningen verifieras och dokumenteras.

Driftinstruktioner är särskilt värdefulla vid återkommande diagnos- och åtgärdskedjor, men ska inte permanent ersätta automation. Om samma instruktion används flera gånger i veckan är det ofta en signal om att produkt eller plattform bör förbättras.

### Kapacitet är en del av driftbarheten

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

Skalbarhet beskriver hur kapaciteten kan förändras när belastningen ändras. Driftbarheten behöver visa när kapaciteten inte räcker och om skalningsmekanismen faktiskt fungerar; en autoscaler ersätter inte kapacitetsförståelse.

### Operativ återkoppling ska påverka arkitekturen

En av de största vinsterna med en gemensam driftbarhetsförmåga är att incidenter och driftdata kan skapa strukturerad återkoppling.

Återkommande problem kan exempelvis visa att ett kontrakt är för skört, en runtimeprofil fel dimensionerad, en recoveryprofil otillräcklig, ägargränser otydliga eller ett manuellt moment moget för automation.

Återkopplingen behöver gå tillbaka till rätt nivå. Ett lokalt kodfel ska inte bli en organisationsstandard, men om många team möter samma problem är det sannolikt inte längre lokalt.

### Incidenthantering och problemhantering är olika perspektiv

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

Mognad syns därför både i hur snabbt tjänsten återställs och i om återkommande fel leder till förbättring.

## Gemensamma tjänster inom förmågan

Förmågan kan realiseras genom flera separata gemensamma tjänster, exempelvis:

### Central Logging Service

Gemensam insamling, retention, sökning och åtkomstkontroll för tekniska loggar. Konsumenten ansvarar fortfarande för att logga meningsfullt och korrekt.

### Monitoring and Tracing

Gemensam insamling av mätvärden och spår samt stöd för instrumentpaneler och larm. Konsumenten definierar vilka signaler som representerar den egna tjänstens hälsa.

### Backup and Recovery Service

Gemensamma profiler för backup, point-in-time recovery och restore. Konsumenten identifierar vad som behöver skyddas och verifierar att hela lösningen kan återställas.

Tjänsterna kan vara separata produkter även om de hör till samma förmåga; det finns inget egenvärde i att samla observerbarhet, backup och DR i en enda teknisk plattform.

## Standardisering ska ske på rätt nivå

Gemensamma standarder kan skapa stor nytta inom driftbarhet eftersom många mekanismer annars implementeras olika i varje produkt.

Exempel på lämpliga standardområden är:

- strukturerad loggning,
- korrelationsmekanism,
- benämning och labels för mätvärden,
- health checks,
- hur spår propagateras,
- förbud mot secrets i loggar,
- backup- och restoreprofiler,
- krav på återkommande restoretest för kritiska data.

Men en standard bör inte automatiskt föreskriva samma detaljnivå för alla system.

Full distributed tracing kan vara rimligt för en komplex integrationskedja och överdrivet för en enkel intern batchtjänst. En sekundär recoverymiljö kan vara motiverad för ett kritiskt verksamhetssystem och ekonomiskt orimlig för en stödtjänst med lågt kontinuitetskrav.

Standarden bör därför ange miniminivåer, gemensamma kontrakt och valbara kvalitetsprofiler snarare än maximal robusthet överallt.

## Ansvar på tre nivåer

Ansvarsfördelningen följer samma modell som i övriga boken:

- **Gemensam arkitekturnivå:** definierar kvalitetsprofiler, gemensamma telemetri- och korrelationskontrakt samt övergripande krav på observerbarhet, backup, restore och DR.
- **Förmågenivå:** utvecklar observerbarhets-, monitoring-, tracing- och recoverytjänster, standarder och golden paths samt samlar återkoppling från konsumenterna.
- **Lösnings-/produktnivå:** härleder egna kvalitetskrav, producerar användbar telemetri, väljer relevanta profiler, kartlägger felmoder och ansvarar för att återställning och driftinstruktioner faktiskt fungerar.

Det gör det möjligt att standardisera mekanismer utan att centralisera den operativa förståelsen av varje system.

## Vanliga anti-patterns

### Dashboarden blir målet

En instrumentpanel finns, men hjälper ingen att förstå tjänstens verkliga tillstånd.

### Alla fel blir larm

Varje teknisk avvikelse skickas till jour och skapar brus och larmtrötthet.

### Logga allt

Loggar blir en osorterad datadump som ökar kostnad, försvårar felsökning och riskerar att sprida skyddsvärd information.

### Backup utan restoretest

Backupjobbet rapporterar grönt år efter år, men ingen vet om återställning faktiskt fungerar.

### Replikering betraktas som backup

Samma logiska fel kopieras snabbt till alla repliker och det saknas en separat återställningspunkt.

### DR reduceras till en andra miljö

Teknisk infrastruktur finns på plats men beslutsvägar, integrationer, identiteter och dataåterställning har aldrig verifierats tillsammans.

### Restart ersätter diagnos

Automatiserad självläkning döljer ett återkommande fel utan att grundorsaken hanteras.

### Plattformsteamet blir ansvarigt för applikationens drift

Konsumenten antar att observerbarhetsplattformen automatiskt kan förstå verksamhetslogiken och producerar därför inte tillräcklig telemetri.

## En praktisk analysordning

En praktisk analys kan följa denna ordning:

1. Utgå från konsekvensen. Återanvänd kvalitetskraven från kapitel 4.
2. Identifiera kritiska användar- och verksamhetsflöden. Vad måste faktiskt fungera?
3. Kartlägg beroenden och felmoder. Vad kan fallera och hur sprids felet?
4. Definiera observerbara signaler. Vilka loggar, mätvärden, spår och verksamhetsnära indikatorer behövs?
5. Definiera SLI och relevanta målnivåer. Hur vet vi om tjänsten håller önskad kvalitet?
6. Utforma larm. Vilka tillstånd kräver mänsklig eller automatisk åtgärd?
7. Planera felisolering och återhämtning. Timeout, återförsök, redundans, failover och andra mekanismer där behovet motiverar dem.
8. Identifiera vad som måste kunna återställas. Data, konfiguration och övriga beroenden.
9. Välj backup- och recoveryprofil. Knyt den till RPO/RTO eller motsvarande behov.
10. Dokumentera operativa procedurer. driftinstruktioner, mandat och eskalering.
11. Verifiera återställningen. Testa restore och DR i proportion till konsekvensen.
12. Lär från drift. Använd incidenter, kapacitetsdata och återkommande manuellt arbete som återkoppling till arkitekturen.

Ordningen gör driftbarheten till en del av lösningsdesignen, inte ett sent övervakningsprojekt.

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

I kapitel 21 – Programvaruutveckling och leverans flyttas fokus från att hålla en körande tjänst begriplig och återställningsbar till den gemensamma vägen från kod till säker och reproducerbar produktion.

## Källor och vidare läsning

**[K1]** OpenTelemetry, *Signals*. https://opentelemetry.io/docs/concepts/signals/

**[K2]** Google, *Site Reliability Engineering – Service Level Objectives* och *Monitoring Distributed Systems*. https://sre.google/sre-book/service-level-objectives/ och https://sre.google/sre-book/monitoring-distributed-systems/

**[K3]** NIST, *SP 800-34 Rev. 1: Contingency Planning Guide for Federal Information Systems*. https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final
