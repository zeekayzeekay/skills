from copy import deepcopy
from decimal import Decimal
import unittest

from csv_summary import summarize
from matching import cost_receipt, select_passage


class SummaryEvidence(unittest.TestCase):
    def test_signed_net(self):
        self.assertEqual(summarize([{"amount": "10.50"}, {"amount": "-3.00"}])["net"], Decimal("7.50"))

    def test_input_unchanged(self):
        rows = [{"amount": "10.50"}, {"amount": "-3.00"}]
        original = deepcopy(rows)
        summarize(rows)
        self.assertEqual(rows, original)


class MatchingEvidence(unittest.TestCase):
    def test_single_passage(self):
        self.assertEqual(select_passage([{"text": "A", "score": 0.9}]), "A")

    def test_one_priced_attempt(self):
        self.assertEqual(cost_receipt([{"cost": 0.25}]), {"known": True, "amount": 0.25})


if __name__ == "__main__":
    unittest.main()
