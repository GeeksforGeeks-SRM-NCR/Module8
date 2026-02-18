def rank_candidates():

    candidates = load_json("data/candidates.json")
    job = load_json("data/job_description.json")
    protected = load_json("data/protected_groups.json")["protected"]

    names = []
    raw_scores = []

    for c in candidates:

        base = skill_similarity(c["skills"], job["skills"])

        counter = counterfactual_score(base, c["group"], protected)

        # ✔ Use counterfactual score directly
        final = counter

        names.append((c["name"], c["group"]))
        raw_scores.append(final)

    norm_scores = normalize(raw_scores)

    final_scores = []

    for i, (name, group) in enumerate(names):

        diversity = diversity_adjustment(name, group)

        final_scores.append((name, norm_scores[i] + diversity))

    final_scores.sort(key=lambda x: x[1], reverse=True)

    return final_scores
