def counterfactual_score(base_score, group, protected):

    if isinstance(protected, (list, set, tuple)) and group in protected:
        return base_score + 0.25

    return base_score
