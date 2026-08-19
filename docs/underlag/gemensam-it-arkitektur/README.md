# Gemensam IT-arkitektur

## Syfte

Detta projekt innehåller en struktur för gemensam IT-arkitektur för en större statlig myndighet.

Målet är att stödja verksamhetsorienterade utvecklingsområden med en sammanhängande uppsättning:

- arkitekturprinciper
- krav och styrande riktlinjer
- guidelines och vägledning
- gemensamma IT-förmågor
- lösningsmönster
- plattformar och tjänsteerbjudanden
- tekniska standarder
- referensarkitekturer
- teknisk referensdokumentation

## Grundläggande riktning

Arkitekturen ska utgå från behov hos verksamhet och IT-stöd:

```text
Behov hos verksamhet och IT-stöd
            ↓
Krav och kvalitetsbehov
            ↓
Gemensamma IT-förmågor
            ↓
Plattformstjänster och lösningsmönster
            ↓
Tekniska byggblock
            ↓
Produkter och konfiguration
```

Tekniska realiteter kan skapa begränsningar, risker och kostnadsdrivare. Dessa ska beskrivas som sådana och inte automatiskt omvandlas till generella krav på utvecklingsområdena.

## Fyra perspektiv

### Förmågeperspektiv
Beskriver vad det stödjande IT-området kan hjälpa utvecklingsområdena med.

### Krav- och kvalitetsperspektiv
Beskriver vilka egenskaper IT-stöd och plattformar behöver kunna uppfylla.

### Artefaktperspektiv
Beskriver vilken typ av information som publiceras, exempelvis princip, riktlinje, guideline, plattform eller standard.

### Leverans- och realiseringsperspektiv
Beskriver hur en tjänst tillhandahålls, exempelvis intern plattform, SaaS, COTS eller extern tjänst.

## Katalogstruktur

```text
.
├── README.md
├── utvecklingsplan.md
├── styrning/
│   ├── gemensamma-arkitekturprinciper.md
│   ├── krav-och-kvalitetsdimensioner.md
│   ├── begreppsmodell.md
│   └── dokumentations-och-styrmodell.md
├── mallar/
│   └── formagedokument.md
├── formagor/
├── monster/
├── plattformar/
├── standarder/
├── referensarkitekturer/
└── teknisk-dokumentation/
```

## Status

Steg 0 och steg 1 är genomförda.

Skapat förmågedokument:

- `formagor/01-interaktion-presentation-kanaler.md`

Nästa steg är:

**Steg 2 – Process, workflow och ärendehantering**


## Aktuell status

Steg 0–16 är genomförda. Nästa steg är **Utvecklingsplanen steg 0–16 är genomförd.**.


## Version 1.0 – konceptuell arkitektur

Utvecklingsplanens steg 0–16 är genomförda.

Den sammanhållna modellen omfattar:

- 11 gemensamma IT-förmågor
- 15 konsoliderade lösningsmönster
- 35 plattforms- och tjänsteerbjudanden
- 25 tekniska standarder
- 7 referensarkitekturer

Se [slutlig korsgranskning](slutlig-korsgranskning.md) och [projektstatus](STATUS.md).

Nästa rekommenderade fas är att komplettera modellen med faktisk nulägesdata, tjänsteägare, produktversioner och support-/livscykelstatus.
