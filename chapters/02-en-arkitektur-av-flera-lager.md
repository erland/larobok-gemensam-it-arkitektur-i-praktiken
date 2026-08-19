# 2. En arkitektur av flera lager

Det är lätt att tala om arkitektur som om den vore en enda sak. I praktiken består en fungerande gemensam IT-arkitektur av flera typer av beskrivningar, beslut och erbjudanden som svarar på olika frågor och förändras i olika takt.

Ett verksamhetsbehov är inte samma sak som ett tekniskt krav. En förmåga är inte samma sak som en plattform. Ett lösningsmönster är inte samma sak som en produktstandard. En referensarkitektur är inte samma sak som en färdig lösningsarkitektur. När nivåerna blandas ihop blir arkitekturen svår att förstå, styra och förändra.

Detta kapitel presenterar den modell som används genom resten av boken. Syftet är att ge en karta över lagren, deras relationer och deras olika förändringstakt. Fördjupningen kommer senare. Här är det viktigare att förstå vilken fråga varje lager besvarar och hur ett konkret teknikval kan spåras tillbaka till det behov som motiverade det.

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

Modellen ska inte läsas som att varje behov måste passera exakt ett objekt i varje lager. Ett behov kan beröra flera förmågor, ett mönster kan spänna över flera förmågor och en plattformstjänst kan realisera delar av flera mönster. En standard kan gälla flera plattformar och samma produkt kan användas i flera tjänster.

Poängen är att lagren representerar olika frågor:

- Behov beskriver vad verksamheten eller IT-stödet behöver kunna uppnå.
- Krav och kvalitetsattribut uttrycker vilka egenskaper lösningen måste ha.
- Förmågor beskriver vilka återkommande typer av stöd IT-området behöver kunna erbjuda.
- Lösningsmönster beskriver återanvändbara sätt att strukturera återkommande problem.
- Plattformstjänster beskriver konsumerbara tekniska erbjudanden.
- Standarder anger gemensamma teknikval, konventioner och ramar.
- Tekniska byggblock beskriver generiska tekniska beståndsdelar.
- Produkter, versioner och konfigurationer beskriver den konkreta realiseringen.

Arkitekturens uppgift är att hålla ihop resonemanget från behov till realisering utan att låsa ihop nivåerna mer än nödvändigt. Om ett projekt behöver hög tillgänglighet bör diskussionen därför inte börja med vilken produkt som ska installeras. Om ett team behöver asynkron kommunikation bör inte meddelandeprodukten väljas innan problemet och kvalitetskraven är förstådda.

## Lager handlar också om förändringstakt

Ett viktigt skäl till att skilja lagren åt är att de förändras i olika takt.

Ett återkommande behov av säker autentisering kan finnas i decennier. Förmågan att hantera identitet och tillit kan därför vara stabil länge. Ett visst protokoll eller en plattform kan leva kortare, och en produktversion kan vara aktuell i bara några år.

Om allt dokumenteras på samma nivå blir stabila beskrivningar fulla av kortlivad teknik. Dokument som borde beskriva vad organisationen behöver kunna göra börjar i stället innehålla produktnamn, versionsnummer och konfigurationsdetaljer. När tekniken förändras ser det då ut som om hela arkitekturen måste ändras.

Det motsatta problemet uppstår när tekniska beslut blir för abstrakta. Välformulerade principer om interoperabilitet och återanvändning räcker inte om teamen saknar tydliga besked om vilka protokoll, plattformar och versioner som faktiskt stöds.

En användbar modell behöver därför både stabilitet och konkretion, men på olika ställen:

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

Detta är ingen absolut regel. Även förmågor förändras och vissa standarder kan vara långlivade. Men skillnaden i förändringstakt hjälper organisationen att avgöra vad som bör vara stabilt och vad som ska kunna bytas ut utan att den övergripande modellen behöver göras om.

## Behov beskriver problemet – inte lösningen

Modellens översta lager är behovet. Ett behov beskriver något verksamheten eller ett IT-stöd behöver kunna uppnå utan att på förhand låsa teknisk realisering.

> En extern part ska kunna lämna in information digitalt och få kvittens på att den tagits emot.

Detta säger ännu inget om API, filöverföring, meddelandekö, webbgränssnitt eller en viss produkt.

Ett annat exempel är att ett internt handläggningsstöd ska kunna fortsätta hantera prioriterade ärenden även om en enskild teknisk komponent fallerar. Det leder vidare till krav på exempelvis tillgänglighet och återställning, men själva behovet ska inte redan innehålla lösningen.

Kapitel 3 fördjupar hur behov hålls produktoberoende och hur verkliga begränsningar skiljs från förtida lösningsval.

## Krav och kvalitetsattribut gör behovet prövbart

Behov behöver konkretiseras för att kunna styra arkitekturen. Därför finns nästa lager: krav och kvalitetsattribut.

Ett påstående som ”systemet måste vara tillgängligt” är sällan tillräckligt. För att påverka design och verifiering behöver det uttryckas mer precist. Verksamhetens tolerans för avbrott kan exempelvis översättas till krav på återställningstid. Ett behov av spårbar handläggning kan bli krav på loggning, revisionsinformation och bevarande. Förväntad toppbelastning kan ge krav på svarstid och skalbarhet.

Kvalitetsattributen fungerar därmed som en bro mellan verksamhetskonsekvens och arkitekturval. De är tvärgående: säkerhet hör inte bara till identitetsområdet, prestanda inte bara till runtime och kontinuitet inte bara till backup. Samma kvalitet kan påverka flera förmågor och flera tekniska lager samtidigt.

Det är också här som generella ambitioner behöver börja få en tydligare innebörd. Två lösningar kan båda vara ”säkra” men kräva olika skyddsnivåer, eller båda vara ”tillgängliga” men med helt olika tolerans för avbrott. Kravlagret gör sådana skillnader synliga innan de översätts till konkreta mönster och teknikval.

Kapitel 4 fördjupar hur kvalitetsattribut formuleras, prioriteras och används som arkitekturdrivare.

## Förmågor skapar en stabil navigationsstruktur

När liknande behov och kvalitetskrav återkommer i många lösningar behöver organisationen kunna strukturera vilket stöd IT-området ska kunna erbjuda. Där kommer förmågorna in.

En förmåga beskriver vad det stödjande IT-området behöver kunna erbjuda stöd för utan att bindas till en viss produkt eller implementation. Exempel är Integration och kommunikation, Identitet och tillit, *Applikationsexekvering och runtime*, Driftbarhet och motståndskraft samt Programvaruutveckling och leverans.

Förmågan fungerar som en relativt stabil navigationsstruktur. Om organisationen byter API-gateway, containerplattform eller identitetsprodukt behöver därför inte själva förmågekartan skrivas om. Förmågan ska samtidigt vara tillräckligt konkret för att samla relevanta behov, kvalitetsfrågor, mönster, tjänsteerbjudanden och standarder inom ett begripligt område.

Den ska inte förväxlas med en organisationsruta. Ett team kan ansvara för flera förmågor och flera team kan bidra till samma förmåga. Själva förmågebegreppet behandlas mer ingående i Del II.

## Lösningsmönster fångar återanvändbart resonemang

En förmåga berättar fortfarande inte exakt hur ett visst problem bör lösas. Därför behövs lösningsmönster.

Ett lösningsmönster är ett återanvändbart sätt att strukturera ett återkommande arkitekturproblem. Det fångar inte bara en rekommenderad lösningsform utan även viktiga designfrågor och villkor för när mönstret passar.

Exempel är Backend for Frontend, *asynkron meddelandekommunikation*, publicera/prenumerera, human workflow, externaliserade verksamhetsregler, cache-aside, tjänsteidentitet och observerbarhet för distribuerade tjänster.

Mönstrets värde ligger i att erfarenheten överlever teknikbyten. Ett mönster för asynkron kommunikation kan exempelvis göra idempotens, ordering, återförsök, dead-letter-hantering och korrelation till explicita designfrågor även om meddelandeprodukten byts ut. Mönster kan dessutom spänna över flera förmågor.

Del IV fördjupar hur lösningsmönster utformas och används.

## Plattformstjänster gör arkitekturen konsumerbar

En gemensam arkitektur blir inte särskilt användbar om den bara består av principer och mönster. Utvecklingsteam behöver också konkreta erbjudanden.

En plattformstjänst är ett återanvändbart tekniskt erbjudande som ett utvecklingsområde kan konsumera, exempelvis en relationell databastjänst, API Management, en containerplattform, en identitetstjänst, central loggning eller en CI/CD-plattform.

Skillnaden mot en produkt är viktig. En containerplattform som tjänst är mer än namnet på programvaran som används. Tjänsten behöver också uttrycka vad konsumenten får, vilka kvalitetsnivåer som erbjuds, ansvarsfördelning, begränsningar och vad konsumenten själv måste göra. Det är alltså erbjudandet och kontraktet mot konsumenten som är arkitekturobjektet; produkten är en del av hur erbjudandet realiseras.

```text
Behov: köra containeriserad applikation med definierad tillgänglighet
        ↓
Förmåga: Applikationsexekvering och runtime
        ↓
Mönster: Containeriserad stateless tjänst
        ↓
Plattformstjänst: Container Application Platform
```

Först därefter behöver organisationen ange vilken produkt eller vilka komponenter som realiserar tjänsten. Det gör det möjligt att behålla ett stabilt erbjudande även när den underliggande tekniken förändras.

Del V fördjupar plattformar som produkter och tjänsteerbjudanden.

## Standarder begränsar variation medvetet

Plattformstjänster svarar på vad organisationen erbjuder. Standarder anger vilka gemensamma teknikval och konventioner som ska eller bör gälla.

En standard kan exempelvis ange hur API:er ska beskrivas, vilka identitetsprotokoll som stöds, hur containerbilder ska byggas eller vilka loggfält som krävs. Det är samtidigt viktigt att skilja en arkitektur- eller teknikstandard från produktstandard, versionsstöd och konkret konfiguration.

```text
Arkitektur-/teknikstandard
        ↓
Produktstandard
        ↓
Versions- och supportstandard
        ↓
Teknisk konfiguration
```

Om dessa nivåer blandas blir standarden både svår att förstå och svår att förvalta. Standarder behöver dessutom kunna förklaras genom vilket behov, vilken kvalitet eller vilket operativt värde de stödjer. Annars riskerar de att bli preferensstyrning.

Standardernas livscykel behandlas mer ingående i Del V.

## Tekniska byggblock och produkter är inte samma sak

Längst ner i realiseringskedjan finns tekniska byggblock och produkter.

Ett tekniskt byggblock är en generisk teknisk beståndsdel, exempelvis operativsystem, databasmotor, reverse proxy, objektlagring eller meddelandebroker. En produkt är en konkret implementation av ett eller flera sådana byggblock.

Skillnaden är praktisk. Ett behov av en meddelandebroker anger ännu inte vilket produktnamn som ska användas. Ett relationellt databaslager anger inte automatiskt leverantör eller version. Samtidigt kan samma produkt realisera flera byggblock eller tjänster.

Produkt, version och konfiguration är nödvändiga i den faktiska implementationen. Poängen är inte att undvika dem, utan att placera dem på rätt nivå så att högre arkitekturdelar inte blir onödigt produktbundna.

## Referensarkitekturen går på tvären

Alla artefakter passar inte in som ett vertikalt steg i kedjan. Referensarkitekturen är det tydligaste exemplet.

En referensarkitektur beskriver en sammanhängande rekommenderad struktur för en viss typ av lösning och kombinerar därför ofta flera förmågor, mönster, plattformar och standarder samtidigt.

```text
Förmågor + mönster + plattformar + standarder
                    ↓
           Referensarkitektur
                    ↓
            Lösningsarkitektur
```

En referensarkitektur för en publik e-tjänst kan exempelvis kombinera interaktion och kanaler, identitet, API-hantering, integration, datalagring, observerbarhet och relevanta säkerhetskrav.

Den är alltså inte en ny förmåga eller ett enskilt mönster, och inte heller en färdig lösningsarkitektur. Den ger en etablerad struktur för en återkommande lösningstyp men lämnar fortfarande utrymme för den konkreta lösningens behov, informationsmodell och kvalitetskrav. På så sätt fungerar referensarkitekturen som en brygga mellan den gemensamma arkitekturen och en faktisk lösningsarkitektur: tillräckligt konkret för att minska startsträckan, men inte så specifik att alla lösningar tvingas bli identiska.

Referensarkitekturer fördjupas i Del VI.

## Spårbarhet gör modellen användbar

Modellen blir värdefull först när man kan följa varför ett beslut finns. Om ett projekt får beskedet att använda en viss gemensam tjänst bör det gå att förstå vilket behov, vilka kvalitetskrav och vilka arkitekturbeslut som motiverar den.

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

Spårbarhet betyder inte att varje pil måste administreras som ett separat dokument. Det betyder att beslutskedjan ska kunna förstås när den behöver granskas, förändras eller ersättas.

Det gör bland annat avsteg lättare att bedöma. Om ett team vill använda en annan teknisk lösning kan diskussionen handla om huruvida behov och kvalitetskrav fortfarande uppfylls, inte bara om ett produktnamn avviker. Det gör också teknikbyten enklare eftersom organisationen kan se vilka tjänster, mönster och krav som påverkas när en produkt avvecklas.

## Relationerna är viktigare än dokumenten

Det är lätt att göra modellen till en dokumentationsövning: ett dokument för varje förmåga, ett för varje mönster och ett för varje standard. Men modellens värde ligger främst i relationerna.

En förmåga bör kunna kopplas till relevanta mönster och plattformstjänster. En plattformstjänst bör visa vilken förmåga den stödjer och vilka kvaliteter den erbjuder. En standard bör kunna förklaras genom vad den styr. En referensarkitektur bör visa vilka delar den kombinerar.

Arkitekturen är därför bättre beskriven som ett nät av relaterade artefakter än som en samling fristående dokument. En sådan syn gör det också lättare att se påverkan av förändring: om en standard avvecklas kan man följa vilka tjänster, mönster och lösningstyper som berörs. Verktyget är sekundärt; relationerna måste vara begripliga även utan ett avancerat arkitekturregister.

## Ett konkret exempel: från e-tjänst till teknik

Anta att en myndighet ska skapa en publik e-tjänst där företag kan lämna uppgifter och följa sina ärenden.

Om arbetet börjar på produktnivå kan diskussionen snabbt handla om frontend-ramverk, databas och containerplattform. Med den lagerindelade modellen kan resonemanget börja högre upp.

1. **Behov**  
   Företag ska kunna identifiera sig, lämna uppgifter, få kvittens och senare se status för sina ärenden.

2. **Kvalitetskrav**  
   Tjänsten behöver bland annat skydda känslig information, ge spårbarhet, vara tillgänglig under definierade perioder och klara uppskattad toppbelastning.

3. **Förmågor**  
   Behovet berör exempelvis *Interaktion, presentation och kanaler*, Identitet och tillit, Process, workflow och ärendehantering, Integration och kommunikation, Data- och informationshantering samt Driftbarhet och motståndskraft.

4. **Mönster**  
   Backend for Frontend, tjänsteidentitet, asynkron meddelandekommunikation och observerbarhet för distribuerade tjänster kan vara relevanta beroende på lösning.

5. **Plattformstjänster**  
   Gemensamma erbjudanden kan ge identitetstjänst, API Management, relationsdatabastjänst, containerplattform och central loggning.

6. **Standarder**  
   API-standard, identitetsprotokoll, observerbarhetsstandard, containerstandard och release-standard kan begränsa den tekniska variationen.

7. **Produkt och konfiguration**  
   Först här behöver realiseringen bli fullt specifik: produkt, version, miljö och konfiguration.

Det innebär inte att arbetet alltid sker strikt uppifrån och ner. Ett befintligt plattformserbjudande kan påverka vad som är ekonomiskt rimligt och ett proof of concept kan visa att ett antagande var fel. Lagerindelningen hjälper oss att förstå vilken typ av information som påverkar vilken typ av beslut, även när arbetet går fram och tillbaka.

## En modell för navigering, inte ett nytt vattenfall

Den vertikala kedjan kan lätt misstolkas som en process där alla behov först ska färdigställas, därefter alla krav, därefter alla förmågor och så vidare. Så är modellen inte avsedd.

I praktiken sker arbetet iterativt. Plattformserfarenheter kan synliggöra nya kvalitetsbehov, återkommande mönster kan ge upphov till standarder och verkliga lösningar kan visa att en förmågegräns behöver justeras.

Modellen beskriver därför logiska beroenden och abstraktionsnivåer, inte en engångssekvens. Behov bör kunna motivera krav och krav bör kunna motivera arkitekturval, men kunskapen om vilka val som är rimliga utvecklas genom återkoppling från verkliga lösningar.

Hur detta etableras organisatoriskt och iterativt behandlas i kapitel 7.

## Vad ska vara stabilt – och vad ska kunna bytas ut?

En enkel kontrollfråga för modellen är:

> Om vi byter produkt i morgon, vilka delar av arkitekturen borde fortfarande vara giltiga?

Om svaret är ”nästan ingenting” är arkitekturen sannolikt för produktbunden.

Den omvända frågan är:

> Om verksamhetsbehovet förändras, vilka delar behöver vi ompröva även om tekniken är densamma?

Om svaret är ”ingenting” är arkitekturen sannolikt för teknikcentrerad.

Det önskvärda är att stabila behov, kvaliteter, principer och förmågor kan leva längre än enskilda produkter, samtidigt som modellen är tillräckligt konkret för att styra faktisk implementation. Det är denna kombination som gör lagerindelningen värdefull.

## Centrala fakta

- Gemensam IT-arkitektur består av flera artefakttyper som svarar på olika frågor och förändras i olika takt.
- Behov beskriver vad som behöver uppnås; krav och kvalitetsattribut gör behovet prövbart.
- Förmågor ger en stabil struktur för återkommande typer av IT-stöd.
- Lösningsmönster fångar återanvändbart arkitekturellt resonemang.
- Plattformstjänster är konsumerbara erbjudanden och bör skiljas från produkterna som realiserar dem.
- Standarder begränsar teknisk variation medvetet och bör hållas åtskilda från version och konfiguration.
- Tekniska byggblock är generiska beståndsdelar; produkter är konkreta implementationer.
- Referensarkitekturer kombinerar flera delar av modellen för en återkommande lösningstyp.
- Spårbarhet från behov till realisering gör beslut begripliga och förändringsbara.
- Lagerindelningen är en navigations- och resonemangsmodell, inte ett vattenfall.

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
