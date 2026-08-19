# 7. Att etablera modellen – ordning, ansvar och iteration

En modell för gemensam IT-arkitektur blir inte användbar bara för att begreppen är väl definierade. Den måste gå att införa i en organisation där system, team, plattformar, leverantörer, standarder och ansvar redan har vuxit fram över tid. Etableringen behöver därför ske iterativt och samtidigt ge nytta i pågående lösningsarbete.

Den bärande ansvarsfördelningen är:

> Gemensam nivå äger spelplanen. Förmågeområden utvecklar de återanvändbara erbjudandena. Lösnings- och produktteam kombinerar dem för konkreta verksamhetsbehov.

Lärandet måste samtidigt kunna röra sig åt andra hållet. Ett återkommande lokalt problem kan motivera ett nytt mönster. Flera likartade mönster kan visa behov av en plattformstjänst. Återkommande avsteg kan visa att en standard eller en förmågegräns behöver omprövas.

Etablering är därför början på en återkopplande arkitekturprocess, inte ett projekt som avslutas när de första dokumenten är skrivna.

## Inventera nuläget – men låt behoven styra strukturen

En inventering av databaser, integrationsprodukter, CI/CD-verktyg, molntjänster och serverplattformar är värdefull, men dagens tekniklandskap bör inte definiera den framtida arkitekturmodellen. Använd inventeringen som faktaunderlag och börja struktureringen i återkommande behov, kvaliteter och risker.

Fråga exempelvis:

- vilka behov återkommer i många lösningar?
- vilka kvaliteter måste organisationen kunna uppnå konsekvent?
- vilka risker blir onödigt stora om varje team löser dem själv?
- var krävs gemensam interoperabilitet?
- vilka kompetenser eller infrastrukturer är rationella att dela?
- vad behöver fortfarande kunna variera lokalt?

Befintliga investeringar, avtal, kompetenser och beroenden är samtidigt verkliga begränsningar. De ska beskriva förutsättningarna för förändring, men inte förväxlas med själva behovet.

## En rekommenderad etableringsordning

En praktisk etablering kan organiseras i nio steg:

1. förstå återkommande behov och viktiga begränsningar,
2. formulera ett litet antal gemensamma principer och kvalitetsdimensioner,
3. skapa en tillräckligt bra första förmågekarta,
4. avgränsa ansvar och beroenden,
5. utse ansvar för förmågorna,
6. prioritera vilka förmågor som ska fördjupas först,
7. utveckla mönster, plattformstjänster och standarder inom de prioriterade områdena,
8. identifiera tvärgående referensarkitekturer,
9. följ upp, lär och justera modellen.

Ordningen anger en riktning, inte ett vattenfall. Ett senare steg kommer ofta att visa att något tidigare behöver ändras.

### 1. Förstå återkommande behov och begränsningar

Målet är inte en fullständig kravkatalog utan en gemensam bild av vilka problem som faktiskt återkommer. Det kan exempelvis vara behov av att exponera digitala tjänster, hantera långlivade processer, utbyta information, fatta spårbara beslut, köra applikationer med definierad tillgänglighet eller leverera programvara säkert och reproducerbart.

Samtidigt behöver viktiga begränsningar göras synliga: lagkrav, informationsklassning, avtal, kompetens, driftmiljöer, externa beroenden och realistisk förändringstakt.

Resultatet behöver vara tillräckligt konkret för att styra nästa steg: en prioriterad bild av återkommande behov och de begränsningar som faktiskt påverkar arkitekturen. Det behöver däremot inte vara komplett. En första etablering tjänar mer på att fånga tio återkommande problem som många team känner igen än på att försöka dokumentera hundratals lokala variationer.

Ett praktiskt sätt att arbeta är att kombinera intervjuer och workshoppar med data från verkliga initiativ: återkommande arkitekturfrågor, incidenter, avsteg, kostnadsdrivare, leveranstider och tekniska beroenden. På så sätt blir behovsbilden förankrad i faktisk friktion snarare än i en abstrakt önskelista.

### 2. Formulera gemensamma principer och kvalitetsdimensioner

Nästa steg är att skapa ett litet antal gemensamma styrsignaler. De behöver inte vara fullständiga från början. Syftet är att ge tillräcklig riktning för att förmågor och ansvar ska kunna diskuteras på ett konsekvent sätt.

Resultatet bör vara en kort, beslutad uppsättning kvalitetsdimensioner och principer som går att använda i verkliga arkitekturfrågor. De behöver också ha en tydlig ägare och en enkel mekanism för omprövning, eftersom de första versionerna kommer att prövas mot verkligheten.

Om organisationen redan här försöker reglera hundratals detaljer riskerar etableringen att fastna i dokumentation innan modellen har prövats. Målet är därför en minsta gemensam styrning som gör nästa steg enklare, inte en fullständig regelbok.

### 3. Skapa en tillräckligt bra första förmågekarta

Förmågekartan ska beskriva vilka typer av stöd det gemensamma IT-området varaktigt behöver kunna erbjuda. Den första versionen behöver inte vara perfekt. Den behöver vara stabil nog för att ge struktur och grov ansvarsfördelning.

Ett område är ofta tillräckligt moget för den första kartan om det beskriver något organisationen behöver kunna göra även om dagens produkter byts ut, om behov och kvalitet går att diskutera utan att först välja teknik och om gränsen mot närliggande områden åtminstone går att beskriva.

Resultatet är en första karta som går att använda och förbättra, inte en slutgiltig taxonomi. Det är också värdefullt att markera osäkra gränser öppet. En förmåga som ännu inte är helt avgränsad behöver inte blockera resten av arbetet, så länge osäkerheten är synlig och någon ansvarar för att reda ut den när mer erfarenhet finns.

### 4. Avgränsa ansvar och beroenden

För varje förmåga behöver det vara begripligt vilket problemområde den omfattar, vad som ligger utanför, vilka andra förmågor den är beroende av och vilka kvaliteter eller samordningsfrågor som är särskilt viktiga.

Gränserna behöver inte vara perfekta. De behöver vara explicita nog för att oenighet ska kunna upptäckas och hanteras. Det gäller särskilt tvärgående frågor som säkerhet, kontinuitet, observerbarhet och informationshantering, där krav, mekanismer och tillämpning ofta ägs på olika nivåer.

Ett användbart resultat från detta steg är därför inte bara en ruta och ett namn, utan en kort gränsbeskrivning: vad förmågan ansvarar för, vad den inte ansvarar för och vilka beroenden som kräver samordning. Den beskrivningen blir senare viktig både för förmågeägare och lösningsteam.

### 5. Utse ansvar för förmågorna

En förmåga utan ansvarig riskerar att stanna som en rubrik i en karta. Någon behöver hålla ihop utvecklingen över tid.

Förmågeansvaret bör normalt omfatta att förstå återkommande konsumentbehov, utveckla vägledning och mönster, identifiera behov av plattformstjänster och standarder, hantera beroenden samt följa användning, brister och återkommande avsteg.

Det behöver inte finnas ett organisatoriskt team per förmåga. Det viktiga är att mandat och ansvar är tydliga och att de är bredare än ägarskapet för en enskild produkt.

Ansvarig behöver också kunna fånga efterfrågan från konsumenterna. Om förmågeansvaret enbart förvaltar befintlig teknik finns en risk att området stelnar kring dagens produkter. Om det däremot kontinuerligt följer återkommande behov kan det avgöra när ett lokalt problem blivit tillräckligt vanligt för att motivera ett gemensamt erbjudande.

### 6. Prioritera vilka förmågor som fördjupas först

Försök inte göra allt samtidigt. Prioritera där bättre gemensam arkitektur kan ge tydlig nytta eller riskreduktion.

En förmåga kan vara särskilt angelägen när många team möter samma problem, dagens variation är dyr eller riskfylld, en större modernisering pågår, flera projekt behöver samma byggblock eller en viktig produkt närmar sig slutet av sin livscykel.

Det är ofta bättre att göra tre prioriterade förmågor verkligt användbara än att skapa en ytlig katalog över alla områden. Prioriteringen bör dessutom vara tidsbunden. När ett område har nått en tillräcklig mognad kan fokus flyttas vidare, medan tidigare förmågor går över i löpande förvaltning och förbättring.

### 7. Utveckla mönster, plattformstjänster och standarder

När ett område prioriterats kan det gemensamma stödet konkretiseras. Återkommande lösningsproblem kan beskrivas som mönster, gemensamma tekniska behov kan paketeras som plattformstjänster och beslut som måste vara konsekventa kan uttryckas som standarder.

Ett område för API:er kan exempelvis erbjuda återanvändbara mönster, API management som tjänst och standarder för kontrakt, autentisering eller versionshantering. Förmågekartan får då ett konkret värde för lösningsteamen.

Resultatet ska vara konsumerbara erbjudanden, inte bara mer dokumentation. Ett bra test är om ett lösningsteam kan förstå när erbjudandet är relevant, hur det används, vilka kvaliteter det ger och vilka begränsningar som följer med det. Om detta fortfarande kräver att teamet först bokar flera möten med centrala experter är erbjudandet sannolikt inte tillräckligt moget.

### 8. Identifiera tvärgående referensarkitekturer

När flera förmågor och erbjudanden har börjat mogna blir återkommande kombinationer synliga. Publika e-tjänster, interna handläggningsstöd eller integrationsintensiva lösningar kan då motivera referensarkitekturer som visar hur flera förmågor samverkar i en typisk lösningsklass.

Referensarkitekturer blir därför ofta bättre när de växer fram ur verkliga återkommande lösningar än när de konstrueras som ett första steg i etableringen. När de väl införs bör de samtidigt förbli tillräckligt generella för att beskriva en lösningsklass, inte frysa en specifik produktkombination som om den vore den enda möjliga realiseringen.

### 9. Följ upp, lär och justera

När modellen används uppstår den viktigaste informationen. Följ därför inte bara efterlevnad, utan även friktion och nytta:

- vilka tjänster används och vilka kringgås?
- vilka standarder kräver ofta avsteg?
- vilka problem löser team fortfarande från grunden?
- var faller ansvar mellan två förmågor?
- vilka kvalitetskrav kan inte mötas med befintliga erbjudanden?
- vilka lokala lösningar återkommer i flera team?

Sådana observationer är arkitektursignaler. De ska kunna leda till nya mönster, förbättrade plattformar, ändrade standarder eller justerade förmågegränser.

Återkopplingen behöver därför ha en mottagare och en rytm. Det kan vara återkommande förmågereview, arkitekturforum eller produktnära feedbackkanaler. Formen är mindre viktig än att erfarenheter inte stannar som lokala irritationer. När samma problem återkommer ska det finnas en väg från observation till gemensam förbättring.

## Tre ansvarsnivåer i praktiken

De tre ansvarsnivåerna är redan en del av modellen. Under etableringen är deras viktigaste funktion att placera beslut där mandat, kunskap och konsekvenser möts.

### Gemensam arkitekturnivå – äger spelplanen

Den gemensamma nivån håller ihop sådant som måste fungera över flera förmågor: begreppsmodell, förmågekarta, gemensamma principer och kvalitetsdimensioner, spelregler för standarder och livscykel samt konflikter och beroenden som går över områdesgränser.

Den ska däremot undvika att detaljbestämma sådant som endast berör ett förmågeområde eller en lösning. Ett praktiskt test är om beslutet måste vara konsekvent över flera förmågor för att helheten ska fungera. Om svaret är nej finns ofta en bättre beslutsnivå längre ned.

### Förmågenivå – utvecklar området och erbjudandena

Förmågeområdet omsätter den gemensamma riktningen till användbart stöd. Här utvecklas mönster, plattformstjänster, förmågespecifika standarder, kvalitetsprofiler och golden paths, samtidigt som beroenden och konsumentbehov hanteras.

Förmågenivån ska göra vanliga och önskvärda lösningar enklare, inte designa varje konsuments lösning. Den bör därför mäta sin framgång i faktisk användning, ledtid, kvalitet och minskad lokal uppfinningsbörda snarare än i hur många styrdokument den producerar.

### Lösnings-/produktnivå – kombinerar och tillämpar

Lösnings- och produktteam kombinerar de gemensamma erbjudandena med den specifika domänen, informationsmodellen, riskbilden och kvalitetskraven. Här görs lokala arkitekturbeslut och här upptäcks också när ett gemensamt erbjudande inte räcker.

Ett team ska alltså inte behöva uppfinna generella mekanismer från grunden när fungerande gemensamma erbjudanden finns, men måste fortfarande avgöra hur de används i den egna lösningen. När erbjudandet inte passar ska teamet kunna beskriva varför. Den informationen är viktig återkoppling till förmågenivån, oavsett om resultatet blir ett avsteg, en förbättring av erbjudandet eller ett nytt mönster.

## Ansvar ska följa beslutets räckvidd

En användbar regel är:

> Ett arkitekturbeslut bör fattas på den lägsta nivå som kan bära beslutets konsekvenser utan att skapa problem för helheten.

Lokala beslut bör stanna lokala när de inte påverkar andra. Beslut som berör flera konsumenter hör hemma på förmågenivå. Gemensamma beslut behövs när konsekvenserna går över flera förmågor eller när interoperabilitet, säkerhet, kostnad eller andra tvärgående egenskaper kräver en gemensam riktning.

Det minskar både risken för central detaljstyrning och risken för onödig fragmentering. Beslutsnivån bör alltså inte väljas utifrån organisatorisk prestige eller vana, utan utifrån hur långt konsekvenserna faktiskt sträcker sig.

## Top-down för sammanhang, bottom-up för lärande

Etableringen behöver röra sig i två riktningar samtidigt.

Top-down behövs för att skapa riktning: gemensamma mål, principer, kvalitetsdimensioner, en första förmågestruktur och tydliga ansvarssnitt.

Bottom-up behövs för att skapa realism: faktiska problem i teamen, återkommande lokala mönster, plattformsfriktion, incidenter, avsteg och erfarenheter från genomförda lösningar.

Enbart top-down ger lätt en idealmodell som ingen använder. Enbart bottom-up riskerar att dokumentera dagens lösningar utan att skapa en gemensam riktning. Mognaden ligger i återkopplingen mellan dem.

## Arbeta i korta etableringscykler

Modellen ska inte bli ”klar” innan den används. En bättre cykel är:

1. skapa en första gemensam modell,
2. välj ett fåtal prioriterade förmågor,
3. utveckla konkreta erbjudanden,
4. använd dem i verkliga lösningar,
5. samla erfarenheter,
6. justera modellen och erbjudandena,
7. gå vidare till nästa prioriterade område.

Varje varv bör ge mer användbar arkitektur, inte bara fler dokument. Det är fullt rimligt att ha en stabil övergripande förmågekarta samtidigt som bara några förmågor har mogna erbjudanden. Mognadsgraden bör då vara synlig så att konsumenterna vet vad som är etablerat, vad som är under utveckling och vad som ännu saknar gemensamt stöd.

## Börja där friktionen är hög

Det finns ingen universell första förmåga. Börja där bättre gemensam arkitektur kan ge tydlig verksamhetsnytta, riskreduktion eller utvecklingseffektivitet.

En organisation med integrationsproblem kan börja med integration och kommunikation. En organisation som moderniserar driftmiljön kan prioritera runtime, driftbarhet och programvaruleverans. Ett område med stora krav på spårbar handläggning kan behöva börja med process, regler, identitet och data.

Tidiga konkreta förbättringar ger dessutom modellen legitimitet. Ett initiativ som löser verkliga problem blir lättare en del av vardagen än ett initiativ som först försöker färdigställa hela katalogen.

## En konkret första leverans

En rimlig första leverans kan vara betydligt mindre än hela modellen i denna bok. Den kan bestå av:

- en gemensam begreppsmodell,
- ett litet antal arkitekturprinciper och kvalitetsdimensioner,
- en första förmågekarta med begripliga gränser,
- namngivna ansvariga för prioriterade förmågor,
- några väl beskrivna mönster,
- konsumerbara plattformstjänster där behovet redan är tydligt,
- tekniska standarder där konsekvens faktiskt behövs,
- någon referensarkitektur för en vanlig lösningsklass,
- en enkel mekanism för återkoppling, beslut och avsteg.

Det viktigaste är att delarna hänger ihop och går att använda i ett verkligt lösningsarbete. En mindre modell där ett team kan gå från behov till relevant förmåga, förstå tillgängliga mönster och tjänster och se vilka standarder som gäller är mer värdefull än en stor dokumentmängd utan tydlig väg genom materialet.

## Tecken på att ansvarsnivån är fel

Tecken på för hög centralisering är bland annat att små lokala teknikbeslut kräver central behandling, arkitekturforum blir godkännandeköer och lösningsteam väntar på besked i frågor där de själva har bäst kunskap.

Tecken på för låg samordning är att samma problem löses på många olika sätt utan tydlig anledning, interoperabilitet kräver specialanpassningar, generella mekanismer byggs om från grunden i varje produkt eller ingen kan säga vem som ansvarar för ett tvärgående problem.

Poängen är inte att hitta mitten på en abstrakt skala, utan att placera varje beslut där kunskap, mandat och konsekvenser bäst kan mötas.

## Mognad är inte mängden dokument

Arkitekturmognad syns inte främst i antalet modeller och dokument. Den syns i att ansvar är begripligt, återkommande problem löses på rätt nivå, gemensamma erbjudanden har verkliga konsumenter, standarder har tydliga motiv och erfarenheter från lösningsteamen faktiskt påverkar den gemensamma arkitekturen.

En mogen modell hjälper organisationen att fatta bättre sammanhängande beslut över tid och kan förändras utan att hela strukturen behöver göras om.

## Från etablering till fördjupning

Grunden är nu på plats. Nästa steg är att fördjupa den mest stabila strukturen i modellen: de gemensamma IT-förmågorna.

Del II börjar därför med frågan: vad är egentligen en IT-förmåga, och hur skiljer den sig från en tjänst, plattform, organisatorisk enhet eller produkt?
