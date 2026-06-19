# 📄 Product Requirements Document (PRD)  
**Project:** `app-preview-craft`  
**Owner:** Senior Product/Engineering Lead – Axentx  
**Date:** 2026‑06‑19  
**Version:** 1.0  

---

## 1. Problem Statement  

Indie iOS developers must create **App Store preview videos** (15‑30 s) to showcase app features and improve conversion. Current solutions are either:

| Pain Point | Existing Alternatives | Why It Fails for Indie Devs |
|------------|-----------------------|-----------------------------|
| **High skill barrier** | Professional video editors (Final Cut, Adobe Premiere) | Steep learning curve, time‑intensive |
| **Expensive tooling** | Paid SaaS (Animoto, InVideo) | Subscription costs are prohibitive for solo devs |
| **Template scarcity** | Generic stock‑video templates | Not tailored to iOS UI/UX, device frames, or Apple guidelines |
| **Manual asset stitching** | DIY screen‑record + manual editing | Inconsistent quality, risk of guideline violations |

Result: Many indie apps ship without a preview video or with low‑quality clips, leading to **lower discoverability and conversion rates** on the App Store.

---

## 2. Target Users  

| Segment | Characteristics | Primary Needs |
|---------|-----------------|---------------|
| **Indie iOS developers** | Solo or <5‑person teams, limited budget, limited video editing experience | Quick, affordable way to generate Apple‑compliant preview videos |
| **App‑store marketers** (freelancers) | Produce multiple previews for different apps, need consistency | Template library, batch processing |
| **Design‑focused devs** | Comfortable with UI design but not video tools | Ability to import design assets (Sketch, Figma, PNG sequences) directly |

**User Personas** (summarized)

1. **Alex – Solo Developer** – 2‑year iOS dev, launches one app per quarter, wants a 30‑second preview in <2 h without learning Premiere.  
2. **Mia – Freelance App Marketer** – Handles 8‑10 apps/month, needs a repeatable workflow and brand‑consistent templates.  
3. **Ravi – UI/UX Designer** – Provides high‑fidelity mockups, wants to see them animated instantly for stakeholder review.

---

## 3. Product Vision & Goals  

| Vision | Deliver a **template‑driven, AI‑enhanced video creator** that lets indie iOS developers produce Apple‑compliant preview videos in minutes, at < $15 per export. |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------|

### Success Goals (SMART)

| # | Goal | Metric | Target (12 mo) |
|---|------|--------|----------------|
| G1 | **Adoption** – Active users creating previews | Monthly Active Users (MAU) | 4 k |
| G2 | **Conversion** – Free‑to‑paid upgrade | % of free users converting to paid plan | 12 % |
| G3 | **Time‑to‑video** – Reduce creation time | Avg. minutes from first asset upload to final video export | ≤ 8 min |
| G4 | **Compliance** – Apple guideline adherence | % of exported videos passing Apple’s automated preview validation | 100 % |
| G5 | **Revenue** – Direct product revenue | ARR from `app-preview-craft` | $480 k |

---

## 4. Key Features (Prioritized)

Features are ordered by **impact → feasibility → dependency**.  

| Priority | Feature | Description | Acceptance Criteria |
|----------|---------|-------------|----------------------|
| **P1** | **Template Library** | Curated, Apple‑compliant video templates (device frames, transitions, text styles). Includes categories: *Game*, *Productivity*, *Health*, *Education*. | • ≥ 20 templates at launch.<br>• All templates pass Apple’s preview guidelines.<br>• Users can preview template before selection. |
| **P1** | **Asset Import & Auto‑Layout** | Drag‑and‑drop of screenshots, screen recordings, or design assets (PNG, JPEG, MP4, Figma/Sketch export). System auto‑places assets into template placeholders based on aspect‑ratio detection. | • 95 % of imported assets correctly mapped to placeholders.<br>• No manual resizing required for > 80 % of assets. |
| **P1** | **AI‑Assisted Caption & Voice‑over Generation** | Optional LLM‑driven generation of short captions (max 30 words) and synthetic voice‑over (Apple‑compatible .m4a) based on developer‑provided feature description. | • Generated captions ≤ 30 words, grammatically correct 98 % of the time.<br>• Voice‑over syncs with video timeline ±0.5 s. |
| **P2** | **Timeline Editor (Lightweight)** | Simple timeline UI to reorder clips, adjust durations, and add optional background music from a royalty‑free library. | • Users can trim clips to any length ≥ 0.5 s.<br>• Exported video reflects timeline edits accurately. |
| **P2** | **One‑Click Export (Apple‑Ready)** | Export directly to `.mov` (H.264, 1080p) with required metadata (device frame, aspect ratio, duration). | • Export completes ≤ 30 s for a 30‑s video.<br>• Exported file passes Apple’s automated preview validation. |
| **P3** | **Batch Processing** | Process multiple app previews in a single session (e.g., for different locales). | • Users can queue ≥ 5 videos; each exported correctly with its own assets. |
| **P3** | **Collaboration Links** | Share a read‑only preview link (hosted on
