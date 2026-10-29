"""Prepare static frontend assets for Vercel's CDN."""

from pathlib import Path
import shutil

PROJECT_ROOT = Path(__file__).resolve().parent
PUBLIC_DIR = PROJECT_ROOT / "public"


def main() -> None:
    PUBLIC_DIR.mkdir(exist_ok=True)
    for filename in ("index.html", "styles.css", "app.js"):
        shutil.copy2(PROJECT_ROOT / filename, PUBLIC_DIR / filename)


if __name__ == "__main__":
    main()
