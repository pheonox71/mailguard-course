# Self-check — Email authentication

1. Expand **SMTP**. Does SMTP+TLS prove the `From:` domain is authorized?
2. Expand **SPF**, **DKIM**, and **DMARC** in one line each.
3. What does `rua=` collect?
4. Why is outbound DLP/hold complementary to DMARC rather than a substitute?
5. **Scenario:** Marketing starts using a new ESP. DMARC aggregate shows SPF fail from new IPs. What should happen before `p=reject`?

---

## Answer key (try first)

1. **Simple Mail Transfer Protocol** — no; TLS encrypts the hop, authorization needs SPF/DKIM/DMARC alignment.
2. SPF: authorized senders in DNS; DKIM: signed content/headers; DMARC: policy + alignment + reporting for the visible From domain.
3. Aggregate pass/fail reports (usually XML) for operators.
4. Hold/DLP address *your* outbound mistakes; DMARC addresses *spoofing of domains* at receivers.
5. Update SPF (and/or DKIM) for the ESP, confirm reports clean up, then tighten policy.
