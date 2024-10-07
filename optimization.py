import numpy as np
import logging

def optimize_workload_knapsack(assignments, engineers):
    num_tasks = len(assignments)
    num_engineers = len(engineers)
    engineer_workloads = {eng['name']: 0 for eng in engineers}

    skill_match_scores = np.zeros((num_tasks, num_engineers))
    for task_idx, (story, _) in enumerate(assignments):
        for eng_idx, engineer in enumerate(engineers):
            skill_match_scores[task_idx, eng_idx] = engineer_workloads[engineer['name']] + 1

    dp = np.zeros((num_tasks + 1, num_engineers + 1))
    keep = np.zeros((num_tasks, num_engineers))

    for task_idx in range(1, num_tasks + 1):
        for eng_idx in range(num_engineers):
            task_score = skill_match_scores[task_idx - 1, eng_idx]
            if dp[task_idx - 1, eng_idx] + task_score > dp[task_idx, eng_idx]:
                dp[task_idx, eng_idx] = dp[task_idx - 1, eng_idx] + task_score
                keep[task_idx - 1, eng_idx] = 1

    best_assignment = []
    task_idx = num_tasks - 1
    eng_idx = num_engineers - 1
    while task_idx >= 0 and eng_idx >= 0:
        if keep[task_idx, eng_idx] == 1:
            story, _ = assignments[task_idx]
            best_engineer = engineers[eng_idx]['name']
            best_assignment.append((story, best_engineer))
            engineer_workloads[best_engineer] += 1
            task_idx -= 1
            eng_idx -= 1
        else:
            task_idx -= 1

    logging.info(f"Optimized Assignments (Knapsack DP): {best_assignment}")
    return best_assignment

# [2023-01-03] (Extraction) schedule note: Document PRD automation results for Extraction

# [2023-01-27] (PRD) schedule note: Improve document extraction for PRD

# [2023-02-13] (Embeddings) schedule note: Improve document extraction for Embeddings

# [2023-03-02] (Extraction) schedule note: Add diagnostics for Extraction

# [2023-03-14] (Assignments) schedule note: Document PRD automation results for Assignments

# [2023-03-28] (Embeddings) schedule note: Document PRD automation results for Embeddings

# [2023-04-11] (Assignments) schedule note: Improve document extraction for Assignments

# [2023-04-28] (Extraction) schedule note: Document PRD automation results for Extraction

# [2023-11-15] (Assignments) schedule note: Improve document extraction for Assignments

# [2023-12-01] (PRD) schedule note: Improve document extraction for PRD

# [2023-12-18] (PRD) schedule note: Add diagnostics for PRD

# [2024-01-09] (Extraction) schedule note: Tune embedding scoring for Extraction

# [2024-09-13] (Assignments) schedule note: Improve document extraction for Assignments

# [2024-10-07] (PRD) schedule note: Improve document extraction for PRD
