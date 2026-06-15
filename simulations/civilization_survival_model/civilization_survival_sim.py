"""Conceptual civilization survival simulation.

This script is a transparent toy model for comparing long-term civilizational
survival under different philosophical assumptions. It is not a validated
forecast, scientific prediction, or policy model. The numerical parameters are
illustrative and should be read as assumptions for discussion.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


YEARS = 300
START_YEAR = 0
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"

TRACKED_COLUMNS = [
    "ecosystem_integrity",
    "circulation_health",
    "resource_base",
    "social_order",
    "technological_capacity",
    "civilizational_survival_index",
]


SCENARIOS = {
    "Dualism / Human Supremacy": {
        "extraction_base": 0.030,
        "tech_extraction_bias": 0.030,
        "restoration_base": 0.004,
        "tech_restoration_bias": 0.004,
        "tech_growth": 0.010,
        "tech_decay": 0.001,
        "social_stress_sensitivity": 0.028,
        "social_repair": 0.004,
    },
    "Conventional Environmentalism": {
        "extraction_base": 0.021,
        "tech_extraction_bias": 0.016,
        "restoration_base": 0.009,
        "tech_restoration_bias": 0.011,
        "tech_growth": 0.008,
        "tech_decay": 0.001,
        "social_stress_sensitivity": 0.020,
        "social_repair": 0.007,
    },
    "Natural Complementary Science": {
        "extraction_base": 0.014,
        "tech_extraction_bias": 0.004,
        "restoration_base": 0.014,
        "tech_restoration_bias": 0.028,
        "tech_growth": 0.007,
        "tech_decay": 0.001,
        "social_stress_sensitivity": 0.013,
        "social_repair": 0.012,
    },
    "Accelerated Extraction Collapse": {
        "extraction_base": 0.044,
        "tech_extraction_bias": 0.045,
        "restoration_base": 0.002,
        "tech_restoration_bias": 0.001,
        "tech_growth": 0.013,
        "tech_decay": 0.002,
        "social_stress_sensitivity": 0.040,
        "social_repair": 0.002,
    },
}


def clamp(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    """Keep model state variables in the conceptual 0-1 range."""
    return float(np.clip(value, lower, upper))


def collapse_risk(state: dict[str, float]) -> float:
    """Estimate risk from critical weaknesses in ecological and social bases."""
    critical_threshold = 0.35
    vulnerable_dimensions = [
        "ecosystem_integrity",
        "circulation_health",
        "resource_base",
        "social_order",
    ]
    deficits = [
        max(0.0, critical_threshold - state[column]) / critical_threshold
        for column in vulnerable_dimensions
    ]
    return clamp(np.mean(deficits), 0.0, 1.0)


def survival_index(state: dict[str, float]) -> float:
    """Combine core continuity conditions into a single conceptual index."""
    ecological_base = (
        0.30 * state["ecosystem_integrity"]
        + 0.25 * state["circulation_health"]
        + 0.20 * state["resource_base"]
        + 0.15 * state["social_order"]
        + 0.10 * state["technological_capacity"]
    )
    risk_penalty = 0.45 * collapse_risk(state)
    return clamp(ecological_base - risk_penalty)


def step_state(state: dict[str, float], params: dict[str, float]) -> dict[str, float]:
    """Advance one year according to transparent conceptual feedback rules."""
    tech = state["technological_capacity"]

    # In dualistic or extraction-centered systems, technology magnifies pressure.
    # In natural-complementary systems, technology is assumed to be governed by
    # natural law, harmony, circulation, structure, order, and Wa, so it can
    # increase restoration capacity instead.
    extraction_pressure = params["extraction_base"] + params["tech_extraction_bias"] * tech
    restoration_capacity = params["restoration_base"] + params["tech_restoration_bias"] * tech

    ecosystem_integrity = clamp(
        state["ecosystem_integrity"]
        + restoration_capacity * (1.0 - state["ecosystem_integrity"])
        - extraction_pressure * (0.65 + 0.35 * tech)
    )

    circulation_health = clamp(
        state["circulation_health"]
        + 0.65 * restoration_capacity * (1.0 - state["circulation_health"])
        + 0.015 * (ecosystem_integrity - state["circulation_health"])
        - 0.70 * extraction_pressure
    )

    resource_base = clamp(
        state["resource_base"]
        + 0.040 * ecosystem_integrity
        + 0.030 * circulation_health
        - 0.080 * extraction_pressure
        - 0.018 * (1.0 - circulation_health)
    )

    scarcity = 1.0 - resource_base
    ecological_disruption = 1.0 - min(ecosystem_integrity, circulation_health)
    social_order = clamp(
        state["social_order"]
        + params["social_repair"] * (1.0 - state["social_order"])
        - params["social_stress_sensitivity"] * (0.55 * scarcity + 0.45 * ecological_disruption)
        - 0.030 * collapse_risk(state)
    )

    technological_capacity = clamp(
        tech
        + params["tech_growth"] * social_order * resource_base
        - params["tech_decay"] * (1.0 - social_order)
        - 0.010 * collapse_risk(state)
    )

    new_state = {
        "ecosystem_integrity": ecosystem_integrity,
        "circulation_health": circulation_health,
        "resource_base": resource_base,
        "social_order": social_order,
        "technological_capacity": technological_capacity,
    }
    new_state["civilizational_survival_index"] = survival_index(new_state)
    return new_state


def run_scenario(name: str, params: dict[str, float]) -> pd.DataFrame:
    """Run one scenario for the full simulation horizon."""
    state = {
        "ecosystem_integrity": 0.82,
        "circulation_health": 0.78,
        "resource_base": 0.86,
        "social_order": 0.80,
        "technological_capacity": 0.55,
    }
    state["civilizational_survival_index"] = survival_index(state)

    rows = []
    for year in range(START_YEAR, YEARS + 1):
        rows.append({"year": year, "scenario": name, **state})
        if year < YEARS:
            state = step_state(state, params)

    return pd.DataFrame(rows)


def run_simulation() -> pd.DataFrame:
    """Run every scenario and return one combined table."""
    frames = [run_scenario(name, params) for name, params in SCENARIOS.items()]
    return pd.concat(frames, ignore_index=True)


def save_outputs(results: pd.DataFrame) -> None:
    """Save the CSV table and a comparison graph."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    csv_path = OUTPUT_DIR / "civilization_survival_results.csv"
    png_path = OUTPUT_DIR / "civilization_survival_index.png"

    results.to_csv(csv_path, index=False)

    plt.figure(figsize=(11, 6.5))
    for scenario, scenario_df in results.groupby("scenario"):
        plt.plot(
            scenario_df["year"],
            scenario_df["civilizational_survival_index"],
            linewidth=2.2,
            label=scenario,
        )

    plt.title("Conceptual Civilizational Survival Index by Scenario")
    plt.xlabel("Year")
    plt.ylabel("Civilizational Survival Index (0-1)")
    plt.ylim(0, 1.02)
    plt.grid(True, alpha=0.28)
    plt.legend()
    plt.tight_layout()
    plt.savefig(png_path, dpi=160)
    plt.close()


def main() -> None:
    results = run_simulation()
    save_outputs(results)
    print(f"Saved CSV and PNG outputs to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
