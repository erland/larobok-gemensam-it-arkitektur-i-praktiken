# Referensarkitektur: Publik e-tjänst

## Syfte

Ge gemensam arkitekturell utgångspunkt för internetexponerade digitala tjänster där externa användare lämnar uppgifter, följer ärenden eller utför myndighetsrelaterade aktiviteter.

## Typiska behov

- tillgängligt och responsivt webbgränssnitt
- extern autentisering eller identifiering
- säkra formulär
- uppladdning av dokument
- bakomliggande verksamhetslogik
- integration med interna system
- hög säkerhet och spårbarhet
- god tillgänglighet

## Berörda förmågor

Primära:
- Interaktion, presentation och kanaler
- Identitet och tillit
- Integration och kommunikation
- Data- och informationshantering

Vanliga tillägg:
- Process, workflow och ärendehantering
- Regler och beslut
- Applikationsexekvering och runtime
- Driftbarhet och motståndskraft

## Logisk struktur

```text
Extern användare
   ↓ HTTPS
Publikt webbgränssnitt
   ↓
BFF / API-lager
   ↓
Domän-/verksamhetstjänster
   ├─ identitet
   ├─ regler/beslut
   ├─ process
   ├─ data
   └─ interna/external integrationer
```

## Rekommenderade lösningsmönster

- Backend for Frontend
- Tjänsteidentitet
- System of record och härledda kopior
- Build once, promote many
- Observability för distribuerade tjänster
- Backup och verifierad återställning
- Human workflow där e-tjänsten initierar handläggning

## Typiska plattformserbjudanden

- Web Application Framework
- Design System
- External Identity / Federation när sådan tjänst etableras
- API Management
- Service Identity
- Relationell databastjänst
- Object Storage Service
- Container Application Platform
- Central Logging Service
- Metrics, Monitoring and Tracing
- CI/CD Platform

## Viktiga kvalitetsdimensioner

- säkerhet och informationsskydd
- tillgänglighet och användbarhet
- tillgänglighet
- prestanda
- skalbarhet
- spårbarhet
- kontinuitet

## Särskilda arkitekturfrågor

- behöver användaren identifieras eller kan tjänsten vara anonym?
- hur hanteras känsliga uppgifter i klienten?
- behövs session eller stateless interaktion?
- hur skyddas publika API:er?
- vilken DDoS-/edge-/gatewaylösning krävs?
- hur kopplas tjänsten till bakomliggande handläggning?

## Begränsning

Publik e-tjänst är en lösningstyp, inte ett produktpaket. Teknikval ska anpassas efter tjänstens risk, komplexitet och målgrupp.
