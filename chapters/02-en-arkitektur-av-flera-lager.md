# 2. En arkitektur av flera lager

Det är lätt att tala om arkitektur som om den vore en enda sak. I praktiken består en fungerande gemensam IT-arkitektur av flera olika typer av beskrivningar, beslut och erbjudanden som förändras i olika takt och svarar på olika frågor.

Ett verksamhetsbehov är inte samma sak som ett tekniskt krav. En förmåga är inte samma sak som en plattform. Ett lösningsmönster är inte samma sak som en produktstandard. En referensarkitektur är inte samma sak som en färdig lösningsarkitektur. När dessa nivåer blandas ihop blir arkitekturen svår att förstå och ännu svårare att förändra.

Detta kapitel presenterar den modell som används genom resten av boken. Syftet är inte att gå på djupet i varje artefakttyp redan här. Kapitlet ger i stället en karta över vilka lager som finns, varför de behöver hållas isär och hur de relaterar till varandra. Kartan visar också hur ett konkret teknikval kan spåras tillbaka till det behov som motiverade det.

En sådan karta är viktig av två skäl. För det första gör den det möjligt att tala om arkitektur utan att omedelbart hamna i produktdiskussioner. För det andra gör den det möjligt att förändra tekniken utan att behöva skriva om hela den övergripande modellen varje gång en produkt, version eller plattform byts ut.

## Från behov till realisering

Den grundläggande kedjan i boken kan beskrivas så här:

```text
Verksamhets- och IT-stödsbehov
        ↓
Krav och kvalitetsattribut
        ↓
Gemensamma IT-förmågor
        ↓
Lösningsmönster
        ↓
Plattformar och tjänsteerbjudanden
        ↓
Tekniska standarder
        ↓
Tekniska byggblock
        ↓
Produkt / version / konfiguration
```

Modellen ska inte läsas som att varje behov måste passera exakt ett objekt i varje lager. Verkligheten är mer komplex. Ett behov kan beröra flera förmågor. Ett lösningsmönster kan spänna över flera förmågor. En plattformstjänst kan realisera delar av flera mönster. En standard kan gälla flera plattformar. Samma produkt kan användas som byggblock i flera olika tjänster.

Poängen är i stället att lagren representerar olika frågor.

- Behov svarar på vad verksamheten eller IT-stödet behöver kunna uppnå.
- Krav och kvalitetsattribut uttrycker vilka egenskaper lösningen måste ha.
- Förmågor beskriver vilka återkommande typer av stöd IT-området behöver kunna erbjuda.
- Lösningsmönster beskriver återanvändbara sätt att strukturera återkommande problem.
- Plattformstjänster beskriver konsumerbara tekniska erbjudanden.
- Standarder anger gemensamma teknikval, konventioner och ramar.
- Tekniska byggblock beskriver generiska tekniska beståndsdelar.
- Produkter, versioner och konfigurationer beskriver den konkreta realiseringen.

Detta gör att samma arkitekturdiskussion kan föras på rätt nivå. Om ett projekt behöver hög tillgänglighet ska man inte börja med frågan om vilken produkt som ska installeras. Om ett team behöver asynkron kommunikation ska man inte först bestämma meddelandeprodukt och därefter försöka formulera vilket problem den löser.

Arkitekturens uppgift är att hålla ihop resonemanget från behov till realisering utan att låsa ihop nivåerna mer än nödvändigt.

## Lager handlar också om förändringstakt

Ett viktigt skäl till att skilja lagren åt är att de förändras i olika takt.

Ett återkommande behov av säker autentisering kan finnas i decennier. Förmågan att hantera identitet och tillit kan därför vara stabil över lång tid. Ett visst protokoll eller en viss plattform kan leva kortare. En produktversion kan vara aktuell i bara några år, ibland ännu kortare.

Om allt dokumenteras på samma nivå uppstår två problem.

Det första är att stabila beskrivningar blir fulla av kortlivad teknik. Ett dokument som borde beskriva vad organisationen behöver kunna göra börjar i stället innehålla versionsnummer, produktnamn och konfigurationsdetaljer. När tekniken förändras måste hela dokumentet revideras, trots att behovet är detsamma.

Det andra problemet är det motsatta: tekniska beslut blir för abstrakta. En organisation kan ha mycket välformulerade principer om interoperabilitet och återanvändning men sakna tydliga besked om vilka protokoll, plattformar och versionsnivåer som faktiskt stöds.

En användbar modell behöver därför både stabilitet och konkretion, men på olika ställen.

Grovt kan man tänka så här:

```text
Långsamt föränderliga delar
  behov
  principer
  kvalitetsdimensioner
  förmågor
        ↓
Medelsnabbt föränderliga delar
  mönster
  referensarkitekturer
  plattformstjänster
  standarder
        ↓
Snabbare föränderliga delar
  produkter
  versioner
  implementation
  konfiguration
```

Detta är inte en absolut regel. Även förmågor kan behöva förändras och vissa standarder kan vara långlivade. Men skillnaden i förändringstakt är en viktig designprincip för dokumentationen.

## Behov beskriver problemet – inte lösningen

Modellens översta lager är behovet. Ett behov beskriver något verksamheten eller ett IT-stöd behöver kunna uppnå utan att på förhand låsa teknisk realisering.

Exempel:

> En extern part ska kunna lämna in information digitalt och få kvittens på att den tagits emot.

Detta är ett behov. Det säger ännu inget om API, filöverföring, meddelandekö, webbgränssnitt eller någon viss produkt.

Ett annat exempel:

> Ett internt handläggningsstöd ska kunna fortsätta hantera prioriterade ärenden även om en enskild teknisk komponent fallerar.

Även detta beskriver ett behov. Det leder sannolikt vidare till krav på tillgänglighet, återställning och kanske redundans, men själva behovet ska inte redan innehålla lösningen.

Denna separation är central därför att behov ofta är mer långlivade än tekniken. Om behovet formuleras som ”systemet ska använda produkt X” har man hoppat över flera lager i modellen och förlorat möjligheten att värdera alternativa lösningar.

Kapitel 3 går djupare i hur behov hålls produktoberoende och hur faktiska begränsningar skiljs från krav.

## Krav och kvalitetsattribut gör behovet prövbart

Behov behöver konkretiseras för att kunna styra arkitekturen. Därför finns nästa lager: krav och kvalitetsattribut.

Ett allmänt påstående som ”systemet måste vara tillgängligt” är sällan tillräckligt. För att bli användbart behöver det uttryckas i en form som kan påverka design och verifieras.

Exempelvis kan verksamhetens tolerans för avbrott översättas till krav på återställningstid. Ett behov av spårbar handläggning kan bli krav på loggning, revisionsinformation och bevarande. Ett stort antal samtidiga användare kan bli krav på svarstid och skalbarhet under en angiven belastning.

Kvalitetsattributen fungerar därför som en bro mellan verksamhetskonsekvens och arkitekturval.

I boken används bland annat följande kvalitetsområden:

- säkerhet,
- tillgänglighet,
- kontinuitet,
- prestanda,
- skalbarhet,
- spårbarhet,
- regelefterlevnad,
- användbarhet,
- förvaltningsbarhet,
- interoperabilitet,
- livscykel,
- kostnadseffektivitet.

De är tvärgående. Säkerhet är exempelvis inte något som bara hör till identitetsområdet. Prestanda hör inte bara till runtime. Kontinuitet hör inte bara till backup. Samma kvalitet kan påverka flera förmågor och flera tekniska lager samtidigt.

Kapitel 4 fördjupar hur kvalitetsattribut formuleras, prioriteras och används som arkitekturdrivare.

## Förmågor skapar en stabil navigationsstruktur

När behov och kvalitetskrav återkommer i många lösningar behöver organisationen kunna strukturera vilket stöd IT-området ska erbjuda. Där kommer förmågorna in.

En förmåga beskriver vad det stödjande IT-området behöver kunna erbjuda stöd för, utan att förmågan binds till en viss produkt eller implementation.

Exempel är:

- Integration och kommunikation
- Identitet och tillit
- Applikationsexekvering och runtime
- Driftbarhet och motståndskraft
- Programvaruutveckling och leverans

Detta gör förmågan användbar som en relativt stabil navigationsstruktur. Om organisationen byter API-gateway, containerplattform eller identitetsprodukt behöver inte själva förmågekartan skrivas om.

Förmågan ska samtidigt inte vara så abstrakt att den saknar praktiskt innehåll. Den behöver kunna samla relevanta behov, kvalitetsfrågor, mönster, tjänsteerbjudanden och standarder inom ett begripligt ansvarsområde.

Det är därför viktigt att inte förväxla förmågan med en organisationsruta. Ett team kan ansvara för flera förmågor, och flera team kan bidra till samma förmåga. Förmågan beskriver ett arkitekturellt ansvar och ett återkommande stödbehov, inte nödvändigtvis hur organisationsträdet ser ut.

Själva förmågebegreppet och skillnaden mot verksamhetsförmåga, tjänst och produkt behandlas mer ingående i kapitel 8.

## Lösningsmönster fångar återanvändbart resonemang

En förmåga berättar fortfarande inte exakt hur ett visst problem bör lösas. Därför behövs lösningsmönster.

Ett lösningsmönster är ett återanvändbart sätt att strukturera ett återkommande och relativt avgränsat arkitekturproblem. Det beskriver inte bara den rekommenderade lösningsformen utan även när den passar, när den inte passar och vilka designfrågor som måste hanteras.

Exempel är:

- Backend for Frontend,
- asynkron meddelandekommunikation,
- publicera/prenumerera,
- human workflow,
- externaliserade verksamhetsregler,
- cache-aside,
- tjänsteidentitet,
- build once, promote many,
- observerbarhet för distribuerade tjänster.

Mönster är viktiga eftersom de bevarar mer än tekniska komponenter. De bevarar erfarenheten av hur ett problem bör tänkas igenom.

Ett mönster för asynkron kommunikation kan exempelvis påminna arkitekten om idempotens, ordering, återförsök, dead-letter-hantering, korrelation och versionshantering. Dessa frågor finns kvar även om den konkreta meddelandeprodukten byts ut.

Mönster spänner ofta över flera förmågor. Ett RAG-mönster kan beröra AI, sökning, datahantering, identitet och driftbarhet. Därför är det olämpligt att gömma ett sådant mönster som en detalj i ett enda förmågedokument.

Del IV återkommer till hur lösningsmönster utformas och används.

## Plattformstjänster gör arkitekturen konsumerbar

En modell blir inte särskilt användbar om den bara består av principer och mönster. Utvecklingsteam behöver också konkreta erbjudanden.

En plattformstjänst är därför ett återanvändbart tekniskt erbjudande som ett utvecklingsområde kan konsumera. Det kan exempelvis vara:

- en relationell databastjänst,
- API Management,
- Enterprise Messaging,
- en containerplattform,
- en identitetstjänst,
- en secrets-tjänst,
- central loggning,
- CI/CD-plattform.

Skillnaden mot en produkt är avgörande.

En containerplattform som tjänst är inte bara namnet på den programvara som används. Tjänsten behöver även beskriva vad konsumenten får, vilka kvalitetsnivåer som erbjuds, vem som ansvarar för drift och uppgraderingar, vilka begränsningar som finns och vad konsumenten själv måste göra.

Man kan därför se plattformstjänsten som ett kontrakt mellan det gemensamma IT-området och det team som bygger lösningen.

Exempel:

```text
Behov: köra containeriserad applikation med definierad tillgänglighet
        ↓
Förmåga: Applikationsexekvering och runtime
        ↓
Mönster: Containeriserad stateless tjänst
        ↓
Plattformstjänst: Container Application Platform
```

Först därefter behöver organisationen ange vilken teknisk produkt eller vilka komponenter som realiserar plattformstjänsten.

Denna skillnad gör det möjligt att behålla ett stabilt tjänsteerbjudande även när den underliggande tekniken utvecklas.

Del V fördjupar hur plattformar bör behandlas som produkter och hur tjänstekontrakt, självservice och ansvar utformas.

## Standarder begränsar variation medvetet

Plattformstjänster svarar på vad organisationen erbjuder. Standarder svarar på vilka gemensamma teknikval och konventioner som ska eller bör gälla.

En standard kan exempelvis ange:

- hur API:er ska beskrivas,
- vilka identitetsprotokoll som stöds,
- hur containerbilder ska byggas,
- vilka loggfält som krävs,
- hur releaser versionssätts,
- vilken databasprodukt som är rekommenderad inom en viss tjänst.

Det är användbart att skilja mellan flera standardnivåer:

```text
Arkitektur-/teknikstandard
        ↓
Produktstandard
        ↓
Versions- och supportstandard
        ↓
Teknisk konfiguration
```

Anta att organisationen har en containerstandard. Den kan uttrycka generella krav på hur containeriserade applikationer ska paketeras och köras. En separat produktstandard kan ange att en viss plattform är organisationens stödda realisering. En supportmatris kan ange vilka versioner som är tillåtna. Den tekniska konfigurationen beskriver sedan hur ett visst kluster faktiskt är satt upp.

Om allt detta blandas i ett dokument blir standarden snabbt både svår att förstå och svår att förvalta.

Standarder behöver dessutom vara kopplade till ett syfte. Ett teknikval som saknar relation till behov, kvalitet eller operativt värde riskerar att bli ren preferensstyrning.

Standardernas livscykel och relation till guardrails behandlas senare i boken.

## Tekniska byggblock och produkter är inte samma sak

Längst ner i realiseringskedjan finns tekniska byggblock och produkter.

Ett tekniskt byggblock är en generisk teknisk beståndsdel, exempelvis:

- operativsystem,
- databasmotor,
- reverse proxy,
- brandvägg,
- objektlagring,
- meddelandebroker,
- router.

En produkt är en konkret implementation av ett eller flera sådana byggblock.

Detta kan verka som en akademisk skillnad, men den är praktiskt viktig. Om arkitekturen uttrycker ett behov av en meddelandebroker har den fortfarande inte bestämt vilket produktnamn som ska användas. Om den uttrycker behov av ett relationellt databaslager har den ännu inte sagt vilken leverantör eller version som gäller.

Samtidigt kan samma produkt realisera flera byggblock eller flera tjänster. En omfattande plattformssvit kan innehålla identitetsfunktioner, samarbetsfunktioner, lagring och automation. Arkitekturen blir därför mer robust om den beskriver tjänsteerbjudanden och byggblock separat från produktpaketeringen.

Produkt, version och konfiguration är naturligtvis nödvändiga för en faktisk implementation. Poängen är inte att undvika dem, utan att placera dem på rätt nivå.

## Referensarkitekturen går på tvären

Alla artefakter passar inte in som ett vertikalt steg i kedjan. Referensarkitekturen är det tydligaste exemplet.

En referensarkitektur beskriver en sammanhängande rekommenderad struktur för en viss typ av lösning. Den kombinerar därför ofta flera förmågor, mönster, plattformar och standarder samtidigt.

Exempel:

```text
Förmågor + mönster + plattformar + standarder
                    ↓
           Referensarkitektur
                    ↓
            Lösningsarkitektur
```

En referensarkitektur för en publik e-tjänst kan exempelvis behöva beskriva:

- interaktion och kanaler,
- identitet,
- API-hantering,
- integration,
- datalagring,
- observerbarhet,
- säkerhetskrav,
- relevanta standarder och ansvarssnitt.

Den är alltså inte en ny förmåga och inte heller ett enskilt mönster. Den är en komposition av flera delar för en återkommande lösningstyp.

Referensarkitekturen är samtidigt inte en färdig lösningsarkitektur. En konkret e-tjänst måste fortfarande ta hänsyn till sitt verksamhetsbehov, sin informationsmodell, sina specifika kvalitetskrav och sina beroenden. Referensarkitekturen minskar startsträckan och ger en etablerad grund, men ersätter inte lösningsarkitektens analys.

Detta fördjupas i del VI.

## Spårbarhet gör modellen användbar

En arkitekturmodell blir värdefull först när man kan följa varför ett beslut finns.

Anta att ett projekt får beskedet att använda en viss gemensam tjänst. Om det enda svaret på frågan ”varför?” är att tjänsten finns på en godkänd lista är styrningen svag.

Ett bättre resonemang är möjligt om modellen ger spårbarhet:

```text
Verksamhetsbehov
    ↓
Kvalitetskrav
    ↓
Berörd förmåga
    ↓
Rekommenderat mönster
    ↓
Plattformstjänst
    ↓
Teknisk standard
    ↓
Produktrealisering
```

Exempel:

```text
Prioriterade ärenden får inte gå förlorade vid komponentfel
    ↓
Krav på återställning, spårbarhet och definierad datavaraktighet
    ↓
Driftbarhet och motståndskraft + Data- och informationshantering
    ↓
Backup och verifierad återställning
    ↓
Backup & Recovery Service
    ↓
Gemensam backup-/restore-standard
    ↓
Vald produkt och konfiguration
```

Spårbarhet betyder inte att varje pil måste dokumenteras som en tung administrativ process. Det betyder att beslutskedjan ska kunna förstås när det behövs.

Det har flera fördelar.

För det första blir avsteg lättare att bedöma. Om ett team vill välja en annan teknisk lösning kan diskussionen handla om huruvida den fortfarande uppfyller behovet och kvalitetskraven, inte bara om den avviker från ett produktnamn.

För det andra blir det lättare att förändra standarder. Om en produkt ska avvecklas kan organisationen se vilka tjänster och mönster som påverkas och vilka krav den ersättande lösningen måste uppfylla.

För det tredje blir arkitekturen mer begriplig för nya medarbetare. De kan se varför olika lager finns och hur de hänger ihop.

## Relationerna är viktigare än dokumenten

Det är lätt att göra en sådan här modell till en dokumentationsövning: ett dokument för varje förmåga, ett för varje mönster, ett för varje plattform och ett för varje standard. Men modellen blir inte bättre bara för att antalet filer ökar.

Det centrala är relationerna.

En förmåga bör kunna peka på relevanta mönster och plattformstjänster. En plattformstjänst bör kunna visa vilken förmåga den stödjer och vilka kvalitetsnivåer den erbjuder. En standard bör kunna förklaras genom vilket problem eller vilken tjänst den styr. En referensarkitektur bör kunna visa vilka delar den kombinerar.

Det är därför mer korrekt att se arkitekturen som ett nät av relaterade artefakter än som en bokhylla med fristående dokument.

I en enkel modell kan relationerna beskrivas med länkar och tabeller. I en större organisation kan samma struktur senare representeras i ett arkitekturregister, en grafdatabas eller ett dokumentationsverktyg. Verktyget är dock sekundärt. Om relationerna är otydliga hjälper inte ett mer avancerat verktyg.

## Ett konkret exempel: från e-tjänst till teknik

Anta att en myndighet ska skapa en ny publik e-tjänst där företag kan lämna uppgifter och följa sina ärenden.

Om arbetet börjar på produktnivå kan diskussionen snabbt handla om vilket frontend-ramverk, vilken databas och vilken containerplattform som ska användas. De frågorna behöver besvaras, men inte först.

Med den lagerindelade modellen kan resonemanget i stället börja högre upp.

1. Behov

Företag ska kunna identifiera sig, lämna uppgifter, få kvittens och senare se status för sina ärenden.

2. Kvalitetskrav

Tjänsten behöver bland annat vara tillgänglig under definierade perioder, skydda känslig information, ge spårbarhet för inlämnade uppgifter och klara en uppskattad toppbelastning.

3. Förmågor

Behovet berör exempelvis:

- Interaktion, presentation och kanaler
- Identitet och tillit
- Process, workflow och ärendehantering
- Integration och kommunikation
- Data- och informationshantering
- Driftbarhet och motståndskraft

4. Mönster

Beroende på lösning kan exempelvis Backend for Frontend, tjänsteidentitet, asynkron meddelandekommunikation och observerbarhet för distribuerade tjänster vara relevanta.

5. Plattformstjänster

Organisationens gemensamma erbjudanden kan sedan ge konkreta alternativ: identitetstjänst, API Management, relationsdatabastjänst, containerplattform och central loggning.

6. Standarder

API-standard, identitetsprotokoll, observerbarhetsstandard, containerstandard och release-standard kan begränsa den tekniska variationen.

7. Produkter och konfiguration

Först här behöver den konkreta realiseringen bli fullt specifik: produkt, version, miljö och konfiguration.

Detta innebär inte att processen alltid sker strikt uppifrån och ner. Ett existerande plattformserbjudande kan påverka vad som är ekonomiskt rimligt. En teknisk begränsning kan vara verklig och behöva tas med som begränsning. Ett proof of concept kan visa att ett antagande var fel.

Men lagerindelningen gör det möjligt att se vilken typ av information som påverkar vilken typ av beslut. Det minskar risken att en lokal produktbegränsning omärkligt omvandlas till ett generellt arkitekturkrav.

## En modell för navigering, inte ett nytt vattenfall

Den vertikala kedjan kan lätt misstolkas som en utvecklingsprocess där organisationen först ska färdigställa alla behov, därefter alla krav, därefter alla förmågor och så vidare.

Så är den inte avsedd.

I praktiken sker arbetet iterativt. När en plattform utvecklas upptäcks nya kvalitetsbehov. När ett lösningsmönster används i flera projekt kan en ny standard behövas. När en referensarkitektur prövas kan gränsen mellan två förmågor behöva justeras. När en produkt når slutet av sin livscykel kan ett plattformserbjudande behöva realiseras på ett nytt sätt.

Modellen beskriver därför logiska beroenden och abstraktionsnivåer, inte en engångssekvens.

Det är en viktig distinktion:

> Behov bör motivera krav, och krav bör kunna motivera arkitekturval. Men kunskapen om vilka krav och val som är rimliga utvecklas genom återkoppling från verkliga lösningar.

Det är först i kapitel 7 som boken går igenom hur denna modell kan etableras organisatoriskt och iterativt. Här räcker det att konstatera att lagren hjälper oss att hålla ordning på resonemanget även när arbetet i praktiken går fram och tillbaka mellan dem.

## Vad ska vara stabilt – och vad ska kunna bytas ut?

En bra kontrollfråga för modellen är:

> Om vi byter produkt i morgon, vilka delar av arkitekturen borde fortfarande vara giltiga?

Om svaret är ”nästan ingenting” är arkitekturen sannolikt för produktbunden.

En annan kontrollfråga är:

> Om verksamhetsbehovet förändras, vilka delar behöver vi då ompröva även om tekniken är densamma?

Om svaret är ”ingenting” är arkitekturen sannolikt för teknikcentrerad.

Det önskvärda är att stabila behov, kvaliteter, principer och förmågor kan leva längre än enskilda produkter, samtidigt som modellen är tillräckligt konkret för att styra faktisk implementation.

Det är just denna kombination som gör lagerindelningen värdefull. Den gör förändring möjlig utan att förlora sammanhang.

## Centrala fakta

- Gemensam IT-arkitektur består av flera artefakttyper som svarar på olika frågor och förändras i olika takt.
- Ett behov ska så långt som möjligt uttrycka vad som behöver uppnås utan att låsa den tekniska realiseringen.
- Krav och kvalitetsattribut gör behov prövbara och fungerar som viktiga arkitekturdrivare.
- Förmågor ger en stabil struktur för vilka återkommande typer av IT-stöd organisationen behöver kunna erbjuda.
- Lösningsmönster fångar återanvändbart arkitekturellt resonemang och kan spänna över flera förmågor.
- Plattformstjänster är konsumerbara erbjudanden och ska skiljas från de produkter som realiserar dem.
- Standarder används för att medvetet begränsa teknisk variation och bör hållas åtskilda från versions- och konfigurationsdetaljer.
- Tekniska byggblock är generiska beståndsdelar; produkter är konkreta implementationer.
- Referensarkitekturer går på tvären genom modellen och kombinerar flera förmågor, mönster, plattformar och standarder.
- Spårbarhet från behov till realisering gör det lättare att förstå beslut, hantera avsteg och byta teknik.
- Lagerindelningen är en navigations- och resonemangsmodell, inte ett strikt vattenfall.

## Begrepp att känna till

Behov – något verksamheten eller ett IT-stöd behöver kunna uppnå.

Krav – en egenskap eller ett resultat som måste uppfyllas.

Kvalitetsattribut – en tvärgående egenskap som exempelvis säkerhet, tillgänglighet, prestanda eller förvaltningsbarhet.

Förmåga – en generell typ av IT-stöd som det stödjande IT-området behöver kunna erbjuda, oberoende av viss produkt.

Lösningsmönster – ett återanvändbart sätt att strukturera ett återkommande arkitekturproblem.

Plattformstjänst – ett konkret återanvändbart erbjudande som ett utvecklingsområde kan konsumera.

Teknisk standard – ett gemensamt beslutat teknikval eller en teknisk konvention.

Tekniskt byggblock – en generisk teknisk beståndsdel som används för att realisera en eller flera tjänster.

Produkt – en konkret teknisk implementation.

Referensarkitektur – en sammanhängande rekommenderad struktur för en viss typ av lösning eller IT-stöd.

Spårbarhet – möjligheten att följa sambandet mellan behov, krav, arkitekturval och teknisk realisering.
