# Quiz — Email authentication

1. Why does SMTP+TLS **not** prove the `From:` domain is authorized — what problem do SPF/DKIM/DMARC exist to solve?
2. Why does SPF check the envelope/HELO identity while DMARC still needs **alignment** with the visible `From:`?
3. Why collect `rua=` aggregate reports before `p=reject` — what fails if you skip them?
4. Why is outbound DLP/hold complementary to DMARC rather than a substitute?

5. **Scenario:** Marketing starts using a new ESP. DMARC aggregate shows SPF fail from new IPs. What should happen before `p=reject`, and why might SPF includes alone be insufficient?

6. **Spot the bug:** A DMARC record places `p=reject` before `v=DMARC1`. What happens and why?
