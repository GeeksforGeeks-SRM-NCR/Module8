def skill_similarity(candidate_skills, job_skills):

    overlap = set(candidate_skills).intersection(set(job_skills))

    return len(overlap) / len(job_skills)
