# Referensarkitekturer

## Syfte

Referensarkitekturerna beskriver återkommande lösningstyper som spänner över flera IT-förmågor, lösningsmönster, plattformar och tekniska standarder.

De ska fungera som **arkitekturella startpunkter**, inte som obligatoriska färdiga lösningar.

## Urvalskriterier

En referensarkitektur tas fram när lösningstypen:

- är vanlig eller strategiskt viktig
- berör flera förmågor
- återkommande kräver liknande arkitekturval
- vinner på gemensamma mönster och plattformserbjudanden
- har tillräckligt underlag från de tidigare stegen

## Framtagna referensarkitekturer

1. [Internt handläggningsstöd](01-internt-handlaggningsstod.md)
2. [Publik e-tjänst](02-publik-e-tjanst.md)
3. [Integrationsintensivt verksamhetssystem](03-integrationsintensivt-verksamhetssystem.md)
4. [Informationsutbyte med annan myndighet](04-informationsutbyte-med-annan-myndighet.md)
5. [Containerbaserad tjänst](05-containerbaserad-tjanst.md)
6. [AI-baserat verksamhetsstöd](06-ai-baserat-verksamhetsstod.md)
7. [Digital arbetsplats](07-digital-arbetsplats.md)

## Kandidater som inte fick egen referensarkitektur nu

Följande kandidater kan tas fram senare om det finns ett tydligt verksamhetsbehov:

- mobil operativ lösning
- geografiskt redundant verksamhetslösning
- batchintensivt verksamhetssystem
- dokumentintensivt verksamhetssystem
- low-code-baserat verksamhetsstöd
- privilegierad administrationsmiljö
- data- och analysplattform som egen lösningstyp

De bedömdes i detta steg vara antingen:
- för specialiserade
- delvis täckta av andra referensarkitekturer
- bättre att utforma först när konkreta plattformserbjudanden och behov är kända

## Hur referensarkitekturer ska användas

Utgå från relevant referensarkitektur och:

1. verifiera vilka behov som faktiskt finns
2. välj endast relevanta förmågor och mönster
3. välj plattformstjänster som matchar kvalitetskraven
4. dokumentera avvikelser och särskilda begränsningar
5. skapa lösningsspecifik arkitektur

Referensarkitekturen ska inte kopieras mekaniskt.

## Relation till övrig dokumentation

```text
Förmågor
   ↓
Mönster + plattformar + standarder
   ↓
Referensarkitektur
   ↓
Lösningsarkitektur för ett konkret IT-stöd
```
