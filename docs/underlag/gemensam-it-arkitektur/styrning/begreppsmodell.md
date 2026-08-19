# Begreppsmodell

## Syfte

Begreppsmodellen skapar en gemensam terminologi för dokumentationen.

## Behov

Ett behov beskriver något som verksamheten eller ett IT-stöd behöver kunna uppnå.

Behov ska så långt som möjligt uttryckas utan att i förväg låsa teknisk realisering.

## Krav

Ett krav beskriver en egenskap eller ett resultat som måste uppfyllas.

Krav kan komma från verksamhetsbehov, gemensamma organisatoriska krav, regulatoriska krav eller andra dokumenterade källor.

## Kvalitetsdimension

En tvärgående egenskap som används för att uttrycka exempelvis säkerhet, tillgänglighet, prestanda eller kontinuitet.

## Förmåga

En generell IT-förmåga som det stödjande IT-området kan erbjuda stöd för.

Exempel: Data- och informationshantering eller Integration och kommunikation.

Förmågan är oberoende av en viss produkt.

## Plattformstjänst

Ett konkret återanvändbart erbjudande som utvecklingsområden kan konsumera.

Exempel: Container Application Platform, Relationell databastjänst eller Enterprise Messaging.

## Tekniskt byggblock

En generisk teknisk beståndsdel som används för att realisera en eller flera plattformstjänster.

Exempel: operativsystem, router, brandvägg, databasmotor, objektlagring eller reverse proxy.

## Produkt

En konkret teknisk produkt eller implementation.

Exempel: OpenShift, RHEL, IBM MQ eller Oracle Database.

## Arkitekturprincip

Ett relativt stabilt vägledande ställningstagande för hur arkitekturval bör göras.

## Krav eller styrande riktlinje

Normativ styrning som anger något som måste eller förväntas följas.

## Guideline / vägledning

Rekommenderande stöd för val och avvägningar. En guideline är inte automatiskt ett obligatoriskt krav.

## Lösningsmönster

Ett återanvändbart sätt att lösa ett återkommande och relativt avgränsat arkitekturproblem.

Mönster kan spänna över flera förmågor.

## Referensarkitektur

En sammanhängande rekommenderad struktur för en viss typ av lösning eller IT-stöd.

Referensarkitekturer spänner normalt över flera förmågor, plattformar och mönster.

## Teknisk standard

Ett gemensamt beslutat teknikval eller en teknisk konvention.

## Teknisk referensdokumentation

Detaljerad dokumentation om hur en plattform, produkt eller standard används, konfigureras eller integreras.

## Begränsning

En faktisk constraint hos en plattform, produkt, miljö eller extern tjänst.

En begränsning är inte automatiskt ett generellt krav på alla IT-stöd.

## Avsteg

Ett medvetet beslut att inte följa ett etablerat krav, standardval eller rekommenderat arbetssätt i en specifik situation.

## Realiseringskedja

```text
Förmåga
   ↓
Plattformstjänst
   ↓
Tekniskt byggblock
   ↓
Produkt / version / konfiguration
```
