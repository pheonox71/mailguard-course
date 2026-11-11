# Worksheet — Cloud-share DLP

## Design a share object

Fields for a mock `ShareLink` (bullets OK): id, owner, visibility enum, expires_at, revoked_at, audit events.

## Short questions

1. What happens when an operator **revokes** a link that was already copied to chat?
2. Why is “passworded ZIP in email” a weak substitute for expiring authenticated links?
3. Map two audit events you would store (upload, download, revoke, expiry).
4. How does this differ from MailGuard’s email **hold** state?

## Mini lab (conceptual or coded)

Implement or sketch: create share → list visibility → revoke → attempt download fails with clear error. Local object store OK.
