<h1 align="center">🍓 Strawberry Risk Mapping</h1>

<p align="center">
  <strong>Reproducible workflow for UAV-based plant-level survival modeling and canopy decline prediction</strong>
</p>

<p align="center">
  <a href="https://doi.org/10.3390/drones10040235">
    <img src="https://img.shields.io/badge/DOI-10.3390%2Fdrones10040235-blue" alt="DOI">
  </a>
</p>

<p align="center">
  <img src="docs/images/workflow.png" alt="Workflow for the Strawberry Risk Mapping pipeline" width="900">
</p>

<p align="center">
  <em>Computational workflow for transforming UAV multispectral imagery into plant-level survival datasets and spatial canopy decline risk maps.</em>
</p>

---

## Companion Publication

This repository contains the computational workflow supporting the publication:

> **Detka, J. R., Purdy, A. J., Melton, F. S., Daugovish, O., Greer, C. A., & Martin, F. N. (2026).**  
> *A Plant-Level Survival Modeling Framework for Spatiotemporal Strawberry Canopy Decline Using UAV Multispectral Time Series.*  
> **Drones**, 10(4), 235.  
> https://doi.org/10.3390/drones10040235

---

## Overview

This repository documents the workflow used to transform UAV multispectral imagery into plant-level survival datasets and predictive canopy decline risk maps.

The workflow combines:

- UAV multispectral image acquisition
- ArcGIS Pro geospatial preprocessing
- Plant-level feature construction
- Leakage-safe Random Survival Forest modeling
- Spatial risk prediction
- Statistical analysis and visualization

This repository accompanies the published manuscript and is intended to support reproducible research and future development of plant-level disease risk modeling workflows.

---

## Repository Structure

| Folder | Purpose |
|---|---|
| `data/processed` | Processed datasets used as inputs to the Random Survival Forest workflow. Large UAV imagery, Pix4D outputs, and intermediate GIS products are not included due to their size. |
| `docs/` | Supporting documentation and figures, including the workflow graphic. |
| `scripts/01_arcgis_preprocessing/` | ArcGIS Pro / ArcPy workflow for transforming UAV multispectral imagery into plant-level canopy metrics. |
| `scripts/02_rsf_modeling/` | Leakage-safe Random Survival Forest workflow, including feature engineering, model training, validation, and spatial risk prediction. |
| `scripts/03_results_and_reporting/` | Risk summaries, post hoc analyses, tables, and publication figures derived from the modeling results. |
| `src/` | Reusable helper functions and utilities (future development). |
| `archive/` | Development archive and earlier workflow versions retained for transparency. |

```text
Strawberry_Risk_Mapping/
│
├── data/
│   ├── processed/
│   └── derived/
│
├── docs/
│   └── images/
│       └── workflow.png
│
├── scripts/
│   ├── 01_arcgis_preprocessing/
│   ├── 02_rsf_modeling/
│   └── 03_results_and_reporting/
│
├── src/
├── archive/
├── LICENSE
├── CITATION.cff
└── README.md
```

## Repository Status

| Stage | Status |
|--------|:------:|
| ArcGIS preprocessing | ✅ |
| RSF modeling | ✅ |
| Results & reporting | 🚧 |

## Getting Started

### Requirements

- ArcGIS Pro
- Python 3.x
- R (for survival modeling)
- Clone this repository

### Configure the workflow

Each major workflow stage contains its own `config.py` file.

Before running a notebook, update the appropriate configuration file to point to your local project directories.

```
scripts/01_arcgis_preprocessing/config.py
scripts/02_rsf_modeling/config.py
```

Large UAV imagery and intermediate GIS products are not included in this repository because of their size.

---

## Workflow Stages

### 01 — ArcGIS Pro Preprocessing

Transform UAV multispectral imagery into plant-level canopy datasets.

Major outputs include:

- Clipped multispectral orthomosaics
- NDVI, NDRE, and Redness Index rasters
- Plant polygons and centroids
- Plant hexagons
- Plant-level canopy metrics exported for statistical modeling

---

### 02 — Random Survival Forest Modeling

Build longitudinal plant datasets, engineer temporal features, and develop leakage-safe Random Survival Forest models.

Major tasks include:

- Feature engineering
- Plant-level train/test splitting
- Per-flight clustering
- Survival data formatting
- Expanding-window Random Survival Forest modeling
- Plant-level risk prediction
- Export of spatial risk layers

---

### 03 — Post-processing and Visualization

Generate summary statistics, post hoc analyses, spatial products, and publication-quality figures.

Major outputs include:

- Risk summary tables
- Post hoc fumigation analyses
- Risk maps
- Figures used in the accompanying publication

---

## Data Availability

The repository contains:

- Processing notebooks
- Analysis scripts
- Documentation
- Configuration files
- Processed example datasets required to reproduce the statistical workflow

---

## Software

This project uses:

- ArcGIS Pro
- ArcPy
- Python
- R
- RandomForestSRC
- GDAL
- Pandas
- GeoPandas
- Rasterio

---

## Citation

If you use this repository in your research, please cite both this repository and the accompanying publication:

```text
Detka, J. R., Purdy, A. J., Melton, F. S., Daugovish, O., Greer, C. A., & Martin, F. N. (2026).

A Plant-Level Survival Modeling Framework for Spatiotemporal Strawberry Canopy Decline Using UAV Multispectral Time Series.

Drones, 10(4), 235.

https://doi.org/10.3390/drones10040235
```

---

## License

This repository is released under the **BSD 3-Clause License**. See the `LICENSE` file for details.
