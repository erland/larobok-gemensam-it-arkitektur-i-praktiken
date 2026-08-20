# 17. Integration och kommunikation

Nästan inget modernt verksamhetsstöd är helt självständigt. Ett system behöver hämta information från ett annat, publicera en händelse, skicka ett meddelande, överföra en fil eller kommunicera med en extern organisation. Även en lösning som är väl avgränsad internt blir därför en del av ett större nät av beroenden.

Det gör integration till mer än en teknisk transportfråga.

När två självständiga lösningar kopplas samman uppstår beroenden i tid, kontrakt, semantik, tillgänglighet, säkerhet och förändringstakt. Valet mellan API, meddelanden, events och filutbyte avgör därför inte bara hur information flyttas. Det påverkar hur lösningarna kan utvecklas, hur fel sprids, vem som äger initiativet och hur lätt sambandet går att förstå och förvalta.

Kärnfrågan i kapitlet är:

> Vilken kommunikationsform passar behovet – och vilken koppling mellan parterna är vi beredda att acceptera?

Kapitlet handlar om den gemensamma IT-förmågan *Integration och kommunikation*. Fokus ligger på informationsutbyte mellan självständiga lösningar och på de mekanismer som kan göras gemensamma. Verksamhetsmässig processorkestrering, informationsägarskap och datalivscykel behandlas som separata frågor, liksom identitet och tillit.

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

Integration är därför en förvaltningsbar relation mellan två eller flera ansvariga parter.

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

- synkronicitet – krävs ett svar i samma interaktion?
- tidskoppling – måste producent och konsument vara tillgängliga samtidigt?
- riktning – är det en begäran, ett meddelande, en händelse eller ett informationspaket?
- antal parter – finns en mottagare eller potentiellt många?
- volym – handlar det om små enskilda meddelanden eller stora datamängder?
- leveranskrav – vad händer om informationen inte når fram direkt?
- ordning – spelar det roll i vilken sekvens meddelanden behandlas?
- aktualitet – hur gammal får informationen bli?
- koppling – hur mycket behöver avsändaren känna till om mottagaren?
- förvaltningsgräns – kan parterna förändras och driftsättas oberoende?

Dessa frågor gör det möjligt att välja mönster efter behov i stället för efter teknisk vana.

## Interaktionsformer: synkront, asynkront och pub/sub

Synkron och asynkron kommunikation löser olika behov och skapar olika former av koppling.

Vid synkron kommunikation skickar en konsument en begäran och väntar på svar innan den kan fortsätta. Det passar när en användare väntar på resultatet, aktuell information måste hämtas eller ett kommando behöver bekräftas direkt.

```text
Klient ── begäran ──▶ Tjänst
       ◀── svar ─────
```

Modellen är enkel att förstå men skapar tidskoppling. Om tjänst B i sin tur anropar C och D växer beroendekedjan:

```text
A → B → C → D
```

Latens summeras och fel kan spridas bakåt. Synkrona API:er är därför ofta rätt val, men de bör användas med förståelse för den operativa koppling de skapar.

Timeout är en del av kontraktet. Lösningen behöver veta hur länge den väntar, vad timeout betyder, om anropet kan provas igen och om operationen kan ha genomförts trots att svaret förlorades. Ett blint återförsök kan annars skapa dubbletter. För vissa operationer behöver kontraktet stödja idempotens eller motsvarande mekanism.[K1]

Vid asynkron kommunikation skickas information utan krav på att mottagaren behandlar den medan avsändaren väntar:

```text
Producent ──▶ Kö ──▶ Konsument
```

Det minskar tidskopplingen och passar när arbete kan ske senare, belastning behöver jämnas ut eller mottagaren måste kunna vara tillfälligt otillgänglig. I stället behöver lösningen hantera omleverans, dubbletter, gamla meddelanden, felparkering och återstart.

Det betyder att robustare tidskoppling inte ger mindre designarbete. Frågor som tidigare hanterades i samma anrop flyttas i stället till meddelandets livscykel. Lösningen behöver veta hur länge ett meddelande får vänta, hur många omleveranser som är rimliga, när ett fel ska kräva mänsklig hantering och hur konsumenten kommer tillbaka till ett känt läge efter ett längre avbrott.

Begrepp som *at-most-once*, *at-least-once* och *exactly-once* är användbara, men infrastrukturen kan inte ensam garantera korrekt verksamhetsutfall när databaser och externa system ingår. Idempotens, deduplicering och tydliga transaktionsgränser blir därför centrala. Det är den verksamhetsmässiga effekten som behöver bli korrekt, inte bara meddelandebussens interna leveransstatus.

Asynkron teknik kan bära både riktade meddelanden och händelser, men semantiken skiljer sig. Ett kommando uttrycker ett önskat arbete, exempelvis `SkapaFraktuppdrag`, medan en händelse beskriver ett faktum som redan inträffat, exempelvis `OrderGodkänd`.

> Events bör beskriva fakta som producenten äger, inte fungera som dolda fjärrkommandon till specifika konsumenter.

I ett publicera/prenumerera-mönster kan flera oberoende konsumenter reagera på samma händelse:

```text
             ┌──▶ Konsument A
Producent ──▶ Topic ──▶ Konsument B
             └──▶ Konsument C
```

Det minskar producentens kunskap om konsumenterna, men inte behovet av stabila kontrakt. Nya konsumenter, historik, versionsförändringar och semantik behöver fortfarande hanteras.

Pub/sub behöver därför besvara frågor som vem som får publicera, hur konsumenter upptäcker relevanta händelser, hur långt bak historik kan läsas och hur en kontraktsförändring påverkar konsumenter som utvecklas i en annan takt. Om producenten måste känna till exakt vilka konsumenter som finns och vänta in deras förändringar har man förlorat en stor del av den avsedda självständigheten.

Teknisk asynkronicitet är alltså inte samma sak som arkitekturell lös koppling.

## API:er – kontrakt, inte bara endpoints

Ett API bör inte reduceras till en teknisk URL och ett antal HTTP-anrop. Det är ett förvaltat kontrakt mellan parter.

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

Det innebär inte att databaser aldrig delas tekniskt. Men om två självständiga ansvar använder samma interna lagringsmodell som sitt primära kontrakt har man skapat en stark koppling som behöver vara medvetet motiverad.

Ett API-kontrakt behöver dessutom beskriva mer än ”happy path”. Felmodell, validering, trafikbegränsningar, autentiseringskrav och versionsstrategi påverkar konsumentens möjlighet att bygga robust. Ett tekniskt korrekt endpoint utan tydlig semantik och livscykel är därför fortfarande ett svagt kontrakt.

## Plattform, filutbyte, dataförflyttning och transformation

Gemensamma integrationsplattformar kan realisera återkommande mekanismer, men de ersätter inte arkitekturansvaret. En större organisation behöver ofta flera erbjudanden snarare än en enda universell integrationsprodukt: API management, messaging, data integration/ETL, hanterad filöverföring och säker extern kommunikation kan ha olika kvalitetsprofiler och målgrupper.

En API Management-tjänst kan exempelvis erbjuda exponering, policy enforcement, autentiseringskopplingar, trafikbegränsning, statistik och utvecklarportal. Den kan däremot inte avgöra var tjänstegränsen bör gå, vem som äger informationen eller om kommunikationen borde vara synkron. Plattformen stödjer mekanismen; ansvar, semantik och gränser behöver fortfarande designas.

Filbaserad integration är på motsvarande sätt inte automatiskt föråldrad. Den kan vara lämplig för stora batcher, periodisk behandling, etablerade externa kontrakt eller när själva filen är leveransenheten. Då behöver format, schema, integritet, kvittens, felhantering, kryptering, retention och omleverans ändå behandlas som ett förvaltat kontrakt.

Särskilt viktigt är att kunna skilja en omleverans från en ny leverans och att veta om en batch är fullständig eller inkrementell. Filer som bara placeras i en katalog utan definierad livscykel är därför inte enklare arkitektur; de är bara ett kontrakt som råkar vara sämre synliggjort.

Dataförflyttning ligger nära integration men har ofta ett annat syfte. Ett operativt API kan ge aktuell information i en affärstransaktion, medan ETL eller replikering kan flytta stora datamängder till analys eller annan bearbetning. Kraven på aktualitet, volym, transaktionell semantik, historik och återkörning skiljer sig därför.

Det är också en ägarskapsfråga. En härledd kopia kan vara helt legitim för analys eller sökning utan att bli ny auktoritativ källa. Integrationslösningen behöver därför bära tillräcklig metadata för att mottagaren ska förstå ursprung, aktualitet och vilken användning kopian är avsedd för.

Det är användbart att skilja mellan:

1. tjänsteintegration – funktionalitet eller aktuell information används mellan lösningar,
2. händelse-/meddelandeintegration – fakta eller arbete distribueras asynkront,
3. dataförflyttning – datamängder kopieras eller transformeras för ett annat ändamål.

Transformation kan behövas mellan olika externa kontrakt, men den får inte bli ett sätt att gömma verksamhetslogik i integrationslagret.

> Integration får anpassa kontrakt och transport, men verksamhetens auktoritativa beslut och domänlogik bör ligga hos den ansvariga domänen.

Frågan är alltså inte om transformation får förekomma, utan om en regel är teknisk mappning eller verksamhetsmässig logik.

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

- syntax – hur kontraktet ser ut,
- semantik – vad informationen betyder,
- beteende – vad producent och konsument kan förvänta sig.

### Parallella versioner har ett pris

Det är lockande att lösa alla förändringar genom att behålla gamla versioner för alltid.

Det skapar i stället en växande förvaltningskostnad.

En mogen integrationsförmåga behöver därför även stöd för:

- annonsering av förändringar,
- migrationsperioder,
- uppföljning av konsumenter,
- deprecation,
- avveckling.

API-kataloger, schemaregister eller andra kontraktskataloger kan hjälpa, men de ersätter inte ansvar mellan producent och konsument. Producenten behöver veta vilka kompatibilitetslöften som faktiskt gäller, och konsumenten behöver kunna planera migration innan en gammal version tas bort. Det gör kontraktslivscykeln till en del av tjänstens förvaltning, inte en engångsaktivitet vid första integrationen.

## Leveranssemantik, felbeteende och ordering

Fel och leveransgarantier behöver designas utifrån interaktionsformen, inte bara utifrån vad plattformen råkar erbjuda.

Vid ett synkront API kan konsumenten få timeout eller felkod direkt. Vid asynkron kommunikation kan ett meddelande levereras igen eller flyttas till en felmekanism. Vid filutbyte kan en hel batch behöva avvisas, delvis accepteras eller köras om.

Det räcker därför inte att säga att ”plattformen hanterar återförsök”. Lösningen behöver definiera verksamhetsmässigt felbeteende:

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

Ordering är på samma sätt ett krav, inte en standardinställning. I vissa flöden är sekvensen kritisk; i andra skapar global ordering bara onödig begränsning i skalbarhet och parallell behandling. Ofta räcker ordning inom en avgränsad nyckel, exempelvis per kund eller ärende, vilket ger större frihet än global serialisering.

Frågor att ställa är exempelvis:

- behövs global ordning eller räcker ordning per kund, ärende eller annan nyckel?
- kan konsumenten hantera sen ankomst?
- kan tillståndet härledas från versionsnummer eller tidsstämplar?
- vad betyder timeout, dubblett eller delvis genomförd operation för verksamheten?

Principen är enkel: beställ inte starkare tekniska garantier än behovet kräver, men lämna inte felbeteendet implicit.

## Integration över organisationsgränser

När kommunikationen går till en annan organisation förändras flera förutsättningar. Den andra parten kan ha andra drifttider, säkerhetsmodeller, kontaktvägar, standarder och förändringscykler. Det gör integrationskontraktet mer likt ett tjänstekontrakt mellan självständiga organisationer än ett internt tekniskt gränssnitt.

Den andra parten kan ha:

- annan förändringstakt,
- annan säkerhetsmodell,
- andra drifttider,
- andra kontaktvägar,
- andra standarder,
- annan incidenthantering.

Det gör tjänstekontrakt och ansvar ännu viktigare.

En extern kommunikationstjänst eller myndighetsgemensam infrastruktur kan erbjuda säker transport eller strukturerat informationsutbyte. Men den löser inte automatiskt frågan om vad informationen betyder eller hur fel hanteras mellan verksamheterna.

Extern integration bör därför behandlas som tjänstekonsumtion med definierade ansvar och begränsningar, inte som ett anonymt nätverksflöde. Kontaktsätt, incidentväg, ändringsavisering, tillgänglighetsförväntningar och eventuell fallback behöver vara kända även när själva transporten levereras av gemensam eller nationell infrastruktur.

## Tvärgående realiseringsfrågor

Integration kräver nätverk, identitet, säkerhet och observerbarhet, men integrationsförmågan bör inte ensam äga dessa områden.

Nätverksregler bör härledas från dokumenterade tjänsterelationer: vem kommunicerar med vem, i vilken riktning, för vilket syfte, med vilken identitet och under vilka kvalitets- och säkerhetskrav. En brandväggsregel utan känd tjänsterelation blir annars snabbt ett historiskt beroende som ingen vågar förändra.

Ett integrationsflöde behöver också kunna svara på vem eller vilken tjänst motparten är, hur den autentiseras, vilken behörighet den har och vilka trust boundaries som passeras. Detta fördjupas i avsnittet om identitet och tillit.

Viktiga flöden behöver dessutom kunna följas över systemgränser, exempelvis med korrelations-id, strukturerad loggning, spårning, meddelandeidentifierare och mätvärden för ködjup, fel och latens. De bredare mekanismerna för observerbarhet och operativ återkoppling behandlas i förmågan för driftbarhet och motståndskraft.

Poängen är att integration definierar kommunikationsrelationens behov, medan andra förmågor tillhandahåller återanvändbara mekanismer för nätverk, identitet, säkerhet och driftbarhet.

Detta är också viktigt för felsökning och förändring. Om ett flöde bara dokumenteras som portar, certifikat och köer blir det svårt att avgöra vad som faktiskt får påverkas av en teknisk ändring. När samma mekanismer i stället kan kopplas till en namngiven tjänsterelation och ett kontrakt blir beroendet begripligt även för den som inte känner den tekniska implementationen.

## Gemensamma plattformstjänster för integration

Ett större IT-område kan behöva flera gemensamma erbjudanden snarare än ”en integrationsplattform”. Exempel är:

- API Management,
- *Enterprise Messaging*,
- *Data Integration / ETL*,
- Managed File Transfer eller motsvarande funktion,
- säker extern konnektivitet,
- tjänster för strukturerat informationsutbyte.

Det viktiga är att varje erbjudande har ett tydligt tjänstekontrakt.

Konsumenten behöver veta:

- vilka behov tjänsten löser,
- vilka interaktionsformer och volymer den är avsedd för,
- vilka garantier den ger och var garantierna slutar,
- vilket ansvar konsumenten fortfarande har,
- hur onboarding och test sker,
- hur kontrakt och versioner hanteras,
- hur tjänsten övervakas och supporteras.

Det bör också vara möjligt att förklara när ett erbjudande inte ska användas. Ett API-erbjudande, en messagingtjänst och en filöverföringstjänst kan alla höra till samma förmåga men vara avsedda för olika behov. Ett tydligt tjänsteerbjudande minskar därför både speciallösningar och tendensen att använda den plattform som råkar vara mest etablerad till allt.

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

En bättre målbild är ofta en sammanhängande portfölj av standardiserade integrationsförmågor och tjänster, där mekanism väljs efter behov.

## Ansvar på tre nivåer

Den gemensamma nivån bör ange vilka integrationsformer organisationen behöver stödja, principer för kontrakt och livscykel, övergripande säkerhets- och spårbarhetskrav samt relevanta interoperabilitetsstandarder.

Förmågeansvaret för Integration och kommunikation utvecklar återanvändbara mönster, standarder, tjänsteerbjudanden, kontrakts- och versionsvägledning samt stöd för test, onboarding och livscykel. Det bör också följa var utvecklingsområden återkommande skapar speciallösningar som signalerar luckor i det gemensamma erbjudandet.

Den konkreta lösningen ansvarar för kommunikationsbehovet, kontraktets verksamhetssemantik, val av mönster, felbeteende, idempotens, timeout, återförsök och hur integrationen används i domänens process.

Det lokala teamet ska alltså inte behöva bygga en egen meddelandeplattform. Men plattformsteamet kan inte avgöra om ett visst verksamhetsflöde bör vara ett API, ett event eller en fil.

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

### Återförsök utan idempotensanalys

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

Arkitekturens uppgift är att göra beroendet avsiktligt, synligt och förvaltningsbart.

Ett bra integrationslandskap gör det möjligt för lösningar att:

- kommunicera genom tydliga kontrakt,
- förändras utan onödig samordning,
- hantera störningar kontrollerat,
- använda gemensamma mekanismer där de ger nytta,
- behålla verksamhetsansvar nära rätt domän.

Det är därför integrationsförmågan inte bör mätas i hur många flöden en central plattform kontrollerar. En bättre fråga är hur lätt organisationen kan skapa och förändra robusta relationer mellan självständiga lösningar.

I nästa kapitel flyttas fokus från själva kommunikationen till frågan om tillit: hur vet en lösning vem människan, tjänsten eller organisationen på andra sidan faktiskt är, och vad den får göra?

## Källor och vidare läsning

**[K1]** IETF/RFC Editor, *RFC 9110: HTTP Semantics*, särskilt avsnittet om idempotenta metoder. https://www.rfc-editor.org/info/rfc9110/

Vidare läsning: Cloud Native Computing Foundation, *CloudEvents specification*. https://cloudevents.io/

Vidare läsning: OASIS Open, *MQTT Version 5.0*. https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html
