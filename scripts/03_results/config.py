from pathlib import Path

REPO_ROOT = Path(r"D:\GitHub\Strawberry_Risk_Mapping")

PROCESSED_DATA = REPO_ROOT / "data" / "processed"
SHAPEFILE_DIR = PROCESSED_DATA / "shapefiles"

FIELD_DIRS = [
    SHAPEFILE_DIR / "field_1",
    SHAPEFILE_DIR / "field_2",
    SHAPEFILE_DIR / "field_3",
]

OUTPUT_DIR = REPO_ROOT / "output"

OUT_CSV = OUTPUT_DIR / "ERL_2023_RiskType_Counts_Percent_AllFields.csv"
OUT_CSV_BYTMT = OUTPUT_DIR / "ERL_2023_RiskType_Counts_Percent_AllFields_BYTMT.csv"

GRAPHICS_DIR = REPO_ROOT / "graphics"
RISK_FRAMES_DIR = GRAPHICS_DIR / "risk_frames"

OUT_TABLE_CSV = OUTPUT_DIR / "ERL_2023_PostHoc_Fumigation_Table4_Python.csv"
ECDF_DIR = GRAPHICS_DIR / "ecdf_plots"