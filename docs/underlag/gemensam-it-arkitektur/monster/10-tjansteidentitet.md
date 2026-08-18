# Lösningsmönster: Tjänsteidentitet

## Syfte

Ge varje system, workload eller tjänst en egen teknisk identitet för system-till-system-kommunikation och åtkomstkontroll.

## Problem

Delade servicekonton eller personliga användarkonton ger svag spårbarhet och komplicerad livscykel.

## När mönstret passar

- backendtjänster anropar varandra
- pipelines behöver teknisk åtkomst
- workloads behöver autentiseras mot databas, messaging eller API

## Riktlinjer

Tjänsteidentiteten bör:

- vara unik för relevant tjänst eller workload
- ges minsta privilegium
- använda kortlivade credentials där det är möjligt
- ha automatiserad rotation/livscykel
- vara spårbar i loggar

## Berörda förmågor

Primärt:
- Identitet och tillit

Sekundärt:
- Integration och kommunikation
- Applikationsexekvering och runtime
- Programvaruutveckling och leverans
