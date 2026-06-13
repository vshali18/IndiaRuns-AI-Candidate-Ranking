import streamlit as st
import pandas as pd
import json

st.title("🤖 AI Candidate Ranking System")

st.write("Paste Job Description and Rank Candidates")

jd = st.text_area("Job Description")

if st.button("Rank Candidates"):

    candidates = []

    with open("candidates.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            candidates.append(json.loads(line))

    df = pd.DataFrame(candidates)

    ai_skills = [
        "NLP",
        "Fine-tuning LLMs",
        "LoRA",
        "Milvus",
        "Python",
        "Machine Learning",
        "Embeddings",
        "Retrieval"
    ]

    results = []

    for _, candidate in df.iterrows():

        profile = candidate["profile"]

        years = profile.get("years_of_experience", 0)

        title = profile.get(
            "current_title", ""
        ).lower()

        good_titles = [
            "machine learning engineer",
            "ml engineer",
            "ai engineer",
            "applied scientist",
            "research engineer"
        ]

        title_score = 0

        for t in good_titles:
            if t in title:
                title_score = 1
                break

        experience_score = 1 if 5 <= years <= 9 else 0

        candidate_skills = [
            skill["name"]
            for skill in candidate["skills"]
        ]

        matches = 0

        for skill in ai_skills:
            if skill in candidate_skills:
                matches += 1

        skill_score = matches / len(ai_skills)

        final_score = (
            0.3 * experience_score +
            0.4 * skill_score +
            0.3 * title_score
        )

        results.append({
            "candidate_id": candidate["candidate_id"],
            "score": final_score,
            "title": profile.get("current_title", "")
        })

    result_df = pd.DataFrame(results)

    result_df = result_df.sort_values(
        by="score",
        ascending=False
    )

    st.subheader("Top Candidates")

    st.dataframe(result_df.head(10))