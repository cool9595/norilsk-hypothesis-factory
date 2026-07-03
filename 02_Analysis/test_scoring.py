import unittest

from hypothesis_factory.models import UncertaintyZone
from hypothesis_factory.scoring.scorer import calculate_uncertainty_importance, final_score


class ScoringTest(unittest.TestCase):
    def test_uncertainty_importance_formula(self):
        zone = UncertaintyZone(
            id="Z",
            type="coverage_gap",
            description="",
            target_kpi="kpi",
            kpi_relevance=1.0,
            gap_severity=0.8,
            contradiction_strength=0.5,
            indirect_mechanism_strength=0.25,
        )
        self.assertEqual(calculate_uncertainty_importance(zone), 0.7)

    def test_final_score_penalizes_risk_and_cost(self):
        score = final_score(
            {
                "value": 1,
                "novelty": 1,
                "feasibility": 1,
                "evidence": 1,
                "uncertainty_importance": 1,
                "risk": 1,
                "cost": 1,
            },
            {"value": 1, "novelty": 1, "feasibility": 1, "evidence": 1, "uncertainty": 1, "risk": 1, "cost": 1},
        )
        self.assertEqual(score, 3.0)


if __name__ == "__main__":
    unittest.main()

