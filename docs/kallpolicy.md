# Källpolicy

## Principer
1. Bokens stabila arkitekturmodell ska i första hand stödjas av etablerade originalkällor, standardorganisationer och välrenommerad facklitteratur.
2. För externa standarder och protokoll används primärkällor: exempelvis IETF/RFC Editor, ISO/IEC/IEEE, W3C, OMG, NIST, OpenID Foundation, CNCF och andra ansvariga standard-/projektorganisationer.
3. Produktversioner, supportstatus, licensvillkor och andra snabbt föränderliga uppgifter verifieras nära publicering och märks som tidskänsliga.
4. Organisationsspecifika val i projektets ursprungliga arkitekturunderlag behandlas som exempel och källa till struktur, inte automatiskt som allmängiltiga rekommendationer.
5. Påståenden om effekter, kostnad, säkerhet eller "best practice" ska kunna spåras till resonemang, empiri eller en tydligt identifierad normativ källa.
6. Sekundärkällor får användas för orientering men viktiga sakpåståenden verifieras mot primärkälla när sådan finns.

## Källapparat i den publicerade boken
Boken använder en lättviktig källapparat för att behålla läsbarheten:

- Externa sakpåståenden som behöver tydlig spårbarhet markeras selektivt i löptext med kapitelvisa markörer `[K1]`, `[K2]` och så vidare. Numreringen börjar om i varje kapitel.
- Markörerna förklaras i en avslutande sektion **Källor och vidare läsning** i samma kapitel. Detta fungerar som kapitelvisa slutnoter och är stabilt i både EPUB och PDF.
- Täta akademiska referenser undviks. En källa återges när den faktiskt bär ett standardpåstående, en definition, en versionsuppgift eller ett centralt externt resonemang.
- Direkta citat används sparsamt. Parafras är huvudregel.
- En samlad bibliografi finns som back matter efter huvudkapitlen. Den samlar de viktigaste källorna utan att ersätta kapitelnoternas spårbarhet.
- Bokens egna syntesmodeller – exempelvis etableringsordningen, ansvar på tre nivåer, flera mognadstrappor och governance-loopen – märks i texten som bokens rekommenderade arbetssätt och ges inte en extern referens som om de vore standarder.
- Versionskänsliga uppgifter anger version och/eller granskningsdatum när det har betydelse.

## Faktakontroll
Varje kapitel ska vid slutgranskning kontrollera:
- externa standarders namn och status,
- versions- och produktpåståenden,
- säkerhets- och regelefterlevnadspåståenden,
- historiska eller kvantitativa påståenden,
- definitioner där flera etablerade betydelser förekommer.

Källregister och granskningsstatus finns i `docs/kallregister.md` och `docs/faktakontroll.md`.
