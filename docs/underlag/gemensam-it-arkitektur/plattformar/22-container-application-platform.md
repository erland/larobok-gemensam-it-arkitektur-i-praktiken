# Plattform/tjänsteerbjudande: Container Application Platform

## Syfte
Tillhandahålla förvaltad exekveringsmiljö för containeriserade workloads.

## Primär förmåga
- Applikationsexekvering och runtime

## Sekundära förmågor
- Driftbarhet och motståndskraft
- Identitet och tillit
- Programvaruutveckling och leverans

## Typiska behov
- stateless backendtjänster
- skalbara containerapplikationer
- standardiserad deployment
- automatiserad restart

## Möjlig realisering
- OpenShift

## Konsumentansvar
- containerimage
- resursprofil
- health checks
- applikationskonfiguration

## Plattformsansvar
- kluster
- noder
- scheduler
- plattformsuppgraderingar
- basobservability
- nätverks- och identityintegration

## Begränsningar
Alla workloads lämpar sig inte för containerplattform.
