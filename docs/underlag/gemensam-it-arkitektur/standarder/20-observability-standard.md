# Teknisk standard: Observability

## Syfte
Standardisera grundläggande telemetri för applikationer och distribuerade tjänster.

## Typ
Teknikstandard

## Relaterade förmågor
- Driftbarhet och motståndskraft
- Integration och kommunikation
- Applikationsexekvering och runtime

## Standard
- Loggar ska vara strukturerade där plattformen stödjer det.
- Gemensam korrelationsmekanism ska användas för distribuerade flöden när relevant.
- Metrics ska ha konsekventa namn och labels.
- Health checks ska skilja på readiness/liveness där plattformen använder detta.
- Distributed tracing ska användas när behovet av end-to-end-felsökning motiverar det.
- Secrets och onödiga skyddsvärda data får inte loggas.

## Avgränsning
Exakt agent/collector eller observabilityprodukt hör till plattformsrealiseringen.
