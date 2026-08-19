# Teknisk standard: Messaging och events

## Syfte
Skapa konsekventa kontrakt för asynkron kommunikation.

## Typ
Arkitektur- och teknikstandard

## Relaterade förmågor
- Integration och kommunikation
- Driftbarhet och motståndskraft

## Standard
Meddelanden och events bör ha:
- tydlig semantik
- versionsbar kontraktsmodell
- korrelationsmetadata där relevant
- unik meddelande-/eventidentitet när dubbletthantering kräver det
- tidsstämpel och producentinformation där relevant

Konsumenter ska designas för omleverans där plattformen kan leverera mer än en gång.

## Events
Verksamhetsevents bör beskriva något som redan inträffat och inte utformas som dold RPC.

## Produktkoppling
IBM MQ kan realisera Enterprise Messaging, men produktdetaljer hör till separat produkt-/plattformdokumentation.
