# Practical Test: Containerized CI/CD Deployment to QA and Production

## 🌐 Live Environments
- **Production Site:** [https://myty.world](https://myty.world)
- **QA Testing Site:** [https://qa.myty.world](https://qa.myty.world)

---

## 🚀 Architecture & Promotion Rules

### Branch and Promotion Strategy
- **QA Deployment:**
  - Pushing changes to the `qa` branch triggers the GitHub Actions workflow.
  - The pipeline runs validation unit tests, builds the container image tagged `:qa`, pushes it to GitHub Container Registry (`ghcr.io`), and deploys it automatically to **[https://qa.myty.world](https://qa.myty.world)**.
- **Production Promotion:**
  - After changes are verified on QA, a Pull Request is approved and merged into the `main` branch.
  - Pushes to `main` trigger the automated pipeline, run tests, build the container image tagged `:latest`, push to `ghcr.io`, and deploy to the production flagship domain **[https://myty.world](https://myty.world)**.
- **Environment Isolation:**
  - Both environments run as separate Docker containers behind Traefik reverse proxy on the same host. QA changes remain isolated on `qa.myty.world` until explicitly reviewed, approved, and merged to `main`.

---

## 🔄 CI/CD Pipeline Summary
1. **Trigger:** Automatically triggered on `push` to `main` (Production) and `qa` (QA) branches.
2. **Validation:** Executes Python unit test suite (`tests/test_website.py`) checking HTML validity, meta viewport, title tags, component structure, and Dockerfile integrity. Any failure immediately stops the pipeline before build or deployment.
3. **Container Build & Registry Push:** Builds the production/QA container image from `Dockerfile` using Docker Buildx and publishes the image to GitHub Packages Container Registry (`ghcr.io`).
4. **Automated Server Deployment:** Securely connects to the DigitalOcean Droplet (`142.93.54.117`) over SSH using the dedicated non-root `deployer` account and key-based authentication (stored in GitHub Repository Secrets). It pulls the respective image tag and restarts the targeted container (`site-prod` or `site-qa`) via Docker Compose.

---

## 🔒 SSH Security & Hardening Evidence

A dedicated non-root administrative account `deployer` was provisioned with `sudo` and `docker` group privileges. Direct root SSH login and password authentication have been disabled globally.

### 1. Successful SSH-Key Login as Non-Root User (`deployer`)
```bash
$ ssh deployer@142.93.54.117 "id && docker ps"
uid=1000(deployer) gid=1000(deployer) groups=1000(deployer),27(sudo),987(docker)
CONTAINER ID   IMAGE              COMMAND                  CREATED        STATUS        PORTS                                      NAMES
32b5ac58d919   traefik:v3.7.13    "/entrypoint.sh --ap…"   2 weeks ago    Up 2 weeks    0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp   hosting373-traefik-1
c6d70f407627   httpd:2.4-alpine   "httpd-foreground"       2 weeks ago    Up 2 weeks    80/tcp                                     hosting373-site-1-1
```

### 2. Root SSH Login Rejected
Direct root login is rejected:
```bash
$ ssh root@142.93.54.117 "echo logged in"
root@142.93.54.117: Permission denied (publickey).
```

### 3. Effective SSH Configuration Settings
Verification of effective daemon configuration (`sshd -T`) confirming root login and password authentication are disabled:
```bash
$ ssh deployer@142.93.54.117 "sudo sshd -T | grep -iE 'permitrootlogin|passwordauthentication|kbdinteractiveauthentication'"
permitrootlogin no
passwordauthentication no
kbdinteractiveauthentication no
```

---

## 📋 Test Evidence & Workflow Runs

- **Image Registry Location:** [GitHub Packages (`ghcr.io/tairij/myty-hosting`)](https://github.com/TairiJ/myty-hosting/pkgs/container/myty-hosting)
- **QA Deployment Workflow Run:** [View QA Workflow Run](https://github.com/TairiJ/myty-hosting/actions)
- **Production Deployment Workflow Run:** [View Production Workflow Run](https://github.com/TairiJ/myty-hosting/actions)

### Visible Change Verification
1. **QA Testing:** A visible environment badge (`QA Testing Environment · qa.myty.world`) is rendered on `https://qa.myty.world`.
2. **Production Promotion:** Upon merge to `main`, the change promotes cleanly to `https://myty.world` displaying the production status.
