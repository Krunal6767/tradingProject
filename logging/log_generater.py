import logging

def setup_logging(log_file):
    """
    Set up logging configuration.

    :param log_file: Path to the log file
    """
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def log_info(message):
    """
    Log an informational message.

    :param message: Message to log
    """
    logging.info(message)

def log_error(message):
    """
    Log an error message.

    :param message: Error message to log
    """
    logging.error(message)

if __name__ == "__main__":
    # Set up logging configuration (replace 'trading_log.log' with your log file path)
    log_file = 'trading_log.log'
    setup_logging(log_file)

    # Log some example messages
    log_info("This is an informational message.")
    log_error("This is an error message.")
