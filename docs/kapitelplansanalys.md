# Analys av kapitelplanen

## Syfte
Denna analys gjordes före skrivstart för kapitel 1 för att kontrollera överlapp, progression och avgränsningar i den ursprungliga 38-kapitelsplanen.

## Huvudfynd

### 1. Kvalitetskrav förekom i två metodkapitel
Ursprungliga kapitel 4, *Kvalitetsattribut som arkitekturens drivkrafter*, och kapitel 10, *Från kvalitetsbehov till förmågekrav*, låg mycket nära varandra. Båda behandlade kedjan från verksamhetskonsekvens till arkitekturkrav. Det senare kapitlet har därför tagits bort som självständigt kapitel. Kravkedjan fördjupas i kapitel 4 och tillämpas praktiskt i kapitel 35.

### 2. Governance introducerades för tidigt och återkom sedan i flera former
Ursprungliga kapitel 6 om styrning överlappade standarder, avsteg, plattformsstyrning samt de avslutande kapitlen om förvaltning. Det har ersatts av ett renodlat kapitel om arkitekturprinciper. Governance, mandat, avsteg och förvaltning samlas i det avslutande governance-kapitlet, när läsaren redan känner de artefakter som ska styras.

### 3. Informationsperspektivet och dataförmågan behövde tydligare gräns
Ursprungliga kapitel 9 och förmågekapitlet om data- och informationshantering riskerade att repetera system of record, kopior och datamodeller. Det nya kapitel 11 fokuserar därför på semantik, informationsägarskap, informationsmodell och data som arkitekturellt ingångsvärde. Förmågekapitel 15 fokuserar på tekniska datahanteringsmekanismer.

### 4. Förmågekapitlen och mönsterkapitlen behöver olika frågor
Det är legitimt att samma teknikområde återkommer i del III och IV, men endast om perspektivet ändras. Del III svarar på *vad organisationen behöver kunna erbjuda och varför*. Del IV svarar på *hur återkommande lösningsproblem kan struktureras*. Den principen är nu explicit i kapitelplanen.

### 5. Plattformskapitlen var relevanta men behövde tydliga ansvarssnitt
Byggblock → plattformstjänst, Platform as a Product och golden paths/självservice är tre närliggande men skilda perspektiv. De behålls som separata kapitel, med explicita avgränsningar: tjänstekontrakt, produktmodell respektive konsumtionsupplevelse/guardrails.

### 6. Förvaltning och evolution var onödigt uppdelade
Ursprungliga kapitel 37 och 38 hade båda ownership, feedback, mätning, livscykel och förändring som kärna. De har slagits samman till *Governance, förvaltning och evolution*. Teknikspecifik livscykel för produkter och versioner ligger däremot kvar separat i kapitel 32.

### 7. Tillämpningsdelen blev mer pedagogisk när metoden kommer före casen
Den nya ordningen är: definiera referensarkitektur → visa arbetsflödet från behov till lösningsarkitektur → tillämpa det på sju återkommande scenarier. Det gör scenarierna till syntes i stället för att de introducerar metoden implicit.

## Resultat
- Ursprunglig plan: 38 kapitel + inledning.
- Första reviderade plan: 36 kapitel + inledning.
- Två självständiga kapitel har absorberats i närliggande kapitel.
- Ett tidigt governance-kapitel har omformats till arkitekturprinciper.
- Tre centrala riskpar har fått explicita avgränsningar: kvalitet/driftbarhet, information/datahantering och plattformstjänst/platform-as-product.

## Bedömning
Den reviderade planen har en tydligare progression och mindre risk för upprepning utan att minska ämnestäckningen. Den lämpar sig bättre för linjär läsning samtidigt som del III–V fortfarande kan användas som referensdelar.

## Kompletterande analys före skrivstart: etableringsordning och ansvar
En efterföljande granskning visade att del I förklarade varför modellen behövs men inte tillräckligt tydligt *i vilken ordning* den bör etableras eller *vem* som bör äga vilka beslut. Det riskerade att få läsaren att tolka modellen som antingen central detaljstyrning eller som en katalog utan etableringsmetod.

Därför har ett nytt kapitel 7, *Att etablera modellen – ordning, ansvar och iteration*, lagts sist i del I. Det introducerar tre ansvarsnivåer: gemensam arkitektur, förmågeområde och lösning/produkt. Kapitlet gör också tydligt att arbetssättet är iterativt: top-down används för sammanhang, gemensamma ramar och prioritering, medan bottom-up-lärande från prioriterade förmågor och konkreta lösningar får justera den övergripande modellen.

Den nya slutliga planeringsstrukturen är 37 kapitel + inledning. Det extra kapitlet tillför inte ett nytt teknikområde utan gör bokens arbetsmetod och ansvarsfördelning explicit, vilket minskar risken för överlapp och otydligt mandat i senare kapitel.
