# Register- och korsreferenssynk efter revision av Del I

Datum: 2026-08-19
Utgångspunkt: revision 72
Omfattning: kapitel 1–7, `docs/begreppsregister.yaml`, `chapters/begreppsregister.md` samt explicita kapitelhänvisningar från kapitel 8–37 tillbaka till Del I.

## Syfte

Efter komprimeringen av Del I kontrollerades att begreppsregistrets markeringar och kompletterande kapitelhänvisningar fortfarande motsvarar den faktiska texten, och att senare kapitel inte hänvisar till resonemang som har försvunnit eller flyttats.

## Markerade kapitel

Fem poster hade Del I-markeringar som inte längre motsvarade faktisk kursivering efter revisionerna:

- Integration och kommunikation: markering i kapitel 6 och 7 borttagen ur metadata; kapitel 5 kvarstår.
- API Management: markering i kapitel 5 borttagen ur metadata.
- Containerplattform: markering i kapitel 6 borttagen ur metadata; kapitel 3–5 kvarstår.
- Internt handläggningsstöd: markering i kapitel 7 borttagen ur metadata; kapitel 1 kvarstår.
- Publik e-tjänst: markering i kapitel 7 borttagen ur metadata; kapitel 4 kvarstår.

## Kompletterande kapitelhänvisningar

Elva relationer till kapitel 1–7 bedömdes efter helhetsläsning vara för svaga eller ha blivit inaktuella och togs bort:

- Programvaruutveckling och leverans → kapitel 6
- Retrieval-Augmented Generation (RAG) → kapitel 2
- Tjänsteidentitet → kapitel 7
- Build once, promote many → kapitel 2
- Backup och verifierad återställning → kapitel 2
- API Management → kapitel 1
- Enterprise Messaging → kapitel 2
- Secrets → kapitel 2
- Container → kapitel 7
- Containerplattform → kapitel 7
- CI/CD → kapitel 4

Relationer behölls när kapitlet fortfarande ger en verklig kompletterande behandling, även om termen förekommer i böjd form. Exempelvis behålls referensarkitekturerna Publik e-tjänst och Internt handläggningsstöd mot kapitel 7, där de används i plural som exempel på återkommande lösningsklasser.

## Läsbart register

`chapters/begreppsregister.md` har synkats mot det korrigerade YAML-underlaget. Registrets princip är oförändrad: huvudsakligt kapitel visas först och i fetstil, följt av högst fem kompletterande kapitel.

## Explicita hänvisningar i senare kapitel

Samtliga explicita hänvisningar från kapitel 8–37 tillbaka till kapitel 1–7 kontrollerades mot den reviderade texten. Hänvisningarna till bland annat behov före teknik, kvalitetsmodellen, avvägningar/reversibilitet, arkitekturprinciper samt ansvar- och iterationsmodellen är fortfarande sakligt korrekta. Ingen manusändring krävdes.

## Resultat

Del I:s korsreferenser är synkade med den komprimerade texten. Inga kapitelnummer eller läsarorienterande hänvisningar behöver ändras.
