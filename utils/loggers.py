import logging
import os

# Create reports folder if not exists
if not os.path.exists("reports"):
    os.makedirs("reports")

def get_logger(name="TestLogger"):
    """
    Creates and returns a logger instance.
    Logs are written to both console and file.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if not logger.handlers:
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        ch.setFormatter(ch_formatter)

        # File handler
        fh = logging.FileHandler("reports/test_log.log")
        fh.setLevel(logging.INFO)
        fh_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(fh_formatter)

        # Add handlers to logger
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger
