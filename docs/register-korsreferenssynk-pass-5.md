# Register- och korsreferenssynk efter revision av Del V

Datum: 2026-08-20
Utgångspunkt: revision 105
Omfattning: kapitel 28–33, `docs/begreppsregister.yaml`, `chapters/begreppsregister.md` samt explicita kapitelhänvisningar inom och till Del V.

## Syfte

Efter revisionen av Del V kontrollerades att begreppsregistrets markeringar och kompletterande kapitelhänvisningar fortfarande motsvarar den faktiska texten, och att explicita kapitelhänvisningar inte pekar på resonemang som har försvunnit eller flyttats.

## Korrigeringar

En markeringskoppling behövde läggas till eftersom begreppet fortfarande är kursiverat som definierat arkitekturobjekt i den reviderade texten:

- **Applikationsexekvering och runtime** som förmåga: kapitel 32.

Övriga kursiverade registerobjekt i kapitel 28–33 hade redan korrekta markeringskopplingar. Förekomster av exempelvis observerbarhet, API, secrets, container och CI/CD som inte är registrerade för respektive kapitel bedömdes vara stödjande exempel eller generiska teknikreferenser, inte sådan kompletterande behandling av registerobjektet som motiverar ytterligare registerrelationer.

## Läsbart register

Ingen synlig ändring behövs i `chapters/begreppsregister.md`. Kapitel 32 finns redan som kompletterande behandlingskapitel för **Applikationsexekvering och runtime**, så korrigeringen gäller endast metadata för den faktiska kursiveringsmarkeringen.

## Explicita kapitelhänvisningar

Hänvisningarna inom Del V kontrollerades och är fortfarande giltiga efter kapitelrevisionerna, bland annat:

- kapitel 28 → kapitel 30 och 32,
- kapitel 29 → kapitel 30,
- kapitel 30 → kapitel 28, 29 och 4,
- kapitel 31 → kapitel 9, 30 och 32,
- kapitel 32 → kapitel 37 och 33,
- kapitel 33 → kapitel 4, 20, 28 och 30.

Explicita hänvisningar från andra delar till Del V kontrollerades också. Hänvisningarna från kapitel 22 och 35 till kapitel 30 samt från kapitel 37 till kapitel 31–32 pekar fortfarande på de avsedda resonemangen. Ingen manusändring krävs.

## Resultat

Del V:s register- och korsreferenser är synkade med den reviderade texten. Endast en metadatajustering i det maskinläsbara begreppsregistret behövdes; manus och läsbart register är oförändrade.
