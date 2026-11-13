# Answer key — Mail flow + DMARC analytics

1. MX decides where recipient MX lookups deliver inbound mail. Outbound smart-hosts relay mail so the visible sending IP may no longer match SPF for the envelope domain.
2. Yes — DMARC needs at least one aligned pass; aligned DKIM rescues legit mail when SPF breaks after relay.
3. Breaks DKIM; DMARC may fail even for legit mail, and SPF assumptions after rewrite are often wrong too.
4. Reports show which sources are legit-but-unaligned vs spoof; jumping to reject breaks those sources without a fix window.
5. Relays invalidate SPF and can break the authentication story; ARC lets downstream receivers see prior authentication results across the chain.
6. Avoid becoming an open relay / sending real mail — the lab is for flow mechanics only.
