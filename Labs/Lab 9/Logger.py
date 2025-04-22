import logging
import logging.handlers
from datetime import timedelta, datetime

logging.basicConfig(force=True)

debug_log = logging.getLogger("FarmLogger")

format = logging.Formatter(  
    fmt=(
        "%(asctime)s | %(levelname)s | %(filename)s | %(message)s"
    )
)

handler = logging.handlers.TimedRotatingFileHandler(
        filename="Labs/Lab 9/Logs/DavidLongLogFiles/Old_Mcdonalds_Security.log", #file name
        when="D", #rolls the log every day
        backupCount=3, # only keep 3 days worth of file backups
)

handler.setFormatter(format)
debug_log.addHandler(handler)
debug_log.setLevel(logging.DEBUG)



debug_log.warning("Bingo isn't acting himself today")
debug_log.error("Bingo has gone missing")
debug_log.error("The farm is out of feed")
debug_log.error("The cold winter wiped out the crops")
debug_log.critical("The wolf broke onto the farm and killed a sheep")
debug_log.critical("The hawk swooped in and ate the chickens")
debug_log.critical("System Failure, Shutting Down")

debug_log = logging.getLogger("FarmLogger.Cameras")

debug_log.info("Another Day passes on the farm")
debug_log.info("Old Mcdonalds Animals are all safe")
debug_log.warning("The wolf appeared")
debug_log.warning("The hawk is circling overhead")
debug_log.error("Security Camera Failure")
debug_log.critical("System Failure, Shutting Down")