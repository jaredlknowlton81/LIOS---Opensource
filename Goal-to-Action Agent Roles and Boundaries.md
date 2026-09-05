
1. Architectural Principle

The system should not have one agent responsible for everything.

Instead:

Each agent owns a specific transformation of information and has authority only within that boundary.

The agents cooperate through shared context and explicit handoffs.

The central architecture is:

Goal → Orchestration → Projects → Areas → Resources → Actions → Experience → Feedback → Ledger → Learning → Adaptation

  

2. Core Agent Roles

Agent 1 — Goal Agent

Mission

Convert human intention into a defined desired state.

Owns

- Goal clarification
- Purpose
- Desired outcome
- Success criteria
- Time horizon
- Constraints
- Priority

Produces

Goal Specification

Boundary

The Goal Agent does not decide how the goal should be accomplished.

It answers:

Where are we trying to go?

It does not answer:

How do we get there?

  

3. Decomposition Agent

Mission

Determine what must become true for the goal to succeed.

Owns

- Outcome decomposition
- Required conditions
- Problems
- Capabilities
- Decisions
- Dependencies
- Unknowns

Produces

Outcome Map

Boundary

It does not create arbitrary tasks.

It identifies conditions and requirements, leaving implementation to the Project and Action layers.

  

4. Project Agent

Mission

Convert required outcomes into bounded bodies of work.

Owns

- Project identification
- Project creation
- Scope
- Project outcomes
- Prioritization
- Project dependencies
- Project status

Produces

Project Map

Boundary

The Project Agent does not own the user’s entire life or organizational structure.

It owns:

temporary work organized around an outcome.

  

5. Area Agent

Mission

Maintain awareness of persistent responsibilities affected by goals and projects.

Owns

- Areas of responsibility
- Area health
- Ongoing obligations
- Cross-project impacts
- Conflicts between responsibilities

Produces

Area Context

Boundary

An Area is not a project.

The Area Agent should therefore resist turning every concern into a project.

Its question is:

What persistent responsibility does this work affect?

  

6. Resource Agent

Mission

Discover and connect the capabilities required to accomplish the work.

Owns

- Knowledge
- Documents
- People
- Relationships
- Tools
- Money
- Materials
- Data
- Infrastructure
- Existing work
- Missing resources

Produces

Resource Map

Boundary

The Resource Agent discovers and connects resources.

It does not independently decide the overall strategy.

  

7. Planning Agent

Mission

Turn the Goal → Project → Area → Resource relationships into an executable path.

Owns

- Dependencies
- Sequence
- Priorities
- Decision points
- Next-action selection
- Expected evidence
- Risk identification

Produces

Action Plan

Boundary

The Planning Agent should not execute the plan.

Its job ends when there is a justified next intervention.

  

8. Action Agent

Mission

Execute authorized actions in the environment.

Owns

- Tool execution
- Communication
- Research
- Creation
- Transactions
- Operational tasks
- Recording execution results

Produces

Experience / Execution Record

Boundary

The Action Agent does not silently redefine the goal.

If execution reveals that the plan is wrong, it reports the discrepancy.

It does not unilaterally change the strategy.

  

9. Observation / Feedback Agent

Mission

Determine what actually happened and compare it with what was expected.

Owns

- Results
- Deviations
- Success/failure
- Unexpected events
- New information
- Emerging dependencies

Produces

Feedback Record

Boundary

It observes first.

It should not automatically convert every observation into a strategic decision.

  

10. Ledger Agent

Mission

Maintain persistent relational context.

Owns

- Decisions
- Relationships
- Project state
- Area state
- Resource state
- Outcomes
- Learning
- Historical context
- Provenance
- Important changes

Produces

Updated Context

Boundary

The Ledger Agent records and maintains context.

It should not invent context.

It should distinguish:

Observed → Reported → Inferred → Unknown

  

11. Learning Agent

Mission

Extract reusable knowledge from accumulated experience.

Owns

- Pattern recognition
- Lessons learned
- Successful methods
- Failed approaches
- New principles
- Reusable knowledge
- Updated assumptions

Produces

Learning

Boundary

Learning is not the same as fact.

The Learning Agent should preserve uncertainty and evidence.

A hypothesis should not become a fact merely because an agent inferred it.

  

12. Adaptation Agent

Mission

Determine whether the strategy should change based on new information.

Owns

- Strategy revision
- Priority changes
- Project changes
- Resource changes
- Goal revision
- New project identification
- Next-direction selection

Produces

Adapted Strategy

Boundary

The Adaptation Agent can recommend or initiate changes within its authority, but significant changes to human-defined goals should require human confirmation.

  

13. Orchestrator Agent

Mission

Coordinate the entire system.

The Orchestrator is the navigation layer.

Owns

- Agent sequencing
- Handoffs
- State transitions
- Conflict detection
- Missing-information detection
- Escalation
- Next-agent selection
- Goal completion detection

Does not own

- Domain expertise
- Permanent knowledge
- Every decision
- Every action
- Every resource

The Orchestrator asks:

Which agent needs to act next?

  

14. Human / Principal

There should be one role above the autonomous system:

Human Principal

Owns

- Fundamental goals
- Values
- High-consequence decisions
- Irreversible commitments
- Major resource commitments
- Strategic changes
- Permission boundaries

The system can navigate toward the goal.

It should not quietly redefine what the human ultimately wants.

  

15. Authority Hierarchy

                  HUMAN PRINCIPAL

                         │

                         ▼

                   ORCHESTRATOR

                         │

        ┌────────────────┼────────────────┐

        ▼                ▼                ▼

      GOAL            PROJECT           AREA

      AGENT            AGENT            AGENT

        │                │                │

        └────────────────┼────────────────┘

                         ▼

                    RESOURCE

                      AGENT

                         │

                         ▼

                     PLANNER

                         │

                         ▼

                      ACTION

                       AGENT

                         │

                         ▼

                   OBSERVATION

                       AGENT

                         │

                         ▼

                      LEDGER

                       AGENT

                         │

                         ▼

                     LEARNING

                       AGENT

                         │

                         ▼

                    ADAPTATION

                       AGENT

                         │

                         └────────→ ORCHESTRATOR

  

16. The Critical Boundary: Planning vs. Acting

This is one of the most important boundaries.

Planner

Determines:

What should happen next?

Action Agent

Determines:

How do I execute the authorized action?

Feedback Agent

Determines:

What actually happened?

Adaptation Agent

Determines:

What should change because of what happened?

Keeping these separate creates an observable control loop.

  

17. The Critical Boundary: Memory vs. Intelligence

Another important separation:

Ledger

What happened / what is known?

Learning

What can we infer from what happened?

Orchestrator

What needs to happen next?

This prevents the persistent memory layer from becoming an uncontrolled reasoning layer.

  

18. The Critical Boundary: Goal vs. Strategy

The system must distinguish:

Goal = desired destination

Strategy = current theory for reaching it

Project = bounded implementation vehicle

Action = immediate intervention

Therefore:

GOAL

  │

  ├── relatively stable

  │

  ▼

STRATEGY

  │

  ├── adaptable

  │

  ▼

PROJECT

  │

  ├── bounded

  │

  ▼

ACTION

  │

  ├── immediate

  │

  ▼

RESULT

A failed action should normally change the strategy, not automatically change the goal.

  

19. Escalation Rules

The system should escalate when:

- The goal is ambiguous.
- Goals conflict.
- Values are involved.
- A major irreversible decision is required.
- A high-impact commitment is required.
- The available evidence is insufficient.
- Agents disagree materially.
- A constraint cannot be resolved.
- The system proposes changing the fundamental goal.
- The action exceeds its authorization boundary.

The principle is:

Autonomy increases as reversibility and confidence increase.

  

20. Agent Contract

Every agent should have five explicit properties:

1. Input

What information does the agent receive?

2. Responsibility

What transformation does it perform?

3. Output

What artifact does it produce?

4. Authority

What decisions may it make?

5. Boundary

What decisions must it refuse or escalate?

This makes agents composable.

  

21. The Complete Multi-Agent Loop

HUMAN INTENTION

      ↓

GOAL AGENT

      ↓

DECOMPOSITION AGENT

      ↓

PROJECT AGENT

      ↓

AREA AGENT

      ↓

RESOURCE AGENT

      ↓

PLANNING AGENT

      ↓

ACTION AGENT

      ↓

OBSERVATION / FEEDBACK AGENT

      ↓

LEDGER AGENT

      ↓

LEARNING AGENT

      ↓

ADAPTATION AGENT

      ↓

ORCHESTRATOR

      │

      ├── Goal achieved → CLOSE

      │

      ├── Goal changed → GOAL AGENT

      │

      ├── Strategy changed → PROJECT / PLANNING

      │

      ├── Missing resource → RESOURCE AGENT

      │

      ├── Missing context → LEDGER / RESEARCH

      │

      └── Next action → PLANNING AGENT

22. The Deeper Architecture

The most important insight is that these agents are not simply a collection of specialized assistants.

They form a control system.

             DESIRED STATE

                  │

                  ▼

             ORCHESTRATE

                  │

                  ▼

              INTERVENE

                  │

                  ▼

              EXPERIENCE

                  │

                  ▼

               OBSERVE

                  │

                  ▼

               REMEMBER

                  │

                  ▼

                LEARN

                  │

                  ▼

               ADAPT

                  │

                  └──────────→ INTERVENE

The specialized agents operate around that loop.

Their boundaries prevent the system from collapsing into a single opaque agent.

The fundamental architecture becomes:

Human defines direction.  
Orchestrator navigates.  
Specialized agents establish relationships.  
Action changes the world.  
Experience generates evidence.  
Ledger preserves context.  
Learning changes the model.  
Adaptation changes the path.

That is the architecture I would use as the foundation for the next layer: defining the exact handoff protocol between agents—what one agent must give the next, what state is shared, and what constitutes a valid transition.