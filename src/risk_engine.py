class RiskEngine:
    """
    Computes academic risk based on behavioral learning signals.
    """

    def __init__(self, study_hours, revision_gap_days, missed_tasks):
        self.study_hours = study_hours
        self.revision_gap_days = revision_gap_days
        self.missed_tasks = missed_tasks

    def compute_risk(self):
        score = 0

        if self.study_hours < 5:
            score += 30
        if self.revision_gap_days > 10:
            score += 40
        if self.missed_tasks > 2:
            score += 30

        return self.classify(score)

    def classify(self, score):
        if score >= 70:
            return "Critical"
        elif score >= 40:
            return "Warning"
        return "Safe"


if __name__ == "__main__":
    engine = RiskEngine(
        study_hours=3,
        revision_gap_days=12,
        missed_tasks=3
    )
    print(engine.compute_risk())
