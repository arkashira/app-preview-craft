# ROADMAP.md – app‑preview‑craft  

*Version: 1.0 – Updated 2026‑06‑19*  

---  

## 1. Vision & Scope  

**app‑preview‑craft** is a template‑driven video creation SaaS for indie iOS developers.  
It enables anyone to generate App Store preview videos that meet Apple’s strict specifications **without any prior video‑editing expertise**.  

The roadmap is organized around three delivery milestones:  

| Milestone | Theme | Target Release | Primary Goal |
|-----------|-------|----------------|--------------|
| **MVP** | Core “one‑click preview” experience | **Q3 2026** | Ship a shippable product that lets a developer create a compliant preview video in ≤ 5 minutes. |
| **v1** | Personalisation & AI‑assist | Q1 2027 | Add branding, voice‑over, music, and fine‑grained timeline editing. |
| **v2** | Collaboration, Marketplace & Cloud Scale | Q3 2027 | Enable teams, a template marketplace, and cloud rendering for large projects. |

---  

## 2. MVP – Must‑Have for Launch  

> **All items marked with `[MVP]` are non‑negotiable for the launch window.**  

| # | Feature | Description | Owner | Status |
|---|---------|-------------|-------|--------|
| **[MVP‑1]** | **Template Library (5 starter templates)** | Pre‑designed, Apple‑compliant layouts (portrait, landscape, 15 s, 30 s). | Product/Design | ✅ Planned |
| **[MVP‑2]** | **Asset Import Wizard** | Drag‑and‑drop screenshots / screen recordings; automatic resizing to required dimensions. | Front‑end | ✅ Planned |
| **[MVP‑3]** | **Auto‑Generated Timeline** | Engine stitches assets into the selected template, adds default transitions, safe‑area cropping, and duration fitting. | Core Engine (vLLM + SGLang) | ✅ Planned |
| **[MVP‑4]** | **Export Engine** | Renders a single MOV/MP4 file that passes Apple’s App Store validation (1080 p, H.264, 30 fps, ≤ 30 s). | DevOps / Rendering | ✅ Planned |
| **[MVP‑5]** | **Web UI (React + Tailwind)** | Clean, responsive UI with step‑by‑step wizard (Template → Assets → Review → Export). | Front‑end | ✅ Planned |
| **[MVP‑6]** | **Project Persistence** | Local browser storage + optional signed‑in “My Projects” (email‑only) for re‑editing. | Backend | ✅ Planned |
| **[MVP‑7]** | **Compliance Checker** | Post‑render validation against Apple’s spec (resolution, aspect, duration, safe‑area). | QA | ✅ Planned |
| **[MVP‑8]** | **Basic Analytics** | Capture conversion (preview‑created, export‑completed) for go‑to‑market validation. | Data | ✅ Planned |
| **[MVP‑9]** | **Documentation & Onboarding** | Quick‑start guide, template preview, FAQ. | PM/Docs | ✅ Planned |

**MVP Success Criteria**  

* ≥ 1 000 unique developers sign‑up within the first 30 days.  
* ≥ 80 % of created videos pass Apple’s automatic validation.  
* Average time‑to‑export ≤ 5 minutes (including rendering on a typical 2023‑MacBook).  

---  

## 3. Version 1 – Personalisation & AI Assist  

| Theme | Feature | Description | Priority | Target Sprint |
|-------|---------|-------------|----------|---------------|
| **Branding** | Custom Logo & Color Scheme | Users can upload a logo and select brand colours that auto‑apply to overlays & text. | High | V1‑S1 |
| **Audio** | Built‑in Music Library (royalty‑free) | Curated 20‑track library; auto‑sync to video tempo. | High | V1‑S2 |
| **Voice‑over** | AI‑generated narration (text‑to‑speech) | One‑click “Add Voice‑over” – select language & style; generated via vLLM TTS model. | Medium | V1‑S3 |
| **Timeline Editing** | Drag‑handle timeline for fine‑tuning clip order & duration. | Gives control without overwhelming novices. | Medium | V1‑S4 |
| **Multi‑language Subtitles** | Auto‑translate UI strings & optional subtitle track. | Expands market reach. | Low | V1‑S5 |
| **Export Profiles** | Direct export to App Store Connect (API upload) & TestFlight preview. | Streamlines developer workflow. | Low | V1‑S6 |
| **Beta‑only Collaboration** | Invite up to 2 teammates to comment on a draft video. | Early team feedback. | Low | V1‑S7 |

**v1
