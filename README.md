# 🏥 MEDICURE — AI Healthcare Web Application

<div align="center">

![MEDICURE Banner](https://img.shields.io/badge/MEDICURE-AI%20Healthcare-0d6e4f?style=for-the-badge&logo=heart&logoColor=white)
![Claude AI](https://img.shields.io/badge/Powered%20by-Claude%20AI-1fd99a?style=for-the-badge)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES2022-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

**A production-grade AI-powered healthcare platform built with pure frontend technologies + Anthropic Claude AI**

*MCA Project — Chandigarh University | Aman Yadav [24MCI10125] | March 2026*

[🚀 Live Demo](#) · [📋 Project Report](#) · [🐛 Report Bug](#) · [✨ Request Feature](#)

</div>

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [AI Agents](#-ai-agents)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Screenshots](#-screenshots)
- [Medicine Database](#-medicine-database)
- [Doctor Directory](#-doctor-directory)
- [API Integration](#-api-integration)
- [State Management](#-state-management)
- [Color System](#-color-system)
- [Known Limitations](#-known-limitations)
- [Future Scope](#-future-scope)
- [Author](#-author)
- [License](#-license)

---

## 🌟 About the Project

**MEDICURE** is a comprehensive, AI-powered healthcare web application that mirrors the functionality of real-world platforms like Practo and Apollo 24/7 — built entirely with **vanilla HTML, CSS, and JavaScript** integrated with the **Anthropic Claude AI API**.

The platform solves three critical problems in modern healthcare:

| Problem | MEDICURE Solution |
|---------|------------------|
| 35% of doctor time lost to paperwork | **NOVA** auto-generates SOAP notes from voice in seconds |
| 50% higher AI misdiagnosis rate in women | **ARIA** includes active clinical bias detection engine |
| Unstructured patient intake wastes consultation time | **ARIA** conducts full intake before the doctor walks in |

### 🏆 Project Highlights

- ✅ **Single HTML file** (~1,771 lines) — zero build tools, zero dependencies
- ✅ **Three AI agents** powered by Claude Sonnet — ARIA, DARA, NOVA
- ✅ **35+ medicines** with AI-powered drug information lookup
- ✅ **10 doctors** across 6 specialties with interactive booking
- ✅ **Role-based dashboards** — separate Patient and Doctor experiences
- ✅ **Full patient-to-doctor pipeline** — ARIA intake → case queue → DARA analysis → report
- ✅ **AI report generation** — health reports for patients + clinical reports for doctors
- ✅ **Deploy anywhere** — GitHub Pages, Netlify, Vercel — zero config

---

## ✨ Key Features

### 🏠 Landing Page
- Animated hero section with floating status cards (ARIA, DARA, NOVA live stats)
- Statistics strip — 4 key healthcare facts
- Three AI agent showcase cards
- **30+ medicine marquee** — two infinite-scroll rows with medicine pill cards
- Appointment booking split section (3-step guide + quick booking form)
- Professional footer

### 🔐 Authentication
- **Patient** and **Doctor** role toggle on Login and Register screens
- Registration collects: Name, Specialization *(doctors only)*, Email, Password, Age, Gender
- Form validation — email uniqueness, min 6-char password, required fields
- Auto-login after registration; session restored on page reload
- **Demo mode** — explore without registering

### 👤 Patient Dashboard (6 Sections)
| Section | Description |
|---------|-------------|
| 🏠 Home | 6-card quick access grid + daily health tip + popular medicines |
| 🩺 ARIA Chat | Multi-turn AI symptom intake chatbot with bias detection |
| 💊 Medicines | AI medicine lookup + 35-card library grid |
| 📍 Find Doctors | Specialty filters + geolocation + booking |
| 📅 Appointments | All booked appointments with status badges |
| 📊 AI Reports | Personal AI health report generator |

### 👨‍⚕️ Doctor Dashboard (5 Sections)
| Section | Description |
|---------|-------------|
| 🏠 Home | Stats: time saved, pending cases, SOAP notes, bias flags |
| 🧠 DARA | Patient analysis with differential diagnosis output |
| 🎙️ NOVA | Voice-to-SOAP documentation recorder |
| 👥 Patient Cases | ARIA intake queue — expandable cards with action buttons |
| 📊 Patient Reports | AI clinical report generator with ICD codes + print button |

### 📅 Appointment Booking
- Modal overlay with 12 time slots (3 rows × 4 columns)
- Slot states: **Available** / **Booked** (greyed, non-clickable) / **Selected** (dark)
- Date picker with today as minimum date
- Reason text area + Confirm / Cancel button pair
- All appointments persisted to `localStorage` per user

---

## 🤖 AI Agents

### 🩺 ARIA — Automated Reception & Intake Agent

```
Role: Patient intake nurse
Mode: Multi-turn conversational (full history maintained)
Language: Hindi + English supported
```

ARIA conducts structured patient intake by asking one question at a time:
symptoms → duration → severity (1–10) → location → triggers → history → medications

**Bias Detection Engine:**
```
If female patient + chest/jaw/arm pain:
  → ⚠ BIAS FLAG: Atypical cardiac presentation detected.
    AI underdiagnoses MI in women by 50% (AHA 2022)

If female patient + fatigue + joint pain:
  → ⚠ BIAS FLAG: Autoimmune underdiagnosis risk.
    Average 7-year delay in women (NIH)
```

After 4–5 exchanges, ARIA auto-generates a `[SUMMARY]` block pushed to the doctor's patient cases queue.

---

### 🧠 DARA — Doctor Advisory & Response Agent

```
Role: Clinical analysis and diagnosis support
Mode: Single-call, structured JSON output
```

**Input fields:** Patient name, age, gender, chief complaint, medical history, vitals

**Output JSON structure:**
```json
{
  "summary": "2-sentence patient overview",
  "urgencyScore": "CRITICAL | HIGH | MEDIUM | LOW",
  "diagnoses": [
    { "name": "...", "confidence": 85, "notes": "..." },
    { "name": "...", "confidence": 65, "notes": "..." },
    { "name": "...", "confidence": 40, "notes": "..." }
  ],
  "patterns": "Key patterns found",
  "unexploredTreatments": "...",
  "safeMedicines": ["...", "..."],
  "avoidMedicines": ["...", "..."],
  "dietAdvice": "...",
  "biasFlags": ["..."],
  "nextSteps": "...",
  "followUpPlan": "..."
}
```

---

### 🎙️ NOVA — Note & Voice Auto-documentation Agent

```
Role: Medical documentation from voice or text
Mode: Single-call, structured JSON output
Input: Web Speech API (voice) OR text area
```

**SOAP Note Output:**
```json
{
  "subjective": "What the patient reported",
  "objective": "Observable findings and vitals",
  "assessment": "Clinical diagnosis",
  "plan": "Treatment, medications, follow-up"
}
```

> 💡 Saves an estimated **2.5 hours per doctor per day**

---

## 🛠 Tech Stack

| Technology | Category | Purpose |
|-----------|----------|---------|
| HTML5 | Frontend | Page structure & semantic markup |
| CSS3 | Frontend | Styling, animations, SPA layouts |
| JavaScript ES2022 | Frontend | SPA routing, state, DOM rendering |
| **Anthropic Claude API** | **AI Backend** | **ARIA, DARA, NOVA agent responses** |
| Google Fonts | Typography | Playfair Display + Plus Jakarta Sans |
| localStorage | Browser | Session, appointments, case persistence |
| Web Speech API | Browser | Voice recording for NOVA |
| CSS Grid + Flexbox | Layout | All major layout areas |
| CSS Custom Properties | Design | Full design token system |

---

## 📁 Project Structure

```
medicure/
│
├── index.html                  ← Entire application (single file)
│   │
│   ├── <style>                 ← All CSS (~500 lines)
│   │   ├── CSS variables       (design tokens)
│   │   ├── Navigation          (sticky nav, logo, user info)
│   │   ├── Landing page        (hero, stats, agents, medicines, footer)
│   │   ├── Auth pages          (login, register, role toggle)
│   │   ├── Dashboard layout    (sidebar, content area)
│   │   ├── ARIA chat           (messages, bias flag, typing indicator)
│   │   ├── Medicine module     (search bar, result grid, card grid)
│   │   ├── Doctor module       (filter pills, doctor cards)
│   │   ├── Appointment modal   (overlay, slot grid, form)
│   │   ├── DARA module         (form, diagnosis bars, output grid)
│   │   ├── NOVA module         (record button, SOAP output)
│   │   ├── Report modules      (patient + doctor report cards)
│   │   ├── Patient cases       (expandable cards, action buttons)
│   │   └── Utilities           (toast, loading spinner, badges)
│   │
│   ├── Pages (7 views)
│   │   ├── #page-landing       (public home page)
│   │   ├── #page-login         (auth — patient/doctor role)
│   │   ├── #page-register      (auth — with specialization)
│   │   ├── #page-patient       (patient dashboard + sidebar)
│   │   └── #page-doctor        (doctor dashboard + sidebar)
│   │
│   └── <script>                ← All JavaScript (~1,000 lines)
│       ├── Constants & Data
│       │   └── ALL_MEDICINES[] (35+ medicine objects)
│       │
│       ├── State Variables
│       │   ├── currentUser     (logged-in user object)
│       │   ├── ariaMessages    (conversation history)
│       │   ├── appointments    (booked appointments)
│       │   ├── loginRole       (patient | doctor)
│       │   ├── selectedSlot    (active time slot)
│       │   └── currentFilter   (active specialty filter)
│       │
│       ├── Router
│       │   ├── showPage()      (top-level page routing)
│       │   ├── showSection()   (patient sidebar sections)
│       │   └── showDocSection()(doctor sidebar sections)
│       │
│       ├── Auth Module
│       │   ├── doLogin()
│       │   ├── doRegister()
│       │   ├── loginSuccess()
│       │   └── doLogout()
│       │
│       ├── AI Module
│       │   ├── callClaude()        (single-call API)
│       │   ├── callClaudeConvo()   (multi-turn API)
│       │   ├── sendARIA()          (ARIA chat handler)
│       │   ├── runDARA()           (DARA analysis)
│       │   ├── generateSOAP()      (NOVA documentation)
│       │   ├── generateHealthReport()   (patient report)
│       │   └── generateDoctorReport()   (clinical report)
│       │
│       ├── Medicine Module
│       │   ├── searchMedicine()
│       │   ├── renderHomeMedGrid()
│       │   └── renderPatientMedGrid()
│       │
│       ├── Doctor Module
│       │   ├── loadDoctors()
│       │   ├── filterDocs()
│       │   └── getLocation()
│       │
│       ├── Appointment Module
│       │   ├── bookDoctor()
│       │   ├── selectSlot()
│       │   ├── confirmAppointment()
│       │   └── loadAppointments()
│       │
│       ├── Patient Cases Module
│       │   ├── loadPatientCases()
│       │   ├── togglePatientReport()
│       │   ├── loadCaseInDARA()
│       │   └── loadCaseInReport()
│       │
│       └── Utilities
│           ├── showToast()
│           ├── loadDailyTip()
│           ├── renderLandingMeds()
│           └── saveARIAReport()
│
└── README.md                   ← This file
```

---

## 🚀 Getting Started

### Prerequisites

- A modern web browser (Chrome 124+, Firefox 125+, Safari 17+)
- An **Anthropic API key** — get one free at [console.anthropic.com](https://console.anthropic.com)

### Installation

**Option 1 — Direct open (simplest)**
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/medicure.git

# Open in browser (no server needed)
open medicure/index.html
```

**Option 2 — Local dev server**
```bash
# Using Python
python3 -m http.server 3000

# Using Node.js
npx serve .

# Then open http://localhost:3000
```

**Option 3 — Deploy to GitHub Pages**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/medicure.git
git push -u origin main
# Enable GitHub Pages in repo Settings → Pages → main branch
```

### API Key Setup

Open `index.html` and locate the `callClaude` function (~line 380). Add your API key:

```javascript
const response = await fetch(CLAUDE_API, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'x-api-key': 'YOUR_ANTHROPIC_API_KEY_HERE',   // ← Add here
    'anthropic-version': '2023-06-01',
    'anthropic-dangerous-direct-browser-calls': 'true'
  },
  // ...
});
```

> ⚠️ **Note:** Exposing API keys in client-side code is for academic/demo purposes only. In production, proxy all AI calls through a backend server.

---

## 📖 Usage

### As a Patient

1. **Register** → select **Patient** role → fill in details
2. **Talk to ARIA** → describe your symptoms in Hindi or English
3. ARIA will ask follow-up questions and generate an intake report
4. **Find Doctors** → filter by specialty → click **Book Appointment**
5. Select a date and time slot → confirm
6. **AI Reports** → enter your health concerns → generate a full health report
7. **My History** → view all past ARIA consultations

### As a Doctor

1. **Register** → select **Doctor** role → enter your specialization
2. **Patient Cases** → view patients who completed ARIA intake
3. Click **Open in DARA** → get differential diagnoses with confidence scores
4. **NOVA Notes** → speak your consultation notes → receive SOAP note instantly
5. **Patient Reports** → generate comprehensive clinical reports with ICD codes
6. Use **Medicine Search** for clinical drug information

### Demo Mode

Click **🎬 Live Demo** on the landing page to explore the patient dashboard without registering.

---

## 📸 Screenshots

| Screen | Description |
|--------|-------------|
| Landing Page | Hero, medicine marquee, AI agents, appointment form |
| ARIA Chat | Multi-turn intake with bias flag detection |
| DARA Analysis | Differential diagnosis with confidence bars |
| NOVA SOAP | Voice recording + SOAP note output |
| Medicine Lookup | AI drug information with 5-cell info grid |
| Doctor Directory | Specialty filters + booking modal with slots |
| AI Health Report | Patient report with risk badge + 11 output sections |
| Clinical Report | Doctor report with ICD, prognosis, print button |

---

## 💊 Medicine Database

35+ medicines across all major pharmacological categories:

| Category | Medicines |
|----------|-----------|
| Analgesics / NSAIDs | Paracetamol, Aspirin, Ibuprofen |
| Antidiabetics | Metformin |
| Antihypertensives | Amlodipine, Losartan, Enalapril, Bisoprolol, Furosemide |
| Antibiotics | Azithromycin, Amoxicillin, Ciprofloxacin, Doxycycline |
| Statins | Atorvastatin |
| Antihistamines | Cetirizine |
| PPIs / Antacids | Omeprazole, Pantoprazole, Ranitidine |
| Beta-Blockers | Metoprolol, Bisoprolol |
| Supplements | Vitamin D3, Folic Acid, Iron Sulfate, Calcium Carbonate, Vitamin C |
| Thyroid | Levothyroxine |
| Corticosteroids | Prednisolone |
| Neuropathic | Gabapentin |
| Antidepressants | Sertraline |
| Antiemetics | Domperidone |
| Asthma / Bronchodilators | Montelukast, Salbutamol |
| Anxiolytics | Diazepam, Clonazepam |
| Antiplatelet | Clopidogrel |
| Antimalarial | Hydroxychloroquine |

Each medicine returns AI-powered info for:
- ✅ Uses & indications
- 💉 Dosage & frequency
- ⚠️ Side effects
- 🚫 Precautions & contraindications
- 🔗 Drug interactions

---

## 👨‍⚕️ Doctor Directory

| Doctor | Specialty | Rating | Experience | Status |
|--------|-----------|--------|------------|--------|
| Dr. Priya Sharma | General Physician | 4.8★ | 12 yrs | Available |
| Dr. Rajesh Kumar | Cardiologist | 4.9★ | 18 yrs | Available |
| Dr. Anita Singh | Dermatologist | 4.6★ | 8 yrs | Unavailable |
| Dr. Vikram Patel | Orthopedic | 4.7★ | 15 yrs | Available |
| Dr. Meera Nair | Pediatrician | 4.9★ | 10 yrs | Available |
| Dr. Suresh Rao | General Physician | 4.5★ | 20 yrs | Available |
| Dr. Kavita Joshi | Cardiologist | 4.8★ | 14 yrs | Unavailable |
| Dr. Arjun Mehta | Orthopedic | 4.4★ | 9 yrs | Available |
| Dr. Deepa Reddy | Gynecologist | 4.7★ | 13 yrs | Available |
| Dr. Sanjay Gupta | Dermatologist | 4.6★ | 11 yrs | Available |

---

## 🔌 API Integration

### Claude API Call — Single Turn
```javascript
async function callClaude(systemPrompt, userMessage, maxTokens = 800) {
  const res = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      model: 'claude-sonnet-4-20250514',
      max_tokens: maxTokens,
      system: systemPrompt,
      messages: [{ role: 'user', content: userMessage }]
    })
  });
  const data = await res.json();
  return data.content[0].text;
}
```

### Claude API Call — Multi-Turn (ARIA)
```javascript
async function callClaudeConvo(systemPrompt, messages, maxTokens = 600) {
  const res = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      model: 'claude-sonnet-4-20250514',
      max_tokens: maxTokens,
      system: systemPrompt,
      messages  // Full conversation history
    })
  });
  const data = await res.json();
  return data.content[0].text;
}
```

### Model Used
```
claude-sonnet-4-20250514
```

---

## 🗃️ State Management

### Runtime State (in-memory)

```javascript
let currentUser    = null;     // Logged-in user session
let loginRole      = 'patient';// Active role toggle
let ariaMessages   = [];       // Full ARIA conversation history
let selectedSlot   = '9:00 AM';// Active appointment slot
let currentFilter  = 'All';    // Active doctor specialty filter
let currentBookingDoctor = ''; // Doctor name for active booking
```

### localStorage Schema

```javascript
// Keys
'mc_current'              → Current user session object
'mc_users'                → Array of all registered accounts
'mc_users[N].history'     → ARIA consultation history per user
'mc_users[N].appointments'→ Booked appointments per user
'mc_cases'                → Doctor patient case queue (from ARIA)

// User Object Shape
{
  id: 1234567890,
  name: "Aman Yadav",
  email: "aman@example.com",
  password: "••••••",       // plaintext — demo only
  role: "patient",          // "patient" | "doctor"
  age: "22",
  gender: "Male",
  spec: "",                 // Specialization (doctors only)
  history: [],              // ARIA consultation records
  appointments: []          // Booked appointment objects
}

// Appointment Object Shape
{
  id: 1234567890,
  doctor: "Dr. Priya Sharma",
  date: "2026-03-15",
  slot: "10:30 AM",
  reason: "Fever and headache for 3 days",
  status: "Confirmed"
}
```

---

## 🎨 Color System

```css
:root {
  --green:       #0d6e4f;   /* Primary — deep forest green     */
  --green2:      #15a474;   /* Secondary — bright green        */
  --green3:      #1fd99a;   /* Tertiary — neon green hover     */
  --green-pale:  #e6f7f2;   /* Fill — light green tint         */
  --green-pale2: #c8f0e3;   /* Fill 2 — medium green tint      */
  --bg:          #f5fbf8;   /* Background — sage white         */
  --text:        #0d1f18;   /* Text primary — near-black       */
  --text-muted:  #527563;   /* Text secondary — muted green    */
  --border:      #c9e8dc;   /* Border — green-tinted separator */
  --amber:       #f59e0b;   /* Ratings and warnings            */
  --red:         #ef4444;   /* Errors and unavailable          */
  --blue:        #2563eb;   /* Info and secondary actions      */
  --shadow:      0 4px 28px rgba(13,110,79,0.10);
  --shadow2:     0 8px 40px rgba(13,110,79,0.18);
  --radius:      18px;
  --radius-sm:   12px;
}
```

**Typography:**
- Display: `Playfair Display` (serif) — headings, section titles
- Body: `Plus Jakarta Sans` (sans-serif) — all UI text

---

## ⚠️ Known Limitations

| Limitation | Details |
|-----------|---------|
| No real backend | All data is client-side; clearing localStorage resets state |
| Plaintext passwords | Stored in localStorage — academic demo only |
| No payment gateway | Appointment booking is local only — no SMS/email confirmation |
| API key exposure | Claude API key visible in source — must proxy in production |
| Static doctor data | Availability is hardcoded mock data |
| Voice recognition | NOVA voice requires Chrome or Safari (not Firefox) |
| No streaming | ARIA responses are request-response, not streamed |
| Internet required | Google Fonts CDN needed for typography |

---

## 🔭 Future Scope

### Immediate Enhancements
- [ ] **Backend API** — Node.js/Express + MongoDB for real persistence
- [ ] **JWT authentication** — bcrypt password hashing
- [ ] **Streaming ARIA** — Claude streaming API (SSE) for real-time feel
- [ ] **Razorpay integration** — real appointment payment
- [ ] **Doctor availability calendar** — real-time slot management
- [ ] **Email confirmations** — appointment booking via Nodemailer

### Feature Additions
- [ ] **Video consultation** — WebRTC peer-to-peer video calls
- [ ] **Prescription module** — doctor writes, patient receives PDF
- [ ] **Lab report upload** — OCR-based data extraction for DARA
- [ ] **Multi-language** — Hindi, Tamil, Bengali, Marathi UI
- [ ] **PWA support** — offline mode + home screen install
- [ ] **Push notifications** — appointment reminders via Web Push
- [ ] **Wearable integration** — heart rate + SpO2 feeds into ARIA context
- [ ] **Insurance module** — claim assistance powered by document AI

---

## 🧪 Testing Checklist

| Flow | Status |
|------|--------|
| User registration (patient + doctor) | ✅ Verified |
| Login — correct credentials, wrong role detection | ✅ Verified |
| Demo mode activation | ✅ Verified |
| ARIA multi-turn conversation | ✅ Verified |
| ARIA bias flag — female + chest pain | ✅ Verified |
| ARIA summary generation + doctor queue save | ✅ Verified |
| Medicine search — text query + quick pills | ✅ Verified |
| Medicine grid — 35+ cards | ✅ Verified |
| Doctor specialty filters (6 filters) | ✅ Verified |
| Geolocation permission request | ✅ Verified |
| Appointment modal — slot selection | ✅ Verified |
| Booked slot non-interactivity | ✅ Verified |
| Appointment persistence after reload | ✅ Verified |
| DARA form validation + API call | ✅ Verified |
| DARA confidence bars rendering | ✅ Verified |
| NOVA text input → SOAP note | ✅ Verified |
| NOVA voice recording (Chrome/Safari) | ✅ Verified |
| Patient cases expandable cards | ✅ Verified |
| Open in DARA prefill | ✅ Verified |
| Patient AI health report (all 11 sections) | ✅ Verified |
| Doctor clinical report (ICD + print) | ✅ Verified |
| Session persistence across reload | ✅ Verified |
| ARIA history display | ✅ Verified |

**Tested on:** Chrome 124 · Firefox 125 · Safari 17

---

## 👨‍💻 Author

**Aman Yadav**
- University ID: `24MCI10125`
- Program: Master of Computer Applications (MCA)
- University: Chandigarh University, India
- Submitted: 3rd March, 2026

---

## 📄 License

This project is submitted as part of the MCA curriculum at Chandigarh University. All code is original work by the author.

```
MIT License — feel free to use, modify, and distribute
with attribution to the original author.
```

---

<div align="center">

**Built with ❤️ and Claude AI**

*MEDICURE — Transforming healthcare with AI, one consultation at a time.*

</div>
