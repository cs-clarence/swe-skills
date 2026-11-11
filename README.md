# swe-skills

Agent skills that wrap the guidelines in [swe-docs](https://github.com/cs-clarence/swe-docs).

## Skills

| Skill | Use it when |
| --- | --- |
| `swe-assess` | Deciding the kind and risk tier of a change before planning |
| `swe-plan` | Planning, sizing and breaking down work |
| `swe-author` | Writing or changing code |
| `swe-review` | Reviewing a change, plan or agent output |
| `swe-debug` | Finding and fixing a defect |
| `swe-release` | Shipping a change and being able to undo it |
| `swe-init` | Optional: setting up swe-docs and these skills in a repo |
| `swe-self-review` | Checking your own change before handing back |

The skills read the guidelines at `docs/guidelines`, so install [swe-docs](https://github.com/cs-clarence/swe-docs) too.

## Install

### Copy or `npx skills`

Each skill is a folder `skills/<name>/` with a `SKILL.md` and sometimes a `references/` folder. Copy the whole folder, not only `SKILL.md`. Copy or install them with any tool that reads that layout, for example `npx skills add cs-clarence/swe-skills` (or `bun x skills add ...`). Add `--skill <name>` to pick skills, and `--copy` to copy instead of symlink; skills land in the selected agent's skills folder, such as `.agents/skills/` or `.claude/skills/`.

### With omni

[projection.omni.yaml](projection.omni.yaml) symlinks each skill into `.agents/skills/`. Register it next to swe-docs in your workspace configuration:

```yaml
projections:
  - source: git
    id: swe-skills
    uri: https://github.com/cs-clarence/swe-skills
    rev: main # pin a tag or commit to control when updates arrive
```

Then run `omni projection sync` from the workspace to create the links.

## Maintaining

Add a skill under `skills/<name>/SKILL.md` and a matching rule in `projection.omni.yaml`. CI lints, validates skills against swe-docs pinned in `.github/swe-docs.ref`, and installs the projection with omni. A weekly job checks against swe-docs `main` and opens an issue on drift. Bump the ref deliberately.
