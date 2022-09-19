
# Priotity Order is debuf , info , warning , error and critical . If I set the level as WARNING then debug and info logs will be skipped


import logging
def test_loggerExample():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler("pytest_log.log")
    Formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(Formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)
    logger.info("Ths is about to give informaton")
    logger.debug("Ths is about Debug")
    logger.warning("This is about warning")
    logger.error("This is about error")
    logger.critical("This is about critcal msg")