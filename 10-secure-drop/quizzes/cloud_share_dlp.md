# Quiz — Cloud-share DLP

1. **Why:** Why does email hold miss an “anyone with the link” cloud file that never traversed SMTP as an attachment?
2. **How:** Name three share-link controls and, for each, what fails without it.
3. **How / trade-off:** What does a **presigned URL** buy you operationally — why is it **reusable** until expiry, and why can’t you revoke one raw S3 presign alone (vs signing-credential lifetime)?
4. **Why:** Does Secure Drop replace DMARC? Explain the different problems.
5. **Scenario:** A share link was emailed to the wrong person. What app-level control helps beyond waiting for expiry, and **how** must the download path be designed for that control to work?
6. **Spot the bug:** Audit log stores the full file bytes of every download. Problem and better design?
7. **How:** Why separate a **non-consuming landing** from **redemption**, and which `Referrer-Policy` value should landing/download responses send?
