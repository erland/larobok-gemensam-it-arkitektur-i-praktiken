# Lösningsmönster: AI med mänsklig kontroll

## Syfte

Använda AI/ML som beslutsstöd eller automatiseringskomponent samtidigt som en människa behåller kontroll över betydelsefulla eller osäkra utfall.

## När mönstret passar

- felaktigt AI-resultat kan få betydande konsekvens
- modellen har osäkerhet som behöver bedömas
- verksamhetsbeslut kräver mänsklig bedömning
- AI används för rekommendation, prioritering eller klassificering

## Struktur

```text
AI/ML-resultat
      ↓
osäkerhet + underlag
      ↓
mänsklig granskning
      ↓
beslut/åtgärd
```

## Viktiga designfrågor

- när mänsklig kontroll krävs
- hur osäkerhet presenteras
- vilka källor och förklaringar visas
- hur feedback används
- hur beslut loggas

## Berörda förmågor

Primärt:
- Analys, sökning och AI

Sekundärt:
- Regler och beslut
- Process, workflow och ärendehantering
- Interaktion, presentation och kanaler
