def skill_similarity(candidate_skills, job_skills):

    if not job_skills:
        return 0.0

    candidate_set = {s.strip().lower() for s in candidate_skills}
    job_set = {s.strip().lower() for s in job_skills}

    overlap = candidate_set.intersection(job_set)

    return len(overlap) / len(job_set)
