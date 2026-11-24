# Taxonomy coverage data (130 metrics)

Baseline run 4712c903 on this branch reported 130 metrics: 96 scored, 34 N/A.
This file records which N/A rows the repository can fix with data and which it cannot.

## Fixed by data in this branch
| Metric(s) | Data |
|---|---|
| IaC Security (4) + Static Code Analysis / IaC Security Scanning (4) | `infra/` Terraform, CloudFormation and Kubernetes fixtures |
| Code Duplication / Test Maintenance Reduction | `tests/test_duplicate_order_flows_a.py` / `_b.py` (deliberate test-suite clones) |
| Mutation Score / Regression Testing Validation | `PricingRules.loyalty_points` constants pinned by `tests/test_loyalty_points.py` |
| Code Churn / Change Impact Analysis, Regression Testing Focus, Risk-Based Testing Prioritization | the tip commit now changes `services/pricing_rules.py`, which `order_service` imports (the previous tip only touched README.md) |
| Coverage Delta (5) | needs a second run on a newer commit, so a baseline run exists |

## Not fixable by repository data (platform side)
| Metric | Reason reported |
|---|---|
| Secrets in Git History, Secrets in Repo History | trufflehog runs weekly only, not on manual runs |
| Static Code Analysis / Pre-Commit Secret Prevention | detect-secrets has no commit telemetry |
| Reporting Validation, Coverage Reporting Validation, Custom Rule Validation, Configuration File Handling, Violation Reporting Validation | "Not measured / not supported" by the platform |
| Logic Coverage Metric | planned task did not start |
| Dependency Health Monitoring, Outdated Dependency Detection | need deps.dev / pip-outdated on the platform |
| Privileged Access Audit | needs the GitHub access-control API for the connected repo |
| Code Review Support, CI/CD Integration Validation, Input Validation Testing, Data Flow Security Analysis | Python evidence exists (pylint, bandit, semgrep) but the platform does not map it to these leaves |
