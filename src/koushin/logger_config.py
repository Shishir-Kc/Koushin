import logging


def setup_logger(name:str):
    from koushin.config.config import cretate_logger_file
    """
       This function will set up logger 
       
       ARGS:
       
        name -> logger name  

    """

    logger = logging.getLogger(name)
    formatter = logging.Formatter(
         "| %(asctime)s | %(levelname)s | %(name)s | %(message)s |"
    )
    file_path = cretate_logger_file()
    file_handler = logging.FileHandler(file_path/"koushin.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
