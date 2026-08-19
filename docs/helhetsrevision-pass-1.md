# Helhetsrevision – pass 1

## Omfattning
Helhetsrevisionen omfattar inledningen och kapitel 1–37 samt kapitelplan, innehålls-canon, terminologi, faktakontroll och projektstatus. Manusets omfattning vid revisionen är cirka 121 000 ord.

## Samlad bedömning
Kapitelstrukturen är stabil och den övergripande progressionen fungerar: modell och beslutslogik → förmågor → lösningsmönster → plattformar och standarder → referens-/lösningsarkitektur → governance. Inget kapitel behöver slås ihop, delas eller flyttas.

## Överlapp
Särskilt granskade gränser:

- **Kapitel 4 / 20:** kapitel 4 äger härledning av kvalitetskrav; kapitel 20 äger teknisk och operativ realisering av driftbarhet, observability och återställning.
- **Kapitel 11 / 15:** kapitel 11 äger mening, semantik och informationsansvar; kapitel 15 äger tekniska datahanteringsmekanismer.
- **Kapitel 17 / 24:** kapitel 17 äger kommunikationsformer och förmågeval; kapitel 24 äger mönsterstruktur, forces och kombinationer.
- **Kapitel 21 / 27:** kapitel 21 äger leveransförmågan; kapitel 27 äger de återanvändbara drift-/leveransmönstren.
- **Kapitel 28 / 29 / 30:** kapitel 28 definierar plattformstjänsten, kapitel 29 produktorienteringen och kapitel 30 konsumtionsvägar/självservice/guardrails.
- **Kapitel 31 / 32 / 37:** kapitel 31 äger standardnivåer, kapitel 32 tekniklivscykeln och kapitel 37 governance för hela arkitektursystemet.

Överlappet mellan dessa kapitel bedöms huvudsakligen vara funktionell repetition som hjälper referensläsning. Några övergångar har skärpts för att undvika att senare kapitel uppfattas som omtag.

## Terminologi
Den tredelade ansvarmodellen är fortsatt konsekvent: **gemensam arkitektur → förmågeområde → lösning/produkt**. Rubriker som jämför nivåerna har normaliserats till **Ansvar på tre nivåer**. Terminologidokumentet har kompletterats med explicita regler för ansvarsnivåer och engelska facktermer.

Distinktionen mellan verksamhetsförmåga och gemensam IT-förmåga är verifierad över helmanuset. Även gränserna mellan förmåga, plattformstjänst, tekniskt byggblock och produkt är konsekventa.

## Balans och omfattning
Huvudkapitlen ligger i huvudsak mellan cirka 2 500 och 4 100 ord. Variationen följer ämnets komplexitet och motiverar inte strukturella ingrepp. De längre kapitlen 13, 16 och 20 är innehållsmässigt motiverade; de kortare kapitlen 29, 31, 33 och 36 har tydliga, avgränsade funktioner och behöver inte fyllas ut artificiellt.

## Faktakontroll
Manusets interna faktakonsistens och markeringen av bokens egna arbetsmodeller har granskats. F-001, F-027 och F-028 kan därför stängas. Externa och tidskänsliga kontrollpunkter som fortfarande är markerade **Öppen** ska däremot inte stängas utan en separat publiceringsnära kontroll mot aktuella primärkällor och, där relevant, organisationens rättsliga/informationsstyrande kontext.

## Redaktionell sammanhållning
Bokens återkommande struktur – problem, gränsdragning, kvaliteter, ansvar, anti-patterns och praktisk analys – fungerar väl för en faktabok som också ska kunna användas som referens. Den återkommande formen ska därför behållas även där den innebär viss avsiktlig repetition.

## Genomförda ändringar
- normaliserade ansvarsrubriker i berörda kapitel,
- skärpte explicita kapitelgränser i kapitel 15, 24, 27 och 37,
- kompletterade terminologicanon för ansvarsnivåer och engelska facktermer,
- rättade projektstatus för kapitel 37,
- stängde helmanusbaserade faktakontrollpunkter F-001, F-027 och F-028,
- lade till F-029 som dokumentation av helhetskontrollen,
- uppdaterade kapitelplanens status till helhetsreviderad – pass 1.

## Rekommenderat nästa steg
1. Publiceringsnära faktagranskning av kvarvarande öppna kontrollpunkter.
2. Språk- och stilputs över hela manuset med fokus på meningsrytm, onödiga anglicismer och repetitiva formuleringar inom – inte mellan – kapitel.
3. Beslut om synlig källapparat och illustrationer.
4. Första komplett byggd EPUB/PDF för typografisk och visuell granskning.
