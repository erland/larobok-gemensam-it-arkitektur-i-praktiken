# 3. Behov före teknik

Det är svårt att fatta teknikoberoende beslut i en organisation som redan har teknik överallt. Befintliga plattformar, avtal, kompetenser, integrationssätt och säkerhetslösningar påverkar vad som upplevs som möjligt. Därför uppstår lätt en omvänd logik: i stället för att först beskriva vilket problem som ska lösas och därefter välja lämplig realisering börjar diskussionen i det som redan finns.

Frågan blir då inte:

> Vad behöver verksamheten eller IT-stödet kunna uppnå?

utan:

> Hur kan vi lösa detta med vår nuvarande plattform?

Det senare är inte alltid fel. En befintlig plattform kan vara både rationell och kostnadseffektiv att återanvända. Problemet uppstår när dess egenskaper omärkligt får definiera behovet. Då blir dagens teknik lätt morgondagens kravbild.

Principen behov före teknik handlar därför inte om att ignorera teknik, kostnad eller befintliga investeringar. Den handlar om att hålla isär tre saker som ofta blandas samman:

1. vad organisationen försöker uppnå,
2. vilka verkliga begränsningar som måste respekteras,
3. vilken teknisk realisering som väljs.

Den separationen är central i resten av boken. Om behov och medel blandas ihop redan från början blir det svårt att senare bedöma kvalitetskrav, jämföra lösningsalternativ eller byta teknik utan att samtidigt behöva omformulera hela problemet.

## När lösningen smyger sig in i behovet

Ett vanligt tecken på teknikdriven kravställning är att behov uttrycks med namn på produkter, protokoll eller plattformar.

Jämför följande formuleringar:

> Systemet ska köras på organisationens containerplattform.

med:

> Tjänsten ska kunna driftsättas reproducerbart, isoleras från andra applikationer, skalas inom givna kapacitetsgränser och förvaltas med organisationens gemensamma drift- och säkerhetsmekanismer.

Den första formuleringen beskriver ett tekniskt beslut. Den andra beskriver egenskaper som kan motivera ett tekniskt beslut.

Det betyder inte att den första formuleringen aldrig hör hemma i arkitekturen. Om organisationen redan har beslutat att en viss typ av tjänst ska använda en gemensam containerplattform kan det vara helt korrekt att uttrycka det som en standard eller begränsning. Men den bör inte förväxlas med det underliggande behovet.

Samma problem uppstår i många andra former:

- ”Vi behöver Kafka” i stället för ”vi behöver distribuera händelser till flera oberoende konsumenter med definierade krav på leverans och ordning”.
- ”Vi behöver en Oracle-databas” i stället för ”vi behöver transaktionell lagring med definierade krav på konsistens, återställning och datalivscykel”.
- ”Vi behöver Kubernetes” i stället för ”vi behöver standardiserad orkestrering och livscykelhantering för containeriserade arbetslaster”.
- ”Vi behöver en AI-assistent” i stället för ”användaren behöver snabbare kunna hitta, sammanställa och bearbeta relevant information med en acceptabel felrisk”.

Produktnamn och tekniker är konkreta, vilket gör dem enkla att diskutera. Behov är ofta svårare. De kräver att man förstår verksamheten, konsekvenserna av fel och vilka egenskaper som faktiskt spelar roll.

Det är därför tekniken lätt vinner diskussionen för tidigt.

## Mål, behov, krav och lösning är olika saker

För att undvika teknikcentrering behöver flera nivåer skiljas åt.

En förenklad kedja är:

```text
Mål
  ↓
Behov
  ↓
Krav
  ↓
Arkitekturval
  ↓
Teknisk lösning
```

Målet beskriver vad organisationen vill åstadkomma. Exempelvis att företag ska kunna hantera ett ärende digitalt utan manuell kontakt.

Behovet beskriver vad verksamheten eller IT-stödet behöver kunna göra för att nå målet. Exempelvis att företag kan identifiera sig, lämna uppgifter och följa ärendets status.

Kravet gör delar av behovet mer precisa eller verifierbara. Exempelvis att en inlämning ska kunna spåras, att vissa uppgifter måste skyddas och att tjänsten ska klara en definierad belastning.

Arkitekturvalet beskriver hur problemet struktureras. Exempelvis separation mellan kanal och domänlogik, asynkron hantering av vissa händelser eller användning av en gemensam identitetstjänst.

Den tekniska lösningen konkretiserar valet i produkter, versioner, konfiguration och implementation.

I praktiken sker arbetet inte linjärt. Ett proof of concept kan visa att ett krav är orimligt dyrt. En säkerhetsbegränsning kan påverka lösningsutrymmet. En befintlig plattform kan göra en viss lösning betydligt billigare än alternativen.

Men även i ett iterativt arbete är nivåerna användbara. De gör det möjligt att se *vad det är som förändras* när ny information kommer fram.

## Ett behov bör beskriva resultat, inte implementation

En praktisk kontrollfråga är:

> Kan behovet fortfarande vara giltigt om vi byter teknik?

Om svaret är nej har formuleringen sannolikt redan bundits för hårt till lösningen.

Anta att en organisation säger:

> Alla externa integrationer ska gå via produkt X.

Det kan vara en helt legitim teknisk standard. Men det underliggande behovet kan i stället vara:

> Externa integrationer ska kunna autentiseras, övervakas, versionshanteras och styras genom gemensamma mekanismer.

Den senare formuleringen överlever ett produktbyte. Den gör det också möjligt att senare fråga om produkt X faktiskt fortfarande är det bästa sättet att uppfylla behovet.

Detta är ett viktigt skäl till att bokens arkitekturmodell skiljer mellan förmåga, plattformstjänst och produkt. Om alla tre nivåerna uttrycks med samma produktnamn blir arkitekturen svår att förändra.

## Teknikoberoende betyder inte teknikblind

Det går att driva principen behov före teknik för långt.

En organisation som låtsas att befintlig teknik, kompetens, kostnad och driftmiljö inte existerar riskerar att skapa arkitektur som är teoretiskt ren men praktiskt orealistisk.

Därför behöver man skilja mellan behov och begränsningar (*constraints*).

En begränsning är en verklig begränsning av lösningsutrymmet. Exempel kan vara:

- information får av rättsliga eller säkerhetsmässiga skäl endast hanteras i vissa miljöer,
- organisationen måste använda ett visst identitetssystem för en viss användargrupp,
- ett externt gränssnitt följer ett obligatoriskt protokoll,
- en äldre kärnlösning kan inte ersättas inom den aktuella tidshorisonten,
- budget eller tid sätter ett konkret tak,
- driftmiljön har definierade nätverks- eller kapacitetsgränser.

Begränsningar är alltså inte samma sak som fria teknikpreferenser.

Jämför:

> Vi använder alltid produkt X.

med:

> Under de kommande tre åren måste lösningen samexistera med produkt X eftersom den är system of record för denna information och inte kan ersättas inom programperioden.

Den senare formuleringen beskriver en faktisk begränsning och dess orsak. Den kan dessutom omprövas när orsaken försvinner.

Det är ofta just denna motivering som saknas när tillfälliga teknikförhållanden blir permanenta arkitekturregler.

## Fråga varför – men inte mekaniskt

En enkel teknik för att komma närmare det verkliga behovet är att fråga varför ett visst teknikönskemål finns.

Exempel:

> Vi behöver en meddelandekö.

Varför?

> För att mottagaren ibland är nere.

Varför är det ett problem?

> För att avsändaren inte får behöva vänta på att mottagaren kommer tillbaka.

Där börjar behovet bli tydligare: tidsmässig frikoppling och möjlighet att hantera temporär otillgänglighet.

Men frågan ”varför?” bör inte användas som en ritual där varje svar ifrågasätts tills diskussionen tappar förankring. Målet är inte att abstrahera bort all konkretion. Målet är att identifiera vilken egenskap eller konsekvens som faktiskt motiverar teknikvalet.

När det är tydligt kan tekniken återintroduceras med ett bättre beslutsunderlag.

## Path dependency: när historien begränsar framtiden

Stora IT-miljöer byggs lager för lager. Ett tidigare beslut påverkar vilka beslut som senare upplevs som möjliga. Detta brukar beskrivas som path dependency: vägen man redan har tagit formar framtida alternativ.

Ett exempel är en organisation som tidigt standardiserar på en viss integrationsplattform. Under åren byggs kompetens, driftprocesser, övervakning, säkerhetskontroller och hundratals integrationer runt den. När nya behov uppstår är plattformen inte längre bara en teknisk produkt. Den har blivit en del av organisationens sätt att arbeta.

Det gör ett byte dyrt även om en annan teknik i isolation skulle vara bättre.

Path dependency är inte i sig ett misslyckande. Gemensamma investeringar ska skapa hävstång och återanvändning. Problemet uppstår när beroendet blir osynligt och gamla beslut behandlas som om de vore naturlagar.

En mogen arkitektur försöker därför göra beroendet explicit:

- Vilka behov löste beslutet ursprungligen?
- Vilka fördelar ger det fortfarande?
- Vilka kostnader skapar det?
- Vilka andra delar av organisationen är beroende av det?
- Vad skulle krävas för att byta?
- När bör beslutet omprövas?

Den typen av frågor gör det möjligt att skilja mellan ett rationellt långsiktigt standardval och ren teknisk tröghet.

## Teknikskuld är inte bara gammal kod

Begreppet teknikskuld används ofta om kod som behöver förbättras. I gemensam IT-arkitektur är problemet bredare.

Teknikskuld kan också finnas i:

- plattformar som blivit svåra att uppgradera,
- standarder som låser organisationen till utgångna arbetssätt,
- integrationsmönster som kräver mycket manuell hantering,
- specialkonfigurationer som hindrar standardisering,
- produktval med få interna kompetensbärare,
- beroenden som saknar tydlig ägare,
- gamla begränsningar som fortsätter gälla trots att deras ursprungliga orsak har försvunnit.

Detta kan kallas arkitekturell teknikskuld: tidigare lösningsval minskar handlingsutrymmet och gör förändring dyrare.

Behov före teknik hjälper inte genom att automatiskt ta bort sådan skuld. Däremot gör principen det lättare att se den.

Om en organisation kan formulera vilket behov en gammal plattform faktiskt fyller går det också att bedöma om behovet kan realiseras på annat sätt. Om plattformen och behovet däremot har blivit synonyma är ett teknikbyte mycket svårare att ens föreställa sig.

## Ett konkret exempel: ”vi behöver en portal”

Anta att en myndighet säger att den behöver en ny portal för externa aktörer.

Ordet portal låter som ett behov men är redan en lösningsidé. Det kan innebära ett webbgränssnitt, inloggning, ärendeöversikt, dokumentutbyte, meddelanden och flera andra funktioner.

En mer behovsdriven analys kan bryta ned önskemålet:

- externa aktörer behöver kunna identifiera sig,
- de behöver kunna se vilka ärenden de har,
- de behöver kunna lämna och komplettera uppgifter,
- de behöver kunna ta emot beslut eller meddelanden,
- de behöver kunna förstå status och nästa steg,
- organisationen behöver kunna spåra vad som har skickats in och när.

Nu blir flera arkitekturella möjligheter synliga.

Kanske behövs en sammanhållen webbkanal. Kanske ska vissa funktioner exponeras genom API:er för aktörer som vill integrera sina egna system. Kanske finns redan en gemensam identitetstjänst och ett ärende-API. Kanske är dokumentutbyte ett separat plattformserbjudande.

Genom att börja i behoven blir ”portal” en möjlig sammansättning av förmågor och tjänster i stället för ett odelbart krav.

Det ger större handlingsfrihet och bättre spårbarhet.

## Ett annat exempel: ”allt ska vara eventdrivet”

Teknikcentrering kan också uppstå genom arkitekturtrender snarare än produkter.

Anta att en organisation beslutar att nya lösningar ska vara eventdrivna.

Det kan bygga på goda erfarenheter av lös koppling, skalbarhet och reaktivitet. Men om principen används utan behovsanalys kan den skapa onödig komplexitet.

Vissa interaktioner är i grunden synkrona. En användare som skickar en enkel fråga och förväntar sig ett direkt svar kan vara bättre betjänt av ett vanligt API-anrop. Att införa asynkrona events kräver då hantering av korrelation, eventual consistency, fel, replay och observerbarhet utan att dessa egenskaper nödvändigtvis löser ett verkligt problem.

En behovsdriven formulering blir i stället:

> Vi behöver kunna frikoppla producenter och konsumenter där flera mottagare behöver reagera på samma affärshändelse eller där tidsmässig frikoppling är viktig.

Då blir eventdriven arkitektur ett mönster som väljs när dess egenskaper passar problemet, inte ett självändamål.

## Begränsningar bör ha ägare och livslängd

Eftersom begränsningar begränsar lösningsutrymmet bör de inte bara skrivas in i ett dokument och glömmas bort.

För viktiga begränsningar är det värdefullt att dokumentera:

- vad begränsningen är,
- varför den finns,
- vem som äger den,
- vilka lösningar den påverkar,
- om den är permanent eller tillfällig,
- när den ska omprövas.

Exempel:

| Begränsning | Orsak | Ägare | Omprövning |
|---|---|---|---|
| Extern identitet ska använda gemensam identitetstjänst | Gemensam tillitsmodell och säkerhetsstyrning | Identitet och tillit | Årligen eller vid större förändring |
| Äldre system måste nås via befintlig integrationsplattform | Kärnsystemet kan inte förändras i pågående program | Integration | Efter programslut |
| Data får endast lagras i godkänd miljöklass | Informationsklassning och säkerhetskrav | Informations-/säkerhetsansvar | Vid förändrad klassning eller miljö |

Det gör stor skillnad om en teknisk begränsning uttrycks som ”så här gör vi” eller som ”detta gäller därför att X, ägs av Y och ska omprövas vid Z”.

Den senare formen stödjer förändring.

## Produktoberoende krav betyder inte generiska krav

Det finns en risk att krav blir så teknikoberoende att de också blir oanvändbara.

Formuleringar som:

> Systemet ska vara säkert.

eller:

> Lösningen ska vara skalbar.

är visserligen produktoberoende, men de ger nästan inget beslutsstöd.

Behov före teknik kräver därför inte bara abstraktion utan också precision.

Det är här nästa kapitel blir viktigt. Kvalitetsattribut behöver uttryckas så att de kan påverka arkitekturen och verifieras. Tillgänglighet, prestanda, säkerhet och återställningsförmåga kan inte lämnas som allmänna ambitioner.

En användbar arbetsordning är därför:

```text
Beskriv behovet utan onödig lösningsbindning
            ↓
Identifiera verkliga begränsningar
            ↓
Gör kvalitetsbehoven konkreta
            ↓
Jämför arkitekturalternativ
            ↓
Välj teknisk realisering
```

Kapitel 4 fördjupar det tredje steget.

## Befintliga plattformar ska påverka beslut – men på rätt nivå

Om organisationen redan har en välfungerande plattform för ett behov är det normalt rationellt att använda den. Gemensam IT-arkitektur ska inte tvinga varje projekt att göra en ny marknadsanalys eller bygga en egen lösning.

Men resonemanget bör vara:

> Behovet och kvalitetskraven passar det etablerade erbjudandet, därför använder vi det.

inte:

> Erbjudandet finns, därför definierar vi problemet så att det passar.

Skillnaden kan verka semantisk, men den är praktiskt viktig.

Den första formuleringen gör det möjligt att identifiera fall där plattformen *inte* passar. Den andra tenderar att göra avsteg till ett organisatoriskt problem även när det egentligen är ett tecken på att erbjudandet inte möter behovet.

Det är också så plattformar kan förbättras. Om flera team visar att ett legitimt återkommande behov inte stöds får förmåge- och plattformsansvariga viktig återkoppling.

Behovsdriven arkitektur är därför inte bara en metod för att välja teknik. Den är också en mekanism för att utveckla de gemensamma erbjudandena.

## Behov före teknik på tre ansvarsnivåer

Principen får olika innebörd beroende på var i organisationen den används.

På gemensam arkitekturnivå handlar den om att definiera långlivade förmågor, principer och kvalitetsdimensioner utan att göra dem onödigt beroende av en viss produktgeneration.

På förmågenivå handlar den om att utveckla mönster, plattformserbjudanden och standarder utifrån återkommande konsumentbehov. Förmågeansvaret bör kunna förklara vilket problem varje gemensamt erbjudande löser och vilka begränsningar det har.

På lösnings-/produktnivå handlar den om att utgå från det konkreta verksamhetsbehovet och välja bland gemensamma byggstenar där de passar, samtidigt som avvikelser motiveras utifrån behov och kvaliteter snarare än preferens.

Detta är ett första exempel på den tredelade ansvarmodell som fördjupas i kapitel 7.

## När behöver man faktiskt börja i tekniken?

Det finns situationer där teknik är en legitim startpunkt.

Exempelvis kan organisationen behöva:

- avveckla en produkt vars support upphör,
- åtgärda en akut sårbarhet,
- konsolidera kostsamma plattformar,
- uppgradera ett operativsystem,
- migrera från en infrastrukturmiljö som stängs ned.

Då uppstår förändringsbehovet faktiskt från tekniksidan.

Men även då är principen användbar. Frågan blir:

> Vilka behov och kvaliteter måste den ersättande lösningen fortsatt uppfylla?

Om en gammal meddelandeplattform ska avvecklas bör man inte automatiskt leta efter ”samma produkt fast ny”. Man bör först förstå vilka integrationsbehov, leveransgarantier, driftskrav och beroenden den gamla plattformen faktiskt hanterade.

Tekniken kan alltså initiera förändringen utan att ensam definiera målbilden.

## Fem kontrollfrågor före ett teknikval

Före ett större tekniskt beslut kan följande frågor användas som enkel kontroll:

1. Vilket behov försöker vi lösa?
   Kan det beskrivas utan produktnamn eller implementationsdetaljer?

2. Vilka egenskaper är avgörande?
   Vad måste vara sant för att lösningen ska vara användbar, säker och förvaltningsbar?

3. Vilka begränsningar är verkliga?
   Vilka begränsningar kommer från juridik, säkerhet, externa parter, tid, ekonomi eller befintliga beroenden?

4. Vilka delar är bara vana eller preferens?
   Finns det antaganden som följer av historiska val snarare än dagens behov?

5. Vad händer om tekniken byts ut?
   Är behov, krav och arkitekturellt resonemang fortfarande begripliga?

Om dessa frågor kan besvaras blir teknikvalet normalt både tydligare och lättare att ompröva.

## Behovsdriven arkitektur gör avsteg mer rationella

I en teknikcentrerad styrmodell bedöms avsteg ofta genom frågan:

> Följer lösningen standarden?

I en behovsdriven modell behövs ytterligare en fråga:

> Uppfyller standardlösningen faktiskt behovet och kvalitetskraven i detta fall?

Det innebär inte att standarder blir frivilliga. Tvärtom kan en gemensam standard vara mycket starkt motiverad av säkerhet, kostnad eller interoperabilitet.

Men ett avsteg kan då bedömas utifrån sakliga kriterier:

- vilket behov som inte täcks,
- vilka kvaliteter som påverkas,
- vilka risker avsteget skapar,
- om avsteget bör vara lokalt eller leda till att den gemensamma förmågan utvecklas.

Detta gör styrningen mer lärande. Ett återkommande avsteg kan vara ett tecken på att standarden eller plattformstjänsten behöver förändras.

## Från lösningskatalog till problemförståelse

Organisationer samlar ofta mycket kunskap om vilka tekniker de använder men mindre strukturerad kunskap om vilka problem teknikerna löser.

En mogen gemensam arkitektur behöver båda.

Det bör gå att svara på:

- Vilka återkommande behov ser vi?
- Vilka kvaliteter är viktigast för dessa behov?
- Vilka förmågor ansvarar för dem?
- Vilka mönster har visat sig fungera?
- Vilka plattformstjänster erbjuder vi?
- Vilka standarder begränsar lösningsutrymmet?
- Vilka produkter råkar realisera detta just nu?

När dessa frågor hålls samman blir tekniken lättare att byta utan att organisationen tappar sin arkitekturella kunskap.

Det är själva poängen med att lägga behov före teknik: inte att göra arkitekturen mindre teknisk, utan att göra teknikvalen mer begripliga och mer hållbara.

## Centrala fakta

- Behov före teknik innebär att först beskriva vad som ska uppnås och varför, innan lösningen låses till en viss produkt eller implementation.
- Mål, behov, krav, arkitekturval och teknisk realisering är olika nivåer och bör kunna skiljas åt även när arbetet är iterativt.
- Ett behov är normalt bättre formulerat om det fortfarande är giltigt när den nuvarande tekniken byts ut.
- Teknikoberoende betyder inte att befintlig teknik, ekonomi eller säkerhetsförutsättningar ska ignoreras.
- Verkliga begränsningar bör beskrivas som begränsningar med tydlig orsak, ägare och omprövningspunkt.
- Path dependency gör att historiska teknikval påverkar framtida handlingsutrymme; detta är inte alltid negativt men bör vara synligt.
- Arkitekturell teknikskuld kan finnas i plattformar, standarder, integrationssätt och beroenden – inte bara i kod.
- Produktoberoende krav måste fortfarande vara tillräckligt precisa för att ge beslutsstöd.
- Befintliga gemensamma plattformar bör påverka teknikval när de möter behovet, men deras existens bör inte ensam definiera behovet.
- Principen gäller på gemensam nivå, förmågenivå och lösnings-/produktnivå, men med olika ansvar.
- Även teknikinitierade förändringar bör återkopplas till vilka behov och kvaliteter den nya lösningen måste bevara.

## Begrepp att känna till

Behov – något verksamheten eller IT-stödet behöver kunna uppnå.

Mål – ett önskat verksamhets- eller organisationsresultat som behov och lösningar ska bidra till.

Begränsning – en verklig begränsning av lösningsutrymmet, exempelvis juridik, säkerhetskrav, externa beroenden, tid eller ekonomi.

Teknikoberoende krav – krav som beskriver nödvändiga egenskaper utan onödig bindning till en viss produkt eller implementation.

Path dependency – att tidigare val formar vilka framtida alternativ som är praktiskt eller ekonomiskt möjliga.

Teknikskuld – framtida kostnad eller minskat handlingsutrymme som följer av tidigare tekniska beslut, genvägar eller kvarvarande beroenden.

Arkitekturval – ett beslut om hur en lösning struktureras för att möta behov och krav.

Realisering – den konkreta implementationen av ett arkitekturval i teknik, produkt, version och konfiguration.
