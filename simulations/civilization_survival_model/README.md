# Civilization Survival Model

This directory contains a simple conceptual simulation comparing long-term civilizational survival under different philosophical assumptions.

The model is **not a predictive scientific model**. It is a transparent toy model for discussion inside the Natural Complementary Science framework. The equations and parameters are illustrative assumptions, not validated forecasts.

## Scenarios

- **Dualism / Human Supremacy**: technological capacity tends to amplify extraction pressure because nature is treated as external or subordinate.
- **Conventional Environmentalism**: extraction is moderated and restoration is present, but the system remains partly centered on human management and resource utility.
- **Natural Complementary Science**: technological capacity is guided by natural law, harmony, circulation, structure, order, and Wa, so it tends to strengthen restoration and systemic continuity.
- **Accelerated Extraction Collapse**: short-term extraction is intensified, causing rapid deterioration of ecological and social foundations.

## Tracked Variables

- `ecosystem_integrity`
- `circulation_health`
- `resource_base`
- `social_order`
- `technological_capacity`
- `civilizational_survival_index`

All values are normalized between 0 and 1.

## Core Concept

The model expresses a philosophical difference in how technology is directed:

- When technology is guided by dualism and human supremacy, it tends to increase extraction pressure.
- When technology is guided by natural complementarity, it tends to increase restoration capacity.
- Collapse risk rises when ecosystem integrity, circulation health, resource stability, or social order fall below critical thresholds.
- Civilization survives longer when natural law, harmony, circulation, structure, order, and Wa are treated as governing design principles.

## Interpretation of Results

In this conceptual model, only the Natural Complementary Science scenario maintained long-term civilizational survivability.

By contrast, the Dualism / Human Supremacy scenario, the Conventional Environmental Management scenario, and the Accelerated Extraction Collapse scenario all showed progressive decline in ecosystem integrity, circulation health, resource stability, social order, and overall civilizational survival.

In particular, scenarios that did not incorporate the restoration of natural circulation into civilizational design showed a rapid decline in survivability around the 50-year mark.

This is not a prediction.
However, in an era of compound risks such as climate change, El Niño, ocean circulation instability, wildfires, droughts, water scarcity, food insecurity, and ecosystem degradation, the model illustrates the danger of designing civilization around economic growth and technological expansion alone.

In this simulation, the only model that maintained long-term survivability was the Natural Complementary Science model, which places Natural Law, Harmony, Circulation, Structure, Order, and Wa at the center of civilizational design.

This result presents Natural Complementary Science not merely as an ideal or philosophy, but as a conceptual framework for redesigning the conditions of civilizational continuity.

## How to Run

Install the minimal dependencies:

```bash
pip install -r requirements.txt
```

Run the simulation:

```bash
python civilization_survival_sim.py
```

The script saves:

- `outputs/civilization_survival_results.csv`
- `outputs/civilization_survival_index.png`

## Scope and Limitations

This module is conceptual and non-predictive. It should not be used for policy forecasting, ecological prediction, risk quantification, or claims of scientific validation. Its purpose is to make assumptions visible and to support discussion about how civilizational values may shape ecological restoration, resource stability, social order, and long-term continuity.
