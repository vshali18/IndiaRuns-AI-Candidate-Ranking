import pandas as pd
import json

# Load dataset
candidates = []

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidates.append(json.loads(line))

df = pd.DataFrame(candidates)

# AI skills from JD
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

results = []

for _, candidate in df.iterrows():

    profile = candidate["profile"]

    years = profile.get(
        "years_of_experience",
        0
    )

    # Experience score
    if 5 <= years <= 9:
        experience_score = 1
    else:
        experience_score = 0

    # Skills score
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
        0.4 * experience_score +
        0.6 * skill_score
    )

    results.append({
        "candidate_id":
            candidate["candidate_id"],
        "score":
            final_score
    })

result_df = pd.DataFrame(results)

result_df = result_df.sort_values(
    by="score",
    ascending=False
)

print(result_df.head(10))
top_candidate_id = result_df.iloc[0]["candidate_id"]

candidate = df[df["candidate_id"] == top_candidate_id].iloc[0]

print("\nTOP CANDIDATE:")
print(candidate["profile"])