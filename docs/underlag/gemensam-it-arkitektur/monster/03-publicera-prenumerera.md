# Lösningsmönster: Publicera/prenumerera

## Syfte

Låta en producent publicera en händelse utan att känna till vilka konsumenter som reagerar på den.

## Problem

Direkta punkt-till-punkt-integrationer skapar koppling mellan producent och varje konsument och gör det svårt att lägga till nya mottagare.

## När mönstret passar

- flera konsumenter kan behöva reagera på samma händelse
- producenten inte ska styra konsumenternas beteende
- händelsen representerar ett redan inträffat faktum
- lös koppling är viktig

## När mönstret inte passar

- en viss mottagare måste utföra ett kommando
- strikt synkront svar krävs
- händelser används som dold RPC

## Riktlinjer

Händelser bör uttryckas som fakta, exempelvis "ÄrendeRegistrerat", inte som tekniska kommandon som "UppdateraSystemB".

## Berörda förmågor

Primärt:
- Integration och kommunikation

Sekundärt:
- Process, workflow och ärendehantering
- Data- och informationshantering
- Analys, sökning och AI
