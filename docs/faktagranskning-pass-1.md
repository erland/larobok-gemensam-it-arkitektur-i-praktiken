# Faktagranskning – pass 1

Datum: 2026-08-19

## Syfte
Detta pass verifierar externa och tidskänsliga sakpåståenden efter helhetsrevisionen. Fokus ligger på standarders aktuella status, etablerad terminologi och påståenden som kan förändras över tid. Bokens egna modeller och rekommendationer granskas separat som interna arbetsramverk och ska inte förväxlas med externa standarder.

## Samlad bedömning
Inga större sakfel hittades som kräver omstrukturering eller omfattande omskrivning. Två mindre textjusteringar gjordes:

1. Kapitel 14 tidsstämplar DMN-statusen till 19 augusti 2026. DMN 1.5 är fortsatt senaste formella version hos OMG; 1.6 och 1.7 är betaversioner.
2. Kapitel 33 beskriver FOCUS bredare som standardisering av faktureringsdata och relaterade kostnads-/användningsbegrepp. FOCUS 1.4, ratificerad 4 juni 2026, omfattar fler dataset än enbart kostnad och användning.

I övrigt behövde de kontrollerade kapitlen inte ändras sakligt.

## Verifierade områden och primärkällor

### Kvalitet, kontinuitet och tillförlitlighet
- ISO/IEC 25010:2023 är aktuell produktkvalitetsmodell och omfattar nio kvalitetskarakteristika.
- NIST SP 800-34 Rev. 1 används fortsatt som relevant källa för kontinuitetsplanering och RTO/RPO-begrepp.
- Google SRE:s material används som källa för SLI/SLO-terminologi och den praktiska rollen för SLO:er.
- OpenTelemetry beskriver observability via telemetri och har stöd för bland annat traces, metrics och logs; projektet har dessutom profiler som en signaltyp. Boken gör inte anspråk på att loggar/metrics/traces är en uttömmande lista över all telemetri.

### Process och beslut
- OMG BPMN 2.0.2 är fortsatt den aktuella formella BPMN-versionen i OMG:s register.
- OMG CMMN 1.1 är fortsatt formell CMMN-version.
- OMG DMN 1.5 är senaste formellt antagna version; 1.6 och 1.7 är betaversioner per 2026-08-19.

### Tillgänglighet
- WCAG 2.2 är fortsatt W3C Recommendation och normativ WCAG 2-standard. WCAG 3.0 är under utveckling och ersätter inte WCAG 2.2 som normativ standard i nuläget.

### Data och distribuerade system
- PostgreSQLs aktuella dokumentation verifierar standardbegreppen transaktionsisolering, MVCC, backup och restore/PITR som de används i bokens teknikoberoende resonemang.
- Cache-aside-definitionen verifierades mot Microsoft Azure Architecture Center: applikationen hämtar data vid cache miss och fyller cachen på begäran.
- Eventual consistency används i boken som en konsistensmodell med fördröjd synlighet, inte som en garanti för en viss produkt.

### Integration och messaging
- RFC 9110 verifierar HTTP:s idempotens-/retrysemantik: automatisk retry av icke-idempotenta metoder kräver kunskap om att operationen faktiskt är idempotent eller inte har tillämpats.
- CloudEvents verifierar att event kan beskrivas i ett gemensamt, protokollagnostiskt format; specifikationen definierar inte i sig leveransgarantier eller säkerhetsmodell.
- MQTT 5.0 verifierar att publish/subscribe-protokoll kan ha explicit QoS-/leveranssemantik. Boken generaliserar inte MQTT:s nivåer till alla meddelandesystem.

### Runtime och containers
- OCI Image Specification och Runtime Specification verifierar separationen mellan image-format och container-runtime.
- Kubernetes aktuella dokumentation verifierar skillnaden mellan liveness-, readiness- och startup-probes samt att readiness kan ta en instans ur tjänstens trafikrouting utan att samma sak som liveness behöver inträffa.
- Boken använder dessa som exempel på runtimekontrakt, inte som universella krav för all applikationsexekvering.

### Identitet och tillit
- NIST SP 800-63-4 är aktuell Digital Identity Guidelines sedan 1 augusti 2025 och skiljer identity proofing, authentication och federation.
- OpenID Connect Core 1.0 incorporating errata set 2 (2023) är fortsatt den centrala OIDC Core-specifikationen.
- RFC 9700 / BCP 240 är aktuell Best Current Practice för OAuth 2.0-säkerhet.
- RFC 8705 är fortsatt relevant för OAuth mTLS-klientautentisering och certifikatbundna access tokens.

### AI och RAG
- RAG:s grundmodell är fortsatt förenlig med Lewis et al. (2020): retrieval kombineras med generering och externa kunskapskällor.
- NIST AI RMF 1.0 och NIST AI 600-1 Generative AI Profile är fortsatt publicerade referenser. NIST anger samtidigt att AI RMF 1.0 är under revision, vilket gör området fortsatt publiceringskänsligt.
- Bokens råd om utvärdering, mänsklig kontroll och begränsad autonomi presenteras som riskbaserade arkitekturprinciper, inte som påståenden om en specifik modell eller leverantör.

### Software supply chain
- NIST SP 800-218 (SSDF 1.1) är fortsatt slutlig publicerad SSDF-version; NIST SP 800-218 Rev. 1 / SSDF 1.2 är fortfarande draft i NIST:s register per 2026-08-19.
- SLSA 1.2 är aktuell specifikation och innehåller Build Track och Source Track. Bokens resonemang om build provenance är fortsatt korrekt.
- SPDX-projektet har 3.x-generationen som aktuell utvecklingslinje; boken nämner formatet utan versionslåsning.
- Sigstore/Cosign är fortsatt exempel på signering/verifiering och transparensbaserad supply-chain-integritet. Boken gör inte implementationen till universellt krav.

### Plattformsteknik
- CNCF TAG App Delivery Platforms White Paper stödjer bokens kärnidéer om självservice, användarupplevelse, dokumentation/onboarding, minskad kognitiv last, valfrihet/komponerbarhet och secure-by-default.
- Samma CNCF-material använder golden path-templates som ett exempel på återanvändbar onboarding och beskriver platform teams som ansvariga för användarbehov, roadmap och gränssnitt.
- CNCF:s Platform Engineering Maturity Model använder både golden paths/paved roads och självservice. Terminologin varierar fortfarande i branschen; boken definierar därför sina egna användningar explicit.

### FinOps och ekonomi
- Aktuella FinOps Framework har domäner för Understand Usage & Cost, Quantify Business Value, Optimize Usage & Cost och Manage the FinOps Practice, med capabilities som bland annat Forecasting, Unit Economics och Architecting & Workload Placement.
- FOCUS 1.4 är senaste ratificerade version per 2026-08-19 och definierar en gemensam struktur för billing data, inklusive fler dataset än bara kostnad och användning.
- Boken använder FinOps och FOCUS som inspirations-/interoperabilitetsramverk, inte som obligatoriska organisationsmodeller.

### Arkitekturbeskrivning och referensarkitektur
- ISO/IEC/IEEE 42010:2022 är aktuell standard för architecture description och viewpoints/views.
- Bokens definition av referensarkitektur kvarstår som praktisk arbetsdefinition. ISO/IEC/IEEE 42024 om architecture foundations/reference architectures är under utveckling och bör inte behandlas som en färdig normativ standard ännu.

## Punkter som fortsatt bör bevakas inför faktisk publicering
Följande behöver inte blockera språkputs, men bör verifieras igen om publiceringen sker väsentligt senare än 2026-08-19:

- AI RMF och GenAI-relaterad NIST-vägledning, eftersom AI RMF 1.0 är under revision.
- NIST SSDF, eftersom version 1.2 ligger som draft.
- OAuth/OIDC-profiler, särskilt nya profiler för federation, DPoP/key binding och högsäkerhets-API:er.
- DMN-status om OMG hinner formalisera 1.6 eller 1.7.
- FOCUS-version och FinOps Framework.
- WCAG 3.0:s utveckling, även om WCAG 2.2 fortsatt är normativ standard i nuläget.
- ISO/IEC/IEEE 42024:s utveckling mot eventuell färdig standard.
- Organisationsspecifika rättsliga krav kring low-code, produktivitets-AI, informationsklassning, arkivering/gallring och offentlig verksamhet. Dessa kan inte faktagranskas universellt utan den specifika organisationens regelverk och jurisdiktion.

## Resultat
Faktagranskning pass 1 bedöms klar. Manuset kan gå vidare till språk- och stilrevision. Ett kort aktualitetspass bör fortfarande göras direkt före publicering för de ovan markerade tidskänsliga områdena.
