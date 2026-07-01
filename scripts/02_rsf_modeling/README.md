# Random Survival Forest Modeling

This notebook converts plant-level canopy metrics generated during the ArcGIS preprocessing workflow into longitudinal datasets for survival analysis.

Major workflow components include:

- Merge canopy metrics across dates
- Feature engineering
- Clustering and event definition
- Random Survival Forest model training
- Model validation
- Risk prediction
- Export of spatial risk layers