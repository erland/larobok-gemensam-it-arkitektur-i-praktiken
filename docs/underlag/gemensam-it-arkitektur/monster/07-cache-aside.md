# Lösningsmönster: Cache-aside

## Syfte

Förbättra prestanda och minska belastning på bakomliggande datakälla genom att läsa från cache när data finns och annars hämta från system of record.

## Struktur

```text
Applikation
  ├─ läs cache
  ├─ vid miss: läs primär källa
  └─ skriv resultat till cache
```

## När mönstret passar

- läsningar är betydligt vanligare än förändringar
- viss stale data kan tolereras
- datat kan återskapas från primär källa

## Risker

- stale data
- invalidation
- cache stampede
- oavsiktlig lagring av skyddsvärda data
- att cache blir ett otydligt system of record

## Berörda förmågor

Primärt:
- Data- och informationshantering

Sekundärt:
- Driftbarhet och motståndskraft
- Applikationsexekvering och runtime
