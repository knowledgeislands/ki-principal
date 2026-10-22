# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rig-attended-steps

**🤖 → 👤 Handoff to supervisor · Run report at 02:21 BST · last mark 02:12 BST**

---

## Done

Read the attended steps in [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md), [KI-TOOL-RIG-CORE-068](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md), [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) and [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) and turned them into the blocks below. Nothing was run on any host and no repository was edited. The record blocks for KI-TOOL-RIG-CORE-069 and KI-TOOL-RIG-CORE-068 are copied byte for byte by line range; I only added the host guard, the `mkdir` and the `tee` to `~/rig-attended-2026-10-22/<record>-<host>.log`. `sol`'s installed Rig is 0.8.0 and includes KI-TOOL-RIG-CORE-062's discovery.

Checks: all eleven blocks pass `zsh -n` and `bash -n`; the probe, N, P and R are byte-identical to the records.

**At a glance**

| Record | Host | Kind | Time | Needs |
| --- | --- | --- | --- | --- |
| KI-TOOL-RIG-CORE-069 | sol | **LIVE**: `.toml` opens in Zed, not Warp | 2 min | a possible consent dialog (GUI click) |
| KI-TOOL-RIG-CORE-069 | terra | nothing | – | – |
| KI-TOOL-RIG-CORE-068 | terra + sol | observe, plus **LIVE** pf reload R | 30–45 min | **terra's own console throughout**, sudo, NordVPN Connect and Disconnect in its GUI, possibly a **reboot** |
| KI-TOOL-RIG-CORE-047 | sol, terra | observe only | 1 min each | sudo password (privileged pf read) |
| KI-TOOL-RIG-CORE-062 | sol, terra | observe only | 1 min each | none |
| KI-TOOL-RIG-CORE-062 rollout | sol, terra | **LIVE, connection-critical** `rig apply --sudo` | 5 min each | sudo, your explicit go (query RIG-ATT-APPLY) |

Only the KI-TOOL-RIG-CORE-069 block and the observe-only blocks are safe to start and walk away from. Every block appends to its log, so a repeat adds to the evidence rather than overwriting it.

### KI-TOOL-RIG-CORE-069 — sol (LIVE, about 2 minutes, at the screen)

Changes `sol`'s default application for `.toml` from Warp to Zed, which is what the declaration already asks for. It tries the three rungs in order and stops at the first one where all three observers report Zed. Expect `legacy: code -50` (confirming the failure's cause). The `workspace` rung may raise a macOS dialog asking to confirm Zed: click to allow; it waits up to 30 seconds. No sudo and no reboot.

**Pass:** a line `069 RESULT: <rung> took effect`, whose preceding `observe after` line names Zed three times (two `dev.zed.Zed` and `/Applications/Zed.app`). `069 RESULT: no rung took effect` is also valid evidence; paste it.

```sh
mkdir -p ~/rig-attended-2026-10-22 && cat > /tmp/rig-069-probe.js <<'PROBE'
ObjC.import("Foundation"); ObjC.import("AppKit"); ObjC.import("CoreServices");
function s(r) { var v = ObjC.unwrap(ObjC.castRefToObject(r)); return v ? String(v) : "-"; }
function run(a) {
  $.NSBundle.bundleWithPath("/System/Library/Frameworks/UniformTypeIdentifiers.framework").load;
  var UT = $.NSClassFromString($("UTType")), t = UT.typeWithFilenameExtension($("toml"));
  var legacy = $.UTTypeCreatePreferredIdentifierForTag($.kUTTagClassFilenameExtension, $("toml"), null);
  var modern = t.identifier, ws = $.NSWorkspace.sharedWorkspace, app = $.NSURL.fileURLWithPath($(a[1]));
  if (a[0] === "observe") { var u = ws.URLForApplicationToOpenContentType(t);
    return [s(legacy), s($.LSCopyDefaultRoleHandlerForContentType(legacy, $.kLSRolesAll)), ObjC.unwrap(modern),
      s($.LSCopyDefaultRoleHandlerForContentType(modern, $.kLSRolesAll)), u.isNil() ? "-" : ObjC.unwrap(u.path)].join(" "); }
  if (a[0] === "legacy") return "code " + $.LSSetDefaultRoleHandlerForContentType(legacy, $.kLSRolesAll, $(a[2]));
  if (a[0] === "modern") return "code " + $.LSSetDefaultRoleHandlerForContentType(modern, $.kLSRolesAll, $(a[2]));
  if (a[0] === "workspace") { var done = false, err = "none";
    ws.setDefaultApplicationAtURLToOpenContentTypeCompletionHandler(app, t, function (e) {
      err = (e && !e.isNil()) ? ObjC.unwrap(e.localizedDescription) : "none"; done = true; });
    var end = $.NSDate.dateWithTimeIntervalSinceNow(30);
    while (!done && $.NSDate.date.compare(end) < 0)
      $.NSRunLoop.currentRunLoop.runModeBeforeDate($.NSDefaultRunLoopMode, $.NSDate.dateWithTimeIntervalSinceNow(0.1));
    return done ? "completed error=" + err : "timeout"; }
  throw new Error("rung must be observe, legacy, modern or workspace");
}
PROBE
( /usr/sbin/ioreg -rd1 -c IOPlatformExpertDevice | grep -q BFDD9EED-C084-5B5C-BECB-070FF0D05916 || { echo "REFUSED: not sol, nothing run"; exit 1; }
  p() { osascript -l JavaScript /tmp/rig-069-probe.js "$1" /Applications/Zed.app dev.zed.Zed 2>&1; }
  echo "== $(date +%T) before: $(p observe)"
  for r in legacy modern workspace; do
    echo "== $r: $(p $r)"; o=$(p observe); echo "== observe after $r: $o"
    if [ "$(echo "$o" | grep -o -i zed | wc -l | tr -d ' ')" -ge 3 ] && ! echo "$o" | grep -q -i warp; then echo "069 RESULT: $r took effect"; exit 0; fi
  done
  echo "069 RESULT: no rung took effect" ) 2>&1 | tee -a ~/rig-attended-2026-10-22/CORE-069-sol.log
```

Restore, only if you want Warp back: rerun the rung that worked with Warp, for example `osascript -l JavaScript /tmp/rig-069-probe.js modern /Applications/Warp.app dev.warp.Warp-Stable`; the manual fallback is Finder › Get Info › Open with › Change All.

**terra:** nothing. The record keeps the probe to `sol`; `terra`'s `.toml` carry follows the release.

### KI-TOOL-RIG-CORE-068 — terra console with sol beside it (30–45 minutes, not walk-away)

This is the record's attended NordVPN check, steps 1 to 10 in [Attended NordVPN check](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md#attended-nordvpn-check); follow those steps for what each run expects, and stop and paste at any mismatch. It needs your **physical presence at terra's console** (N and R refuse over SSH), the **sudo password** on terra, **GUI clicks** in NordVPN (record its settings, kill switch off, Connect, Disconnect, Quit), and possibly a **restart of terra** (step 9 fallback). N and P only read. **R is LIVE**: it reloads Apple's `/etc/pf.conf` into root and reloads Rig's anchor; its tested restore path is itself, rehearsed at step 4 before NordVPN connects, with NordVPN's own disconnect and a restart as fallbacks. Run order: 1 (GUI) → N terra → P sol → R terra, N terra, P sol → Connect, N terra → P sol → Disconnect and Quit, N terra (R and N again only if `RIG NOT EVALUATED`) → P sol → 10 (GUI).

**Pass:** steps 2 to 4 match the record (`N VERDICT: RIG EVALUATED` with `rig rules 8`; P shows `GREETING RFB` on tailnet 5900, `TIMEOUT` on LAN 5900, `CONNECTS, no greeting` on LAN 22; `R RESULT: apple root reload rc=0 | rig anchor reload rc=0`), steps 5 to 8 are captured whatever they show, and terra ends at step 2's result. Expected at step 5: `root calls com.apple/*: NO`, `anchor "main/*"`, `RIG NOT EVALUATED`.

**N, terra console (observe, sudo):**

```sh
mkdir -p ~/rig-attended-2026-10-22
( /usr/sbin/ioreg -rd1 -c IOPlatformExpertDevice | grep -q 2C1DB95F-EC29-535D-A7CC-333EDF838C02 || { echo "REFUSED: not terra, nothing run"; exit 1; }
  [ -z "$SSH_CONNECTION" ] || { echo "REFUSED: this is an SSH session; use terra's own console"; exit 1; }
  [ -t 0 ] || { echo "REFUSED: no terminal, nothing run"; exit 1; }
  echo "== $(date +%T) NordVPN app: $(/usr/bin/pgrep -f '/NordVPN[.]app/Contents/MacOS/' >/dev/null && echo running || echo 'not running')"
  /sbin/ifconfig | awk '/^[a-z]/{n=$1} /inet6? /{print "== addr", n, $2}' | grep -v -E ' lo0: | fe80:'
  /usr/sbin/scutil --nc list 2>/dev/null | grep "(Connected)" | sed "s/^/== connected: /"
  tun=$(/sbin/ifconfig | awk '/^[a-z]/{n=$1} /inet6 fd7a:115c:a1e0:/{sub(":$","",n); print n; exit}')
  echo "== tailnet interface: ${tun:-NOT FOUND}"
  sudo /bin/zsh -fc '
/usr/sbin/ioreg -rd1 -c IOPlatformExpertDevice | grep -q 2C1DB95F-EC29-535D-A7CC-333EDF838C02 || { print "REFUSED: not terra"; exit 1; }
L=uk.me.kris.rig.firewall.screen-sharing; tun=$1; u=
info=$(/sbin/pfctl -s info 2>/dev/null) || u="$u info"
root=$(/sbin/pfctl -s rules 2>/dev/null) || u="$u root-rules"
loaded=$(/sbin/pfctl -a com.apple/$L -s rules 2>/dev/null) || u="$u rig-rules"
want=$(/sbin/pfctl -nvf /etc/pf.anchors/$L 2>/dev/null) || u="$u anchor-file"
ifs=$(/sbin/pfctl -s Interfaces -v 2>/dev/null) || u="$u interfaces"
kids=$(/sbin/pfctl -a com.apple -s Anchors 2>/dev/null) || u="$u com.apple-anchors"
print "== pf: ${info%%$'\''\n'\''*}"; print "== enable references"; /sbin/pfctl -s References 2>/dev/null
print "== root rules"; print -r -- "$root"; print "== root nat"; /sbin/pfctl -s nat 2>/dev/null
print "== skip"; print -r -- "$ifs" | grep -i skip || print none
print "== root anchors"; /sbin/pfctl -s Anchors 2>/dev/null; print "== com.apple anchors"; print -r -- "$kids"
print "== main anchors"; /sbin/pfctl -a main -s Anchors -v 2>/dev/null
for a in NordVPN $(/sbin/pfctl -a NordVPN -s Anchors -v 2>/dev/null); do print "== $a rules"; /sbin/pfctl -a $a -s rules 2>/dev/null; print "== $a nat"; /sbin/pfctl -a $a -s nat 2>/dev/null; done
norm() { sed -e "s/[[:space:]][[:space:]]*/ /g" -e "s/ $//" -e "s/ keep state$//" -e "s/ flags S\/SA$//" | grep -v "^$"; }
n=$(print -r -- "$loaded" | grep -c .)
[ "$(print -r -- "$loaded" | norm)" = "$(print -r -- "$want" | norm)" ] && c=yes || c=NO
print -r -- "$info" | grep -q "^Status: Enabled" && on=yes || on=NO
print -r -- "$root" | grep -q "^anchor \"com.apple/\*\"" && e=yes || e=NO
m=$(print -r -- "$root" | grep -o "^anchor \"[^\"]*\"" | grep -v "\"com.apple/\*\"" | tr "\n" " ")
pre=$(print -r -- "$root" | sed "/^anchor \"com.apple\/\*\"/,\$d" | grep -v -c -E "^(scrub-|nat-|rdr-|dummynet-)?anchor ")
sib=0; for k in ${(f)kids}; do k=${k//[[:space:]]/}; [ "$k" = com.apple/$L ] && continue; s=$(/sbin/pfctl -a $k -s rules 2>/dev/null | grep -c .); sib=$((sib+s)); done
sk=no; for i in en0 $tun; do print -r -- "$ifs" | grep -i skip | grep -q -w $i && sk="$sk $i"; done
print "N RESULT: pf enabled: $on | rig rules $n, match file: $c | root calls com.apple/*: $e | other root anchors: ${m:-none} | root rules before call: $pre | rules in other com.apple children: $sib | skipped: $sk | unreadable:${u:- none}"
if [ -n "$u" ] || [ -z "$tun" ]; then print "N VERDICT: UNKNOWN - paste everything above"
elif [ $e = NO ] || [ $on = NO ] || [ $n = 0 ]; then print "N VERDICT: RIG NOT EVALUATED - paste everything above"
elif [ $c = yes ] && [ $pre = 0 ] && [ $sib = 0 ] && [ "$sk" = no ]; then print "N VERDICT: RIG EVALUATED"
else print "N VERDICT: UNKNOWN - paste everything above"; fi
' zsh "$tun" ) 2>&1 | tee -a ~/rig-attended-2026-10-22/CORE-068-terra.log
```

**P, sol (observe, no sudo).** First edit `LAN=` and `T6=` to step 2's `en0` and `fd7a:` addresses.

```sh
mkdir -p ~/rig-attended-2026-10-22
( /usr/sbin/ioreg -rd1 -c IOPlatformExpertDevice | grep -q BFDD9EED-C084-5B5C-BECB-070FF0D05916 || { echo "REFUSED: not sol, nothing run"; exit 1; }
  LAN=192.168.1.22; T4=100.96.126.29; T6=
  echo "== $(date +%T) ssh alias terra -> $(ssh -G terra 2>/dev/null | awk '$1=="hostname"{print $2}') (tailnet is $T4)"
  e=$(ssh -o ControlMaster=no -o ControlPath=none -o ConnectTimeout=10 -o BatchMode=yes terra '/usr/sbin/ioreg -rd1 -c IOPlatformExpertDevice | grep -q 2C1DB95F-EC29-535D-A7CC-333EDF838C02 && echo terra' 2>&1)
  [ "$e" = terra ] && echo "P SSH terra: open" || echo "P SSH terra: FAILED ($(print -r -- "$e" | tail -1))"
  probe() { local b z; b=$(nc -G 5 -w 5 $2 $3 </dev/null 2>/dev/null | head -c 12 | tr -d "\n")
    case "$b" in RFB*) echo "P $1 $3: GREETING $b"; return;; esac
    z=$(nc -v -z -G 5 -w 5 $2 $3 2>&1)
    case "$z" in *succeeded*) echo "P $1 $3: CONNECTS, no greeting";; *refused*) echo "P $1 $3: REFUSED";; *timed\ out*|*Timeout*|"") echo "P $1 $3: TIMEOUT";; *) echo "P $1 $3: OTHER ($z)";; esac; }
  probe "tailnet $T4" $T4 5900; probe "LAN $LAN" $LAN 5900; probe "LAN $LAN" $LAN 22
  [ -z "$T6" ] || probe "tailnet $T6" $T6 5900 ) 2>&1 | tee -a ~/rig-attended-2026-10-22/CORE-068-sol.log
```

**R, terra console (LIVE pf reload, sudo; only at step 4, and at step 7 if N says `RIG NOT EVALUATED`):**

```sh
mkdir -p ~/rig-attended-2026-10-22
( /usr/sbin/ioreg -rd1 -c IOPlatformExpertDevice | grep -q 2C1DB95F-EC29-535D-A7CC-333EDF838C02 || { echo "REFUSED: not terra, nothing run"; exit 1; }
  [ -z "$SSH_CONNECTION" ] || { echo "REFUSED: this is an SSH session; use terra's own console"; exit 1; }
  [ -t 0 ] || { echo "REFUSED: no terminal, nothing run"; exit 1; }
  /usr/bin/pgrep -f '/NordVPN[.]app/Contents/MacOS/' >/dev/null && { echo "REFUSED: NordVPN app is running; disconnect and quit it first, nothing run"; exit 1; }
  /usr/sbin/scutil --nc list 2>/dev/null | grep "(Connected)" | grep -v -i tailscale | grep -q . && { echo "REFUSED: a VPN other than Tailscale is connected, nothing run"; exit 1; }
  echo "R START $(date +%T)"
  sudo /bin/zsh -fc '
/usr/sbin/ioreg -rd1 -c IOPlatformExpertDevice | grep -q 2C1DB95F-EC29-535D-A7CC-333EDF838C02 || { print "REFUSED: not terra"; exit 1; }
[ -f /Library/LaunchDaemons/uk.me.kris.rig.firewall.screen-sharing.plist ] && [ -f /etc/pf.anchors/uk.me.kris.rig.firewall.screen-sharing ] || { print "REFUSED: Rig files missing, nothing run"; exit 1; }
/sbin/pfctl -n -f /etc/pf.conf 2>/dev/null || { print "REFUSED: /etc/pf.conf does not parse, nothing run"; exit 1; }
/sbin/pfctl -f /etc/pf.conf; a=$?
/sbin/pfctl -E -a com.apple/uk.me.kris.rig.firewall.screen-sharing -f /etc/pf.anchors/uk.me.kris.rig.firewall.screen-sharing; b=$?
print "R RESULT: apple root reload rc=$a | rig anchor reload rc=$b"
' ) 2>&1 | tee -a ~/rig-attended-2026-10-22/CORE-068-terra.log
```

### KI-TOOL-RIG-CORE-047 — sol then terra (observe only, about 1 minute each, sudo password)

Records the firewall's live state: Rig's version, doctor, and a privileged read of root's ruleset and Rig's anchor. It changes nothing. The record's outstanding acceptance items are NordVPN on and off, which KI-TOOL-RIG-CORE-068's check supplies, and `rig apply --sudo` on terra, which the KI-TOOL-RIG-CORE-062 rollout below supplies. Run terra's at its console or through `ssh -t terra`.

**Pass:** `root calls com.apple/*: yes`, `rig anchor rules: 8` and no VPN other than Tailscale listed as connected. A doctor finding `drifted (anchor-changed)` for the firewall is expected until the rollout rewrites the anchor; any other firewall finding, or `rig anchor rules: 0`, is a fail to paste.

```sh
mkdir -p ~/rig-attended-2026-10-22 && ( /usr/sbin/ioreg -rd1 -c IOPlatformExpertDevice | grep -q BFDD9EED-C084-5B5C-BECB-070FF0D05916 || { echo "REFUSED: not sol, nothing run"; exit 1; }
  echo "== $(date +%T) $(hostname -s) $(rig --version 2>&1)"
  /usr/sbin/scutil --nc list 2>/dev/null | grep "(Connected)" | sed "s/^/== connected: /"
  rig doctor
  r=$(sudo /sbin/pfctl -s rules 2>/dev/null); echo "$r"
  echo "$r" | grep -q '^anchor "com.apple/\*"' && echo "root calls com.apple/*: yes" || echo "root calls com.apple/*: NO"
  echo "rig anchor rules: $(sudo /sbin/pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -s rules 2>/dev/null | grep -c .)" ) 2>&1 | tee -a ~/rig-attended-2026-10-22/CORE-047-sol.log
```

terra: the same block with the guard and log name changed.

```sh
mkdir -p ~/rig-attended-2026-10-22 && ( /usr/sbin/ioreg -rd1 -c IOPlatformExpertDevice | grep -q 2C1DB95F-EC29-535D-A7CC-333EDF838C02 || { echo "REFUSED: not terra, nothing run"; exit 1; }
  echo "== $(date +%T) $(hostname -s) $(rig --version 2>&1)"
  /usr/sbin/scutil --nc list 2>/dev/null | grep "(Connected)" | sed "s/^/== connected: /"
  rig doctor
  r=$(sudo /sbin/pfctl -s rules 2>/dev/null); echo "$r"
  echo "$r" | grep -q '^anchor "com.apple/\*"' && echo "root calls com.apple/*: yes" || echo "root calls com.apple/*: NO"
  echo "rig anchor rules: $(sudo /sbin/pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -s rules 2>/dev/null | grep -c .)" ) 2>&1 | tee -a ~/rig-attended-2026-10-22/CORE-047-terra.log
```

### KI-TOOL-RIG-CORE-062 — sol then terra (observe only, under a minute each, no sudo)

Shows the tailnet addresses Rig discovers and would render as the anchor's only destinations; this is the record's missing read-only confirmation on terra. It changes nothing.

**Pass on sol:** `rig show` names `100.90.130.74` and `fd7a:115c:a1e0::b636:824c`, and the ifconfig line lists exactly one `utun` interface holding both. **Pass on terra:** `rig --version` is 0.8.0 or later, one `utun` interface holds `100.96.126.29` and an `fd7a:115c:a1e0:` address, and `rig show` names both. `tailnet-address-undiscoverable`, or two `utun` interfaces, is a fail to paste.

```sh
mkdir -p ~/rig-attended-2026-10-22 && ( /usr/sbin/ioreg -rd1 -c IOPlatformExpertDevice | grep -q BFDD9EED-C084-5B5C-BECB-070FF0D05916 || { echo "REFUSED: not sol, nothing run"; exit 1; }
  echo "== $(date +%T) $(hostname -s) $(rig --version 2>&1)"
  /sbin/ifconfig | awk '/^[a-z]/{n=$1} /inet6? (100\.|fd7a:115c:a1e0:)/{print "== tailnet addr", n, $2}'
  rig show firewall:screen-sharing-tailnet ) 2>&1 | tee -a ~/rig-attended-2026-10-22/CORE-062-sol.log
```

```sh
mkdir -p ~/rig-attended-2026-10-22 && ( /usr/sbin/ioreg -rd1 -c IOPlatformExpertDevice | grep -q 2C1DB95F-EC29-535D-A7CC-333EDF838C02 || { echo "REFUSED: not terra, nothing run"; exit 1; }
  echo "== $(date +%T) $(hostname -s) $(rig --version 2>&1)"
  /sbin/ifconfig | awk '/^[a-z]/{n=$1} /inet6? (100\.|fd7a:115c:a1e0:)/{print "== tailnet addr", n, $2}'
  rig show firewall:screen-sharing-tailnet ) 2>&1 | tee -a ~/rig-attended-2026-10-22/CORE-062-terra.log
```

### KI-TOOL-RIG-CORE-062 rollout — LIVE, connection-critical, only on your explicit go (about 5 minutes each)

Rewrites each Mac's installed range anchor to the own-address anchor with `rig apply --sudo`, and on terra also closes KI-TOOL-RIG-CORE-047's outstanding `rig apply --sudo`. Run it **after** KI-TOOL-RIG-CORE-068's check, so that check compares against the anchor it was written for. It needs the **sudo password** and your **presence at that Mac's screen**. SSH (port 22) is never in the anchor. Only run it once the observe-only 062 block for that host has passed. It refuses if NordVPN is running, if a VPN other than Tailscale is connected, or if root does not call `com.apple/*`.

**Pass:** `completed=1` and `failed=0`; afterwards `rig anchor rules` is non-zero, and doctor shows no firewall finding. Then run the probe from the other Mac.

**Restore path (tested on terra and sol, 19 October 2026; needs no Rig and works over SSH):** `sudo launchctl bootout system/uk.me.kris.rig.firewall.screen-sharing` then `sudo pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -F all`; this reopens 5900 as before Rig. To put the protection back: `sudo launchctl bootstrap system /Library/LaunchDaemons/uk.me.kris.rig.firewall.screen-sharing.plist`. Always type the locator in full; an empty one once shut terra down.

```sh
mkdir -p ~/rig-attended-2026-10-22 && ( /usr/sbin/ioreg -rd1 -c IOPlatformExpertDevice | grep -q BFDD9EED-C084-5B5C-BECB-070FF0D05916 || { echo "REFUSED: not sol, nothing run"; exit 1; }
  [ -t 0 ] || { echo "REFUSED: no terminal"; exit 1; }
  /usr/bin/pgrep -f '/NordVPN[.]app/Contents/MacOS/' >/dev/null && { echo "REFUSED: quit NordVPN first, nothing run"; exit 1; }
  /usr/sbin/scutil --nc list 2>/dev/null | grep "(Connected)" | grep -v -i tailscale | grep -q . && { echo "REFUSED: a VPN other than Tailscale is connected, nothing run"; exit 1; }
  sudo /sbin/pfctl -s rules 2>/dev/null | grep -q '^anchor "com.apple/\*"' || { echo "REFUSED: root does not call com.apple/*, nothing run"; exit 1; }
  echo "== $(date +%T) apply on $(hostname -s)"
  rig apply --sudo --target firewall:screen-sharing-tailnet
  echo "rig anchor rules: $(sudo /sbin/pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -s rules 2>/dev/null | grep -c .)"
  rig doctor ) 2>&1 | tee -a ~/rig-attended-2026-10-22/CORE-062-sol.log
```

terra: the same with terra's guard and log.

```sh
mkdir -p ~/rig-attended-2026-10-22 && ( /usr/sbin/ioreg -rd1 -c IOPlatformExpertDevice | grep -q 2C1DB95F-EC29-535D-A7CC-333EDF838C02 || { echo "REFUSED: not terra, nothing run"; exit 1; }
  [ -t 0 ] || { echo "REFUSED: no terminal"; exit 1; }
  /usr/bin/pgrep -f '/NordVPN[.]app/Contents/MacOS/' >/dev/null && { echo "REFUSED: quit NordVPN first, nothing run"; exit 1; }
  /usr/sbin/scutil --nc list 2>/dev/null | grep "(Connected)" | grep -v -i tailscale | grep -q . && { echo "REFUSED: a VPN other than Tailscale is connected, nothing run"; exit 1; }
  sudo /sbin/pfctl -s rules 2>/dev/null | grep -q '^anchor "com.apple/\*"' || { echo "REFUSED: root does not call com.apple/*, nothing run"; exit 1; }
  echo "== $(date +%T) apply on $(hostname -s)"
  rig apply --sudo --target firewall:screen-sharing-tailnet
  echo "rig anchor rules: $(sudo /sbin/pfctl -a com.apple/uk.me.kris.rig.firewall.screen-sharing -s rules 2>/dev/null | grep -c .)"
  rig doctor ) 2>&1 | tee -a ~/rig-attended-2026-10-22/CORE-062-terra.log
```

**Probe after each apply, from the other Mac (observe).** Set `H` (target hostname), `TS` and `LAN`: for terra `100.96.126.29` and terra's `en0` address; for sol `100.90.130.74` and `192.168.1.37`. **Pass:** tailnet 5900 `open`, LAN 5900 `closed or filtered`, LAN 22 `open`.

```sh
mkdir -p ~/rig-attended-2026-10-22 && ( H=terra; TS=100.96.126.29; LAN=192.168.1.22
  pr() { /usr/bin/nc -z -G 5 -w 5 $2 $3 >/dev/null 2>&1 && echo "probe $H $1 $2 $3: open" || echo "probe $H $1 $2 $3: closed or filtered"; }
  pr tailnet $TS 5900; pr LAN $LAN 5900; pr LAN $LAN 22 ) 2>&1 | tee -a ~/rig-attended-2026-10-22/CORE-062-probe.log
```

## In Progress

Nothing. Evidence lands in `~/rig-attended-2026-10-22/` on each Mac; paste or point the coordinator at those logs when you are done.

## Queries

**RIG-ATT-ORDER**

**Context:** You asked for something really simple to run now. KI-TOOL-RIG-CORE-069 and the observe-only KI-TOOL-RIG-CORE-047 and KI-TOOL-RIG-CORE-062 blocks take about five minutes in all. KI-TOOL-RIG-CORE-068's NordVPN check takes 30–45 minutes at terra's console and cannot be left running.

**Query:** What do you run tonight?

**Options:** a) (recommended, confidence high - quick, and only the `.toml` handler changes) run KI-TOOL-RIG-CORE-069 on sol and the observe-only KI-TOOL-RIG-CORE-047 and KI-TOOL-RIG-CORE-062 blocks on both Macs now, and do KI-TOOL-RIG-CORE-068 and the rollout in a later sitting at terra. b) do everything now, in the order above. c) KI-TOOL-RIG-CORE-069 only.

**RIG-ATT-APPLY**

**Context:** The KI-TOOL-RIG-CORE-062 rollout rewrites a firewall on both Macs. It is connection-critical. Its restore path was rehearsed on both Macs on 19 October 2026, and SSH is never restricted. RIG-ATTENDED does not say whether you approve a live apply.

**Query:** Do you approve the attended `rig apply --sudo` rollout on sol and terra after KI-TOOL-RIG-CORE-068's check?

**Options:** a) (recommended, confidence medium - the restore path is tested, but it changes both Macs' firewall and should follow KI-TOOL-RIG-CORE-068) yes, in a later sitting after KI-TOOL-RIG-CORE-068. b) yes, tonight. c) not yet.

**RIG-ATT-SOL-NORDVPN**

**Context:** KI-TOOL-RIG-CORE-047's Verify asked for NordVPN on and off on sol. KI-TOOL-RIG-CORE-068 replaced that with a terra-only check, and its N and R blocks refuse anywhere except terra.

**Query:** Does KI-TOOL-RIG-CORE-068's terra check also settle KI-TOOL-RIG-CORE-047's NordVPN item?

**Options:** a) (recommended, confidence medium - both Macs run the same NordVPN helper template, and sol's preflight already read it) yes, terra's check stands for both. b) no; plan a sol variant as follow-up work.
