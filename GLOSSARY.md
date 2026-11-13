# Glossary

Shared terms for **mailguard-course**. Acronyms appear as **full name (ABBREV)** with a one-line meaning. Prefer this list when a module reading has not expanded a term yet; readings still expand on first use in their own file.

**Authorship:** AI-generated course scaffolding.

---

## Identity & authentication

| Term | Meaning |
|------|---------|
| **Multi-Factor Authentication (MFA)** | Require more than one independent factor (e.g. password + device code) to authenticate. |
| **One-Time Password (OTP)** | Short-lived code used once (or within a short window) as a second factor. |
| **HMAC-based One-Time Password (HOTP)** | OTP from a shared secret and an incrementing counter (RFC 4226). |
| **Hash-based Message Authentication Code (HMAC)** | Keyed hash proving integrity/authenticity of a message; building block for HOTP/TOTP. |
| **Time-based One-Time Password (TOTP)** | HOTP where the counter is derived from Unix time ÷ time step (often 30s; RFC 6238). |
| **OpenID Connect (OIDC)** | Identity layer on OAuth 2.0: login + ID token so apps can know *who* signed in. |
| **OAuth 2.0** | Authorization framework for delegated access (tokens), not a full login protocol by itself. |
| **JSON Web Token (JWT)** | Compact signed (often) token format used to carry claims between parties. |
| **Single Sign-On (SSO)** | One login session used across multiple apps — often via OIDC/SAML. |
| **Security Assertion Markup Language (SAML)** | XML-based federated login protocol; older enterprise alternative/complement to OIDC. |
| **Web Authentication (WebAuthn)** | Browser API for phishing-resistant authenticators (security keys / passkeys). |
| **Passkey** | User-friendly WebAuthn credential (often synced or device-bound) for phishing-resistant sign-in. |
| **Identity Provider (IdP)** | Service that authenticates users and issues assertions/tokens to relying apps. |
| **Zero Trust Network Access (ZTNA)** | App-scoped remote access that verifies identity (and often device context) instead of broad VPN LAN admission. |
| **Virtual Private Network (VPN)** | Encrypted tunnel into a network; classical remote access often admits users to wide internal ranges. |
| **Device certificate / posture** | Cryptographic device identity or health signals used as extra access context (conceptually; not a full MDM course). |

## Email security & MailGuard domain

| Term | Meaning |
|------|---------|
| **Data Loss Prevention (DLP)** | Policies that detect/block sensitive data leaving approved channels (e.g. email or cloud shares). |
| **Missend** | Accidental delivery to the wrong recipient (typo, wrong autocomplete, mixed internal/external). |
| **Business Email Compromise (BEC)** | Fraud that hijacks or spoofs business email to trick victims (e.g. fake payment requests). |
| **Simple Mail Transfer Protocol (SMTP)** | Store-and-forward protocol that moves email between servers (and submission clients). |
| **Sender Policy Framework (SPF)** | DNS-published authorization of which hosts may send mail for a domain. |
| **DomainKeys Identified Mail (DKIM)** | Cryptographic signature on email with a public key published in DNS. |
| **Domain-based Message Authentication, Reporting and Conformance (DMARC)** | Policy + alignment of the visible From domain with SPF/DKIM results, plus reporting. |
| **Mail Exchanger (MX)** | DNS record type that names the hosts that accept mail for a domain. |
| **Hold / suspend** | Temporary quarantine of a message pending review or timeout — neither allow nor hard reject. |
| **Allow / reject (discard)** | Policy actions: pass through vs block (and often drop) the message. |
| **First-match-wins** | Evaluate ordered rules; stop at the first matching rule’s action. |
| **Secure transfer** | Controlled file sharing (upload, store, expiring link, audit) instead of raw email attachments. |
| **Cloud-share DLP** | Governing file links (visibility, expiry, revoke, audit) beyond the email path. |
| **Software as a Service (SaaS)** | Vendor-hosted software delivered over the network; MailGuard is a *learning* SaaS shape, not a product clone. |

## Cryptography (applied literacy)

| Term | Meaning |
|------|---------|
| **Transport Layer Security (TLS)** | Protocol that encrypts and authenticates network connections (e.g. HTTPS, SMTP with TLS). |
| **X.509 certificate** | Signed binding of a public key to a name (and related fields), used in TLS trust chains. |
| **Authenticated Encryption with Associated Data (AEAD)** | Encryption that also detects tampering; associated data is authenticated but not encrypted. |
| **Hash-based Message Authentication Code (HMAC)** | Keyed hash proving integrity/authenticity; also listed under Identity when used for OTP. |

## APIs, apps & workers

| Term | Meaning |
|------|---------|
| **Application Programming Interface (API)** | Contract for how clients talk to a service (here, often HTTP/JSON). |
| **FastAPI** | Modern Python web framework for building APIs with type hints and OpenAPI docs. |
| **OpenAPI** | Standard description of an HTTP API (formerly Swagger); used for docs and client generation. |
| **Create, Read, Update, Delete (CRUD)** | Basic resource operations on stored entities. |
| **Single-Page Application (SPA)** | Frontend that updates in-browser (e.g. Vue admin) talking to an API. |
| **End-to-End (E2E)** | Test that drives the full user path (UI → API → storage), not just one unit. |
| **Dead-Letter Queue (DLQ)** | Side queue for messages that failed processing after retries. |

## Cloud, CI & platform

| Term | Meaning |
|------|---------|
| **Amazon Web Services (AWS)** | Major public cloud; used here for deploy/storage/queue practice. |
| **Infrastructure as Code (IaC)** | Declare infra in files (e.g. Terraform) and apply via tooling, not click-ops alone. |
| **Identity and Access Management (IAM)** | Cloud users/roles/policies controlling who can do what on which resources. |
| **Continuous Integration (CI)** | Automated build/test (and often lint) on each change, typically via GitHub Actions here. |
| **Software Bill of Materials (SBOM)** | Inventory of components/dependencies in an artifact for supply-chain review. |
| **Kubernetes (K8s)** | Container orchestration API; local practice via kind/minikube before managed clusters. |
| **Elastic Kubernetes Service (EKS)** | AWS-managed Kubernetes control plane (named as a *next step*, not required locally). |
| **OpenTelemetry (OTel)** | Vendor-neutral APIs/SDKs for traces, metrics, and logs. |
| **Site Reliability Engineering (SRE)** | Practice of running reliable systems with engineering + operations habits (SLIs/SLOs, postmortems). |
| **Service Level Indicator (SLI)** | Quantitative measure of one aspect of service level (e.g. success ratio, latency). |
| **Service Level Objective (SLO)** | Target value/range for an SLI over a window. |
| **Error budget** | Allowed unreliability implied by an SLO; guides reliability vs feature investment. |
| **GitOps** | Desired cluster/app state lives in Git; a controller syncs the live system to match. |
| **Policy-as-code** | Express admission/security rules as code/config (e.g. Kyverno, Conftest) checked in CI or cluster. |

## Quality & process

| Term | Meaning |
|------|---------|
| **Domain-Specific Language (DSL)** | Mini-language for one problem domain; Challenge Gym deliberately *avoids* inventing one. |
| **Request for Comments (RFC)** | IETF (and similar) standards documents (e.g. RFC 6238 for TOTP). |
| **Open Worldwide Application Security Project (OWASP)** | Community publishing practical app-sec guidance (cheat sheets, Juice Shop, etc.). |
| **National Institute of Standards and Technology (NIST)** | U.S. standards body; SP 800-63 covers digital identity; SP 800-207 covers zero trust architecture. |
| **STRIDE** | Threat-category mnemonic: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege. |
| **Software Assurance Maturity Model (SAMM)** | OWASP model for measuring secure-SDLC practices (awareness in this course — not a cert). |
| **Secure Software Development Life Cycle (SDLC)** | Building security activities into requirements, design, build, test, and operate. |
| **Open-source software (OSS)** | Software with source available under an open license; contribution practice is an optional stretch here. |

---

When you introduce a new shared acronym in a module, add a row here and expand it on first use in that module’s reading.
