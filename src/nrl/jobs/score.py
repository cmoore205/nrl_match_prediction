"""
Score job. Joins predictions to results and records accuracy.
"""
import logging
from nrl.core.config import settings

logging.basicConfig(level=settings.log_level)
log = logging.getLogger("nrl.jobs.score")

def main() -> None:
    log.info("Score Started (env=%s) -- PLACEHOLDER --", settings.env)
    log.info("Score Finished -- PLACEHOLDER --")

if __name__ == "__main__":
    main()