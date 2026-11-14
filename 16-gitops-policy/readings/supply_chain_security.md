# Reading — Supply-chain security

## Learning objectives

1. Produce or consume an **SBOM** for an image/app you build.
2. **Pin digests** (images and deps) and enable automated update PRs (Dependabot-class).
3. Sketch **cosign** signature verify, **attestations at admission**, and **SLSA**-minded provenance claims honestly.

**Why this matters.** Compromised npm/PyPI packages and unsigned `:latest` images bypass otherwise careful app code. Without SBOMs, pinning, and signature checks, GitOps happily syncs poisoned desired state. On the job, platform and security reviews ask how you know what shipped and whether anyone signed it.

**How it works.**

1. Build an image/artifact in CI with a **locked** dependency file (`package-lock.json`, `poetry.lock`, `go.sum`).
2. Generate an **SBOM** (CycloneDX/SPDX) and store it next to the artifact.
3. Enable **Dependabot** (or Renovate) so bumps are reviewable PRs — not silent `latest`.
4. Sign the image with **cosign** (keyless OIDC is common on GitHub Actions); verify signatures **and** provenance attestations before cluster sync.
5. At **admission** (Kyverno/OPA Gatekeeper/admission webhook), require a verified attestation for the image digest — CI-only checks are skipped when someone force-pushes a tag.
6. Aim for **SLSA**-style provenance (who built what from which source) — claim only the level you actually automated.

```text
source → CI build (pinned deps + digests) → SBOM + cosign sign/attest
        → admission verify (signature + attestation) → GitOps sync
```

### Worked example

```bash
# Conceptual — pin digest + SBOM + sign + attest (tool versions vary)
IMAGE_DIGEST="ghcr.io/example/mailguard-api@sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
cosign sign --yes "$IMAGE_DIGEST"
cosign attest --yes --predicate slsa-predicate.json "$IMAGE_DIGEST"
# Keyless (Fulcio): cosign requires who signed + which OIDC issuer issued the
# cert. Without --certificate-identity / --certificate-oidc-issuer (or --key for
# a public key), verify cannot decide which signatures to trust.
cosign verify "$IMAGE_DIGEST" \
  --certificate-identity="$CERT_IDENTITY" \
  --certificate-oidc-issuer="$CERT_OIDC_ISSUER"
cosign verify-attestation "$IMAGE_DIGEST" \
  --type slsaprovenance \
  --certificate-identity="$CERT_IDENTITY" \
  --certificate-oidc-issuer="$CERT_OIDC_ISSUER"
# Admission: policy admits only digests that pass verify + verify-attestation
# SBOM: syft / trivy image "$IMAGE_DIGEST" -o cyclonedx-json > sbom.json
```

**Pin digests, not mutable tags.** Fixtures and prod overlays should prefer `image@sha256:…` (see [`../fixtures/good_deployment.yaml`](../fixtures/good_deployment.yaml)). Tags move; digests name exact bits for forensics and admission.

### Advisory — cosign legacy JSON bundles (GHSA-fx35-mq7g-6g98)

**Why it matters.** Keyless `cosign verify-blob` / `verify-blob-attestation` with a **legacy JSON `--bundle`** could skip certificate identity checks when the bundle’s `cert` field held a bare public key instead of an X.509 cert ([GHSA-fx35-mq7g-6g98](https://github.com/sigstore/cosign/security/advisories/GHSA-fx35-mq7g-6g98)).

**How to stay safe.**

| Series | Upgrade to (minimum) |
|--------|----------------------|
| cosign v2.x | **2.6.5** |
| cosign v3.x | **3.1.3** |

Prefer the modern Sigstore protobuf bundle (`--new-bundle-format`). OCI image `cosign verify` / `verify-attestation` paths were not affected; still pin a patched CLI in CI so blob/attestation jobs inherit the fix.

### Common misconceptions / what goes wrong

- **“SBOM alone blocks malware.”** It inventories; policy + updates + signatures act on the inventory.
- **“`:latest` or a floating tag is fine for demos.”** Untagged drift breaks forensics; pin **digests** for anything that matters.
- **“CI signed it, so admission can skip attestations.”** A later tag retarget or cluster apply bypasses CI — verify signature + attestation at admission against the digest.
- **“We are SLSA 4.”** Overclaiming fails audits — document the controls you actually run.
- **“Signing replaces vulnerability scanning.”** Signatures prove origin; scanners find known CVEs.
- **“Any cosign version is fine for legacy bundles.”** Unpatched ≤2.6.4 / ≤3.1.2 can bypass identity on legacy blob bundles — upgrade or stop using legacy JSON bundles.

## Read these (verified)

1. [SLSA](https://slsa.dev/)
2. [Sigstore cosign](https://docs.sigstore.dev/cosign/system_config/installation/)
3. [GitHub Dependabot](https://docs.github.com/en/code-security/dependabot)
4. [CycloneDX](https://cyclonedx.org/)

## Next step

Add a one-page note to your Module 16 assignment: which digests you pin, where the SBOM lives, whether signature **and** attestation verify run at admission (not only CI), and which cosign version you pin in the pipeline.
