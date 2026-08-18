# Referensarkitektur: Digital arbetsplats

## Syfte

Ge gemensam arkitekturell utgångspunkt för intern digital arbetsmiljö med produktivitetsverktyg, samarbetsytor, dokumentdelning och AI-stöd.

## Typiska behov

- dokumentproduktion
- e-post och kalender
- teamytor
- dokumentdelning
- möten och chatt
- extern samverkan
- produktivitets-AI
- livscykel för arbetsytor

## Berörda förmågor

Primär:
- Arbetsplats, samarbete och produktivitet

Stödjande:
- Identitet och tillit
- Data- och informationshantering
- Analys, sökning och AI
- Integration och kommunikation

## Logisk struktur

```text
Intern användare
   ↓
Productivity Suite / Collaboration
   ├─ personliga arbetsytor
   ├─ teamytor
   ├─ e-post/möten
   └─ produktivitets-AI
        ↓
Gemensam identitet och informationsskydd
```

## Rekommenderade lösningsmönster

- Kontrollerad samarbetsyta
- System of record och härledda kopior
- AI med mänsklig kontroll där produktivitets-AI används för betydelsefulla underlag

## Typiska plattformserbjudanden

- Productivity Suite
- Collaboration and Workspace Services
- Productivity AI Assistant
- Low-Code Productivity Platform
- Workforce Identity

## Möjlig realisering

- Microsoft 365
- Teams
- SharePoint
- OneDrive
- Microsoft 365 Copilot eller annan godkänd tjänst
- Power Platform för avgränsade behov

## Viktiga kvalitetsdimensioner

- säkerhet och informationsskydd
- användbarhet och tillgänglighet
- regelefterlevnad
- livscykel
- portabilitet
- kostnadseffektivitet

## Arkitekturval att göra

- personlig eller gemensam yta?
- arbetsmaterial eller system of record?
- får extern delning ske?
- när blir low-code-lösningen ett verksamhetssystem?
- vilka AI-funktioner är tillåtna för vilken informationsklass?

## Begränsning

Digital arbetsplats ska inte ersätta verksamhetssystem när behovet kräver formell process, hög transaktionskontroll eller tydligt system of record.
