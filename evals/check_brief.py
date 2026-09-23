#!/usr/bin/env python3
"""Contract checker for prospecting-research replies (spec section 4).

Deterministic checks only. Judgment (is the fact right, is the Because sensible) is scored separately
against evals/cases.md. Usage:
  check_brief.py <brief.md> [...]              one line per file, plus a JSON summary at the end
  check_brief.py --consistency <glob> [...]    compares repeated runs of the same case
"""
import glob, json, re, sys
from collections import Counter

TYPES = r"(catalyst|symptom|intent|absence|competitor)"
DATE = r"(20\d\d|January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)"
LINK = r"(https?://|<http)"


def split(text):
    m = re.search(r"```json\s*(\{.*?\})\s*```", text, re.S)
    js = None
    if m:
        try:
            js = json.loads(m.group(1))
        except Exception:
            js = "INVALID"
    slack = text[: m.start()] if m else text
    slack = re.sub(r"^```\s*$", "", slack, flags=re.M)
    return slack.strip(), js


def line(slack, label):
    """A labelled line: *Label* text, or the older *Label:* text."""
    m = re.search(r"^\*" + re.escape(label) + r":?\*\s*(.*)$", slack, re.M)
    return m.group(1).strip() if m else None


def words(slack):
    """Prose words only: links and the label markers are not prose."""
    t = re.sub(r"<[^>]+>", " ", slack)
    t = re.sub(r"https?://\S+", " ", t)
    return len(t.split())


HEADER_RE = re.compile(r"^\*\[?(REACH OUT|WORTH A LOOK|CHECK FIRST|SKIP|ALREADY A CUSTOMER|NEED THE PERSON|NEED THE COMPANY)\]?[^*\n]*\*", re.M | re.I)


def as_delivered(text):
    """What the rep receives: the surface posts from the header down (surfaces/prospecting-research-slack/src/brief.ts)."""
    m = HEADER_RE.search(text)
    return text[m.start():] if m else text


def check(path, surface=False):
    text = open(path, encoding="utf-8").read()
    if surface:
        text = as_delivered(text)
    slack, js = split(text)
    res = {"file": path, "checks": {}}
    c = res["checks"]
    c["json_valid"] = isinstance(js, dict)
    status = (js.get("verdict") or js.get("status") or "").lower().replace(" ", "_") if isinstance(js, dict) else None
    status = {"already_a_customer": "already_customer", "brief": "brief"}.get(status, status)
    c["no_dashes"] = not re.search("[\u2013\u2014]", text)
    c["no_copy"] = not re.search(r"(?im)^(subject:|hi |hey |dear )|\n(best|cheers|thanks),?\s*\n", slack)
    first = next((l for l in slack.splitlines() if l.strip()), "")

    if re.match(r"^\*ALREADY A CUSTOMER · .+\*$", first) or first.lower().startswith("already a customer"):
        res["kind"] = "customer"
        head = "\n".join([l for l in slack.splitlines() if l.strip()][:3])
        c["customer_link"] = bool(re.search(r"https?://", head))
        c["customer_shape"] = bool(re.match(r"^\*ALREADY A CUSTOMER · .+\*$", first))
        c["json_status"] = status == "already_customer"
    elif re.match(r"^\*NEED THE (PERSON|COMPANY) · ", first) or (not re.search(r"^\*(REACH OUT|WORTH A LOOK|CHECK FIRST|SKIP) · ", slack, re.M) and "_Why them_" not in slack):
        res["kind"] = "ask"
        lines = [l for l in slack.splitlines() if l.strip()]
        c["ask_short"] = len(lines) <= 3
        c["ask_shape"] = bool(re.match(r"^\*NEED THE (PERSON|COMPANY) · .+\*$", lines[0])) if lines else False
        c["json_status"] = status in ("ask_for_person", "ask_for_company", "need_the_person", "need_the_company")
    else:
        res["kind"] = "brief"
        lines = [l for l in slack.splitlines() if l.strip()]
        hi = next((i for i, l in enumerate(lines[:3]) if re.match(r"^\*(REACH OUT|WORTH A LOOK|CHECK FIRST|SKIP) · .+\*$", l)), None)
        c["verdict_header"] = hi is not None
        pre = lines[:hi] if hi else []
        c["refusal_short"] = len(pre) <= 1 and all(len(l.split()) <= 25 for l in pre)
        body = lines[hi:] if hi is not None else lines
        person = body[1] if len(body) > 1 else ""
        c["person_line"] = bool(re.search(r"(verified|not verified|title disputed)", person, re.I)) and bool(re.search(r"(strong fit|partial|caution)", person, re.I))
        slack = "\n".join(body)
        bc = line(slack, "Because") or ""
        # the Because names a cause and the problem the person likely owns, in the present
        c["because_template"] = bool(bc) and bool(re.search(
            r"\b(likely|typically|probably) (?:\w+ ){0,2}owns?\b|no problem\b.{0,40}\bmaps?\b", bc, re.I))
        ow = line(slack, "Open with") or ""
        c["open_with"] = bool(ow) and len(ow.split()) <= 18
        ask = line(slack, "Ask") or ""
        c["ask_question"] = ask.strip().endswith(("?", '?"', "?'")) or (status == "skip" and re.search(r"^(none|nothing)", ask.strip().strip('"'), re.I) is not None)
        c["check_first"] = line(slack, "Check first") is not None
        def why(label):
            m = re.search(r"^_" + label + r"_\s*(.*)$", slack, re.M)
            return m.group(1).strip() if m else None
        wt, wn, wy, wu = why("Why them"), why("Why now"), why("Why you"), why("Why us")
        deeper = why("One level deeper")
        # a Why label with nothing after it means the text was pushed onto the next line
        c["four_whys"] = all(x is not None and len(x.split()) >= 3 for x in (wt, wn, wy, wu))
        # Why now carries the signal only; what it means sits on its own line under it
        c["whys_short"] = all(len((x or "").split()) <= 30 for x in (wt, wn, wy, wu, deeper) if x is not None)
        c["deeper_line"] = deeper is not None or "No signal found" in (wn or "")
        # a Why line is one line in the agent's own words: a quoted page sentence is how it grows
        c["whys_own_words"] = not any(re.search(r"\u201c[^\u201d]{25,}\u201d|\"[^\"]{40,}\"", x or "") for x in (wt, wn, wy))
        wn = wn or ""
        dated = bool(re.search(DATE, wn)) or bool(re.search(r"\b(current|checked)\b", wn, re.I))
        c["why_now"] = ("No signal found" in wn) or (bool(re.search(TYPES, wn, re.I)) and dated)
        src = line(slack, "Sources") or ""
        c["sources_line"] = bool(re.search(r"\]\(https?://|https?://", src))
        top = "\n".join(body[: next((i for i, l in enumerate(body) if l.startswith(("_Why", "*THE EVIDENCE*"))), len(body))])
        top = top.replace("*THE CALL*", "")
        c["top_block_90"] = words(top) <= 95
        c["under_400"] = words(slack) < 400
        # the three tiers: a rep who reads only THE CALL can act
        c["tier_labels"] = all(t in slack for t in ("*THE CALL*", "*THE EVIDENCE*", "*HOW TO WORK IT*"))
        work = re.search(r"\*HOW TO WORK IT\*\s*(.*?)(?=\n\*Sources\*)", slack, re.S)
        wt = work.group(1) if work else ""
        bullets = [l for l in wt.splitlines() if l.strip().startswith(("-", "\u2022"))]
        c["work_bullets"] = 3 <= len(bullets) <= 6 and all(len(b.split()) <= 35 for b in bullets)
        c["work_handoff"] = "copywriting agent" in wt
        # advice to the rep, never a line to send
        c["work_not_copy"] = not re.search(r"(?im)^(subject:|hi |hey |dear )|\u201c[^\u201d]{40,}\u201d", wt)
        res["words"] = words(slack)
        res["top_words"] = words(top)
        if isinstance(js, dict):
            sm = js.get("smart")
            # the verdict follows the evidence: a disputed or unverified person, or a caution fit,
            # cannot be a REACH OUT however good the signal is
            ps = (js.get("person_status") or "").lower()
            fit = ((js.get("why_them") or {}).get("fit") or "").lower()
            c["verdict_fits_evidence"] = not (status == "reach_out" and
                                              (ps in ("title_disputed", "not_verified", "appears_left") or fit == "caution"))
            c["json_status"] = True
            c["json_verdict"] = status in ("reach_out", "worth_a_look", "check_first", "skip")
            c["smart_present"] = isinstance(sm, dict) and all(k in sm for k in "smart")
            r = sm.get("r", {}) if isinstance(sm, dict) else {}
            # on a SKIP there is no cost of inaction to compute, so "not applicable" is the honest answer
            c["smart_r_honest"] = isinstance(r, dict) and (
                r.get("ask") is True or bool(r.get("source")) or status == "skip")
        else:
            c["json_status"] = c["json_verdict"] = c["smart_present"] = c["smart_r_honest"] = c["verdict_fits_evidence"] = False
    res["pass"] = all(c.values())
    res["failed"] = [k for k, v in c.items() if not v]
    return res, js


def consistency(paths):
    """Share of key fields that match the most common value across repeated runs, averaged."""
    rows = []
    for p in paths:
        _, js = check(p)
        if not isinstance(js, dict):
            rows.append({})
            continue
        rows.append({
            "verdict": (js.get("verdict") or js.get("status") or "").lower(),
            "fit": (js.get("why_them") or {}).get("fit"),
            "person_status": js.get("person_status"),
            "persona": ((js.get("why_you") or {}).get("persona") or "").lower()[:25],
            "none_found": (js.get("why_now") or {}).get("none_found"),
            "because_template": (js.get("because") or {}).get("template"),
            "problem": ((js.get("because") or {}).get("problem") or "").lower().replace(" ", "-")[:20],
        })
    keys = [k for k in (rows[0] if rows else {})] or ["status"]
    scores = {}
    for k in keys:
        vals = [r.get(k) for r in rows]
        top = Counter(vals).most_common(1)[0][1] if vals else 0
        scores[k] = top / len(vals) if vals else 0
    return sum(scores.values()) / len(scores), scores


if __name__ == "__main__":
    args = sys.argv[1:]
    surface = "--surface" in args
    args = [a for a in args if a != "--surface"]
    if args and args[0] == "--consistency":
        for g in args[1:]:
            paths = sorted(glob.glob(g))
            score, detail = consistency(paths)
            print(f"{g}: runs={len(paths)} consistency={score:.2f} {json.dumps(detail)}")
        sys.exit(0)
    out = []
    for p in args:
        r, _ = check(p, surface=surface)
        out.append(r)
        print(("PASS " if r["pass"] else "FAIL ") + r["kind"].ljust(8) + p + ("  failed: " + ",".join(r["failed"]) if r["failed"] else "") + (f"  words={r['words']}/top{r.get('top_words',0)}" if "words" in r else ""))
    print(json.dumps({"files": len(out), "pass": sum(r["pass"] for r in out)}))
