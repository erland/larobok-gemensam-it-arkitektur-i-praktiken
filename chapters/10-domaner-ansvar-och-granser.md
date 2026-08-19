# 10. Domäner, ansvar och gränser

En gemensam förmågekarta hjälper en organisation att beskriva vilket återkommande IT-stöd som behöver finnas. Den kan visa att organisationen behöver förmågor för exempelvis integration, identitet, datahantering, programvaruleverans och driftbarhet. Den kan också hjälpa till att tydliggöra vad som bör hanteras gemensamt och vad som bör ligga närmare en lösning eller verksamhetsdomän.

Men en förmågekarta svarar inte på alla arkitekturfrågor. Den berättar inte automatiskt var gränsen mellan två verksamhetsområden bör gå, vem som äger ett visst begrepp eller en affärsregel, vilken del av en lösning som får ändra ett visst dataobjekt eller vilka delar som bör kunna förändras oberoende av varandra.

Detta är frågor om domäner, ansvar och gränser. De är centrala eftersom en arkitektur inte bara består av återanvändbara tekniska byggstenar. Den består också av självständiga delar som behöver tydligt ansvar för sin logik, information och förändring. Om gränserna är otydliga sprids verksamhetslogik mellan system, data får konkurrerande ägare och förändringar kräver samordning mellan allt fler team.

Detta kapitel behandlar därför de arkitekturproblem som inte bör lösas genom att göra ännu mer gemensamt.

## Två kartor som svarar på olika frågor

Det är lätt att blanda ihop en gemensam IT-förmågekarta med en domänmodell eller verksamhetsarkitektur. De kan båda beskriva organisationen på en relativt stabil nivå, men de svarar på olika frågor.

En gemensam IT-förmågekarta frågar exempelvis:

> Vilket återkommande IT-stöd behöver organisationen kunna erbjuda flera verksamhetsområden?

En domänorienterad analys frågar i stället:

> Vilka verksamhetsmässiga problem, begrepp, regler och ansvar hör naturligt ihop och bör kunna utvecklas med så lite beroende som möjligt till andra delar?

Skillnaden kan illustreras så här:

```text
Gemensam IT-förmåga             Verksamhetsdomän
-------------------             -----------------
Integration                     Tillståndshantering
Identitet                       Uppbörd
Datahantering                   Kontrollverksamhet
Workflow                        Personaladministration
Observerbarhet                  Inköp
```

Förmågorna till vänster kan återanvändas av många domäner. Domänerna till höger bär verksamhetens eget ansvar och innehåll. Samma verksamhetsdomän använder därför ofta flera gemensamma IT-förmågor, samtidigt som en gemensam IT-förmåga stödjer flera verksamhetsdomäner.

```text
                Gemensamma IT-förmågor
        ┌──────────┬──────────┬──────────┐
        │ Identitet│Integration│ Data     │
        └─────┬────┴─────┬────┴────┬─────┘
              │          │         │
      ┌───────▼──────────▼─────────▼──────┐
      │          Domän A                  │
      └───────────────────────────────────┘
              │          │         │
      ┌───────▼──────────▼─────────▼──────┐
      │          Domän B                  │
      └───────────────────────────────────┘
```

Detta är en viktig distinktion genom resten av boken: gemensamma förmågor beskriver återanvändbart stöd; domäner beskriver verksamhetsnära ansvar.

## Domänen som ansvarsyta

Ordet *domän* används på många sätt. I detta sammanhang är det mest användbart att se en domän som en sammanhängande ansvarsyta kring ett visst problemområde.

En domän kännetecknas ofta av att den har egna centrala begrepp, regler som hör ihop, information vars mening bestäms inom området, beslut som bör kunna fattas nära området och en förändringstakt som inte nödvändigtvis följer andra domäner.

Det betyder inte att en domän måste motsvara en organisatorisk enhet. En avdelning kan innehålla flera domäner och en domän kan sträcka sig över flera organisatoriska enheter. Det betyder inte heller att en domän automatiskt ska bli en applikation eller mikrotjänst. Domänen beskriver först och främst ansvaret och problemet. Den tekniska realiseringen är ett senare beslut.

En domän kan därför vara stabil även när implementationen byts ut. Ett ärendeområde kan exempelvis gå från en monolitisk applikation till flera tjänster utan att själva ansvarsytan förändras. Omvänt kan en teknisk komponent behöva delas upp mellan flera domäner därför att den råkat samla regler och information som förändras av helt olika verksamhetsskäl. Det är därför mer robust att utgå från ansvar och förändring än från dagens systemkarta.

## Bounded context – när ett begrepp behöver en tydlig betydelse

Ett användbart begrepp från Domain-Driven Design är *bounded context*.[K1] Det kan på svenska beskrivas som ett avgränsat sammanhang där en viss modell och terminologi har en bestämd betydelse.

Det är särskilt värdefullt i större organisationer eftersom samma ord ofta betyder olika saker i olika verksamhetsområden.

Ta begreppet *kund*. I ett faktureringssammanhang kan kund vara den juridiska eller fysiska person som är betalningsansvarig. I ett supportärende kan kund vara den person som kontaktar organisationen. I en behörighetsmodell kan samma individ i stället beskrivas som användare, ombud eller representant.

Det är frestande att skapa en enda global datamodell där ordet *kund* får exakt samma definition överallt. Ibland är det möjligt och önskvärt, men ofta leder det till en modell där olika verksamhetsbehov pressas in i samma begrepp.

Ett bounded context accepterar i stället att betydelsen kan vara lokal – så länge gränsen är tydlig och integrationen mellan sammanhangen är explicit.

> Gemensam semantik ska skapas där gemensam semantik faktiskt behövs. Där olika verksamhetskontexter har legitima skillnader ska dessa skillnader göras explicita i stället för att döljas i en överlastad gemensam modell.

Detta blir särskilt viktigt i nästa kapitel, där information och data behandlas som arkitekturella ingångsvärden.

## Cohesion, coupling och förändringsberoenden

Bra gränser samlar sådant som har stark cohesion, alltså inre sammanhållning, och begränsar coupling till omgivningen. Det kan vara funktioner, regler och data som används för samma verksamhetsmål, behöver förstå samma begrepp eller ofta förändras av samma anledning.

En praktisk fråga är:

> Om denna verksamhetsregel ändras, vilka andra delar måste vi nästan alltid förstå och ändra samtidigt?

Om två komponenter ständigt behöver förändras tillsammans kan det vara ett tecken på att de hör till samma ansvarsyta. Omvänt kan en stor lösning innehålla delar som nästan aldrig behöver förändras tillsammans. Då kan tydligare domän- eller modulgränser minska samordningen.

Coupling blir tydlig när en förändring kräver att andra system, databaser eller team måste ändras samtidigt. Problemet är inte att beroenden finns, utan att de är otydliga, instabila eller oproportionerligt dyra att förändra.

Detta är en viktig motvikt till återanvändning. En gemensam komponent kan minska duplicering men samtidigt öka coupling. Om hundra lösningar blir beroende av samma verksamhetsnära bibliotek kan en liten ändring kräva samordning med hundra konsumenter.

En bra gemensam arkitektur försöker därför återanvända sådant som är stabilt och generellt, medan verksamhetsnära variation får stanna nära sin domän.

Det betyder också att graden av coupling behöver bedömas i fler dimensioner än tekniska anrop. Två komponenter kan vara löst kopplade i runtime men starkt kopplade genom gemensam releaseplanering, delade datamodeller eller ett gemensamt beslutsforum. Om varje förändring kräver samordning med samma parter är beroendet arkitekturellt relevant även när inga synkrona API-anrop finns.

På motsvarande sätt kan en synkron integration vara acceptabel om kontraktet är stabilt, ägarskapet tydligt och konsumenten kan hantera tillfällig otillgänglighet. Målet är alltså inte en viss integrationsstil utan beroenden vars konsekvenser är förstådda och rimliga.

Arkitekturgränser bör av samma skäl i första hand följa stabilt ansvar och sammanhängande förändringsytor, inte dagens organisationsschema. Team och avdelningar förändras; domänansvar och centrala begrepp kan vara betydligt mer långlivade. Organisationen måste ändå göra ägarskapet explicit, så att någon faktiskt kan prioritera och fatta beslut inom gränsen.

## Ägarskap måste vara tydligare än åtkomst

Ett vanligt arkitekturproblem uppstår när flera system kan läsa och skriva samma information utan att det är tydligt vem som faktiskt äger den.

Det är viktigt att skilja mellan:

- vem som äger betydelsen av informationen,
- vem som är system of record eller auktoritativ källa,
- vem som får ändra den,
- vem som får läsa eller kopiera den,
- och vem som ansvarar för kvalitet och livscykel.

Att ett system tekniskt kan skriva i en tabell betyder inte att det bör ha rätt att ändra informationens verksamhetsmässiga innebörd.

```text
Domän A äger uppgiften
        │
        ├─ publicerar kontrakt/händelser
        │
        ▼
Domän B använder uppgiften
        │
        └─ får inte bli parallell ägare
```

En konsument kan behöva en lokal kopia för sökning, analys, tillgänglighet eller prestanda. Det gör inte kopian till ny auktoritativ källa. Ägarskapet behöver därför beskrivas oberoende av den fysiska lagringen.

Ett vanligt tecken på otydligt ägarskap är att flera team kan korrigera samma verksamhetsuppgift direkt därför att det är tekniskt enklast. Det löser ett kortsiktigt problem men gör det svårt att veta vilken regel som ska gälla vid konflikt. Ett tydligare ansvarssnitt låter i stället ägande domän avgöra ändringen och publicera resultatet till konsumenterna. Det kan innebära mer explicit kommunikation, men minskar antalet platser där verksamhetsregler behöver hållas synkroniserade.

## Gränser, integration och autonomi

Arkitekturgränser finns på flera nivåer. En begreppsgräns avgör var en viss definition gäller. En ansvarsgräns avgör vem som får besluta om regler och beteenden. En datagräns beskriver vem som är auktoritativ källa. En förändringsgräns avgör vad som ska kunna releasas oberoende. Säkerhets-, tillits- och exekveringsgränser kan sedan ge ytterligare tekniska avgränsningar.

Dessa gränser behöver inte sammanfalla. Ett bounded context kan realiseras som flera moduler i samma applikation. Två domäner kan köras i samma runtime men ändå ha separerade datamodeller och tydliga ansvar. Omvänt skapar två mikrotjänster inte automatiskt två välavgränsade domäner om de delar samma begrepp, databas och förändringscykel.

Det är därför användbart att beskriva gränser explicit i arkitekturen. En lösning kan till exempel ha en tydlig ansvars- och datagräns mellan två domäner men ingen fysisk exekveringsgräns ännu. Det kan vara ett fullt medvetet val. Om behovet av oberoende skalning, säkerhetsisolering eller releasefrekvens senare ökar kan den tekniska gränsen flyttas utan att ansvarsfördelningen behöver ritas om.

Integration är därför en del av domändesignen, inte bara ett tekniskt steg efteråt. Vid en domängräns behöver det vara tydligt vem som initierar kommunikationen, vem som äger kontraktet, vilken information som får lämna domänen och hur förändringar versioneras. Först därefter blir valet mellan API, meddelanden, events, filutbyte och andra mekanismer meningsfullt.

```text
Ansvar och domängräns
          ↓
Informationskontrakt
          ↓
Kvalitetskrav
          ↓
Integrationsmönster
          ↓
Teknisk realisering
```

Tydliga gränser skapar också faktisk autonomi. Ett team kan bara förändra självständigt om det vet vilka beslut det äger, vilka kontrakt det måste respektera och vilken information det får förändra. Ett team som delar databas och verksamhetslogik med fem andra team kan ha stor formell frihet men liten praktisk autonomi.

> Tydliga gränser begränsar vissa lokala val men ökar den praktiska friheten inom gränsen.

## Gemensam plattform ska inte bli en verksamhetsdomän

När en organisation bygger gemensamma plattformar uppstår ibland en subtil förskjutning. Plattformen börjar med generell teknik men tar gradvis över verksamhetslogik för att ”göra det enklare” för konsumenterna.

Ett workflow-erbjudande kan exempelvis börja innehålla organisationens specifika regler för ärendeprioritering. En integrationsplattform kan börja tolka verksamhetens domänobjekt. En gemensam dataplattform kan bli den plats där begrepp och affärsregler bestäms, trots att plattformsteamet saknar verksamhetsmandat.

Det gör plattformen svårare att återanvända och flyttar verksamhetsansvaret bort från den domän som bäst kan förstå och förändra det.

> En gemensam plattform får gärna bära generella tekniska mekanismer, men den bör vara försiktig med att bära verksamhetsspecifik mening och beslut.

En messagingplattform kan ansvara för leverans, autentisering, retention och observerbarhet utan att bestämma vad en verksamhetshändelse betyder. En regelplattform kan erbjuda exekvering, versionshantering och spårbarhet medan verksamhetsdomänen äger själva regelinnehållet.

## Gemensamma kontrakt utan gemensam intern modell

Interoperabilitet kräver ofta gemensamma kontrakt, men det betyder inte att alla interna modeller måste vara identiska.

Anta att två domäner behöver utbyta information om ett beslut. Domän A kanske använder en intern modell med ett tiotal objekt och detaljerade statusar. Domän B behöver bara veta beslutets identitet, utfall, datum och vilken part det gäller.

Ett explicit integrationskontrakt kan då vara bättre än att Domän B tvingas använda Domän A:s fullständiga interna modell:

```text
Domän A:s interna modell
          ↓
   publicerat kontrakt
          ↓
Domän B:s egen modell
```

Det gör båda domänerna friare att förändras internt. En gemensam kanonisk modell kan vara värdefull för vissa stabila, verkligt gemensamma begrepp och kodverk, men blir problematisk om den försöker ersätta all lokal semantik.

Målet är inte maximal enhetlighet. Målet är tillräcklig gemensam förståelse vid gränsen.

## Federation när ansvaret är gemensamt men kunskapen lokal

Vissa frågor passar varken för full lokal autonomi eller full centralisering. Då kan den federerade ansvarmodell som introducerades i föregående kapitel användas för domänspecifik semantik.

Flera domäner kan exempelvis använda samma centrala begrepp – person, organisation eller geografisk plats – men med olika perspektiv. Organisationen kan då behöva gemensamma identifierare, en gemensam kärndefinition och vissa kvalitetsregler, samtidigt som varje domän äger sina lokala utvidgningar.

Det kräver tydligt ägarskap för kärnan, explicita kontrakt och en process för förändringar i den gemensamma semantiken. Federation är alltså inte otydligt delat ansvar; den kräver ofta skarpare gränser än en central modell.

En användbar kontrollfråga är därför om varje förändring har en tydlig beslutsägare. Om en ändring i den gemensamma kärnan kräver konsensus mellan alla konsumenter har modellen sannolikt inte blivit federerad utan bara distribuerat sitt otydliga ägarskap. Federering fungerar bäst när den gemensamma kärnan är liten och stabil och när lokala variationer kan utvecklas utan att alla andra behöver involveras.

## Två vanliga sätt att förstöra domängränser

### Den centrala allt-i-allo-tjänsten

En central tjänst kan börja med ett rimligt gemensamt ansvar men successivt få ansvar för allt som flera system råkar behöva: identitet, kontaktuppgifter, preferenser, behörigheter, avtal, ärendehistorik, dokument och verksamhetsregler.

På pappret ser det ut som återanvändning. I praktiken blir tjänsten ofta en semantisk monolit och organisatorisk flaskhals. Alla domäner behöver förändra den och tjänstens modell fylls med specialfall.

Problemet är inte att tjänsten är central, utan att ansvaret saknar sammanhängande gräns. Verkligt gemensamma identitets- och referensdata, domänspecifik information och generella tekniska tjänster behöver ofta separeras även om det ger fler komponenter.

### Delad databas som integrationsmodell

En annan genväg är att flera domäner eller applikationer använder varandras tabeller direkt. Det är enkelt i början men gör databasschemat till ett dolt gemensamt kontrakt. När en tabell ändras kan flera konsumenter gå sönder och ägarskapet blir oklart.

Det innebär inte att varje modul måste ha en separat fysisk databas. Två moduler kan använda samma databasinstans men separata scheman och definierade gränssnitt. Omvänt kan två tjänster ha separata databaser men ändå vara starkt kopplade om de ständigt måste samordna modeller och releaser.

Fysisk separation är ett verktyg – inte definitionen av en bra gräns.

## Hur man hittar bättre gränser

Det finns ingen mekanisk metod som alltid ger rätt domängränser, men ett antal frågor är praktiskt användbara:

- Vilka begrepp används med samma betydelse och vilka betyder olika saker i olika sammanhang?
- Vilka regler förändras av samma anledning?
- Vem har kunskap och mandat att fatta beslut?
- Vilken information är auktoritativ var?
- Var uppstår återkommande samordning mellan team?
- Vilken variation är legitim och bör därför få finnas kvar?
- Vilka beroenden bör vara riktade producent–konsumentrelationer i stället för ömsesidig kännedom om interna modeller?

Frågorna bör användas som hypoteser, inte som absoluta regler. Precis som förmågekartan behöver domängränser kunna justeras när organisationen lär sig mer.

Det är ofta värdefullt att testa en föreslagen gräns mot konkreta förändringsscenarier. Välj några realistiska förändringar – en ny regel, ett nytt informationsfält, ett ändrat integrationskontrakt eller ett nytt kvalitetskrav – och fråga vilka team, modeller och releaser som måste beröras. Om nästan varje scenario passerar samma gräns är den sannolikt för porös eller placerad på fel ställe. Om två delar däremot nästan alltid förändras tillsammans kan separationen vara onödigt dyr.

Även driftincidenter kan ge signaler. Om en incident i en domän regelbundet kräver specialistkunskap från flera andra domäner, eller om felsökning kräver direkt åtkomst till andras interna data, kan ansvarssnittet behöva göras tydligare.

## En praktisk modell: från ansvar till teknik

När en ny lösning eller ett nytt verksamhetsområde ska designas kan följande ordning vara användbar:

```text
1. Identifiera verksamhetsansvar
        ↓
2. Identifiera centrala begrepp och regler
        ↓
3. Formulera domängränser och ägarskap
        ↓
4. Beskriv informationsutbyte mellan gränser
        ↓
5. Identifiera kvalitetskrav för gränssnitten
        ↓
6. Välj mönster och gemensamma förmågor
        ↓
7. Välj plattformar och teknisk realisering
```

Gemensam arkitektur svarar på vilka byggstenar och ramar organisationen kan återanvända. Domänanalysen svarar på vilket ansvar som ska byggas med dem. Båda perspektiven behövs.

Den tidigare etablerade ansvarmodellen kan här användas direkt: den gemensamma nivån sätter spelregler och tvärgående krav, förmågeområdet erbjuder generella mekanismer och vägledning, medan den verksamhetsnära lösningen äger sin domänmodell, sina regler och sin information. Poängen är inte att introducera ytterligare en ansvarmodell, utan att se till att gemensamma byggstenar stärker domängränserna i stället för att sudda ut dem.

## Gränsen är en hypotes som måste prövas

Det finns sällan en perfekt domänmodell som kan ritas fram en gång för alla. Gränser är hypoteser som behöver prövas mot faktisk förändring.

Tecken på att en gräns bör omprövas kan vara återkommande synkroniserade releaser, stora mängder gemensam verksamhetslogik, samma information som ändras från flera håll, en central komponent som fylls med domänspecifika specialfall eller ett team som ständigt behöver beslut från ett annat team för att förändra sin egen produkt.

Det motsatta kan också inträffa. Två områden som separerats kan visa sig ha så stark cohesion att uppdelningen skapar mer koordinering än självständighet.

Arkitekturens mål är därför inte maximalt antal gränser, utan gränser som gör ansvar och förändring begripliga.

En gräns som fungerar väl över tid brukar ge två praktiska effekter: förändringar inom området kan oftast göras utan bred samordning, och förändringar som passerar gränsen sker genom ett litet antal kända kontrakt. Det är ett mer användbart kvalitetskriterium än att räkna tjänster, databaser eller team.

## Sammanfattning

Gemensamma IT-förmågor och domäner kompletterar varandra men löser olika problem. Förmågemodellen beskriver vilket återanvändbart IT-stöd organisationen behöver kunna erbjuda. Domänperspektivet beskriver var verksamhetens egen mening, regler, information och förändringsansvar hör hemma.

Bra gränser samlar sådant som förändras tillsammans, gör ägarskap och semantik tydliga och begränsar beroenden mellan ansvarssytor. Gemensamma plattformar bör bära generella mekanismer snarare än verksamhetsspecifik mening, och interoperabilitet kräver gemensamma kontrakt men inte nödvändigtvis en gemensam intern modell.

Tekniska gränser som API:er, processer och databaser är verktyg för att realisera ansvarssnitt – inte en ersättning för domänanalysen. Gränser behöver dessutom kunna omprövas när förändringsmönster och beroenden visar att den ursprungliga hypotesen inte håller.

I nästa kapitel flyttas fokus från ansvarssnitten till det som passerar genom dem: information och data som arkitekturella ingångsvärden.

## Källor och vidare läsning

**[K1]** Eric Evans, *Domain-Driven Design Reference* (2015), särskilt Strategic Design och Bounded Context. https://www.domainlanguage.com/ddd/reference/
