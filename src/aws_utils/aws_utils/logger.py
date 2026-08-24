# aws_utils/logger.py
import logging
import os

def setup_logger(name: str) -> logging.Logger:
    """
    Configura um logger com formato simples: datahora - mensagem.
    Grava logs no console e em logs/app.log.
    """
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level, logging.INFO))

    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s - %(message)s")

        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(getattr(logging, log_level, logging.INFO))
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        # File handler
        os.makedirs("logs", exist_ok=True)
        fh = logging.FileHandler("logs/app.log")
        fh.setLevel(getattr(logging, log_level, logging.INFO))
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
