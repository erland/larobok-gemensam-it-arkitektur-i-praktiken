# Register- och korsreferenssynk efter revision av Del IV

Datum: 2026-08-20
Utgångspunkt: revision 98
Omfattning: kapitel 23–27, `docs/begreppsregister.yaml`, `chapters/begreppsregister.md` samt explicita kapitelhänvisningar inom och till Del IV.

## Syfte

Efter komprimeringen och omstruktureringen av Del IV kontrollerades att begreppsregistrets markeringar och kompletterande kapitelhänvisningar fortfarande motsvarar den faktiska texten, och att kapitelhänvisningar inte pekar på resonemang som har försvunnit eller flyttats.

## Korrigeringar

En markeringskoppling behövde läggas till eftersom begreppet fortfarande är kursiverat i den reviderade texten:

- **Tjänsteidentitet** som lösningsmönster: kapitel 23.

En kompletterande relation togs bort eftersom den efter revisionen inte längre ger en konkret behandling av registerbegreppet:

- **Internt handläggningsstöd**: kapitel 23 togs bort. Kapitel 23 beskriver fortfarande hur referensarkitekturer relaterar till lösningsmönster, men behandlar inte längre referensarkitekturen Internt handläggningsstöd som sådan.

Övriga relationer till kapitel 23–27 behölls när kapitlen fortfarande ger tydlig kompletterande behandling även om registertermens exakta formulering inte används. Det gäller bland annat process-, regel- och datförmågorna i kapitel 25 samt Enterprise Messaging, Service Identity, Secrets Management och Container Application Platform i de mönsterkapitel där deras problemområde faktiskt behandlas.

## Läsbart register

De två metadataändringarna påverkar inte de kapitelnummer som visas i `chapters/begreppsregister.md`: Tjänsteidentitet har redan samma huvudsakliga och kompletterande behandlingskapitel i det läsbara registret, och kapitel 23 låg utanför de fem kompletterande kapitel som visades för Internt handläggningsstöd. Ingen synlig registerrad behövde därför ändras.

## Explicita kapitelhänvisningar

De explicita hänvisningarna inom Del IV kontrollerades:

- kapitel 24 hänvisar fortfarande korrekt till driftmönstren i kapitel 27,
- kapitel 25 hänvisar fortfarande korrekt till integrationsmönstren i kapitel 24 och driftmönstren i kapitel 27,
- kapitel 26 hänvisar fortfarande korrekt till Human workflow i kapitel 25.

Inga explicita hänvisningar från senare kapitel till kapitel 23–27 behöver justeras.

## Resultat

Del IV:s register- och korsreferenser är synkade med den reviderade texten. Ingen manusändring eller synlig ändring av det läsbara registret krävs.
