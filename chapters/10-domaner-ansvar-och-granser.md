# 10. Domäner, ansvar och gränser

En gemensam förmågekarta hjälper en organisation att beskriva vilket återkommande IT-stöd som behöver finnas. Den kan visa att organisationen behöver förmågor för exempelvis integration, identitet, datahantering, programvaruleverans och driftbarhet. Den kan också hjälpa till att tydliggöra vad som bör hanteras gemensamt och vad som bör ligga närmare en lösning eller verksamhetsdomän.

Men en förmågekarta svarar inte på alla arkitekturfrågor.

Den berättar inte automatiskt:

- var gränsen mellan två verksamhetsområden bör gå,
- vem som äger ett visst begrepp eller en viss affärsregel,
- vilken del av en lösning som får ändra ett visst dataobjekt,
- vilka tjänster som bör förändras tillsammans,
- hur beroenden mellan olika delar av verksamheten bör hanteras,
- eller hur man undviker att gemensamma plattformar börjar ta över verksamhetens eget ansvar.

Detta är frågor om domäner, ansvar och gränser.

De är centrala eftersom en arkitektur inte bara består av återanvändbara tekniska byggstenar. Den består också av självständiga delar som behöver ha tydligt ansvar för sin egen logik, information och förändring. Om dessa gränser är otydliga uppstår ofta en annan typ av fragmentering än den som gemensamma plattformar är avsedda att lösa: verksamhetslogik sprids mellan system, data får flera konkurrerande ägare och förändringar kräver samordning mellan allt fler team.

Detta kapitel behandlar därför de arkitekturproblem som inte bör lösas genom att göra ännu mer gemensamt.

## Två kartor som svarar på olika frågor

Det är lätt att blanda ihop en gemensam IT-förmågekarta med en domänmodell eller verksamhetsarkitektur. De kan båda beskriva organisationen på en relativt stabil nivå, men de svarar på olika frågor.

En gemensam IT-förmågekarta frågar exempelvis:

> Vilket återkommande IT-stöd behöver organisationen kunna erbjuda flera verksamhetsområden?

En domänorienterad analys frågar i stället:

> Vilka verksamhetsmässiga problem, begrepp, regler och ansvar hör naturligt ihop och bör kunna utvecklas med så lite beroende som möjligt till andra delar?

Skillnaden kan illustreras så här:

```text
Gemensam IT-förmåga             Verksamhetsdomän
-------------------             -----------------
Integration                     Tillståndshantering
Identitet                       Uppbörd
Datahantering                   Kontrollverksamhet
Workflow                        Personaladministration
Observerbarhet                   Inköp
```

Förmågorna till vänster kan återanvändas av många domäner. Domänerna till höger bär verksamhetens eget ansvar och innehåll.

Det innebär att samma verksamhetsdomän ofta använder flera gemensamma IT-förmågor, samtidigt som en gemensam IT-förmåga stödjer flera verksamhetsdomäner.

```text
                Gemensamma IT-förmågor
        ┌──────────┬──────────┬──────────┐
        │ Identitet│Integration│ Data     │
        └─────┬────┴─────┬────┴────┬─────┘
              │          │         │
      ┌───────▼──────────▼─────────▼──────┐
      │          Domän A                  │
      └───────────────────────────────────┘
              │          │         │
      ┌───────▼──────────▼─────────▼──────┐
      │          Domän B                  │
      └───────────────────────────────────┘
```

Detta är en viktig distinktion genom resten av boken: gemensamma förmågor beskriver återanvändbart stöd; domäner beskriver verksamhetsnära ansvar.

## Domänen som ansvarsyta

Ordet *domän* används på många sätt. I detta sammanhang är det mest användbart att se en domän som en sammanhängande ansvarsyta kring ett visst problemområde.

En domän kännetecknas ofta av att den har:

- egna centrala begrepp,
- regler som hör ihop,
- data eller information vars mening bestäms inom området,
- beslut som bör kunna fattas nära området,
- en förändringstakt som inte nödvändigtvis följer andra domäner,
- och ett tydligt verksamhetsmässigt ansvar.

Det betyder inte att en domän måste motsvara en organisatorisk enhet. En avdelning kan innehålla flera domäner och en domän kan sträcka sig över flera organisatoriska enheter.

Det betyder inte heller att en domän automatiskt ska bli en applikation eller mikrotjänst. Domänen beskriver först och främst ansvaret och problemet. Den tekniska realiseringen är ett senare beslut.

Detta är samma grundprincip som tidigare i boken: behov och ansvar bör förstås innan tekniken väljs.

## Bounded context – när ett begrepp behöver en tydlig betydelse

Ett användbart begrepp från Domain-Driven Design är *bounded context*.[K1] Det kan på svenska beskrivas som ett avgränsat sammanhang där en viss modell och terminologi har en bestämd betydelse.

Det är särskilt värdefullt i större organisationer eftersom samma ord ofta betyder olika saker i olika verksamhetsområden.

Ta begreppet *kund*.

I ett faktureringssammanhang kan kund vara den juridiska eller fysiska person som är betalningsansvarig. I ett supportärende kan kund vara den person som kontaktar organisationen. I en behörighetsmodell kan samma individ i stället beskrivas som användare, ombud eller representant.

Det är frestande att försöka skapa en enda global datamodell där ordet *kund* får exakt samma definition överallt. Ibland är det möjligt och önskvärt, men ofta leder det till en modell som blir svår att förstå eftersom olika verksamhetsbehov pressas in i samma begrepp.

Ett bounded context accepterar i stället att betydelsen kan vara lokal – så länge gränsen är tydlig och integrationen mellan sammanhangen är explicit.

Det ger en viktig arkitekturprincip:

> Gemensam semantik ska skapas där gemensam semantik faktiskt behövs. Där olika verksamhetskontexter har legitima skillnader ska dessa skillnader göras explicita i stället för att döljas i en överlastad gemensam modell.

Detta blir särskilt viktigt i nästa kapitel, där information och data behandlas som arkitekturella ingångsvärden.

## Cohesion – sådant som förändras tillsammans bör höra ihop

En bra gräns samlar sådant som har stark cohesion, alltså inre sammanhållning.

Det kan exempelvis vara funktioner, regler och data som:

- används för samma verksamhetsmål,
- behöver förstå samma begrepp,
- ofta förändras av samma anledning,
- behöver vara konsistenta i samma transaktionella eller verksamhetsmässiga sammanhang,
- eller ägs av samma verksamhetsansvar.

Ett enkelt sätt att resonera är att fråga:

> Om denna verksamhetsregel ändras, vilka andra delar måste vi nästan alltid förstå och ändra samtidigt?

Om två komponenter ständigt behöver förändras tillsammans kan det vara ett tecken på att de egentligen hör till samma ansvarsyta.

Omvänt kan en stor lösning innehålla delar som nästan aldrig behöver förändras tillsammans. Då kan en uppdelning i tydligare domäner eller moduler minska samordningsbehovet.

Hög cohesion innebär alltså inte att allt ska ligga i samma tekniska process eller kodbas. Det betyder att arkitekturen bör respektera vilka delar som konceptuellt hör ihop.

## Coupling – kostnaden för beroenden

Om cohesion handlar om sammanhållning inom en gräns handlar coupling om beroendet mellan gränser.

Alla system har beroenden. Målet är därför inte noll coupling, utan att beroenden ska vara:

- nödvändiga,
- begripliga,
- stabila,
- explicita,
- och möjliga att förändra utan oproportionerlig samordning.

Hög coupling märks ofta först när organisationen försöker förändra något.

Ett team ska exempelvis ändra ett regelverk men upptäcker att:

1. ett annat systems databas måste ändras,
2. ett tredje system måste releasas samtidigt,
3. ett centralt integrationsteam behöver konfigurera om ett flöde,
4. flera konsumenter använder en odokumenterad intern datastruktur,
5. och ingen vet säkert vem som äger det gemensamma begreppet.

Problemet är då inte bara tekniskt. Arkitekturen har skapat ett nät av gemensamt ansvar utan tydliga gränser.

Detta är en viktig motvikt till återanvändning. En gemensam komponent kan minska duplicering men samtidigt öka coupling. Om hundra lösningar blir beroende av samma verksamhetsnära bibliotek kan en liten ändring kräva samordning med hundra konsumenter.

Återanvändning är därför inte gratis.

En bra gemensam arkitektur försöker återanvända sådant som är stabilt och generellt, medan verksamhetsnära variation får stanna nära sin domän.

## Ägarskap måste vara tydligare än åtkomst

Ett vanligt arkitekturproblem uppstår när flera system kan läsa och skriva samma information utan att det är tydligt vem som faktiskt äger den.

Det är viktigt att skilja mellan:

- vem som äger betydelsen av informationen,
- vem som är system of record eller auktoritativ källa,
- vem som får ändra den,
- vem som får läsa eller kopiera den,
- och vem som ansvarar för kvalitet och livscykel.

Att ett system tekniskt kan skriva i en tabell betyder inte att det bör ha rätt att ändra informationens verksamhetsmässiga innebörd.

Ett robust ansvarssnitt är ofta asymmetriskt:

```text
Domän A äger uppgiften
        │
        ├─ publicerar kontrakt/händelser
        │
        ▼
Domän B använder uppgiften
        │
        └─ får inte bli parallell ägare
```

Detta minskar risken för att flera delar av organisationen utvecklar egna versioner av sanningen.

Men även här finns nyanser. En konsument kan behöva en lokal kopia för sökning, analys, tillgänglighet eller prestanda. Det gör inte kopian till ny auktoritativ källa. Ägarskapet behöver därför beskrivas oberoende av den fysiska lagringen.

Denna distinktion blir central när boken senare behandlar system of record, härledda kopior, cache och datakontrakt.

## Ansvar bör följa förändring, inte bara organisation

Organisationer förändras snabbare än många arkitekturmodeller. Team slås ihop, delas, byter namn eller flyttar mellan avdelningar. Om arkitekturgränserna definieras direkt utifrån dagens organisationsschema riskerar modellen därför att bli instabil.

Samtidigt kan ansvar inte vara helt frikopplat från organisationen. Någon måste faktiskt kunna fatta beslut, prioritera och bära konsekvenser.

En användbar princip är därför:

> Arkitekturgränsen bör i första hand följa ett stabilt ansvar och en sammanhängande förändringsyta. Organisationen bör därefter göra ägarskapet explicit.

Detta minskar två vanliga problem:

### 1. Organisatorisk spegling

Varje organisatorisk enhet får ett eget systemområde, även när verksamhetsansvaret egentligen skär tvärs genom organisationen.

### 2. Tekniskt ägarskap utan verksamhetsägarskap

Ett IT-team blir formell ägare av ett system men har inget mandat att avgöra reglerna och informationens betydelse. Resultatet blir att varje förändring kräver informella förhandlingar med flera verksamhetsparter.

Bra ägarskap behöver därför kombinera tekniskt ansvar med ett tydligt verksamhetsmässigt mandat eller åtminstone ett väldefinierat beslutsgränssnitt mot verksamheten.

## Gränser kan ligga på flera nivåer

När ordet gräns används i arkitektur är det lätt att tänka enbart på API:er eller nätverksgränser. Men gränser finns på flera nivåer.

### Begreppsgräns

Var gäller en viss definition och terminologi?

### Ansvarsgräns

Vem får besluta om regler, beteenden och information?

### Datagräns

Vem är auktoritativ källa och genom vilka kontrakt får andra använda informationen?

### Förändringsgräns

Vilka delar ska kunna förändras och releasas oberoende?

### Säkerhets- och tillitsgräns

När passerar data eller anrop mellan parter med olika tillit, klassning eller ansvar?

### Teknisk exekveringsgräns

Vilka delar körs separat, skalar separat eller isoleras av driftmässiga skäl?

Dessa gränser behöver inte sammanfalla exakt.

En bounded context kan exempelvis realiseras som flera moduler i samma applikation. Två domäner kan tillfälligt köras i samma runtime men ändå ha separerade datamodeller och tydliga ansvar. Omvänt skapar två mikrotjänster inte automatiskt två välavgränsade domäner om de delar samma begrepp, databas och förändringscykel.

Det är därför riskabelt att använda teknikens gränser som ersättning för domänanalys.

## Gemensam plattform ska inte bli en verksamhetsdomän

När en organisation bygger gemensamma plattformar uppstår ibland en subtil förskjutning. Plattformen börjar med generell teknik men tar gradvis över verksamhetslogik för att ”göra det enklare” för konsumenterna.

Ett workflow-erbjudande kan exempelvis börja innehålla organisationens specifika regler för ärendeprioritering. En integrationsplattform kan börja transformera och tolka verksamhetens domänobjekt. En gemensam dataplattform kan bli den plats där begrepp och affärsregler bestäms, trots att plattformsteamet saknar verksamhetsmandat.

Detta skapar två problem.

För det första blir den gemensamma plattformen svårare att återanvända eftersom den inte längre är generell.

För det andra flyttas verksamhetsansvaret bort från den domän som har bäst förutsättningar att förstå och förändra det.

En användbar tumregel är:

> En gemensam plattform får gärna bära generella tekniska mekanismer, men den bör vara försiktig med att bära verksamhetsspecifik mening och beslut.

En messagingplattform kan exempelvis ansvara för leverans, autentisering, retention och observerbarhet. Den bör normalt inte bestämma vad en verksamhetshändelse betyder.

En regelplattform kan erbjuda exekvering, versionshantering och spårbarhet för regler. Den verksamhetsdomän som använder plattformen bör däremot äga själva regelinnehållet.

Detta är ett konkret exempel på ansvarsfördelningen från kapitel 7:

```text
Gemensam nivå
  definierar spelplan och tvärgående krav
          ↓
Förmågeområde
  erbjuder generell mekanism och vägledning
          ↓
Domän/lösning
  äger verksamhetens mening och tillämpning
```

## Gemensamma kontrakt utan gemensam intern modell

Interoperabilitet kräver ofta gemensamma kontrakt, men detta betyder inte att alla interna modeller måste vara identiska.

Anta att två domäner behöver utbyta information om ett beslut. Domän A kanske använder en intern modell med ett tiotal objekt och detaljerade statusar. Domän B behöver bara veta beslutets identitet, utfall, datum och vilken part det gäller.

Det finns då inget självklart värde i att Domän B ska använda Domän A:s fullständiga interna modell.

Ett bättre alternativ kan vara att definiera ett explicit integrationskontrakt:

```text
Domän A:s interna modell
          ↓
   publicerat kontrakt
          ↓
Domän B:s egen modell
```

Detta gör båda domänerna friare att förändras internt.

Principen är viktig eftersom organisationer annars lätt skapar en ”enterprise canonical model” som alla system måste anpassa sig till. En sådan modell kan vara värdefull för vissa stabila, verkligt gemensamma begrepp och kodverk, men blir problematisk om den försöker ersätta all lokal semantik.

Målet är inte maximal enhetlighet. Målet är tillräcklig gemensam förståelse vid gränsen.

## Integrationsgränsen är en del av domändesignen

Integration betraktas ibland som ett tekniskt problem som kommer efter att systemen är designade. Men gränsen mellan domäner är i sig ett arkitekturbeslut.

Det behöver bland annat avgöras:

- vem initierar kommunikationen,
- vem äger kontraktet,
- vilken information får lämna domänen,
- vilken koppling konsumenten får till producentens interna modell,
- hur förändringar versioneras,
- vilken konsistens som krävs,
- och vad som händer om den andra domänen inte är tillgänglig.

Dessa frågor påverkar sedan valet mellan API, meddelanden, events, filutbyte och andra mekanismer. Därför bör domängränsen förstås före integrationsmönstret.

Detta är ett återkommande samband genom boken:

```text
Ansvar och domängräns
          ↓
Informationskontrakt
          ↓
Kvalitetskrav
          ↓
Integrationsmönster
          ↓
Teknisk realisering
```

Att börja längst ned i kedjan – exempelvis med frågan ”ska vi använda Kafka eller REST?” – riskerar att lösa fel problem.

## Autonomi kräver tydliga gränser

Organisationer vill ofta att produktteam ska vara autonoma. Men autonomi uppstår inte bara genom att man säger att teamen får fatta beslut själva.

Ett team kan endast vara verkligt autonomt om det är tydligt:

- vilka beslut teamet äger,
- vilka kontrakt det måste respektera,
- vilka beroenden det har,
- vilken information det får förändra,
- och vilka gemensamma mekanismer det kan konsumera utan manuell samordning.

Otydliga gränser skapar därför motsatsen till autonomi. Teamet måste fråga andra innan varje förändring eftersom ingen vet vem som har mandat.

Detta leder till en viktig paradox:

> Tydliga gränser begränsar vissa lokala val men ökar den praktiska friheten inom gränsen.

Ett team som äger sin domänmodell, sina regler och sin interna implementation kan förändra mycket snabbt om gränssnitten mot omvärlden är stabila. Ett team som delar databas och verksamhetslogik med fem andra team kan ha stor formell frihet men mycket liten faktisk autonomi.

## Federation när ett ansvar är gemensamt men kunskapen lokal

Vissa frågor passar varken för full lokal autonomi eller full centralisering. Då kan ett federerat arbetssätt vara lämpligt.

Anta att flera domäner använder samma centrala begrepp – exempelvis person, organisation eller geografisk plats – men med olika perspektiv. Organisationen behöver kanske en gemensam kärna, gemensamma identifierare och vissa gemensamma kvalitetsregler. Samtidigt måste varje domän kunna utöka informationen med lokala egenskaper.

Ett federerat ansvar kan då innebära:

- gemensamma minsta definitioner,
- tydligt ägarskap för kärninformationen,
- lokalt ansvar för domänspecifika utvidgningar,
- gemensamma kontrakt för utbyte,
- och ett forum där förändringar i gränssnitt eller gemensam semantik samordnas.

Federation är alltså inte kompromiss i betydelsen otydlighet. Tvärtom kräver en federerad modell ofta ännu tydligare gränser och ansvar än en central modell.

## Anti-pattern: den centrala allt-i-allo-tjänsten

Ett återkommande arkitekturproblem är en central tjänst som successivt får ansvar för allt som flera system råkar behöva.

Den kan börja som en enkel gemensam kundtjänst men får med tiden ansvar för:

- kundidentitet,
- kontaktuppgifter,
- preferenser,
- behörigheter,
- avtal,
- ärendehistorik,
- dokument,
- notifieringar,
- sökning,
- och verksamhetsregler.

På pappret ser detta ut som återanvändning. I praktiken blir tjänsten ofta en organisatorisk flaskhals och semantisk monolit.

Alla domäner behöver förändra den. Ingen enskild domän kan längre utvecklas utan att samordna sig med centraltjänsten. Tjänstens datamodell fylls med specialfall och begrepp som betyder olika saker för olika konsumenter.

Problemet är inte att tjänsten är central i sig. Problemet är att dess ansvar saknar sammanhängande gräns.

En bättre modell kan vara att skilja mellan:

- verkligt gemensamma identitets- och referensdata,
- domänspecifik information,
- generella tekniska tjänster,
- och integrationskontrakt mellan dessa delar.

Det ger fler komponenter men färre otydliga ansvar.

## Anti-pattern: delad databas som integrationsmodell

En annan vanlig genväg är att flera domäner eller applikationer delar samma databas och använder varandras tabeller direkt.

Det kan vara effektivt i början. Man slipper API:er, meddelanden och duplicering av data. Men priset blir ofta att databasschemat utvecklas till ett dolt gemensamt kontrakt.

När Domän A ändrar en tabell kan Domän B gå sönder. När båda behöver ändra samma kolumn blir ägarskapet oklart. Databasens tekniska struktur börjar styra verksamhetens gränser.

Det innebär inte att varje modul alltid behöver en separat fysisk databas. Det viktiga är att det logiska ägarskapet och åtkomsten är tydligt avgränsade.

Två moduler kan ligga i samma databasinstans men ändå använda separata scheman och endast kommunicera genom definierade gränssnitt. Omvänt kan två tjänster ha separata databaser men ändå vara starkt kopplade om de ständigt måste samordna sina modeller och releaser.

Fysisk separation är därför ett verktyg – inte definitionen av en bra gräns.

## Hur man hittar bättre gränser

Det finns ingen mekanisk metod som alltid ger rätt domängränser, men ett antal frågor är praktiskt användbara.

### Vilka begrepp hör naturligt ihop?

Om samma begrepp används med samma betydelse och regler är det ett argument för sammanhållning. Om ordet betyder olika saker kan det vara ett tecken på olika kontexter.

### Vilka regler förändras av samma anledning?

Om flera regler nästan alltid förändras tillsammans bör de sannolikt ägas tillsammans.

### Vem har kunskap och mandat?

Om inget tydligt verksamhetsansvar finns blir den tekniska gränsen svår att förvalta oavsett hur snygg modellen är.

### Vilken information är auktoritativ var?

Otydligt informationsägarskap är ofta ett symptom på otydliga domängränser.

### Var uppstår mest samordning?

Om två team måste synkronisera nästan varje förändring kan gränsen ligga fel – eller kontraktet mellan dem vara för instabilt.

### Vilken variation är legitim?

Om två områden har olika regler därför att verksamheten faktiskt skiljer sig ska arkitekturen inte nödvändigtvis eliminera skillnaden.

### Vilka beroenden bör vara riktade?

En tydlig producent–konsumentrelation är ofta lättare att hantera än två domäner som ömsesidigt känner till varandras interna modeller.

Dessa frågor bör användas som hypoteser, inte som absoluta regler. Precis som förmågekartan behöver domängränser kunna justeras när organisationen lär sig mer.

## En praktisk modell: från ansvar till teknik

När en ny lösning eller ett nytt verksamhetsområde ska designas kan följande ordning vara användbar:

```text
1. Identifiera verksamhetsansvar
        ↓
2. Identifiera centrala begrepp och regler
        ↓
3. Formulera domängränser och ägarskap
        ↓
4. Beskriv informationsutbyte mellan gränser
        ↓
5. Identifiera kvalitetskrav för gränssnitten
        ↓
6. Välj mönster och gemensamma förmågor
        ↓
7. Välj plattformar och teknisk realisering
```

Denna ordning kompletterar den gemensamma arkitekturmodell som etablerats tidigare i boken.

Gemensam arkitektur svarar på vilka byggstenar och ramar som organisationen kan återanvända. Domänanalysen svarar på vilket ansvar som ska byggas med dem.

Båda perspektiven behövs.

## Tre ansvarsnivåer – nu med domänperspektivet

Den tredelade ansvarmodellen från kapitel 7 kan nu preciseras ytterligare.

### Gemensam arkitektur

Den gemensamma nivån bör bland annat:

- definiera hur domäner och ansvar relaterar till den gemensamma förmågemodellen,
- skapa gemensamma regler för interoperabilitet och kontrakt,
- identifiera verkligt gemensamma begrepp där sådan samordning behövs,
- undvika att gemensamma plattformar tar över verksamhetens domänansvar,
- och synliggöra systemiska beroenden mellan flera domäner.

### Förmågeområde

Ett förmågeområde bör:

- erbjuda generella mekanismer som flera domäner kan använda,
- definiera vad konsumenten respektive plattformen ansvarar för,
- skapa mönster och standarder som respekterar domängränser,
- undvika verksamhetsspecifik logik i generella tjänster,
- och ge stöd för säkra, observerbara och förändringsbara gränssnitt.

### Lösning eller produkt

Den verksamhetsnära lösningen bör:

- äga sin domänmodell och verksamhetslogik,
- tydliggöra sina bounded contexts eller motsvarande ansvarssnitt,
- definiera vilka data den är auktoritativ för,
- publicera och konsumera kontrakt vid domängränser,
- och använda gemensamma plattformar utan att flytta bort sitt verksamhetsansvar.

Detta gör ansvarsfördelningen mer konkret. Det gemensamma området äger inte verksamhetsdomänen, men det skapar spelregler och byggstenar som gör domänerna möjliga att utveckla självständigt.

## Gränsen är en hypotes som måste prövas

Det är frestande att tro att det finns en perfekt domänmodell som kan ritas fram i ett tidigt arkitekturprojekt och därefter förbli stabil. I praktiken är gränser ofta hypoteser.

Tecken på att en gräns bör omprövas kan vara:

- återkommande synkroniserade releaser,
- stora mängder gemensam verksamhetslogik,
- samma information ändras från flera håll,
- många översättningar mellan två modeller som egentligen är identiska,
- en central komponent fylls med domänspecifika specialfall,
- ett team behöver ständigt beslut från ett annat team för att förändra sin egen produkt,
- eller ett ”gemensamt” begrepp orsakar fler konflikter än det löser.

Det motsatta kan också inträffa. Två områden som separerats kan visa sig ha så stark cohesion att uppdelningen skapar mer koordinering än självständighet.

Arkitekturens mål är därför inte maximalt antal gränser, utan gränser som gör ansvar och förändring begripliga.

## Sammanfattning

Gemensamma IT-förmågor och domäner kompletterar varandra men löser olika problem.

Förmågemodellen beskriver vilket återanvändbart IT-stöd organisationen behöver kunna erbjuda. Domänperspektivet beskriver var verksamhetens egen mening, regler, information och förändringsansvar hör hemma.

De viktigaste principerna i kapitlet är:

- en gemensam IT-förmåga är inte en verksamhetsdomän,
- domäner bör formas kring sammanhängande ansvar och förändring,
- bounded contexts gör lokal semantik och begreppsbetydelse explicit,
- hög cohesion inom en gräns och kontrollerad coupling mellan gränser underlättar förändring,
- informationsägarskap måste skiljas från teknisk åtkomst och fysisk lagring,
- gemensamma plattformar bör bära generella mekanismer snarare än verksamhetsspecifik mening,
- interoperabilitet kräver gemensamma kontrakt men inte nödvändigtvis en enda intern modell,
- tekniska gränser som API:er, processer och databaser ska inte användas som ersättning för ansvarsdiskussionen,
- autonomi kräver tydliga ansvarssnitt,
- och domängränser ska behandlas som prövbara arkitekturhypoteser, inte som eviga sanningar.

I nästa kapitel flyttas fokus från själva ansvarssnitten till det som passerar genom dem: information och data som arkitekturella ingångsvärden. Där blir frågan vem som äger ett begrepp, en informationsmängd eller en auktoritativ källa ännu mer konkret – innan vi senare går vidare till den tekniska förmågan för lagring och datahantering.

## Källor och vidare läsning

**[K1]** Eric Evans, *Domain-Driven Design Reference* (2015), särskilt Strategic Design och Bounded Context. https://www.domainlanguage.com/ddd/reference/
