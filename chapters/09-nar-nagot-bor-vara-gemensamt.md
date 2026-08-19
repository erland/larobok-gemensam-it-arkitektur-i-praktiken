# 9. När något bör vara gemensamt

Att en organisation arbetar med gemensamma IT-förmågor betyder inte att allt bör göras gemensamt. Tvärtom blir förmågemodellen användbar först när den hjälper organisationen att skilja mellan sådant som vinner på gemensamt ansvar och sådant som bör ligga nära den verksamhetsdomän, produkt eller lösning där behovet uppstår.

Detta är en av de svåraste avvägningarna i en större IT-organisation. Om för lite görs gemensamt uppstår duplicering, inkompatibilitet, ojämn kvalitet och onödigt höga kostnader. Om för mycket centraliseras uppstår i stället köer, svag verksamhetsanpassning, långsam förändring och gemensamma plattformar som försöker lösa alla problem men passar få riktigt bra.

Frågan är därför inte:

> Vad kan vi centralisera?

utan snarare:

> Vilka behov är så återkommande, riskfyllda eller beroende av gemensam samordning att organisationen tjänar på att bära ett gemensamt ansvar för dem?

Detta kapitel introducerar en beslutsmodell för den frågan. Fokus ligger på **vad som lämpar sig för gemensamt ansvar**. Hur ett gemensamt tekniskt erbjudande senare utformas som plattformstjänst, produkt eller självservice behandlas i del V.

## Gemensamt ansvar är inte samma sak som central produktion

Det första som behöver klarläggas är att *gemensamt* inte automatiskt betyder *centralt producerat av ett enda team*.

En organisation kan ha ett gemensamt ansvar för exempelvis identitet, API-principer eller observerbarhet samtidigt som delar av realiseringen är federerad. Ett centralt arkitekturområde kan definiera gemensamma krav och gränser, flera plattformsteam kan erbjuda olika tekniska byggblock och lösningsteamen kan bära ansvar för lokal konfiguration och användning.

Det innebär att man bör skilja mellan åtminstone fyra frågor:

1. **Behöver området ha gemensamma regler eller mål?**
2. **Behöver organisationen erbjuda en gemensam tjänst eller plattform?**
3. **Behöver realiseringen skötas av en central organisatorisk enhet?**
4. **Vilken variation bör vara tillåten nära lösningen?**

Dessa frågor har inte alltid samma svar.

Identitetsfederation är ett tydligt exempel. Organisationen kan behöva gemensamma tillitsregler, gemensamma protokoll och ett begränsat antal identitetsleverantörer. Men det betyder inte att varje behörighetsbeslut i varje verksamhetssystem bör fattas centralt. Själva autentiseringen kan vara starkt gemensam medan den verksamhetsnära auktorisationen behöver ligga närmare domänen.

På motsvarande sätt kan organisationen ha en gemensam standard för loggformat och spårbarhet, en gemensam loggplattform och ändå låta varje produktteam äga vilka verksamhetshändelser som är meningsfulla att logga.

**Gemensamt ansvar handlar därför främst om sammanhang, kompatibilitet och uthållighet – inte om organisationsform.**

## Sex frågor som hjälper till att bedöma gemensamhet

Det finns ingen enskild matematisk gräns för när något bör vara gemensamt. Däremot återkommer ett antal egenskaper som gör gemensamt ansvar mer eller mindre motiverat.

I den här boken används sex huvudfrågor:

1. Finns tydliga **skalfördelar**?
2. Finns **risker eller styrkrav** som behöver hanteras konsekvent?
3. Kräver området **specialiserad kompetens** som inte rimligen kan dupliceras överallt?
4. Finns ett starkt behov av **interoperabilitet och gemensamma kontrakt**?
5. Är problemet **återkommande och tillräckligt likartat** mellan flera konsumenter?
6. Finns det samtidigt ett behov av **lokal differentiering** som gör full centralisering olämplig?

De fem första frågorna talar ofta för ökad gemensamhet. Den sjätte fungerar som motvikt. Det är sällan klokt att optimera enbart för återanvändning om det sker på bekostnad av verksamhetens behov av variation.

## Skalfördelar – när en lösning kan betjäna många

Det mest intuitiva argumentet för gemensamhet är skala.

Om tio produktteam behöver samma typ av teknisk stöd är det ofta ineffektivt att tio team var för sig ska upphandla, installera, konfigurera, säkra, övervaka och livscykelhantera var sin variant. Gemensamt ansvar kan då minska både direkt kostnad och den dolda kostnaden för duplicerad kompetens och förvaltning.

Typiska områden där skalfördelar kan vara betydande är:

- källkodshantering,
- CI/CD-infrastruktur,
- identitets- och certifikattjänster,
- central loggning,
- backup och återställning,
- container- eller runtimeplattformar,
- meddelandeinfrastruktur,
- gemensamma databastjänster,
- standardiserade utvecklarverktyg.

Men skala är inte bara en kostnadsfråga. Ett gemensamt erbjudande kan också göra en avancerad lösning praktiskt tillgänglig för fler team. Ett enskilt produktteam kanske inte har resurser att bygga en robust certifikatlivscykel, självservice för secrets eller avancerad observerbarhet. Om detta finns som gemensamt erbjudande kan teamet konsumera en högre kvalitet än det rimligen hade kunnat skapa självt.

Samtidigt finns en viktig gräns: **skalfördelar uppstår bara när behoven faktiskt är tillräckligt lika**.

Om ett gemensamt erbjudande kräver så många specialfall att varje konsument ändå måste ha en unik lösning kan den tänkta skalfördelen försvinna. Då kan en gemensam standard eller ett gemensamt kontrakt vara mer värdefullt än en enda gemensam teknisk tjänst.

## Risk och styrkrav – när variation blir dyr eller farlig

Vissa områden lämpar sig för gemensamt ansvar därför att konsekvenserna av fel är stora.

Identitet, secrets, certifikat, backup, säkerhetsloggning och programvaruförsörjningskedja är exempel där svag eller inkonsekvent hantering i en enda lösning kan skapa risk långt utanför det lokala teamet.

Gemensamhet kan då motiveras av behovet att:

- säkerställa miniminivåer,
- skapa spårbarhet,
- kunna genomföra kontroller,
- reagera samordnat vid incidenter,
- hantera sårbarheter och livscykler,
- minska antalet unika säkerhetslösningar,
- ge en tydlig ansvarspunkt för kritiska mekanismer.

Det betyder inte att varje säkerhetsbeslut ska centraliseras. Snarare bör organisationen fråga vilken del av risken som är **systemisk**.

Ett produktteam kan till exempel själv behöva avgöra vilka data en viss roll får se. Men organisationen kan samtidigt behöva en gemensam mekanism för autentisering, gemensamma krav på stark autentisering och gemensamma protokoll för identitetsöverföring.

Ju mer ett fel kan påverka flera lösningar, organisationens tillit eller möjligheten att uppfylla externa krav, desto starkare är argumentet för gemensamma ramar och ofta även gemensamma tjänster.

## Specialiserad kompetens – när expertis bör koncentreras

Vissa tekniska områden kräver djup kompetens som är svår att upprätthålla i varje enskilt produktteam.

Det kan handla om exempelvis:

- PKI och certifikathantering,
- avancerad nätverksdesign,
- databasmotorns drift och återställning,
- meddelandemäklares klustring och leveranssemantik,
- Kubernetes- eller containerplattformars interna drift,
- avancerad observerbarhet,
- sökindexering,
- AI-infrastruktur eller modellförvaltning.

Om varje team måste bygga upp full specialistkompetens blir organisationen både dyr och sårbar. Kunskapen kan bli tunn, ojämnt fördelad och beroende av enskilda personer.

Ett gemensamt förmågeområde kan i stället koncentrera specialistkompetensen och göra den konsumerbar genom dokumenterade tjänster, standarder och stödformer.

Här finns dock en viktig balans. Specialistkompetens får inte bli en exklusiv kunskapsö som gör alla andra beroende av manuella beställningar. Ett moget gemensamt område försöker i stället **produktifiera expertisen**:

```text
Specialistkunskap
       ↓
Standarder och automatiserade kontroller
       ↓
Plattformstjänster och golden paths
       ↓
Självservice där konsumenten kan agera själv
```

Det gemensamma området skapar då hävstång på sin kompetens i stället för att skapa en kö till specialisterna.

## Interoperabilitet – när flera måste kunna förstå varandra

Det starkaste argumentet för gemensamhet är ibland inte effektivitet utan **interoperabilitet**.

Två system som ska utbyta information kan inte var för sig bestämma helt olika kontrakt och ändå förvänta sig friktionsfri samverkan. Samma sak gäller identiteter, meddelanden, events, loggkorrelation, tidsformat, kodverk och många andra gränssnitt.

I sådana fall behöver organisationen ofta gemensamma standarder även om själva implementationen förblir decentraliserad.

Detta leder till en viktig princip:

> Ju mer ett beslut påverkar gränsen mellan två självständiga delar, desto starkare är behovet av gemensam samordning.

Det är en annan situation än ett rent internt implementationsval. Ett team kan ofta själv välja hur en intern algoritm organiseras. Men API-kontraktet mot andra team eller tjänster kan behöva följa gemensamma regler eftersom konsekvensen annars bärs av flera parter.

Interoperabilitet är därför ett tydligt exempel på varför **gemensam standard** och **gemensam plattform** är olika saker. Organisationen kan behöva ett gemensamt API-format utan att varje API måste köras genom samma gateway. Den kan behöva ett gemensamt eventkontrakt utan att alla domäner måste använda exakt samma interna programmeringsmodell.

## Återkommande likartade behov – när återanvändning faktiskt är möjlig

För att något ska bli en bra gemensam förmåga eller tjänst behöver problemet inte vara identiskt överallt, men det måste finnas en tillräckligt stabil gemensam kärna.

Detta kan testas genom att fråga:

- Uppstår behovet i flera verksamhetsområden?
- Är de viktigaste kvalitetskraven tillräckligt lika?
- Kan ett gemensamt kontrakt formuleras utan att känna till varje verksamhetsdomän?
- Kan variation uttryckas genom konfiguration eller tydliga tjänstenivåer?
- Skulle en gemensam lösning kunna utvecklas oberoende av enskilda konsumenters releaseplaner?

Om svaret ofta är ja finns förutsättningar för gemensamt ansvar.

Om svaret däremot är att varje konsument behöver unik processlogik, unik datamodell, unik regulatorisk tolkning och unik livscykel kan det som först såg gemensamt ut i själva verket vara domänspecifikt.

Detta är särskilt relevant för verksamhetsnära plattformar som workflow, case management, regler och analys. Där kan det finnas gemensamma tekniska byggblock, men den verksamhetsmässiga betydelsen behöver ofta ligga nära domänen.

Ett bra gemensamt erbjudande försöker därför hitta **minsta men värdefulla gemensamma nämnare**, inte maximal funktionell täckning.

## Differentiering – när lokal variation är själva poängen

Ett område bör inte göras gemensamt enbart för att flera team råkar arbeta med något som ser liknande ut.

Om den lokala variationen är viktig för verksamhetens resultat kan centralisering minska värdet.

Ett publikt användargränssnitt och ett internt specialistverktyg kan båda behöva webbteknik, men användarresor, tillgänglighetskrav, förändringstakt och interaktionsmönster kan skilja sig kraftigt. Ett gemensamt designsystem kan fortfarande vara värdefullt, medan en gemensam färdig frontendplattform med hårt låst navigationsmodell kan bli begränsande.

Samma princip gäller verksamhetsregler. Det kan vara klokt att erbjuda gemensam regelteknik, versionshantering och spårbarhet. Men själva reglernas innehåll och ägarskap bör normalt ligga där verksamhetskunskapen finns.

Det är därför ofta mer träffsäkert att fråga:

> Vilken del av problemet behöver vara gemensam, och vilken del behöver medvetet få variera?

än att försöka klassificera hela området som antingen centraliserat eller decentraliserat.

## Ett spektrum: lokalt, federerat och gemensamt

I praktiken är gemensamhet ett spektrum. Tre idealtypiska lägen är användbara:

### Lokalt ansvar

Varje produkt- eller domänteam väljer och förvaltar sin egen lösning inom breda gemensamma principer.

Det passar när:

- behovet är starkt domänspecifikt,
- beroendena till andra är små,
- riskerna är lokala,
- variation ger verkligt värde,
- kostnaden för gemensam samordning är större än nyttan.

### Federerat ansvar

Gemensamma kontrakt, standarder eller grundkomponenter kombineras med lokal realisering och lokalt ägarskap.

Det passar när:

- interoperabilitet kräver gemensamma regler,
- flera tekniska realiseringar behöver kunna samexistera,
- verksamhetsnära variation är betydande,
- organisationen vill undvika både fragmentering och central köbildning.

### Gemensamt tjänsteansvar

Organisationen erbjuder en konsumerbar gemensam tjänst eller plattform med tydligt ägarskap och livscykel.

Det passar när:

- behovet är återkommande och relativt homogent,
- skalfördelarna är stora,
- specialiserad kompetens bör koncentreras,
- risk eller compliance talar för enhetlighet,
- en gemensam tjänst kan ge bättre användarupplevelse än lokal egenproduktion.

Dessa lägen kan dessutom kombineras inom samma förmåga.

För *Integration och kommunikation* kan organisationen exempelvis ha:

- gemensamma API- och eventstandarder,
- en gemensam API management-tjänst,
- en gemensam meddelandetjänst,
- federerat ägarskap för integrationskontrakt,
- lokalt ansvar för domänens data och semantik.

Förmågan är gemensam, men ansvarsmönstret är inte monolitiskt.

## Centralisering har också kostnader

Gemensamma initiativ motiveras ofta genom de problem de ska lösa, men deras egna kostnader glöms lätt bort.

Ett centraliserat erbjudande kan skapa:

- väntetider och beroenden,
- långsammare anpassning,
- lägre känsla av ägarskap hos konsumenterna,
- en stor gemensam failure domain,
- överstandardisering,
- svårigheter att prioritera mellan många olika behov,
- teknisk inlåsning om en gemensam plattform blir obligatorisk för länge.

Detta betyder inte att gemensamma plattformar är fel, utan att deras nytta måste jämföras med **samordningskostnaden**.

En gemensam lösning som sparar tio team fem timmars arbete per år men kräver ett helt centralt team för att förvaltas är knappast en skalfördel. En gemensam lösning som däremot minskar säkerhetsrisk, gör återställning verifierbar och eliminerar hundratals lokala speciallösningar kan vara mycket värdefull även om plattformsteamet i sig är kostsamt.

Gemensamhet behöver därför bedömas som ett arkitekturbeslut med samma disciplin som andra större val: alternativ, konsekvenser, kvaliteter, kostnader och omprövningsvillkor.

## En enkel bedömningsmatris

Som praktiskt stöd kan ett kandidatbehov bedömas längs några dimensioner:

| Fråga | Låg drivkraft för gemensamt | Hög drivkraft för gemensamt |
|---|---|---|
| Förekomst | Få, unika behov | Många återkommande behov |
| Risk | Lokal och begränsad | Systemisk eller regulatoriskt viktig |
| Kompetens | Vanlig och lättillgänglig | Djup specialistkompetens |
| Interoperabilitet | Små externa beroenden | Många beroenden och kontrakt |
| Standardiserbarhet | Stor domänvariation | Stabil gemensam kärna |
| Skala | Liten eller obefintlig vinst | Stor kostnads-/kvalitetsvinst |
| Differentiering | Variation skapar verksamhetsvärde | Variation ger liten nytta |

Matrisen ska inte summeras mekaniskt till ett tal. Den är ett sätt att göra resonemanget synligt.

Ett område kan exempelvis ha låg skalfördel men mycket hög systemisk risk. Då kan gemensamma standarder ändå vara motiverade. Ett annat område kan ha hög teknisk skalfördel men så stark verksamhetsdifferentiering att organisationen bör erbjuda gemensamma byggblock snarare än en enda komplett lösning.

Poängen är att undvika två dåliga tumregler:

> Om flera använder det ska det centraliseras.

eller:

> Teamen är autonoma, alltså ska allt vara lokalt.

Båda missar arkitekturens verkliga fråga: **var behöver beroenden och ansvar samordnas för att helheten ska fungera?**

## Bedöm förmågan och tjänsten separat

En särskilt viktig distinktion är att en gemensam **förmåga** inte automatiskt innebär en gemensam **plattformstjänst**.

Organisationen kan behöva ett gemensamt ansvar för *Interaktion, presentation och kanaler* utan att erbjuda en enda frontendplattform. Förmågeområdet kan i stället äga designsystem, tillgänglighetsstandarder, kanalprinciper och vissa återanvändbara komponenter.

På samma sätt kan *Data- och informationshantering* vara en tydlig gemensam förmåga medan vissa specialiserade databaser eller datalager fortfarande ägs lokalt.

Bedömningen bör därför ske i två steg:

```text
1. Behöver organisationen bära ett gemensamt ansvar för området?
                         ↓
2. Vilka delar av detta ansvar bör realiseras som gemensamma
   standarder, mönster, tjänster eller plattformar?
```

Det första steget formar förmågekartan. Det andra formar erbjudandeportföljen.

Om stegen blandas ihop finns risk att förmågekartan blir en direkt avbildning av dagens plattformskatalog. Då försvinner den stabilitet som var en av huvudpoängerna med förmågebegreppet.

## Gemensamt betyder att någon måste äga helheten

Även i en federerad modell behöver det vara tydligt vem som håller ihop området.

Ett gemensamt förmågeansvar behöver kunna:

- följa återkommande behov hos flera konsumenter,
- identifiera gemensamma kvalitetskrav,
- definiera gränsen mot närliggande förmågor,
- förvalta relevanta principer och standarder,
- avgöra vilka mönster som bör rekommenderas,
- bedöma när en gemensam tjänst är motiverad,
- följa teknik- och produktlivscykler,
- synliggöra beroenden och luckor,
- samla återkoppling från faktiska lösningar.

Det innebär inte att förmågeansvarig ska fatta alla lokala beslut. Rollen är snarare att säkerställa att organisationen inte tappar bort helheten medan implementation och verksamhetsnära variation förblir distribuerad.

Detta knyter tillbaka till ansvarmodellen från kapitel 7:

- den **gemensamma arkitekturen** definierar spelplanen,
- **förmågeområdet** utvecklar det gemensamma stödet inom sitt område,
- **lösnings- och produktteamen** tillämpar och kombinerar stödet i konkreta verksamhetslösningar.

Frågan om gemensamhet avgör alltså inte vem som skriver varje rad kod. Den avgör **på vilken nivå organisationen behöver bära ett sammanhållet ansvar**.

## Gemensamhet ska kunna omprövas

Ett beslut att göra något gemensamt är inte permanent.

Teknikutveckling kan förändra kostnadsbilden. En tjänst som tidigare krävde djup specialistkompetens kan bli en standardiserad molntjänst. Ett område som en gång var likartat kan med tiden utvecklas i olika verksamhetsriktningar. Eller omvänt kan flera lokala lösningar mogna så att en gemensam kärna blir tydlig först efter några år.

Därför bör organisationen regelbundet fråga:

- Används det gemensamma erbjudandet faktiskt?
- Löser det fortfarande ett återkommande behov?
- Är variationen under kontroll eller växer specialfallen?
- Ger erbjudandet skala eller har det blivit en flaskhals?
- Har riskbilden förändrats?
- Finns lokala lösningar som visar en bättre väg?
- Bör något som är centralt bli mer federerat – eller tvärtom?

Detta är samma iterativa logik som etablerades i kapitel 7. Förmågekartan är stabilare än produktlandskapet, men den är inte immun mot lärande.

## Tre exempel

### Exempel 1: Secrets management

Många team behöver hantera lösenord, tokens, nycklar och andra hemligheter. Felhantering kan ge allvarliga säkerhetskonsekvenser. Kompetensen för säker lagring, rotation, audit och åtkomstkontroll är specialiserad. Behoven är samtidigt relativt lika mellan många lösningar.

Det talar starkt för gemensamt ansvar och ofta för en gemensam tjänst.

Det lokala teamet behöver ändå äga vilka hemligheter dess lösning använder, när de ska bytas och vilka applikationsidentiteter som ska få åtkomst.

### Exempel 2: Verksamhetsspecifik beslutslogik

Flera system behöver fatta beslut, men reglernas innehåll, juridiska betydelse och förändringstakt kan vara starkt verksamhetsspecifika.

Det kan finnas skäl för gemensamma mönster, standarder för spårbarhet och eventuellt en gemensam regelplattform. Däremot bör reglernas semantik och ägarskap normalt inte centraliseras till ett IT-plattformsteam.

Här blir en federerad modell ofta mer rimlig än full centralisering.

### Exempel 3: Observerbarhet

Alla produktteam behöver kunna förstå sina system i drift. Gemensam korrelation, logghantering, mätvärden, tracing och larmkedjor ger stora skalfördelar och förbättrar möjligheten att felsöka över systemgränser.

Det talar för gemensamma standarder och gemensam plattform.

Men plattformsteamet kan inte veta vilka verksamhetsmått som visar om en ansökningsprocess eller ett kontrollflöde fungerar korrekt. Den semantiska instrumenteringen behöver därför ligga nära lösningen.

Även här är den bästa modellen en kombination av gemensam infrastruktur och lokalt ansvar.

## En tumregel för beslutets nivå

Ett användbart sätt att sammanfatta kapitlet är att låta **konsekvensens räckvidd** styra beslutets nivå.

Om ett beslut främst påverkar ett enda teams implementation bör det normalt kunna fattas lokalt.

Om beslutet påverkar flera team genom kontrakt, gemensamma risker eller återanvändbara erbjudanden behöver förmågeområdet ofta hålla ihop frågan.

Om beslutet påverkar flera förmågor, organisationens gemensamma säkerhets- eller kvalitetsnivå eller den övergripande arkitekturmodellen behöver det hanteras på gemensam nivå.

Detta kan uttryckas så här:

```text
Lokal konsekvens
      ↓
Lösning / produkt

Konsekvens för flera konsumenter inom ett område
      ↓
Förmågeområde

Konsekvens över flera förmågor eller hela organisationen
      ↓
Gemensam arkitektur
```

Målet är inte maximal centralisering. Målet är att **lägga ansvaret på den lägsta nivå som fortfarande kan bära hela konsekvensen av beslutet**.

## Sammanfattning

Något bör inte göras gemensamt bara för att det går att göra gemensamt.

Gemensamt ansvar är främst motiverat när flera av följande gäller:

- behovet återkommer hos många konsumenter,
- skalfördelarna är betydande,
- risk eller styrkrav behöver hanteras konsekvent,
- specialistkompetens bör koncentreras,
- interoperabilitet kräver gemensamma kontrakt,
- den gemensamma kärnan är stabil nog att standardisera.

Samtidigt måste organisationen skydda den variation som skapar verkligt verksamhetsvärde. Därför är federerade modeller ofta lika viktiga som helt centrala tjänster.

Den avgörande frågan är inte om en teknik ska vara central eller lokal, utan **vilket ansvar som måste hållas ihop på vilken nivå**.

I nästa kapitel flyttas perspektivet från gemensamhet till gränser. En förmågekarta kan visa vilka tekniska stödområden organisationen behöver bära ansvar för, men den löser inte frågan om hur verksamhetsdomäner, dataägarskap och lösningsansvar ska avgränsas. Det kräver ett kompletterande domänperspektiv.
