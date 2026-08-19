# Plattform/tjänsteerbjudande: Cache Service

## Syfte
Tillhandahålla snabb, återuppbyggbar lagring för kortlivad eller härledd data.

## Primär förmåga
- Data- och informationshantering

## Sekundära förmågor
- Driftbarhet och motståndskraft
- Applikationsexekvering och runtime

## Typiska behov
- minska latency
- avlasta bakomliggande datakälla
- sessionsnära eller temporär data

## Konsumentansvar
- definiera TTL/invalidation
- hantera stale data
- säkerställa att cache inte blir system of record

## Begränsningar
Cache får inte användas som enda lagring för verksamhetskritisk persistent information.
