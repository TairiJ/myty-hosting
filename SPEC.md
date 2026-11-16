# SPEC.md

## Agreed Scope
- Deploy the supplied **Creator Calculator** on the existing MYTY server infrastructure (Docker, Traefik, HTTPS) without altering or adding any new services.
- Preserve all existing functionality (portfolio site, GitHub repo list, signal log, etc.).
- Use the current `main` branch as the production baseline; the calculator must be reachable via a stable HTTPS URL.
- No additional server installations, upgrades, or feature additions beyond UI redesign already merged.

## Calculator URL
- **HTTPS URL:** https://myty.world#calculator  *(will be live after merging to `main`)*
- **QA verification URL:** https://qa.myty.world#calculator (already functional).

## Evidence Links
| Evidence | Description |
|----------|-------------|
| GitHub Actions CI run | [CI run badge]({CI_RUN_URL}) – shows all checks passed.
| Pull Request | [{PR_NUMBER}]({PR_URL}) – merges `feature/design-lab-review-environment` into `main`.
| Issue | [{ISSUE_NUMBER}]({ISSUE_URL}) – tracks the final submission.
| Unit Test Output | `tests/test_website.py` output (included in `evidence.json`).
| curl verification | HTTPS response headers and snippet of calculator output (included in `evidence.json`).

## Submission
- **Repository URL:** https://github.com/TairiJ/myty-hosting
- Ensure the above `SPEC.md` is present at the repository root when submitting.
