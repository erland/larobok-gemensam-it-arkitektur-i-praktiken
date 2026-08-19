# Lösningsmönster: Observability för distribuerade tjänster

## Syfte

Kombinera strukturerade loggar, metrics, tracing och korrelation för att kunna förstå beteendet i en distribuerad lösning.

## Problem

En användartransaktion kan passera flera tjänster, köer och integrationslager. Lokala loggar räcker då inte för att förstå helheten.

## Delar

- strukturerad loggning
- korrelations-ID
- tekniska och verksamhetsnära metrics
- distributed tracing
- central insamling
- dashboards och åtgärdsbara larm

## När mönstret passar

- mikrotjänster
- integrationsintensiva lösningar
- flöden över flera plattformar
- höga krav på felsökning och spårbarhet

## Berörda förmågor

Primärt:
- Driftbarhet och motståndskraft

Sekundärt:
- Integration och kommunikation
- Applikationsexekvering och runtime
- Programvaruutveckling och leverans
