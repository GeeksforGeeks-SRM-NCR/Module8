def normalize(scores):
    if not scores:
        return []

    max_val = max(scores)
    min_val = min(scores)

    if max_val == min_val:
        return [0.5] * len(scores)

    return [(s - min_val) / (max_val - min_val) for s in scores]
