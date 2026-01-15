import numpy as np
def analyze_scores(scores):
    total_students = scores.size

    mean_score = np.round(np.mean(scores), 2)
    median_score = np.round(np.median(scores), 2)
    std_deviation = np.round(np.std(scores), 2)

    passed = np.sum(scores >= 50)
    failed = np.sum(scores < 50)
    failed_percentage = np.round((failed / total_students)*100, 2)

    return {
        "total_students": total_students,
        "mean_score":mean_score,
        "median_score": median_score,
        "std_deviation": std_deviation,
        "Passed students": passed,
        "Failed students": failed_percentage
    }
scores = np.array([45, 78, 62, 49, 90, 55, 30])
result = analyze_scores(scores)
print(result)
