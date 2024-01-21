import logging

class LoggingModule:
    def __init__(self):
        self.logger = logging.getLogger('system_logger')
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        # Create a file handler to store logs in a centralized location
        file_handler = logging.FileHandler('system_logs.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        
        # Create a console handler to display logs in the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        
        # Add the handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def log_activity(self, activity):
        self.logger.debug(activity)
    
    def log_error(self, error):
        self.logger.error(error)

# Usage example
logging_module = LoggingModule()
logging_module.log_activity('System started')
logging_module.log_error('An error occurred')
