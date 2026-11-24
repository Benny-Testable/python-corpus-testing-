"""Test Maintenance Reduction fixture: this file and its twin
(test_duplicate_order_flows_a.py / _b.py) repeat the same setup and assertions
on purpose, so jscpd measures duplication inside the test suite."""


def _expected_rates(rules):
    rows = []
    for tier in ("standard", "silver", "gold"):
        for units in (0, 25, 100, 500):
            for promo in (None, "SPRING10", "VOLUME5", "LOYAL15"):
                rate = rules.combined(tier, units, promo)
                assert 0.0 <= rate <= 0.20
                rows.append((tier, units, promo, rate))
    return rows


def test_rate_grid_is_bounded_and_complete(rules):
    rows = _expected_rates(rules)
    assert len(rows) == 48
    assert max(r[3] for r in rows) == 0.20
    assert min(r[3] for r in rows) == 0.0
    gold_rows = [r for r in rows if r[0] == "gold"]
    assert len(gold_rows) == 16
    assert all(r[3] >= 0.10 for r in gold_rows)
    standard_plain = [r for r in rows if r[0] == "standard" and r[2] is None]
    assert [r[3] for r in standard_plain] == [0.0, 0.02, 0.05, 0.08]
