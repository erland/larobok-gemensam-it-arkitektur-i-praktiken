# Lösningsmönster: Asynkron meddelandekommunikation

## Syfte

Minska tidskoppling mellan producent och konsument genom att överföra meddelanden via en förmedlande messagingtjänst.

## Problem

Synkrona anrop kräver normalt att båda parter är tillgängliga samtidigt. Vid tillfälliga fel eller hög belastning kan detta skapa felkedjor och stark koppling.

## När mönstret passar

- mottagaren behöver inte svara omedelbart
- meddelanden behöver kunna buffras
- robust leverans är viktig
- producent och konsument ska kunna skalas oberoende
- arbetet kan utföras senare

## När mönstret inte passar

- användaren behöver omedelbart svar
- operationen är enkel och naturligt synkron
- verksamheten inte kan hantera eventual consistency

## Viktiga designfrågor

- leveransgaranti
- idempotens
- ordering
- retry
- dead-letter-hantering
- korrelation
- versionshantering av meddelanden

## Berörda förmågor

Primärt:
- Integration och kommunikation

Sekundärt:
- Process, workflow och ärendehantering
- Driftbarhet och motståndskraft
- Data- och informationshantering
