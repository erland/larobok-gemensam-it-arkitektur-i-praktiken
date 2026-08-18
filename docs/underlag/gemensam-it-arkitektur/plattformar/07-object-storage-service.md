# Plattform/tjänsteerbjudande: Object Storage Service

## Syfte
Tillhandahålla skalbar objektlagring för filer, dokument, bilder och andra större binära objekt.

## Primär förmåga
- Data- och informationshantering

## Typiska behov
- stora binära objekt
- dokument och bilagor
- immutable eller relativt sällan ändrad data
- kostnadseffektiv lagring

## Konsumentansvar
- metadata
- relation till verksamhetsobjekt
- retention
- accesskontroll

## Plattformsansvar
- lagringskapacitet
- redundans
- teknisk åtkomst
- livscykelfunktioner där tjänsten stödjer det

## Möjlig realisering
- Ceph som tekniskt byggblock/realisering

## Begränsningar
Objektlagring ersätter inte relationsdatabas eller dokumenthanteringssystem.
