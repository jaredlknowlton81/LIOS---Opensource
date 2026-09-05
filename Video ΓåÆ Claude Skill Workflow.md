---
title: Video to Claude Skill Workflow
aliases: [Video to Claude Skill, YouTube to Claude Skill]
tags: [claude-skills, workflow, ai-tools]
type: process
source: "Awa K. Penn — awa-newsletter.beehiiv.com/subscribe"
created: 2026-09-04
---
Video → Skill Extraction Workflow

A repeatable procedure for converting a YouTube video that teaches a clear, reusable method into a Claude Skill.

Purpose

Transform procedural knowledge embedded in a video into an explicit, reusable capability.

Pipeline:

Source → Transcript → Method → Rules → Failure Modes → Output Contract → Skill → Use → Feedback → Revision

1. Select the Right Video

Good candidates

Choose videos containing:

- A repeatable process
- A framework
- A methodology
- A checklist
- A tutorial
- A decision procedure
- A research or analysis method
- A workflow
- A problem-solving system
- A set of reusable rules

Poor candidates

Skip videos that are primarily:

- Vlogs
- Opinion pieces
- Reactions
- Entertainment
- Personal storytelling
- News without a reusable method
- Discussions without an operational process

Selection test

Ask:

Can the video’s method be expressed as a sequence of decisions or actions that another person could repeatedly perform?

If yes, continue.

2. Obtain the Transcript

Capture the complete transcript whenever possible.

Preserve:

- The order of ideas
- Examples
- Repeated rules
- Exceptions
- Warnings
- Qualifications
- Definitions
- Expected outputs

Do not immediately summarize.

First preserve the source material.

3. Extract the Method

Answer these five questions.

1. What problem does this method solve?

State:

- The problem
- Who experiences it
- When the method is useful
- What happens without the method

2. What are the steps?

Reconstruct the procedure in order.

For each step identify:

- Input
- Action
- Decision
- Output
- Condition for moving forward

3. What rules does the creator repeat?

Extract recurring principles.

Separate:

- Hard rules
- Preferences
- Heuristics
- Constraints
- Exceptions

4. What mistakes does the creator warn against?

Identify failure modes.

For each one describe:

- What goes wrong
- Why it goes wrong
- How to detect it
- How to prevent or correct it

5. What should Claude produce?

Define the output contract.

Specify:

- Required output
- Desired structure
- Level of detail
- Quality criteria
- Any formatting requirements

4. Recover the Underlying Logic

Do not merely copy the video’s steps.

Ask:

What is the deeper mechanism that makes this method work?

Identify:

Inputs

What information or resources does the method require?

Transformations

What does the method do to those inputs?

Decisions

Where does judgment enter?

Constraints

What must not happen?

Feedback

How does the user know whether the method worked?

Adaptation

What should change when the method encounters a new situation?

This converts a tutorial into a more general capability.

5. Define the Skill Boundary

Write explicitly:

The skill should be used when:

- …

The skill should not be used when:

- …

The skill requires:

- …

The skill produces:

- …

This prevents the skill from becoming an overly broad collection of instructions.

6. Build

SKILL.md

Use the extracted method to create the Claude Skill.

The skill should contain:

1. Purpose
2. When to use
3. When not to use
4. Inputs
5. Procedure
6. Rules
7. Decision points
8. Failure modes
9. Quality checks
10. Output format
11. Examples, when useful

The instructions should tell Claude what to do, not merely explain what the video creator believes.

7. Preserve Source Attribution

Record the source separately from the operational instructions.

Include:

- Video title
- Creator
- URL
- Date accessed
- Transcript source
- Relevant timestamps

The source provides provenance.

The Skill provides capability.

Do not confuse the two.

8. Test the Skill

Give Claude several test cases.

Test 1 — Normal case

Does the skill perform the intended process?

Test 2 — Ambiguous case

Does it recognize missing information rather than inventing an answer?

Test 3 — Edge case

Does it handle an unusual situation correctly?

Test 4 — Failure case

Does it recognize when the skill should not be applied?

Test 5 — Transfer case

Can it apply the underlying method to a situation different from the original video?

The fifth test is particularly important.

A successful Skill should capture the method, not merely reproduce the video’s example.

9. Evaluate the Result

Ask:

- Does the skill solve the original problem?
- Is the procedure reproducible?
- Are important decisions explicit?
- Are failure modes covered?
- Are assumptions visible?
- Does it know when not to act?
- Does the output match the intended contract?
- Does it generalize beyond the original example?
- Is the skill shorter and clearer than the original transcript?

10. Create the Improvement Loop

After using the Skill, capture:

Input → Skill execution → Output → Failure / Success → Feedback → Revision

Update the Skill when recurring evidence reveals:

- Missing instructions
- Ambiguous rules
- Repeated failure modes
- Unnecessary complexity
- Better decision criteria
- Better output formats

The Skill becomes a living piece of procedural knowledge.

Reusable Prompt

Use this when converting a new video:

Use the skill-creator to build a Claude Skill from this video transcript.

First extract the underlying method rather than merely summarizing the transcript.

Identify:

1. The problem being solved
2. The intended user and use cases
3. The procedure, in order
4. Inputs and outputs for each step
5. Repeated rules and principles
6. Decision points and branching logic
7. Constraints and exceptions
8. Common mistakes and failure modes
9. Quality criteria
10. The desired output contract

Then determine the deeper mechanism that makes the method work.

Define:

- When the skill should be used
- When it should not be used
- What information it requires
- What it should produce
- What assumptions it must not make

Create a concise, reusable SKILL.md that encodes the method as an operational capability.

Preserve the distinction between:

source material → extracted knowledge → operational instructions

Do not invent steps that are not supported by the transcript. Where the source is ambiguous, identify the ambiguity rather than silently filling the gap.

Finally, propose test cases that determine whether the resulting skill actually generalizes beyond the video’s examples.