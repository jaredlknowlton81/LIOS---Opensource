Convert procedural knowledge embedded in a YouTube video into an explicit, reusable ChatGPT capability.

The objective is not simply to summarize the video. The objective is to identify the underlying method, formalize it, and turn it into something ChatGPT can reliably execute and improve through feedback.

Core Pipeline

Source → Transcript → Method → Rules → Failure Modes → Output Contract → Capability → Use → Feedback → Revision



1. Select the Right Video

Good Candidates

Prioritize videos containing:

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

Poor Candidates

Usually skip videos that are primarily:

- Vlogs
- Opinion pieces
- Reactions
- Entertainment
- Personal storytelling

  

2. Transcript → Method

The transcript is evidence, not the final product.

Separate:

- Instruction from commentary
- Procedure from explanation
- Rules from opinions
- Demonstrations from anecdotes
- Reusable patterns from one-off examples

The central question is:

What does this person actually do that another agent could learn to do?

  

3. Extract the Method

Identify the underlying procedure.

Capture:

- Starting conditions
- Required inputs
- Sequence of actions
- Decision points
- Criteria for choosing between alternatives
- Intermediate outputs
- Completion conditions
- Expected result

Convert narrative explanation into operational steps.

  

4. Extract Rules

Make implicit judgment explicit.

Examples of rule forms:

- If X, do Y.
- If X and Y, choose Z.
- Do not proceed when X is missing.
- Prefer A over B when condition C applies.
- When uncertain, verify rather than assume.

Rules should be specific enough for ChatGPT to apply consistently.

  

5. Extract Failure Modes

Identify where the method can break.

For each failure mode capture:

Failure → Cause → Prevention → Recovery

Look for:

- Common mistakes
- Edge cases
- Misinterpretations
- Missing inputs
- Incorrect assumptions
- Situations where the method should not be used
- Conditions requiring human judgment or verification

  

6. Define the Output Contract

Specify what successful execution must produce.

Include:

- Required output
- Structure
- Level of detail
- Quality criteria
- Constraints
- Required checks
- What counts as completion

The output contract makes the capability testable.

  

7. Build the ChatGPT Capability

A reusable capability can be structured as:

SKILL NAME

Purpose

When to use

When not to use

  

INPUTS

Required inputs

Optional inputs

Missing-information behavior

  

METHOD

Step 1

Step 2

Step 3

...

  

RULES

Rule 1

Rule 2

...

  

DECISION LOGIC

If X → do Y

If A → choose B

If uncertain → verify

  

FAILURE MODES

Failure

Why it happens

Prevention

Recovery

  

OUTPUT CONTRACT

Required output

Structure

Quality criteria

Constraints

  

SELF-CHECK

Before finalizing:

□ ...

□ ...

□ ...

  

FEEDBACK LOOP

Observe → Evaluate → Revise

  

The Critical Transformation

Video ≠ Skill

A video contains a mixture of:

- Explanation
- Examples
- Anecdotes
- Opinions
- Context
- Demonstrations
- Procedure

The extraction process transforms these into:

|   |   |
|---|---|
|Video Content|Skill Representation|
|Explanation|Procedure|
|Examples|Patterns|
|Advice|Rules|
|Warnings|Failure modes|
|Demonstration|Execution logic|
|Desired result|Output contract|

The essential transformation is:

Video → Evidence → Method → Operational Rules → Executable Procedure → ChatGPT Capability

  

Skill Extraction vs. Summarization

A summarizer asks:

“What did the creator say?”

A skill extractor asks:

“What capability is embedded in what the creator taught, and how can another agent reliably perform it?”

This distinction is the foundation of the workflow.

  

Integration With the Larger Architecture

The workflow provides a mechanism for converting external knowledge into reusable intelligence:

External Knowledge  
↓  
Skill Extraction  
↓  
Skill Library  
↓  
AI / ChatGPT  
↓  
Projects & Action  
↓  
Results  
↓  
Feedback  
↓  
Skill Revision

This creates a continuous learning loop in which useful methods are not merely remembered—they become reusable capabilities that can be executed, evaluated, and improved.

  

Working Principle

The desired end state is not:

“I watched a useful video.”

It is:

“I extracted a reusable capability from the video, made it executable, tested it, and created a mechanism for improving it.”

  

Reusable Workflow

When given a qualifying YouTube video:

1. Determine whether it contains transferable procedural knowledge.
2. Obtain and clean the transcript.
3. Extract the underlying method.
4. Formalize rules and decision logic.
5. Identify failure modes and boundaries.
6. Define the output contract.
7. Convert the method into a ChatGPT-ready capability.
8. Test it against realistic inputs.
9. Evaluate the results.
10. Revise the capability based on observed failures.
11. Add the improved capability to the Skill Library.