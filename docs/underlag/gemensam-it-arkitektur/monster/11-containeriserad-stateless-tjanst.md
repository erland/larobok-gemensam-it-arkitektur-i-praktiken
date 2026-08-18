# Lösningsmönster: Containeriserad stateless tjänst

## Syfte

Paketera en stateless applikation som en reproducerbar containerartefakt som kan skalas och ersättas oberoende av persistent verksamhetsdata.

## När mönstret passar

- backendtjänsten kan vara stateless
- horisontell skalning är relevant
- standardiserad containerplattform finns
- konfiguration kan externaliseras

## Riktlinjer

- persistent data lagras utanför lokal containerdisk
- konfiguration och secrets externaliseras
- readiness/liveness definieras
- kontrollerad shutdown stöds
- resursprofil dokumenteras
- samma image promoveras mellan miljöer

## Berörda förmågor

Primärt:
- Applikationsexekvering och runtime

Sekundärt:
- Programvaruutveckling och leverans
- Driftbarhet och motståndskraft
- Identitet och tillit
- Data- och informationshantering
