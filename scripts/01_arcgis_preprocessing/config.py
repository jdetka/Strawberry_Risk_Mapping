"""
Configuration file for the Strawberry Risk Mapping project.
Update PROJECT_ROOT to point to the location of your local project data.
"""

from pathlib import Path

# =============================================================================
# PROJECT ROOT
# =============================================================================

PROJECT_ROOT = Path(r"D:\2023_El_Rio_Lobo")

# =============================================================================
# PROJECT FOLDERS
# =============================================================================

RASTERS = PROJECT_ROOT / "Rasters"
CLIPPED_RASTERS = RASTERS / "clipped"

VECTORS = PROJECT_ROOT / "Vectors"
TREATMENT_BLOCKS = VECTORS / "Treatment_Blocks"

# Outputs
NDVI_OUTPUT = CLIPPED_RASTERS / "NDVI_Output"
CLASSIFICATION_OUTPUT = PROJECT_ROOT / "Classification_Raster_Output"
POLYGON_OUTPUT = PROJECT_ROOT / "Polygon_Output"
HEXAGON_TEMP_OUTPUT = PROJECT_ROOT / "Hexagon_Temp_Output"
CENTROID_OUTPUT = VECTORS / "Centroid_Output"

# =============================================================================
# PROJECT SETTINGS
# =============================================================================

SITE_CODE = "ERL"
FIELDS = [1, 2, 3, 4]