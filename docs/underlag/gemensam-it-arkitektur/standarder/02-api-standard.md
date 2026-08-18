# Teknisk standard: API

## Syfte
Skapa konsekventa och förvaltningsbara API:er mellan självständiga system och tjänster.

## Typ
Arkitektur- och teknikstandard

## Relaterade förmågor
- Integration och kommunikation
- Identitet och tillit
- Driftbarhet och motståndskraft

## Standard
- HTTP-baserade API:er ska använda etablerade HTTP-semantiker.
- API-kontrakt ska dokumenteras maskinläsbart där det är lämpligt.
- Felmodeller ska vara konsekventa.
- Versionsstrategi och bakåtkompatibilitet ska vara definierade.
- Korrelations-ID ska stödjas när end-to-end-spårbarhet krävs.
- Autentisering och auktorisation ska använda godkända identitetsstandarder.

## Rekommenderat format
- JSON för vanliga REST-liknande API:er om inget annat behov motiverar annat.
- OpenAPI för kontraktsbeskrivning där REST/HTTP används.

## Avgränsning
Standarden styr gränssnittets egenskaper, inte intern implementation.
