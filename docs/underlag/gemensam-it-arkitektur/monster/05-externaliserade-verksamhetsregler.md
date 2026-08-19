# Lösningsmönster: Externaliserade verksamhetsregler

## Syfte

Separera verksamhetsregler som behöver egen livscykel, spårbarhet eller återanvändning från applikationens övriga programkod.

## Problem

Regler som är spridda i kod kan vara svåra att förstå, återanvända och förändra när de har hög verksamhetsmässig betydelse.

## När mönstret passar

- samma regel används i flera sammanhang
- regelverket förändras ofta
- verksamheten behöver kunna granska regeln
- regelversion behöver kunna kopplas till historiskt beslut
- beslutstabeller eller deklarativa modeller passar väl

## När mönstret inte passar

- logiken är liten och lokal
- regeln följer samma livscykel som applikationskoden
- en regelmotor skulle öka komplexiteten utan tydlig nytta

## Berörda förmågor

Primärt:
- Regler och beslut

Sekundärt:
- Process, workflow och ärendehantering
- Integration och kommunikation
- Data- och informationshantering
