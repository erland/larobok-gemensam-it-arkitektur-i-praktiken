# Förmåga: Arbetsplats, samarbete och produktivitet

> **Status:** Utkast  
> **Ansvarig:** Gemensam IT-arkitektur / stödjande IT-område  
> **Senast reviderad:** 2026-08-18

## 1. Syfte, omfattning och relationer

### 1.1 Syfte

Förmågan ska ge medarbetare och organisatoriska enheter gemensamma digitala verktyg för dokumentproduktion, kommunikation, samarbete, informationsdelning och personlig eller gemensam produktivitet.

Syftet är att ge en naturlig hemvist för generell arbetsplats-IT som Microsoft 365, Office, Teams, SharePoint, OneDrive och liknande tjänster utan att sammanblanda dessa med verksamhetsspecifika applikationer och plattformar.

Förmågan ska också stödja tydlig gränsdragning mellan generella produktivitetsverktyg och IT-stöd som förvaltar verksamhetsprocesser, verksamhetsinformation eller myndighetskritisk logik.

### 1.2 Omfattning

Förmågan omfattar bland annat:

- ordbehandling, kalkyl och presentation
- e-post och kalender
- chatt, möten och digital kommunikation
- samarbetsytor
- personliga och gemensamma dokumentytor
- dokumentdelning
- gemensam redigering
- versionshantering i produktivitetsverktyg
- intranätsnära samarbetsytor
- team- och projektarbetsytor
- produktivitetsassistenter
- generella low-code/no-code-verktyg där de används som produktivitetsstöd
- enklare automatisering av personliga eller administrativa arbetsflöden
- desktop- och webbklienter för produktivitetsverktyg
- offline- och mobil åtkomst där tjänsten stödjer detta

### 1.3 Utanför förmågan

Följande hör primärt hemma i andra förmågor:

- verksamhetsspecifika användargränssnitt och digitala kanaler – **Interaktion, presentation och kanaler**
- ärendehantering och verksamhetsworkflow – **Process, workflow och ärendehantering**
- system of record och primär verksamhetsdata – **Data- och informationshantering**
- BI och avancerad analys – **Analys, sökning och AI**
- identiteter och autentisering – **Identitet och tillit**
- integrationsplattformar och API:er – **Integration och kommunikation**
- utvecklingsverktyg och CI/CD – **Programvaruutveckling och leverans**

Generella produktivitetsverktyg ska inte bli system of record för kritisk verksamhetsinformation utan uttryckligt arkitekturbeslut och dokumenterat behov.

### 1.4 Relation till andra förmågor

**Interaktion, presentation och kanaler** ansvarar för verksamhetsspecifika gränssnitt, medan denna förmåga avser generella verktyg för personligt och gemensamt arbete.

**Data- och informationshantering** ansvarar för verksamhetsinformationens auktoritativa lagring och livscykel. Dokumentytor här är främst arbets- och samarbetsytor.

**Process, workflow och ärendehantering** används när arbetsflödet är en egentlig verksamhetsprocess med lång livscykel, spårbarhet eller ärendelogik.

**Analys, sökning och AI** kan tillhandahålla avancerad analys och AI-tjänster, medan produktivitetsassistenter kan konsumera dessa inom arbetsplatsverktyg.

**Identitet och tillit** ger åtkomstkontroll, federation och användaridentiteter.

---

## 2. Behov och användningsområden

### 2.1 Typiska behov

En medarbetare eller organisatorisk enhet kan behöva stöd för att:

- skapa dokument, kalkyler och presentationer
- samarbeta i realtid i dokument
- dela arbetsmaterial inom en grupp
- kommunicera via e-post, chatt och möten
- strukturera dokument och arbetsmaterial i teamytor
- arbeta mobilt eller på distans
- hantera gemensamma kalendrar
- automatisera enklare administrativa uppgifter
- använda AI-assistent för sammanfattning, textstöd eller sökning
- skapa tillfälliga projekt- eller samarbetsytor
- dela information med externa parter under kontrollerade former
- arbeta med gemensamma mallar och dokumentstandarder

### 2.2 Typiska användningsfall

#### Gemensam projektyta

En projektgrupp behöver dela dokument, mötesanteckningar, filer och uppgifter under projektets livstid.

#### Personligt dokumentarbete

En medarbetare skapar och redigerar dokument, kalkyler och presentationer som underlag för sitt arbete.

#### Samarbete med extern part

En arbetsgrupp behöver dela vissa dokument eller delta i digitala möten med extern organisation.

#### Produktivitetsassistent

En AI-baserad assistent används för att sammanfatta möten, formulera texter eller söka i användarens tillåtna arbetsmaterial.

#### Enkel administrativ automatisering

En användare eller grupp automatiserar ett enkelt godkännandeflöde eller informationsutskick som inte är en kärnverksamhetsprocess.

### 2.3 Centrala arkitekturfrågor

Utvecklings- eller förvaltningsområdet bör bland annat ta ställning till:

- Är behovet generell produktivitet eller ett verksamhetsspecifikt IT-stöd?
- Är informationen arbetsmaterial eller auktoritativ verksamhetsinformation?
- Behöver informationen långtidsbevaras?
- Vilken informationsklassning gäller?
- Får information delas externt?
- Vilken typ av extern samverkan krävs?
- Behövs offline- eller mobil åtkomst?
- När blir ett enkelt workflow till en riktig verksamhetsprocess?
- När blir en lista eller dokumentyta ett otillräckligt system of record?
- Vilka livscykel- och gallringskrav finns för arbetsytan?
- Hur hanteras ägarskap när personer byter roll eller lämnar organisationen?
- Hur ska produktivitetsassistenter få åtkomst till information?
- Vilka data får användas av externa AI-funktioner?
- Hur undviks skugg-IT eller oavsiktlig verksamhetskritisk lösning i generella verktyg?

---

## 3. Förmågespecifika arkitekturprinciper

Gemensamma principer finns i `../styrning/gemensamma-arkitekturprinciper.md`.

### P-ASP-01 Arbetsplatsverktyg för generell produktivitet

**Princip:**  
Gemensamma arbetsplats- och samarbetsverktyg ska användas för generell produktivitet och samarbete, inte som standardplattform för verksamhetsspecifik systemutveckling.

**Motivering:**  
Det minskar risken att kritiska verksamhetslösningar byggs utan rätt livscykel, testning och förvaltning.

### P-ASP-02 System of record ska vara tydligt

**Princip:**  
När information har verksamhetsmässig auktoritet ska det vara tydligt om arbetsplatsverktyget är system of record eller endast arbetsyta/kopia.

**Motivering:**  
Samarbetsytor skapar annars lätt parallella och otydliga informationskällor.

### P-ASP-03 Delning ska följa informationsbehov och klassning

**Princip:**  
Intern och extern delning ska styras utifrån informationens skyddsbehov och mottagarkrets.

**Motivering:**  
Produktivitetsverktyg gör delning enkelt, vilket kräver tydliga kontrollprinciper.

### P-ASP-04 Enkla automatiseringar ska hållas enkla

**Princip:**  
Low-code/no-code och personliga automationer bör användas för avgränsade produktivitetsbehov och inte oavsiktligt utvecklas till verksamhetskritiska system utan motsvarande styrning.

**Motivering:**  
Tekniken kan sänka tröskeln för att bygga lösningar men tar inte bort behov av arkitektur, säkerhet och förvaltning.

### P-ASP-05 Samarbetsytor ska ha livscykel

**Princip:**  
Team-, projekt- och dokumentytor ska ha definierat ägarskap och livscykel.

**Motivering:**  
Övergivna ytor skapar informationsrisk, kostnad och otydlighet.

### P-ASP-06 Produktivitets-AI ska respektera befintliga åtkomsträttigheter

**Princip:**  
AI-assistenter i arbetsplatsmiljön ska endast få använda information som användaren och tjänsten har rätt att komma åt.

**Motivering:**  
AI-funktionalitet får inte skapa nya genvägar runt behörighetsmodellen.

### P-ASP-07 Standardverktyg före lokala duplicat

**Princip:**  
Gemensamma produktivitets- och samarbetsverktyg bör användas före lokala alternativ när de uppfyller behovet.

**Motivering:**  
Det minskar kostnad, supportbörda och informationsfragmentering.

---

## 4. Krav och styrande riktlinjer

### KR-ASP-01 Godkända arbetsplatsverktyg

**Krav:**  
Organisationens arbetsrelaterade dokument, kommunikation och samarbetsytor ska hanteras i godkända tjänster när dessa stödjer behovet och informationsklassningen.

**Motivering/källa:**  
Säkerhet, förvaltningsbarhet och support.

### KR-ASP-02 Ägarskap för samarbetsytor

**Krav:**  
Gemensamma team-, projekt- och dokumentytor ska ha identifierad ägare eller ansvarig funktion.

**Motivering/källa:**  
Informationsförvaltning och livscykel.

### KR-ASP-03 Extern delning

**Krav:**  
Extern delning av information ska använda godkända mekanismer och följa tillämpliga regler för informationsklassning, mottagare och åtkomsttid.

**Motivering/källa:**  
Säkerhet och regelefterlevnad.

### KR-ASP-04 Verksamhetskritiska lösningar

**Krav:**  
Lösningar byggda i generella produktivitets- eller low-codeverktyg som blir verksamhetskritiska ska omfattas av motsvarande krav på ägarskap, testning, säkerhet, kontinuitet och livscykel som andra verksamhetssystem.

**Motivering/källa:**  
Risk och förvaltningsbarhet.

### KR-ASP-05 Informationslivscykel

**Krav:**  
Samarbetsytor som innehåller information med retention-, bevarande- eller gallringskrav ska ha definierad hantering för detta.

**Motivering/källa:**  
Regelefterlevnad och informationsförvaltning.

### KR-ASP-06 Personberoende ytor

**Krav:**  
Verksamhetsviktig gemensam information ska inte vara beroende av en enskild persons privata arbetsyta utan dokumenterad överlämnings- och ägarstruktur.

**Motivering/källa:**  
Kontinuitet och ansvar.

### KR-ASP-07 AI-assistent och skyddsvärd information

**Krav:**  
Produktivitetsassistenter får endast behandla information inom de användnings- och skyddsramar som är beslutade för tjänsten.

**Motivering/källa:**  
Säkerhet, informationsskydd och regelefterlevnad.

---

## 5. Guidelines och vägledning

### Microsoft Office som förmåga eller produkt?

Microsoft Office är en produkt-/tjänstesvit som realiserar delar av denna förmåga.

Behovet bör beskrivas som exempelvis:

- dokumentproduktion
- kalkyl
- presentation
- samarbete

inte som ett arkitekturkrav på "Office" i sig om annan tjänst skulle kunna uppfylla samma behov.

### Microsoft 365 som plattformserbjudande

Microsoft 365 kan ses som ett sammansatt SaaS-erbjudande som realiserar flera delar av förmågan, exempelvis:

- Office
- Teams
- SharePoint
- OneDrive
- Exchange
- produktivitets-AI

Det bör kunna länkas till flera plattform-/tjänstedokument utan att behöva pressas in som en enda homogen teknisk komponent.

### SharePoint/Teams eller verksamhetssystem?

SharePoint/Teams passar ofta för:

- arbetsmaterial
- samarbete
- dokumentdelning
- projekt- och teamytor
- enklare listor och koordinering

Överväg verksamhetssystem när behovet omfattar:

- komplex domänlogik
- långlivade ärenden
- höga transaktionsvolymer
- strikt system of record
- avancerad integration
- komplex behörighetsmodell
- hög tillgänglighet
- omfattande test- och releasekrav

### OneDrive eller gemensam dokumentyta?

OneDrive är främst personlig arbetsyta.

Gemensam information som ska leva oberoende av en individ bör normalt ligga i en gemensam yta med organisatoriskt ägarskap.

### När blir Power Automate ett verksamhetsworkflow?

En enkel produktivitetsautomation kan ligga här när den exempelvis:

- skickar påminnelser
- kopierar data mellan personliga verktyg
- hanterar enkel intern administrativ koordinering

När flödet får:

- lång livslängd
- verksamhetskritisk status
- komplexa regler
- många användare
- formella ärenden
- krav på audit och versionering

bör det bedömas mot **Process, workflow och ärendehantering**.

### Var passar Power Apps?

Power Apps kan realisera:

- enklare interna gränssnitt – relation till **Interaktion, presentation och kanaler**
- enklare produktivitetslösningar – relation till denna förmåga
- mer avancerade verksamhetsapplikationer – då behöver hela arkitekturen bedömas utifrån berörda förmågor

Produkten i sig ska alltså inte avgöra klassificeringen.

### Produktivitets-AI eller verksamhets-AI?

AI som hjälper en användare med:

- text
- mötesanteckningar
- sammanfattning
- generell sökning

kan höra hemma som produktivitetsfunktion här.

AI som klassificerar ärenden, gör riskbedömning eller påverkar verksamhetsbeslut hör primärt hemma i **Analys, sökning och AI**.

### Filserver eller samarbetsyta?

Traditionell filserver kan vara lämplig för vissa tekniska eller legacybehov, men mänskligt samarbete bör normalt bedömas mot modern samarbetsyta med:

- versionshantering
- åtkomstkontroll
- sökning
- metadata
- livscykel

Applikationsfiler hör däremot primärt hemma i **Data- och informationshantering**.

### När standardlösningen inte passar

Beskriv behovet i termer av:

- användargrupp
- samarbetsform
- informationsklassning
- extern delning
- retention
- mobil/offline
- dokumentvolym
- workflowkomplexitet
- system of record
- integrationsbehov
- verksamhetskritikalitet

Därefter bedöms om arbetsplatsplattformen räcker eller om ett verksamhetssystem behövs.

---

## 6. Plattformar och tjänsteerbjudanden

I detta steg identifieras kandidater. Detaljerade plattformsdokument skapas separat senare eller tidigare vid konkret behov.

| Erbjudande | Syfte | Lämpligt för | Möjlig realisering idag | Status |
|---|---|---|---|---|
| Productivity Suite | Dokument, kalkyl och presentation | generell personlig produktivitet | Microsoft Office / Microsoft 365 Apps | Kandidat |
| Collaboration and Meetings | Chatt, möten och teamsamarbete | intern och extern samverkan | Microsoft Teams | Kandidat |
| Team/Document Workspace | Gemensamma dokument- och samarbetsytor | team, projekt och informationsdelning | SharePoint | Kandidat |
| Personal Work Storage | Personlig fil- och arbetsyta | individuellt arbetsmaterial | OneDrive | Kandidat |
| Mail and Calendar | E-post och kalender | generell kommunikation och planering | Exchange Online eller motsvarande | Kandidat |
| Productivity AI Assistant | AI-stöd i produktivitetsmiljön | text, sammanfattning, sökning, mötesstöd | Microsoft 365 Copilot eller annan godkänd tjänst | Kandidat |
| Low-Code Productivity Platform | Enkel automation och interna lösningar | avgränsade produktivitetsbehov | Power Platform-komponenter | Kandidat |
| Shared File Service | Traditionell gemensam filyta | legacy-/specialbehov | Befintlig filserver eller annan realisering | Kandidat |

### Sammansatta plattformar

Microsoft 365 är ett exempel på ett **sammansatt SaaS-erbjudande** som realiserar flera av ovanstående tjänster.

Power Platform är ett exempel på en plattform som kan realisera flera förmågor och ska därför länkas till respektive förmåga utifrån användningsfallet, inte klassificeras enbart här.

---

## 7. Standarder och teknikval

| Standard/teknikval | Status | Tillämpning |
|---|---|---|
| Microsoft 365 / Office | Befintligt eller möjligt produktval att verifiera | produktivitets- och samarbetsverktyg |
| Teams | Befintligt eller möjligt produktval att verifiera | samarbete och möten |
| SharePoint | Befintligt eller möjligt produktval att verifiera | gemensamma arbetsytor |
| OneDrive | Befintligt eller möjligt produktval att verifiera | personlig arbetsyta |
| Power Platform governance | Kandidat | low-code/no-code och automation |
| Dokumentklassnings-/delningsstandard | Kandidat | dokument och samarbetsytor |
| Workspace lifecycle-standard | Kandidat | skapande, ägarskap och avveckling |
| Extern delningsstandard | Kandidat | extern åtkomst |
| Produktivitets-AI-policy | Kandidat | godkänd användning av AI-assistenter |
| Dokumentformatstandard | Kandidat | långsiktig interoperabilitet och utbyte |

Exakta licensplaner, produktversioner och tenantkonfigurationer ska dokumenteras separat.

---

## 8. Relaterade artefakter och kvalitetsdimensioner

### 8.1 Relevanta kvalitetsdimensioner

Särskilt viktiga dimensioner är:

- **Säkerhet och informationsskydd** – samarbetsverktyg förenklar delning och hanterar stora informationsmängder.
- **Tillgänglighet** – arbetsplatsverktyg är centrala för dagligt arbete.
- **Kontinuitet och återställningsförmåga** – viktig information får inte försvinna vid konto- eller tjänsteproblem.
- **Spårbarhet och verifierbarhet** – delning och åtkomst kan behöva kunna följas.
- **Regelefterlevnad** – retention, gallring, arkivering och extern delning är centrala frågor.
- **Tillgänglighet och användbarhet för användare** – arbetsplatsverktyg används av breda användargrupper.
- **Förvaltningsbarhet och förändringsbarhet** – tenant-, workspace- och appsprawl behöver kontrolleras.
- **Interoperabilitet och portabilitet** – dokumentformat och exportmöjligheter påverkar långsiktig användning.
- **Livscykel och hållbarhet** – SaaS-funktioner och licensmodeller förändras snabbt.
- **Kostnads- och resurseffektivitet** – licenser och duplicerade verktyg behöver styras.

### 8.2 Lösningsmönster

Identifierade kandidater:

- Personal Workspace
- Team Workspace
- Controlled External Collaboration
- Document Co-Authoring
- Workspace Lifecycle
- Information Promotion from Workspace to System of Record
- Low-Code Productivity Automation
- Productivity AI with Existing Permissions
- Shared Document Template
- Temporary Project Workspace

### 8.3 Plattformar

Identifierade kandidater:

- Productivity Suite
- Collaboration and Meetings
- Team/Document Workspace
- Personal Work Storage
- Mail and Calendar
- Productivity AI Assistant
- Low-Code Productivity Platform
- Shared File Service

### 8.4 Tekniska standarder

Identifierade kandidater:

- Microsoft 365/Office-standard
- Teams-standard
- SharePoint-standard
- OneDrive-standard
- Power Platform governance
- dokumentklassnings-/delningsstandard
- workspace lifecycle-standard
- extern delningsstandard
- produktivitets-AI-policy
- dokumentformatstandard

### 8.5 Kandidater till referensarkitekturer

Följande kandidater identifieras eller stärks:

- **Digital arbetsplats för intern användare**
- **Kontrollerad extern samarbetsyta**
- **Projektarbetsplats med definierad informationslivscykel**
- **Low-code-baserat internt produktivitetsstöd**
- **Produktivitets-AI i myndighetsmiljö**
- **Övergång från samarbetsyta till förvaltat verksamhetssystem**
- **Internt handläggningsstöd med koppling till arbetsplatsverktyg**

### 8.6 Teknisk dokumentation

När konkreta arbetsplats- och samarbetsplattformar dokumenteras bör teknisk referens exempelvis omfatta:

- tenantkonfiguration
- identitet och federation
- delningspolicy
- externa gäster
- retention
- DLP/informationsskydd
- workspace provisioning
- ägarskap
- klientkonfiguration
- mobil åtkomst
- offline
- AI-assistentkonfiguration
- Power Platform environments
- connectors
- tekniska begränsningar

---

## Arbetsanteckningar

### Identifierade kandidater

**Lösningsmönster**
- Personal Workspace
- Team Workspace
- Controlled External Collaboration
- Document Co-Authoring
- Workspace Lifecycle
- Information Promotion from Workspace to System of Record
- Low-Code Productivity Automation
- Productivity AI with Existing Permissions
- Shared Document Template
- Temporary Project Workspace

**Plattformar/tjänster**
- Productivity Suite
- Collaboration and Meetings
- Team/Document Workspace
- Personal Work Storage
- Mail and Calendar
- Productivity AI Assistant
- Low-Code Productivity Platform
- Shared File Service

**Tekniska standarder**
- Microsoft 365/Office
- Teams
- SharePoint
- OneDrive
- Power Platform governance
- dokumentklassnings-/delningsstandard
- workspace lifecycle-standard
- extern delningsstandard
- produktivitets-AI-policy
- dokumentformatstandard

**Referensarkitekturer**
- digital arbetsplats för intern användare
- kontrollerad extern samarbetsyta
- projektarbetsplats med definierad informationslivscykel
- low-code-baserat internt produktivitetsstöd
- produktivitets-AI i myndighetsmiljö
- övergång från samarbetsyta till förvaltat verksamhetssystem

**Gränsdragningsfrågor**
- när SharePoint/Power Platform-lösning blir ett verksamhetssystem
- hur dokumentytor ska relateras till formell arkivering och records management
- om e-post och kalender behöver egna tjänsteerbjudanden eller kan ingå i ett samlat Productivity Suite-erbjudande
- hur produktivitets-AI ska relateras till den gemensamma AI-förmågan
- hur traditionell filserver ska hanteras mot både denna förmåga och Data- och informationshantering
