# Plattform/tjänsteerbjudande: Enterprise Messaging

## Syfte
Tillhandahålla robust asynkron meddelandekommunikation mellan system.

## Primär förmåga
- Integration och kommunikation

## Typiska behov
- köbaserad kommunikation
- buffring
- robust leverans
- lösare tidskoppling

## Möjlig realisering
- IBM MQ

## Konsumentansvar
- meddelandekontrakt
- idempotens
- retrystrategi
- verksamhetssemantik

## Plattformsansvar
- queue managers/brokers
- teknisk redundans
- monitorering
- kapacitet

## Begränsningar
Messagingplattformen ska inte bära verksamhetsprocesslogik.
