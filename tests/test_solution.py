"""Regression tests for the Codeforces 580D solution."""

from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SOLUTION = ROOT / "kefa_and_dishes.py"


def run_solution(test_input: str) -> str:
    """Run the solution and return its standard output."""
    result = subprocess.run(
        [sys.executable, str(SOLUTION)],
        input=test_input,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class KefaAndDishesTests(unittest.TestCase):
    def test_official_sample(self) -> None:
        test_input = """\
4 3 2
1 2 3 4
2 1 5
3 4 2
"""
        self.assertEqual(run_solution(test_input), "12")

    def test_single_dish(self) -> None:
        test_input = """\
3 1 1
5 2 4
1 2 10
"""
        self.assertEqual(run_solution(test_input), "5")

    def test_order_dependent_bonuses(self) -> None:
        test_input = """\
3 3 3
1 2 3
1 2 10
2 3 20
1 3 1
"""
        self.assertEqual(run_solution(test_input), "36")


if __name__ == "__main__":
    unittest.main()
