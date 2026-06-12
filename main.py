import pandas as pd
import json

candidates = []

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidates.append(json.loads(line))

df = pd.DataFrame(candidates)

candidate = df.iloc[0]

# Experience Score
years = candidate["profile"]["years_of_experience"]

if 5 <= years <= 9:
    experience_score = 1
else:
    experience_score = 0

# AI Skills
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

candidate_skills = [
    skill["name"]
    for skill in candidate["skills"]
]

skill_matches = 0

for skill in ai_skills:
    if skill in candidate_skills:
        skill_matches += 1

skill_score = skill_matches / len(ai_skills)

print("Experience Score:", experience_score)
print("Skill Score:", round(skill_score, 2))

final_score = (
    experience_score * 0.4 +
    skill_score * 0.6
)

print("Final Score:", round(final_score, 2))