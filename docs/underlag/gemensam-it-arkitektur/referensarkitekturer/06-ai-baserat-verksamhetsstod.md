# Referensarkitektur: AI-baserat verksamhetsstöd

## Syfte

Ge gemensam arkitekturell utgångspunkt för verksamhetsnära AI-funktioner som sammanfattning, klassificering, kunskapsstöd, rekommendation eller beslutsstöd.

## Typiska behov

- generativ AI
- semantisk sökning
- RAG
- klassificering eller prediktion
- användargränssnitt för AI-stöd
- källhänvisning
- mänsklig kontroll
- modell-/promptspårbarhet

## Berörda förmågor

Primära:
- Analys, sökning och AI
- Data- och informationshantering
- Identitet och tillit

Vanliga tillägg:
- Interaktion, presentation och kanaler
- Regler och beslut
- Process, workflow och ärendehantering
- Integration och kommunikation
- Driftbarhet och motståndskraft

## Logisk struktur

```text
Användare / process
      ↓
AI-tjänst / assistent
      ├─ LLM / ML-modell
      ├─ RAG / sökindex
      ├─ regler/guardrails
      └─ godkända verktyg/API:er
             ↓
      mänsklig kontroll vid behov
```

## Rekommenderade lösningsmönster

- RAG
- AI med mänsklig kontroll
- Externaliserade verksamhetsregler
- System of record och härledda kopior
- Tjänsteidentitet
- Observability för distribuerade tjänster

## Typiska plattformserbjudanden

- Managed LLM Service
- RAG/Knowledge Service
- Search and Indexing Service
- Business Rules Platform
- Service Identity
- API Management
- Central Logging Service
- Metrics, Monitoring and Tracing

## Viktiga kvalitetsdimensioner

- säkerhet och informationsskydd
- spårbarhet och verifierbarhet
- regelefterlevnad
- förvaltningsbarhet
- kostnadseffektivitet
- prestanda

## Arkitekturval att göra

- deterministic regel eller AI?
- extern eller intern modell?
- behövs RAG?
- vilka informationskällor är tillåtna?
- behöver människa godkänna resultatet?
- hur mäts kvalitet?
- vilka modell-/promptversioner behöver spåras?
- vilka verktyg får en agent använda?

## Begränsning

AI-resultat ska inte ges högre tillit än källor, modell och utvärdering motiverar.
