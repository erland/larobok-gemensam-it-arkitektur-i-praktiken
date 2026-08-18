# Förmåga: Interaktion, presentation och kanaler

> **Status:** Utkast – steg 1  
> **Ansvarig:** Gemensam IT-arkitektur / ansvarig funktion för digitala gränssnitt  
> **Senast reviderad:** 2026-08-18

## 1. Syfte, omfattning och relationer

### 1.1 Syfte

Förmågan **Interaktion, presentation och kanaler** samlar den gemensamma IT-arkitektur som stödjer hur användare och andra aktörer möter myndighetens digitala IT-stöd. Syftet är att ge verksamhetsorienterade utvecklingsområden en gemensam grund för att skapa användbara, tillgängliga, säkra, sammanhållna och långsiktigt förvaltningsbara gränssnitt och kanaler.

Förmågan ska minska behovet av att varje utvecklingsområde själv tar ställning till återkommande frågor om exempelvis webbarkitektur, komponenter, formulär, kanalval och frontendteknik. Den ska samtidigt lämna utrymme för att lösningens faktiska behov styr valet av kanal och teknisk realisering.

Förmågan ska alltså inte definiera verksamhetens användarflöden eller funktionella behov. Den ska erbjuda principer, vägledning, standarder och gemensamma tjänster som gör det enklare för utvecklingsområdena att realisera dessa behov på ett enhetligt och ändamålsenligt sätt.

### 1.2 Omfattning

Förmågan omfattar gemensamma arkitekturfrågor och erbjudanden för bland annat:

- webbaserade användargränssnitt
- interna administrativa och handläggande gränssnitt
- publika e-tjänster och självservicegränssnitt
- responsiva gränssnitt för olika skärmstorlekar
- mobila användargränssnitt och, när behov finns, särskilda mobilapplikationer
- design system och återanvändbara UI-komponenter
- formulär, datainmatning och felpresentation
- navigation och informationspresentation
- användarnära notifieringar och kanalval
- klientnära tillstånds- och sessionshantering
- klientnära felhantering och observability
- stöd för flerspråkighet där verksamhetsbehov finns
- gemensamma frontendramverk och frontendstandarder
- relationen mellan presentation, backendtjänster och API:er
- kanalnära säkerhets- och integritetsfrågor
- användbarhet och digital tillgänglighet som kvaliteter i lösningen

Förmågan omfattar både sådant som konsumeras direkt av utvecklingsteam, exempelvis ett design system eller ett standardiserat webbramverk, och arkitekturvägledning för hur olika presentations- och kanalbehov bör realiseras.

### 1.3 Utanför förmågan

Följande ligger primärt i andra förmågeområden även när de används av ett användargränssnitt:

- **Process, workflow och ärendehantering** – verksamhetsprocesser, ärendeflöden och arbetsköer.
- **Regler och beslut** – verksamhetsregler, beslutstabeller och beslutslogik.
- **Data- och informationshantering** – persistens, dokumentlagring, databaser och informationslivscykel.
- **Analys, sökning och AI** – sökplattformar, analys, BI och AI-funktioner. Ett AI-baserat användargränssnitt kan använda denna förmåga men AI-funktionen i sig hör inte hit.
- **Integration och kommunikation** – API management, messaging, event och nätverkskommunikation.
- **Identitet och tillit** – identiteter, autentisering, auktorisation, federation och certifikat.
- **Applikationsexekvering och runtime** – miljöer där frontend- eller backendkomponenter exekveras.
- **Driftbarhet och motståndskraft** – central loggning, övervakning och återställning.
- **Programvaruutveckling och leverans** – källkod, bygg, test, CI/CD och utvecklingsmiljö.
- **Arbetsplats, samarbete och produktivitet** – generella arbetsverktyg som Microsoft Office och samarbetsytor.

Förmågan kan hänvisa till tjänster och standarder inom dessa områden men ska inte duplicera deras styrning.

### 1.4 Relation till andra förmågor

**Identitet och tillit** är nära kopplad till alla autentiserade användargränssnitt. Interaktionsförmågan beskriver hur identitetsfunktioner används i användarupplevelsen, medan identitetsförmågan äger mekanismer och tjänster för autentisering och auktorisation.

**Integration och kommunikation** tillhandahåller gränssnitt mellan frontend och bakomliggande tjänster. Ett frontendteam ska normalt konsumera definierade API:er eller ett kanalnära backendgränssnitt i stället för att exponeras direkt mot interna system eller databaser.

**Programvaruutveckling och leverans** tillhandahåller de verktyg och pipelines som används för att utveckla och leverera frontendkod. Denna förmåga anger vilka frontendarkitektoniska standarder som gäller men inte hur CI/CD-plattformen implementeras.

**Data- och informationshantering** påverkar bland annat hur data får presenteras, exporteras, cachas eller lagras lokalt. Informationskrav ska styra dessa beslut, inte klientteknikens möjligheter.

**Analys, sökning och AI** kan erbjuda funktioner som exponeras i ett användargränssnitt. Interaktionsförmågan ansvarar då för hur funktionen presenteras och används, medan analys-/AI-förmågan ansvarar för själva analys- eller AI-tjänsten.

---

## 2. Behov och användningsområden

### 2.1 Typiska behov

Utvecklingsområden kan exempelvis behöva:

- skapa ett nytt internt handläggnings- eller administrationsgränssnitt
- skapa eller modernisera en publik e-tjänst
- ge operativ personal tillgång till funktioner på mobil eller bärbar utrustning
- skapa en gemensam användarupplevelse över flera bakomliggande IT-stöd
- införa återanvändbara formulär och UI-komponenter
- stödja användare med olika funktionsförutsättningar
- ge användaren notifieringar om händelser eller uppgifter
- presentera information från flera tjänster i en sammanhållen vy
- stödja olika språk eller målgrupper
- minska lokal variation i frontendteknik och komponenter
- byta eller uppgradera frontendteknik utan att behöva förändra verksamhetslogik
- skapa ett gränssnitt som kan utvecklas och driftsättas oberoende av bakomliggande tjänster

### 2.2 Typiska användningsfall

#### Internt handläggningsstöd

En handläggare behöver en webbaserad arbetsyta för att söka fram information, hantera ett ärende och initiera verksamhetsfunktioner. Gränssnittet behöver vara effektivt för frekvent användning, stödja tangentbordsnavigation och hantera information med definierade skyddsbehov.

Förmågan kan bidra med design system, webbramverk, formulärkomponenter och vägledning för kanalnära backend/API, medan ärendelogik, data och identitet hanteras av andra förmågor.

#### Publik e-tjänst

En privatperson eller ett företag behöver lämna information till myndigheten via ett digitalt formulär. Lösningen behöver fungera på olika enheter, ge tydlig återkoppling och hantera autentisering där detta krävs.

Förmågan bidrar med principer för tillgänglighet, responsivitet, formulär, felpresentation och webbarkitektur. Verksamhetsprocessen och informationshanteringen ligger utanför förmågan.

#### Operativ mobil användning

Personal behöver kunna använda ett IT-stöd i fält där uppkoppling, skärmstorlek och arbetssituation skiljer sig från kontorsmiljön. Det kan finnas behov av kamera, positionering, lokal cache eller offlinearbete.

Förmågan ska hjälpa till att avgöra om responsiv webb är tillräcklig eller om en särskild mobil lösning är motiverad. Infrastruktur, device management och bakomliggande synkronisering hanteras i samverkan med andra förmågor.

#### Sammanhållen informationsvy

En användare behöver se information från flera bakomliggande system i en gemensam vy. Det kan finnas behov av ett Backend for Frontend eller annat kanalnära API-lager för att undvika att klienten blir hårt kopplad till interna tjänster.

### 2.3 Centrala arkitekturfrågor

Vid framtagande av ett gränssnitt bör utvecklingsområdet bland annat ta ställning till:

1. **Vilka användare och användningssituationer ska stödjas?**  
   Intern eller extern användare, stationär eller mobil, frekvent eller sporadisk användning, särskilda tillgänglighetsbehov och eventuell användning i operativ miljö.

2. **Vilken kanal är mest ändamålsenlig?**  
   Responsiv webb, native mobil, portal, produktplattform eller annan kanal bör väljas utifrån behov och inte utifrån lokala teknikpreferenser.

3. **Hur rik behöver klienten vara?**  
   Ett enkelt informations- eller formulärflöde behöver inte nödvändigtvis en omfattande SPA-arkitektur. Ett komplext interaktivt arbetsstöd kan däremot motivera det.

4. **Vilken information får hanteras i klienten?**  
   Informationsskydd och integritet påverkar lokal cache, webbläsarlagring, export, utskrift, notifieringar och felmeddelanden.

5. **Var ska verksamhetslogik ligga?**  
   Kritisk verksamhetslogik och auktoritativ validering ska inte vara beroende av klienten.

6. **Hur kopplas klienten till backend?**  
   Direkt mot ett ändamålsenligt API, via Backend for Frontend eller via en produktplattform. Valet ska minimera onödig koppling och exponering av interna tjänster.

7. **Vilka gemensamma komponenter kan återanvändas?**  
   Design system, formulär, autentiseringsintegration, notifiering och andra gemensamma byggstenar bör utvärderas innan lokala lösningar skapas.

8. **Hur ska gränssnittet livscykelhanteras?**  
   Frontendramverk, beroenden, browser support och komponentbibliotek behöver kunna uppgraderas över tid.

---

## 3. Förmågespecifika arkitekturprinciper

Gemensamma arkitekturprinciper finns i `../styrning/gemensamma-arkitekturprinciper.md`. Nedanstående principer är specifika för denna förmåga.

### P-IPK-01 Användarbehov styr kanal och interaktion

**Princip:**  
Kanal, interaktionsmönster och presentationsform ska väljas utifrån identifierade användargrupper, arbetsuppgifter och användningssituationer.

**Motivering:**  
Samma tekniska kanal är inte optimal för alla behov. Operativt mobilt arbete, intern handläggning och publik självservice kan kräva olika egenskaper.

**Konsekvens:**  
Ett utvecklingsområde ska kunna motivera kanalval utifrån behov. Befintlig teknik eller organisatorisk hemvist ska inte ensamt styra valet.

### P-IPK-02 Gemensam användarupplevelse genom återanvändning

**Princip:**  
Gemensamt design system, komponenter och etablerade interaktionsmönster ska användas när de uppfyller behovet.

**Motivering:**  
Återanvändning ger en mer enhetlig användarupplevelse, minskar dubbel utveckling och koncentrerar tillgänglighets- och kvalitetsarbete.

**Konsekvens:**  
Lokala UI-komponenter bör skapas först när det finns ett dokumenterat behov som det gemensamma erbjudandet inte kan möta.

### P-IPK-03 Presentation separeras från verksamhetslogik

**Princip:**  
Presentation och kanalnära logik ska så långt som möjligt hållas separerade från auktoritativ verksamhetslogik och informationshantering.

**Motivering:**  
Separation möjliggör flera kanaler, enklare teknikbyten, konsekvent validering och minskad risk att verksamhetsregler bara finns i en viss klient.

**Konsekvens:**  
Kritiska regler och auktorisation ska verifieras på tjänste-/serversidan även om klienten ger tidig återkoppling till användaren.

### P-IPK-04 Tillgänglighet och användbarhet byggs in från början

**Princip:**  
Digital tillgänglighet och användbarhet ska behandlas som grundläggande kvaliteter under hela utvecklingslivscykeln.

**Motivering:**  
Tillgänglighet kan inte effektivt kvalitetssäkras enbart genom kontroll i slutet av utvecklingen. Arkitektur, komponentval och interaktionsdesign påverkar resultatet tidigt.

**Konsekvens:**  
Gemensamma komponenter, utvecklingsprocess och test behöver stödja tillgänglighet kontinuerligt.

### P-IPK-05 Minsta nödvändiga klientkomplexitet

**Princip:**  
Klientarkitekturen bör inte vara mer komplex än vad användningsfallet kräver.

**Motivering:**  
Omfattande frontendramverk och distribuerade klient/backend-arkitekturer medför kostnader för bygg, säkerhet, test, prestanda och livscykel.

**Konsekvens:**  
Serverrenderad webb, en produktplattforms inbyggda UI eller andra enklare alternativ kan vara bättre än en SPA när behovet är begränsat.

### P-IPK-06 Kanalnära säkerhet är del av lösningen

**Princip:**  
Säkerhetsmekanismer och informationsskydd i gränssnitt ska utformas proportionerligt utifrån användare, information och risk.

**Motivering:**  
Alla gränssnitt har inte samma skyddsbehov. Samtidigt kan felaktig lokal lagring, export eller notifiering exponera information även om backend är korrekt skyddad.

**Konsekvens:**  
Informationsklassning och riskbedömning ska påverka exempelvis sessioner, cache, webbläsarlagring, export och notifieringsinnehåll.

### P-IPK-07 Teknikval ska vara utbytbara över tid

**Princip:**  
Frontendramverk och andra klienttekniker ska användas så att verksamhetslogik och integrationskontrakt inte i onödan låses till en viss implementation.

**Motivering:**  
Frontendteknik har ofta kortare livscykel än verksamhetsstödet.

**Konsekvens:**  
Tekniska ramverk ska behandlas som realiseringar av förmågan och livscykelhanteras separat från stabila verksamhets- och arkitekturkontrakt.

---

## 4. Krav och styrande riktlinjer

Nedanstående krav är ett myndighetsnära förslag och behöver vid faktisk användning beslutas och spåras till myndighetens egna styrande källor.

### KR-IPK-01 Gemensamt design system

**Krav:**  
Nya egenutvecklade webbgränssnitt ska använda myndighetens gemensamma design system för de komponenter och interaktionsmönster som design systemet stödjer, om inte ett dokumenterat behov motiverar annat.

**Motivering/källa:**  
Enhetlighet, återanvändning, tillgänglighet och effektiv förvaltning.

**Tillämpningsområde:**  
Egenutvecklade interna och externa webbgränssnitt.

**Kommentar:**  
Kravet innebär inte att varje lösning måste ha identisk visuell utformning om målgrupp och användningssituation kräver variation.

### KR-IPK-02 Tillgänglighet ska verifieras under utvecklingen

**Krav:**  
Digitala gränssnitt ska utvecklas och verifieras mot myndighetens beslutade krav på digital tillgänglighet. Automatiserade kontroller ska vid behov kompletteras med manuella kontroller och användningsnära test.

**Motivering/källa:**  
Regelefterlevnad, användbarhet och myndighetens ansvar att erbjuda fungerande digitala tjänster för olika användare.

**Tillämpningsområde:**  
Publika och interna gränssnitt i den omfattning beslutade krav gäller.

### KR-IPK-03 Auktoritativ validering på tjänstesidan

**Krav:**  
Verksamhetskritiska regler, behörighetskontroller och auktoritativ validering ska genomföras i betrodda backend- eller tjänstekomponenter och får inte enbart finnas i klienten.

**Motivering/källa:**  
Säkerhet, dataintegritet och möjlighet att stödja flera kanaler.

**Tillämpningsområde:**  
Klient/server-baserade lösningar.

### KR-IPK-04 Inga direkta databasanslutningar från användarklient

**Krav:**  
Webb- och mobilklienter ska inte ansluta direkt till verksamhetsdatabaser. Åtkomst ska ske via definierade tjänstegränssnitt eller andra godkända backendkomponenter.

**Motivering/källa:**  
Säkerhet, lös koppling, förvaltningsbarhet och kontroll av verksamhetsregler.

**Tillämpningsområde:**  
Egenutvecklade webb- och mobilklienter.

### KR-IPK-05 Secrets får inte distribueras till klienten

**Krav:**  
Hemligheter som privata nycklar, lösenord eller andra credentials som ger utökad åtkomst ska inte byggas in i eller distribueras med klientkod.

**Motivering/källa:**  
Klientkod och klientmiljö kan inte betraktas som en betrodd lagringsplats för serverhemligheter.

**Tillämpningsområde:**  
Webb-, mobil- och desktopklienter.

### KR-IPK-06 Hantering av känslig information i klienten

**Krav:**  
Lokal lagring, cache, export, utskrift, urklipp och notifiering av skyddsvärd information ska styras av lösningens informations- och säkerhetskrav.

**Motivering/källa:**  
Informationsskydd och minimering av oavsiktlig exponering.

**Tillämpningsområde:**  
Gränssnitt som hanterar information med särskilda skyddsbehov.

### KR-IPK-07 Stödda klientmiljöer ska vara definierade

**Krav:**  
Varje användargränssnitt ska ha en definierad och förvaltad målbild för stödda webbläsare, operativsystem, enhetstyper eller motsvarande klientmiljöer.

**Motivering/källa:**  
Testbarhet, supportbarhet och livscykelhantering.

**Tillämpningsområde:**  
Alla digitala klientgränssnitt.

### KR-IPK-08 Tredjepartsberoenden ska livscykelhanteras

**Krav:**  
Frontendramverk, bibliotek och andra tredjepartsberoenden ska omfattas av myndighetens processer för dependency management, licenshantering, sårbarhetshantering och livscykel.

**Motivering/källa:**  
Säkerhet och långsiktig förvaltningsbarhet.

**Tillämpningsområde:**  
Egenutvecklade klienter med externa beroenden.

### KR-IPK-09 Klientfel ska kunna felsökas utan att känsliga data exponeras

**Krav:**  
Klientapplikationer ska utformas så att relevanta tekniska fel kan korreleras och felsökas utan att känsliga uppgifter eller onödiga personuppgifter loggas eller visas för användaren.

**Motivering/källa:**  
Driftbarhet och informationsskydd.

**Tillämpningsområde:**  
Interaktiva klientapplikationer där teknisk felsökning krävs.

### KR-IPK-10 Responsivitet eller motiverad kanalavgränsning

**Krav:**  
Webbgränssnitt ska utformas för de skärmstorlekar och enhetstyper som följer av målgruppens faktiska användningssituation. Om ett gränssnitt avsiktligt begränsas till viss klienttyp ska detta vara ett medvetet och dokumenterat arkitekturval.

**Motivering/källa:**  
Användbarhet och kostnadseffektiv kanaldesign.

**Tillämpningsområde:**  
Webbaserade gränssnitt.

---

## 5. Guidelines och vägledning

### 5.1 När bör Angular användas?

Angular är ett naturligt standardkandidat för större, långlivade egenutvecklade webbapplikationer när myndigheten vill koncentrera kompetens, komponentåteranvändning, säkerhetsarbete och livscykelhantering kring ett gemensamt ramverk.

Angular bör särskilt övervägas när lösningen har:

- ett relativt rikt och interaktivt användargränssnitt
- flera vyer och komplex klientnavigation
- behov av standardiserad frontendarkitektur
- behov av gemensamt komponentbibliotek
- en förväntad lång förvaltningsperiod
- flera utvecklingsteam som gynnas av gemensam kompetens

Angular behöver inte vara förstahandsval när:

- tjänsten huvudsakligen består av enkel informationspresentation eller ett litet formulärflöde
- den tekniska produktplattformen redan erbjuder ett ändamålsenligt och förvaltat gränssnitt
- en serverrenderad lösning ger lägre komplexitet och möter samtliga behov
- gränssnittet är en mindre, kortlivad eller specialiserad klient där ett annat beslutat alternativ är mer proportionerligt

Det separata standarddokumentet för Angular bör senare definiera stödda versioner, projektkonventioner och livscykel.

### 5.2 Responsiv webb eller särskild mobil applikation?

**Responsiv webb bör normalt vara förstahandsalternativ** när samma verksamhetsfunktion ska användas på flera enhetstyper och lösningen inte kräver omfattande offlinefunktion eller avancerad åtkomst till enhetens hårdvara.

En särskild mobilapplikation kan vara motiverad när:

- arbetet huvudsakligen utförs i fält
- offlinearbete är centralt
- kamera, positionering, sensorer eller annan enhetsfunktion är väsentlig
- mycket snabb och specialiserad mobil interaktion krävs
- bakgrundssynkronisering eller pushfunktioner är centrala
- säkerhetskrav kräver särskild device integration

Beslutet bör väga samman användbarhet, säkerhet, device management, releaseprocess, kompetens och förvaltningskostnad.

### 5.3 SPA, serverrenderad webb eller produktplattform?

Ett rikt interaktivt arbetsstöd kan lämpa sig väl för SPA-arkitektur. En enklare publik tjänst kan ofta realiseras med serverrenderad webb med lägre klientkomplexitet. Om verksamhetsstödet byggs i en etablerad produktivitets- eller verksamhetsplattform kan dess inbyggda UI-funktioner vara rätt val.

Valet ska baseras på behov och livscykel, inte på att ett visst frontendramverk är standard för alla situationer.

### 5.4 När är Backend for Frontend lämpligt?

Ett Backend for Frontend (BFF) kan vara lämpligt när klienten behöver:

- sammanställa information från flera tjänster
- få ett kontrakt särskilt anpassat till kanalen
- minska antalet nätverksanrop
- isoleras från förändringar i interna tjänstegränssnitt
- hantera kanalnära sessions- eller tokenflöden på serversidan
- undvika att interna API:er exponeras direkt till externa klienter

BFF bör inte införas slentrianmässigt om befintliga API:er redan ger ett lämpligt kontrakt. Varje ytterligare tjänstelager medför egen drift, test och livscykel.

### 5.5 När bör en ny gemensam UI-komponent skapas?

En ny gemensam komponent bör övervägas när:

1. behovet återkommer eller sannolikt kommer att återkomma
2. befintligt design system inte möter behovet
3. komponenten kan göras generell utan att bädda in ett enskilt systems verksamhetslogik
4. accessibility, säkerhet och användbarhet kan kvalitetssäkras
5. någon kan ta långsiktigt förvaltningsansvar

Ett teams lokala behov är inte automatiskt ett skäl att utöka det gemensamma design systemet.

### 5.6 Klientnära tillstånd och lokal lagring

Tillstånd bör endast lagras i klienten när det finns ett tydligt användnings- eller prestandabehov. Lokal lagring ska inte användas som ersättning för auktoritativ informationshantering.

För varje typ av lokalt tillstånd bör teamet bedöma:

- informationskänslighet
- livslängd
- risk vid delad eller förlorad enhet
- behov av kryptering
- konsekvens vid föråldrad data
- möjlighet till central radering eller sessionsavslut

### 5.7 Notifieringar och kanalval

Notifieringskanal bör väljas efter tidskritikalitet, informationskänslighet, mottagarens situation och behov av kvittens.

E-post och SMS kan vara lämpliga för att uppmärksamma användaren på att något har hänt men bör inte automatiskt bära hela det skyddsvärda innehållet. För känsligare information kan notifieringen i stället hänvisa användaren till en autentiserad kanal.

### 5.8 När standardlösningen inte passar

Om ett utvecklingsområde bedömer att standardiserat ramverk, design system eller kanalstrategi inte möter behovet bör följande dokumenteras:

1. vilket behov som inte kan uppfyllas
2. relevanta kvalitetskrav
3. vilka standardalternativ som har utvärderats
4. konsekvenser av alternativ lösning
5. påverkan på kompetens, förvaltning, säkerhet och livscykel

Detta underlag används i myndighetens gemensamma process för arkitekturbeslut eller avsteg. Enskilda avstegsbeslut lagras inte i detta förmågedokument.

---

## 6. Plattformar och tjänsteerbjudanden

Detta avsnitt beskriver identifierade **erbjudandekandidater**. Detaljerade plattformsdokument skapas separat när plattformskatalogen utvecklas.

| Erbjudande | Syfte | Lämpligt för | Status i detta steg |
|---|---|---|---|
| Web Application Framework | Standardiserat stöd för utveckling av större webbklienter | Egenutvecklade interaktiva webbgränssnitt | Kandidat |
| Design System | Gemensamma visuella och interaktiva komponenter | Interna och externa digitala gränssnitt | Kandidat |
| Formulärstöd | Gemensamma komponenter och mönster för datainmatning | E-tjänster och verksamhetsstöd med formulär | Kandidat |
| Notifieringstjänst | Gemensam kanaloberoende notifiering | IT-stöd som behöver e-post, SMS, push eller in-app-notiser | Kandidat |
| Mobil kanal / mobilutvecklingsstöd | Gemensamma principer och eventuellt plattformsstöd för mobil användning | Operativa eller andra mobilcentrerade lösningar | Behov ska verifieras |

### 6.1 Web Application Framework

Erbjudandet bör abstrahera gemensamma beslut kring frontendramverk, projektstruktur, design system-integration, test, säkerhetskontroller och livscykel.

**Nuvarande identifierad teknisk realisering:** Angular.

Ett utvecklingsområde bör i första hand kunna välja det konsumentnära erbjudandet *Web Application Framework*. Detaljer om exakt Angular-version, byggverktyg och konfiguration ska ligga i standard- och teknisk dokumentation.

### 6.2 Design System

Ett gemensamt Design System bör erbjuda återanvändbara komponenter, visuella regler och interaktionsmönster som kvalitetssäkrats för myndighetens behov.

Det bör bland annat kunna omfatta:

- typografi och visuella tokens
- knappar och länkar
- formulärkomponenter
- navigation
- tabeller och informationspresentation
- dialoger
- status-, varnings- och felpresentation
- tillgänglighetsanpassade interaktionsmönster

Design systemet bör ha en egen livscykel och förvaltning och inte vara hårt bundet till ett enskilt verksamhetssystem.

### 6.3 Formulärstöd

Formulärstöd kan vara en del av design systemet eller ett separat erbjudande beroende på ambitionsnivå. Syftet är att standardisera återkommande funktioner som fältkomponenter, klientnära valideringsåterkoppling, felpresentation och tillgänglig interaktion.

Auktoritativ verksamhetsvalidering ska fortfarande ligga på tjänstesidan.

### 6.4 Notifieringstjänst

En gemensam notifieringstjänst kan abstrahera kanalval och teknisk anslutning till exempelvis e-post, SMS, push eller meddelande inne i en autentiserad tjänst.

Tjänsten bör ha ett tydligt kontrakt för vilka typer av information som får skickas i respektive kanal och hur leveransstatus hanteras.

### 6.5 Mobil kanal / mobilutvecklingsstöd

Innan en separat mobilplattform etableras bör återkommande myndighetsbehov verifieras. Ett gemensamt erbjudande kan i ett första skede bestå av riktlinjer, säkerhetsmönster, device integration och distributionsstöd snarare än ett specifikt utvecklingsramverk.

---

## 7. Standarder och teknikval

Detta avsnitt anger identifierade standardkandidater. Detaljerade standarddokument skapas separat i senare steg eller när behov uppstår.

| Standard/teknikval | Föreslagen roll | Tillämpning | Status |
|---|---|---|---|
| Angular | Standardramverk | Större egenutvecklade webbklienter | Identifierad kandidat |
| TypeScript | Språkstandard | Klientkod i Angular-baserade lösningar | Identifierad kandidat |
| HTML/CSS och öppna webbstandarder | Grundstandard | Webbaserade gränssnitt | Identifierad kandidat |
| Myndighetens Design System | UI-standard | Gemensamma komponenter och interaktionsmönster | Behöver etableras/beskrivas |
| Browser support policy | Livscykelstandard | Stödda webbläsare och klientmiljöer | Behöver beskrivas |
| Frontend security baseline | Säkerhetsstandard | Headers, klientnära säkerhetsregler, dependencykrav | Behöver beskrivas |

### Angular

Angular bör i detta förslag behandlas som ett **teknikval inom Web Application Framework**, inte som själva förmågan. Standarddokumentet bör senare beskriva exempelvis:

- när standarden gäller
- stödda huvudversioner och uppgraderingsprincip
- rekommenderad projektstruktur
- integration med design system
- test- och kvalitetskrav
- dependency management
- hur avsteg hanteras

### Öppna webbstandarder

Lösningar bör använda standardiserade webbfunktioner där sådana finns och undvika onödiga webbläsarspecifika beroenden. Semantisk HTML och standardiserade webb-API:er bidrar till tillgänglighet, interoperabilitet och livscykelbarhet.

### Browser support policy

Stödda klientmiljöer bör hanteras som en gemensam livscykelstandard snarare än beslutas individuellt i varje applikation. Enskilda lösningar kan behöva avvika utifrån målgrupp, men avvikelsen ska vara medveten.

---

## 8. Relaterade artefakter och kvalitetsdimensioner

### 8.1 Relevanta kvalitetsdimensioner

Följande dimensioner från `../styrning/krav-och-kvalitetsdimensioner.md` är särskilt viktiga för förmågan.

#### Säkerhet och informationsskydd

Påverkar bland annat sessioner, lokal lagring, export, felmeddelanden, tredjepartsberoenden, klient/server-gränssnitt och notifieringar.

#### Tillgänglighet

Publika och interna kritiska gränssnitt kan behöva olika tillgänglighetsmål. Klientarkitektur, CDN/cache, backendberoenden och deployment påverkar den upplevda tillgängligheten.

#### Prestanda

Särskilt relevant för initial laddningstid, interaktion, nätverksanrop och stora informationsmängder. Optimering ska utgå från användningsbehov snarare än generella tekniska antaganden.

#### Skalbarhet och kapacitet

Publika tjänster eller gemensamma gränssnitt kan behöva hantera stora eller varierande användarvolymer. Skalbarhetsbehovet påverkar både frontendleverans och bakomliggande tjänster.

#### Spårbarhet och verifierbarhet

Klientfel och kritiska användarflöden kan behöva kunna korreleras med backendhändelser. Detta ska göras utan onödig insamling av känslig användardata.

#### Regelefterlevnad

Påverkar bland annat digital tillgänglighet, personuppgiftshantering och informationsskydd. Förmågespecifika krav ska vid produktionssättning kunna spåras till myndighetens beslutade styrande källor.

#### Tillgänglighet och användbarhet för användare

Är en kärndimension för förmågan och påverkar design, komponenter, navigation, text, formulär och test.

#### Förvaltningsbarhet och förändringsbarhet

Frontendramverk och komponentbibliotek förändras snabbt. Enhetlig teknik och separerad verksamhetslogik minskar kostnaden för uppgradering och förändring.

#### Interoperabilitet och portabilitet

Öppna webbstandarder och tydliga API-kontrakt minskar onödigt beroende av en viss klientteknik.

#### Livscykel och hållbarhet

Ramverk, browsersupport och tredjepartsbibliotek behöver aktiv versions- och avvecklingshantering.

#### Kostnads- och resurseffektivitet

Gemensamma ramverk och komponenter ska minska dubblering, men standardisering får inte skapa oproportionerlig komplexitet för enkla behov.

### 8.2 Identifierade lösningsmönster

Följande kandidater bör föras vidare till den gemensamma mönsterkatalogen:

1. **Backend for Frontend** – kanalnära backend som anpassar och aggregerar bakomliggande tjänster.
2. **Single Page Application med backend-API** – för rika interaktiva webbklienter.
3. **Serverrenderad webbapplikation** – för enklare eller innehålls-/formulärorienterade tjänster.
4. **Mobil klient med offline/synkronisering** – för operativ användning med varierande konnektivitet.
5. **Gemensamt formulärmönster** – återanvändbara principer för formulär, valideringsåterkoppling och felpresentation.
6. **Kanaloberoende notifiering** – separerar verksamhetshändelse från val av notifieringskanal.

Mönstren ska inte färdigställas inom denna förmåga eftersom flera av dem berör integration, identitet, data och runtime.

### 8.3 Identifierade plattformar och tjänster

- Web Application Framework
- Design System
- Formulärstöd
- Notifieringstjänst
- eventuell Mobil kanal / mobilutvecklingsstöd

### 8.4 Identifierade tekniska standarder

- Angular
- TypeScript
- öppna webbstandarder
- Browser support policy
- Frontend security baseline
- Design System-standard

### 8.5 Kandidater till referensarkitekturer

Följande tvärgående referensarkitekturer har identifierats men bör tas fram först när fler förmågor är genomarbetade:

- **Internt handläggningsstöd** – interaktion, process/ärende, regler, data, identitet, integration, runtime och driftbarhet.
- **Publik e-tjänst** – interaktion, identitet, integration, data, säkerhet, runtime och driftbarhet.
- **Mobil operativ lösning** – interaktion, kommunikation, identitet, data/synkronisering, runtime och driftbarhet.

### 8.6 Teknisk dokumentation

Detaljerad dokumentation bör senare länkas för exempelvis:

- Angular-projektstruktur och kodkonventioner
- användning av Design System-komponenter
- integration mot autentisering
- frontend observability
- CI/CD för frontendprojekt
- lokal utvecklingsmiljö
- säkerhetskonfiguration för webbklienter

Denna dokumentation ska ligga utanför förmågedokumentet eftersom den förändras snabbare än arkitekturens behovs- och styrningsnivå.

---

## Arbetsanteckningar inför kommande steg

### Identifierade kandidater

**Lösningsmönster**
- Backend for Frontend
- Single Page Application med backend-API
- serverrenderad webbapplikation
- mobil klient med offline/synkronisering
- gemensamt formulärmönster
- kanaloberoende notifiering

**Plattformar/tjänster**
- Web Application Framework
- Design System
- Formulärstöd
- Notifieringstjänst
- eventuell Mobil kanal / mobilutvecklingsstöd

**Tekniska standarder**
- Angular
- TypeScript
- öppna webbstandarder
- Browser support policy
- Frontend security baseline
- Design System-standard

**Referensarkitekturer**
- internt handläggningsstöd
- publik e-tjänst
- mobil operativ lösning

**Gränsdragningsfrågor att återbesöka**
- var gemensam notifiering primärt ska höra hemma: Interaktion eller Integration
- om formulärstöd ska vara en del av Design System eller ett separat tjänsteerbjudande
- hur mobil utveckling ska delas mellan Interaktion, Arbetsplats och Programvaruutveckling
- hur AI-baserade konversationsgränssnitt ska delas mellan Interaktion och Analys/sökning/AI
- hur en eventuell portalplattform ska klassificeras om den både erbjuder UI, identitet, innehåll och workflow
