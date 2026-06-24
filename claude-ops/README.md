# claude-ops/

Task files for the overnight runner. One file per phase, each pointing at the relevant
`src/vlamem/` modules.

**The one hard rule (CLAUDE.md §4): validate before you automate.** Build and verify a
pipeline interactively first; only then queue its task here for overnight runs. An
unvalidated pipeline will run all night and hand back a confident, wrong number.

Tag legend:
- `[CC]` — Claude Code owns it. Safe to queue overnight *once the pipeline is validated*.
- `[YOU]` — human judgment; cannot be delegated.
- `[VERIFY]` — Claude Code builds/runs it; the human must verify before any downstream use.
