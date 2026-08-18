# Referensarkitektur: Integrationsintensivt verksamhetssystem

## Syfte

Ge en gemensam arkitekturell utgångspunkt för system som utbyter stora mängder information med många interna eller externa system och där integration är en central del av lösningen.

## Typiska behov

- många API-beroenden
- asynkron messaging
- events
- filutbyte
- externa myndighetskopplingar
- robust felhantering
- korrelation och felsökning
- versionshantering av kontrakt

## Berörda förmågor

Primära:
- Integration och kommunikation
- Data- och informationshantering
- Driftbarhet och motståndskraft

Stödjande:
- Identitet och tillit
- Process, workflow och ärendehantering
- Applikationsexekvering och runtime

## Logisk struktur

```text
          ┌─ API-part
          ├─ Messaging-part
Domän ────┼─ Eventkonsument/producent
          ├─ Filutbyte
          └─ Extern myndighetstjänst
```

Gemensamt:
- tjänsteidentiteter
- kontrakt och versioner
- retry/idempotens
- korrelation
- central observability

## Rekommenderade lösningsmönster

- Asynkron meddelandekommunikation
- Publicera/prenumerera
- System of record och härledda kopior
- Tjänsteidentitet
- Observability för distribuerade tjänster
- Backend for Frontend där användargränssnitt finns

## Typiska plattformserbjudanden

- API Management
- Enterprise Messaging
- Data Integration / ETL
- Secure Government Connectivity
- Structured Government Exchange
- Service Identity
- PKI / Certificate Service
- Central Logging Service
- Metrics, Monitoring and Tracing

## Viktiga kvalitetsdimensioner

- interoperabilitet
- tillgänglighet
- kontinuitet
- spårbarhet
- prestanda
- säkerhet
- förändringsbarhet

## Arkitekturval att göra

- synkron API eller asynkron messaging?
- event eller kommando?
- direkt integration eller mellanliggande plattform?
- hur hanteras dubbletter?
- vilken ordering krävs?
- hur fungerar fallback vid extern otillgänglighet?
- vilka kontrakt får förändras utan samtidiga releaser?

## Begränsning

Integrationsplattformen ska inte bli systemets domänmodell eller verksamhetsprocessmotor.
