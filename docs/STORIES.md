# STORIES.md – app‑preview‑craft  

## Overview  
**Goal:** Deliver a lightweight, template‑driven video creator that lets indie iOS developers generate App Store preview videos in minutes, without any prior video‑editing expertise.  

The backlog is organized into **Epics** and ordered to support a **Minimum Viable Product (MVP)** launch. Each story follows the “As a …, I want …, so that …” format and includes concrete Acceptance Criteria (AC).

---  

## EPIC 1 – Core Video Creation  

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| 1 | **As an indie iOS developer, I want to select a pre‑built video template, so that I can start a preview video that already complies with Apple’s layout guidelines.** | - A gallery of ≥ 5 Apple‑compliant templates is displayed on the landing screen.<br>- Templates show a thumbnail, duration (15 s, 30 s, 60 s), and supported device frames (iPhone 14, iPhone 14 Pro, iPad).<br>- Selecting a template opens the **Project Builder** with the chosen template pre‑loaded. |
| 2 | **As a developer, I want to drag‑and‑drop my app screenshots into the template timeline, so that the visual flow matches my app’s user journey.** | - Screenshots can be imported from local disk or the macOS Photos library.<br>- Each screenshot appears as a draggable thumbnail on the timeline.<br>- The system enforces Apple’s required aspect ratios (16:9, 19.5:9) and warns on mismatches.<br>- Dropping a screenshot onto a placeholder automatically scales/crops to fit. |
| 3 | **As a developer, I want the tool to automatically generate transitions and timing between screenshots, so that the video looks polished without manual tweaking.** | - Default transition (cross‑fade) is applied between consecutive screenshots.<br>- Total video length matches the selected template’s target duration (e.g., 30 s).<br>- Users can preview the auto‑timed video in‑app with a “Play” button. |
| 4 | **As a developer, I want to add optional overlay text (title, caption) to any frame, so that I can highlight key features.** | - An “Add Text” button appears on each timeline slot.<br>- Text editor supports up to 3 lines, custom font (from a limited Apple‑approved list), size, color, and position presets (top, center, bottom).<br>- Real‑time preview updates as text is edited. |
| 5 | **As a developer, I want to preview the final video before export, so that I can ensure it meets my expectations.** | - A “Preview” mode plays the assembled video at 1× speed with audio (if added).<br>- Users can scrub the timeline and jump to any frame.<br>- The preview respects the final export resolution (1080 p). |

---  

## EPIC 2 – Asset & Audio Management  

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| 6 | **As a developer, I want to attach background music from a curated royalty‑free library, so that my preview feels engaging without licensing headaches.** | - A “Music Library” panel lists ≥ 20 tracks, each with duration ≤ 60 s.<br>- Users can preview a track, select it, and set start offset (0‑30 s).<br>- Selected track is automatically trimmed/faded to match video length. |
| 7 | **As a developer, I want to upload a custom audio file (e.g., a voice‑over), so that I can personalize the narration.** | - Supported formats: MP3, AAC, WAV.<br>- File size limit: 20 MB.<br>- Uploaded audio appears on a separate “Voice‑over” track with waveform preview.<br>- Users can adjust volume relative to background music. |

---  

## EPIC 3 – Export & Compliance  

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| 8 | **As a developer, I want to export the video in Apple‑required specifications (1080 p, H.264, .mov/.mp4), so that I can upload it directly to App Store Connect.** | - Export button generates a file with: 1920 × 1080 px, 30 fps, H.264 codec, ≤ 500 MB.<br>- File format defaults to .mov but .mp4 is also available.<br>- Export completes within 30 seconds for a 30‑second video on a typical MacBook Pro (M1). |
| 9 | **As a developer, I want the tool to validate the final video against Apple’s App Store preview guidelines, so that I avoid re‑submission failures.** | - After export, a validation step checks: duration (15/30/60 s), resolution, aspect ratio, safe‑area margins, and audio level limits.<br>- Any violations are listed with actionable messages (e.g., “Video exceeds 30 s – trim or select a shorter template”). |
| 10 | **As a developer, I want a one‑click “Upload to App Store Connect” option, so that I can skip manual file transfer.** | - Users can link their Apple Developer account via OAuth (App Store Connect API).<br
