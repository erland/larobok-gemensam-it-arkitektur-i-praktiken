# 3. Behov före teknik

Det är svårt att fatta teknikoberoende beslut i en organisation som redan har teknik överallt. Befintliga plattformar, avtal, kompetenser, integrationssätt och säkerhetslösningar påverkar vad som upplevs som möjligt. Därför uppstår lätt en omvänd logik: i stället för att först beskriva vilket problem som ska lösas och därefter välja lämplig realisering börjar diskussionen i det som redan finns.

Frågan blir då inte:

> Vad behöver verksamheten eller IT-stödet kunna uppnå?

utan:

> Hur kan vi lösa detta med vår nuvarande plattform?

Det senare är inte alltid fel. En befintlig plattform kan vara både rationell och kostnadseffektiv att återanvända. Problemet uppstår när dess egenskaper omärkligt får definiera behovet. Då blir dagens teknik lätt morgondagens kravbild.

Principen behov före teknik handlar därför om att hålla isär tre saker:

1. vad organisationen försöker uppnå,
2. vilka verkliga begränsningar som måste respekteras,
3. vilken teknisk realisering som väljs.

Om behov och medel blandas ihop blir det svårare att jämföra lösningar, formulera relevanta kvalitetskrav och byta teknik utan att samtidigt behöva omformulera själva problemet.

## När lösningen smyger sig in i behovet

Ett vanligt tecken på teknikdriven kravställning är att behov uttrycks med namn på produkter, protokoll eller plattformar.

Jämför:

> Systemet ska köras på organisationens *containerplattform*.

med:

> Tjänsten ska kunna driftsättas reproducerbart, isoleras från andra applikationer, skalas inom givna kapacitetsgränser och förvaltas med organisationens gemensamma drift- och säkerhetsmekanismer.

Den första formuleringen beskriver ett tekniskt beslut. Den andra beskriver egenskaper som kan motivera ett tekniskt beslut.

Om organisationen redan har beslutat att en viss typ av tjänst ska använda en gemensam containerplattform kan den första formuleringen mycket väl vara korrekt som standard eller begränsning. Men den bör inte förväxlas med det underliggande behovet.

Samma problem uppstår i andra former:

- ”Vi behöver Kafka” i stället för ”vi behöver distribuera händelser till flera oberoende konsumenter med definierade krav på leverans och ordning”.
- ”Vi behöver en Oracle-databas” i stället för ”vi behöver transaktionell lagring med definierade krav på konsistens, återställning och datalivscykel”.
- ”Vi behöver Kubernetes” i stället för ”vi behöver standardiserad orkestrering och livscykelhantering för containeriserade arbetslaster”.
- ”Vi behöver en AI-assistent” i stället för ”användaren behöver snabbare kunna hitta, sammanställa och bearbeta relevant information med en acceptabel felrisk”.

Produktnamn och tekniker är konkreta och därför lätta att diskutera. Behov kräver mer analys: vilket resultat som ska uppnås, vilka konsekvenser fel får och vilka egenskaper som faktiskt spelar roll.

## Mål, behov, krav och lösning är olika saker

För att undvika teknikcentrering behöver flera nivåer skiljas åt:

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

Målet beskriver vad organisationen vill åstadkomma. Behovet beskriver vad verksamheten eller IT-stödet behöver kunna göra för att nå målet. Kraven gör behovet mer precist och verifierbart. Arkitekturvalet beskriver hur problemet struktureras. Den tekniska lösningen konkretiserar valet i produkter, versioner, konfiguration och implementation.

Arbetet är sällan linjärt. Ett proof of concept kan visa att ett krav är orimligt dyrt. En säkerhetsbegränsning kan minska lösningsutrymmet. En befintlig plattform kan göra ett alternativ betydligt mer attraktivt än andra. Men nivåerna är fortfarande användbara eftersom de gör det möjligt att se *vad* som behöver omprövas när ny information kommer fram.

## Ett behov bör beskriva resultat, inte implementation

En praktisk kontrollfråga är:

> Kan behovet fortfarande vara giltigt om vi byter teknik?

Om svaret är nej har formuleringen sannolikt redan bundits för hårt till lösningen.

Anta att en organisation säger:

> Alla externa integrationer ska gå via produkt X.

Det kan vara en legitim teknisk standard. Det underliggande behovet kan däremot vara:

> Externa integrationer ska kunna autentiseras, övervakas, versionshanteras och styras genom gemensamma mekanismer.

Den senare formuleringen överlever ett produktbyte och gör det möjligt att senare bedöma om produkt X fortfarande är ett lämpligt sätt att realisera behovet.

## Teknikoberoende betyder inte teknikblind

Principen kan drivas för långt. En organisation som låtsas att befintlig teknik, kompetens, kostnad och driftmiljö inte existerar riskerar att skapa arkitektur som är teoretiskt ren men praktiskt orealistisk.

Därför behöver behov skiljas från begränsningar (*constraints*). En begränsning är något som faktiskt begränsar lösningsutrymmet, exempelvis att:

- information av rättsliga eller säkerhetsmässiga skäl endast får hanteras i vissa miljöer,
- ett visst identitetssystem måste användas för en användargrupp,
- ett externt gränssnitt följer ett obligatoriskt protokoll,
- en äldre kärnlösning inte kan ersättas inom aktuell tidshorisont,
- budget eller tid sätter ett konkret tak,
- driftmiljön har givna nätverks- eller kapacitetsgränser.

Begränsningar är alltså inte samma sak som teknikpreferenser.

Jämför:

> Vi använder alltid produkt X.

med:

> Under de kommande tre åren måste lösningen samexistera med produkt X eftersom den är system of record för denna information och inte kan ersättas inom programperioden.

Den senare formuleringen anger både orsak och tidshorisont. Den kan därför omprövas när förutsättningarna förändras.

## Fråga varför – men inte mekaniskt

En enkel teknik för att komma närmare behovet är att fråga varför ett teknikönskemål finns.

> Vi behöver en meddelandekö.

Varför?

> För att mottagaren ibland är nere.

Varför är det ett problem?

> För att avsändaren inte får behöva vänta på att mottagaren kommer tillbaka.

Där börjar behovet bli tydligare: tidsmässig frikoppling och hantering av temporär otillgänglighet.

Frågan ”varför?” bör dock inte användas som en ritual där varje svar abstraheras ytterligare. Målet är att identifiera vilken egenskap eller konsekvens som motiverar teknikvalet, inte att göra problemet så generiskt att det tappar betydelse.

## Path dependency: när historien begränsar framtiden

Stora IT-miljöer byggs lager för lager. Ett tidigare beslut påverkar vilka beslut som senare upplevs som möjliga. Detta brukar beskrivas som path dependency: den väg organisationen redan tagit formar framtida alternativ.

En organisation kan exempelvis ha standardiserat på en integrationsplattform. Med tiden byggs kompetens, driftprocesser, övervakning, säkerhetskontroller och många integrationer runt den. Plattformen är då inte längre bara en teknisk produkt utan en del av organisationens sätt att arbeta.

Det gör ett byte dyrt även om en annan teknik isolerat sett skulle vara bättre.

Path dependency är inte i sig ett misslyckande. Gemensamma investeringar ska skapa återanvändning och hävstång. En plattform som många lösningar bygger på kan vara värdefull just därför att organisationen har investerat i kompetens, säkerhetsmekanismer och driftförmåga runt den. Problemet uppstår först när beroendet blir osynligt och gamla beslut behandlas som naturlagar.

Det är också viktigt att skilja mellan kostnaden för att byta och skälet att stanna kvar. Höga byteskostnader kan vara rationella att acceptera under lång tid, men de är inte ett bevis för att den befintliga lösningen alltid är rätt. Arkitekturen behöver därför synliggöra både den nytta som byggts upp och den tröghet som följer med den.

Därför bör det vara möjligt att svara på:

- vilket behov beslutet ursprungligen löste,
- vilka fördelar det fortfarande ger,
- vilka kostnader och beroenden det skapar,
- vad som skulle krävas för att byta,
- när beslutet bör omprövas.

På så sätt går det att skilja ett rationellt långsiktigt standardval från ren teknisk tröghet.

## Teknikskuld är mer än gammal kod

Teknikskuld kan också finnas i plattformar, standarder, integrationssätt, specialkonfigurationer och beroenden. Gemensamt för dessa fall är att tidigare val minskar handlingsutrymmet eller gör förändring dyrare.

Principen behov före teknik tar inte bort sådan skuld, men gör den lättare att se. Om organisationen kan beskriva vilket behov en gammal plattform faktiskt fyller går det också att pröva om samma behov kan realiseras på annat sätt. Om plattformen och behovet blivit synonyma blir ett teknikbyte svårare att ens föreställa sig.

Det gör också skillnad för hur skulden prioriteras. En gammal komponent som fortfarande uppfyller sitt behov med rimlig risk är inte nödvändigtvis akut att ersätta. En modern plattform som däremot tvingar fram speciallösningar för återkommande behov kan skapa större arkitekturell skuld trots att tekniken i sig är ny. Fokus bör därför ligga på handlingsutrymme och konsekvenser, inte på ålder.

## Ett konkret exempel: ”vi behöver en portal”

Anta att en myndighet säger att den behöver en ny portal för externa aktörer.

Ordet portal låter som ett behov men är redan en lösningsidé. En behovsdriven analys kan i stället visa att externa aktörer behöver kunna:

- identifiera sig,
- se sina ärenden,
- lämna och komplettera uppgifter,
- ta emot beslut eller meddelanden,
- förstå status och nästa steg.

Organisationen behöver dessutom kunna spåra vad som skickats in och när.

När behoven skiljs från lösningsnamnet blir flera arkitekturella alternativ synliga. Kanske behövs en sammanhållen webbkanal. Kanske bör vissa funktioner också exponeras genom API:er. Kanske finns redan en gemensam identitetstjänst och ett ärende-API. Dokumentutbyte kan vara ett separat plattformserbjudande.

Analysen kan dessutom visa att olika aktörsgrupper behöver olika kanaler men samma bakomliggande tjänster. Då blir det möjligt att återanvända identitet, ärendeinformation och meddelandefunktioner utan att tvinga alla användare in i samma gränssnitt. Det är ett konkret exempel på varför en lösningsterm kan vara för grov för att fungera som behovsbeskrivning.

”Portal” blir då en möjlig sammansättning av förmågor och tjänster i stället för ett odelbart krav.

## Ett kort exempel: ”allt ska vara eventdrivet”

Teknikcentrering kan också uppstå genom arkitekturtrender. Ett generellt krav på eventdriven arkitektur kan bygga på goda erfarenheter av lös koppling och skalbarhet men ändå skapa onödig komplexitet när behovet i grunden är synkront.

En mer användbar formulering är:

> Vi behöver kunna frikoppla producenter och konsumenter där flera mottagare behöver reagera på samma affärshändelse eller där tidsmässig frikoppling är viktig.

Då blir eventdriven arkitektur ett mönster som väljs när dess egenskaper passar problemet, inte ett självändamål.

## Begränsningar bör ha ägare och livslängd

Viktiga begränsningar bör dokumenteras med orsak, ägare och omprövningspunkt.

| Begränsning | Orsak | Ägare | Omprövning |
|---|---|---|---|
| Extern identitet ska använda gemensam identitetstjänst | Gemensam tillitsmodell och säkerhetsstyrning | Identitet och tillit | Årligen eller vid större förändring |
| Äldre system måste nås via befintlig integrationsplattform | Kärnsystemet kan inte förändras i pågående program | Integration | Efter programslut |
| Data får endast lagras i godkänd miljöklass | Informationsklassning och säkerhetskrav | Informations-/säkerhetsansvar | Vid förändrad klassning eller miljö |

Det är stor skillnad mellan ”så här gör vi” och ”detta gäller därför att X, ägs av Y och ska omprövas vid Z”. Den senare formen stödjer förändring.

Ägarskapet behöver inte innebära att en enskild person ensam får upphäva begränsningen. Poängen är att någon funktion ansvarar för att orsaken fortfarande är giltig, att konsekvenserna är kända och att omprövning faktiskt sker. Utan ett sådant ansvar tenderar tillfälliga begränsningar att leva vidare långt efter att deras ursprungliga skäl har försvunnit.

## Produktoberoende krav betyder inte generiska krav

Det finns en risk att krav blir så teknikoberoende att de också blir oanvändbara.

> Systemet ska vara säkert.

eller:

> Lösningen ska vara skalbar.

är produktoberoende men ger nästan inget beslutsstöd.

Behov före teknik kräver därför inte bara abstraktion utan precision. En användbar arbetsordning är:

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

Nästa steg är att fördjupa hur kvalitetsbehoven görs till användbara arkitekturdrivare.

## Befintliga plattformar ska påverka beslut – men på rätt nivå

Om organisationen redan har en välfungerande plattform för ett behov är det normalt rationellt att använda den. Resonemanget bör dock vara:

> Behovet och kvalitetskraven passar det etablerade erbjudandet, därför använder vi det.

inte:

> Erbjudandet finns, därför definierar vi problemet så att det passar.

Den första formuleringen gör det möjligt att identifiera fall där plattformen inte passar och ger samtidigt återkoppling till den gemensamma förmågan när återkommande behov saknar stöd.

Detta är viktigt även för plattformsförvaltningen. Om flera team behöver samma egenskap och alla tvingas bygga lokala kompletteringar är problemet kanske inte att teamen avviker, utan att det gemensamma erbjudandet är ofullständigt. På motsvarande sätt kan ett mycket ovanligt behov motivera en lokal lösning utan att plattformen behöver breddas. Behovsbilden blir därmed ett underlag både för konsumtion och för utveckling av gemensamma tjänster.

## Behov före teknik på tre ansvarsnivåer

Principen gäller på alla tre ansvarsnivåerna, men på olika sätt. På gemensam nivå innebär den att långlivade förmågor och principer inte binds onödigt till en produktgeneration. På förmågenivå innebär den att mönster och plattformserbjudanden utvecklas utifrån återkommande konsumentbehov. På lösnings-/produktnivå innebär den att gemensamma byggstenar används där de möter det konkreta behovet.

Den praktiska ansvarsfördelningen mellan nivåerna utvecklas senare i denna del.

## När behöver man faktiskt börja i tekniken?

Ibland kommer förändringsbehovet från tekniksidan: en produkt tappar support, en sårbarhet måste åtgärdas, en plattform ska konsolideras eller en infrastrukturmiljö avvecklas.

Då är teknik en legitim startpunkt. Men frågan kvarstår:

> Vilka behov och kvaliteter måste den ersättande lösningen fortsatt uppfylla?

Om en gammal meddelandeplattform ska avvecklas bör man därför inte automatiskt leta efter ”samma produkt fast ny”, utan först förstå vilka integrationsbehov, leveransgarantier, driftskrav och beroenden den gamla plattformen faktiskt hanterade.

Tekniken kan initiera förändringen utan att ensam definiera målbilden.

## Fem kontrollfrågor före ett teknikval

Före ett större tekniskt beslut kan följande frågor användas:

1. **Vilket behov försöker vi lösa?** Kan det beskrivas utan produktnamn eller implementationsdetaljer?
2. **Vilka egenskaper är avgörande?** Vad måste vara sant för att lösningen ska vara användbar, säker och förvaltningsbar?
3. **Vilka begränsningar är verkliga?** Vad följer av juridik, säkerhet, externa parter, tid, ekonomi eller befintliga beroenden?
4. **Vilka delar är vana eller preferens?** Finns antaganden som följer av historiska val snarare än dagens behov?
5. **Vad händer om tekniken byts ut?** Är behov, krav och arkitekturellt resonemang fortfarande begripliga?

Frågorna gör teknikvalet tydligare och lättare att ompröva.

## Från problemförståelse till teknikval

En mogen gemensam arkitektur behöver både kunskap om tekniklandskapet och en tydlig bild av vilka problem tekniken ska lösa. Sambandet från behov och kvalitetskrav till arkitekturval och realisering behöver därför gå att följa i båda riktningarna.

Poängen med behov före teknik är inte att göra arkitekturen mindre teknisk, utan att göra teknikvalen mer begripliga, jämförbara och förändringsbara.

## Centrala fakta

- Behov före teknik innebär att beskriva vad som ska uppnås och varför innan lösningen binds till en viss produkt eller implementation.
- Mål, behov, krav, arkitekturval och teknisk realisering är olika nivåer även när arbetet är iterativt.
- Ett behov är normalt bättre formulerat om det fortfarande är giltigt när den nuvarande tekniken byts ut.
- Teknikoberoende betyder inte att befintlig teknik, ekonomi eller säkerhetsförutsättningar ska ignoreras.
- Verkliga begränsningar bör ha tydlig orsak, ägare och omprövningspunkt.
- Path dependency gör att historiska teknikval påverkar framtida handlingsutrymme och bör därför vara synligt.
- Produktoberoende krav måste fortfarande vara tillräckligt precisa för att ge beslutsstöd.
- Befintliga gemensamma plattformar bör påverka teknikval när de möter behovet, men deras existens bör inte ensam definiera behovet.
- Även teknikinitierade förändringar bör återkopplas till de behov och kvaliteter som måste bevaras.

## Begrepp att känna till

Behov – något verksamheten eller IT-stödet behöver kunna uppnå.

Mål – ett önskat verksamhets- eller organisationsresultat som behov och lösningar ska bidra till.

Begränsning – en verklig begränsning av lösningsutrymmet, exempelvis juridik, säkerhetskrav, externa beroenden, tid eller ekonomi.

Teknikoberoende krav – krav som beskriver nödvändiga egenskaper utan onödig bindning till en viss produkt eller implementation.

Path dependency – att tidigare val formar vilka framtida alternativ som är praktiskt eller ekonomiskt möjliga.

Teknikskuld – framtida kostnad eller minskat handlingsutrymme som följer av tidigare tekniska beslut, genvägar eller kvarvarande beroenden.

Arkitekturval – ett beslut om hur en lösning struktureras för att möta behov och krav.

Realisering – den konkreta implementationen av ett arkitekturval i teknik, produkt, version och konfiguration.
