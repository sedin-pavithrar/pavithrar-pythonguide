from custom_logger_module import Logger

log = Logger() # internally logger = Logger.__new__(Logger)
                #Logger.__init__(logger)

log.info("Application started")
log.debug("Loading configuration file")
log.warning("API response time is high")
log.error("Database connection failed")