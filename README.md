# AI-Powered Candidate Ranking System

## Problem Statement
Traditional recruitment systems rely heavily on keyword matching, often missing highly relevant candidates.

## Solution
This project ranks candidates using:
- Experience Score
- AI Skills Score
- Job Title Relevance
- Candidate Ranking Logic

## Dataset
100,000 candidate profiles provided by the Redrob AI Challenge.

## Output
Top 100 ranked candidates in CSV format.

## Technologies
- Python
- Pandas
- JSON

## Results
Submission successfully validated using the official validator.

## Web Application

This project includes a Streamlit-based web application for candidate ranking.

Features:
- Paste Job Description
- Rank Candidates
- Display Top 10 Candidates
- Score candidates based on skills, experience, and title relevance

Run locally:

pip install -r requirements.txt

streamlit run app.py
