# Lösningsmönster: System of record och härledda kopior

## Syfte

Tydliggöra vilken källa som är auktoritativ för en informationsmängd och hur cache, index, analyslager och andra kopior förhåller sig till den.

## Problem

När samma information finns i flera tekniska representationer kan det bli oklart vilken kopia som är den riktiga och hur avvikelser ska hanteras.

## När mönstret passar

- sökindex byggs från primärdata
- cache används
- analyslager eller read models skapas
- data replikeras för läsning
- flera system behöver lokala kopior

## Regler

Varje härledd kopia bör ha:

- identifierad källa
- synkroniseringsmodell
- tolererad aktualitet
- återuppbyggnadsstrategi
- tydligt ansvar

## Berörda förmågor

Primärt:
- Data- och informationshantering

Sekundärt:
- Analys, sökning och AI
- Integration och kommunikation
- Driftbarhet och motståndskraft
