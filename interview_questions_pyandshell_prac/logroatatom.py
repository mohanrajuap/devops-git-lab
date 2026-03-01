from pathlib import Path
from datetime import datetime

LOG_FILE = Path("/data/tomcat/catalina.out")
MAX_SIZE = 5 * 1024 * 1024  # 5 MB

if LOG_FILE.exists() and LOG_FILE.stat().st_size > MAX_SIZE:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    rotated_file = LOG_FILE.parent / f"catalina_{timestamp}.out"
    LOG_FILE.rename(rotated_file)
    LOG_FILE.touch()
