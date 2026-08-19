# Lösningsmönster: Build once, promote many

## Syfte

Bygga en releaseartefakt en gång och därefter promovera exakt samma artefakt genom test-, acceptans- och produktionsmiljöer.

## Problem

Om programvaran byggs om per miljö går det inte längre att vara säker på att den produktionssatta artefakten är samma artefakt som testades.

## Struktur

```text
Källkod
  ↓
Build + test
  ↓
Versionsmärkt artefakt
  ├─ test
  ├─ acceptans
  └─ produktion
```

## Förutsättningar

- miljöspecifik konfiguration separeras från artefakten
- artefakter lagras i kontrollerat register
- version och källa är spårbara

## Berörda förmågor

Primärt:
- Programvaruutveckling och leverans

Sekundärt:
- Applikationsexekvering och runtime
- Identitet och tillit
