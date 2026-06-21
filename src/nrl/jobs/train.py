"""
Train job. This fits the model and persists a versioned artifact.
"""
import logging
from nrl.core.config import settings

logging.basicConfig(level=settings.log_level)
log = logging.getLogger("nrl.jobs.train")

def main() -> None:
    log.info("Train Started (env=%s) -- PLACEHOLDER --", settings.env)
    log.info("Train Finished -- PLACEHOLDER --")

if __name__ == "__main__":
    main()