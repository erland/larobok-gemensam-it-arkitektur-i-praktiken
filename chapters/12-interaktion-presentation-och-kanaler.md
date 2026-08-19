# 12. Interaktion, presentation och kanaler

När människor möter ett IT-stöd möter de sällan dess interna arkitektur. De möter ett gränssnitt.

Det kan vara en publik e-tjänst, ett internt handläggningsstöd, en mobil klient, en självserviceportal eller ett administrativt verktyg. För användaren är detta ofta hela systemet. Om gränssnittet är svårt att förstå, långsamt, otillgängligt eller inkonsekvent spelar det liten roll att bakomliggande tjänster är tekniskt välstrukturerade.

Samtidigt är användargränssnitt ett område där lokal variation lätt växer snabbt. Ett team väljer ett frontend-ramverk, ett annat skapar egna komponenter, ett tredje bygger en särskild notifieringslösning och ett fjärde etablerar en ny portalstruktur. Varje beslut kan vara rimligt i sitt lokala sammanhang, men tillsammans kan de skapa en flora av tekniker, interaktionsmönster och förvaltningsmodeller som är dyr att bära.

Förmågan Interaktion, presentation och kanaler handlar därför om vad ett stödjande IT-område varaktigt behöver kunna erbjuda för att organisationens digitala gränssnitt ska bli användbara, tillgängliga, säkra, förändringsbara och kostnadseffektiva.

Det betyder inte att en central funktion ska designa alla gränssnitt. Det betyder heller inte att alla kanaler ska se identiska ut eller byggas med samma teknik. Förmågan ska i stället skapa en gemensam grund där sådant som vinner på återanvändning kan standardiseras, samtidigt som verksamhetsnära team behåller ansvar för sina faktiska användare, arbetsuppgifter och funktionella behov.

## Förmågan börjar i användningssituationen

Ett vanligt misstag är att börja diskussionen om interaktion med teknik:

- ska vi använda ett visst JavaScript-ramverk?
- ska detta vara en app eller webb?
- behöver vi en portal?
- ska vi bygga ett SPA?
- ska vi använda samma komponentbibliotek som ett annat system?

Detta är realiseringsfrågor. De kan vara viktiga, men de kommer senare.

Den första frågan bör vara:

> Vilken användningssituation behöver stödjas, och vilka egenskaper måste interaktionen ha för att fungera där?

Ett internt handläggningsstöd som används åtta timmar om dagen har andra behov än en publik e-tjänst som en person använder någon gång per år. Ett operativt stöd i fält har andra förutsättningar än en administrativ webbapplikation på kontoret. En tjänst som används av externa företag kan behöva fungera med andra identiteter, webbläsare, språk och supportmönster än ett internt verktyg.

Därför behöver analysen börja med exempelvis:

- vilka användargrupper som finns,
- vilka uppgifter de försöker utföra,
- hur ofta tjänsten används,
- vilken enhet och miljö användningen sker i,
- om användaren är intern eller extern,
- om uppgiften är tidskritisk,
- om arbetet måste kunna utföras med begränsad uppkoppling,
- vilka tillgänglighetsbehov som behöver mötas,
- vilken information som visas eller matas in,
- och vilka konsekvenser ett missförstånd eller felaktigt handhavande kan få.

Detta är samma princip som tidigare i boken: behov före teknik. För interaktionsförmågan innebär den att kanal, presentationsform och klientarkitektur ska motiveras av användningssituationen i stället för av vilket ramverk organisationen råkar ha mest erfarenhet av.

## Förmågan är bredare än frontendutveckling

Det är frestande att likställa Interaktion, presentation och kanaler med frontendteknik. Det blir för smalt.

Förmågan behöver typiskt omfatta stöd för flera typer av frågor:

- webbarkitektur,
- visuella och interaktiva designmönster,
- design system och återanvändbara UI-komponenter,
- formulär och felpresentation,
- navigation och informationspresentation,
- responsivitet,
- mobil användning,
- klientnära tillstånd,
- notifieringar,
- flerspråkighet,
- frontend-ramverk,
- browser support,
- klientnära säkerhet,
- klientnära observerbarhet,
- och relationen mellan klienten och bakomliggande API:er.

Det viktiga är att dessa frågor hänger ihop ur konsumentens perspektiv. Ett utvecklingsteam som ska bygga en ny e-tjänst vill sällan konsumera tjugo separata styrdokument och själv försöka förstå hur allt ska kombineras. Ett moget förmågeområde behöver kunna erbjuda en sammanhållen väg från behov till rekommenderad realisering.

Det kan exempelvis innebära att teamet får tillgång till:

- ett gemensamt design system,
- ett rekommenderat webbapplikationsramverk,
- färdiga integrationsmönster mot identitetstjänster,
- riktlinjer för klient/server-gränsen,
- teststöd för tillgänglighet,
- säkerhetsbaseline för webbläsarklienter,
- mallar för formulär,
- och en gemensam browser support policy.

Detta är förmågestöd. Den faktiska verksamhetsupplevelsen måste fortfarande utformas i den lösning där användarbehovet finns.

## Gränsen mot andra förmågor är avgörande

Interaktionsförmågan ligger nära nästan alla andra förmågor i boken. Därför är gränsdragningen viktig.

Ett användargränssnitt kan exempelvis visa ett ärende, men ärendehanteringen tillhör inte interaktionsförmågan. Ett formulär kan ge återkoppling om en verksamhetsregel, men den auktoritativa regeln hör hemma i förmågan Regler och beslut. En klient kan initiera sökning, men själva söktjänsten och indexeringen hör hemma i Analys, sökning och AI.

Samma princip gäller för identitet. Interaktionsförmågan behöver beskriva hur inloggning, sessioner, utloggning och behörighetsfel möter användaren. Men autentisering, federation, tjänsteidentitet och andra tillitsmekanismer tillhör Identitet och tillit.

På motsvarande sätt kan en frontend konsumera API:er, men API management, meddelandekommunikation och integrationskontrakt hör hemma i Integration och kommunikation.

Den praktiska gränsen kan formuleras så här:

> Interaktionsförmågan äger hur användaren möter och använder funktionaliteten. När frågan övergår till att handla om den auktoritativa verksamhetslogiken, informationen eller den tekniska mekanismen bakom funktionen tar en annan förmåga över.

Detta minskar risken att frontend blir ett lager där ansvar från resten av arkitekturen råkar samlas.

## Presentation ska inte bli bärare av auktoritativ verksamhetslogik

Ett vanligt problem i äldre och även moderna system är att kritisk verksamhetslogik byggs in i klienten.

Det kan börja oskyldigt. Ett formulär behöver kontrollera att ett datum är rimligt. En knapp ska bara visas för vissa användare. Ett belopp ska beräknas direkt i gränssnittet. Med tiden växer klienten och fler regler hamnar där eftersom det är snabbt och ger bra användarrespons.

Problemet uppstår när klientens logik börjar betraktas som auktoritativ.

En användarklient är normalt inte rätt plats för:

- slutlig behörighetskontroll,
- auktoritativ validering,
- kritiska verksamhetsregler,
- normerande beräkningar,
- eller beslut som måste vara konsekventa över flera kanaler.

Klienten kan mycket väl ge tidig återkoppling. Ett formulär kan exempelvis markera att ett fält har fel format innan information skickas till servern. Men den betrodda tjänsten behöver fortfarande verifiera det som är relevant för verksamhetsbeslut, informationsintegritet och säkerhet.

Det finns flera skäl till detta.

För det första kan klientkod förändras eller manipuleras. För det andra kan samma verksamhetsfunktion senare behöva användas från en annan kanal. För det tredje blir regler svårare att förvalta om deras normerande version är utspridd över flera klienter.

Det innebär inte att all logik ska flyttas från frontend. Interaktionslogik hör naturligt hemma där. Exempel är:

- visning och döljning av komponenter för bättre användarupplevelse,
- navigationslogik,
- lokal formatering,
- klientnära tillstånd,
- optimistisk återkoppling,
- och presentation av valideringsresultat.

Frågan är alltså inte om klienten får innehålla logik, utan vilken typ av logik den får vara auktoritativ för.

## Design system som gemensamt erbjudande

Ett av de tydligaste exemplen på vad som kan vinna på gemensamt ansvar är ett design system.

Ett design system är mer än en samling färdiga knappar. Ett moget erbjudande kan kombinera:

- visuella designprinciper,
- typografi och design tokens,
- återanvändbara komponenter,
- etablerade interaktionsmönster,
- tillgänglighetsstöd,
- dokumentation,
- versionshantering,
- och ibland kodbibliotek för ett eller flera ramverk.

Värdet är inte bara att gränssnitt ser mer enhetliga ut.

Gemensamma komponenter kan koncentrera arbete som annars skulle behöva upprepas i många team. Ett tillgängligt formulärfält, en korrekt felpresentation eller en robust dialogkomponent kan vara dyr att designa, implementera och testa väl. Om varje team gör det separat får organisationen både högre kostnad och större variation i kvalitet.

Ett gemensamt design system kan därför ge skalfördelar inom:

- användbarhet,
- tillgänglighet,
- design,
- frontendutveckling,
- kvalitetssäkring,
- och livscykelhantering.

Men designsystemet ersätter inte verksamhetsnära UX-arbete.

En komponent kan vara tillgänglig och väl utformad i sig men användas på ett olämpligt sätt i en viss tjänst. Ett designsystem kan inte avgöra vilken information som ska visas först för en handläggare, vilken ordning ett komplext formulär bör ha eller hur en viss målgrupp bäst förstår ett verksamhetsbegrepp.

Därför är ansvarsfördelningen viktig:

Förmågeområdet kan äga komponenter, designprinciper och gemensamma interaktionsmönster. Lösningsteamet äger hur dessa används för att skapa en fungerande upplevelse i den faktiska verksamhetskontexten.

## Tillgänglighet behöver byggas in i förmågan

Digital tillgänglighet är ett tydligt exempel på en kvalitet som inte bör behandlas som en slutkontroll.

W3C:s Web Content Accessibility Guidelines, WCAG, strukturerar tillgänglighetskrav kring principerna att innehåll ska vara möjligt att uppfatta, hantera, förstå och använda robust med olika tekniker.[K1] Den praktiska konsekvensen för arkitekturen är viktigare här än den enskilda standardversionen: tillgänglighet påverkas av design, semantik, komponentval, tangentbordsinteraktion, felhantering, navigation och testbarhet genom hela utvecklingslivscykeln.

Om organisationen väntar till slutet och därefter testar färdiga sidor kan många fel vara dyra att rätta. Ett olämpligt komponentbibliotek, ett egenbyggt interaktionsmönster eller en felaktig struktur kan redan vara djupt integrerad i tjänsten.

Förmågeområdet kan därför göra tillgänglighet enklare genom att tillhandahålla:

- semantiskt korrekta komponenter,
- dokumenterade tangentbordsmönster,
- vägledning för fokus och felpresentation,
- teststöd,
- automatiserade kontroller där de ger värde,
- och gemensamma kvalitetskriterier.

Men även här gäller samma ansvarsfördelning: en tekniskt korrekt komponent garanterar inte att hela tjänsten är begriplig och användbar.

## Kanalval är ett arkitekturbeslut

Orden *kanal* och *gränssnitt* blandas ibland ihop. En kanal beskriver i detta sammanhang sättet eller sammanhanget där användaren möter tjänsten, exempelvis:

- responsiv webb,
- särskild mobilapplikation,
- intern webbapplikation,
- publik självservice,
- portal,
- notifieringskanal,
- eller ett konversationsbaserat gränssnitt.

Det finns sällan en kanal som är bäst i alla situationer.

### Responsiv webb

Responsiv webb är ofta ett starkt förstahandsalternativ när samma funktion ska vara tillgänglig på flera skärmstorlekar och lösningen inte kräver särskilt djup integration med enheten.

Fördelarna kan vara:

- en gemensam distributionsmodell,
- låg tröskel för användaren,
- mindre fragmentering mellan plattformar,
- och enklare gemensam livscykel.

Men responsivitet löser inte automatiskt alla mobila användningsproblem. Ett gränssnitt som tekniskt passar på en liten skärm kan fortfarande vara olämpligt i fält, med handskar, dålig uppkoppling eller behov av kamera och bakgrundssynkronisering.

### Särskild mobilapplikation

En särskild mobilklient kan vara motiverad när användningssituationen kräver egenskaper som:

- avancerat offlinearbete,
- omfattande lokal synkronisering,
- kamera eller sensorer,
- positionering,
- pushfunktioner,
- bakgrundsarbete,
- eller djupare integration med enhetens säkerhetsmekanismer.

Detta medför samtidigt större ansvar för distribution, device management, versionshantering, kompatibilitet och säkerhet. Därför bör en separat app vara ett motiverat val, inte en statusmarkör för att tjänsten uppfattas som modern.

## Minsta nödvändiga klientkomplexitet

Klientteknik är ett område där lösningar lätt blir mer avancerade än behoven kräver.

Ett rikt interaktivt handläggningsstöd kan behöva en omfattande klientapplikation med lokal tillstånd management, avancerad navigation och många interaktiva komponenter. En enkel publik informations- eller formulärtjänst kan däremot fungera utmärkt med en enklare serverrenderad modell.

Detta kan uttryckas som en princip:

> Klienten bör inte vara mer komplex än användningsfallet kräver.

Mer klientkomplexitet ger inte bara fler funktioner. Den för också med sig kostnader:

- större beroendeträd,
- tätare uppgraderingsbehov,
- mer klientnära säkerhetsarbete,
- fler felmoder,
- mer avancerad byggkedja,
- fler tester,
- och ibland svårare felsökning.

Därför bör organisationens standardiserade webberbjudande vara en rekommenderad väg när behovet passar, inte ett krav att varje webbsida byggs med samma applikationsramverk.

Det är en viktig skillnad mellan en standardiserad förmåga och teknikmonokultur.

## Web Application Framework som plattformstjänst

Ett gemensamt Web Application Framework kan vara ett konkret plattformserbjudande inom förmågan.

Erbjudandet bör dock inte definieras som namnet på ett specifikt ramverk. Dess konsumentvärde är större än så.

Det kan exempelvis ge team:

- standardiserad projektstruktur,
- integration med design system,
- etablerad autentiseringsintegration,
- testkonventioner,
- säkerhetskontroller,
- bygg- och leveransstöd,
- browser support,
- integrationspunkter för observerbarhet,
- dokumentation,
- och en definierad support- och uppgraderingsmodell.

Ett tekniskt ramverk som Angular, React eller något annat kan vara den aktuella realiseringen. Men det är inte själva tjänsten.

Detta följer bokens generella metamodell:

```text
Interaktion, presentation och kanaler
                ↓
      Web Application Framework
                ↓
 projektmallar, bibliotek och integrationer
                ↓
  aktuellt ramverk, version och konfiguration
```

Om det tekniska ramverket byts ska förmågan och det konsumentnära erbjudandets syfte fortfarande kunna bestå.

## Frontendens relation till backend

En klient behöver nästan alltid hämta, skicka eller förändra information i bakomliggande tjänster. Där uppstår en viktig arkitekturfråga:

> Ska klienten konsumera befintliga API:er direkt eller behöver den ett kanalnära backendlager?

I vissa lösningar är ett direkt API-kontrakt fullt tillräckligt. Att lägga till ytterligare ett lager skulle bara skapa mer kod, drift och livscykel.

I andra situationer kan ett Backend for Frontend, BFF, vara lämpligt.

Ett BFF kan exempelvis:

- aggregera information från flera bakomliggande tjänster,
- ge klienten ett kontrakt anpassat till kanalens behov,
- minska antalet nätverksanrop,
- isolera klienten från interna tjänsteförändringar,
- hantera vissa kanalnära sessions- eller tokenflöden på serversidan,
- och minska behovet av att exponera interna API:er direkt mot klientmiljön.

Men ett BFF är ett lösningsmönster, inte ett obligatoriskt arkitekturlager. Om varje frontend automatiskt får en BFF oavsett behov har organisationen bara skapat ytterligare ett standardiserat lager att utveckla, drifta och felsöka.

Det djupare resonemanget om BFF och andra lösningsmönster kommer i del IV. I detta förmågekapitel räcker det att konstatera att interaktionsförmågan behöver hjälpa team att välja ett ändamålsenligt klient/backend-gränssnitt.

## Klientnära tillstånd och lokal lagring

Moderna klienter kan lagra stora mängder information lokalt. Det är tekniskt enkelt och därför lätt att göra utan att först analysera konsekvenserna.

För varje form av lokalt tillstånd behöver man fråga:

- varför informationen behöver finnas i klienten,
- hur länge den behöver finnas,
- hur känslig den är,
- vad som händer om enheten delas eller förloras,
- hur gammal information får bli,
- om informationen kan återskapas,
- och om den måste raderas när sessionen avslutas.

Lokal lagring ska inte bli en skuggdatabas för auktoritativ verksamhetsinformation.

Det kan däremot finnas legitima behov av exempelvis:

- tillfällig formulärstate,
- användarpreferenser,
- cache för prestanda,
- offlinearbete,
- eller återupptagning av en pågående uppgift.

Behovet avgör mekanismen. Informationsklassning och kvalitetskrav avgör vilka skydd och begränsningar som behövs.

## Säkerhet i klienten är mer än inloggning

När säkerhet diskuteras i användargränssnitt hamnar fokus ofta på autentisering. Det är bara en del av problemet.

Klientnära säkerhet omfattar också frågor som:

- var tokens och sessionsinformation hanteras,
- vilka uppgifter som får ligga i lokal lagring,
- vad som får visas i felmeddelanden,
- om känslig information får exporteras eller skrivas ut,
- hur tredjepartsbibliotek hanteras,
- vilka externa resurser klienten laddar,
- och hur teknisk telemetri utformas utan att samla in onödiga person- eller verksamhetsuppgifter.

En grundregel är att hemligheter som privata nycklar eller servercredentials inte ska distribueras till en klient som användaren kontrollerar. På samma sätt behöver backend göra de auktoritativa behörighetskontrollerna även om klienten anpassar vad som visas för att ge en bättre användarupplevelse.

Den fullständiga tillitsmodellen behandlas senare i kapitel 18. Interaktionsförmågan behöver framför allt säkerställa att dess standarder och gemensamma byggstenar inte gör det lätt att bygga klienter som underminerar den modellen.

## Notifieringar är både interaktion och integration

Notifieringar är ett bra exempel på att förmågegränser inte alltid är självklara.

Ur användarens perspektiv är notifieringen en del av interaktionen. Den ska komma vid rätt tidpunkt, i rätt kanal och med ett begripligt innehåll.

Ur den tekniska arkitekturens perspektiv kan notifieringen samtidigt kräva integration mot e-post, SMS, pushinfrastruktur eller externa leverantörer.

Det gör att ansvaret kan delas:

- Interaktionsförmågan kan äga principer för kanalval, användarupplevelse och vilken typ av innehåll som lämpar sig för olika kanaler.
- Integrationsförmågan kan äga tekniska transportmekanismer och gemensamma anslutningar.
- En gemensam notifieringstjänst kan ligga organisatoriskt på ett ställe men fortfarande realisera behov från flera förmågor.

Det viktiga är inte vilken ruta i organisationsschemat tjänsten hamnar i. Det viktiga är att konsumentansvar, plattformsansvar och arkitekturgränser är tydliga.

## Observerbarhet börjar även i klienten

Ett distribuerat användarflöde kan passera webbläsare, gateway, BFF, flera backend-tjänster och databaser. Om ett fel bara uppfattas som ”något gick fel” i klienten blir felsökningen dyr.

Därför behöver interaktionsförmågan stödja klientnära observerbarhet.

Det kan innebära att:

- tekniska fel får korrelationsidentifierare,
- klienthändelser kan kopplas till backendanrop,
- versionsinformation går att fastställa,
- felkategorier är standardiserade,
- och relevant telemetri kan samlas in.

Men observerbarhet får inte bli synonymt med att skicka hela användarens data till centrala loggar. Informationsskyddet måste finnas kvar även i felsökningsmekanismerna.

Den centrala observerbarhetsplattformen hör till Driftbarhet och motståndskraft. Interaktionsförmågan ansvarar för att klienten producerar användbar och säker signalering till den.

## Tekniken förändras snabbare än förmågan

Frontendområdet illustrerar tydligt varför boken separerar stabil arkitektur från teknisk realisering.

Ramverk, byggverktyg, bibliotek och browserfunktioner förändras snabbare än organisationens grundläggande behov av digital interaktion.

Förmågan bör därför uttryckas stabilt:

> Organisationen behöver kunna skapa och förvalta användbara, tillgängliga, säkra och sammanhängande digitala gränssnitt över relevanta kanaler.

Plattformserbjudandet kan vara mer konkret:

> Organisationen erbjuder en standardiserad väg för större webbaserade klientapplikationer.

Teknikstandarden kan vara ännu mer konkret:

> För en viss period rekommenderas ett visst ramverk, språk och stödd versionsfamilj.

Och den tekniska dokumentationen får vara mest föränderlig:

> Så här konfigureras den aktuella versionen, byggverktyget och projektmallen.

Genom denna separation kan ramverket bytas utan att hela förmågemodellen behöver skrivas om.

## Typiska kvalitetsattribut för förmågan

Alla kvalitetsattribut från kapitel 4 kan vara relevanta, men vissa återkommer särskilt ofta inom interaktion och presentation.

### Användbarhet

Gränssnittet måste hjälpa användaren att utföra sin uppgift korrekt och effektivt. För ett internt arbetsstöd kan snabb navigation och stöd för frekvent användning vara viktigare än visuell förenkling. För en sällan använd publik tjänst kan tydlighet och vägledning väga tyngre.

### Tillgänglighet

Tjänsten behöver fungera för användare med olika funktionsförutsättningar och hjälpmedel. Detta påverkar både design och teknisk implementation och behöver byggas in i komponenter, interaktionsmönster och test.

### Prestanda

Användarupplevd prestanda påverkas av mer än serversvarstid. Paketstorlek, rendering, antal nätverksanrop, latens, cache och klientens hårdvara kan alla påverka upplevelsen.

### Säkerhet och informationsskydd

Sessioner, lokal lagring, export, notifiering, felpresentation och tredjepartsberoenden är exempel på klientnära säkerhetsfrågor.

### Förvaltningsbarhet

Frontendramverk och beroenden kan ha snabb livscykel. Standardiserad struktur, gemensamma komponenter och en tydlig supportpolicy minskar kostnaden för att hålla applikationer uppdaterade.

### Interoperabilitet och portabilitet

Öppna webbstandarder och stabila API-kontrakt minskar onödiga beroenden till ett visst ramverk eller en viss klientmiljö.

## Vad bör vara gemensamt och vad bör vara lokalt?

Kapitel 9 etablerade att gemensamt ansvar ska motiveras, inte antas. Interaktionsförmågan är ett bra område för att tillämpa den principen.

Sådant som ofta lämpar sig väl för gemensamt ansvar är:

- design system,
- tillgänglighetsbaseline,
- browser support policy,
- frontend security baseline,
- rekommenderade projektstrukturer,
- integration mot gemensam identitet,
- standardiserad telemetri,
- och ett eller flera stödda webbutvecklingserbjudanden.

Sådant som normalt behöver ligga nära verksamhetslösningen är:

- användarresor,
- informationsprioritering,
- verksamhetsspecifik navigation,
- lokala arbetsflöden,
- språk och innehåll,
- och den konkreta kombinationen av komponenter i ett visst användningsfall.

Mellan dessa finns ett federerat område. En lokal lösning kan exempelvis utveckla en ny komponent som senare visar sig vara generell nog att flyttas in i det gemensamma designsystemet. På samma sätt kan ett nytt kanalbehov först prövas lokalt och därefter bli ett gemensamt erbjudande om det återkommer.

Detta är ett exempel på den iterativa modell som introducerades i kapitel 7.

## En praktisk analysordning

När ett nytt interaktionsbehov uppstår kan förmågeområdet och lösningsteamet arbeta i ungefär följande ordning.

### 1. Beskriv användningssituationen

Vilka användare, uppgifter, miljöer, enheter och begränsningar finns?

### 2. Identifiera kvalitetskraven

Vilka krav finns på tillgänglighet, användbarhet, prestanda, säkerhet, kontinuitet och förvaltningsbarhet?

### 3. Välj kanal efter behov

Är responsiv webb tillräcklig? Behövs särskild mobil funktion? Är en befintlig produktplattform mer proportionerlig än egenutveckling?

### 4. Återanvänd gemensamma erbjudanden

Vilket design system, webbramverk, formulärstöd eller annan gemensam komponent täcker behovet?

### 5. Definiera klientens ansvar

Vilken tillstånd och vilken interaktionslogik hör hemma i klienten? Vilken logik måste vara auktoritativ på serversidan?

### 6. Definiera backendgränsen

Kan klienten använda befintliga API:er direkt eller finns behov av exempelvis BFF?

### 7. Bedöm informations- och säkerhetskonsekvenser

Vilka uppgifter får lagras lokalt, exporteras, visas i notifieringar eller skickas som telemetri?

### 8. Planera livscykeln

Vilka klientmiljöer stöds? Hur uppgraderas beroenden? Vem äger eventuella lokala komponenter och avsteg?

Ordningen ska inte användas mekaniskt. Den fungerar som ett sätt att säkerställa att teknikvalet inte blir det första beslutet och att ansvar från andra förmågor inte oavsiktligt hamnar i klienten.

## Förmågan som konsumerbart stöd

En mogen Interaktion, presentation och kanaler-förmåga bör inte bara bestå av principer i ett dokument. Den behöver bli användbar för utvecklingsteam.

Det kan innebära en kombination av:

- design system,
- dokumenterade interaktionsmönster,
- tillgänglighetsstöd,
- gemensamma komponentbibliotek,
- rekommenderat webbramverk,
- projektmallar,
- säkerhetsbaseline,
- browser support policy,
- exempelimplementationer,
- golden paths,
- och rådgivning för kanal- och klientarkitektur.

Det är först när stödet är lättare att använda än att uppfinna en lokal variant som standardisering på allvar börjar ge effekt.

Detta är också en viktig övergång till senare delar av boken. Förmågan beskriver vad organisationen behöver kunna erbjuda stöd inom. Lösningsmönstren beskriver senare återkommande sätt att strukturera lösningar. Plattformstjänsterna beskriver konsumerbara erbjudanden och standarderna anger vilken variation som organisationen vill styra.

## Sammanfattning

Interaktion, presentation och kanaler är förmågan som formar mötet mellan människor och organisationens digitala IT-stöd.

Den omfattar mer än frontend-ramverk. Den behöver ge ett sammanhållet stöd för kanalval, design system, komponenter, tillgänglighet, klientarkitektur, formulär, notifieringar, säkerhet, browser support och klientens relation till backend.

Samtidigt måste gränsen mot andra förmågor vara tydlig. Interaktionsförmågan ska inte ta över processlogik, verksamhetsregler, informationsägarskap, identitetsmekanismer eller integration bara för att funktionerna exponeras i ett gränssnitt.

Några centrala principer är:

- användarbehov och användningssituation styr kanalvalet,
- gemensamma komponenter återanvänds när de möter behovet,
- auktoritativ verksamhetslogik hålls utanför klienten,
- tillgänglighet och användbarhet byggs in från början,
- klientarkitekturen ska inte vara mer komplex än behovet kräver,
- klientnära säkerhet och informationsskydd är en del av lösningen,
- och frontendteknik ska kunna livscykelhanteras utan att organisationens stabila förmågemodell behöver förändras.

Förmågan visar därmed tydligt hur den gemensamma arkitekturmodellen är tänkt att fungera. Organisationen standardiserar inte användarupplevelsen genom att centralt designa varje tjänst. Den skapar i stället gemensamma byggstenar, principer och rekommenderade vägar som gör det lättare för lokala lösningsteam att skapa bra och långsiktigt hållbara gränssnitt.

I nästa kapitel flyttas fokus från användarens interaktion till sådant som ofta pågår över längre tid bakom gränssnittet: processer, workflow och ärendehantering.

## Källor och vidare läsning

**[K1]** W3C, *Web Content Accessibility Guidelines (WCAG) 2.2*, W3C Recommendation. https://www.w3.org/TR/WCAG22/
