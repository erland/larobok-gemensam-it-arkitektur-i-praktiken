# 7. Att etablera modellen – ordning, ansvar och iteration

En modell för gemensam IT-arkitektur blir inte användbar bara för att begreppen är väl definierade. Den måste också gå att etablera i en verklig organisation där det redan finns system, team, plattformar, leverantörer, tekniska standarder, budgetar och ansvar som vuxit fram över tid. Det gör etableringen till en arkitekturfråga i sig.

Det är lätt att föreställa sig arbetet som en sekvens där organisationen först ritar den perfekta förmågekartan, därefter definierar alla lösningsmönster, sedan specificerar plattformarna, beslutar standarderna och slutligen låter projekten börja använda dem. Ett sådant upplägg ser rationellt ut på papperet men riskerar att bli både långsamt och verklighetsfrånvänt. Arkitekturen behöver formas av faktiska behov och erfarenheter samtidigt som den skapar ett gemensamt sammanhang som lokala beslut kan förhålla sig till.

Det här kapitlet presenterar därför bokens rekommenderade arbetssätt för att etablera modellen. Det är inte en universell standard och inte en process som måste följas mekaniskt. Syftet är att ge en praktisk ordning och en ansvarsfördelning som minskar risken för två vanliga ytterligheter: central detaljstyrning och oberoende lokal optimering.

Den bärande tanken är enkel:

> Gemensam nivå ska äga spelplanen. Förmågeområden ska utveckla de återanvändbara erbjudandena. Lösnings- och produktteam ska använda och kombinera dem för konkreta verksamhetsbehov.

Samtidigt måste erfarenheter kunna röra sig åt andra hållet. När en lösning upptäcker ett återkommande problem kan det leda till ett nytt mönster. När flera mönster kräver samma tekniska mekanism kan det motivera en plattformstjänst. När en standard ofta behöver undantag kan standarden eller själva förmågegränsen behöva omprövas.

Etablering är därför inte en engångsövning. Det är början på en återkopplande arkitekturprocess.

## Börja inte med katalogen

När en organisation vill skapa ordning i ett komplext IT-landskap är det lockande att börja inventera det som redan finns. Vilka databaser använder vi? Vilka integrationsprodukter har vi? Vilka CI/CD-verktyg finns? Vilka molntjänster och serverplattformar betalar vi för?

Inventeringen kan vara värdefull, men den bör inte vara modellens utgångspunkt. Om dagens tekniklandskap får definiera strukturen blir den gemensamma arkitekturen lätt en dokumentation av historiska beslut snarare än ett stöd för framtida beslut.

Etableringen bör i stället börja med frågor som:

- vilka typer av behov återkommer i många verksamhetslösningar?
- vilka kvalitetskrav behöver organisationen kunna möta konsekvent?
- vilka risker blir onödigt stora om varje team löser dem själv?
- vilka områden kräver gemensam interoperabilitet?
- var finns kompetens eller infrastruktur som är rationell att dela?
- vilka delar behöver vara lokalt differentierade för att verksamheten ska kunna utvecklas snabbt?

Det betyder inte att det befintliga landskapet ignoreras. Befintliga investeringar, avtal, kompetenser och tekniska beroenden är verkliga begränsningar. Men de ska beskriva förutsättningarna för förändring, inte definiera vilka behov organisationen har.

Den distinktionen från kapitel 3 blir särskilt viktig under etableringen. Ett konstaterande som ”vi har en central integrationsplattform” är inte samma sak som ”vi behöver förmåga till säker, spårbar och förändringsbar kommunikation mellan system”. Det första beskriver en realisering. Det andra beskriver något organisationen behöver kunna åstadkomma även den dag dagens produkt har ersatts.

## En rekommenderad etableringsordning

En praktisk etablering kan organiseras i nio steg:

1. förstå återkommande behov och verkliga begränsningar,
2. formulera gemensamma principer och kvalitetsdimensioner,
3. skapa en tillräckligt bra första förmågekarta,
4. avgränsa ansvar och beroenden,
5. utse ansvar för förmågorna,
6. prioritera vilka förmågor som behöver fördjupas först,
7. utveckla mönster, plattformstjänster och standarder inom de prioriterade områdena,
8. identifiera tvärgående referensarkitekturer,
9. följ upp, lär och justera modellen.

Ordningen är avsiktlig, men den är inte ett vattenfall. Ett senare steg kommer ofta att visa att något tidigare behöver ändras. Det är inte ett misslyckande utan en förväntad del av arbetet.

### 1. Förstå återkommande behov och begränsningar

Det första målet är inte att skapa en fullständig kravkatalog. Målet är att förstå vilka problem som faktiskt återkommer på organisationsnivå.

En myndighet eller större organisation kan exempelvis se återkommande behov av att:

- exponera digitala tjänster till externa användare,
- hantera långlivade ärenden och mänskliga arbetssteg,
- utbyta information med andra organisationer,
- fatta spårbara regelbaserade beslut,
- lagra och återställa verksamhetskritisk information,
- köra applikationer med definierade tillgänglighetsnivåer,
- autentisera människor och tekniska tjänster,
- leverera programvara reproducerbart och säkert,
- övervaka distribuerade lösningar,
- erbjuda samarbets- och produktivitetsverktyg.

Samtidigt behöver viktiga begränsningar göras synliga: lagkrav, informationsklassning, befintliga avtal, kompetens, nätförutsättningar, driftmiljöer, beroenden till externa aktörer och realistisk förändringstakt.

Det viktiga är att hålla isär de två kategorierna. Behovet beskriver vad organisationen behöver kunna åstadkomma. Begränsningen beskriver ett villkor som arkitekturen måste ta hänsyn till.

### 2. Formulera gemensamma principer och kvalitetsdimensioner

Innan förmågekartan blir för detaljerad behöver organisationen ett litet antal gemensamma styrsignaler. Kapitel 4 och 6 beskrev två typer: kvalitetsdimensioner och arkitekturprinciper.

Kvalitetsdimensionerna hjälper organisationen att ställa samma slags frågor över flera områden. Tillgänglighet, säkerhet, spårbarhet, interoperabilitet och förvaltningsbarhet behöver exempelvis inte betyda samma nivå överallt, men de behöver kunna diskuteras med ett gemensamt språk.

Principerna uttrycker återkommande prioriteringar. ”Behov före teknik”, ”problem löses på lämplig arkitekturnivå” och ”ansvar och gränssnitt ska vara tydliga” påverkar hur själva etableringen genomförs.

Här bör ambitionen vara liten men användbar. En organisation som försöker besluta hundratals detaljer innan den har testat modellen riskerar att skapa en regelbok som saknar kontakt med det arbete den ska stödja.

### 3. Skapa en tillräckligt bra första förmågekarta

Nästa steg är att beskriva vilka typer av stöd organisationens gemensamma IT-område varaktigt behöver kunna erbjuda.

Nyckelorden är tillräckligt bra första. Förmågekartan behöver vara stabil nog för att ge struktur, men inte så detaljerad att månader används till att avgöra exakt var varje teknisk mekanism hör hemma.

En första karta kan exempelvis identifiera områden som interaktion, process, regler, data, integration, identitet, runtime, driftbarhet och programvaruleverans. Det viktiga i detta läge är inte att bevisa att indelningen är den enda möjliga. Det viktiga är att varje område beskriver ett begripligt och relativt långlivat ansvar som går att fördjupa.

Kapitel 8 kommer att definiera förmågebegreppet mer precist. Under etableringen räcker följande test långt:

- beskriver området något organisationen behöver kunna göra eller erbjuda även om dagens produkter byts ut?
- är området begripligt för andra än specialisterna som arbetar med dagens verktyg?
- kan man resonera om behov, kvalitet, ansvar och utveckling för området utan att först välja produkt?
- är gränsen mot närliggande områden åtminstone möjlig att beskriva?

Om svaren huvudsakligen är ja är området ofta tillräckligt stabilt för den första kartan.

### 4. Avgränsa ansvar och beroenden

En lista över förmågor räcker inte. Om ingen vet var ett problem hör hemma uppstår snabbt antingen dubbelarbete eller tomrum.

För varje förmåga behöver därför några grundfrågor besvaras:

- vilket problemområde omfattar förmågan?
- vad ligger uttryckligen utanför?
- vilka andra förmågor är den beroende av?
- vilka kvaliteter är särskilt viktiga?
- vilka beslut behöver koordineras med andra områden?
- vilka konsumenter förväntas använda stödet?

Gränserna behöver inte vara perfekta. De behöver vara diskuterbara. En oklar gräns som är explicit dokumenterad är ofta lättare att hantera än två områden som båda antar att den andre ansvarar för frågan.

Detta gäller särskilt tvärgående frågor. Säkerhet, kontinuitet, observerbarhet, informationshantering och livscykel går inte alltid att stoppa in i en enda organisatorisk låda. Det centrala blir då att skilja på vem som sätter gemensamma krav, vem som tillhandahåller mekanismer och vem som tillämpar dem i en konkret lösning.

### 5. Utse ansvar för förmågorna

En förmåga utan ansvarig riskerar att bli en rubrik i en arkitekturkarta. Någon behöver ha mandat att utveckla området över tid.

Det betyder inte nödvändigtvis att varje förmåga måste motsvara ett organisatoriskt team. En organisatorisk enhet kan ansvara för flera förmågor och en förmåga kan kräva samverkan mellan flera team. Men det behöver vara tydligt vem som håller ihop förmågans utveckling.

Förmågeansvaret bör normalt omfatta att:

- förstå återkommande konsumentbehov,
- utveckla förmågespecifik vägledning,
- identifiera och förvalta relevanta lösningsmönster,
- formulera behov av gemensamma plattformstjänster,
- bidra till eller äga relevanta standarder,
- hantera beroenden till andra förmågor,
- följa användning, brister och återkommande avsteg,
- föreslå förändringar när området inte längre möter organisationens behov.

Det är viktigt att skilja detta från produktägarskap. En produktägare kan ansvara för exempelvis en konkret API-managementprodukt. Förmågeansvaret för integration och kommunikation är bredare och ska fortfarande vara begripligt om produkten byts ut eller om flera tekniska realiseringar används parallellt.

### 6. Prioritera vilka förmågor som fördjupas först

Nästa frestelse är att göra allt samtidigt. Elva förmågor kan snabbt ge hundratals mönster, tjänster, standarder och beroenden. Om allt ska bli komplett innan något används blir etableringen ett dokumentationsprogram snarare än arkitekturutveckling.

Prioriteringen bör i stället styras av verklig nytta och risk. En förmåga kan vara särskilt angelägen därför att:

- många lösningsteam har samma problem,
- dagens variation skapar hög kostnad eller säkerhetsrisk,
- en större förändring eller modernisering är på väg,
- flera projekt behöver samma nya byggblock,
- en teknisk produkt närmar sig slutet av sin livscykel,
- externa krav förändras,
- organisationen saknar ett tydligt ansvar i ett kritiskt område.

Det är ofta bättre att fördjupa tre viktiga förmågor så att de faktiskt hjälper lösningsteamen än att skriva en ytlig katalog för alla områden.

### 7. Utveckla mönster, plattformstjänster och standarder

När ett förmågeområde prioriterats kan detaljarbetet börja. Här blir separationen mellan artefakttyperna från kapitel 2 viktig.

Ett återkommande lösningsproblem kan beskrivas som ett lösningsmönster. Ett tekniskt behov som många team behöver konsumera kan paketeras som en plattformstjänst. Ett beslut som behöver vara konsekvent för interoperabilitet, risk eller förvaltning kan uttryckas som en standard.

De tre artefakterna ska inte ersätta varandra.

Anta att flera team behöver exponera API:er. Förmågeområdet kan då utveckla mönster för hur API:er används i olika typer av lösningar, erbjuda API management som gemensam plattformstjänst och besluta tekniska standarder för exempelvis kontrakt, autentisering eller versionshantering. Ett enskilt produktteam använder sedan dessa byggstenar i sin lösningsarkitektur.

Det är i detta steg som den gemensamma arkitekturen börjar få konkret värde för konsumenterna. Förmågekartan i sig löser inget projektproblem. Värdet uppstår när den leder till begriplig vägledning och återanvändbara erbjudanden.

### 8. Identifiera tvärgående referensarkitekturer

När flera förmågor utvecklats blir återkommande kombinationer synliga. En publik e-tjänst kan exempelvis återkommande behöva interaktion, identitet, integration, data, runtime och driftbarhet. Ett internt handläggningsstöd kan kombinera workflow, regler, data, dokument, integration och observerbarhet.

När samma kombination och samma arkitekturella frågor återkommer kan en referensarkitektur vara mer användbar än att varje förmåga dokumenteras separat.

Referensarkitekturen är därför ofta svår att utforma väl allra först. Om den skapas innan förmågorna och deras erbjudanden är förstådda riskerar den att bli antingen abstrakt eller starkt färgad av ett enskilt system. När förmågeperspektivet mognat kan referensarkitekturen i stället visa hur flera delar samverkar i en typisk lösningsklass.

### 9. Följ upp, lär och justera

När modellen börjar användas uppstår den viktigaste informationen: vad som faktiskt fungerar.

Organisationen bör aktivt följa exempelvis:

- vilka plattformstjänster som används och vilka som kringgås,
- vilka standarder som ofta kräver avsteg,
- vilka frågor lösningsteamen fortfarande behöver lösa från grunden,
- var ansvar faller mellan två förmågor,
- vilka mönster som misstolkas eller saknar nödvändiga variationer,
- vilka kvalitetskrav som inte kan uppfyllas med befintliga erbjudanden,
- vilka lokala lösningar som återkommer i flera team.

Detta är inte bara förvaltningsdata. Det är arkitektursignaler.

Om fem produktteam bygger samma lokala mekanism kan det vara tecken på ett saknat gemensamt erbjudande. Om ingen använder en standardiserad plattform kan problemet ligga i plattformens användbarhet, kostnadsmodell eller leveranstid snarare än i teamens följsamhet. Om samma avsteg godkänns om och om igen kan standarden vara felkalibrerad.

Arkitekturen behöver därför mäta mer än efterlevnad. Den behöver mäta friktion och nytta.

## Tre ansvarsnivåer

Etableringsordningen blir betydligt tydligare om arkitekturen skiljer mellan tre ansvarsnivåer. De är analytiska nivåer, inte ett krav på tre organisatoriska hierarkier.

### Gemensam arkitekturnivå – äger spelplanen

Den gemensamma nivån ansvarar för sådant som måste hänga ihop över flera förmågor. Typiska uppgifter är att:

- förvalta den övergripande begrepps- och metamodellen,
- hålla ihop den gemensamma förmågekartan,
- definiera gemensamma arkitekturprinciper,
- definiera tvärgående kvalitetsdimensioner,
- besluta gemensamma regler för standarder och livscykel,
- tydliggöra ansvar och beroenden mellan förmågor,
- identifiera behov av tvärgående referensarkitekturer,
- hantera konflikter som inte kan lösas inom ett enskilt förmågeområde.

Den gemensamma nivån ska däremot vara försiktig med att detaljbestämma tekniska lösningar som bara berör ett område. Om varje API-regel, databasinställning eller CI/CD-mekanism måste beslutas centralt blir arkitekturen en flaskhals.

Ett bra test är:

> Behöver detta beslut vara konsekvent över flera förmågor för att helheten ska fungera?

Om svaret är nej finns det ofta en lägre och bättre beslutsnivå.

### Förmågenivå – utvecklar området och erbjudandena

Förmågeområdet ansvarar för att omsätta den gemensamma spelplanen till ett användbart stöd inom sitt område.

Här hör frågor hemma som:

- vilka återkommande behov har konsumenterna?
- vilka lösningsmönster bör rekommenderas?
- vilka gemensamma plattformstjänster behövs?
- vilka tekniska standarder krävs inom området?
- vilka golden paths eller automatiserade flöden kan sänka tröskeln?
- vilka kvalitetsprofiler behöver tjänsterna kunna erbjuda?
- vilka beroenden finns mot andra förmågor?
- hur ser livscykeln ut för områdets tekniska realiseringar?

Förmågenivån ska samtidigt undvika att designa varje konsuments lösning. Den ska göra vanliga och önskvärda lösningar enklare, inte göra lokala arkitekter och produktteam överflödiga.

### Lösnings-/produktnivå – kombinerar och tillämpar

Det konkreta verksamhetsbehovet finns på lösnings- och produktnivån. Här måste arkitekturen ta hänsyn till den specifika domänen, informationsmodellen, riskerna, kvalitetskraven och integrationskontexten.

Teamet behöver kunna:

- välja relevanta mönster och plattformstjänster,
- kombinera erbjudanden från flera förmågor,
- utforma domän- och lösningsspecifika delar,
- göra explicita avvägningar,
- dokumentera lokala arkitekturbeslut,
- identifiera när ett gemensamt erbjudande inte räcker,
- initiera ett motiverat avsteg när det behövs.

Ett produktteam ska alltså inte behöva uppfinna tjänsteidentitet, observerbarhet eller containerplattform från grunden om organisationen redan erbjuder fungerande gemensamma lösningar. Men teamet måste fortfarande avgöra hur identiteter, loggning, driftkrav och runtime passar just den produktens behov.

## Ansvar ska följa beslutets räckvidd

De tre nivåerna kan sammanfattas med en generell regel:

> Ett arkitekturbeslut bör fattas på den lägsta nivå som kan bära beslutets konsekvenser utan att skapa problem för helheten.

Det innebär att ett lokalt beslut bör stanna lokalt när det inte påverkar andra. Ett förmågebeslut behöver samordnas inom förmågan när flera konsumenter påverkas. Ett gemensamt beslut behövs när konsekvenserna går över flera förmågor eller när interoperabilitet, säkerhet, kostnad eller andra systemegenskaper kräver en gemensam riktning.

Detta är ett sätt att undvika både centralism och fragmentering.

Om beslut alltid flyttas uppåt blir den gemensamma nivån överlastad och långt från den konkreta kunskapen. Om beslut alltid lämnas lokalt upptäcker organisationen för sent att varje team har skapat olika kontrakt, olika identitetsmodeller eller olika sätt att hantera kritiska risker.

## Top-down för sammanhang, bottom-up för lärande

Etableringen behöver därför röra sig i två riktningar samtidigt.

Top-down behövs för att skapa sammanhang:

- gemensamma mål och begränsningar,
- principer,
- kvalitetsdimensioner,
- en första förmågestruktur,
- ansvarssnitt,
- spelregler för gemensamma artefakter.

Bottom-up behövs för att skapa realism:

- faktiska problem i produktteam,
- återkommande lokala mönster,
- plattformsfriktion,
- driftincidenter,
- svårigheter att möta kvalitetskrav,
- avsteg och teknisk skuld,
- erfarenheter från genomförda lösningar.

Den ena riktningen utan den andra är otillräcklig.

En enbart top-down-driven arkitektur riskerar att beskriva en idealvärld som ingen använder. En enbart bottom-up-driven arkitektur riskerar att katalogisera dagens lösningar utan att skapa en gemensam riktning.

Mognaden ligger i återkopplingen mellan dem.

## Undvik ett arkitekturvattenfall

Det är därför missvisande att tänka att modellen ska ”bli klar” innan den börjar användas.

En bättre etableringscykel är:

1. skapa en första gemensam modell,
2. välj ett fåtal prioriterade förmågor,
3. utveckla konkreta artefakter och erbjudanden,
4. använd dem i verkliga lösningar,
5. samla erfarenheter,
6. justera både förmågan och den övergripande modellen,
7. utöka till nästa prioriterade område.

Varje varv bör ge mer användbar arkitektur, inte bara mer dokumentation.

Det kan innebära att den första förmågekartan innehåller elva områden men att bara tre har mogna tjänstekataloger. Det är inte nödvändigtvis ett problem. Transparens om mognadsgrad är bättre än att skapa skenbar fullständighet.

## Börja där friktionen är hög

Var organisationen börjar beror på dess situation. Det finns ingen universell första förmåga.

En organisation med många integrationsproblem kan börja med integration och kommunikation. En organisation som moderniserar sin driftmiljö kan prioritera runtime, driftbarhet och programvaruleverans. En verksamhet med stora krav på spårbar handläggning kan behöva börja med process, regler, identitet och data.

Det gemensamma kriteriet är inte teknisk trendighet. Det är var bättre gemensam arkitektur kan ge tydlig verksamhetsnytta, riskreduktion eller utvecklingseffektivitet.

Detta ger också ett sätt att få legitimitet. Ett arkitekturinitiativ som tidigt löser verkliga problem har bättre förutsättningar att bli en del av vardagen än ett initiativ som först efter flera år producerar en komplett katalog.

## En konkret första leverans

För en organisation som börjar från ett ganska fragmenterat läge kan en rimlig första leverans vara betydligt mindre än hela modellen i denna bok.

Den kan bestå av:

- en dokumenterad begreppsmodell,
- fem till tio gemensamma arkitekturprinciper,
- ett antal gemensamma kvalitetsdimensioner,
- en första förmågekarta med tydliga gränsbeskrivningar,
- namngivna ansvariga för de mest prioriterade förmågorna,
- ett fåtal väl beskrivna lösningsmönster,
- några konsumerbara plattformstjänster där behovet redan är tydligt,
- tekniska standarder endast där konsekvensen faktiskt behövs,
- en eller två referensarkitekturer för vanliga lösningsklasser,
- en enkel mekanism för återkoppling, beslut och avsteg.

Det viktigaste är att delarna hänger ihop. En mindre modell där ett lösningsteam kan gå från behov till relevant förmåga, hitta ett mönster, förstå vilket plattformserbjudande som finns och se vilka standarder som gäller är mer värdefull än en mycket större dokumentmängd utan spårbarhet.

## Tecken på att ansvarsnivån är fel

Etableringen bör också kunna upptäcka när beslut hamnat på fel nivå.

Några typiska signaler på för hög centralisering är:

- små lokala teknikbeslut kräver central behandling,
- arkitekturforum blir köer för godkännande,
- standarder beskriver detaljer som saknar tvärgående konsekvens,
- lösningsteam väntar på centrala besked i frågor där de själva har bäst kunskap,
- gemensamma plattformar används trots att de inte möter behovet eftersom avsteg är för svåra.

Typiska signaler på för låg samordning är:

- samma problem löses på många olika sätt utan tydlig anledning,
- interoperabilitet kräver specialanpassning mellan varje par av system,
- identitet, loggning eller säkerhet byggs om från grunden i varje produkt,
- flera team upphandlar eller driver likvärdig infrastruktur,
- organisationen saknar gemensamt svar på produktlivscykel eller kritiska sårbarheter,
- ingen kan säga vem som ansvarar för ett tvärgående problem.

Arkitekturarbetet bör inte sträva efter mitten av en abstrakt skala. Det bör placera varje typ av beslut där kunskap, ansvar och konsekvenser bäst kan mötas.

## Mognad är inte mängden dokument

Det går att skapa många arkitekturartefakter utan att organisationen blir bättre på arkitektur.

En mognare modell kännetecknas snarare av att:

- ansvar är begripligt,
- återkommande problem fångas och löses på lämplig nivå,
- plattformserbjudanden har verkliga konsumenter,
- standarder har tydliga motiv,
- lösningsteam kan hitta och förstå relevant vägledning,
- kvalitetskrav går att spåra till tekniska egenskaper,
- avsteg ger lärande i stället för enbart administration,
- artefakter kan förändras utan att hela modellen behöver ritas om,
- lokala erfarenheter påverkar gemensamma beslut.

Det är därför rimligt att se arkitekturmognad som förmågan att fatta bättre sammanhängande beslut över tid, inte som hur komplett ett dokumentbibliotek är.

## Från etablering till fördjupning

Del I har nu byggt upp bokens grundmodell. Vi har gått från problemet med fragmentering och lokal optimering, via lager och spårbarhet, till behov, kvalitetsattribut, arkitekturbeslut och principer. I detta kapitel har dessa delar satts in i en praktisk etableringsordning och en ansvarmodell.

Nästa fråga blir mer precis: vad är egentligen en gemensam IT-förmåga?

För att kunna använda förmågekartan som den stabila delen av arkitekturen behöver vi skilja den från verksamhetsförmågor, tjänster, plattformar, organisatoriska team och produkter. Vi behöver också förstå varför vissa saker lämpar sig för gemensamt ansvar medan andra bör ligga nära verksamhetsdomänen.

Det är utgångspunkten för del II.
