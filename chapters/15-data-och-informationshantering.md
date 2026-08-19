# 15. Data- och informationshantering

## Från informationsbehov till teknisk datahantering

I kapitel 11 behandlades informationens mening, ägarskap och livscykel innan teknik väljs. Det kapitlet svarade på frågor som *vad betyder informationen, vem äger den och vilken källa är auktoritativ?* Här tar vi nästa steg. Frågan är hur informationen ska realiseras tekniskt så att den kan lagras, ändras, återställas, kopieras, sökas fram och leva vidare över tid.

Det är en annan fråga än informationsmodellering. Två verksamhetsområden kan ha väl definierade begrepp och tydligt informationsägarskap men ändå behöva helt olika tekniska mekanismer. En transaktionell ärendedatabas, ett dokumentarkiv, en cache och ett sökindex hanterar alla data, men de har olika ansvar, olika livscykel och olika krav på konsistens och återställning.

Förmågan Data- och informationshantering handlar därför inte om att välja en favoritdatabas. Den handlar om att kunna översätta informationsbehov och kvalitetskrav till lämpliga lagrings- och datahanteringsmekanismer.

En användbar grundregel är:

> Välj inte lagringsteknik först. Beskriv först informationens roll, livslängd, åtkomstmönster, konsistensbehov, volym, skyddsbehov och återställningskrav.

Detta är behov-före-teknik-principen tillämpad specifikt på persistent och härledd data. Informationssemantiken från kapitel 11 tas här som ett ingångsvärde och återförklaras därför inte.

## Data är inte en enda typ av tekniskt problem

Ordet *data* används ofta som om det vore en homogen resurs. I praktiken kan en lösning samtidigt behöva hantera exempelvis:

- strukturerad transaktionell verksamhetsdata,
- dokument och större binära objekt,
- kortlivad cache,
- historiska versioner,
- referensdata,
- integrationskopior,
- sökindex,
- analyskopior,
- temporära arbetsdata,
- revisions- och auditdata.

Dessa informationsmängder kan ha helt olika tekniska egenskaper. En transaktionell datakälla kan kräva stark konsistens och tydlig transaktionsgräns. Ett sökindex kan i stället acceptera att det ligger några sekunder efter sin källa, eftersom dess uppgift är snabb informationsåtkomst och inte att vara auktoritativ källa. En cache bör ofta betraktas som förbrukningsbar och möjlig att bygga om. Ett dokument kan behöva bevaras i årtionden och överleva flera generationer av applikationer.

Det betyder att arkitekturfrågan sällan är:

> Vilken databas använder vi?

En bättre fråga är:

> Vilka typer av dataansvar finns i lösningen, och vilka tekniska mekanismer passar respektive ansvar?

## System of record och härledda kopior

När samma information förekommer på flera ställen är det centralt att skilja mellan auktoritativ källa och härledd kopia.

Ett system of record, eller en auktoritativ källa, är den plats vars tillstånd gäller när flera representationer skiljer sig åt. Det betyder inte nödvändigtvis att all information måste ligga i ett enda system. Tvärtom kan olika domäner vara auktoritativa för olika informationsmängder.

En härledd kopia kan exempelvis vara:

- en cache,
- ett sökindex,
- en replika för läsning,
- en rapporteringsdatabas,
- en materialiserad vy,
- en lokal kopia av referensdata,
- data i en analysplattform.

Kopior är alltså inte ett problem i sig. Många skalbara och användbara system är beroende av kopior. Problemet uppstår när kopians syfte, källa och återuppbyggnadsstrategi är oklara.

För varje viktig kopia bör man därför kunna svara på fyra frågor:

1. Vilken källa är auktoritativ?
2. Varför finns kopian?
3. Hur hålls den tillräckligt aktuell?
4. Vad gör vi om kopian förloras eller blir felaktig?

Den fjärde frågan är särskilt viktig. Om svaret är *vi kan återskapa den från källan* är kopian tekniskt annorlunda än data som måste återställas från backup eftersom originalet annars går förlorat.

## Relationell data – stark när relationerna och transaktionerna är viktiga

Relationella databaser är ett vanligt val för strukturerad verksamhetsdata. De är särskilt användbara när lösningen behöver:

- tydliga relationer mellan data,
- transaktioner över flera förändringar,
- integritetsregler,
- flexibla strukturerade frågor,
- konsekvent uppdatering av relaterad information.

Det betyder inte att all strukturerad data måste vara relationell. Men när verksamhetens regler uttrycker samband som måste vara sanna samtidigt är en relationell modell ofta ett naturligt alternativ.

Ett exempel kan vara en utbetalning som består av ett beslut, ett belopp, en mottagare och en bokföringspost. Om dessa förändringar måste betraktas som en sammanhängande enhet kan en transaktionell mekanism vara viktigare än maximal horisontell skalbarhet.

Det centrala är därför inte SQL som teknik, utan vilka konsistens- och transaktionsbehov verksamheten har.

### Databasen bör inte bli integrationsyta

En frestande genväg är att låta flera oberoende applikationer läsa och skriva i samma databas. Det kan fungera kortsiktigt, men skapar ofta stark koppling:

- konsumenter blir beroende av interna tabellstrukturer,
- schemaförändringar får större konsekvensyta,
- ägarskapet blir oklart,
- behörighetsmodellen blir svårare,
- domängränser suddas ut.

En gemensam relationsdatabastjänst kan därför vara mycket värdefull som plattformserbjudande, samtidigt som en gemensam databas mellan oberoende system ofta är en dålig integrationsmodell.

Detta illustrerar skillnaden mellan att standardisera en teknisk förmåga och att centralisera verksamhetsdata.

## Objektlagring för stora och binära objekt

Dokument, bilder, videofiler och andra större binära objekt har andra egenskaper än transaktionella poster. De kan vara stora, relativt sällan ändras och behöva lagras kostnadseffektivt över lång tid.

Objektlagring är då ofta ett lämpligt tekniskt mönster. Den kan ge:

- skalbar lagringskapacitet,
- enkel hantering av stora objekt,
- metadata kopplad till objekt,
- stöd för livscykelregler,
- möjlighet till redundans och geografisk distribution beroende på tjänst.

Men objektlagring löser inte hela informationsproblemet. En verksamhetslösning behöver fortfarande veta:

- vilket verksamhetsobjekt dokumentet hör till,
- vilka metadata som beskriver det,
- vem som får läsa det,
- hur länge det ska sparas,
- när det får gallras,
- vilken version som gäller.

Det är därför vanligt att den strukturerade metadatarelationen hanteras separat från själva binärinnehållet.

Objektlagring ska inte heller förväxlas med ett dokumenthanteringssystem. Ett dokumenthanteringssystem kan ha funktioner för klassificering, versionshantering, arbetsflöde, bevarande och användarinteraktion som ligger långt utanför ren lagring.

## Cache – snabbare åtkomst med medveten inkonsistens

Cache används för att minska svarstid eller avlasta en bakomliggande källa. Den är särskilt användbar när samma data läses ofta men förändras mer sällan.

Men cache innebär nästan alltid en ny fråga: hur länge får kopian vara fel?

Det är där cachearkitekturen börjar. Viktiga frågor är exempelvis:

- Vilken TTL, *time to live*, är rimlig?
- Hur sker invalidation?
- Vad händer om invalidation misslyckas?
- Får användaren se gammal data?
- Vad händer vid cachemiss?
- Ska cache kunna byggas om automatiskt?
- Innehåller cachen skyddsvärd information?

Ett vanligt mönster är cache-aside. Applikationen läser först från cache. Om värdet saknas hämtas det från auktoritativ källa och läggs i cachen. Mönstret är enkelt, men ställer krav på hur utgången data hanteras.

En viktig princip är:

> Cache ska normalt inte vara den enda plats där verksamhetskritisk persistent information finns.

Om förlust av cachen innebär permanent informationsförlust är den inte längre bara en cache.

## Konsistens är ett verksamhetskrav innan det är en databaskonfiguration

Konsistens diskuteras ofta som en teknisk egenskap, men rätt nivå måste härledas från verksamhetskonsekvensen.

För vissa data är det acceptabelt att en kopia ligger efter källan. Ett sökresultat som uppdateras några sekunder senare kan vara fullt tillräckligt. För andra data kan ett gammalt värde leda till felaktiga beslut, dubbel utbetalning eller brott mot ett styrande krav.

Frågan är därför inte bara om lösningen är *starkt* eller *eventuellt* konsistent. Man behöver beskriva:

- vilka informationsmängder som måste ändras atomärt,
- vilka kopior som får släpa efter,
- hur länge de får släpa efter,
- vilka fel som kan uppstå vid konflikt,
- vem eller vad som löser konflikten.

### Transaktionsgränser bör följa ansvar

Ju större transaktionsgräns, desto starkare koppling mellan komponenterna. Att kräva en enda atomär transaktion över flera oberoende system kan göra arkitekturen dyr och svårföränderlig.

Därför är en central designfråga:

> Vilket tillstånd måste faktiskt vara konsistent som en enhet?

Om två förändringar hör till samma domänansvar kan en lokal transaktion vara rimlig. Om de tillhör oberoende domäner behöver lösningen ofta acceptera att förändringen sker i flera steg och hantera mellanlägen explicit.

Detta är en brygga mot kapitel 17 om integration och kommunikation, där meddelanden, events och asynkrona mönster behandlas mer i detalj.

## Historik är inte samma sak som backup

Begreppen historik, audit och backup blandas ofta ihop.

Historik behövs när verksamheten vill förstå hur informationen förändrats över tid. Det kan handla om tidigare versioner, giltighetsperioder eller statusförändringar.

Auditdata behövs när man vill kunna svara på vem eller vad som utförde en förändring, när den skedde och eventuellt varför.

Backup är en återställningsmekanism för att hantera teknisk förlust eller korruption.

En backup är därför normalt inte en lämplig verksamhetsfunktion för att visa hur ett ärende såg ut för tre månader sedan. Och en auditlogg är inte automatiskt en tillräcklig backupstrategi.

När historik behövs bör man välja modell medvetet. Några vanliga alternativ är:

- versionskolumner eller giltighetsintervall,
- separata historiktabeller,
- förändringsloggar,
- immutable records för vissa typer av data,
- event sourcing i de fall där händelsehistoriken verkligen är domänens primära modell.

Event sourcing kan ge mycket rik historik, men innebär också en annan mental och teknisk modell. Det bör därför inte införas enbart för att ”vi behöver audit”.

## Retention, bevarande och gallring måste byggas in

Information lever inte för evigt bara för att lagringskostnaden är låg. Samtidigt får information inte gallras bara för att den är tekniskt gammal.

Retention och gallring måste härledas från verksamhetsbehov, rättsliga krav, informationsklassning och arkivkrav. Den tekniska lösningen behöver därefter kunna realisera reglerna.

Det kan innebära att lösningen behöver:

- märka data med relevanta livscykelmetadata,
- identifiera när retentionstiden börjar räknas,
- skilja mellan aktiv data och långtidsbevarande,
- kunna gallra selektivt,
- hantera kopior och index samtidigt,
- dokumentera undantag och legal hold-liknande situationer där gallring tillfälligt stoppas,
- verifiera att gallring faktiskt genomförts där det krävs.

Det viktiga är att livscykeln gäller hela informationslandskapet. Om originalet gallras men samma information ligger kvar i cache, analyskopior och testmiljöer är livscykeln inte konsekvent hanterad.

## Schemaförändringar är en del av systemets livscykel

Persistent data överlever ofta många versioner av applikationskoden. Därför är schemaevolution en central arkitekturfråga.

En förändring kan exempelvis innebära att:

- en kolumn läggs till,
- ett fält byter betydelse,
- data delas upp i nya strukturer,
- ett kodverk ersätts,
- ett gammalt fält tas bort,
- stora datamängder måste migreras.

Det är riskfyllt att behandla sådana förändringar som en engångsaktivitet vid driftsättning. I system med krav på hög tillgänglighet behöver schema och kod ibland kunna samexistera under en övergångsperiod.

En robust strategi kan därför innehålla steg som:

1. introducera en bakåtkompatibel struktur,
2. driftsätta kod som kan hantera både gammal och ny representation,
3. migrera befintlig data,
4. verifiera resultatet,
5. börja använda den nya representationen fullt ut,
6. ta bort den gamla först när beroendena är borta.

Detta illustrerar att dataförvaltning och releasehantering hänger samman, även om CI/CD-förmågan behandlas senare i kapitel 21.

## Migration mellan plattformar måste planeras innan den behövs

Tekniska plattformar har kortare livslängd än många informationsmängder. Data som skapas idag kan behöva vara begriplig och åtkomlig långt efter att nuvarande databasprodukt eller lagringsplattform är avvecklad.

Därför är portabilitet en viktig men ofta förbisedd kvalitet.

Det innebär inte att all data alltid måste ligga i ett helt leverantörsneutralt format. Det betyder däremot att organisationen bör förstå:

- hur data exporteras,
- vilka metadata som krävs för att tolka exporten,
- hur binära objekt och relationer återskapas,
- vilka produktunika funktioner som används,
- hur lång tid en migrering realistiskt kan ta,
- vilka beroenden som måste brytas före teknikbyte.

En standardiserad databastjänst kan alltså vara mycket värdefull samtidigt som arkitekturen undviker onödig inlåsning.

## Backup och återställning börjar med dataförlustens konsekvens

Backup nämns ofta som en teknisk checkruta: *databasen backas upp varje natt*. Det säger väldigt lite om verksamhetens faktiska återställningsförmåga.

Frågan bör i stället börja med konsekvensen:

- Hur mycket data får gå förlorad?
- Hur länge får informationen vara otillgänglig?
- Måste enskilda objekt kunna återställas?
- Måste hela tjänsten återställas till en konsistent tidpunkt?
- Hur hanteras beroenden mellan flera datakällor?
- Hur verifieras att backupen faktiskt går att använda?

Här möts dataförmågan och förmågan Driftbarhet och motståndskraft. Dataområdet behöver uttrycka vad informationen kräver. Den gemensamma driftförmågan kan sedan erbjuda backup-, replikerings- och återställningstjänster som uppfyller olika profiler.

Detta är ett bra exempel på varför förmågekartan inte innebär isolerade silor. Ett informationskrav kan behöva realiseras av flera förmågor tillsammans.

## Replikering är inte backup

Replikering kan höja tillgängligheten genom att flera kopior finns samtidigt. Men om en felaktig ändring, korruption eller oavsiktlig radering replikeras till alla kopior har man fortfarande förlorat korrekt data.

Backup och replikering har därför olika syften:

- replikering hjälper främst vid komponent- eller platsfel och kan stödja tillgänglighet,
- backup hjälper till att återgå till ett tidigare korrekt tillstånd efter förlust eller korruption.

En robust lösning kan behöva båda.

## Kryptering och åtkomst ska följa informationens skyddsbehov

Data är ofta det som ytterst ska skyddas. Därför måste datahanteringen kopplas till informationsklassning och tillit.

Viktiga frågor är exempelvis:

- Vilka identiteter får läsa eller förändra informationen?
- Behöver data krypteras i vila?
- Hur hanteras nycklar?
- Behöver åtkomst loggas?
- Kan administratörer läsa verksamhetsdata?
- Får data lämna en viss miljö eller jurisdiktion?
- Hur hanteras data i backup, repliker och testmiljöer?

Identitet, autentisering och tjänsteidentitet behandlas i kapitel 18. Här är poängen att dataförmågan måste uttrycka skyddsbehovet och se till att skyddet omfattar hela datans livscykel, inte bara den primära databasen.

## Testdata är också dataarkitektur

Produktionsdata kopieras ofta till test- och utvecklingsmiljöer eftersom realistiska datamängder underlättar felsökning och prestandatest. Men detta kan skapa en ny skyddsyta och nya livscykelproblem.

Organisationen behöver därför ta ställning till exempelvis:

- om produktionsdata alls får användas utanför produktion,
- om data måste maskeras eller syntetiseras,
- vilka identiteter som får åtkomst,
- hur länge testkopior får leva,
- hur de gallras,
- hur reproducerbara testfall skapas utan känsliga uppgifter.

Det är ett exempel på att teknisk bekvämlighet inte får skapa oavsiktliga informationskopior utan definierat syfte.

## Data nära domänansvaret

Kapitel 10 etablerade att domängränser och ansvar är viktigare än en organisationsgemensam datamodell. Samma princip bör normalt styra teknisk lagring.

Verksamhetsdata bör i regel ägas nära den domän eller tjänst som ansvarar för dess betydelse och förändring. Det minskar risken att flera oberoende lösningar börjar skriva direkt i samma data och därmed blir hårt kopplade.

Det innebär inte ”en fysisk databas per mikrotjänst” som dogm. Principen handlar om ägarskap och förändringsmandat, inte om antal serverinstanser.

Flera logiska databaser kan tekniskt ligga på samma förvaltade plattform. Samtidigt kan en stor monolitisk applikation ha flera tydliga domänansvar trots en gemensam databas. Arkitekturfrågan är vem som äger modellen och vilka gränser andra konsumenter måste respektera.

## Gemensamma plattformstjänster utan gemensam verksamhetsdata

Ett stödjande IT-område kan med stor fördel erbjuda standardiserade datatjänster, exempelvis:

- relationell databastjänst,
- objektlagring,
- cachetjänst,
- dokumentlagring,
- referens- eller masterdatatjänster i de fall där behovet verkligen är gemensamt,
- migrerings- och backupstöd.

En förvaltad relationsdatabastjänst kan exempelvis ansvara för:

- databasinstans,
- patchning,
- teknisk hög tillgänglighet,
- monitorering,
- backup enligt vald profil,
- etablerade anslutningsmönster.

Konsumenten kan samtidigt ansvara för:

- datamodell,
- schema,
- migrationslogik,
- index- och frågedesign,
- informationsklassning,
- korrekt användning av transaktioner.

Detta är ett viktigt tjänstekontrakt. Plattformsteamet kan göra det enkelt att få en robust databas utan att behöva äga verksamhetens data eller dess semantik.

## Kvalitetskrav för dataförmågan

### Korrekthet och konsistens

Data måste vara tillräckligt korrekt och konsistent för sitt verksamhetssyfte. Kravet varierar mellan informationsmängder och får inte reduceras till en generell produktinställning.

### Tillgänglighet

Vissa data måste vara tillgängliga även när delar av infrastrukturen fallerar. Andra kan tåla längre avbrott. Tillgänglighetsprofilen bör därför härledas från verksamhetskonsekvensen.

### Kontinuitet och återställningsförmåga

Organisationen behöver förstå acceptabel dataförlust, återställningstid och hur återställning verifieras. Backup utan testad restore är en ofullständig förmåga.

### Prestanda

Åtkomstmönster påverkar datamodell, indexering, cache och ibland val av lagringsmekanism. Ett system med mycket skrivningar har andra behov än ett system med komplexa läsfrågor.

### Skalbarhet och kapacitet

Datamängder växer över tid. Kapacitetsplanering måste därför inkludera både primär data, historik, index, repliker och backup – inte bara dagens aktiva databas.

### Säkerhet och informationsskydd

Skyddsnivån ska följa informationens klassning och omfatta primärkällor, kopior, backup och testdata.

### Spårbarhet

Vissa verksamheter behöver kunna visa tidigare tillstånd, förändringshistorik och vem som utfört en förändring. Detta bör designas explicit i stället för att hoppas att tekniska loggar räcker.

### Förvaltningsbarhet och förändringsbarhet

Schema, migrering och teknikbyte är normala delar av livscykeln. Datadesign som bara fungerar för den första releasen är inte hållbar.

### Portabilitet

Data lever ofta längre än den produkt som lagrar den. Export- och migreringsförmåga kan därför vara en viktig kvalitet även när ett teknikbyte inte är nära förestående.

### Kostnadseffektivitet

All data behöver inte ligga på den dyraste och snabbaste lagringsnivån. Historik, backup och binära objekt kan ha andra profiler än aktiv transaktionell data.

## Ansvar på tre nivåer

### Gemensam arkitektur

På gemensam nivå bör organisationen definiera de principer som måste hålla ihop flera förmågor och lösningar. Det kan omfatta:

- krav på tydlig auktoritativ källa,
- principer för kopior och återuppbyggnad,
- gemensamma kvalitetsprofiler för backup och tillgänglighet,
- regler för informationsklassning och skydd,
- principer för portabilitet och livscykel,
- gränsen mellan datahantering, integration, analys och drift.

Den gemensamma nivån bör däremot normalt inte designa varje lösnings datamodell.

### Förmågeområde

Förmågeansvaret för Data- och informationshantering bör utveckla konsumerbart stöd som:

- databas- och lagringstjänster,
- vägledning för transaktioner och konsistens,
- mönster för cache och härledda kopior,
- standardiserade backup-/restore-profiler tillsammans med driftförmågan,
- migreringsstöd,
- standarder för tekniska dataformat och persistence där det ger nytta,
- tydliga ansvarskontrakt mellan konsument och plattform.

Förmågeområdet bör också följa vilka lokala speciallösningar som återkommer. Om många team bygger samma typ av datatjänst kan det vara en signal om ett saknat gemensamt erbjudande.

### Lösning eller produkt

Den konkreta lösningen måste fortfarande fatta beslut om:

- vilka data den äger,
- vilken lagringsmodell som passar,
- schema och index,
- transaktionsgränser,
- cachebehov,
- historik,
- retention,
- migrationsstrategi,
- vilka kopior som är tillåtna,
- hur kvalitetskraven verifieras.

Gemensamma plattformar kan minska mängden tekniskt arbete, men de kan inte ersätta domänspecifik datadesign.

## Vanliga anti-patterns

### Databasen väljs före behovet

”Vi använder alltid produkt X” blir utgångspunkt innan informationens egenskaper är analyserade. Resultatet kan fungera men leda till onödig komplexitet, kostnad eller inlåsning.

### Den gemensamma databasen

Flera oberoende system delar schema och skriver direkt i varandras tabeller. Den tekniska enkelheten blir en långsiktig kopplingskostnad.

### Cache som permanent sanning

En cache börjar användas för unik verksamhetsdata eftersom den är snabb och enkel. Först vid fel upptäcks att återuppbyggnad saknas.

### Backup som historik

Verksamheten behöver kunna se tidigare tillstånd men lösningen förlitar sig på backup. Återställningskopior blir då ett opraktiskt och riskfyllt sätt att uppfylla ett funktionellt historikbehov.

### Replikering som backup

Flera samtidiga kopior antas skydda mot all dataförlust, trots att logiska fel och raderingar kan replikeras till samtliga.

### Kopior utan ägare

Data exporteras till filer, index, analysmiljöer och testmiljöer utan tydlig livscykel. Ingen vet vilka kopior som måste uppdateras eller gallras.

### Permanent temporär data

”Tillfälliga” tabeller, köer eller filer saknar ägare och retention och blir efter några år en kritisk del av systemet.

### Schemaförändring som driftsättningsdetalj

Migrering planeras först när releasen redan är färdig. Stor datamängd, lång körningstid eller bakåtkompatibilitet upptäcks för sent.

### Produktformat som informationsmodell

Verksamhetens långsiktiga data blir så beroende av produktens interna representation att export och migrering kräver ett eget räddningsprojekt.

## En praktisk analysordning

När en lösning eller förmåga ska utforma sin datahantering kan följande ordning användas.

### 1. Identifiera informationsmängderna

Beskriv vilken information lösningen ansvarar för och vilka mängder som bara är kopior eller referenser.

### 2. Fastställ auktoritativ källa

För varje viktig informationsmängd: vilken komponent eller domän har mandat att ändra sanningen?

### 3. Beskriv livslängden

Är informationen kortlivad, långlivad eller arkivvärd? När börjar retention räknas och när får den gallras?

### 4. Beskriv åtkomstmönstren

Hur ofta läses och skrivs data? Behövs relationsfrågor, stora objekt, fulltextsökning eller mycket snabb nyckelåtkomst?

### 5. Definiera konsistenskraven

Vilka förändringar måste vara atomära? Vilka kopior får vara fördröjda och hur länge?

### 6. Definiera historik- och spårbarhetsbehov

Behövs tidigare tillstånd, audit eller båda? Hur länge ska historiken finnas?

### 7. Definiera skyddsbehovet

Klassning, åtkomst, kryptering, datalokalitet och loggning ska vara kända innan data sprids till flera tekniska lager.

### 8. Definiera återställningskraven

Beskriv acceptabel dataförlust, återställningstid och vilken granularitet återställningen behöver ha.

### 9. Identifiera tillåtna kopior

Cache, index, repliker och analyskopior ska ha syfte, källa, synkronisering och livscykel.

### 10. Välj teknisk mekanism

Först nu är det rimligt att välja exempelvis relationell databas, objektlagring, cache eller andra datahanteringstjänster.

### 11. Planera schemaevolution och migrering

Beskriv hur data och kod ska kunna förändras utan oacceptabla driftstopp eller informationsförlust.

### 12. Verifiera hela livscykeln

Testa inte bara att data kan skrivas och läsas. Verifiera även backup, restore, gallring, migration och återuppbyggnad av sekundära kopior.

## Förmågan som konsumerbart stöd

En mogen dataförmåga känns inte igen på antalet databaser som driftas. Den känns igen på hur enkelt ett utvecklingsteam kan uttrycka sina behov och få ett lämpligt, säkert och förvaltat stöd.

Ett bra erbjudande kan exempelvis låta ett team välja mellan dokumenterade kvalitetsprofiler för en relationsdatabastjänst:

- standardprofil för normal verksamhetskritikalitet,
- högre tillgänglighetsprofil,
- särskild backup-/retentionprofil,
- definierade kapacitetsnivåer.

Tjänsten bör samtidigt vara tydlig med vad den inte löser. Plattformen kan exempelvis tillhandahålla backup och teknisk HA, men konsumenten ansvarar fortfarande för att datamodell, retention och återställningskrav är korrekta för verksamheten.

På samma sätt kan en objektlagringstjänst erbjuda robust lagring men inte automatiskt bli ett dokumenthanteringssystem, och en cachetjänst kan erbjuda snabb åtkomst men inte ta ansvar för verksamhetens sanning.

Det är denna tydliga ansvarsfördelning som gör ett tekniskt byggblock till en användbar plattformstjänst.

## Sammanfattning

Data- och informationshantering som gemensam IT-förmåga handlar inte primärt om databasteknik. Den handlar om att kunna realisera informationens behov genom rätt kombination av lagring, konsistens, historik, kopior, retention, återställning och förändringsförmåga.

Några huvudprinciper är särskilt viktiga:

- informationsbehov ska komma före lagringsteknik,
- auktoritativ källa ska vara tydlig,
- kopior ska ha definierat syfte och livscykel,
- cache, repliker och backup har olika roller,
- historik ska inte förväxlas med återställning,
- retention och gallring måste omfatta hela informationslandskapet,
- schemaevolution och migrering är normala livscykelproblem,
- verksamhetsdata bör normalt ägas nära sitt domänansvar,
- gemensamma dataplattformar ska standardisera mekanismer utan att ta över verksamhetens semantik.

När dessa principer är tydliga blir teknikvalet enklare. Då kan relationell databas, objektlagring, cache och andra tjänster väljas som svar på kända behov i stället för som utgångspunkt för arkitekturen.

Nästa kapitel flyttar perspektivet från lagring och informationslivscykel till hur data används för analys, sökning och AI. Där blir många av de här principerna fortfarande avgörande: ett sökindex, en analyskopia eller en RAG-lösning är bara så tillförlitlig som den informationsgrund och den kopplingsmodell som ligger bakom den.
