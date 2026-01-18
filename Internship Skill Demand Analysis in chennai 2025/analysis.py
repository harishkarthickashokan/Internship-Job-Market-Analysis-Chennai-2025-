import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

def clean_skill(text):
    if pd.isna(text):
        return []
    text = text.lower()
    text = re.sub(r'[^a-z,\+\s]', '', text)
    skills = [s.strip() for s in text.split(',') if s.strip()]
    return skills

def map_posting_range(val):
    if val <= 0:
        return "Low"
    elif val <= 2.5:
        return "Medium"
    else:
        return "High"

def main():
    
    df = pd.read_csv("internship-in-chennai.csv")

    if 'posting_count' in df.columns:
        df['posting_count'] = df['posting_count'].astype(float)
        df['posting_level'] = df['posting_count'].apply(map_posting_range)
        print("\nConverted posting_count to posting_level:")
        print(df[['posting_count','posting_level']].head(), "\n")
    else:
        print("\n Column 'posting_count' not found! Tell me the correct column name.\n")

    role_counts = df['profile'].value_counts().reset_index()
    role_counts.columns = ['profile', 'count']

    print("\nTop 15 Most Preferred Internship Roles:\n")
    print(role_counts.head(15))
    df['Skills_clean'] = df['Skills'].apply(clean_skill)

    all_skills = []
    for row in df['Skills_clean']:
        all_skills.extend(row)

    skill_freq = Counter(all_skills).most_common(20)

    print("\nTop 20 Skills Freshers Need to Learn:\n")
    for skill, count in skill_freq:
        print(f"{skill} : {count}")

   
  plt.figure(figsize=(10,5))
    plt.bar(role_counts['profile'][:10], role_counts['count'][:10])
    plt.title("Top Internship Roles (Demand)")
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Roles")
    plt.ylabel("Posting Count")
    plt.tight_layout()
    plt.show()


    skills, counts = zip(*skill_freq)
    plt.figure(figsize=(10,5))
    plt.bar(skills, counts)
    plt.title("Top Required Skills for Freshers")
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Skills")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

