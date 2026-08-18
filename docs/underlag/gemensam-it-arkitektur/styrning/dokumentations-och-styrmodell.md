# Dokumentations- och styrmodell

## Syfte

Dokumentations- och styrmodellen beskriver hur olika arkitekturartefakter används, hur de relaterar till varandra och hur dokumentationen hålls konsistent över tid.

## Huvudprincip

Förmågedokumenten är arkitekturens stabila ingång och huvudsakliga navigationsstruktur.

Detaljerade mönster, plattformar, standarder och teknisk dokumentation ska ligga separat och länkas från relevanta förmågor.

## Artefakttyper

### Arkitekturprinciper
Stabila, teknikoberoende ställningstaganden.

### Krav och styrande riktlinjer
Normativ styrning. Det ska vara tydligt vad som är obligatoriskt, varför det gäller och hur avsteg hanteras.

### Guidelines och vägledning
Rekommendationer och beslutsstöd. Ska hjälpa utvecklingsområden att förstå när och varför ett val är lämpligt.

### Lösningsmönster
Återanvändbara lösningar på återkommande arkitekturproblem. Ligger separat eftersom de ofta berör flera förmågor.

### Plattformar och tjänsteerbjudanden
Konsumerbara erbjudanden med tydligt syfte, målgrupp, kvalitetsprofil, ansvar och begränsningar.

### Tekniska standarder
Beslutade teknikval och konventioner. Hålls separat från de mer stabila förmågedokumenten.

### Referensarkitekturer
Tvärgående rekommenderade lösningsstrukturer. Tas fram när förmåge- och plattformsbilden är tillräckligt stabil.

### Teknisk referensdokumentation
Implementations- och konfigurationsnära dokumentation för plattformar, produkter och standarder.

## Förmågedokument

Varje förmågedokument ska innehålla:

1. Syfte, omfattning och relationer
2. Behov och användningsområden
3. Förmågespecifika arkitekturprinciper
4. Krav och styrande riktlinjer
5. Guidelines och vägledning
6. Plattformar och tjänsteerbjudanden
7. Standarder och teknikval
8. Relaterade artefakter och kvalitetsdimensioner

Lösningsmönster, referensarkitekturer och teknisk referensdokumentation ska normalt inte skrivas in i fulltext i förmågedokumentet.

## Normativ nivå

Följande ord bör användas konsekvent:

- **ska** – obligatoriskt krav
- **bör** – rekommenderat arbetssätt där avvikelse kan vara motiverad
- **kan** – tillåtet alternativ eller möjlighet

En guideline ska inte använda "ska" utan att det verkligen är avsett som ett styrande krav.

## Spårbarhet

Styrande krav bör där det är relevant kunna spåras till:

- verksamhetsbehov
- gemensamt organisatoriskt krav
- regulatoriskt krav
- säkerhetskrav
- beslutad arkitekturprincip
- uttrycklig plattformsbegränsning

## Förändring och livscykel

Förmågor och gemensamma principer förväntas förändras långsamt.

Plattformar, standarder, produkter och versionsinformation förväntas förändras snabbare och ska därför hållas separerade.

## Avsteg

Enskilda avsteg ska inte lagras som löpande innehåll i förmågedokumenten.

Förmågedokumenten ska däremot ge vägledning om när standardlösningen kan vara olämplig och hänvisa till myndighetens gemensamma process för arkitekturbeslut och avsteg.

Återkommande avsteg ska användas som återkoppling för att förbättra riktlinjer, plattformar eller standarder.

## Metadata

Separata artefakter bör minst ha:

- titel
- artefakttyp
- status
- ansvarig
- berörda förmågor
- relevanta kvalitetsdimensioner
- livscykelstatus
- senast reviderad

Metadata kan senare formaliseras i front matter om dokumentationen publiceras i ett dokumentationsverktyg.
