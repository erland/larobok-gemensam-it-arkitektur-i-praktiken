# Teknisk standard: Container

## Syfte
Standardisera paketering och grundkrav för containeriserade workloads.

## Typ
Teknikstandard

## Relaterade förmågor
- Applikationsexekvering och runtime
- Programvaruutveckling och leverans

## Standard
- OCI-kompatibla containerimages ska användas.
- Images ska vara reproducerbart byggda.
- Miljöspecifik konfiguration och secrets ska externaliseras.
- Basimages ska komma från godkända källor.
- Onödiga paket och privilegier ska undvikas.
- Health checks ska definieras när plattformen använder dem.
- Persistent verksamhetsdata ska inte vara beroende av ephemeral containerdisk.

## Livscykel
Godkända base images och versioner hålls separat.
