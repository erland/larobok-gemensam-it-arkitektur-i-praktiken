# Typografi- och korsreferensrevision – pass 2

Datum: 2026-08-19

## Syfte

Införa en diskret begreppsmarkering och ett samlat begreppsregister utan att lägga kapitelhänvisningar i den löpande texten.

## Genomförande

- Ett maskinläsbart register har skapats i `docs/begreppsregister.yaml`.
- Registret omfattar 93 definierade arkitekturobjekt: 11 förmåga, 15 lösningsmönster, 35 plattform/tjänst, 25 teknisk standard, 7 referensarkitektur.
- Kursivering används sparsamt i huvudkapitlen. Högst tre definierade objekt markeras per kapitel och bara vid första betydelsefulla förekomsten.
- Totalt infördes 90 diskreta begreppsmarkeringar i de 37 huvudkapitlen.
- Inga formuleringar av typen ”se kapitel …” har införts i löptexten.
- `chapters/begreppsregister.md` har lagts sist i boken efter bibliografin.
- Registerhänvisningar använder kapitelnummer, inte sidnummer, så att samma modell fungerar i både EPUB och PDF.

## Princip

Markeringen ska hjälpa läsaren att känna igen objekt i bokens modell, inte styra bort läsaren från det aktuella resonemanget. Registret bär navigeringen.
