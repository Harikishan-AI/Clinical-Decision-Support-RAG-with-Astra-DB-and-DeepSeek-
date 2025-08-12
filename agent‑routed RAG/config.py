import os
import sys
from typing import Optional

from dotenv import load_dotenv


def load_env(dotenv_path: Optional[str] = ".env") -> None:
    """Load environment variables from a .env file if present."""
    try:
        load_dotenv(dotenv_path=dotenv_path, override=False)
    except Exception:
        # Safe fallback if dotenv is not available yet
        pass


def require_env(var_name: str) -> str:
    """Read a required environment variable or exit with an error."""
    value = os.environ.get(var_name, "").strip()
    if not value:
        print(f"Environment variable '{var_name}' is required.")
        sys.exit(1)
    return value


