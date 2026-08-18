# Plattformar och tjänsteerbjudanden

## Syfte

Denna katalog beskriver konsumerbara IT-erbjudanden som utvecklingsområden kan använda för att realisera behov inom de gemensamma IT-förmågorna.

Ett tjänsteerbjudande ska beskriva **vad konsumenten får**, vilka behov det stödjer, vilka kvaliteter som erbjuds, vilka begränsningar som finns och hur ansvaret delas mellan konsument och plattformsområde.

Produkten eller tekniken som används under erbjudandet är en **realisering**, inte själva tjänstebegreppet.

## Grundmodell

```text
Förmåga
   ↓
Plattform/tjänsteerbjudande
   ↓
Tekniska byggblock
   ↓
Produkt / version / konfiguration
```

Exempel:

```text
Applikationsexekvering och runtime
   ↓
Container Application Platform
   ↓
containerorkestrering + noder + nät + storage
   ↓
OpenShift + RHEL + konfiguration
```

## Konsoliderade erbjudanden

### Interaktion
- [Web Application Framework](01-web-application-framework.md)
- [Design System](02-design-system.md)

### Process och regler
- [Workflow/Process Platform](03-workflow-process-platform.md)
- [Case Management Platform](04-case-management-platform.md)
- [Business Rules Platform](05-business-rules-platform.md)

### Data
- [Relationell databastjänst](06-relationell-databastjanst.md)
- [Object Storage Service](07-object-storage-service.md)
- [Cache Service](08-cache-service.md)

### Analys, sökning och AI
- [Search and Indexing Service](09-search-indexing-service.md)
- [Business Intelligence and Reporting](10-bi-reporting-service.md)
- [Managed LLM Service](11-managed-llm-service.md)
- [RAG/Knowledge Service](12-rag-knowledge-service.md)

### Integration och kommunikation
- [API Management](13-api-management.md)
- [Enterprise Messaging](14-enterprise-messaging.md)
- [Data Integration / ETL](15-data-integration-etl.md)
- [Secure Government Connectivity](16-secure-government-connectivity.md)
- [Structured Government Exchange](17-structured-government-exchange.md)

### Identitet och tillit
- [Workforce Identity](18-workforce-identity.md)
- [Service Identity](19-service-identity.md)
- [PKI / Certificate Service](20-pki-certificate-service.md)
- [Secrets Management](21-secrets-management.md)

### Runtime
- [Container Application Platform](22-container-application-platform.md)
- [Java Application Runtime](23-java-application-runtime.md)
- [Virtual Machine Runtime](24-virtual-machine-runtime.md)

### Driftbarhet och motståndskraft
- [Central Logging Service](25-central-logging-service.md)
- [Metrics, Monitoring and Tracing](26-monitoring-tracing-service.md)
- [Backup and Recovery Service](27-backup-recovery-service.md)

### Programvaruutveckling och leverans
- [Source Code Management](28-source-code-management.md)
- [CI/CD Platform](29-ci-cd-platform.md)
- [Artifact Repository](30-artifact-repository.md)
- [Developer Tooling](31-developer-tooling.md)

### Arbetsplats, samarbete och produktivitet
- [Productivity Suite](32-productivity-suite.md)
- [Collaboration and Workspace Services](33-collaboration-workspace.md)
- [Productivity AI Assistant](34-productivity-ai-assistant.md)
- [Low-Code Productivity Platform](35-low-code-productivity-platform.md)

## Konsolideringsbeslut

Flera kandidater från förmågedokumenten har slagits ihop:

- **Metrics and Monitoring**, **Distributed Tracing** och delar av **Operational Dashboard** samlas tills vidare i `Metrics, Monitoring and Tracing`.
- **Backup Service** och **Restore Service / Recovery Support** samlas i `Backup and Recovery Service`.
- **Work Queue Service** betraktas tills vidare som en del av Workflow/Process eller Case Management snarare än eget plattformserbjudande.
- **Decision Service** betraktas tills vidare som en tjänsteprofil på Business Rules Platform.
- **File Storage Service** tas inte upp som eget förstahandserbjudande innan konkreta behov visar att det inte kan täckas av Object Storage, Shared File Service eller arbetsplatsytor.
- **Linux Runtime** behandlas som teknisk profil/realisering under VM/andra runtimeerbjudanden.
- **Web/Proxy Runtime** behandlas tills vidare som realiseringskomponent under runtime eller kommunikation, inte som eget centralt erbjudande.
- **Microsoft 365** ses som ett sammansatt SaaS-erbjudande som realiserar flera tjänster i arbetsplatskategorin.
- **Power Platform** ses som en tvärgående plattform vars komponenter kan realisera flera förmågor.

## Produktkopplingar

| Produkt/teknik | Primärt tjänsteerbjudande |
|---|---|
| Angular | Web Application Framework |
| Microsoft Office / Microsoft 365 | Productivity Suite |
| RHEL | Virtual Machine Runtime / tekniskt byggblock |
| JBoss EAP | Java Application Runtime |
| JBoss Core Services | runtime-/proxyrealisering, ännu ej eget erbjudande |
| Jenkins | CI/CD Platform |
| IntelliJ IDEA | Developer Tooling |
| JPA | teknisk standard, inte plattform |
| Oracle Database | Relationell databastjänst |
| Elasticsearch | Search and Indexing Service |
| Power BI | Business Intelligence and Reporting |
| SQL Server | Relationell databastjänst |
| Microsoft SSIS | Data Integration / ETL |
| Ceph | realisering/byggblock för Object Storage m.m. |
| OpenShift | Container Application Platform |
| Trådlöst nätverk | kommunikationstjänst; ännu inte eget katalogdokument i denna första konsolidering |
| SGSI | Secure Government Connectivity |
| SHS | Structured Government Exchange, under lokal verifiering |
| IBM MQ | Enterprise Messaging |
| Power Platform | Low-Code Productivity Platform + tvärgående realisering |

## Livscykel

Varje tjänsteerbjudande bör i nästa mognadsfas kompletteras med:

- ansvarig tjänsteägare
- status: planerad / pilot / rekommenderad / standard / avveckling
- kvalitetsprofiler
- SLA/SLO där relevant
- beställnings-/anslutningsprocess
- kostnadsmodell där relevant
- produktrealisering och versioner
- supporthorisont
- kända begränsningar
