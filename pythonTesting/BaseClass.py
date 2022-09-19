import inspect
import logging
class BaseClass:
      def getLogger(self):
          loggerName = inspect.stack()[1][3]
          logger = logging.getLogger(loggerName)
          fileHandler = logging.FileHandler("pytest_log.log")
          Formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
          fileHandler.setFormatter(Formatter)
          logger.addHandler(fileHandler)
          logger.setLevel(logging.INFO)
          return logger