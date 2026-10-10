# Exploratory Testing Reference

Load this only for planning or running a full exploratory session.

## Inputs

Mission, time box, product area, change set, personas, environment, data constraints, known risks, and previous defects.

## Session Design

1. Write a one-sentence charter naming feature, persona, and target risk.
2. Establish a clean state and record build/environment identifiers.
3. Tour the happy path once, then vary state, sequence, data, permissions, timing, and interruption.
4. Select useful heuristics: boundaries, CRUD, state transitions, recovery, concurrency, accessibility, compatibility, and observability.
5. Keep timestamped notes linking action, observation, and evidence.
6. Convert stable discoveries into regression candidates and suspected failures into defect-analysis inputs.

## Output and Exit

Report charter, duration, coverage, variations, observations, defects, questions, and residual risk. Stop at the time box, safety boundary, unreliable environment, or blocking condition.
