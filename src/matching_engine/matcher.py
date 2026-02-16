from matching_engine.scoring import skill_similarity
from matching_engine.fairness import counterfactual_score
from matching_engine.normalization import normalize
from matching_engine.diversity import diversity_adjustment
from utils.data_loader import load_json

def rank_candidates():

    candidates = load_json("data/candidates.json")
    job = load_json("data/job_description.json")
    protected = load_json("data/protected_groups.json")["protected"]

    names = []
    raw_scores = []

    for c in candidates:

        base = skill_similarity(c["skills"], job["skills"])

        counter = counterfactual_score(base, c["group"], protected)

        fairness_gap = abs(base - counter)

        final = base - fairness_gap

        names.append((c["name"], c["group"]))
        raw_scores.append(final)

    norm_scores = normalize(raw_scores)

    final_scores = []

    for i, (name, group) in enumerate(names):

        diversity = diversity_adjustment(name, group)

        final_scores.append((name, norm_scores[i] + diversity))

    final_scores.sort(key=lambda x: x[1], reverse=True)

    return final_scores
