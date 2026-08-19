# Innehålls-canon

## Gemensam profil
- Språk: svenska
- book_kind: factbook
- book_type: subject_overview
- Nivå/faktadjup: erfaren–avancerad
- Läsarprofil: arkitekter, plattformsansvariga, tekniska ledare och styrande roller i större IT-organisationer
- Ton: saklig, tydlig, resonerande och praktiskt förankrad

## Terminologi och fasta definitioner
| Begrepp | Första kapitel | Definition | Kommentar |
|---|---:|---|---|
| Behov | 2 | Ett önskat resultat eller problem som IT-stödet behöver bidra till att lösa. | Ska inte förväxlas med ett redan valt tekniskt svar. |
| Kvalitetsattribut | 4 | En mätbar eller bedömningsbar egenskap hos en lösning, exempelvis tillgänglighet, prestanda eller säkerhet. | Används som drivkraft för arkitekturval. |
| Gemensam IT-förmåga | 8 | Något ett stödjande IT-område varaktigt behöver kunna erbjuda stöd inom. | Skild från verksamhetsförmåga och enskild plattform. |
| Lösningsmönster | 23 | Ett återanvändbart sätt att strukturera en lösning i en återkommande kontext med tydliga avvägningar. | Är vägledning, inte komplett lösningsdesign. |
| Plattformstjänst | 28 | Ett konsumerbart tekniskt erbjudande med definierat värde, gränssnitt och ansvar. | Produkten är realisering, inte själva förmågan. |
| Teknisk standard | 31 | Ett styrande eller rekommenderat val som skapar kompatibilitet, konsekvens eller kontrollerad variation. | Standardnivå måste anges. |
| Referensarkitektur | 34 | En återanvändbar arkitektur för en klass av lösningar som visar struktur, principer och variation points. | Ska inte kopieras som färdig lösningsarkitektur. |

## Återkommande exempel, case eller berättargrepp
- En större myndighet används som neutral bakgrund för exempel.
- Sju återkommande lösningsscenarier återkommer från källmaterialet.
- Exempel ska illustrera beslut och avvägningar, inte organisationsspecifika sanningar.

## Arkitekturmodell som ska vara konsekvent genom boken
Behov → kvalitetskrav → gemensamma IT-förmågor → lösningsmönster/plattformstjänster → tekniska standarder/byggblock → produkter, versioner och konfiguration. Referensarkitekturer skär tvärs genom flera lager.

## Ansvarsnivåer som ska vara konsekventa genom boken
Boken skiljer mellan tre nivåer som inte får blandas ihop:

1. **Gemensam arkitektur** – äger spelplanen: gemensam begreppsmodell, förmågekarta och gränser, tvärgående principer och kvalitetsdimensioner, gemensamma regler för standarder/livscykel/avsteg samt formerna för hur artefakter beskrivs och hur beroenden hanteras.
2. **Förmågeområde** – äger fördjupningen inom ett avgränsat område: behov och användningsfall, förmågespecifika principer, lösningsmönster, plattformstjänster, relevanta standarder, golden paths, tekniklivscykel och beroenden till andra förmågor.
3. **Lösning/produkt** – äger den konkreta tillämpningen för ett verksamhetsbehov: lösningsarkitektur, val mellan tillåtna alternativ, kombination av gemensamma byggstenar, domänspecifika komponenter och implementation.

Grundprincip: **centralt definieras det som måste hänga ihop; förmågeansvar utvecklar innehållet inom dessa ramar; lösningsteam tillämpar och kombinerar.** Gemensam arkitektur ska därför inte detaljdesigna varje förmåga, och förmågeområden ska inte detaljdesigna varje verksamhetslösning.

## Etableringsprincip
Modellen ska beskrivas som iterativ, inte som ett vattenfall. Rekommenderat arbetssätt är top-down för sammanhang och prioritering, kombinerat med bottom-up-lärande från fördjupade förmågor och konkreta lösningar. Den första förmågekartan behöver vara tillräckligt bra för att kunna användas, men ska kunna ändras när ansvar, beroenden och praktiska erfarenheter blir tydligare.
