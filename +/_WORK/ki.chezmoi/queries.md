# ki.chezmoi queries

## Open

### FIREWALL-DESKTOP - Accept the Screen Sharing check as it stands

Since 13:06 BST, with Kris. firewall-auto-fix resolved the hung-worker and false-RESTORED findings and added authenticated SSH checks (LAN, tailnet IPv4 and IPv6); firewall-auto-review-2 is NOT READY on one point: the Screen Sharing check reaches the login challenge but cannot log in without a password, so a broken desktop service would still pass. Coordinator view: the rules only filter port 5900 by source address, reaching the challenge proves the firewall passes the connection, and authenticated SSH stays as a way back in. Options: a) accept and run (recommended, high, reviewer disagrees); b) one Screen Sharing check by Kris from sol before the change is confirmed.

## Parked

None (Kris unparked everything, 24 October).
