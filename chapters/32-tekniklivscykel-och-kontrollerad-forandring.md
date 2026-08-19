# 32. Tekniklivscykel och kontrollerad förändring

Tekniska standarder behöver stabilitet för att skapa värde. Samtidigt är nästan all teknik föränderlig. Produkter får nya huvudversioner, gamla versioner lämnar support, säkerhetskrav skärps, nya arbetssätt blir möjliga och tidigare rimliga val kan bli dyra att bära vidare.

Det skapar en grundläggande spänning. Om organisationen byter riktning för ofta blir den gemensamma arkitekturen instabil och dyr. Om den förändras för långsamt blir standarderna i stället ett hinder som håller kvar lösningarna i teknik som inte längre är ändamålsenlig.

Tekniklivscykel handlar därför inte om att alltid välja det nyaste. Den handlar om att förändra teknikportföljen med tillräcklig framförhållning, tydliga beslut och kontrollerade övergångar.

Det är också viktigt att skilja detta från den bredare governancefrågan. I det här kapitlet ligger fokus på livscykeln för tekniker, produkter, versioner och närliggande standarder. Hur hela arkitekturmodellen förvaltas, hur mandat organiseras och hur gemensam governance fungerar över tid behandlas i kapitel 37.

## Stabil arkitektur kräver rörlig teknik

En av bokens bärande principer är separationen mellan stabil arkitektur och föränderlig teknik.

En förmåga som *Applikationsexekvering och runtime* kan vara relevant under mycket lång tid. Ett plattformserbjudande som *Container Application Platform* kan också leva länge som tjänstekoncept. Däremot kommer den konkreta produkten, huvudversionen, operativsystemet och konfigurationen bakom erbjudandet sannolikt att förändras betydligt snabbare.

Det går att beskriva som flera förändringstakter:

```text
Förmåga                         förändras långsamt
    ↓
Plattformstjänst                förändras vid behov
    ↓
Teknisk standard                förändras oftare
    ↓
Produkt och huvudversion        förändras snabbare
    ↓
Patchnivå och konfiguration     förändras kontinuerligt
```

Poängen är inte att varje lager alltid följer exakt denna takt. Poängen är att de inte bör vara hårt sammanbundna.

Om en förmågebeskrivning säger att organisationen erbjuder ”OpenShift version X” har en föränderlig produktdetalj byggts in i ett stabilt arkitekturlager. Om en produktstandard däremot anger vilken *containerplattform* som för närvarande är godkänd är förändringen placerad där den hör hemma.

Detta gör livscykelhantering möjlig utan att hela arkitekturmodellen behöver skrivas om vid varje teknikskifte.

## Livscykelstatus behöver vara explicit

En organisation behöver kunna uttrycka mer än bara ”standard” eller ”inte standard”.

En praktisk livscykelmodell kan exempelvis innehålla följande tillstånd:

1. Utforskas – tekniken undersöks men är inte rekommenderad för normal produktion.
2. Utvärderas – tekniken prövas kontrollerat i pilot eller begränsad användning.
3. Godkänd – tekniken får användas under angivna villkor, men är inte nödvändigtvis förstahandsval.
4. Rekommenderad – tekniken är ett aktivt förstahandsval inom definierad kontext.
5. Begränsad – ny användning bör normalt inte startas, men befintliga lösningar kan fortsätta under vissa villkor.
6. Deprecated – tekniken ska inte användas för nyutveckling och befintliga användare behöver planera migration.
7. Retired – tekniken är avvecklad som gemensamt stödd väg.

Detta är en praktisk modell för boken, inte en universell industristandard. Organisationen kan välja andra namn eller fler nivåer. Det viktiga är att statusen besvarar en praktisk fråga:

> Vad betyder det här tillståndet för den som ska fatta ett teknikbeslut i dag?

En status utan konsekvens är bara metadata.

Om ”deprecated” inte säger något om nyanvändning, support, migration eller tidsram blir begreppet för svagt för att styra beteende.

## Technology radar är karta, inte beslutsprotokoll

Många organisationer använder någon form av technology radar för att synliggöra teknikens status. En sådan radar kan vara värdefull eftersom den ger en snabb bild av exempelvis:

- tekniker som bör provas,
- tekniker som kan användas,
- tekniker som är rekommenderade,
- tekniker som bör undvikas eller fasas ut.

Men en radar bör inte bära all livscykelinformation själv.

En punkt i en radar kan säga *vilken riktning* organisationen har valt. Den förklarar sällan tillräckligt väl:

- varför statusen ändrades,
- vilket användningsområde beslutet gäller,
- vilka versioner som omfattas,
- hur länge support finns,
- vilka beroenden som påverkas,
- hur migrering ska ske,
- vem som äger beslutet.

Radarn fungerar därför bäst som navigerings- och kommunikationsyta ovanpå mer precisa artefakter.

```text
Technology radar
       ↓
Livscykelstatus
       ↓
Standard / produktbeslut
       ↓
Supportfönster och migrationsplan
       ↓
Teknisk referensdokumentation
```

Det minskar risken att en färgad ring eller etikett blir en förenklad ersättning för ett faktiskt arkitekturbeslut.

## Teknik, produkt och version har olika livscykler

En vanlig källa till förvirring är att flera saker behandlas som om de hade samma livscykel.

Ta en relationsdatabastjänst som exempel.

Organisationen kan samtidigt ha:

- relationsdatabas som långsiktigt relevant teknikprincip,
- en gemensam relationsdatabastjänst som aktiv plattformstjänst,
- en viss databasprodukt som rekommenderad realisering,
- produktens huvudversion 16 som stödd,
- huvudversion 14 som på väg ut ur support,
- specifika patchnivåer som hanteras operativt.

Om allt detta sammanfattas med formuleringen ”PostgreSQL är standard” förloras viktig information.

Livscykeln behöver därför kunna uttryckas på flera nivåer:

```text
Tjänst:      Relationsdatabastjänst        aktiv
Produkt:     Produkt A                     rekommenderad
Version:     v16                           rekommenderad
Version:     v15                           stödd
Version:     v14                           deprecated
Patch:       aktuell säkerhetsnivå         obligatorisk
```

Det gör det möjligt att förändra en del utan att automatiskt förändra de andra.

## End of support är en arkitektursignal

Leverantörens eller communityns supportdatum är inte bara en driftfråga.

När en version närmar sig slutet av sitt underhåll förändras lösningens riskprofil. Det kan påverka:

- säkerhetsuppdateringar,
- tillgång till felrättningar,
- leverantörsstöd,
- kompatibilitet med andra komponenter,
- möjligheten att uppfylla interna krav,
- kostnaden för särskild support,
- återställnings- och kontinuitetsförmåga.

Därför bör end-of-life och end-of-support användas som framåtblickande arkitektursignaler, inte som datum som upptäcks först när de passerats.

En mogen livscykelprocess frågar exempelvis:

> Vilka versioner lämnar normal support under de kommande 12, 24 och 36 månaderna?

Det gör att migration kan bli en planerad del av portfölj- och plattformsarbetet i stället för en akut teknisk händelse.

Samtidigt bör leverantörens datum inte ensamt styra organisationens status. En produkt kan behöva avvecklas tidigare därför att den inte längre passar arkitekturen. En organisation kan i vissa fall också bära en version under en övergångsperiod trots att den lämnat normal support, men då är det ett medvetet risk- och undantagsbeslut.

## Supportfönster är ett tjänstekontrakt

När en gemensam plattform erbjuder teknik till många konsumenter blir versionssupport en del av tjänstens kontrakt.

Konsumenterna behöver veta exempelvis:

- vilka huvudversioner som stöds,
- hur länge de normalt stöds,
- hur långt i förväg deprecation annonseras,
- vem som genomför plattformsuppgraderingen,
- vad konsumenten själv behöver ändra,
- vilka kompatibilitetskrav som gäller,
- vad som händer när supportfönstret stängs.

Det är inte tillräckligt att plattformsteamet vet detta internt.

För en Java-runtime kan tjänstekontraktet exempelvis skilja mellan:

- rekommenderad JDK-version för nya tjänster,
- äldre men fortfarande stödda versioner,
- versioner där endast migration stöds,
- versioner som inte längre får köras på den gemensamma plattformen.

Ett tydligt supportfönster hjälper lösningsteam att planera sin egen livscykel och minskar behovet av specialförhandlingar.

## Deprecation är början på en migration

En av de viktigaste principerna i tekniklivscykel är:

> Deprecation är inte slutet på ett beslut. Det är starten på ett förändringsarbete.

Att märka en teknik som deprecated utan att skapa en väg bort från den löser nästan inget.

Ett deprecationbeslut bör normalt kunna besvara:

- Vad är det som fasas ut?
- Varför?
- Gäller det nyanvändning, befintlig användning eller båda?
- Vilken rekommenderad ersättare finns?
- Vilka kända skillnader finns mellan gammal och ny väg?
- När upphör normal support?
- När måste migration vara klar?
- Vem ansvarar för plattformssidan av migrationen?
- Vem ansvarar för anpassning i konsumerande lösningar?
- Hur följs migrationen upp?

Detta gör deprecation till ett styrt övergångstillstånd i stället för en etikett på en katalogpost.

## Sunset behöver vara ett verkligt datum eller villkor

Begreppet *sunset* används ofta för den punkt då en gammal tjänst, version eller teknikväg inte längre ska vara tillgänglig.

För att vara användbart behöver det vara konkret.

Exempel:

```text
2027-03-01  Ny användning stoppas
2027-06-01  Automatisk migreringshjälp tillgänglig
2027-10-01  Normal support upphör
2028-01-31  Plattformsvägen stängs
```

I andra fall kan ett villkor vara mer relevant än ett fast datum, exempelvis att en gammal API-version avvecklas när samtliga identifierade konsumenter migrerat och en minsta observationsperiod passerat.

Poängen är att slutläget måste gå att planera mot.

Ett ”ska avvecklas framöver” utan datum, kriterium eller ägare blir lätt permanent teknisk skuld.

## Migration är en delad leverans

Teknikmigration beskrivs ibland som om ett plattformsteam bara behöver uppgradera den gemensamma komponenten. I praktiken finns ofta minst två förändringsytor:

```text
Plattformsförändring
       +
Konsumentanpassning
       =
Faktiskt teknikskifte
```

Exempelvis kan en ny runtimeversion kräva att plattformen:

- publicerar nya images,
- uppdaterar byggkedjan,
- förändrar basoperativsystem,
- erbjuder ny dokumentation,
- uppdaterar golden paths.

Samtidigt kan konsumenterna behöva:

- uppgradera bibliotek,
- ändra kod,
- köra regressionstester,
- justera konfiguration,
- verifiera prestanda,
- planera produktionssättning.

Därför bör en migrationsplan tydligt skilja mellan enablement och adoption.

Plattformen kan möjliggöra migrationen, men det innebär inte att alla konsumenter automatiskt är migrerade.

## Inventering före migration

Det är svårt att styra en tekniklivscykel om ingen vet var tekniken används.

Inför större förändringar behövs därför en rimlig inventering av exempelvis:

- konsumerande system,
- versioner,
- ägare,
- kritikalitet,
- beroenden,
- avvikelser från standardkonfiguration,
- uppskattad migrationskomplexitet.

Det betyder inte att organisationen måste bygga en perfekt CMDB innan något får förändras. Men för gemensamma plattformar bör konsumtionen vara tillräckligt spårbar för att besvara:

> Vilka påverkas om vi avslutar stödet för den här vägen?

Här blir de tidigare kapitlens plattformskatalog, självservice och automatisering viktiga. Om en plattform konsumeras deklarativt kan mycket av inventeringen komma från faktisk konfiguration och telemetri i stället för manuella kalkylblad.

## Migration behöver risksegmenteras

Alla konsumenter bör inte nödvändigtvis migreras på samma sätt eller samtidigt.

En praktisk segmentering kan ta hänsyn till:

- verksamhetskritikalitet,
- teknisk komplexitet,
- förändringstakt,
- regulatoriska beroenden,
- testbarhet,
- integrationsyta,
- data- och återställningsrisk.

Ett mindre internt verktyg kan exempelvis vara lämpligt som tidig pilot. Ett mycket kritiskt verksamhetssystem kan behöva vänta tills plattform, stödmaterial och erfarenheter är mer mogna.

En sådan ordning gör det möjligt att använda tidiga migreringar för lärande utan att göra de mest riskfyllda systemen till försökskaniner.

## Kompatibilitet minskar migrationskostnad

Tekniklivscykel är lättare att hantera när plattformar och standarder utformas för förändring från början.

Exempel på sådana egenskaper är:

- tydliga API- och tjänstekontrakt,
- versionerade gränssnitt,
- bakåtkompatibla förändringar där det är rimligt,
- automatiserade kompatibilitetstester,
- reproducerbara builds,
- automatiserade regressionstester,
- separation mellan konfiguration och kod,
- observerbarhet som gör regressionsrisk synlig,
- portabilitet där den har verkligt värde.

Detta betyder inte att all teknik måste vara utbytbar utan kostnad. Den typen av full abstraktion kan bli dyr och minska nyttan av plattformen.

Målet är snarare kontrollerbar förändringskostnad.

## Versioner bör inte leva för evigt

En till synes konsumentvänlig strategi är att stödja många versioner under mycket lång tid.

Problemet är att varje extra version kan multiplicera:

- säkerhetsarbete,
- testmatriser,
- dokumentation,
- kompetensbehov,
- driftvarianter,
- felsökningsvägar,
- beroendekombinationer.

Det kan skapa ett läge där plattformen lägger en stor del av sin kapacitet på historisk kompatibilitet i stället för att förbättra det aktuella erbjudandet.

Livscykelstyrning behöver därför balansera två kostnader:

```text
Kostnad för migration
        ↕
Kostnad för fortsatt variation
```

Det finns inget universellt optimalt supportfönster. Men organisationen bör kunna förklara varför fönstret ser ut som det gör och vilken typ av konsumentbehov det är avsett att stödja.

## En standard kan vara aktiv även när en produkt byts

Tekniklivscykeln visar varför standardnivåerna i kapitel 31 är viktiga.

Anta att organisationen har följande:

- API:er ska beskrivas maskinläsbart,
- ett gemensamt API Management-erbjudande används,
- produkt A är dagens standardprodukt.

Om produkt A ska ersättas av produkt B behöver inte den övergripande API-standarden avvecklas. Inte heller behöver API Management som tjänstekoncept försvinna.

Förändringen kan koncentreras till produkt- och realiseringslagret.

```text
API-standard                  består
API Management-tjänst         består
Produkt A                     deprecated
Produkt B                     rekommenderad
```

Det är precis denna separation som gör en gemensam arkitektur långsiktigt förvaltningsbar.

## Experiment behöver exit-kriterier

Kapitel 31 beskrev behovet av en kontrollerad experimentväg. Tekniklivscykeln behöver också beskriva hur experiment lämnas.

Ett experiment bör inte bli ett permanent specialfall bara för att ingen fattar nästa beslut.

Redan när tekniken börjar utvärderas bör det finnas kriterier för möjliga utfall:

### Gå vidare

Tekniken löser ett identifierat problem och har tillräckligt stöd för att gå vidare till pilot, godkänd eller rekommenderad status.

### Fortsätt utvärdera

Det finns fortfarande relevant osäkerhet och ett tydligt nästa lärandemål.

### Avsluta

Tekniken ger inte tillräcklig nytta, uppfyller inte kvalitetskrav eller är olämplig för organisationens kontext.

Ett avslutat experiment behöver också städas:

- testmiljöer tas bort,
- data raderas eller hanteras enligt livscykelkrav,
- temporära identiteter stängs,
- specialkonfiguration avvecklas,
- dokumenterade lärdomar bevaras.

Det gör experiment till en kontrollerad del av teknikportföljen i stället för en dold källa till nya permanenta teknikvarianter.

## Introduktion bör börja med ett problem

Precis som kapitel 3 argumenterade för behov före teknik bör ny teknik inte få plats i portföljen bara för att den är intressant.

En kandidat bör kunna kopplas till ett problem eller en möjlighet, exempelvis:

- dagens plattform uppfyller inte ett viktigt kvalitetskrav,
- en nuvarande produkt närmar sig slutet av support,
- kostnaden för dagens lösning är oproportionerlig,
- återkommande lokala speciallösningar visar ett saknat gemensamt behov,
- en ny teknik kan väsentligt förenkla leverans eller drift,
- ett nytt regulatoriskt krav kräver annan funktionalitet.

Detta ger en bättre utgångspunkt för utvärdering än frågan:

> Är den nya tekniken bra?

Den mer användbara frågan är:

> Är den bättre för vårt identifierade behov, givet våra kvalitetskrav, kostnader och migrationskonsekvenser?

## Införande behöver kvalitetsgrindar

Att en teknik fungerar i ett proof of concept innebär inte att den är redo som gemensam standard eller plattformskomponent.

För att gå från utvärdering till bredare användning kan organisationen behöva verifiera områden som:

- säkerhet,
- driftbarhet,
- supportmodell,
- backup och återställning,
- observerbarhet,
- kapacitet och skalning,
- kostnadsmodell,
- kompetenstillgång,
- licens- och avtalsfrågor,
- integrationsförmåga,
- automatiserad leverans,
- livscykel och exitmöjlighet.

Vilka kriterier som är relevanta beror på tekniken. En IDE-plugin behöver inte samma analys som en databasplattform.

Principen är proportionalitet: ju större gemensam konsekvens tekniken får, desto starkare behöver introduktionsbeslutet vara.

## Teknisk skuld kan vara ett medvetet övergångstillstånd

Under en migration kommer organisationen ofta att bära både gammal och ny teknik samtidigt.

Det är inte automatiskt ett misslyckande. Parallella vägar kan vara en rationell kostnad för kontrollerad förändring.

Problemet uppstår när övergången saknar slutpunkt.

Det är därför användbart att skilja mellan:

- avsiktlig övergångsskuld – gammal teknik finns kvar under en planerad migration,
- permanent oavsiktlig variation – gammal teknik lever vidare utan aktivt beslut.

Den första kan vara sund. Den andra tenderar att växa.

Ett bra livscykelbeslut gör övergångsskulden synlig genom ägare, tidsram och exitkriterium.

## Tidsbegränsade undantag hör ihop med livscykeln

En lösning kan ibland inte följa den rekommenderade livscykeln.

Exempelvis kan ett system:

- vara beroende av en tredjepartsprodukt som ännu inte stödjer nästa version,
- stå inför en nära förestående avveckling där migration inte är ekonomiskt rimlig,
- ha regulatoriska begränsningar för förändringstidpunkt,
- kräva en längre testperiod på grund av verksamhetskritikalitet.

Då kan ett tidsbegränsat undantag vara bättre än att låtsas att standarden följs.

Ett sådant undantag bör beskriva:

- varför migration inte sker enligt normal plan,
- vilken risk som accepteras,
- vilka kompensatoriska åtgärder som behövs,
- vem som äger risken,
- hur länge undantaget gäller,
- vilket nästa beslutstillfälle är.

Det är viktigt att undantaget inte automatiskt flyttar den gemensamma teknikens status bakåt. En gammal version kan vara deprecated även om vissa konsumenter har godkända övergångsundantag.

## Avveckling är mer än att sluta supportera

En teknik är inte fullt avvecklad bara för att standarddokumentet markerats som retired.

En faktisk avveckling kan kräva att organisationen:

- verifierar att inga aktiva konsumenter återstår,
- stoppar ny provisionering,
- stänger tjänsteendpoints,
- tar bort artefakter och images,
- avslutar licenser eller avtal,
- avvecklar identiteter och certifikat,
- hanterar kvarvarande data,
- rensar dokumentation och golden paths,
- tar bort monitoring och backupjobb,
- uppdaterar referensarkitekturer och standardkatalog,
- dokumenterar vad som ersatt tekniken.

Det finns alltså en skillnad mellan beslutad retirement och tekniskt slutförd retirement.

Det bör gå att se vilken av dessa två punkter som avses.

## Livscykelmetadata behöver vara maskinläsbar där det ger värde

När teknikportföljen växer blir det svårt att hålla status manuellt i fristående dokument.

Vissa metadata lämpar sig därför väl för strukturerad hantering, exempelvis:

- status,
- ägare,
- rekommenderad version,
- stödda versioner,
- deprecationdatum,
- sunsetdatum,
- ersättande teknik,
- berörda förmågor,
- länk till standard,
- länk till migrationsguide.

Det kan möjliggöra automatiska vyer som:

- vilka tekniker närmar sig sunset?
- vilka lösningar använder deprecated versioner?
- vilka golden paths genererar fortfarande gammal teknik?
- vilka plattformar saknar publicerad livscykel?

Det innebär inte att hela arkitekturen ska reduceras till metadata. Rationale, avvägningar och migrationskontext behöver fortfarande mänskligt begriplig dokumentation.

Men maskinläsbara livscykeldata gör styrningen mer operativ.

## Automatisk styrning bör följa livscykeln

När en teknik går genom livscykeln bör även verktygen förändras.

Ett möjligt förlopp är:

### Rekommenderad

- finns i standardtemplates,
- erbjuds via självservice,
- används av golden paths,
- kontrolleras automatiskt som normal väg.

### Begränsad

- befintliga konsumenter stöds,
- ny provisionering kräver motivering,
- templates pekar inte längre dit.

### Deprecated

- ny användning blockeras eller varnas tydligt,
- migrationsinformation visas,
- automatiska rapporter identifierar kvarvarande konsumenter.

### Retired

- provisionering är avstängd,
- artefakter och pipelines har städats,
- endast historisk dokumentation återstår där den behövs.

På detta sätt blir livscykeln inte bara en katalogstatus utan en förändring i den faktiska konsumtionsupplevelsen.

## Kostnaden för förändring behöver synliggöras

Teknikbyte har nästan alltid en kostnad. Den kan ligga hos olika aktörer:

- plattformsteamet,
- lösningsteamen,
- driftorganisationen,
- verksamheten genom test och produktionsrisk,
- upphandling/licens,
- utbildning och kompetensutveckling.

Om den gemensamma arkitekturen bara räknar plattformens egen kostnad kan ett teknikskifte se billigare ut än det är.

Samtidigt finns en kostnad för att inte förändra:

- ökande supportkostnad,
- säkerhetsrisk,
- kompetensbrist,
- sämre utvecklarupplevelse,
- minskad automation,
- tekniska begränsningar,
- dyrare framtida migrering.

Tekniklivscykel är därför ett ekonomiskt beslut lika mycket som ett tekniskt. Kapitel 33 fördjupar kostnad, kapacitet och incitament som arkitekturfrågor.

## Ansvar på tre nivåer

Bokens tredelade ansvarmodell passar särskilt väl för tekniklivscykel.

### Gemensam arkitekturnivå

Den gemensamma nivån bör definiera spelregler som behöver vara konsekventa över flera förmågor:

- gemensam livscykelmodell,
- betydelsen av statusar,
- minsta metadata,
- principer för deprecation och sunset,
- hur undantag och riskacceptans kopplas till livscykeln,
- hur tvärgående beroenden hanteras,
- hur större teknikskiften påverkar referensarkitekturer och gemensamma standarder.

Den gemensamma nivån bör däremot inte behöva besluta varje versionsuppgradering.

### Förmågenivå

Förmågeansvaret bör äga teknikportföljen inom sitt område.

Det kan innebära att:

- följa externa supportfönster,
- utvärdera nya tekniker,
- föreslå statusförändringar,
- planera plattforms- och produktmigrationer,
- publicera rekommenderade versioner,
- ge konsumenterna framförhållning,
- följa adoption och kvarvarande gammal teknik.

Det är här mycket av den praktiska livscykelhanteringen bör ske.

### Lösnings-/produktnivå

Lösningsteamen ansvarar för sin faktiska konsumtion.

De behöver:

- känna till vilka versioner och tekniker de använder,
- planera migration inom annonserade fönster,
- testa sina lösningar mot nya versioner,
- undvika att introducera ny användning av deprecated teknik,
- begära tidsbegränsat undantag när migration inte är rimlig,
- ge återkoppling om migrationsproblem och dolda beroenden.

Det gör tekniklivscykeln till ett delat ansvar med tydliga gränser, inte ett centralt uppgraderingsprojekt som någon annan förväntas lösa.

## En praktisk livscykelprocess

En återkommande process kan beskrivas i nio steg:

1. Observera – följ supportfönster, problem, nya behov och teknikutveckling.
2. Identifiera drivkraft – vilket problem eller vilken risk motiverar förändring?
3. Utvärdera – pröva kandidater mot behov, kvalitetskrav och konsekvenser.
4. Besluta status – välj exempelvis utvärderad, godkänd eller rekommenderad.
5. Produktifiera vägen – uppdatera standard, plattform, golden path och dokumentation.
6. Annons­era övergång – publicera deprecation, supportfönster och målstatus med framförhållning.
7. Migrera – möjliggör och följ adoption hos konsumenterna.
8. Verifiera retirement – säkerställ att beroenden, data, artefakter och driftmekanismer är avvecklade.
9. Lär – använd erfarenheter för att förbättra nästa teknikskifte.

Processen behöver inte vara tung för varje teknik. Förändringens räckvidd bör styra hur formell den behöver vara.

## Några vanliga anti-patterns

### Evig preview

En teknik har status ”pilot” eller ”under utvärdering” i flera år men används ändå i produktion av många team.

Problemet är inte namnet utan att organisationen undviker att fatta ett riktigt beslut om stöd, ansvar och framtid.

### Deprecated utan migrationsväg

En standard markeras som gammal, men det finns ingen ersättare, dokumentation eller kapacitet att hjälpa konsumenterna vidare.

Statusen skapar då skuld utan att skapa förändring.

### Sunset utan inventering

Ett datum beslutas utan att organisationen vet vilka konsumenter som påverkas.

Det leder ofta till sena undantag och uppskjutna datum.

### Stöd för allt

Plattformen fortsätter stödja varje historisk version för att undvika konflikt med konsumenterna.

Resultatet blir ökande variation, kostnad och minskad förändringsförmåga.

### Upgrade by surprise

Gemensam teknik uppgraderas med kort framförhållning och konsumenterna förväntas anpassa sig omedelbart.

Det flyttar plattformens planeringsproblem till lösningsteamen och underminerar tilliten till den gemensamma vägen.

### Technology radar utan ägare

Tekniker flyttas mellan ringar eller kategorier, men ingen äger supportfönster, migrationsplan eller faktisk konsumtion.

Radarn blir då mer kommunikationsgrafik än styrinstrument.

### Ny standard före ny väg

Den gamla tekniken förbjuds innan den nya tekniken finns tillgänglig genom plattform, dokumentation och support.

Det skapar ett styrglapp där teamen förväntas följa en standard de praktiskt inte kan konsumera.

## En praktisk analysordning

När en teknik eller produkt behöver förändra livscykelstatus kan följande frågor användas:

1. Vilken artefakt förändras? Teknik, produkt, version, plattformstjänst eller standard?
2. Vad driver förändringen? Support, säkerhet, kvalitet, kostnad, behov eller strategisk riktning?
3. Vilka konsumenter och beroenden påverkas?
4. Vilken målstatus ska tekniken få?
5. Finns en rekommenderad ersättare eller krävs fortsatt utvärdering?
6. Vilka kvalitetskrav måste den nya vägen verifiera?
7. Vad behöver plattformen göra för att möjliggöra förändringen?
8. Vad behöver konsumerande lösningar göra?
9. Vilket supportfönster och vilket sunsetvillkor är rimligt?
10. Hur hanteras legitima undantag?
11. Hur mäts faktisk migration och kvarvarande användning?
12. Vilka artefakter och automationer måste uppdateras när statusen ändras?

Om organisationen inte kan besvara dessa frågor är det ofta för tidigt att kommunicera en definitiv retirement eller att göra den nya tekniken till gemensam standard.

## Kontrollerad förändring i stället för frusen standardisering

Målet med tekniklivscykel är inte maximal förändringstakt. Det är inte heller maximal stabilitet.

Målet är förutsägbar förändring.

En välfungerande modell gör det möjligt att samtidigt säga:

- den här tekniken är stabil och rekommenderad i dag,
- vi vet vilka signaler som kan göra att den omprövas,
- vi följer externa och interna livscykelrisker,
- vi kan introducera alternativ kontrollerat,
- konsumenterna får rimlig framförhållning,
- en deprecated väg har en faktisk migrationsplan,
- gamla vägar kan slutligen stängas.

Det är först då standardisering och förändringsförmåga slutar vara motsatser.

```text
Stabil standard i nuet
        +
Tydlig livscykel
        +
Kontrollerad experimentväg
        +
Planerad migration
        =
Långsiktigt förändringsbar arkitektur
```

Nästa kapitel fördjupar en annan kraft som påverkar nästan alla dessa beslut: ekonomi, kostnad och kapacitet. En teknik kan vara funktionellt lämplig och arkitekturellt välstrukturerad men ändå skapa fel incitament eller oproportionerliga gemensamma kostnader. Därför behöver även ekonomin göras till ett explicit arkitekturperspektiv.
