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
- Plant-level feature engineering
- Python data processing
- Survival modeling in R
- Spatial prediction and visualization

This repository accompanies the published manuscript and is intended to support reproducible research and future development of plant-level disease risk modeling workflows.

---

## Repository Structure

| Folder | Purpose |
|---|---|
| `data/` | Placeholder for raw, interim, and processed data documentation. Large UAV datasets are not stored in this repository. |
| `docs/` | Supporting documentation and figures, including the workflow graphic. |
| `scripts/01_arcgis_preprocessing/` | ArcGIS Pro / ArcPy preprocessing workflow for UAV imagery and plant-level spatial metrics. |
| `scripts/02_python_processing/` | Python processing for plant-level feature construction, quality control, and longitudinal dataset preparation. |
| `scripts/03_survival_modeling/` | R-based survival modeling workflow, including Random Survival Forest analyses. |
| `scripts/04_risk_mapping/` | Spatial prediction and risk mapping outputs. |
| `scripts/05_figures/` | Publication figures and tables. |
| `src/` | Reusable project code, helper functions, or package-style utilities. |
| `archive/` | Development archive and earlier workflow versions retained for transparency. |

```text
Strawberry_Risk_Mapping/
│
├── data/
├── docs/
│   └── images/
│       └── workflow.png
├── scripts/
│   ├── 01_arcgis_preprocessing/
│   ├── 02_python_processing/
│   ├── 03_survival_modeling/
│   ├── 04_risk_mapping/
│   └── 05_figures/
├── src/
├── archive/
├── LICENSE
├── CITATION.cff
└── README.md
```

## Getting Started

### Requirements

- ArcGIS Pro
- Python 3.x
- R (for survival modeling)
- Clone this repository

### Configure the project

Update the project root in:

```text
scripts/01_arcgis_preprocessing/config.py

---

## Workflow Stages

### 01 — ArcGIS Pro Preprocessing

Preprocess UAV multispectral imagery into plant-level spatial datasets.

Outputs include:

- Clipped orthomosaics
- NDVI, NDRE, and Redness Index rasters
- Plant polygons
- Plant centroids
- Plant hexagons
- Plant-level canopy metrics

### 02 — Python Processing

Integrate plant-level observations, perform quality control, and prepare longitudinal datasets for survival analysis.

### 03 — Survival Modeling

Develop plant-level survival models in R using Random Survival Forests and associated analyses.

### 04 — Risk Mapping

Project predicted survival probabilities back into geographic space to generate canopy decline risk maps.

### 05 — Figures and Tables

Generate publication-quality figures and tables used in the manuscript.

---

## Data Availability

Large UAV imagery, Pix4D outputs, geodatabases, and intermediate raster products are **not included** because of their size.

The repository contains:

- Processing notebooks
- Analysis scripts
- Documentation
- Configuration templates
- Example datasets, where possible

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
