"""
Ingest job. This pulls NRl fixtures/results into Postgres
"""
import logging
from nrl.core.config import settings

logging.basicConfig(level=settings.log_level)
log = logging.getLogger("nrl.jobs.ingest")

def main() -> None:
    log.info("Ingest started (env=%s) -- PLACEHOLDER --", settings.env)
    log.info("Ingestion finished --PLACEHOLDER")

if __name__ == "__main__":
    main()