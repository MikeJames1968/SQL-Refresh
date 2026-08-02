import numpy as np

# Rows are students, columns are exam scores

scores = np.array([
    [78, 85, 92, 88],
    [65, 70, 72, 68],
    [90, 95, 94, 99],
    [55, 60, 58, 62],
    [81, 79, 85, 87]
])

# Test 1 - explore the data

print("scores numpy array - basics")
print("=" * 26)
print("shape:", scores.shape)
print("dimensions:", scores.ndim)
print("type:", scores.dtype)
print("size: (bytes)", scores.nbytes, "\n")

# Test 2 - overall stats

print("scores numpy array - statistics")
print("=" * 31)
print("average score:", scores.mean())
print("highest score:", scores.max())
print("lowest score:", scores.min())
print("std deviation:", scores.std(), "\n")

# Test 3 - per student stats

print("scores numpy array - per student statistics")
print("=" * 43)

print("student average max min")
for student, results in enumerate(scores):
    print(f"{student+1:<8}{results.mean():<8}{results.max():<4}{results.min():<4}")

# Test 4 - per subject stats

print("\nscores numpy array - per subject statistics")
print("=" * 43)

print("subject average max min")
for subject, results in enumerate(scores.T):
    print(f"{subject+1:<8}{results.mean():<8}{results.max():<4}{results.min():<4}")

# Note - solutions for tests 1-4 were too "pythonic" - tests 5-8 I attempt to use numpy solutions whereever possible

# Test 5 - boolean indexing. Need to be more numpy, less pythonic

print("\nboolean indexing")
print("=" * 16)

over_89 = scores > 90
print("scores 90 or over: ", scores[over_89])
print("total: ", np.sum(over_89))

# Test 6 - array arithmetic

print("\narray arithmetic")
print("=" * 16)

bonus_scores = scores + 5
print("original scores:")
print(scores)
print("scores+5:")
print(bonus_scores)

# Test 7 - boolean mask

print("\npasses:")
passes = scores >= 70
print(passes)

# Test 8 - ranking with argsort

averages = np.mean(scores,axis=1)
rank = np.argsort(-averages)
ranked_averages = np.char.mod('%.2f',averages[rank])
results_table = np.column_stack((np.arange(1, len(rank)+1), rank+1, ranked_averages))

print("\nrank student average")
print(results_table)
