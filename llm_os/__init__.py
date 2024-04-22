from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR: Path = Path(__file__).parent

from .storage import client  # noqa

load_dotenv()
