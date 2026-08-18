# Lösningsmönster

## Syfte

Denna katalog innehåller återanvändbara lösningsmönster som identifierats under framtagandet av de gemensamma IT-förmågorna.

Ett mönster ska beskriva ett återkommande arkitekturproblem och ett återanvändbart sätt att lösa det. Mönster är **inte produkter**, **inte plattformstjänster** och **inte referensarkitekturer**.

Mönster kan beröra flera förmågor. De placeras därför separat från förmågedokumenten.

## Urvalskriterier

En kandidat har fått ett eget mönsterdokument när den:

- återkommer i flera lösningar eller förmågor
- beskriver ett faktiskt arkitekturproblem, inte bara en teknisk funktion
- är tillräckligt stabil och teknikoberoende
- har tydliga situationer där den passar respektive inte passar
- ger verkligt beslutsstöd för utvecklingsområden

Kandidater som är för produktspecifika, för små eller främst hör hemma som teknisk standard har inte fått egna dokument i detta steg.

## Konsoliderade mönster

### Interaktion
- [Backend for Frontend](01-backend-for-frontend.md)

### Process och regler
- [Human workflow](04-human-workflow.md)
- [Externaliserade verksamhetsregler](05-externaliserade-verksamhetsregler.md)

### Data
- [System of record och härledda kopior](06-system-of-record-och-harledda-kopior.md)
- [Cache-aside](07-cache-aside.md)

### Integration
- [Asynkron meddelandekommunikation](02-asynkron-meddelandekommunikation.md)
- [Publicera/prenumerera](03-publicera-prenumerera.md)

### AI
- [Retrieval-Augmented Generation (RAG)](08-rag.md)
- [AI med mänsklig kontroll](09-ai-med-mansklig-kontroll.md)

### Identitet
- [Tjänsteidentitet](10-tjansteidentitet.md)

### Runtime och leverans
- [Containeriserad stateless tjänst](11-containeriserad-stateless-tjanst.md)
- [Build once, promote many](12-build-once-promote-many.md)

### Driftbarhet och motståndskraft
- [Observability för distribuerade tjänster](13-observability-for-distribuerade-tjanster.md)
- [Backup och verifierad återställning](14-backup-och-verifierad-aterstallning.md)

### Arbetsplats
- [Kontrollerad samarbetsyta](15-kontrollerad-samarbetsyta.md)

## Kandidater som inte fick eget dokument i steg 12

Följande typer av kandidater behålls tills vidare i förmågedokumentens arbetsanteckningar eller behandlas senare som standard, plattform eller del av annat mönster:

- mycket konkreta deploymentvarianter som rolling och blue/green
- enskilda retry-/circuit breaker-/bulkhead-mekanismer
- API Facade och Gateway när de främst är plattforms-/teknikval
- schema migration som främst kan bli teknisk standard/vägledning
- specifika accesskontrollmodeller som RBAC/ABAC
- tekniska nätverksmönster på lägre realiseringsnivå
- enskilda Power Platform-/produktivitetsmönster
- patterns som endast förekommer i ett smalt specialfall

De kan få egna dokument senare om referensarkitekturer eller plattformskatalogen visar att de behöver återanvändas självständigt.

## Relation till referensarkitekturer

Referensarkitekturer ska kunna kombinera flera av dessa mönster.

Exempel:

```text
Referensarkitektur: Internt handläggningsstöd
  ├─ Backend for Frontend
  ├─ Human workflow
  ├─ Externaliserade verksamhetsregler
  ├─ System of record och härledda kopior
  ├─ Tjänsteidentitet
  └─ Observability för distribuerade tjänster
```

Referensarkitekturer tas fram först i ett senare steg.
