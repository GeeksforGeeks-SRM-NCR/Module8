# Recruitment Counterfactual Fairness Challenge (Level 100)

## Overview

This project implements an advanced recruitment matching system.

The system ranks candidates using a multi-stage scoring pipeline:

1. Skill similarity scoring
2. Counterfactual fairness adjustment
3. Score normalization
4. Diversity reweighting
5. Final ranking

The algorithm executes successfully but contains subtle logical flaws.

Participants must analyse and fix the algorithm.


--------------------------------------------------

## Your Task

You must:

- Run the system.
- Observe the generated ranking.
- Analyse the full scoring pipeline.
- Identify fairness or ranking issues.
- Improve or redesign the algorithm.

Important:

The bug is NOT a syntax error.
The program runs normally.

The issue lies in algorithm design.


--------------------------------------------------

## Setup

Install dependencies:

pip install -r requirements.txt


--------------------------------------------------

## How to Run

Run the main program:

python src/main.py


--------------------------------------------------

## Expected Behaviour

The program will:

- Load candidate and job data.
- Compute multiple scoring stages.
- Output a ranked list of candidates.

Note:

The ranking may look reasonable but contains hidden fairness issues.


--------------------------------------------------

## Challenge Goals

- Understand counterfactual fairness.
- Analyse multi-stage scoring pipelines.
- Identify interaction bugs between algorithm components.
- Ensure fairness adjustments actually influence ranking.


--------------------------------------------------

## Tips

- Review scoring order carefully.
- Compare intermediate scores.
- Think about how normalization affects fairness signals.
