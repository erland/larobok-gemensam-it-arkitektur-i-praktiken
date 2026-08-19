# 17. Integration och kommunikation

Nästan inget modernt verksamhetsstöd är helt självständigt. Ett system behöver hämta information från ett annat, publicera en händelse, skicka ett meddelande, överföra en fil eller kommunicera med en extern organisation. Även en lösning som är väl avgränsad internt blir därför en del av ett större nät av beroenden.

Det gör integration till mer än en teknisk transportfråga.

När två självständiga lösningar kopplas samman uppstår beroenden i tid, kontrakt, semantik, tillgänglighet, säkerhet och förändringstakt. Valet mellan API, meddelanden, events och filutbyte avgör därför inte bara hur information flyttas. Det påverkar hur lösningarna kan utvecklas, hur fel sprids, vem som äger initiativet och hur lätt sambandet går att förstå och förvalta.

Kärnfrågan i kapitlet är:

> **Vilken kommunikationsform passar behovet – och vilken koppling mellan parterna är vi beredda att acceptera?**

Kapitlet handlar om den gemensamma IT-förmågan **Integration och kommunikation**. Fokus ligger på informationsutbyte mellan självständiga lösningar och på de mekanismer som kan göras gemensamma. Verksamhetsmässig processorkestrering behandlades i kapitel 13. Informationsägarskap och datalivscykel behandlades i kapitel 11 och 15. Identitet och tillit kommer i kapitel 18.

## Integration är ett beroende mellan självständiga parter

Det är lätt att beskriva integration som en pil mellan två rutor:

```text
System A  ───────▶  System B
```

Men pilen döljer de viktigaste frågorna.

För att kommunikationen ska fungera måste parterna vara överens om åtminstone delar av följande:

- vad informationen betyder,
- vilket format eller kontrakt som används,
- vem som initierar kommunikationen,
- om svar krävs omedelbart,
- hur fel uttrycks,
- vad som händer när mottagaren inte är tillgänglig,
- hur förändringar versioneras,
- vilka säkerhetsmekanismer som krävs,
- hur flödet kan följas vid felsökning.

Integration är därför en **förvaltningsbar relation** mellan två eller flera ansvariga parter.

Detta blir särskilt viktigt när parterna har olika livscykel. Två komponenter inom samma kodbas kan ofta ändras samtidigt. Två självständiga system, kanske med olika produktteam eller organisationer, kan inte förutsättas göra det.

En robust integrationsarkitektur behöver därför stödja självständighet snarare än att i onödan göra lösningarna till en distribuerad monolit.

## Börja med kommunikationsbehovet

Precis som i resten av boken bör lösningsvalet inte vara utgångspunkten.

Frågan är inte först:

> Ska vi använda REST, en meddelandekö eller Kafka?

Frågan är exempelvis:

> Behöver avsändaren svar innan arbetet kan fortsätta?

eller:

> Behöver mottagaren kunna vara otillgänglig när informationen skickas?

eller:

> Ska flera oberoende konsumenter kunna reagera på att något har hänt?

Några centrala dimensioner är:

- **synkronicitet** – krävs ett svar i samma interaktion?
- **tidskoppling** – måste producent och konsument vara tillgängliga samtidigt?
- **riktning** – är det en begäran, ett meddelande, en händelse eller ett informationspaket?
- **antal parter** – finns en mottagare eller potentiellt många?
- **volym** – handlar det om små enskilda meddelanden eller stora datamängder?
- **leveranskrav** – vad händer om informationen inte når fram direkt?
- **ordning** – spelar det roll i vilken sekvens meddelanden behandlas?
- **aktualitet** – hur gammal får informationen bli?
- **koppling** – hur mycket behöver avsändaren känna till om mottagaren?
- **förvaltningsgräns** – kan parterna förändras och driftsättas oberoende?

Dessa frågor gör det möjligt att välja mönster efter behov i stället för efter teknisk vana.

## Synkron kommunikation – när svaret behövs nu

Vid synkron kommunikation skickar en konsument en begäran och väntar på ett svar innan den kan fortsätta.

Det är ofta ett naturligt val när:

- en användare väntar på resultatet,
- aktuell information måste hämtas,
- ett kommando behöver bekräftas direkt,
- transaktionen logiskt kräver omedelbar återkoppling.

Ett typiskt exempel är ett API-anrop:

```text
Klient ── begäran ──▶ Tjänst
       ◀── svar ─────
```

Modellen är enkel att förstå, men den skapar **tidskoppling**. Konsumenten är beroende av att tjänsten kan svara inom en rimlig tid just när anropet görs.

Om tjänst B i sin tur anropar C och D kan beroendekedjan snabbt bli längre:

```text
A → B → C → D
```

Tillgängligheten i hela användarflödet påverkas då av samtliga kritiska beroenden. Latens summeras och fel kan spridas bakåt genom kedjan.

Det betyder inte att synkrona API:er är fel. De är ofta precis rätt. Men man bör använda dem med förståelse för vilken operativ koppling de skapar.

### Timeout är en del av kontraktet

Ett synkront anrop får aldrig i praktiken antas kunna vänta obegränsat.

En lösning behöver veta:

- hur länge den väntar,
- vad en timeout betyder,
- om anropet kan provas igen,
- om operationen kan ha genomförts trots att svaret förlorades,
- vilket beteende användaren eller processen får vid fel.

Retry är därför inte automatiskt säkert.

Om ett anrop betyder ”skapa betalning” och klienten inte vet om första försöket lyckades kan ett blint nytt försök skapa en dublett. För vissa operationer behöver kontraktet därför stödja **idempotens** eller någon annan mekanism som gör upprepning kontrollerad.

## Asynkron meddelandekommunikation – när parterna inte behöver mötas i tid

Vid asynkron kommunikation skickas information utan krav på att mottagaren behandlar den omedelbart medan avsändaren väntar.

En mellanliggande meddelandetjänst kan exempelvis lagra meddelandet tills konsumenten kan ta hand om det:

```text
Producent ──▶ Kö ──▶ Konsument
```

Detta kan minska tidskopplingen mellan parterna. Producenten behöver inte nödvändigtvis vara beroende av att konsumenten är tillgänglig just då.

Asynkron kommunikation passar exempelvis när:

- arbetet kan ske senare,
- mottagaren behöver kunna vara tillfälligt otillgänglig,
- belastning behöver jämnas ut,
- robust leverans är viktigare än omedelbart svar,
- processen naturligt består av flera steg över tid.

Men robustare tidskoppling innebär inte mindre designarbete. Tvärtom flyttas flera frågor från det omedelbara anropet till meddelandeflödet.

Man behöver bland annat ta ställning till:

- hur omleverans fungerar,
- hur dubbletter hanteras,
- om ordning behöver bevaras,
- vad som händer efter upprepade misslyckanden,
- hur gamla meddelanden får bli,
- hur konsumenten återstartas efter avbrott,
- hur ett meddelande kan spåras genom flödet.

### Leveransgarantier behöver förstås i sitt sammanhang

Begrepp som *at-most-once*, *at-least-once* och *exactly-once* används ofta när meddelandesystem diskuteras. De kan vara användbara, men de får inte ersätta analysen av hela affärsoperationen.

En infrastruktur kan ge starka garantier inom sin egen gräns, men den verksamhetsmässiga effekten kan involvera databasuppdateringar, externa system och andra komponenter.

Den viktigaste frågan blir därför ofta:

> **Hur säkerställer vi korrekt verksamhetsutfall när ett meddelande kan behandlas mer än en gång eller när utfallet efter ett fel är osäkert?**

Idempotent behandling, deduplicering och tydliga transaktionsgränser blir då centrala mekanismer.

## Meddelande och händelse är inte samma sak

Asynkron teknik används ofta både för **meddelanden** och **events**, men semantiken skiljer sig.

Ett riktat meddelande kan uttrycka ett önskat arbete:

```text
SkapaFraktuppdrag
```

En händelse uttrycker i stället något som redan har inträffat:

```text
OrderGodkänd
```

Skillnaden är viktig eftersom den påverkar ansvar.

Ett kommando har normalt en tänkt mottagare som förväntas göra något. En händelse publiceras av den som äger faktumet och behöver inte känna till vilka konsumenter som reagerar.

Det ger en användbar princip:

> **Events bör beskriva fakta som producenten äger, inte fungera som dolda fjärrkommandon till specifika konsumenter.**

Om ett event i praktiken betyder ”System B måste nu göra X” och producenten är beroende av detta för att kunna fortsätta, finns fortfarande en stark verksamhetsmässig koppling även om tekniken råkar vara pub/sub.

Teknisk asynkronicitet är alltså inte samma sak som arkitekturell lös koppling.

## Publicera/prenumerera – när flera konsumenter kan reagera

I ett publicera/prenumerera-mönster publiceras en händelse eller ett meddelande till ett ämne eller en kanal där flera konsumenter kan prenumerera.

```text
             ┌──▶ Konsument A
Producent ──▶ Topic ──▶ Konsument B
             └──▶ Konsument C
```

Det kan minska producentens kunskap om konsumenterna. Nya konsumenter kan ibland läggas till utan att producenten förändras.

Det passar särskilt väl när:

- samma händelse är relevant för flera oberoende parter,
- producenten inte ska orkestrera deras arbete,
- konsumenterna har egna ansvar och livscykler.

Men pub/sub skapar nya frågor:

- hur vet man vilka konsumenter som faktiskt finns?
- vad händer om en konsument tolkar händelsen fel?
- hur förändras eventets kontrakt över tid?
- hur länge behöver gamla konsumentversioner stödjas?
- kan en ny konsument återskapa historik eller bara se nya events?

Lös koppling betyder alltså inte frånvaro av kontrakt. Tvärtom behöver kontraktet ofta vara ännu mer stabilt när producent och konsument inte koordinerar varje förändring.

## API:er – kontrakt, inte bara endpoints

Ett API bör inte reduceras till en teknisk URL och ett antal HTTP-anrop. Det är ett **förvaltat kontrakt** mellan parter.

Ett bra API-kontrakt behöver göra relevanta delar tydliga:

- operationer och resurser,
- informationsmodell och semantik,
- valideringsregler,
- felmodell,
- autentiserings- och auktorisationskrav,
- versionsstrategi,
- begränsningar kring trafik och användning,
- livscykel och avveckling.

Det finns också en viktig gräns mellan API och intern implementation.

Om konsumenter blir beroende av interna tabeller, filstrukturer eller tekniska datamodeller förlorar producenten möjligheten att förändra implementationen självständigt.

Direkt databasåtkomst mellan självständiga IT-stöd är därför normalt ett varningstecken som integrationsmodell.

Det betyder inte att databaser aldrig delas tekniskt. Men om två självständiga ansvar använder samma interna lagringsmodell som sitt primära kontrakt har man skapat en stark koppling som behöver vara medvetet motiverad.

## API management är inte detsamma som integrationsarkitektur

En organisation kan erbjuda en gemensam API Management-tjänst med exempelvis:

- exponering av API:er,
- policy enforcement,
- autentiseringskopplingar,
- trafikbegränsning,
- statistik,
- utvecklarportal eller katalogfunktioner.

Det kan ge stor nytta.

Men en API gateway kan inte avgöra:

- vad tjänstegränsen bör vara,
- vem som äger informationen,
- om kommunikationen borde vara synkron,
- hur kontraktet bör utformas verksamhetsmässigt,
- hur en domän bör delas upp.

Detta illustrerar bokens generella modell. Plattformen realiserar återkommande mekanismer. Arkitekturansvaret för behov, ansvar och gränser finns fortfarande kvar.

## Filutbyte är fortfarande integration

Filbaserad integration beskrivs ibland som gammaldags och ersättningsbar med API:er. Det är en för enkel bild.

Filer kan vara ett lämpligt val när:

- stora informationsmängder överförs i batch,
- mottagaren arbetar periodiskt,
- externa parter har etablerade filbaserade kontrakt,
- formatet i sig är en definierad leveransenhet,
- direkt interaktiv kommunikation inte behövs.

En filöverföring behöver ändå behandlas som ett förvaltat kontrakt.

Man behöver exempelvis definiera:

- format och schema,
- namngivning,
- fullständig eller inkrementell leverans,
- kontrollsummor eller andra integritetsmekanismer,
- kvittens,
- felhantering,
- kryptering och åtkomst,
- retention och borttagning,
- hur omleverans skiljs från en ny leverans.

Problemet med filintegration är alltså inte att den använder en fil. Problemet uppstår när filen blir ett odokumenterat tekniskt sidospår utan tydligt ägarskap och livscykel.

## Dataförflyttning och integration är närliggande men inte identiska

ETL, replikering och andra former av dataförflyttning ligger nära integration. Men syftet kan vara ett annat.

Ett operativt API kan tillhandahålla aktuell information för en affärstransaktion. Ett ETL-flöde kan i stället kopiera stora mängder data till ett analyslager.

Båda flyttar information, men de har olika krav på exempelvis:

- aktualitet,
- transaktionell semantik,
- volym,
- historik,
- felhantering,
- återkörning.

Det är därför användbart att fråga om flödet primärt är:

1. **tjänsteintegration** – funktionalitet eller aktuell information används mellan lösningar,
2. **händelse-/meddelandeintegration** – fakta eller arbete distribueras asynkront,
3. **dataförflyttning** – datamängder kopieras eller transformeras för ett annat ändamål.

Gemensamma integrationsförmågor kan stödja alla tre, men bör inte tvinga dem genom samma tekniska mekanism.

## Transformation kan lösa kontraktsproblem – men också dölja dem

Integrationslager används ofta för att transformera meddelanden mellan olika format.

Det kan vara rimligt. Två system med olika externa kontrakt behöver inte ha samma interna modell.

Men transformation kan också bli ett sätt att gömma otydligt ägarskap. Om en central integrationsplattform innehåller stora mängder verksamhetslogik kan den gradvis utvecklas till en svårförvaltad mellanvärld där ingen riktigt vet vem som äger reglerna.

En bra tumregel är:

> **Integration får anpassa kontrakt och transport, men verksamhetens auktoritativa beslut och domänlogik bör ligga hos den ansvariga domänen.**

Det betyder inte att transformation måste vara trivial. Men man bör kunna förklara om en regel i integrationslagret är teknisk mappning eller verksamhetsmässig logik.

## Kontraktslivscykeln är lika viktig som tekniken

Två självständiga system kommer förr eller senare att förändras.

Därför behöver integrationskontrakt en livscykel.

En förändring kan vara:

- bakåtkompatibel,
- kompatibel endast för vissa konsumenter,
- brytande.

Exempel på ofta mindre riskfyllda förändringar kan vara att lägga till ett valfritt fält. Att ta bort ett fält, ändra dess betydelse eller byta datatyp kan däremot bryta konsumenter.

Men teknisk kompatibilitet räcker inte alltid. Ett fält kan behålla samma namn och typ men få en ny verksamhetsmässig betydelse. Då är formatet kompatibelt medan semantiken inte är det.

Versionsstrategin behöver därför behandla både:

- **syntax** – hur kontraktet ser ut,
- **semantik** – vad informationen betyder,
- **beteende** – vad producent och konsument kan förvänta sig.

### Parallella versioner har ett pris

Det är lockande att lösa alla förändringar genom att behålla gamla versioner för alltid.

Det skapar i stället en växande förvaltningskostnad.

En mogen integrationsförmåga behöver därför även stöd för:

- annonsering av förändringar,
- migrationsperioder,
- uppföljning av konsumenter,
- deprecation,
- avveckling.

API-kataloger, schemaregister eller andra kontraktskataloger kan hjälpa, men de ersätter inte ansvar mellan producent och konsument.

## Felhantering måste designas per interaktionsform

Ett tekniskt fel betyder olika saker beroende på kommunikationsmönstret.

Vid ett synkront API kan konsumenten få timeout eller felkod direkt.

Vid asynkron kommunikation kan meddelandet ligga kvar i en kö, levereras igen eller flyttas till en särskild felhanteringsmekanism efter upprepade misslyckanden.

Vid filutbyte kan en hel batch behöva avvisas, delvis accepteras eller behandlas på nytt.

Det är därför otillräckligt att säga ”plattformen hanterar retry”. Lösningen behöver definiera **verksamhetsmässigt felbeteende**.

Exempel:

```text
Tekniskt avbrott
      ↓
Meddelande kan inte behandlas
      ↓
Automatisk omleverans
      ↓
Fortsatt fel
      ↓
Parkerat felobjekt + larm
      ↓
Korrigering / beslut / kontrollerad återkörning
```

Frågan är inte bara hur infrastrukturen reagerar, utan hur verksamheten återgår till ett korrekt tillstånd.

## Ordering är ett krav – inte en standardinställning

Asynkrona flöden väcker ofta frågan om ordning.

I vissa fall är ordningen kritisk. Om ett konto först öppnas och sedan stängs kan motsatt behandlingsordning ge ett orimligt resultat.

I andra fall spelar ordningen ingen roll, och stark ordering kan då skapa onödig begränsning i skalbarhet och parallell behandling.

Man bör därför fråga:

- behöver alla meddelanden ordnas globalt?
- räcker ordning per kund, ärende eller annan nyckel?
- kan konsumenten hantera sen ankomst?
- kan tillståndet härledas från versionsnummer eller tidsstämplar?

Principen är densamma som på andra områden:

> **Beställ inte starkare tekniska garantier än behovet kräver.**

## Integration över organisationsgränser

När kommunikationen går till en annan organisation förändras flera förutsättningar.

Den andra parten kan ha:

- annan förändringstakt,
- annan säkerhetsmodell,
- andra drifttider,
- andra kontaktvägar,
- andra standarder,
- annan incidenthantering.

Det gör tjänstekontrakt och ansvar ännu viktigare.

En extern kommunikationstjänst eller myndighetsgemensam infrastruktur kan erbjuda säker transport eller strukturerat informationsutbyte. Men den löser inte automatiskt frågan om vad informationen betyder eller hur fel hanteras mellan verksamheterna.

Extern integration bör därför behandlas som **tjänstekonsumtion med definierade ansvar och begränsningar**, inte som ett anonymt nätverksflöde.

## Nätverk är en realisering av kommunikationsbehovet

På teknisk nivå kräver integration naturligtvis nätverk, DNS, routing, brandväggar, lastbalansering och andra kommunikationsmekanismer.

Men dessa bör härledas från det dokumenterade flödet.

I stället för att börja med:

> Öppna port 443 mellan zon A och zon B.

bör arkitekturen kunna förklara:

- vilken tjänst som kommunicerar,
- med vilken motpart,
- i vilken riktning,
- för vilket syfte,
- med vilken identitet,
- vilken information som överförs,
- vilka kvalitets- och säkerhetskrav som gäller.

Därefter kan nätverks- och säkerhetskontrollerna realisera behovet.

Detta gör även tekniska regler mer förvaltningsbara. En brandväggsregel utan känd tjänsterelation blir annars snabbt ett historiskt mysterium som ingen vågar ta bort.

## Säkerhet och identitet korsar integrationsförmågan

Integrationsförmågan behöver säker kommunikation, men bör inte ensam äga identitetsmodellen.

Kapitel 18 fördjupar detta. Här räcker det att konstatera att ett integrationsflöde normalt behöver kunna svara på frågor som:

- vem eller vilken tjänst är motparten?
- hur autentiseras den?
- vilken behörighet har den?
- hur skyddas information i transit?
- hur hanteras certifikat, nycklar och hemligheter?
- korsar flödet en trust boundary?

Det är ett exempel på hur förmågorna samverkar. Integration äger kommunikationsmönstret och kontraktet. Identitet och tillit erbjuder mekanismer för att avgöra vem som kommunicerar och under vilka förutsättningar.

## Observability över systemgränser

Ett fel i en distribuerad lösning kan passera flera system innan effekten märks.

Därför behöver viktiga integrationsflöden kunna korreleras över komponentgränser.

Det kan innebära:

- korrelations-id,
- strukturerad loggning,
- spårning av anrop,
- meddelandeidentifierare,
- gemensamma tidsreferenser,
- metrics för ködjup, fel och latens.

Men även här behöver ansvar hållas isär. Integrationsförmågan definierar vilka egenskaper flödet behöver. Den gemensamma förmågan för driftbarhet och motståndskraft, som behandlas i kapitel 20, tillhandahåller de bredare mekanismerna för observability och operativ återkoppling.

## Gemensamma plattformstjänster för integration

Ett större IT-område kan behöva flera gemensamma erbjudanden snarare än ”en integrationsplattform”. Exempel är:

- **API Management**,
- **Enterprise Messaging**,
- **Data Integration / ETL**,
- **Managed File Transfer** eller motsvarande funktion,
- säker extern konnektivitet,
- tjänster för strukturerat informationsutbyte.

Det viktiga är att varje erbjudande har ett tydligt tjänstekontrakt.

Konsumenten behöver veta:

- vilka behov tjänsten löser,
- vilka garantier den ger,
- vilket ansvar konsumenten fortfarande har,
- hur onboarding sker,
- hur kontrakt och versioner hanteras,
- hur tjänsten övervakas och supporteras.

Detta är samma plattform-as-a-product-perspektiv som senare fördjupas i del V.

### Undvik den universella integrationsplattformen

Ett vanligt anti-pattern är idén att all kommunikation måste gå genom en enda central produkt eller integrationsmotor.

Det kan skapa:

- teknisk och organisatorisk flaskhals,
- onödiga hopp och ökad latens,
- centraliserad verksamhetslogik,
- svår förändringskoordinering,
- en integrationsplattform som blir beroende av allt och förstås av få.

Gemensam förmåga betyder inte att alla mönster behöver realiseras i samma produkt.

En bättre målbild är ofta en **sammanhängande portfölj av standardiserade integrationsförmågor och tjänster**, där mekanism väljs efter behov.

## Ansvar på tre nivåer

Den tredelade ansvarmodellen från kapitel 7 är särskilt användbar för integration.

### Gemensam arkitekturnivå

På den gemensamma nivån bör man exempelvis fastställa:

- vilka integrationsformer organisationen ska kunna stödja,
- gemensamma principer för kontrakt och livscykel,
- övergripande säkerhets- och spårbarhetskrav,
- när gemensamma plattformstjänster ska användas,
- gemensamma interoperabilitetsstandarder där de behövs,
- hur externa kommunikationsformer ska styras.

Den gemensamma nivån bör däremot normalt inte designa varje API eller event.

### Förmågenivå

De som ansvarar för Integration och kommunikation bör exempelvis utveckla:

- lösningsmönster för synkron och asynkron integration,
- API- och meddelandestandarder,
- tjänsteerbjudanden som API management och messaging,
- kontrakts- och versionsvägledning,
- golden paths för vanliga integrationsscenarier,
- stöd för test, observability och onboarding,
- livscykel för integrationsprodukter och protokoll.

Förmågeansvaret bör också följa var utvecklingsområden återkommande skapar egna speciallösningar. Det kan vara ett tecken på att det gemensamma erbjudandet saknar något.

### Lösnings-/produktnivå

Det konkreta systemet ansvarar bland annat för:

- vilket kommunikationsbehov som finns,
- vilket mönster som passar,
- kontraktets verksamhetssemantik,
- felbeteende och idempotens,
- timeout- och retrystrategi,
- hur integrationen används i domänens process,
- att kraven på säkerhet och driftbarhet uppfylls.

Det lokala teamet ska alltså inte behöva bygga en egen meddelandeplattform. Men plattformsteamet kan inte avgöra om ett visst verksamhetsflöde borde vara ett API, ett event eller en fil.

## Vanliga anti-patterns

### Ett integrationssätt för allt

Organisationen har investerat i en viss produkt eller metod och försöker därför använda den för alla behov.

**Konsekvens:** mönstret styr problemet i stället för tvärtom.

### Direkt databasåtkomst som normal integration

Ett system läser eller skriver direkt i ett annat systems interna databas.

**Konsekvens:** stark koppling till intern implementation, otydligt ägarskap och svår förändring.

### Event som fjärrkommando

Ett så kallat event är i praktiken ett krav på att en specifik konsument ska utföra något.

**Konsekvens:** beroendet döljs i stället för att försvinna.

### Central integrationslogik

Verksamhetsregler och domänbeslut flyttas till en gemensam integrationsmotor.

**Konsekvens:** domänansvaret urholkas och integrationslagret blir svårt att förstå och förändra.

### Retry utan idempotensanalys

Tekniska fel möts med automatiska omförsök utan analys av operationens verksamhetsmässiga effekt.

**Konsekvens:** dubletter och inkonsistenta resultat.

### Versioner som aldrig avvecklas

Nya kontraktsversioner läggs till men gamla konsumenter migreras aldrig.

**Konsekvens:** växande kompatibilitetsbörda och långsammare förändring.

### Nätverksregel utan tjänsteägare

Kommunikation öppnas tekniskt men saknar dokumenterat syfte och ansvar.

**Konsekvens:** svårstyrd säkerhetsyta och historiska beroenden som ingen kan värdera.

## En praktisk analysordning

När ett integrationsbehov uppstår kan följande ordning användas.

### 1. Identifiera ansvariga parter

Vilken domän eller lösning äger informationen eller funktionen? Vem konsumerar den?

### 2. Beskriv behovet utan teknik

Vad behöver kommuniceras och varför? Behövs omedelbart svar?

### 3. Klassificera interaktionen

Är det främst:

- synkron tjänsteintegration,
- riktad asynkron meddelandekommunikation,
- händelsepublicering,
- filutbyte,
- dataförflyttning?

### 4. Identifiera kopplingskraven

Måste parterna vara tillgängliga samtidigt? Känner producenten konsumenten? Hur självständiga behöver de vara?

### 5. Definiera kontraktet

Vilken information, semantik, felmodell och livscykel gäller?

### 6. Definiera kvalitetskrav

Vilka krav finns på latens, tillgänglighet, leverans, ordering, volym, aktualitet och spårbarhet?

### 7. Definiera felbeteendet

Vad händer vid timeout, dubblett, avbrott, ogiltigt innehåll eller långvarigt konsumentfel?

### 8. Definiera tillit och skydd

Vilka identiteter, behörigheter och säkerhetsgränser berörs?

### 9. Välj mönster och gemensam tjänst

Först nu väljs exempelvis API management, messaging, pub/sub, filöverföring eller annan realisering.

### 10. Planera kontraktets förändring

Hur versioneras, migreras och avvecklas integrationen?

Denna ordning är inte ett obligatoriskt processflöde. Den är ett sätt att förhindra att teknikvalet föregår förståelsen för relationen mellan parterna.

## Integrationens mål är kontrollerad självständighet

Bra integration handlar inte om att eliminera alla beroenden. Om två verksamhetsförmågor faktiskt behöver samverka finns ett beroende.

Arkitekturens uppgift är att göra beroendet **avsiktligt, synligt och förvaltningsbart**.

Ett bra integrationslandskap gör det möjligt för lösningar att:

- kommunicera genom tydliga kontrakt,
- förändras utan onödig samordning,
- hantera störningar kontrollerat,
- använda gemensamma mekanismer där de ger nytta,
- behålla verksamhetsansvar nära rätt domän.

Det är därför integrationsförmågan inte bör mätas i hur många flöden en central plattform kontrollerar. En bättre fråga är hur lätt organisationen kan skapa och förändra **robusta relationer mellan självständiga lösningar**.

I nästa kapitel flyttas fokus från själva kommunikationen till frågan om tillit: **hur vet en lösning vem människan, tjänsten eller organisationen på andra sidan faktiskt är, och vad den får göra?**
