import pandas as pd
import json

# Load dataset
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
    "Embeddings",
    "Machine Learning",
    "LLM",
    "Retrieval"
]

good_titles = [
    "machine learning engineer",
    "ml engineer",
    "ai engineer",
    "data scientist",
    "applied scientist",
    "research engineer"
]

results = []

for _, candidate in df.iterrows():

    profile = candidate["profile"]

    years = profile.get("years_of_experience", 0)

    title = profile.get("current_title", "").lower()

    # Experience Score
    if 5 <= years <= 9:
        experience_score = 1
    else:
        experience_score = 0

    # Title Score
    title_score = 0

    for t in good_titles:
        if t in title:
            title_score = 1
            break

    # Skill Score
    candidate_skills = [
        skill["name"]
        for skill in candidate["skills"]
    ]

    matches = 0

    for skill in ai_skills:
        if skill in candidate_skills:
            matches += 1

    skill_score = matches / len(ai_skills)

    # Final Score
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
    by=["score", "candidate_id"],
    ascending=[False, True]
)

print(result_df.head(10))

result_df = result_df.head(100)
result_df = result_df.reset_index(drop=True)

result_df["rank"] = result_df.index + 1

result_df["reasoning"] = (
    "Relevant AI title and skills match"
)

submission = result_df[
    ["candidate_id", "rank", "score", "reasoning"]
]

submission.to_csv(
    "submission.csv",
    index=False
)

print("submission.csv created successfully!")