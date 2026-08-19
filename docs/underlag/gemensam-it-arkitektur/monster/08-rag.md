# Lösningsmönster: Retrieval-Augmented Generation (RAG)

## Syfte

Grunda generativ AI i godkända och aktuella informationskällor genom att söka fram relevant underlag och skicka detta som kontext till en språkmodell.

## Struktur

```text
Fråga
  ↓
Sökning / retrieval
  ↓
Relevant källmaterial
  ↓
Språkmodell
  ↓
Svar + källreferenser
```

## När mönstret passar

- språkmodellen behöver myndighetsspecifik kunskap
- information ändras oftare än modellens grundträning
- källhänvisning och verifierbarhet är viktiga
- dokumentmängden är för stor för statisk prompt

## Viktiga designfrågor

- godkända källor
- accesskontroll
- dokumentlivscykel
- chunkning och embeddings
- aktualitet
- källreferenser
- utvärdering av retrieval och svarskvalitet

## Berörda förmågor

Primärt:
- Analys, sökning och AI

Sekundärt:
- Data- och informationshantering
- Identitet och tillit
- Integration och kommunikation
- Driftbarhet och motståndskraft
