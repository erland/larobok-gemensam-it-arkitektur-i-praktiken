# Tekniska standarder

## Syfte

Standardkatalogen beskriver beslutade eller kandidata teknikval och tekniska konventioner som stödjer de gemensamma IT-förmågorna.

Standarderna ska hållas separerade från:
- förmågor
- plattformstjänster
- exakta produktversioner
- detaljerad konfiguration

## Standardtyper

### Arkitektur- och teknikstandard
Relativt stabil regel för hur en teknisk lösning bör utformas, exempelvis API-kontrakt, observability eller containerpaketering.

### Produktstandard
Anger en godkänd eller rekommenderad produktfamilj som realisering av ett tjänsteerbjudande, exempelvis OpenShift, JBoss EAP eller Power BI.

### Versions-/supportstandard
Anger exakta versioner, supportperioder och avvecklingsdatum. Dessa bör **inte** ligga i de stabila standarddokumenten utan i separat livscykel-/supportmatris.

### Konfigurationsstandard
Detaljerade tekniska inställningar, cipher suites, basimages, plugins, portkonfiguration osv. Dessa bör ligga närmare teknisk referensdokumentation.

## Konsoliderade standarder

### Interaktion
- [Web frontend](01-web-frontend-standard.md)

### Integration och kommunikation
- [API](02-api-standard.md)
- [Messaging och events](03-messaging-event-standard.md)
- [Nätverks- och tjänstekommunikation](24-teknisk-kommunikationsstandard.md)
- [Myndighetsgemensam kommunikation](25-sgsi-shs-produktstandard.md)

### Identitet och tillit
- [Identitets- och federationsprotokoll](04-identitetsprotokoll-standard.md)
- [Service identity](05-service-identity-standard.md)
- [Secrets](06-secrets-standard.md)

### Data
- [Java persistence](07-java-persistence-standard.md)
- [Relationella databaser](08-relationsdatabas-produktstandard.md)
- [Objektlagring](09-object-storage-realisering-standard.md)

### Analys
- [Sökplattform](10-search-platform-standard.md)
- [BI och rapportering](11-bi-platform-standard.md)

### Runtime
- [Container](12-container-standard.md)
- [Containerplattform / OpenShift](13-openshift-produktstandard.md)
- [Java Application Runtime / JBoss EAP](14-java-runtime-produktstandard.md)
- [Linux serveroperativsystem / RHEL](15-linux-os-produktstandard.md)

### Programvaruutveckling och leverans
- [CI/CD / Jenkins](16-ci-cd-produktstandard.md)
- [Developer tooling / IntelliJ IDEA](17-developer-tooling-standard.md)
- [Git och repository](18-git-repository-standard.md)
- [Release- och versionsidentifiering](19-release-version-standard.md)

### Driftbarhet och motståndskraft
- [Observability](20-observability-standard.md)
- [Backup och återställning](21-backup-recovery-standard.md)

### Arbetsplats
- [Microsoft 365](22-m365-produktstandard.md)
- [Power Platform governance](23-power-platform-governance-standard.md)

## Konsolideringsbeslut

Följande kandidater från förmågedokumenten har **inte** fått egna stabila standardfiler i detta steg:

- exakta Java-, Angular-, RHEL-, OpenShift-, JBoss- och produktversioner
- specifika base images
- Jenkins plugins
- exakta TLS-cipher suites
- produktspecifika installationsparametrar
- exakta retentionvärden
- konkreta CPU/minnesprofiler
- queue naming, topic naming och andra lokala konventioner som ännu inte är tillräckligt verifierade
- lokala SGSI/SHS-detaljer

Dessa bör hanteras i framtida versions-/supportmatris eller teknisk referensdokumentation.

## Produkt → tjänst → standard

| Produkt/teknik | Tjänsteerbjudande | Standard |
|---|---|---|
| Angular | Web Application Framework | Web frontend |
| JPA | Relationell databastjänst / Java-lösning | Java persistence |
| Oracle Database | Relationell databastjänst | Relationella databaser |
| SQL Server | Relationell databastjänst | Relationella databaser |
| Ceph | Object Storage Service m.fl. | Objektlagring |
| Elasticsearch | Search and Indexing Service | Sökplattform |
| Power BI | BI and Reporting | BI och rapportering |
| IBM MQ | Enterprise Messaging | Messaging och events |
| OpenShift | Container Application Platform | Container + OpenShift |
| JBoss EAP | Java Application Runtime | Java Application Runtime |
| RHEL | VM/runtimebyggblock | Linux serveroperativsystem |
| Jenkins | CI/CD Platform | CI/CD |
| IntelliJ IDEA | Developer Tooling | Developer tooling |
| Microsoft 365 | Productivity Suite/Workspace | Microsoft 365 |
| Power Platform | Low-Code Productivity Platform | Power Platform governance |
| SGSI / SHS | Government connectivity/exchange | Myndighetsgemensam kommunikation |

## Livscykelprincip

En standard ska inte behöva ändras varje gång en produkt får en ny minorversion.

Rekommenderad separation:

```text
Standard
  ↓
Godkänd produktfamilj
  ↓
Supportmatris
  ↓
Exakt version
  ↓
Teknisk konfiguration
```

## Nästa mognadssteg

Efter referensarkitekturerna bör en separat support-/livscykelmatris kunna skapas med:
- produkt
- aktuell rekommenderad version
- minsta stödda version
- supportslut
- planerad migrering
- ansvarig
