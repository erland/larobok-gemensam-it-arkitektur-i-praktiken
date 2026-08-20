# 18. Identitet och tillit

När en människa loggar in i ett verksamhetsstöd, när en backend-tjänst anropar ett API eller när två organisationer utbyter information behöver systemen kunna avgöra vem eller vad som finns på andra sidan. Det räcker inte att kommunikationen tekniskt når fram. Det måste också finnas en grund för tillit.

Det gör identitet till en arkitekturfråga.

En lokal användartabell kan verka enkel i ett enskilt system. Ett statiskt lösenord mellan två tjänster kan verka pragmatiskt. Ett certifikat kan installeras manuellt och fungera i flera år. Men när organisationen får hundratals lösningar uppstår frågor om livscykel, spårbarhet, behörigheter, federation, credential-rotation, incidenter och avveckling. Identiteter och tillitsrelationer blir då en gemensam infrastruktur som behöver vara lika genomtänkt som integration, runtime och datahantering.

Kärnfrågan i kapitlet är:

> Hur etablerar och förvaltar vi tillit mellan människor, tjänster och organisationer utan att varje lösning bygger sin egen identitetsvärld?

Kapitlet behandlar den gemensamma IT-förmågan *Identitet och tillit*. Fokus ligger på identiteter, autentisering, federation, tjänsteidentiteter, auktorisationsunderlag, PKI, certifikat och secrets. Säkerhet i vidare mening är däremot tvärgående. Hotmodellering, nätsegmentering, säker kodning, sårbarhetshantering och informationsskydd kan inte reduceras till identitetsförmågan.

## Identitet är mer än ett användarnamn

I vardagligt språk används identitet ofta som synonym till ett användarkonto. Arkitektoniskt behöver begreppet vara bredare.

En digital identitet är en representation av ett subjekt eller en aktör som behöver kunna kännas igen i ett digitalt sammanhang. Det kan exempelvis vara en anställd, extern användare, organisation, applikation, backend-tjänst, workload, CI/CD-pipeline eller administratör med särskilt privilegierad åtkomst.

Det är viktigt att skilja mellan:

- identitet – vem eller vad aktören representerar,
- konto – en teknisk representation i ett visst system eller en viss identitetsdomän,
- credential – något som används för att bevisa eller stödja ett påstående om identiteten,
- attribut – egenskaper som beskriver identiteten,
- session eller token – en tidsbegränsad representation som används efter autentisering eller auktorisation.

Om dessa blandas ihop blir livscykeln svår att förstå. En person kan ha en stabil organisatorisk identitet men flera konton och autentiseringsmetoder. En tjänst kan ha en logisk identitet men få kortlivade credentials dynamiskt i varje körmiljö.

## Autentisering och auktorisation är olika frågor

En av de viktigaste distinktionerna i identitetsarkitekturen är skillnaden mellan autentisering och auktorisation.

Autentisering svarar i princip på:

> Vem eller vad är aktören?

Auktorisation svarar på:

> Vad får den autentiserade aktören göra i detta sammanhang?

En central identitetstjänst kan fastställa att användaren är en viss person och leverera verifierade attribut. Det betyder inte att den centrala tjänsten måste känna till om personen får fatta ett visst verksamhetsbeslut i ett visst ärende. Det kan bero på organisatorisk roll, delegering, ärendets status, informationsklass, relation till berörd part eller andra verksamhetsregler.

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

En identitetsplattform skapar inte automatiskt tillit. Tillit uppstår när en part accepterar att en annan part kan göra vissa påståenden eller utföra vissa handlingar inom ett definierat sammanhang.

Exempel är att en applikation accepterar organisationens identitetsleverantör, ett API accepterar en token från en viss auktorisationsserver eller en tjänst accepterar ett certifikat som kan härledas till en betrodd utfärdare.

Varje sådan relation behöver svar på frågor som:

- Vem får utfärda identiteten eller intyget?
- Vad betyder attributen?
- Hur länge gäller de?
- Hur återkallas eller avvecklas tilliten?
- Vilka säkerhetsnivåer förutsätts?
- Hur hanteras incidenter?
- Vem ansvarar för att relationen fortfarande är korrekt?

Därför bör tillit dokumenteras som en avsiktlig relation med ägare och livscykel, inte som ett historiskt tekniskt undantag som råkar fungera. En trustrelation behöver också vara avgränsad: att en part får intyga en användares identitet betyder inte att samma part automatiskt får avgöra användarens verksamhetsbehörighet. På samma sätt innebär ett betrott certifikat inte att varje operation från innehavaren ska accepteras. Tillit behöver därför alltid kopplas till ett tydligt syfte och en definierad mottagare.

## Människoidentitet: livscykel, autentisering och federation

I större organisationer finns normalt behov av en gemensam identitetsdomän för den egna arbetsstyrkan. En *workforce identity*-förmåga kan ge stöd för central autentisering, single sign-on, flerfaktorsautentisering, kontolivscykel, organisatoriska attribut, federation samt återställning och spärrning.

Nyttan är inte bara användarvänlighet. Organisationen kan knyta identitetens livscykel till auktoritativa källor och gemensamma kontrollmekanismer. Om varje system i stället skapar egna lokala användarkonton uppstår parallella livscykler, varierande autentiseringsstyrka, kvarvarande konton och svårare incidenthantering.

En lokal användarrepresentation kan fortfarande behövas för domänspecifika inställningar eller interna identifierare. Men den bör då kopplas till en gemensamt förvaltad identitet i stället för att bli en ny fristående autentiseringsvärld.

Det gör också identitetsdomänen till en viktig gräns. Samma person kan förekomma i flera sammanhang utan att alla sammanhang behöver dela samma lokala kontomodell eller behörighetsstruktur. Det gemensamma bör främst vara den stabila identiteten och de överenskomna attributen; domänspecifik representation och åtkomst kan fortfarande variera.

### Identitetens livscykel

Identitetsarkitektur handlar lika mycket om avveckling som om inloggning. En mänsklig identitet kan genomgå händelser som:

```text
Anställning → organisatoriskt byte → ändrat uppdrag → ledighet → avslut
```

Varje händelse kan påverka vilka konton, grupper, roller och privilegier som ska finnas. Det är därför viktigt att skilja mellan auktoritativ person- och organisationsinformation, identitetslivscykel och behörighetslivscykel. Att en person arbetar på en viss enhet betyder inte automatiskt att personen ska få alla behörigheter som kan associeras med enheten.

### Autentiseringsstyrka ska följa risken

All autentisering behöver inte ha samma styrka. En intern informationssida och en administrativ funktion med långtgående privilegier har olika konsekvens om fel person får åtkomst.

Bedömningen kan påverkas av informationens känslighet, vilken åtgärd som kan utföras, identitetssäkring, risk för credential-stöld och konsekvensen av kontoövertagande. Flerfaktorsautentisering är viktigt, men hjälper inte om användaren redan har felaktiga privilegier eller om en komprometterad tjänsteidentitet kan agera utan begränsning.

Det viktiga är därför kombinationen av rätt identitet, lämplig autentiseringsstyrka, minsta privilegium, begränsad giltighet, spårbarhet och fungerande livscykel.

### Federation – låna identitet utan att kopiera den

När användare tillhör en annan identitetsdomän uppstår frågan om federation. I stället för att skapa en lokal identitet kan den mottagande tjänsten lita på att en extern identitetsleverantör autentiserar användaren och lämnar över ett definierat identitetsintyg.

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

Det centrala arkitekturproblemet är inte bara protokollet utan trustmodellen: vilka utfärdare som accepteras, hur parterna identifieras, vilka attribut som får användas, vilken assurance som ligger bakom och hur nycklar, metadata, incidenter och avveckling hanteras.

OpenID Connect[K2] är ett etablerat protokoll för modern användarautentisering byggt ovanpå OAuth 2.0. OAuth används i sin tur för auktoriserad eller delegerad åtkomst till skyddade resurser och bör inte beskrivas som ett autentiseringsprotokoll i sig. SAML kan fortfarande vara relevant i miljöer där det redan är den etablerade federationsmekanismen.

Organisationen bör profilera ett begränsat antal godkända sätt att federera identitet så att säkerhetskrav, metadata, tokenhantering och livscykel inte behöver uppfinnas på nytt. En federationsprofil kan exempelvis ange vilka utfärdare som får betros, hur klienter registreras, hur signeringsnycklar publiceras och roteras, vilka claims som är obligatoriska och hur felaktiga eller komprometterade relationer stängs av. Det är ofta mer värdefullt än att bara namnge ett protokoll.

### Claims och attribut kräver semantik

Ett identitetsintyg kan innehålla claims eller attribut som namn, identifierare eller organisatorisk tillhörighet. Ett sådant attribut är bara användbart om man vet vem som ansvarar för informationen, vad värdet betyder, hur aktuellt det är och i vilket syfte det får användas.

Identitetsclaims bör därför behandlas som andra informationskontrakt: de behöver semantik, ägare och livscykel. Att en token tekniskt innehåller ett fält gör inte fältet till lämpligt underlag för ett kritiskt verksamhetsbeslut. En organisatorisk tillhörighet kan exempelvis vara korrekt som kataloginformation men ändå för grov för att avgöra vem som får fatta ett visst beslut. I andra fall kan ett attribut behöva hämtas från en mer auktoritativ verksamhetskälla än identitetsplattformen.

## Tjänsteidentitet och credentials

Människor är bara en del av identitetslandskapet. Moderna system består av tjänster, workloads, integrationskomponenter, pipelines och automatiserade agenter som kommunicerar utan en människa i varje interaktion.

Ett vanligt anti-pattern är att sådana komponenter använder en namngiven persons konto, ett delat servicekonto, statiska lösenord eller API-nycklar som aldrig roteras. Det gör ansvar, spårbarhet och avveckling svåra.

Ett bättre mönster är tjänsteidentitet:

```text
Tjänst A ── egen identitet ──▶ Tjänst B
```

Identiteten bör vara unik för relevant tjänst eller workload, kopplad till dess tekniska livscykel, begränsad till minsta nödvändiga privilegium och möjlig att spåra. Där det är praktiskt möjligt bör credentials vara kortlivade eller automatiskt roterade.

Det skapar en viktig koppling till runtimeförmågan. En modern runtimeplattform kan utfärda och distribuera workload-identiteter utan att statiska hemligheter behöver byggas in i images eller konfiguration. Det gör också identiteten mer nära knuten till den faktiska körningen: när workloaden försvinner kan dess credential upphöra att vara giltig, och en ny instans kan få en ny kortlivad credential utan manuell hantering.

### Eget ansvar eller användardelegering

En backend-tjänst kan agera i eget ansvar, exempelvis när en schemalagd komponent uppdaterar ett index, eller för en användares räkning när en operation fortsätter över flera tjänster.

Modellerna bör inte blandas. Om en användartoken okritiskt skickas vidare genom många tjänster kan privilegier spridas längre än avsett. Om allt i stället görs med backendens tjänsteidentitet kan användarkontexten försvinna. Arkitekturen behöver därför uttryckligen avgöra vem som agerar i vems ansvar. Det påverkar både tokenmodell, loggning och auktorisation. I vissa flöden behöver den bakomliggande tjänsten känna till både den tekniska anroparen och den ursprungliga användaren, eftersom de svarar på olika frågor: vilken komponent gjorde anropet och på vems uppdrag skedde det?

### PKI, certifikat och teknisk tillit

PKI används för att knyta kryptografiska nycklar till identiteter genom certifikat och betrodda utfärdare. Certifikat kan exempelvis användas för TLS, mTLS, tjänsteidentitet eller signering.

Det viktiga arkitekturperspektivet är att certifikatet inte bara är en fil utan har en livscykel:

```text
Beställning → utfärdande → distribution → användning → förnyelse/rotation → avveckling
```

En gemensam PKI- och certifikattjänst bör därför stödja kontrollerad identitet, ägarskap, automatisering, förnyelse och avveckling. Den behöver också göra det möjligt att förstå vilka certifikat som finns, var de används och vem som ansvarar för dem. Annars flyttas bara den manuella hanteringen till en central utfärdare. mTLS kan ge stark maskin-till-maskin-autentisering, men svarar fortfarande inte på vilka operationer den autentiserade tjänsten får utföra.

### Secrets är credentials – inte konfiguration

Lösenord, privata nycklar och API-nycklar behöver behandlas annorlunda än vanlig konfiguration. Om de hamnar i källkod, images, generella konfigurationsfiler eller dokumentation blir de svåra att rotera och avveckla.

En gemensam *secrets management*-tjänst kan ge skyddad lagring, kontrollerad åtkomst, audit, rotation och tidsbegränsad distribution. Den löser dock inte automatiskt frågan om hur många kopior som skapas efter att en secret hämtats eller om konsumenten faktiskt klarar rotation utan driftstopp. Därför behöver credential-livscykeln omfatta både lagringen och användningen.

Den långsiktigt bättre lösningen är ofta att minska mängden långlivade secrets. Om en workload kan få en kortlivad identitet från runtimeplattformen är det normalt bättre än att distribuera ett statiskt lösenord från ett valv. Secrets management och service identity är därmed närliggande men olika förmågor: den ena skyddar credentials som fortfarande måste finnas, den andra kan minska behovet av dem.

### Privilegier och minsta privilegium har en livscykel

Administrativa identiteter kan få åtkomst som vanliga användare aldrig bör ha. Det kan gälla plattforms-, databas-, säkerhets- eller identitetsadministration och åtkomst till produktionsmiljöer.

Här behövs ofta stark autentisering, separering från vanlig användaridentitet, tidsbegränsad åtkomst, tydlig loggning och fungerande reservvägar för nödsituationer. Delade administratörskonton bör undvikas.

Minsta privilegium är samtidigt inte ett engångsbeslut. Personer byter roller, tjänster får nya funktioner och projekt avslutas. Åtkomst behöver därför ha ägare, kunna omprövas och avvecklas när underlaget försvinner. Särskilt känsliga credentials bör ha kort giltighet där det är möjligt. För privilegierad åtkomst kan det också vara motiverat med just-in-time-behörighet, särskild sessionsloggning eller en separat administrativ identitet så att vardagsanvändningen inte automatiskt sker med höga rättigheter.

### Tokens är tidsbegränsade säkerhetsobjekt

I federerade och API-baserade arkitekturer bär tokens information om en autentiserad eller auktoriserad kontext. En token har bland annat utfärdare, avsedd mottagare, giltighetstid, scopes eller andra behörighetsuppgifter och kryptografiskt skydd.

Den bör därför inte accepteras bara för att signaturen är korrekt. Mottagaren måste även verifiera att token är av rätt typ, kommer från rätt utfärdare och är avsedd för rätt sammanhang.

Moderna OAuth-profiler och säkerhetsrekommendationer har utvecklats för att minska riskerna med felaktig tokenhantering och alltför bred återanvändning.[K3] För den gemensamma arkitekturen talar det för standardiserade profiler snarare än applikationsspecifika varianter. En profil bör till exempel ange vilka token-typer som får användas mellan vilka parter, hur audience verifieras, hur scopes tolkas och när vidaredelegering är tillåten. På så sätt blir tokenhanteringen en styrd del av tillitsmodellen i stället för ett lokalt integrationsbeslut.

## Identity proofing är en annan fråga än autentisering

Särskilt för externa användare behöver man skilja mellan två frågor:

1. Hur vet vi vilken verklig person eller organisation den digitala identiteten representerar?
2. Hur verifierar vi senare att den som försöker logga in kontrollerar rätt autentiseringsmedel?

Den första handlar om identity proofing eller identitetssäkring vid etableringen av identiteten. Den andra handlar om autentisering. En tekniskt stark autentisering kan alltså inte kompensera för en svag eller felaktig ursprunglig identitetskoppling.

Aktuella riktlinjer för digital identitet, exempelvis NIST SP 800-63-4[K1], skiljer uttryckligen mellan identitetssäkring, autentisering och federation. Boken använder inte NIST:s nivåmodell som ett generellt krav, men distinktionen är användbar även utanför det ramverket. Den hjälper också organisationen att undvika ett vanligt misstag: att välja starkare autentisering som kompensation för att identiteten etablerades på ett otillräckligt säkert sätt från början.

## Identitet och Zero Trust

Den användbara kärnan i Zero Trust är att åtkomst inte bör följa automatiskt av att en aktör befinner sig på ett visst nät eller innanför en traditionell perimeter. Identitet, enhet, kontext, policy och den skyddade resursen behöver i stället ingå i åtkomstbeslutet.

Det betyder inte att identitetsplattformen ensam realiserar Zero Trust. Nätverk, enhetssäkerhet, policy enforcement, observerbarhet och informationsskydd behöver samverka.

Zero Trust-perspektivet förstärker också betydelsen av tjänsteidentiteter. När nätposition inte längre ska vara det huvudsakliga tillitsbeviset behöver varje relevant workload kunna identifieras och bedömas på ett sätt som fungerar även när anrop passerar flera nät- eller plattformsgränser. Det gör identitet och runtime nära kopplade, men de förblir olika förmågor: runtime utfärdar eller distribuerar ofta identiteten, medan identitetsförmågan definierar trustmodell, profiler och livscykel.

För förmågemodellen är lärdomen främst:

> Implicit tillit bör ersättas med explicita, verifierbara och förvaltade tillitsrelationer där konsekvensen motiverar det.

## Gemensamma plattformstjänster och standardprofiler

Identitet och tillit kan realiseras genom flera separata plattformserbjudanden, exempelvis:

- *Workforce Identity* för interna användares identiteter, autentisering, SSO, MFA, federation och kontolivscykel,
- *Service Identity* för tjänste- och workload-identiteter, maskin-till-maskin-autentisering och kortlivade credentials,
- *PKI & Certificate Service* för certifikatutfärdande, trust anchors, förnyelse, rotation och avveckling,
- *Secrets Management* för skyddad lagring och distribution av hemliga credentials när sådana fortfarande behövs.

I en större organisation kan även externa identiteter, privileged access och policybaserad auktorisation bli egna erbjudanden. Erbjudandena behöver ha tydliga målgrupper och gränser. Workforce identity bör exempelvis inte automatiskt bli platsen där alla verksamhetsspecifika behörighetsregler modelleras, och secrets management bör inte vara standardlösningen för identiteter som kan utfärdas dynamiskt.

Förmågan är stabilare än produktportföljen; produkter och runtime-integrationer kan bytas utan att behovet av identitet och tillit försvinner.

Gemensamma standarder bör samtidigt profilera användningen, inte bara namnge protokoll. Att skriva ”använd OAuth” eller ”använd OIDC” är otillräckligt. En användbar standard behöver exempelvis ange godkända profiler och användningsfall, hur klienter autentiseras, hur tokenlivslängder och scopes hanteras, hur nycklar roteras och hur tjänsteidentiteter provisioneras. Den bör också ange när ett visst mönster inte är lämpligt, exempelvis när en användartoken inte ska vidarebefordras eller när mTLS behöver kompletteras med separat auktorisationsinformation.

Exakta produktinställningar bör däremot ligga i produkt- och konfigurationsstandarder med kortare livslängd än den gemensamma arkitekturen. En sådan separation gör det möjligt att byta identitetsprodukt eller uppdatera protokollkonfiguration utan att förmågemodellen och de övergripande tillitsprinciperna behöver skrivas om.

## Ansvar och gränser

Den gemensamma arkitekturen bör definiera identitets- och trustprinciper, huvudtyper av identiteter, övergripande krav på autentisering och credential-hantering, federation, tjänsteidentiteter och särskilt privilegierad åtkomst.

Förmågeansvaret omsätter detta i identitetsplattformar, federationstjänster, service identity, PKI, secrets management, standardprofiler och operativa processer för incidenter och avveckling.

Den konkreta lösningen ansvarar fortfarande för vilka användargrupper som behöver åtkomst, vilka verksamhetsoperationer de får utföra, hur identitetsattribut används i domänens behörighetsmodell och vilka tjänsteidentiteter eller externa parter lösningen behöver.

Gemensam identitet tar alltså inte bort lösningens ansvar för sin egen auktorisationsmodell. Den gemensamma nivån ska göra identitets- och trustfrågorna enklare och säkrare att lösa, inte absorbera den domänkunskap som krävs för att avgöra vad en användare eller tjänst faktiskt får göra.

## Vanliga anti-patterns

### Lokal användardatabas som standardlösning

Varje applikation skapar egna användarnamn och lösenord trots att en gemensam identitetstjänst finns.

**Konsekvens:** parallella livscykler, svagare kontroll och högre förvaltningskostnad.

### Personliga eller delade konton för tjänster

Tekniska integrationer använder en namngiven persons credentials eller flera tjänster delar samma tekniska identitet.

**Konsekvens:** otydligt ansvar, svag spårbarhet och svårt att tillämpa minsta privilegium.

### Hemligheter utan kontrollerad livscykel

API-nycklar eller lösenord checkas in tillsammans med applikationen eller skapas med lång livslängd utan rotation.

**Konsekvens:** okontrollerade kopior, svår avveckling och större konsekvens vid kompromettering.

### Central identitetsplattform som verksamhetsregelverk

Alla verksamhetsspecifika åtkomstbeslut pressas in i den centrala IAM-lösningen.

**Konsekvens:** identitetsplattformen får känna till domändetaljer och blir ett förändringshinder.

### Rollinflation

Varje ny kombination av rättigheter skapar en ny global roll.

**Konsekvens:** modellen blir svår att förstå och förvalta.

### Implicit trust eller universella tokens

Interna tjänster får åtkomst bara för att de finns på ”rätt nät”, eller samma token skickas vidare mellan många resurser oavsett avsedd mottagare.

**Konsekvens:** svagare separation mellan tillitsdomäner och större konsekvens när en gräns komprometteras.

Anti-patternen illustrerar en gemensam grundorsak: tilliten är bredare än behovet. En bättre design begränsar både vem som får uttala sig om en identitet och var ett credential eller en token får användas.

## En praktisk analysordning

När ett nytt identitets- eller tillitsbehov uppstår kan följande ordning användas:

1. Identifiera aktörerna: människor, tjänster, workloads, organisationer eller administrativa identiteter.
2. Identifiera identitetsdomänen och vem som äger identiteten.
3. Beskriv vad som behöver bevisas.
4. Bedöm assurance och konsekvens om fel identitet accepteras eller får för stor åtkomst.
5. Separera autentisering från auktorisation.
6. Identifiera federation eller andra trustrelationer och villkoren för dem.
7. Välj identitets- och credentialmodell: workforce identity, service identity, certifikat, delegerad åtkomst eller annan mekanism.
8. Definiera hur identitet och credentials skapas, förändras, roteras, spärras och avvecklas.
9. Definiera spårbarheten till rätt mänsklig eller teknisk identitet.
10. Välj först därefter gemensam plattform och standardprofil.

Analysen bör dokumentera de viktigaste trustrelationerna och deras ägare, inte bara den valda produkten. Då går det senare att byta identitetsleverantör, certifikattjänst eller runtimeintegration utan att förlora förståelsen för varför relationen finns och vilka krav den ska uppfylla.

Ordningen hjälper organisationen att undvika två ytterligheter: att varje system skapar en egen identitetslösning och att den centrala identitetsplattformen försöker äga alla verksamhetsbeslut. Den gör också valet av teknik senare i processen: först när aktör, trustmodell, assurance, delegering och livscykel är begripliga går det att avgöra om behovet bäst möts med federation, certifikat, service identity, secrets management eller en kombination.

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

I nästa kapitel flyttas fokus till den miljö där många av dessa identiteter används: hur applikationer och workloads exekveras standardiserat, isolerat och portabelt i en gemensam runtimeförmåga.

## Källor och vidare läsning

**[K1]** NIST, *SP 800-63-4: Digital Identity Guidelines* (2025). https://csrc.nist.gov/pubs/sp/800/63/4/final

**[K2]** OpenID Foundation, *OpenID Connect Core 1.0 incorporating errata set 2* (2023). https://openid.net/specs/openid-connect-core-1_0.html

**[K3]** IETF/RFC Editor, *RFC 9700 / BCP 240: Best Current Practice for OAuth 2.0 Security* (2025). https://www.rfc-editor.org/info/rfc9700/
