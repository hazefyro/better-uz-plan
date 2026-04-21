import json
import sys
from pathlib import Path

import httpx
from bs4 import BeautifulSoup

from app.config.settings import settings
from app.core.parser import parse_groups

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def main() -> int:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("groups.json")

    with httpx.Client(timeout=10) as client:
        resp = client.get(settings.SUPPORTED_MAJOR)
        resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    groups = parse_groups(soup)

    out.write_text(
        json.dumps(
            [g.model_dump() for g in groups], indent=2, ensure_ascii=False
        ),
        encoding="utf-8",
    )

    print(f"Saved {len(groups)} groups to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
