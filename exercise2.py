import pandas as pd
def top_students(df):
    dept_avg = df.groupby("department")["score"].transform("mean")
    result = df[df["score"]> dept_avg]
    return result.sort_values(by="score", ascending=False)
data={
    "name": ["Alice", "Bob", "Charlie", "David", "Eva",],
    "department": ["Math", "Math", "Physics", "Physics", "Math"],
    "score": [85, 78, 92, 88, 76]}
df = pd.DataFrame(data)
print(top_students(df))