"""
Predict job. Writes predictions for the upcoming round
"""
import logging
from nrl.core.config import settings

logging.basicConfig(level=settings.log_level)
log = logging.getLogger("nrl.jobs.predict")

def main() -> None:
    log.info("Predict Started (env=%s) -- PLACEHOLDER --", settings.env)
    log.info("Predict Finished -- PLACEHOLDER -- ")

if __name__ == "__main__":
    main()