def normalize(scores):

    max_val = max(scores)
    min_val = min(scores)

    return [(s - min_val)/(max_val - min_val + 0.5) for s in scores]
