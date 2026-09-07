"""Keep the small experiment helpers importable without installing a package."""
import sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
