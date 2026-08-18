# Teknisk standard: Secrets

## Syfte
Standardisera hantering av lösenord, nycklar, tokens och andra tekniska secrets.

## Typ
Teknikstandard

## Standard
Secrets:
- får inte lagras i klartext i källkod
- får inte byggas in i images eller releaseartefakter
- ska lagras i godkänd secretslösning
- ska kunna roteras
- ska ha definierat ägarskap
- ska endast exponeras till workloads som behöver dem

## Relaterade förmågor
- Identitet och tillit
- Programvaruutveckling och leverans
- Applikationsexekvering och runtime
