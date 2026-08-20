# Register- och korsreferenssynk efter revision av Del III

Datum: 2026-08-20
Utgångspunkt: revision 92
Omfattning: kapitel 12–22, `docs/begreppsregister.yaml`, `chapters/begreppsregister.md` samt explicita kapitelhänvisningar till Del III från övriga kapitel.

## Syfte

Efter komprimeringen och omstruktureringen av Del III kontrollerades att begreppsregistrets markeringar och kompletterande kapitelhänvisningar fortfarande motsvarar den faktiska texten, och att andra kapitel inte hänvisar till resonemang som har försvunnit eller flyttats.

## Korrigeringar

Tre markeringskopplingar behövde läggas till eftersom begreppen fortfarande är kursiverade i den reviderade texten:

- **Service Identity** som plattform/tjänst: kapitel 18.
- **Service Identity** som teknisk standard: kapitel 18.
- **Java Application Runtime** som teknisk standard: kapitel 19.

Sex kompletterande relationer togs bort eftersom de efter revisionen inte längre ger en tydlig behandling av registerbegreppet:

- **Retrieval-Augmented Generation (RAG):** kapitel 12, 13, 17 och 18 togs bort. Kapitel 16 behålls eftersom RAG behandlas utförligt där, trots att registertermens fullständiga formulering inte används ordagrant.
- **Container:** kapitel 18 togs bort.
- **CI/CD:** kapitel 15 togs bort.

Relationerna **Backup och återställning → kapitel 15** och **Driftbarhet och motståndskraft → kapitel 17** behölls eftersom kapitlen fortfarande ger tydlig kompletterande behandling även om exakt registerterm inte används ordagrant.

## Läsbart register

`chapters/begreppsregister.md` har synkats med det korrigerade YAML-underlaget för de poster vars synliga kapitelurval förändrades. Principen är oförändrad: huvudsakligt kapitel visas först och i fetstil, följt av högst fem kompletterande kapitel.

## Explicita kapitelhänvisningar

Explicita hänvisningar från andra delar av boken till kapitel 12–22 kontrollerades. Hänvisningarna till kapitel 13–15 i mönsterdelen, kapitel 17 i integrationsmönstren, kapitel 20–21 i drift- och leveransmönstren samt kapitel 20 i ekonomidelen pekar fortfarande på resonemang som finns kvar efter revisionerna. Ingen manusändring krävdes.

## Resultat

Del III:s register- och korsreferenser är synkade med den reviderade texten. Inga kapitelnummer eller läsarorienterande hänvisningar behöver ändras.
