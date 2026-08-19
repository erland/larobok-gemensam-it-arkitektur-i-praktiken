# Förmåga: Analys, sökning och AI

> **Status:** Utkast  
> **Ansvarig:** Gemensam IT-arkitektur / stödjande IT-område  
> **Senast reviderad:** 2026-08-18

## 1. Syfte, omfattning och relationer

### 1.1 Syfte

Förmågan ska ge utvecklingsområden stöd för att söka, sammanställa, analysera och dra slutsatser från information samt använda maskininlärning och generativ AI på ett kontrollerat, återanvändbart och förvaltningsbart sätt.

Syftet är att skapa en gemensam struktur för behov som går utöver primär datahantering, exempelvis informationssökning, rapportering, prediktion, klassificering, språkmodeller och agentbaserade funktioner.

Förmågan ska samtidigt tydligt skilja mellan:

- primär datahantering
- deterministiska verksamhetsregler
- analytisk bearbetning
- probabilistisk AI/ML-baserad inferens

### 1.2 Omfattning

Förmågan omfattar bland annat:

- informationssökning och indexering
- fulltextsökning
- rapportering och dashboards
- Business Intelligence
- analytiska datamodeller
- dataanalys
- statistisk analys
- maskininlärning
- klassificering och prediktion
- modellträning och modellinferens
- generativ AI
- stora språkmodeller
- embeddings och semantisk sökning
- Retrieval-Augmented Generation (RAG)
- prompt- och modellhantering
- AI-agentplattformar
- modellutvärdering
- kvalitetsmätning för AI
- human-in-the-loop
- guardrails och begränsning av AI-beteende
- spårbarhet och observability för AI-tjänster

### 1.3 Utanför förmågan

Följande hör primärt hemma i andra förmågor:

- primär persistens, databaser, filer och informationslivscykel – **Data- och informationshantering**
- explicita verksamhetsregler och beslutstabeller – **Regler och beslut**
- processorkestrering och human workflow – **Process, workflow och ärendehantering**
- API:er, events och transport av data – **Integration och kommunikation**
- användargränssnitt för analys eller AI – **Interaktion, presentation och kanaler**
- identiteter och behörigheter – **Identitet och tillit**
- exekveringsmiljöer för modeller eller analysjobb – **Applikationsexekvering och runtime**
- generell övervakning och drift – **Driftbarhet och motståndskraft**

### 1.4 Relation till andra förmågor

**Data- och informationshantering** tillhandahåller primära informationskällor, medan denna förmåga använder kopior, index, modeller och analytiska strukturer för att söka, analysera eller härleda nya resultat.

**Regler och beslut** används när ett beslut kan uttryckas explicit och deterministiskt. Denna förmåga används när resultatet bygger på statistisk analys, ML eller generativ AI.

**Integration och kommunikation** används för att exponera analys-, sök- och AI-tjänster samt för att hämta data från andra system.

**Interaktion, presentation och kanaler** används för dashboards, sökgränssnitt, assistenter och andra användarnära funktioner.

**Process, workflow och ärendehantering** kan använda analys- eller AI-resultat som indata, men processens styrning bör hållas separat från modellens inferens.

---

## 2. Behov och användningsområden

### 2.1 Typiska behov

Ett utvecklingsområde kan behöva stöd när ett IT-stöd ska:

- erbjuda fulltextsökning i stora informationsmängder
- skapa dashboards och verksamhetsrapportering
- analysera trender eller avvikelser
- klassificera ärenden eller dokument
- förutsäga utfall eller risk
- generera text eller sammanfattningar
- söka semantiskt i dokument
- använda RAG över interna kunskapskällor
- använda en AI-assistent för användarstöd eller produktivitet
- anropa en gemensam LLM-tjänst
- använda AI-agent som utför flera kontrollerade steg
- utvärdera modeller innan produktionssättning
- följa upp modellkvalitet över tid
- kombinera explicita regler med AI-baserade bedömningssignaler

### 2.2 Typiska användningsfall

#### Fulltextsökning i verksamhetsinformation

Information från ett eller flera system indexeras i en separat söktjänst för snabb och flexibel sökning.

#### Operativ dashboard

Verksamhetsdata sammanställs och visualiseras för uppföljning av exempelvis volymer, ledtider eller utfall.

#### Klassificeringsmodell

En modell bedömer vilken kategori ett dokument eller ärende sannolikt tillhör och returnerar sannolikhet eller klass.

#### Generativ AI-assistent

En språkmodell används för att sammanfatta, formulera eller ge stöd utifrån definierade informationskällor.

#### RAG-baserad kunskapstjänst

En språkmodell kombineras med sökning i godkända interna dokument för att ge mer faktabaserade svar.

#### AI-baserat beslutsstöd

En modell ger en rekommendation eller riskindikator som sedan används av människa eller regelbaserad beslutstjänst.

### 2.3 Centrala arkitekturfrågor

Utvecklingsområdet bör bland annat ta ställning till:

- Är behovet sökning, rapportering, analys, ML eller generativ AI?
- Vilken information används som källa?
- Är källdata auktoritativ eller en sekundär kopia?
- Hur färska måste data vara?
- Behöver resultatet vara deterministiskt?
- Hur ska osäkerhet eller sannolikhet hanteras?
- Måste resultat kunna förklaras?
- Hur ska modell- eller promptversion spåras?
- Vilka data får användas för träning, inferens eller promptning?
- Får data lämna myndighetens tekniska miljö eller jurisdiktion?
- Krävs human-in-the-loop?
- Vad händer om modellen ger felaktigt, osäkert eller olämpligt resultat?
- Hur mäts kvalitet före och efter produktionssättning?
- Hur upptäcks modell- eller datadrift?
- Vilka kostnads- och kapacitetskrav finns?
- Hur undviks att AI-genererat innehåll behandlas som verifierad fakta utan kontroll?

---

## 3. Förmågespecifika arkitekturprinciper

Gemensamma principer finns i `../styrning/gemensamma-arkitekturprinciper.md`.

### P-ASA-01 Analyskopior och index ska inte bli otydliga system of record

**Princip:**  
Sökindex, analyslager och modellfeatures ska ha tydliga källor och ska inte oavsiktligt behandlas som primära verksamhetsdata.

**Motivering:**  
Sekundära representationer har ofta annan uppdateringsfrekvens, kvalitet och livscykel än källsystemet.

### P-ASA-02 Deterministiska och probabilistiska resultat ska hållas isär

**Princip:**  
AI- och ML-resultat ska inte beskrivas eller behandlas som deterministiska regler när de i själva verket bygger på sannolikhet eller modellinferens.

**Motivering:**  
Det påverkar förklarbarhet, risk, testning och hur resultatet får användas i verksamheten.

### P-ASA-03 AI ska användas där tekniken ger tydlig nytta

**Princip:**  
AI ska införas när den löser ett identifierat behov bättre än enklare och mer förutsägbara alternativ.

**Motivering:**  
AI innebär ofta högre komplexitet kring data, risk, kostnad, kvalitet och förvaltning.

### P-ASA-04 Informationskällor ska vara tydliga

**Princip:**  
AI-, sök- och analyslösningar ska kunna beskriva vilka informationskällor de använder och vilken aktualitet och kvalitet dessa har.

**Motivering:**  
Resultatkvalitet kan inte bedömas utan förståelse för källdata.

### P-ASA-05 Mänsklig kontroll ska användas när konsekvensen kräver det

**Princip:**  
Human-in-the-loop ska användas när felaktiga AI-resultat kan få betydande verksamhetsmässiga, rättsliga eller säkerhetsmässiga konsekvenser.

**Motivering:**  
Automatiseringens nivå ska vara proportionerlig mot risk.

### P-ASA-06 Modeller, prompts och kunskapskällor ska livscykelhanteras

**Princip:**  
Modellversioner, promptmallar, embeddingmodeller och centrala kunskapskällor ska behandlas som förvaltningsbara artefakter när de påverkar verksamhetsutfall.

**Motivering:**  
Förändringar kan påverka resultat även utan förändring i traditionell applikationskod.

### P-ASA-07 Genererade svar ska inte ges högre tillit än underlaget medger

**Princip:**  
AI-genererat innehåll ska presenteras och användas med hänsyn till modellens och källornas osäkerhet.

**Motivering:**  
Språkmodeller kan producera övertygande men felaktigt innehåll.

---

## 4. Krav och styrande riktlinjer

### KR-ASA-01 Identifierade informationskällor

**Krav:**  
Produktionssatta analys-, sök- och AI-lösningar ska dokumentera sina väsentliga informationskällor och hur dessa uppdateras.

**Motivering/källa:**  
Spårbarhet, datakvalitet och förvaltningsbarhet.

### KR-ASA-02 Informationsskydd vid AI-användning

**Krav:**  
Data som skickas till AI- eller analystjänster ska hanteras enligt informationsklassning och myndighetens säkerhetskrav, inklusive regler för externa tjänster.

**Motivering/källa:**  
Säkerhet, regelefterlevnad och informationsskydd.

### KR-ASA-03 Modell- och promptversionering

**Krav:**  
När modell, prompt eller annan AI-konfiguration kan påverka ett verksamhetsmässigt viktigt resultat ska relevant version kunna identifieras.

**Motivering/källa:**  
Spårbarhet och verifierbarhet.

### KR-ASA-04 Kvalitetsutvärdering före produktionssättning

**Krav:**  
AI-/ML-lösningar med verksamhetsmässig betydelse ska ha definierade kvalitetsmått och verifieras före produktionssättning.

**Motivering/källa:**  
Korrekthet, riskhantering och förvaltningsbarhet.

### KR-ASA-05 Fel- och fallbackbeteende

**Krav:**  
Lösningar som är beroende av AI- eller analystjänster ska definiera hur de beter sig vid timeout, otillgänglighet, låg säkerhet eller otillförlitligt resultat.

**Motivering/källa:**  
Kontinuitet och robusthet.

### KR-ASA-06 Källhänvisning där användningsfallet kräver det

**Krav:**  
RAG- eller kunskapsbaserade lösningar ska kunna presentera eller logga relevanta källor när detta krävs för verifierbarhet eller användartillit.

**Motivering/källa:**  
Spårbarhet och verifierbarhet.

### KR-ASA-07 Sekundära sök- och analyslager

**Krav:**  
Sökindex, datamarts och andra sekundära representationer ska ha definierad källa, synkroniseringsmodell och återuppbyggnadsstrategi.

**Motivering/källa:**  
Korrekthet och driftbarhet.

### KR-ASA-08 Automatiserade beslut

**Krav:**  
AI-/ML-resultat får inte ensamt användas för automatiserade verksamhetsbeslut med betydande konsekvens utan att tillämpliga krav på rättslig grund, risk, förklarbarhet och kontroll är utredda och uppfyllda.

**Motivering/källa:**  
Regelefterlevnad, risk och rättssäkerhet.

---

## 5. Guidelines och vägledning

### Elasticsearch som söktjänst eller primär databas?

Elasticsearch är normalt lämpligt som sök- och indexeringslager när:

- fulltextsökning är central
- komplex filtrering och relevansrankning behövs
- stora informationsmängder behöver indexeras
- sökmodellen kan återuppbyggas från källsystem

Det bör inte automatiskt användas som system of record enbart för att det tekniskt kan lagra data.

### När passar Power BI?

Power BI är lämpligt när verksamheten behöver:

- dashboards
- interaktiv analys
- rapportering
- visuella sammanställningar
- självbetjäning inom kontrollerade informationsramar

Bedöm särskilt datakällor, uppdateringsfrekvens, informationsklassning och publiceringsmodell.

### Rapportering eller operativ funktion?

Rapportering och BI bör inte ersätta verksamhetsapplikationens operativa funktioner.

Om användaren behöver agera direkt på aktuell verksamhetsdata kan en applikationsvy eller särskild tjänst vara mer lämplig än en BI-rapport.

### När bör generativ AI användas?

Överväg generativ AI när uppgiften exempelvis handlar om:

- sammanfattning
- textgenerering
- semantisk sökning
- informationsassistans
- naturligt språk som gränssnitt

Undvik att använda LLM som ersättning för enkel deterministic logik, traditionell sökning eller regelmotor när dessa ger säkrare och billigare resultat.

### När behövs RAG?

RAG är lämpligt när en språkmodell behöver använda myndighetsspecifik eller aktuell information som inte kan förväntas finnas korrekt i modellens grundträning.

Definiera:

- godkända källor
- indexeringsprocess
- åtkomstkontroll
- metadata
- aktualitet
- hur källor presenteras
- hur dokument som inte längre är giltiga tas bort

### AI eller explicit regel?

Använd explicit regel när:

- beteendet måste vara deterministiskt
- villkoren är kända
- verksamheten behöver exakt förutsägbarhet
- resultatet måste kunna förklaras direkt från regeln

Använd AI/ML när problemet kräver mönsterigenkänning, prediktion eller språkförståelse.

### Hur bör AI kombineras med regler?

Ett användbart mönster kan vara:

```text
AI/ML
  ↓
bedömning eller signal
  ↓
explicit regel / mänsklig kontroll
  ↓
verksamhetsbeslut
```

På så sätt separeras probabilistisk inferens från själva beslutets styrning.

### När bör en AI-agent användas?

Överväg agent när en AI-funktion behöver:

- utföra flera steg
- välja mellan godkända verktyg
- läsa och skriva via definierade API:er
- hantera en begränsad uppgift med tydliga guardrails

Undvik obegränsad autonomi. Definiera vilka verktyg agenten får använda, vilka data den får se och vilka åtgärder som kräver mänskligt godkännande.

### Extern AI-tjänst eller intern modellplattform?

Bedöm bland annat:

- informationsklassning
- datalokalitet
- leverantörens datahantering
- modellkvalitet
- kostnad
- latency
- tillgänglighet
- lock-in
- möjlighet till loggning och kontroll
- krav på specialmodell eller finjustering

### När standardlösningen inte passar

Beskriv behovet i termer av:

- datatyper
- informationsklass
- volym
- latency
- kvalitet
- förklarbarhet
- modelltyp
- antal inferenser
- kostnadsram
- jurisdiktion
- behov av human-in-the-loop

Därefter bedöms om gemensam sök-, BI-, ML- eller AI-tjänst kan möta behovet.

---

## 6. Plattformar och tjänsteerbjudanden

I detta steg identifieras kandidater. Detaljerade plattformsdokument skapas separat senare eller tidigare vid konkret behov.

| Erbjudande | Syfte | Lämpligt för | Möjlig realisering idag | Status |
|---|---|---|---|---|
| Search and Indexing Service | Fulltextsökning och indexering | verksamhetssökning och sök-API | Elasticsearch | Kandidat |
| Business Intelligence and Reporting | Rapportering och dashboards | verksamhetsuppföljning och analys | Power BI | Kandidat |
| Analytics Platform | Analytisk bearbetning och data science | analysjobb, modeller och experiment | Ej beslutad i detta steg | Kandidat |
| Managed LLM Service | Kontrollerad åtkomst till språkmodeller | generativ AI och assistentfunktioner | Ej beslutad | Kandidat |
| RAG/Knowledge Service | Gemensam semantisk sökning och kunskapsgrundning | AI över interna dokument | Ej beslutad | Kandidat |
| ML Model Serving | Produktionssättning av ML-modeller | klassificering och prediktion | Ej beslutad | Kandidat |
| AI Agent Platform | Kontrollerad agentexekvering | fler-stegs AI-uppgifter | Ej beslutad | Kandidat |
| AI Evaluation Service | Test och kvalitetssäkring av AI | modeller, prompts och RAG | Ej beslutad | Kandidat |

---

## 7. Standarder och teknikval

| Standard/teknikval | Status | Tillämpning |
|---|---|---|
| Elasticsearch | Befintlig produkt att klassificera | Sök- och indexeringstjänst |
| Power BI | Befintlig produkt att klassificera | BI och rapportering |
| Standard för AI-modellmetadata | Kandidat | Modellversion, syfte, ägare och status |
| Prompt-/konfigurationsversionering | Kandidat | Generativ AI |
| RAG-metadata och källreferenser | Kandidat | Kunskapsbaserad AI |
| AI-utvärderingsstandard | Kandidat | Kvalitetsmätning före och efter produktionssättning |
| Standard för AI-guardrails | Kandidat | Begränsning av AI-beteende och verktygsanvändning |
| Embedding-/vektorstandard | Kandidat | Semantisk sökning och RAG |

Produktversioner och modellval ska dokumenteras separat.

---

## 8. Relaterade artefakter och kvalitetsdimensioner

### 8.1 Relevanta kvalitetsdimensioner

Särskilt viktiga dimensioner är:

- **Säkerhet och informationsskydd** – AI- och analyslösningar hanterar ofta stora informationsmängder och externa tjänster.
- **Tillgänglighet** – operativa sök- och AI-funktioner kan bli kritiska beroenden.
- **Prestanda** – sök, analys och modellinferens kan ha höga latency- och kapacitetskrav.
- **Skalbarhet och kapacitet** – index, analysjobb och AI-inferens kan vara resursintensiva.
- **Spårbarhet och verifierbarhet** – viktigt för modellversioner, prompts, källor och resultat.
- **Regelefterlevnad** – särskilt relevant för AI, personuppgifter och automatiserade beslut.
- **Förvaltningsbarhet och förändringsbarhet** – modeller, prompts och index förändras oberoende av applikationskod.
- **Interoperabilitet och portabilitet** – modell- och leverantörsberoende kan vara betydande.
- **Livscykel och hållbarhet** – AI-teknik förändras snabbt.
- **Kostnads- och resurseffektivitet** – analys och AI kan ha stor och varierande resurskostnad.

### 8.2 Lösningsmönster

Identifierade kandidater:

- Search Index as Derived Data
- Operational Search
- BI / Analytical Read Model
- RAG
- Semantic Search
- Human-in-the-loop AI
- AI-assisted Decision with Rule Guardrails
- Model Serving
- Batch Scoring
- AI Gateway
- Controlled AI Agent
- Model/Prompt Versioning
- AI Evaluation and Observability

### 8.3 Plattformar

Identifierade kandidater:

- Search and Indexing Service
- Business Intelligence and Reporting
- Analytics Platform
- Managed LLM Service
- RAG/Knowledge Service
- ML Model Serving
- AI Agent Platform
- AI Evaluation Service

### 8.4 Tekniska standarder

Identifierade kandidater:

- Elasticsearch-standard
- Power BI-standard
- AI-modellmetadata
- promptversionering
- RAG-metadata och källreferenser
- AI-utvärderingsstandard
- AI-guardrails
- embedding-/vektorstandard

### 8.5 Kandidater till referensarkitekturer

Följande kandidater stärks eller identifieras:

- **Data- och analyslösning**
- **AI-baserat verksamhetsstöd**
- **RAG-baserad kunskapstjänst**
- **AI-baserat beslutsstöd med human-in-the-loop**
- **Regelintensivt verksamhetssystem med AI-signaler**
- **Internt handläggningsstöd med AI-assistent**
- **Publik e-tjänst med AI-stöd** – endast där risk och användningsfall motiverar detta

### 8.6 Teknisk dokumentation

När konkreta analys- och AI-plattformar väljs bör teknisk dokumentation exempelvis omfatta:

- anslutning till datakällor
- indexering
- modell-/promptdeployment
- versionshantering
- autentisering och auktorisation
- nätverks- och datalokalitet
- logging och observability
- kvalitetsmått
- guardrails
- kostnads- och kvotstyrning
- backup/restore för index och metadata
- tekniska begränsningar

---

## Arbetsanteckningar

### Identifierade kandidater

**Lösningsmönster**
- Search Index as Derived Data
- Operational Search
- BI / Analytical Read Model
- RAG
- Semantic Search
- Human-in-the-loop AI
- AI-assisted Decision with Rule Guardrails
- Model Serving
- Batch Scoring
- AI Gateway
- Controlled AI Agent
- Model/Prompt Versioning
- AI Evaluation and Observability

**Plattformar/tjänster**
- Search and Indexing Service
- Business Intelligence and Reporting
- Analytics Platform
- Managed LLM Service
- RAG/Knowledge Service
- ML Model Serving
- AI Agent Platform
- AI Evaluation Service

**Tekniska standarder**
- Elasticsearch
- Power BI
- AI-modellmetadata
- promptversionering
- RAG-metadata och källreferenser
- AI-utvärderingsstandard
- AI-guardrails
- embedding-/vektorstandard

**Referensarkitekturer**
- data- och analyslösning
- AI-baserat verksamhetsstöd
- RAG-baserad kunskapstjänst
- AI-baserat beslutsstöd med human-in-the-loop
- regelintensivt verksamhetssystem med AI-signaler
- internt handläggningsstöd med AI-assistent

**Gränsdragningsfrågor**
- hur mycket sökning som bör ligga här jämfört med Data- och informationshantering
- när rapportering blir operativ applikationsfunktion snarare än BI
- hur AI-baserade och regelbaserade beslut ska styras tillsammans
- om generativ AI, ML och BI på sikt bör delas i underområden
- hur externa AI-tjänster ska beskrivas mot framtida leverans-/realiseringsmodell
