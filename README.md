# Gemensam IT-arkitektur i praktiken

Detta är bokprojektet för faktaboken **Gemensam IT-arkitektur i praktiken**. Projektet är skapat från Lärobokskaparens kanoniska projektmall.

## Nuvarande läge
Projektet befinner sig i skrivfas. Bokspecifikation, kapitelplan, källpolicy, terminologi och innehålls-canon är etablerade, och kapitel 1–25 är skapade som första utkast. Det ursprungliga arkitekturmaterialet ligger som arbetsunderlag under `docs/underlag/gemensam-it-arkitektur/` och exporteras inte som boktext.

## Arbetsflöde
1. Förfina planen vid behov.
2. Skriv kapitel ett i taget och lägg in dem i `book.yaml` först när de är faktiska bokkapitel.
3. Håll `docs/faktakontroll.md`, `docs/terminologi.md` och `docs/innehalls-canon.md` synkroniserade.
4. Validera projektet före och efter varje revision.
5. Bygg EPUB/PDF reproducerbart med projektets scripts och GitHub Actions.
