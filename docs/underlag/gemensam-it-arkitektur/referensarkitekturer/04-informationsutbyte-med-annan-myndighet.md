# Referensarkitektur: Informationsutbyte med annan myndighet

## Syfte

Ge gemensam arkitekturell utgångspunkt för strukturerat och säkert informationsutbyte mellan myndigheten och andra offentliga organisationer.

## Typiska behov

- säker kommunikation över organisationsgräns
- tydliga kontrakt och ansvar
- kvittens och spårbarhet
- certifikat och teknisk trust
- strukturerade meddelanden eller filer
- robust hantering av avbrott

## Berörda förmågor

Primära:
- Integration och kommunikation
- Identitet och tillit

Stödjande:
- Data- och informationshantering
- Driftbarhet och motståndskraft
- Process, workflow och ärendehantering

## Logisk struktur

```text
Internt verksamhetssystem
   ↓
Integrations-/utbytestjänst
   ↓
Säker kommunikation / myndighetsgemensam tjänst
   ↓
Extern myndighet
```

## Rekommenderade lösningsmönster

- Asynkron meddelandekommunikation
- Tjänsteidentitet
- Observability för distribuerade tjänster
- System of record och härledda kopior

## Typiska plattformserbjudanden

- Secure Government Connectivity
- Structured Government Exchange
- Enterprise Messaging
- Managed File Transfer om sådan tjänst etableras
- PKI / Certificate Service
- Service Identity
- Central Logging Service

## Möjliga realiseringar

- SGSI där kommunikationsbehovet motsvarar tjänstens egenskaper
- SHS där lokal tjänst och användningsmodell motsvarar strukturerat utbyte

## Viktiga kvalitetsdimensioner

- säkerhet och informationsskydd
- spårbarhet
- regelefterlevnad
- interoperabilitet
- kontinuitet

## Arkitekturval att göra

- API, message eller fil?
- synkront eller asynkront?
- krav på kvittens?
- krav på ordering?
- vilka certifikat/trustrelationer krävs?
- hur hanteras mottagarens otillgänglighet?
- hur länge får data köas?

## Viktig reservation

Exakt användning av SGSI och SHS måste verifieras mot myndighetens faktiska lokala implementation och gällande tjänstebeskrivningar.
