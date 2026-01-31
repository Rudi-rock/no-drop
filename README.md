# No-Drop 🎓
### Academic Early-Warning System to Prevent Student Failure

## Overview
No-Drop is an early-warning system designed to identify students at risk of academic failure **before** they fail examinations.

Unlike traditional systems that rely on marks, No-Drop focuses on **behavioral learning signals** such as:
- Study inactivity
- Revision gaps
- Missed academic tasks
- Sudden drops in engagement

The system generates a **risk classification** and enables early, targeted interventions.

---

## Problem Statement
Academic failure is rarely sudden.  
Students typically experience a gradual decline in engagement, consistency, and confidence — which current academic systems fail to detect in time.

Most institutions act **after exam results**, when recovery is no longer possible.

---

## Solution
No-Drop continuously monitors student activity patterns and assigns a dynamic risk score.

Based on this score, students are classified into:
- Safe
- Warning
- Critical

This allows educators to intervene early through academic counseling, workload adjustment, or personalized support.

---

## System Design
**Input**
- Study time logs
- Revision intervals
- Assignment submission data

**Processing**
- Rule-based risk scoring (AI-ready architecture)

**Output**
- Risk category per student
- Actionable intervention triggers

---

## Current Implementation (v1)
- Rule-based risk scoring engine
- CSV-based input simulation
- Python-based logic layer

---

## Tech Stack
- Python
- Pandas
- Modular rule engine

---

## Future Enhancements
- Machine learning–based risk prediction
- LMS integration (Moodle, Google Classroom)
- Real-time dashboards for faculty
- Automated student nudges

---

## Author
Rudra Pratap Singh  
B.Tech CSE — SRM Kattankulathur

## Running the Project
pip install -r requirements.txt
python src/risk_engine.py


