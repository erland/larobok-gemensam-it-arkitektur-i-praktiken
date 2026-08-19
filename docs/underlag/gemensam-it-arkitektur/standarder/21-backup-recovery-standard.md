# Teknisk standard: Backup och återställning

## Syfte
Standardisera kopplingen mellan informationsbehov och teknisk backup/restore.

## Typ
Arkitektur- och teknikstandard

## Relaterade förmågor
- Driftbarhet och motståndskraft
- Data- och informationshantering

## Standard
- Backupnivå ska härledas från dokumenterade återställningsbehov.
- RPO/RTO eller motsvarande ska definieras när det är relevant.
- Restore ska testas återkommande för kritiska data.
- Replikering får inte betraktas som full ersättning för backup utan analys.
- Backup ska separeras från primär fel-/hotdomän när behovet kräver det.

## Livscykel
Retentionprofiler och teknik hålls separat.
