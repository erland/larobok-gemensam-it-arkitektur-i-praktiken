# Referensarkitektur: Containerbaserad tjänst

## Syfte

Ge gemensam arkitekturell utgångspunkt för moderna backendtjänster som paketeras som containers och körs på gemensam containerplattform.

## Typiska behov

- stateless exekvering
- horisontell skalning
- automatiserad deployment
- standardiserad observability
- tjänsteidentitet och secrets
- snabb återstart

## Berörda förmågor

Primära:
- Applikationsexekvering och runtime
- Programvaruutveckling och leverans
- Driftbarhet och motståndskraft

Stödjande:
- Identitet och tillit
- Integration och kommunikation
- Data- och informationshantering

## Logisk struktur

```text
Git
 ↓
CI/CD
 ↓
Containerimage
 ↓
Artifact Repository
 ↓
Container Application Platform
   ├─ Service Identity / Secrets
   ├─ API / Messaging
   ├─ Data Services
   └─ Observability
```

## Rekommenderade lösningsmönster

- Containeriserad stateless tjänst
- Build once, promote many
- Tjänsteidentitet
- Observability för distribuerade tjänster
- Backup och verifierad återställning där persistent data finns

## Typiska plattformserbjudanden

- Source Code Management
- CI/CD Platform
- Artifact Repository
- Container Application Platform
- Service Identity
- Secrets Management
- Central Logging Service
- Metrics, Monitoring and Tracing
- API Management eller Enterprise Messaging vid behov
- Relationell databastjänst eller annan datatjänst vid behov

## Möjlig realisering

- OpenShift som Container Application Platform
- Jenkins som CI/CD Platform

## Viktiga kvalitetsdimensioner

- förvaltningsbarhet
- tillgänglighet
- skalbarhet
- säkerhet
- spårbarhet
- livscykel

## Arkitekturval att göra

- stateless eller stateful?
- resursprofil?
- autoscaling?
- nätverks- och exponeringsmodell?
- rollback eller roll-forward?
- vilka health checks krävs?

## Begränsning

Containerisering är inte ett mål i sig. Workloads med OS-nära beroenden eller leverantörskrav kan passa bättre på annan runtime.
