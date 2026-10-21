# Product Backlog & Atomic User Stories

> **Single Source of Truth for Sprint Planning & GitHub Issues**  
> **Repository:** [TairiJ/myty-hosting](https://github.com/TairiJ/myty-hosting)

This backlog contains atomic, prioritized user stories formatted for immediate creation as GitHub Issues following the INVEST criteria.

---

## 🏃 Sprint 1: Usability, Mobile Responsiveness, & Health Checks

### Issue #1 — `feat(ui): Add responsive mobile navigation drawer`
- **User Story:**
  As a mobile visitor browsing `myty.world`,  
  I want a responsive slide-out navigation menu,  
  So that I can smoothly navigate between Hero, Jukebox, Pillars, and Calculator on smaller screens.
- **Acceptance Criteria:**
  - [ ] Hamburger toggle button appears on viewports `< 768px`.
  - [ ] Clicking toggle expands an accessible mobile drawer with all navigation links.
  - [ ] Selecting a link automatically closes the drawer and smoothly scrolls to the target anchor.
  - [ ] Pressing `Escape` or tapping outside closes the drawer.
- **Definition of Done:**
  - [ ] Unit tests pass: `python -m unittest tests/test_website.py`.
  - [ ] Tested on Chrome Mobile simulation (iPhone 14 / Pixel 7).
  - [ ] Deployed to QA (`qa.myty.world`) and verified.

---

### Issue #2 — `feat(calculator): Add Radian/Degree toggle for scientific trigonometric functions`
- **User Story:**
  As a STEM student using the scientific calculator,  
  I want to toggle trigonometric calculations between Degrees and Radians,  
  So that I can calculate accurate values for calculus and trigonometry problems.
- **Acceptance Criteria:**
  - [ ] Add a `DEG / RAD` toggle pill inside the scientific keypad.
  - [ ] When in `DEG` mode, `sin(90)` evaluates to `1`.
  - [ ] When in `RAD` mode, `sin(π/2)` evaluates to `1`.
  - [ ] Expression sub-display accurately labels the selected mode (e.g. `sin(90°)` vs `sin(1.57 rad)`).
- **Definition of Done:**
  - [ ] Test assertion added to `tests/test_website.py` verifying angle mode state.
  - [ ] Deployed to QA (`qa.myty.world`) and verified.

---

### Issue #3 — `feat(ops): Implement lightweight HTTP health check endpoint (/healthz)`
- **User Story:**
  As a DevOps engineer operating the Docker deployment,  
  I want an explicit `/healthz` HTTP endpoint returning `200 OK`,  
  So that Traefik and Docker healthcheck daemons can accurately monitor container liveness.
- **Acceptance Criteria:**
  - [ ] Requesting `https://myty.world/healthz` or `https://qa.myty.world/healthz` returns `200 OK` with body `OK`.
  - [ ] Docker Compose `healthcheck` block configured on `site-prod` and `site-qa`.
  - [ ] Healthcheck status visible in `docker ps`.
- **Definition of Done:**
  - [ ] Added to `deploy/docker-compose.yml`.
  - [ ] Verified via `curl -sI https://qa.myty.world/healthz`.

---

## 🏃 Sprint 2: Extended Feature Enhancements

### Issue #4 — `feat(jukebox): Implement multi-track selector and audio streaming preview`
- **User Story:**
  As a fan of Tizz's music visiting the Jukebox,  
  I want to cycle through multiple featured tracks from "Black Love Letterz",  
  So that I can preview different songs with track metadata and streaming links.
- **Acceptance Criteria:**
  - [ ] Jukebox contains tracklist selector (Next/Prev track buttons).
  - [ ] Track title, release year, and duration update dynamically.
  - [ ] Direct links to Spotify and Apple Music update for each track.
- **Definition of Done:**
  - [ ] Tested in QA environment.
  - [ ] Verified across dark and light themes.

---

### Issue #5 — `docs(ci): Add GitHub Pages documentation deployment workflow`
- **User Story:**
  As a visitor or prospective employer inspecting the project repository,  
  I want the repository documentation (`docs/` and `book/`) automatically published to GitHub Pages,  
  So that anyone can read the architecture and textbook in a polished web viewer.
- **Acceptance Criteria:**
  - [ ] Add `.github/workflows/pages.yml` deploying on changes to `docs/**`.
  - [ ] GitHub Pages URL linked in repository header and README.
- **Definition of Done:**
  - [ ] GitHub Pages workflow runs successfully.
  - [ ] Live URL verified.
