# Lösningsmönster: Backend for Frontend

## Syfte

Skapa ett särskilt backendgränssnitt anpassat till behoven hos en viss kanal eller klienttyp utan att exponera interna domän- och integrationsgränssnitt direkt till klienten.

## Problem

Olika klienter, exempelvis webb, mobil och interna handläggargränssnitt, kan behöva olika dataformat, aggregering, sessionshantering och säkerhetsmekanismer. Ett gemensamt generiskt API riskerar antingen att bli för brett eller att flytta för mycket orkestrering till klienten.

## När mönstret passar

- flera klienttyper har tydligt olika behov
- klienten annars skulle behöva anropa många backendtjänster
- kanalnära logik behöver samlas på serversidan
- autentisering, sessionshantering eller API-sammansättning behöver hanteras nära klienten

## När mönstret inte passar

- en enkel klient kan använda ett stabilt domän-API direkt
- BFF-lagret bara vidarebefordrar anrop utan att tillföra värde
- organisationen skapar ett BFF per frontend utan faktisk behovsskillnad

## Struktur

```text
Klient
  ↓
Backend for Frontend
  ↓
Domän- och plattformstjänster
```

## Konsekvenser

**Fördelar**
- tydligare kanalansvar
- mindre koppling mellan klient och interna tjänster
- enklare optimering per kanal

**Nackdelar**
- ytterligare komponent att utveckla och drifta
- risk för duplicerad logik mellan flera BFF:er

## Berörda förmågor

Primärt:
- Interaktion, presentation och kanaler

Sekundärt:
- Integration och kommunikation
- Identitet och tillit
- Driftbarhet och motståndskraft
