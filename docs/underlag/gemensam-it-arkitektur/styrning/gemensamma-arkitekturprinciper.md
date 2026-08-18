# Gemensamma arkitekturprinciper

## Syfte

Principerna beskriver hur arkitekturval ska göras inom den gemensamma IT-arkitekturen. De ska vara relativt stabila och så långt som möjligt teknikoberoende.

## P1. Behov före teknik

Tekniska lösningar och tekniska krav ska härledas från identifierade behov hos verksamhet och IT-stöd samt från gemensamma organisatoriska eller regulatoriska krav.

En produkts eller plattforms nuvarande begränsning får inte utan uttryckligt beslut omvandlas till ett generellt krav på alla IT-stöd.

## P2. Standardiserade erbjudanden när de möter behovet

Gemensamma plattformstjänster, mönster och standarder ska användas när de på ett ändamålsenligt sätt uppfyller IT-stödets behov och kvalitetskrav.

Standardisering är ett medel för effektivitet och kvalitet, inte ett självändamål.

## P3. Problem löses på lämplig arkitekturnivå

Ett problem ska så långt som möjligt lösas på den nivå där det naturligt hör hemma.

Ett applikationsproblem ska inte automatiskt lösas i nätverket, och ett gemensamt plattformsproblem ska inte behöva lösas separat i varje applikation.

## P4. Ansvar och gränssnitt ska vara tydliga

Varje plattformstjänst ska ha ett tydligt tjänstekontrakt och en tydlig ansvarsfördelning mellan konsument och levererande IT-område.

Underliggande teknisk komplexitet bör abstraheras där det är ändamålsenligt.

## P5. Säkerhet och andra kvaliteter byggs in

Säkerhet, tillgänglighet, kontinuitet, spårbarhet, användbarhet och andra relevanta kvaliteter ska hanteras som egenskaper hos lösningen från början.

De ska inte enbart hanteras som efterkontroller eller som ansvar för ett separat teknikområde.

## P6. Separation mellan stabil arkitektur och föränderlig teknik

Förmågor, principer och behov ska hållas separerade från produkter, versioner och konfigurationsdetaljer.

Det ska vara möjligt att byta teknisk realisering utan att den övergripande arkitekturmodellen behöver göras om.

## P7. Återanvändning före lokal speciallösning

Gemensamma komponenter, tjänster och mönster ska återanvändas när de uppfyller behovet.

Lokala speciallösningar ska motiveras av verkliga skillnader i behov eller kvalitetskrav.

## P8. Automatisering och reproducerbarhet eftersträvas

Bygg, test, konfiguration, deployment och infrastruktur bör automatiseras där det är praktiskt och proportionerligt.

Reproducerbara arbetssätt minskar beroende av manuell hantering och enskilda personer.

## P9. Livscykel och förvaltning beaktas vid beslut

Arkitekturval ska bedömas utifrån hela livscykeln: införande, drift, förändring, uppgradering, support, kostnad och avveckling.

Kortsiktig utvecklingshastighet får inte ensam styra teknikval.

## P10. Avsteg ska kunna motiveras

Standarder och riktlinjer ska inte hindra välmotiverade lösningar när standarderbjudandet inte möter behovet.

Avsteg ska vara spårbara och återkommande avsteg ska kunna leda till förändring av standard, guideline eller plattformserbjudande.
