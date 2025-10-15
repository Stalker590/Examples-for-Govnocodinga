from datetime import datetime, timezone
import time

def get_utc_now() -> datetime:
    """
    Повертає точний час за UTC.
    """
    return datetime.now(timezone.utc)

