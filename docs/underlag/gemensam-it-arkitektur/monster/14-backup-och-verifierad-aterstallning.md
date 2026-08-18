# Lösningsmönster: Backup och verifierad återställning

## Syfte

Säkerställa att data och nödvändig konfiguration inte bara säkerhetskopieras utan faktiskt kan återställas inom den kvalitetsnivå som behovet kräver.

## Problem

Att backupjobbet lyckas betyder inte att återställning fungerar eller att rätt data finns med.

## Mönster

1. definiera skyddsvärda data och konfiguration
2. härled RPO/RTO eller motsvarande
3. skapa backup enligt profil
4. separera backup från primär fel-/hotdomän där behovet kräver det
5. testa restore återkommande
6. dokumentera resultat och avvikelser

## Berörda förmågor

Primärt:
- Driftbarhet och motståndskraft

Sekundärt:
- Data- och informationshantering
- Applikationsexekvering och runtime
