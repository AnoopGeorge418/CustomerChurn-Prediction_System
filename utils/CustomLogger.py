import logging, os, sys
from datetime import datetime

class CustomLogger:
    """Custom logger class to handle logging across the application"""

    def __init__(self, log_file = None, module_name = None):
        # Create logs directory if it doesn't exist
        log_dir = os.path.join(os.getcwd(), 'logs')
        os.makedirs(log_dir, exist_ok = True)

        # Generate log filename with timestamp if not provided
        if log_file is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            module_prefix = f"{module_name}_"if module_name else ""
            log_file = os.path.join(log_dir, f"{module_prefix}log_{timestamp}.log")

        # Configure logging format
        logging_format = "[%(asctime)s] %(levelname)s - %(name)s - %(module)s - %(funcNamre)s - %(lineno)d - %(message)s"
        date_format = "%Y-%m-%d %H:%M:%S"

        # Set up file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter(logging_format, date_format))

        # Set up console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(logging.Formatter(logging_format, date_format))

        # Get logger instance
        logger_name = module_name if module_name else "main"
        self.logger = logging.getLogger(logger_name)

        # Set log level
        self.logger.setLevel(logging.INFO)

        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

        # Prevent log propagation to avoid duplicate logs
        self.logger.propagate = False

    def get_logger(self):
        """Return the configured logger instance"""
        return self.logger
    
    def info(self, message):
        """Log info level message"""
        self.logger.info(message)
    
    def warning(self, message):
        """Log warning level message"""
        self.logger.warning(message)
    
    def error(self, message):
        """Log error level message"""
        self.logger.error(message)
    
    def critical(self, message):
        """Log critical level message"""
        self.logger.critical(message)

    def debug(self, message):
        """Log debug level message"""
        self.logger.debug(message)

