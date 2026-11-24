"""Copy the bundled image to the requested output directory."""

import os
from pathlib import Path
import shutil


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    if not source.is_file():
        raise SystemExit(f"Missing bundled image: {source}")

    output_value = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    output_dir = Path(output_value if output_value.strip() else "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    with source.open("rb") as image, (output_dir / "entry.png").open("wb") as output:
        shutil.copyfileobj(image, output, length=1024 * 1024)


if __name__ == "__main__":
    main()
