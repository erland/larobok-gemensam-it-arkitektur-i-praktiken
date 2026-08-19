# Terminologi

| Term | Föredragen svensk term | Användning i boken |
|---|---|---|
| capability | förmåga | Kvalificera som verksamhetsförmåga eller gemensam IT-förmåga när sammanhanget kan vara oklart. |
| quality attribute | kvalitetsattribut | Kan även beskrivas som kvalitetsdimension i källmaterialet; boken använder kvalitetsattribut när egenskapen driver arkitekturval. |
| solution pattern | lösningsmönster | Återanvändbar arkitekturlösning i en viss kontext. |
| platform service | plattformstjänst | Konsumerbart erbjudande; skilj från teknisk produkt. |
| technical building block | tekniskt byggblock | Teknisk komponent eller mekanism som realiserar en tjänst. |
| reference architecture | referensarkitektur | Generell arkitektur för en klass av lösningar. |
| guardrail | guardrail / styrande räcke | Engelska termen kan användas första gången med svensk förklaring. |
| golden path | golden path / rekommenderad väg | Används för en automatiserad, lättillgänglig standardväg för utveckling. |
| system of record | system of record / auktoritativ källa | Välj uttryck efter sammanhang; definiera tydligt. |
| bounded context | bounded context / avgränsad domänkontext | DDD-term; behåll originalterm vid första introduktion. |
| observability | observerbarhet | Ange den engelska termen vid första introduktionen när den behövs för igenkänning. |
| resilience | motståndskraft / resiliens | Föredra motståndskraft när det fungerar språkligt. |

## Ansvarsnivåer
Använd följande tre benämningar konsekvent när ansvar jämförs mellan nivåer:

1. **gemensam arkitektur** – spelplan, tvärgående ramar och sådant som måste hänga ihop,
2. **förmågeområde** – fördjupning, erbjudanden, mönster och standarder inom ett område,
3. **lösning/produkt** – konkret tillämpning för ett verksamhetsbehov.

I löptext kan "gemensam nivå", "förmågenivå" och "lösnings-/produktnivå" användas när sammanhanget redan är etablerat, men rubriker om den tredelade modellen ska använda formen **Ansvar på tre nivåer**.

## Engelska facktermer
Behåll etablerade engelska termer när en svensk översättning riskerar att bli mindre precis, men introducera dem med svensk förklaring första gången. Undvik att växla mellan flera svenska översättningar för samma begrepp i samma kapitel.

## Språk- och stilval efter manusrevision
Följande val gäller i löptext efter språk- och stilrevision pass 1:

- **avvägning** föredras framför *trade-off*; den engelska termen används bara när den i sig diskuteras.
- **observerbarhet** föredras framför *observability*; den engelska termen anges vid första introduktionen.
- **begränsning** föredras framför *constraint*; den engelska termen kan anges vid första introduktionen när den arkitekturella fackbetydelsen behöver markeras.
- **driftsättning** föredras framför *deployment*.
- **telemetri** föredras framför *telemetry*.
- **återförsök** föredras framför *retry*.
- **mätvärden**, **spår** och **instrumentpaneler** föredras framför *metrics*, *traces* och *dashboards* när betydelsen är densamma.
- **utvecklarupplevelse** används i svensk löptext; *Developer Experience (DevEx)* anges vid första introduktionen.

Etablerade termer som *runtime*, *workflow*, *bounded context*, *golden path*, *paved road*, *stateless/stateful*, *showback/chargeback* och protokollspecifika begrepp får behållas när en svensk översättning skulle bli mindre precis eller mindre etablerad. Introducera då termen med en kort svensk förklaring första gången den är central.
