# Register- och korsreferenssynk efter revision av Del II

Datum: 2026-08-19
Utgångspunkt: revision 78
Omfattning: kapitel 8–11, `docs/begreppsregister.yaml`, `chapters/begreppsregister.md` samt explicita kapitelhänvisningar från senare kapitel tillbaka till Del II.

## Syfte

Efter komprimeringen och omstruktureringen av Del II kontrollerades att begreppsregistrets markeringar och kompletterande kapitelhänvisningar fortfarande motsvarar den faktiska texten, och att senare kapitel inte hänvisar till resonemang som har försvunnit eller flyttats.

## Korrigeringar

Fyra registerposter behövde synkas:

- **Data- och informationshantering:** kompletterande relation till kapitel 9 togs bort eftersom den explicita behandlingen försvann i revisionen av kapitlet. Den tidigare markeringskopplingen till kapitel 11 togs också bort eftersom begreppet inte längre är kursiverat där. Kapitel 11 ligger kvar som kompletterande behandling eftersom informations- och datafrågorna fortfarande behandlas utförligt där.
- **System of record och härledda kopior:** markeringskopplingen till kapitel 11 togs bort eftersom den fullständiga registertermen inte längre är kursiverad. Kapitel 11 behålls som kompletterande behandling; `system of record` och auktoritativ källa behandlas fortfarande explicit.
- **Retrieval-Augmented Generation (RAG):** en gammal markeringskoppling till kapitel 10 togs bort. Kapitel 10 innehåller ingen sådan begreppsmarkering efter domänrevisionen.
- **Backup och återställning:** markerings- och kompletterande kapitelkoppling till kapitel 11 togs bort eftersom den tidigare explicita behandlingen har komprimerats till generella återställningskrav. Kapitel 9 behålls som kompletterande behandling.

## Läsbart register

`chapters/begreppsregister.md` har regenererats från det korrigerade YAML-underlaget. Principen är oförändrad: huvudsakligt kapitel visas först och i fetstil, följt av högst fem kompletterande kapitel.

## Explicita kapitelhänvisningar

Explicita hänvisningar från kapitel 12–37 tillbaka till kapitel 8–11 kontrollerades. Hänvisningarna till gemensamhetsbedömning i kapitel 9, domängränser och coupling i kapitel 10 samt informationsägarskap, semantik och auktoritativa källor i kapitel 11 är fortfarande sakligt korrekta. Ingen manusändring krävdes.

## Resultat

Del II:s register- och korsreferenser är synkade med den reviderade texten. Inga kapitelnummer eller läsarorienterande hänvisningar behöver ändras.
