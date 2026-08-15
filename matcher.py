def rank_candidates(candidates, jd):
    results = []
    for c in candidates:
        # Transparent weighted score:
        # 55% required-skill coverage + 30% overall textual relevance + 15% project/experience signals.
        project_terms = ["project", "internship", "experience", "developed", "built", "worked"]
        lower = c["text"].lower()
        project_signal = min(100, sum(1 for x in project_terms if x in lower) * 16.7)
        score = round(
            c["skill_score"] * 0.55 +
            c["relevance_score"] * 0.30 +
            project_signal * 0.15
        )
        score = max(0, min(100, score))

        if score >= 75:
            recommendation = "🟢 Highly Recommended"
        elif score >= 60:
            recommendation = "🟡 Consider"
        else:
            recommendation = "🔴 Low Match"

        if c["matched_skills"]:
            explanation = (
                f"Strong alignment with {len(c['matched_skills'])} required skill(s): "
                + ", ".join(c["matched_skills"][:6]) + ". "
            )
        else:
            explanation = "Few required technical skills were detected. "

        if c["missing_skills"]:
            explanation += "Primary skill gaps: " + ", ".join(c["missing_skills"][:5]) + "."
        else:
            explanation += "No major required-skill gaps were detected."

        c.update({
            "score": score,
            "project_signal": round(project_signal),
            "recommendation": recommendation,
            "explanation": explanation
        })
        results.append(c)

    return sorted(results, key=lambda x: x["score"], reverse=True)
