# Sanchi: MPLADS Scheme Surveillance & Anomaly Audit Portal
### Smart India Hackathon 2026 | Problem Statement ID: 26102
**Ministry of Statistics & Programme Implementation (MoSPI), Government of India**  
*Enterprise Decision-Support Platform for Public Expenditure Integrity & Milestone Tracking*

---

## 📌 Submission Quick-Access Matrix

| Resource | Access Link / Location | Description |
|---|---|---|
| 🌐 **Live Web Application** | [sih-2026-mpals-main.onrender.com](https://sih-2026-mpals-main.onrender.com/) | Deployed full-stack cloud instance with live REST API & interactive UI |
| 🎥 **YouTube Video Walkthrough** | [Watch Demo on YouTube](https://youtu.be/kuiuq0MSW7A?si=QFERS4v-arDcV6sq) | Official project video demonstration showcasing RBAC, anomaly engine & case triage |
| 🏛️ **Nodal Ministry** | **MoSPI (Govt of India)** | Ministry of Statistics and Programme Implementation |
| 🎯 **Problem Statement** | **PS ID: 26102** | Automated detection of expenditure irregularities, milestone divergence & ghost assets in MPLADS |

---

## 🏛️ Executive Summary & Core Mission

The **Members of Parliament Local Area Development Scheme (MPLADS)** channels substantial public developmental capital across all parliamentary constituencies in India. Effective oversight faces critical challenges:
1. **Auditing Scalability Deficit**: Manual post-facto review cannot scale across 770+ MPs and tens of thousands of active works.
2. **Milestone Divergence (Payment vs. Progress)**: Public Financial Management System (PFMS) disbursements often outpace verified ground execution.
3. **Asset Inspection Gaps**: High-value completed projects risk becoming "ghost assets" without mandatory third-party geo-tagged inspections.
4. **Data Silos**: Information fragmentation between PFMS financial ledgers, e-SAKSHI administrative sanctions, GeM procurement bids, and district field offices.

**Sanchi** is an enterprise-grade AI decision-support and surveillance portal engineered adhering to **Guidelines for Indian Government Websites (GIGW 3.0)**, the **Digital Personal Data Protection (DPDP) Act, 2023**, and **STQC/CERT-In** cybersecurity baselines.

---

## 🔬 Explainable Statistical Anomaly Engine

Sanchi prioritizes **100% explainable, mathematically auditable statistical formulations** rather than opaque black-box neural networks, ensuring administrative defensibility before district magistrates, state nodal committees, and parliamentary audit panels:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   SANCHI STATISTICAL SURVEILLANCE ENGINE               │
├────────────────────────────────┬───────────────────────────────────────┤
│  1. Parametric Z-Score         │  Z = (x - μ) / σ  (|Z| > 3.0 Outlier) │
│  2. Non-Parametric IQR Fencing │  [Q1 - 1.5*IQR,  Q3 + 1.5*IQR]        │
│  3. Cohort Peer Deviation      │  Δ% = ((x - M_state) / M_state) * 100 │
│  4. Milestone Divergence Gap   │  Gap = (Paid% - Completed%) ≥ 20%     │
│  5. Rapid Pre-Execution Payout │  Disbursed ≥ 85% with Progress ≤ 20%  │
│  6. Unverified Asset Deficit   │  Sanction ≥ ₹25L, Status=Done, No GIS │
└────────────────────────────────┴───────────────────────────────────────┘
```

| Surveillance Module | Formulation & Threshold | Administrative Objective |
|---|---|---|
| **Z-Score Outlier Analysis** | $Z = \frac{x - \mu}{\sigma}$ ($|Z| > 3.0$) | Flags allocation amounts that sharply diverge from national statistical distributions. |
| **IQR Fencing** | $[Q_1 - 1.5 \times \text{IQR}, Q_3 + 1.5 \times \text{IQR}]$ | Detects extreme skewness without assuming underlying Gaussian distribution. |
| **Cohort Peer Variance** | Deviation % from State peer group median | Identifies localized allocation anomalies within identical state jurisdictions. |
| **Milestone Divergence** | $\text{Gap} = \left(\frac{\text{Paid}}{\text{Sanctioned}} \times 100\right) - \text{Physical \%} \ge 20\%$ | Identifies contractor payments released in excess of certified physical progress. |
| **Premature Disbursal** | Paid $\ge 85\%$ while Progress $\le 20\%$ | Generates immediate Critical flag for anomalous pre-completion contractor liquidity. |
| **Geo-Tag Inspection Deficit** | Sanction $\ge ₹25\text{ Lakhs}$, Completed, Unverified | Prevents fictitious/ghost asset creation by requiring NIC GIS photo verification. |

Every risk score is **fully explainable**: clicking any MP or alert opens an itemized factor breakdown explaining exactly why the score was computed.

---

## 🛡️ Role-Based Access Control (RBAC) & Jurisdictional Scoping

Sanchi implements cryptographic **JSON Web Token (JWT)** session authentication and **bcrypt password hashing** (`saltRounds=10`). All API endpoints enforce strict scope filtering:

| Role | Default User | Default Password | Jurisdictional Remit & Security Scope |
|---|---|---|---|
| 🏛️ **Ministry Admin** | `admin@mospi.gov.in` | `Password@123` | **National Scope**: All 773 MPs, 36 States/UTs, all civil works & alerts |
| 🏢 **State Nodal Officer** | `nodal.maharashtra@gov.in` | `Password@123` | **State Scope**: Restricted strictly to Maharashtra (MPs, works & alerts) |
| 📍 **District Collector** | `dm.mumbai@nic.in` | `Password@123` | **District Scope**: Restricted to Mumbai City district works & inspections |
| 👤 **Hon'ble MP** | `mp.abhishek@sansad.nic.in` | `Password@123` | **Constituency Scope**: Personal recommendations, disbursements & status |
| 👥 **Public Guest / Citizen** | *Unauthenticated* | *N/A* | **Transparency View**: Aggregated public statistics; triage & action tools locked |

---

## 🔍 Investigation Workspace & Statutory Notice Dispatch

Alerts in Sanchi feed into an interactive, multi-role **Investigation Workspace**:
1. **Explainable Why Flagged**: Shows mathematical formula, standard deviation, and ledger trail.
2. **Evidence Comparison**: Correlates sanctioned budget, cumulative expenditure, payment timestamps, and NIC geo-tagging.
3. **Statutory Notice Dispatch**: Authorized officers can trigger simulated official **NIC SMS notices** dispatched to District Magistrates and Hon'ble MP secretariats with unique tracking reference numbers (`NIC-MOSPI-...`).
4. **Immutable Audit Log**: Records case resolution status transitions (`Open`, `Under Review`, `Resolved`, `False Positive`) with officer identity and timestamp.

---

## 📊 Dataset Provenance & Seed Statistics

The database is initialized with verified, real-world parliamentary baselines:
- **773 Members of Parliament**: 100% complete dataset covering Lok Sabha constituencies and Rajya Sabha members.
- **847 Civil Works**: Representative developmental works covering **all 36 States and Union Territories of India**.
- **1,495 Anomaly Alerts**: Calibrated across Critical, High, Medium, and Low severity classifications.
- **2,089 Payment Vouchers**: Granular milestone transactions simulating PFMS/EAT ledger distributions.
- **847 Physical Assets**: Geo-tagged infrastructure assets with GPS coordinates and inspection statuses.

---

## 🚀 Quickstart & Deployment Guide

### Prerequisites
- **Node.js**: `v20.0.0` or `v22.0.0+` (LTS recommended)
- **npm**: `v9.0.0+`
- **Zero Frontend Bundling**: Pure native ES6/HTML5 SPA; all third-party libraries (Leaflet, Chart.js) are locally vendored or CDN-fallback enabled.

### 1. Installation
Clone the repository and install server dependencies:
```bash
git clone https://github.com/Amizhthan404/SANCHI.git
cd SANCHI
npm run setup
```
*(The root `setup` script installs server dependencies and automatically migrates & seeds the SQLite database).*

### 2. Manual Database Setup (Optional)
```bash
npm --prefix server run db:setup
```
This runs schema migrations and seeds `server/db/mplads.sqlite` with the complete 773-MP and 847-works dataset.

### 3. Launching Application

#### Development Mode (with hot-reload):
```bash
npm run dev
```

#### Production Build & Run:
```bash
npm run build
npm start
```

Access the portal in your web browser at:  
👉 **`https://sih-2026-mpals-main.onrender.com/`** (Live Cloud Deployment)  
👉 **`http://localhost:5000`** (Local Instance)

---

## 📁 Repository Structure

```
SIH-2026---Sanchi/
├── index.html                   # Official Government SPA (GIGW 3.0 compliant)
├── render.yaml                  # Automated zero-config deployment manifest for Render
├── package.json                 # Root script orchestration
├── .gitignore                   # Comprehensive enterprise ignore rules
├── .env.example                 # Environment configuration template
│
├── css/
│   ├── main.css                 # Government design system (MoSPI / NIC color tokens, skeletons)
│   └── animations.css           # Institutional micro-interactions (no bouncy transitions)
│
├── js/
│   ├── app.js                   # Application state, router, modals, skeleton renderers
│   ├── ai-engine.js             # Statistical formatters & anomaly classification
│   ├── charts.js                # Dual-axis timeline & donut visualization engine
│   ├── data.js                  # REST API client with JWT session persistence
│   └── map.js                   # Pan-India choropleth heatmap & Leaflet marker engine
│
├── scripts/
│   └── enrich_dataset.py        # Offline synthetic works generator (847 works, 36 States/UTs)
│
├── data/
│   ├── Allocated Limit for Honble MPs.xlsx      # Official Rajya Sabha full dataset (773 MPs)
│   ├── Allocated Limit for Honble MPs (1).xlsx  # Official Rajya Sabha current term dataset
│   └── gen_data.py              # Parsing script for raw parliament spreadsheets
│
├── vendor/
│   └── chartjs/
│       └── chart.umd.min.js     # Vendored offline Chart.js 4.4.8 engine
│
└── server/                      # Express + TypeScript REST API Backend
    ├── src/
    │   ├── config/              # Robust multi-path database & static path resolution
    │   ├── controllers/         # Scoped controllers (Auth, MPs, Works, Alerts, States, Summary)
    │   ├── middleware/          # JWT authentication & jurisdictional RBAC guards
    │   ├── routes/              # Express REST routes (/api/auth, /api/alerts, /api/works)
    │   ├── services/            # Statistical Anomaly Engine (Single Source of Truth)
    │   ├── types/               # TypeScript data models and interfaces
    │   └── index.ts             # Server entry point
    ├── db/
    │   ├── migrations/          # Schema definitions (PostgreSQL & SQLite compatible)
    │   ├── seeds/               # Seeding script with bcrypt hashing & realistic data
    │   │   ├── seed-data.json   # 847 works, 773 MPs, 1495 alerts
    │   │   └── seed.ts          # Database populator script
    │   └── schema.sql           # Canonical relational schema
    ├── tsconfig.json            # TypeScript build configuration
    └── package.json             # Backend dependencies
```

---

## 🔒 Security & Statutory Compliance Standards

1. **Information Technology Act, 2000 (Sections 43, 66 & 72)**: Strict legal warnings and immutable session logging for unauthorized access attempts.
2. **Digital Personal Data Protection (DPDP) Act, 2023**: Purpose-limited data access, role-level redaction, and strict PII masking.
3. **Guidelines for Indian Government Websites (GIGW 3.0)**: Accessible color contrasts (WCAG 2.1 AA), keyboard navigability, and official National Emblem/Tri-colour standards.
4. **STQC & CERT-In Guidelines**: AES-256 TLS 1.3 transport security, strict Content Security Policy (CSP), parameterized SQL queries preventing injection, and salted bcrypt credential storage.

---

*Engineered for Smart India Hackathon 2026 · Problem Statement 26102 · Ministry of Statistics & Programme Implementation (MoSPI)*
