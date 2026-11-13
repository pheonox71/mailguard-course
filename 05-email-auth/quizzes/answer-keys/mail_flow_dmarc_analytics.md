# Answer key — Mail flow + DMARC analytics

1. MX inbound.
2. Yes.
3. Breaks DKIM; DMARC may fail even for legit mail.
4. none → quarantine → reject.
5. Authenticated Received Chain.
6. Avoid becoming an open relay / sending real mail.
