# Skills root index

Personal, forked skill library. Category dirs live under `skills/`.

> 摘要: 我自己的技能库总目录说明（哪些技能、怎么装、怎么更新）
> 标签: 技能库, skills, 索引

## Layout

    skills/
      engineering/    real-engineering flows (tdd, implement, to-prd, triage, ...)
      productivity/   interviewing, handoff, writing, teaching
      personal/       article editing, obsidian vault
      in-progress/    drafts not yet stable
      misc/           small utilities
      companion/      anime-desktop-companion (has a ~1.4 GB runtime, do NOT index it)

## How a skill is defined

A skill is a directory containing `SKILL.md` whose frontmatter is:

    ---
    name: kebab-case-name
    description: One line: what it does + when to use it (this line is what the agent reads to decide).
    ---

Then the body: overview, steps, commands, pitfalls, verification.

## Commands

    # list every skill in this repo
    python "scripts\index_skills.py"   # 在仓库根目录执行

    # new skill from template
    mkdir "SKIILS仓库\skills\<category>\<my-skill>" ; copy "skills\_template\SKILL.md" ...
