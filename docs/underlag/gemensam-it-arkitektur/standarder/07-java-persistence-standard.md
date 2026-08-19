# Teknisk standard: Java persistence

## Syfte
Ge gemensam vägledning för Java-baserad åtkomst till relationell data.

## Typ
Teknikstandard

## Relaterade förmågor
- Data- och informationshantering
- Programvaruutveckling och leverans

## Standard
JPA är rekommenderad standard när ORM-abstraktionen passar domänen och åtkomstmönstret.

Direkt SQL eller annan accessmodell kan användas när:
- komplexa queries kräver det
- prestanda motiverar det
- batch-/bulkbehov passar bättre
- JPA skapar onödig abstraktionskostnad

## Avgränsning
JPA är inte en databastjänst och styr inte val mellan Oracle, SQL Server eller annan relationell databas.
