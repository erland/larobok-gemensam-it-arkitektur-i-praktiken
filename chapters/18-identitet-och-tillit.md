# 18. Identitet och tillit

När en människa loggar in i ett verksamhetsstöd, när en backend-tjänst anropar ett API eller när två organisationer utbyter information behöver systemen kunna avgöra vem eller vad som finns på andra sidan. Det räcker inte att kommunikationen tekniskt når fram. Det måste också finnas en grund för tillit.

Det gör identitet till en arkitekturfråga.

En lokal användartabell kan verka enkel i ett enskilt system. Ett statiskt lösenord mellan två tjänster kan verka pragmatiskt. Ett certifikat kan installeras manuellt och fungera i flera år. Men när organisationen får hundratals lösningar uppstår frågor om livscykel, spårbarhet, behörigheter, federation, credential-rotation, incidenter och avveckling. Identiteter och tillitsrelationer blir då en gemensam infrastruktur som behöver vara lika genomtänkt som integration, runtime och datahantering.

Kärnfrågan i kapitlet är:

> **Hur etablerar och förvaltar vi tillit mellan människor, tjänster och organisationer utan att varje lösning bygger sin egen identitetsvärld?**

Kapitlet behandlar den gemensamma IT-förmågan **Identitet och tillit**. Fokus ligger på identiteter, autentisering, federation, tjänsteidentiteter, auktorisationsunderlag, PKI, certifikat och secrets. Säkerhet i vidare mening är däremot tvärgående. Hotmodellering, nätsegmentering, säker kodning, sårbarhetshantering och informationsskydd kan inte reduceras till identitetsförmågan.

## Identitet är mer än ett användarnamn

I vardagligt språk används identitet ofta som synonym till ett användarkonto. Arkitektoniskt behöver begreppet vara bredare.

En digital identitet är en representation av ett **subjekt** eller en **aktör** som behöver kunna kännas igen i ett digitalt sammanhang. Det kan exempelvis vara:

- en anställd,
- en extern användare,
- en organisation,
- en applikation,
- en backend-tjänst,
- en workload i en runtimeplattform,
- en CI/CD-pipeline,
- en administratör med särskilt privilegierad åtkomst.

Identiteten behöver inte innehålla all information om aktören. Den behöver innehålla eller kunna kopplas till tillräckliga uppgifter för det aktuella behovet.

Det är därför viktigt att skilja mellan:

- **identitet** – vem eller vad aktören representerar,
- **konto** – en teknisk representation i ett visst system eller en viss identitetsdomän,
- **credential** – något som används för att bevisa eller stödja ett påstående om identiteten,
- **attribut** – egenskaper som kan beskriva identiteten,
- **session eller token** – en tidsbegränsad representation som kan användas efter en autentiserings- eller auktorisationsprocess.

Om dessa blandas ihop blir livscykeln snabbt svår att förstå. En person kan exempelvis ha en stabil organisatorisk identitet men flera konton, autentiseringsmetoder och aktiva sessioner. En tjänst kan ha en logisk identitet men få kortlivade credentials dynamiskt i varje körmiljö.

## Autentisering och auktorisation är olika frågor

En av de viktigaste distinktionerna i identitetsarkitekturen är skillnaden mellan autentisering och auktorisation.

Autentisering svarar i princip på:

> **Vem eller vad är aktören?**

Auktorisation svarar på:

> **Vad får den autentiserade aktören göra i detta sammanhang?**

Skillnaden är enkel att formulera men viktig i designen.

En central identitetstjänst kan exempelvis fastställa att användaren är en viss person och leverera verifierade attribut. Det betyder inte att den centrala tjänsten måste känna till om personen får fatta ett visst verksamhetsbeslut i ett visst ärende.

Det senare kan bero på:

- organisatorisk roll,
- delegering,
- ärendets status,
- informationsklass,
- relation till den berörda parten,
- separation of duties,
- särskilda verksamhetsregler.

En arkitektur där autentisering och all verksamhetsauktorisation pressas in i samma centrala identitetsprodukt riskerar därför att göra identitetsplattformen till en ny central monolit.

En bättre separation är ofta:

```text
Gemensam identitetstjänst
        │
        │ autentiserar och lämnar verifierade attribut
        ▼
Lösning eller domän
        │
        │ tillämpar behörighets- och verksamhetsregler
        ▼
Tillåten eller nekad åtgärd
```

Det betyder inte att auktorisation alltid måste vara lokal. Gemensamma policykomponenter, rollmodeller eller attributtjänster kan vara motiverade. Men ansvaret bör placeras där beslutets betydelse kan förstås.

## Tillit är en relation – inte en produkt

En identitetsplattform skapar inte automatiskt tillit.

Tillit uppstår när en part accepterar att en annan part kan göra vissa påståenden eller utföra vissa handlingar inom ett definierat sammanhang.

Exempel:

- en applikation accepterar att organisationens identitetsleverantör autentiserar interna användare,
- en myndighet accepterar identitetsintyg från en extern identitetsleverantör,
- ett API accepterar en token utfärdad av en viss auktorisationsserver,
- en tjänst accepterar ett certifikat som kan härledas till en betrodd certifikatutfärdare,
- en runtimeplattform utfärdar en tjänsteidentitet till en workload som får anropa en annan tjänst.

Varje sådan relation behöver svar på frågor som:

- Vem får utfärda identiteten eller intyget?
- Vad betyder attributen?
- Hur länge gäller de?
- Hur återkallas eller avvecklas tilliten?
- Vilka säkerhetsnivåer förutsätts?
- Hur hanteras incidenter?
- Vem ansvarar för att relationen fortfarande är korrekt?

Därför bör tillit dokumenteras som en **avsiktlig relation med ägare och livscykel**, inte som ett historiskt tekniskt undantag som råkar fungera.

## Människors identiteter och workforce identity

I större organisationer finns normalt ett behov av en gemensam identitetsdomän för den egna arbetsstyrkan. Det omfattar exempelvis anställda, konsulter och andra personer som arbetar inom organisationens miljö.

En sådan workforce identity-förmåga kan ge stöd för:

- central autentisering,
- single sign-on,
- flerfaktorsautentisering,
- livscykel för konton,
- koppling till organisatoriska attribut,
- federation till interna och externa tjänster,
- policy för autentiseringsstyrka,
- återställning och spärrning.

Den stora nyttan är inte bara användarvänlighet. Den är att organisationen kan knyta identitetens livscykel till auktoritativa källor och gemensamma kontrollmekanismer.

Om varje system i stället skapar egna lokala användarkonton uppstår flera parallella problem:

- avslutade användare kan ligga kvar,
- namn och organisatorisk tillhörighet blir inkonsistenta,
- autentiseringsstyrkan varierar,
- samma användare får flera credentials,
- incidenthantering måste göras i många system,
- revision och spårbarhet blir svårare.

Principen **gemensam identitet före lokal identitet** är därför ofta en bra utgångspunkt när det gemensamma erbjudandet faktiskt stödjer målgruppen och kvalitetskraven.

Det innebär inte att alla applikationer saknar lokal användarrepresentation. Ett system kan behöva lagra domänspecifika inställningar eller interna identifierare. Men den lokala representationen bör då kopplas till en gemensamt förvaltad identitet i stället för att bli en ny fristående autentiseringsvärld.

## Identitetens livscykel

Identitetsarkitektur handlar lika mycket om avveckling som om inloggning.

En mänsklig identitet kan genomgå händelser som:

```text
Anställning → organisatoriskt byte → ändrat uppdrag → ledighet → avslut
```

Varje händelse kan påverka:

- vilka konton som ska finnas,
- vilka grupper och roller som gäller,
- vilka system som får nås,
- vilka privilegier som ska tas bort,
- vilka sessions- eller autentiseringsmekanismer som behöver spärras.

En identitetsplattform kan automatisera mycket av detta, men endast om den kan lita på bra källinformation och om ansvarsfördelningen är tydlig.

Det är därför viktigt att skilja mellan:

- **auktoritativ person- och organisationsinformation**, exempelvis från HR- eller organisationssystem,
- **identitetslivscykel**, som omsätter informationen till digitala identiteter och konton,
- **behörighetslivscykel**, som avgör vilken åtkomst identiteten ska få i olika sammanhang.

Att en person arbetar på en viss organisatorisk enhet betyder inte automatiskt att personen ska få alla behörigheter som kan associeras med enheten.

## Autentiseringsstyrka ska följa risken

All autentisering behöver inte ha samma styrka.

En intern informationssida och en administrativ funktion med långtgående privilegier har olika konsekvens om fel person får åtkomst. Arkitekturen behöver därför utgå från risk och användningssituation snarare än från en enda universell inloggningsmekanism.

Faktorer kan vara:

- informationens känslighet,
- vilken åtgärd som kan utföras,
- om användaren är intern eller extern,
- vilken identitetssäkring som finns bakom identiteten,
- risk för nätfiske eller credential-stöld,
- konsekvensen av kontoövertagande,
- behov av starkare autentisering vid särskilt känsliga åtgärder.

Flerfaktorsautentisering är ett viktigt verktyg, men det löser inte alla identitetsproblem. En stark autentisering hjälper inte om användaren redan har felaktiga privilegier eller om en komprometterad tjänsteidentitet kan agera utan begränsning.

Det viktiga är därför kombinationen av:

- rätt identitet,
- lämplig autentiseringsstyrka,
- minsta nödvändiga privilegium,
- begränsad giltighet,
- spårbarhet,
- fungerande livscykel.

## Federation – låna identitet utan att kopiera den

När användare tillhör en annan identitetsdomän uppstår frågan om federation.

Utan federation kan den mottagande organisationen skapa ett lokalt konto för den externa personen. Det kan fungera i liten skala men skapar lätt dubbla livscykler.

Med federation kan den mottagande tjänsten i stället lita på att en extern identitetsleverantör autentiserar användaren och lämnar över ett definierat identitetsintyg eller motsvarande information.

Förenklat:

```text
Användare
   │
   ▼
Extern identitetsleverantör
   │  autentiserar
   │  lämnar verifierat intyg/claims
   ▼
Mottagande tjänst
```

Det centrala arkitekturproblemet är inte bara protokollet. Det är **trustmodellen**.

Man behöver förstå:

- vilka identitetsleverantörer som accepteras,
- hur parterna identifieras tekniskt,
- vilka attribut som får användas,
- hur attributens betydelse är definierad,
- vilken autentiserings- och identitetssäkring som ligger bakom,
- hur nycklar och metadata förvaltas,
- hur incidenter och avveckling hanteras.

Standardiserade federationsprotokoll gör interoperabilitet möjlig, men de ersätter inte denna överenskommelse.

För modern användarautentisering är OpenID Connect ett etablerat protokoll byggt ovanpå OAuth 2.0. OAuth används i sin tur för auktoriserad eller delegerad åtkomst till skyddade resurser. Det är viktigt att inte beskriva OAuth i sig som ett användarautentiseringsprotokoll. SAML kan fortfarande vara relevant i befintliga eller externa federationsmiljöer där det är den etablerade mekanismen.

Poängen för den gemensamma arkitekturen är inte att varje lösning ska välja protokoll fritt. Organisationen bör erbjuda och profilera ett begränsat antal godkända sätt att federera identitet, så att säkerhetskrav, metadata, tokenhantering och livscykel inte behöver uppfinnas på nytt.

## Claims och attribut är inte automatiskt sanning för alla ändamål

Ett identitetsintyg kan innehålla claims eller attribut om användaren, exempelvis namn, identifierare eller organisatorisk tillhörighet.

Det är frestande att använda alla sådana attribut direkt för behörighetsbeslut. Men ett attribut är bara användbart om man vet:

- vem som ansvarar för informationen,
- vad värdet betyder,
- hur aktuellt det är,
- i vilket syfte det får användas,
- om det kan förändras under en aktiv session,
- om mottagaren verkligen behöver informationen.

Det är därför bra att tänka på identitetsclaims ungefär som andra informationskontrakt i boken: de behöver semantik, ägare och livscykel.

Att en token tekniskt innehåller ett fält gör inte fältet till lämpligt underlag för ett kritiskt verksamhetsbeslut.

## Tjänster behöver egna identiteter

Människor är bara en del av identitetslandskapet.

Moderna system består av tjänster, workloads, integrationskomponenter, pipelines och automatiserade agenter som kommunicerar utan en människa i varje interaktion.

Ett vanligt anti-pattern är att sådana komponenter använder:

- en namngiven persons konto,
- ett delat servicekonto,
- ett statiskt lösenord som kopieras till flera miljöer,
- en API-nyckel som aldrig roteras.

Det gör ansvar, spårbarhet och avveckling svåra.

Ett bättre mönster är **tjänsteidentitet**:

```text
Tjänst A ── egen identitet ──▶ Tjänst B
```

Identiteten bör i möjligaste mån vara:

- unik för den relevanta tjänsten eller workloaden,
- kopplad till dess tekniska livscykel,
- begränsad till minsta nödvändiga privilegium,
- möjlig att spåra i loggar,
- försedd med kortlivade eller automatiskt roterade credentials där det är praktiskt möjligt.

Det skapar en viktig koppling till nästa kapitel om runtime. En modern runtimeplattform kan vara en central del av hur workload-identiteter utfärdas och distribueras utan att statiska hemligheter behöver byggas in i images eller konfiguration.

## Tjänsteidentitet och användardelegering är inte samma sak

En backend-tjänst kan agera i två principiellt olika roller.

### Tjänsten agerar i eget ansvar

Exempelvis hämtar en schemalagd komponent information för att uppdatera ett index.

Då bör tjänsten normalt använda sin **egen tjänsteidentitet**.

### Tjänsten agerar för en användares räkning

Exempelvis anropar en backend ett annat API för att slutföra den operation som användaren initierade.

Då kan den bakomliggande tjänsten behöva information om användarkontexten eller en kontrollerad form av delegerad åtkomst.

Det är farligt att blanda modellerna. Om en användartoken okritiskt skickas vidare genom många tjänster kan privilegier spridas längre än avsett. Om allt i stället görs med backendens tjänsteidentitet kan den bakomliggande användarkontexten försvinna.

Arkitekturen behöver därför uttryckligen avgöra **vem som agerar i vems ansvar**.

## PKI och certifikat – teknisk tillit med livscykel

Public Key Infrastructure, PKI, används för att knyta kryptografiska nycklar till identiteter genom certifikat och betrodda utfärdare.

I en organisation kan certifikat exempelvis användas för:

- serveridentitet i TLS,
- ömsesidig TLS där båda parter autentiseras,
- tjänste- eller klientidentitet,
- signerande av artefakter eller meddelanden,
- vissa externa tillitsrelationer.

Det viktiga arkitekturperspektivet är att certifikatet inte bara är en fil.

Det har en livscykel:

```text
Beställning → utfärdande → distribution → användning → förnyelse/rotation → avveckling
```

Om denna livscykel är manuell och otydlig uppstår välkända operativa problem: certifikat går ut oväntat, gamla certifikat ligger kvar, privata nycklar kopieras mellan miljöer och ingen vet vem som äger förnyelsen.

En gemensam PKI- och certifikattjänst bör därför inte bara utfärda certifikat. Den bör stödja kontrollerad identitet, ägarskap, automatisering, förnyelse och avveckling.

Ömsesidig TLS, mTLS, kan ge stark maskin-till-maskin-autentisering där båda parter presenterar certifikat. Men mTLS svarar fortfarande inte på alla auktorisationsfrågor. Att en tjänst är autentiserad betyder inte automatiskt att den får göra vilken operation som helst.

## Secrets är credentials – inte konfiguration

Lösenord, privata nycklar, API-nycklar och andra hemliga credentials behöver behandlas annorlunda än vanlig konfiguration.

Ett återkommande anti-pattern är att secrets hamnar i:

- källkod,
- Git-repositorier,
- container-images,
- generella konfigurationsfiler,
- dokumentation eller scripts,
- kopierade lokala miljöfiler.

Problemet är inte bara risken för läckage. Det blir också svårt att rotera hemligheten, veta vilka kopior som finns och avveckla åtkomst.

En gemensam secrets management-tjänst kan ge stöd för:

- skyddad lagring,
- kontrollerad åtkomst,
- audit,
- rotation,
- tidsbegränsad distribution,
- separation mellan miljöer.

Men den bästa långsiktiga lösningen är ofta att **minska mängden långlivade secrets**. Om en workload kan få en kortlivad identitet från sin runtimeplattform är det ofta bättre än att lägga ett statiskt lösenord i ett centralt valv och sedan distribuera det.

Secrets management och service identity är därför närliggande men olika förmågor: den ena skyddar hemliga credentials, den andra försöker göra identiteten och credential-livscykeln mer explicit och automatiserad.

## Privilegierad åtkomst är ett särskilt fall

Administrativa identiteter kan få åtkomst som vanliga användare aldrig bör ha. Det kan handla om:

- plattformsadministration,
- databasadministration,
- säkerhetsadministration,
- hantering av identitetsplattformen själv,
- åtkomst till produktionsmiljöer.

Här behöver organisationen ofta starkare kontroll än vid vanlig användaråtkomst.

Principer kan vara:

- separera vanlig användaridentitet från privilegierad funktion,
- använd stark autentisering,
- tillämpa minsta privilegium,
- begränsa åtkomsten i tid när det är möjligt,
- logga och följ upp privilegierade aktiviteter,
- undvik delade administratörskonton,
- ha en fungerande reservväg för nödsituationer utan att den blir normalvägen.

Privileged access management kan vara ett eget plattformserbjudande i en större organisation, även om det konceptuellt ligger nära identitetsförmågan.

## Minsta privilegium är en livscykelfråga

Principen om minsta privilegium uttrycks ofta som att en identitet bara ska ha den åtkomst som krävs.

Utmaningen är att behovet förändras.

En person byter roll. En tjänst får en ny funktion. Ett gammalt API avvecklas. Ett projekt avslutas. Ett tillfälligt administrativt behov försvinner.

Om organisationen bara kontrollerar privilegiet när åtkomsten skapas kommer rättigheterna att ackumuleras över tid.

Minsta privilegium kräver därför:

- tydligt ägarskap,
- regelbunden omprövning där risken motiverar det,
- automatisk avveckling när underlaget för åtkomsten försvinner,
- korta giltighetstider för särskilt känsliga credentials där det är möjligt,
- möjlighet att spåra varför åtkomsten beviljades.

Detta är ett exempel på hur identitet, governance och drift möts utan att bli samma förmåga.

## Tokens behöver förstås som tidsbegränsade säkerhetsobjekt

I federerade och API-baserade arkitekturer används ofta tokens för att bära information om en autentiserad eller auktoriserad kontext.

Det är lätt att betrakta en token som ett neutralt dataformat. Arkitektoniskt är den ett säkerhetsobjekt med egenskaper som:

- utfärdare,
- avsedd mottagare eller resurs,
- giltighetstid,
- scopes eller andra behörighetsuppgifter,
- claims,
- kryptografiskt skydd,
- regler för vidarebefordran och lagring.

En token bör därför inte automatiskt accepteras bara för att dess signatur är tekniskt korrekt. Mottagaren behöver även verifiera att token är av rätt typ, kommer från rätt utfärdare och är avsedd för rätt sammanhang.

Moderna OAuth-profiler och säkerhetsrekommendationer har utvecklats just för att minska riskerna med felaktig tokenhantering, osäkra flöden och alltför bred återanvändning. För en gemensam arkitektur talar det för att organisationen bör ha standardiserade profiler snarare än att varje applikation konfigurerar protokollen på egen hand.

## Identity proofing är en annan fråga än autentisering

Särskilt för externa användare behöver man skilja på två frågor:

1. Hur vet vi vilken verklig person eller organisation den digitala identiteten representerar?
2. Hur verifierar vi vid ett senare tillfälle att den som försöker logga in kontrollerar rätt autentiseringsmedel?

Den första frågan handlar om **identity proofing** eller identitetssäkring vid etableringen av identiteten. Den andra handlar om autentisering.

En tekniskt stark autentisering kan alltså inte kompensera för en svag eller felaktig ursprunglig identitetskoppling.

Detta är en viktig anledning till att identitetsarkitektur behöver beskriva assurance och trustmodell, inte bara protokoll.

Aktuella riktlinjer för digital identitet, exempelvis NIST SP 800-63-4, skiljer uttryckligen mellan identitetssäkring, autentisering och federation. Boken använder inte NIST:s nivåmodell som ett generellt krav för alla organisationer, men distinktionen är användbar även utanför det ramverket.

## Identitet och Zero Trust

Begreppet Zero Trust används ofta i identitetssammanhang. Den användbara kärnan är att åtkomst inte bör följa automatiskt av att en aktör befinner sig på ett visst nät eller innanför en traditionell perimeter.

Identitet, enhet, kontext, policy och den skyddade resursen behöver i stället ingå i åtkomstbeslutet.

Det betyder dock inte att identitetsplattformen ensam realiserar Zero Trust. Nätverk, enhetssäkerhet, policy enforcement, observerbarhet och informationsskydd behöver samverka.

För förmågemodellen är lärdomen därför främst:

> **Implicit tillit bör ersättas med explicita, verifierbara och förvaltade tillitsrelationer där konsekvensen motiverar det.**

Det ligger väl i linje med identitetsförmågan utan att göra den till synonym med hela säkerhetsarkitekturen.

## Gemensamma plattformstjänster

Identitet och tillit kan realiseras genom flera separata plattformserbjudanden.

### Workforce Identity

Stöd för interna användares identiteter, autentisering, SSO, MFA, federation och kontolivscykel.

### Service Identity

Stöd för tjänste- och workload-identiteter, maskin-till-maskin-autentisering och kortlivade credentials.

### PKI & Certificate Service

Stöd för certifikatutfärdande, trust anchors, förnyelse, rotation och avveckling.

### Secrets Management

Stöd för skyddad lagring och distribution av hemliga credentials när sådana fortfarande behövs.

I en större organisation kan även externa identiteter, privileged access och policybaserad auktorisation bli egna tjänsteerbjudanden.

Poängen är densamma som i tidigare förmågekapitel: förmågan är stabilare än den konkreta produktportföljen. Produkter, protokollprofiler och runtime-integrationer kan bytas utan att behovet av identitet och tillit försvinner.

## Standarder bör profilera – inte bara namnge protokoll

Det är inte tillräckligt att en standard säger:

> Använd OAuth.

OAuth är ett ramverk med olika roller, flöden, tokenmodeller och säkerhetsöverväganden. På motsvarande sätt behöver organisationen mer än orden OpenID Connect, SAML eller mTLS.

En användbar teknisk standard kan behöva ange:

- vilka protokoll och profiler som är godkända för vilka användningsfall,
- vilka flöden som får användas,
- hur klienter autentiseras,
- vilka tokenlivslängder och scopes som är rimliga,
- hur redirect-URI:er och metadata hanteras,
- hur nyckelrotation sker,
- hur tjänsteidentiteter provisioneras,
- när mTLS eller andra proof-of-possession-mekanismer krävs,
- vilka claims som är gemensamma och vad de betyder.

Standarden behöver samtidigt undvika att frysa dagens produktkonfiguration i arkitekturlagret. Exakta inställningar kan ligga i produkt- och konfigurationsstandarder med kortare livslängd.

## Ansvar på tre nivåer

Bokens tredelade ansvarmodell är särskilt användbar för identitet eftersom centralisering annars lätt går för långt.

### Gemensam arkitekturnivå

Här bör organisationen bland annat definiera:

- gemensamma identitets- och trustprinciper,
- vilka huvudtyper av identiteter som finns,
- övergripande krav på autentisering och credential-hantering,
- principer för federation,
- gemensamma protokollprofiler,
- krav på tjänsteidentiteter,
- förhållandet mellan identitet och audit,
- regler för särskilt privilegierad åtkomst.

### Förmågenivå

Ansvariga för Identitet och tillit bör bland annat utveckla:

- identitetsplattformar och tjänsteerbjudanden,
- integration med auktoritativa identitetskällor,
- federationstjänster,
- service identity,
- PKI och certifikatlivscykel,
- secrets management,
- standarder och golden paths,
- operativa processer för incidenter och avveckling,
- gemensamma attribut- och claimkontrakt där det finns nytta.

### Lösnings-/produktnivå

Den konkreta lösningen ansvarar fortfarande för frågor som:

- vilka användargrupper som faktiskt behöver åtkomst,
- vilka verksamhetsoperationer de får utföra,
- hur identitetsattribut används i domänens behörighetsmodell,
- vilka externa integrationsparter som behövs,
- vilka tjänsteidentiteter lösningen kräver,
- hur fel och identitetsrelaterade undantag hanteras i användarflödet.

Gemensam identitet tar alltså inte bort lösningens ansvar för sin egen auktorisationsmodell.

## Vanliga anti-patterns

### Lokal användardatabas som standardlösning

Varje applikation skapar egna användarnamn och lösenord trots att en gemensam identitetstjänst finns.

**Konsekvens:** parallella livscykler, svagare kontroll och högre förvaltningskostnad.

### Personligt konto som tjänstekonto

En teknisk integration använder en namngiven persons credentials.

**Konsekvens:** otydligt ansvar, bristande spårbarhet och problem när personen byter roll eller slutar.

### Delade servicekonton

Flera tjänster använder samma tekniska identitet.

**Konsekvens:** svårt att avgöra vilken komponent som gjorde vad och svårt att tillämpa minsta privilegium.

### Hemlighet i källkod

API-nycklar eller lösenord checkas in tillsammans med applikationen.

**Konsekvens:** svår rotation, okontrollerade kopior och risk för läckage.

### Eviga credentials

Nycklar eller certifikat skapas med lång livslängd och saknar automatisk rotation.

**Konsekvens:** större konsekvens vid kompromettering och hög operativ risk vid utgång.

### Central identitetsplattform som verksamhetsregelverk

Alla verksamhetsspecifika åtkomstbeslut pressas in i den centrala IAM-lösningen.

**Konsekvens:** identitetsplattformen får känna till domändetaljer och blir ett förändringshinder.

### Rollinflation

Varje ny kombination av rättigheter skapar en ny global roll.

**Konsekvens:** modellen blir svår att förstå, kombinera och förvalta.

### Implicit trust mellan interna tjänster

En tjänst får åtkomst bara för att den finns på ”rätt nät”.

**Konsekvens:** otydlig säkerhetsmodell och stor konsekvens när nätgränsen kringgås.

### Token som universellt identitetskort

Samma token skickas vidare mellan många resurser oavsett avsedd mottagare.

**Konsekvens:** bredare exponeringsyta och svagare separation mellan tillitsdomäner.

## En praktisk analysordning

När ett nytt identitets- eller tillitsbehov uppstår kan följande ordning användas.

### 1. Identifiera aktörerna

Är de människor, tjänster, workloads, organisationer eller administrativa identiteter?

### 2. Identifiera identitetsdomänen

Vem äger identiteten? Är den intern, extern eller teknisk?

### 3. Beskriv vad som behöver bevisas

Behöver vi veta personens identitet, tjänstens identitet, organisationstillhörighet eller bara att en viss klient är godkänd?

### 4. Bedöm assurance och konsekvens

Vilken risk uppstår om fel identitet accepteras eller rätt identitet får för stor åtkomst?

### 5. Separera autentisering från auktorisation

Vilken del kan göras gemensamt och vilken del kräver domänens egen kontext?

### 6. Identifiera federation eller trustrelationer

Vilka externa eller interna utfärdare behöver betros och på vilka villkor?

### 7. Välj identitets- och credentialmodell

Behövs workforce identity, service identity, certifikat, delegerad åtkomst eller annan mekanism?

### 8. Definiera livscykeln

Hur skapas, förändras, roteras, spärras och avvecklas identiteten och dess credentials?

### 9. Definiera spårbarheten

Kan relevanta handlingar kopplas till rätt mänsklig eller teknisk identitet?

### 10. Välj gemensam plattform och standardprofil

Först när behovet är tydligt väljs den konkreta mekanismen och dess konfiguration.

Denna ordning hjälper organisationen att undvika två ytterligheter: att varje system skapar en egen identitetslösning och att den centrala identitetsplattformen försöker äga alla verksamhetsbeslut.

## Tillit ska vara explicit, begränsad och möjlig att avveckla

En mogen identitetsarkitektur mäts inte i hur många system som är kopplade till samma katalog. Den mäts i hur väl organisationen kan förstå och förändra sina tillitsrelationer.

Bra identitetsarkitektur gör det möjligt att svara på frågor som:

- Vem eller vad är denna aktör?
- Vem står bakom påståendet?
- Vilken säkerhetsnivå ligger bakom?
- Vad får aktören göra här?
- Hur länge gäller tilliten?
- Hur kan den återkallas?
- Vem ansvarar för livscykeln?
- Kan vi i efterhand förstå vilken identitet som gjorde vad?

Det är först när dessa frågor kan besvaras som identitet går från att vara en inloggningsfunktion till att bli en verklig gemensam IT-förmåga.

I nästa kapitel flyttas fokus till den miljö där många av dessa identiteter faktiskt används: **hur applikationer och workloads exekveras standardiserat, isolerat och portabelt i en gemensam runtimeförmåga.**
