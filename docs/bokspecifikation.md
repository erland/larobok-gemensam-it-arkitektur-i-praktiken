# Bokspecifikation

## Titel och undertitel
**Titel:** Gemensam IT-arkitektur i praktiken  
**Undertitel:** Från behov och förmågor till mönster, plattformar, standarder och referensarkitekturer

## Bokprofil
- `book_kind`: `factbook`
- `book_type`: `subject_overview`
- Motivering: Boken ska ge en systematisk och fördjupad förståelse av ett arkitekturområde. Den ska vara pedagogisk men inte bygga på övningsprogression eller kursmoment.

## Språk och författare
- Språk: svenska
- Författare: Erland Lindmark

## Ämne och syfte
Boken ska förklara hur en större organisation kan strukturera och styra gemensam IT-arkitektur utan att börja i produkter. Den följer kedjan från verksamhets- och IT-stödsbehov via kvalitetskrav och gemensamma IT-förmågor till lösningsmönster, plattformstjänster, tekniska standarder och referensarkitekturer.

Syftet är både att ge en stabil begreppsmodell och att visa hur modellen används för verkliga arkitekturbeslut, styrning, plattformsutveckling och lösningsarkitektur. Boken ska också göra etableringsordningen explicit och tydligt skilja mellan vad som bör beslutas på gemensam arkitekturnivå, vad som bör ägas av respektive förmågeområde och vad som hör hemma i konkreta lösningar och produkter.

## Målgrupp
Primär målgrupp:
- enterprise-, verksamhets-, informations-, lösnings- och IT-arkitekter
- plattformsansvariga och plattformsproduktägare
- tekniska ledare och utvecklingsledare
- personer som ansvarar för tekniska standarder, governance eller gemensamma IT-tjänster

Sekundär målgrupp:
- produktägare och chefer som behöver förstå arkitekturens styrlogik
- utvecklare och tekniska specialister som vill förstå varför gemensamma plattformar och standarder ser ut som de gör

## Nivå eller faktadjup
Erfaren till avancerad. Boken ska kunna läsas av en tekniskt kunnig läsare utan att kräva specialistkunskap inom alla delområden. Centrala begrepp ska förklaras innan djupare resonemang introduceras.

## Omfattning och avgränsningar
Planerad omfattning: cirka 300–450 boksidor beroende på slutligt exempel- och diagraminnehåll.

Boken ska:
- fördjupa den modell som finns i källmaterialet
- komplettera med områden som beslutsmetodik, domänarkitektur, plattform-as-a-product, governance, livscykel, säkerhet och praktisk tillämpning
- använda teknik- och produktnamn sparsamt och främst som exempel
- hålla den stabila arkitekturmodellen åtskild från snabbt föränderliga produktval

Boken ska inte vara:
- en produktkatalog för en viss organisation
- en komplett handbok i TOGAF, DDD, ITIL, säkerhetsarkitektur eller plattformsteknik
- en detaljerad implementationsguide för enskilda tekniker

## Ton och stil
- saklig, tydlig och resonemangsdriven
- praktiskt orienterad utan att bli receptbok
- många konkreta exempel och jämförelser
- diagram och tabeller används där de förklarar relationer bättre än löptext
- undvik konsultjargong när ett enklare svenskt uttryck fungerar

## Faktaboksspecifikt
- Ämnesbredd/fördjupning: bred modell med selektiv djupdykning i beslutspunkter och tvärgående frågor
- Form: främst förklarande ämnesöversikt, med referensartade delar
- Centrala faktaområden: behovsdriven arkitektur, förmågemodell, kvalitetsattribut, arkitekturbeslut, domän- och informationsperspektiv, lösningsmönster, plattformstjänster, standarder, referensarkitekturer, governance, säkerhet, resiliens och livscykel
- Källkrav: primärkällor och officiell dokumentation för standarder och tidskänsliga tekniska fakta; etablerad facklitteratur och originalkällor för arkitekturmetoder
- Tidskänslighet: bokens kärnmodell ska vara långlivad. Produkter, versionskrav, standardversioner och aktuella rekommendationer ska behandlas som tidskänsliga exempel.
- Synliga referenser: nej som standard i löptext; samlad källförteckning/noter kan införas senare om det förbättrar trovärdighet och spårbarhet

## Omslag och illustrationer
- Omslagsbild: ännu inte beslutad.
- Inre illustrationer: avstängda tills vidare. Arkitekturdiagram kan senare skapas som funktionella figurer snarare än dekorativa illustrationer.

## Återkommande exempel/case/berättargrepp
Boken använder återkommande exempel från en tänkt större myndighet/organisation:
- internt handläggningsstöd
- publik e-tjänst
- integrationsintensivt verksamhetssystem
- informationsutbyte med extern part
- containerbaserad tjänst
- AI-baserat verksamhetsstöd
- digital arbetsplats

Exemplen ska visa samma arkitekturbegrepp från olika perspektiv och synliggöra avvägningar snarare än ett enda facit.

## Kvalitetskriterier
- Begreppen förmåga, behov, kvalitet, mönster, plattform, standard, byggblock, produkt och referensarkitektur används konsekvent.
- Boken skiljer tydligt mellan generell modell och organisationsspecifik realisering.
- Varje större tekniskt råd förklarar varför och vilka trade-offs som finns.
- Tvärgående frågor som säkerhet, resiliens, kostnad och livscykel integreras i resonemangen.
- Praktiska exempel visar hur modellen används från behov till beslut.
- Etableringsordning och ansvar följer den tredelade modellen gemensam arkitektur → förmågeområde → lösning/produkt, utan att beskrivas som ett strikt vattenfall.
