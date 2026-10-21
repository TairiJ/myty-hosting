# Architectural Decision Record (ADR): Hosting & Deployment Strategy

**Decision Title:** Containerized VPS Deployment (DigitalOcean + Traefik) vs. GitHub Pages  
**Date:** October 2026  
**Status:** **Accepted**  
**Stakeholders:** Course Instructor, Project Lead (Tairi Johnson), Future AI Agents  

---

## 1. Context & Problem Statement

During project review, the instructor recommended evaluating hosting options:
> *"a live site potentially hosted on github pages (but we have my domain so honestly, whatever you feel would make the most sense for the workflow but explain your decision to me)."*

The objective is to establish an industry-standard, secure, and reproducible deployment workflow that demonstrates full DevOps competency while maximizing development agility and visibility.

---

## 2. Options Considered

### Option A: Static GitHub Pages (`tairij.github.io/myty-hosting`)
* **How it works:** GitHub builds static HTML/CSS/JS from a branch (`gh-pages` or `main/docs`) and serves it directly on GitHub's shared CDN infrastructure.
* **Pros:**
  - Zero server maintenance, zero hosting cost.
  - Automatic HTTPS provided by GitHub.
  - Trivial CI/CD configuration (`actions/deploy-pages`).
* **Cons:**
  - **No Containerization:** Fails the core practical exam requirement: *"deploy a simple containerized website to QA and production"*.
  - **No Infrastructure Control:** Cannot demonstrate SSH hardening, non-root user isolation, UFW firewall configuration, or Linux administration.
  - **No Reverse Proxy:** Cannot demonstrate Traefik reverse-proxy routing, dynamic Docker discovery, or multi-subdomain SSL management.
  - **Single Environment Bottleneck:** GitHub Pages typically binds to one branch/environment at a time; simulating true, separate QA and Production subdomains with distinct containers is clumsy or impossible.

---

### Option B: Dedicated Containerized VPS via DigitalOcean + Traefik + Custom Domain (Selected)
* **How it works:** A dedicated Ubuntu 24.04 Droplet (`142.93.54.117`) runs Traefik v3.7 as an edge router. GitHub Actions builds container images from `Dockerfile`, publishes to GitHub Container Registry (`ghcr.io`), and deploys containerized services (`site-prod` and `site-qa`) via SSH using a hardened, non-root `deployer` account. Traefik routes incoming traffic to `myty.world` and `qa.myty.world` with automatic Let's Encrypt TLS certificates.
* **Pros:**
  - **100% Alignment with Course Learning Objectives:** Demonstrates full-stack infrastructure engineering: Docker containerization, image registries, SSH key security, reverse proxies, and automated deployment.
  - **True Multi-Environment Isolation:** Production (`myty.world`) and QA (`qa.myty.world`) run in completely isolated containers. Breaking changes on QA never touch production.
  - **Professional Branding & Real-World Domain:** Uses real-world domains (`myty.world`, `qa.myty.world`, `traefik.myty.world`) configured via DNS A records.
  - **Secure Automated CD:** Demonstrates real remote server orchestration via SSH keys without exposing root access or passwords.
* **Cons:**
  - Requires maintaining the Droplet and monitoring certificate renewals (both automated via Docker restart policies and Traefik ACME challenge).

---

## 3. Decision & Rationale

**We have chosen Option B (DigitalOcean + Traefik + Custom Domain) as our primary application delivery platform.**

### Key Reasons:
1. **Rubric Compliance:** The practical test rubric explicitly states:
   > *"Your own server: Use your own DigitalOcean Droplet to run your website."*  
   > *"A Docker image and automatic deployment: Your workflow must run a basic test or validation, build the Docker image, push it to an image registry, and automatically deploy it to your server."*  
   Choosing GitHub Pages for the main application would forfeit the 20-point "Own Server" criterion and the 20-point "CI/CD and image" criterion.
2. **Pedagogical Value:** Deploying via Docker Compose and Traefik reflects production DevOps environments (Kubernetes, AWS ECS, Docker Swarm) far better than static page hosting.
3. **Environment Separation:** Subdomains `qa.myty.world` and `myty.world` provide genuine isolation where promotion rules can be demonstrated live in class.

---

## 4. The Hybrid Approach: Documentation on GitHub Pages (Optional Extension)

To capture the benefits mentioned by the instructor regarding **visibility**:
- **Application Core:** Deployed to **[https://myty.world](https://myty.world)** and **[https://qa.myty.world](https://qa.myty.world)** via DigitalOcean Droplet.
- **Documentation (Optional):** If a standalone documentation site (e.g. MkDocs, Docusaurus, or book reader) is desired, GitHub Pages can be enabled as a secondary target pointing to `docs/` or the existing `book/` directory.

This architecture delivers **maximum DevOps rigor for grading** while maintaining **effortless visibility for documentation**.
