# GitHub Intelligence Brief — Claude Code Workflow
**Source:** GitHub Trending · Week of April 10, 2026
**Prepared for:** Claude Code sessions across all projects

---

## Executive Summary

Three repos this week directly improve how Claude Code operates —
one is a plug-and-play install, one is a structural workflow model,
and one turns Claude Code into a managed team member.
Combined, they address the three biggest Claude Code failure modes:
inconsistency, lack of structure, and isolation from the broader workflow.

---

## 1. forrestchang/andrej-karpathy-skills → Install Today
**★ 11.4k | +2,230 this week | Markdown | MIT**

### Why It Matters
Andrej Karpathy identified 3 root causes of LLM coding failure.
This repo turned them into a CLAUDE.md that Claude Code reads
automatically at session start. One install, persistent guardrails.

### The 3 Pitfalls It Prevents
1. **Silent assumptions** — model guesses instead of asking.
2. **Over-engineering** — 1,000 lines when 100 would do.
3. **Unintended changes** — touching code it doesn't understand.

### The 4 Principles It Enforces
1. **Think Before Coding** — explicit assumptions, clarifying questions first.
2. **Simplicity First** — only what was asked, no speculative additions.
3. **Surgical Changes** — every changed line traces to the request.
4. **Goal-Driven Execution** — verifiable success criteria, write tests first.

### Implementation — Do This Now
**Via Claude Code plugin (fastest):**
```
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

**Via CLAUDE.md in each repo (manual, more control):**
```bash
# Run in each repo root:
curl -fsSL https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md
```

Apply to: `thekpihub-website`, `atherAI`, `lumina-numerology`.

---

## 2. multica-ai/multica → Claude Code as a Teammate
**★ 5.4k | +3,201 this week | TypeScript | MIT**

### Why It Matters
Multica explicitly supports Claude Code. It wraps agents in a kanban
board, issue tracker, and progress dashboard — turning solo Claude Code
runs into a managed, inspectable workflow. "Your next 10 hires won't be human."

### What It Does
- Assign a GitHub issue to Claude Code like assigning to a colleague.
- Claude Code picks it up, executes, comments updates, reports blockers.
- Real-time progress via WebSocket. Full audit trail.
- Works with Claude Code, Codex, and OpenCode — not locked in.

### Architecture
- Frontend: Next.js 16
- Backend: Go + WebSockets + PostgreSQL 17 (pgvector)
- Runtime: local daemon that detects Claude Code on PATH

### Implementation Guide
**Option A — Cloud (zero setup):**
1. Sign up at multica.ai
2. Connect your GitHub repos
3. Assign issues to Claude Code agent

**Option B — Self-hosted:**
```bash
# Docker Compose deployment
git clone https://github.com/multica-ai/multica
cd multica
docker compose up -d
```
Then connect your repos and start assigning tasks to Claude Code.

**Workflow:**
1. Create GitHub issue for any task (bug, feature, chore)
2. Assign to Claude Code agent in Multica board
3. Claude Code runs, Multica shows live progress + comments
4. Review output, merge or iterate

---

## 3. Yeachan-Heo/oh-my-codex → Workflow Structure Model
**★ 20.4k | +9,737 this week | TypeScript | MIT**

### Why It Matters
Oh My Codex solves the same problem as Karpathy-skills but at the
workflow level: not just how Claude Code should behave, but in what
sequence. The $deep-interview → $ralplan → $ralph → $team loop
is the canonical structured agent workflow pattern of 2026.
Even though it targets Codex CLI, the pattern is directly adoptable
for Claude Code sessions.

### The 4 Canonical Commands (Pattern to Adapt)
| Command | Purpose | Claude Code Equivalent |
|---------|---------|----------------------|
| `$deep-interview` | Clarify scope & requirements | Ask clarifying questions before starting |
| `$ralplan` | Generate plan, get approval | Draft implementation plan, wait for OK |
| `$ralph` | Persistent completion loop | Execute until done, don't stop early |
| `$team` | Parallel agent coordination | Multi-agent tasks with role assignments |

### State Model to Adopt (`.omx/` → `.claude/`)
OMX stores plans, logs, memory, runtime state in `.omx/`.
Adapt this for Claude Code by maintaining a `.claude/` directory with:
```
.claude/
  plans/          # implementation plans before execution
  logs/           # session logs
  memory/         # cross-session context
  hooks/          # pre/post task hooks
```

### Implementation Guide
1. Add the 4-step workflow as a CLAUDE.md instruction block:
   > "Before any task: (1) clarify scope, (2) present plan,
   > (3) wait for approval, (4) execute persistently."
2. Create `.claude/plans/` directory in each repo.
3. Before each Claude Code session, have it write a plan file
   and confirm before touching any code.
4. For complex tasks, use the `$team` pattern: split into
   parallel workstreams with explicit role assignments.

---

## Combined Workflow (Recommended Stack)

```
Karpathy-skills CLAUDE.md       ← behavioral guardrails
        +
Multica issue board              ← task assignment & tracking
        +
OMX workflow pattern in CLAUDE.md ← structured execution sequence
```

**Session start checklist:**
- [ ] CLAUDE.md loaded with Karpathy principles
- [ ] Task assigned via Multica with clear issue description
- [ ] Claude Code runs $deep-interview equivalent before touching code
- [ ] Plan written to `.claude/plans/` before execution
- [ ] Output reviewed in Multica dashboard

---

## Priority Order

| Priority | Action | Effort | Impact |
|----------|--------|--------|--------|
| P0 | Install Karpathy-skills CLAUDE.md in all repos | 5 min | Immediate |
| P1 | Add OMX 4-step workflow to CLAUDE.md | 15 min | High |
| P0 | Set up Multica Cloud for issue-to-agent workflow | 30 min | High |
| P2 | Create `.claude/plans/` structure in each repo | 10 min | Medium |
