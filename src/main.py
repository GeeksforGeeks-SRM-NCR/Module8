from matching_engine.matcher import rank_candidates

print("Final Ranking:")

try:
    results = rank_candidates()
    for name, score in results:
        print(f"{name}: {score:.3f}")
except Exception as e:
    print("Error while ranking candidates:")
    print(e)
