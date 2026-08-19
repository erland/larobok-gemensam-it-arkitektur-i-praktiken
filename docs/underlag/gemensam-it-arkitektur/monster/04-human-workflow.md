# Lösningsmönster: Human workflow

## Syfte

Kombinera automatiserade steg med manuella arbetsuppgifter i ett långlivat och spårbart verksamhetsflöde.

## Problem

Verksamhetsprocesser kan behöva vänta på mänsklig handläggning under timmar, dagar eller längre. Vanlig request/response-logik är olämplig för sådana flöden.

## När mönstret passar

- processen innehåller manuella aktiviteter
- arbetsuppgifter behöver tilldelas roller eller köer
- deadlines, eskalering eller påminnelser behövs
- processens status behöver följas över tid
- flödet måste kunna återupptas efter omstart

## När mönstret inte passar

- sekvensen är kortlivad och helt automatisk
- några få lokala UI-steg kan hanteras enklare i applikationen

## Struktur

```text
Process
 ├─ automatiskt steg
 ├─ human task → arbetskö/användare
 ├─ beslut
 └─ nästa steg
```

## Berörda förmågor

Primärt:
- Process, workflow och ärendehantering

Sekundärt:
- Interaktion, presentation och kanaler
- Regler och beslut
- Identitet och tillit
- Driftbarhet och motståndskraft
