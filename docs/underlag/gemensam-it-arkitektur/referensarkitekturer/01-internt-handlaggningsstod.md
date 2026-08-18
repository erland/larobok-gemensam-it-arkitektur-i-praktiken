# Referensarkitektur: Internt handläggningsstöd

## Syfte

Ge en gemensam arkitekturell utgångspunkt för interna verksamhetssystem där handläggare arbetar med ärenden, uppgifter, beslut, dokument och integrationer över tid.

Referensarkitekturen är teknikneutral på övergripande nivå och visar vilka förmågor, mönster och tjänsteerbjudanden som typiskt kombineras.

## Typiska behov

- handläggning av ärenden över längre tid
- arbetsköer och uppgifter
- roll- och behörighetsstyrd åtkomst
- verksamhetsregler och beslut
- dokument och bilagor
- integration med flera interna eller externa system
- spårbarhet och historik
- hög driftbarhet

## Berörda förmågor

Primära:
- Interaktion, presentation och kanaler
- Process, workflow och ärendehantering
- Regler och beslut
- Data- och informationshantering

Stödjande:
- Integration och kommunikation
- Identitet och tillit
- Applikationsexekvering och runtime
- Driftbarhet och motståndskraft
- Programvaruutveckling och leverans

## Logisk struktur

```text
Handläggare
   ↓
Webbgränssnitt
   ↓
Backend for Frontend / API
   ↓
Domäntjänster
   ├─ Workflow / ärendehantering
   ├─ Regel-/beslutstjänst
   ├─ Verksamhetsdata
   ├─ Dokument
   └─ Integrationer
```

Tvärgående:
- identitet och behörighet
- loggning, metrics och tracing
- backup och återställning
- CI/CD
- tjänsteidentiteter

## Rekommenderade lösningsmönster

- Backend for Frontend
- Human workflow
- Externaliserade verksamhetsregler
- System of record och härledda kopior
- Tjänsteidentitet
- Observability för distribuerade tjänster
- Backup och verifierad återställning

## Typiska plattformserbjudanden

- Web Application Framework
- Design System
- Workflow/Process Platform eller Case Management Platform
- Business Rules Platform där behov finns
- Relationell databastjänst
- Object Storage Service för dokument/bilagor
- API Management och/eller Enterprise Messaging
- Workforce Identity
- Service Identity
- Container Application Platform eller Java Application Runtime
- Central Logging Service
- Metrics, Monitoring and Tracing
- Backup and Recovery Service
- CI/CD Platform

## Viktiga kvalitetsdimensioner

- säkerhet och informationsskydd
- tillgänglighet
- kontinuitet och återställningsförmåga
- spårbarhet och verifierbarhet
- användbarhet
- förvaltningsbarhet och förändringsbarhet

## Arkitekturval att göra per lösning

- workflowmotor eller vanlig applikationslogik?
- separat regelmotor eller domänlogik?
- dokumentlagring eller traditionell databas?
- synkron eller asynkron integration?
- container eller annan runtime?
- vilken tillgänglighets-/backup-profil krävs?

## Begränsning

Referensarkitekturen innebär inte att alla handläggningsstöd ska använda alla komponenter. Endast de delar som motiveras av behov ska användas.
