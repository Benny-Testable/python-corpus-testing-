"""Exact-value tests for PricingRules.loyalty_points (mutation constant pins)."""
import pytest


@pytest.mark.parametrize("amount,member,expected", [
    (0, False, 0), (9, False, 0), (10, False, 1), (100, False, 10),
    (100, True, 20), (4999, False, 499), (4999, True, 998),
    (5000, False, 600), (5000, True, 1100),
])
def test_loyalty_points(rules, amount, member, expected):
    assert rules.loyalty_points(amount, member) == expected


def test_loyalty_points_rejects_negative(rules):
    with pytest.raises(ValueError):
        rules.loyalty_points(-1)


@pytest.mark.parametrize("points,expected", [
    (0, "member"), (99, "member"), (100, "silver"), (499, "silver"),
    (500, "gold"), (999, "gold"), (1000, "platinum"),
])
def test_loyalty_tier(rules, points, expected):
    assert rules.loyalty_tier(points) == expected
