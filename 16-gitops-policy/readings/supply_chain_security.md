# Reading — Supply-chain security

## Learning objectives

1. Produce or consume an **SBOM** for an image/app you build.
2. **Pin** dependencies and enable automated update PRs (Dependabot-class).
3. Sketch **cosign** signature verify and **SLSA**-minded provenance claims honestly.

**Why this matters.** Compromised npm/PyPI packages and unsigned `:latest` images bypass otherwise careful app code. Without SBOMs, pinning, and signature checks, GitOps happily syncs poisoned desired state. On the job, platform and security reviews ask how you know what shipped and whether anyone signed it.

**How it works.**

1. Build an image/artifact in CI with a **locked** dependency file (`package-lock.json`, `poetry.lock`, `go.sum`).
2. Generate an **SBOM** (CycloneDX/SPDX) and store it next to the artifact.
3. Enable **Dependabot** (or Renovate) so bumps are reviewable PRs — not silent `latest`.
4. Sign the image with **cosign** (keyless OIDC is common on GitHub Actions); verify before cluster sync.
5. Aim for **SLSA**-style provenance (who built what from which source) — claim only the level you actually automated.

```text
source → CI build (pinned deps) → SBOM + cosign signature → policy verify → GitOps sync
```

### Worked example

```bash
# Conceptual — pin + SBOM + sign (tool versions vary)
cosign sign --yes "$IMAGE_DIGEST"
cosign verify "$IMAGE_DIGEST"
# SBOM: syft / trivy image "$IMAGE" -o cyclonedx-json > sbom.json
```

### Common misconceptions / what goes wrong

- **“SBOM alone blocks malware.”** It inventories; policy + updates + signatures act on the inventory.
- **“`:latest` is fine for demos.”** Untagged drift breaks forensics; pin digests for anything that matters.
- **“We are SLSA 4.”** Overclaiming fails audits — document the controls you actually run.
- **“Signing replaces vulnerability scanning.”** Signatures prove origin; scanners find known CVEs.

## Read these (verified)

1. [SLSA](https://slsa.dev/)
2. [Sigstore cosign](https://docs.sigstore.dev/cosign/system_config/installation/)
3. [GitHub Dependabot](https://docs.github.com/en/code-security/dependabot)
4. [CycloneDX](https://cyclonedx.org/)

## Next step

Add a one-page note to your Module 16 assignment: what you pin, where the SBOM lives, and whether verify runs in CI or admission.
