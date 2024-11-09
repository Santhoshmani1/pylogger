import logging

logger_config = [
    {"name": "DEBUG", "level": logging.DEBUG, "color": "02"}, 
    {"name": "INFO", "level": logging.INFO, "color": "92"}, 
    {"name": "WARNING", "level": logging.WARNING, "color": "01;93"}, 
    {"name": "ERROR", "level": logging.ERROR, "color": "01;91"}, 
    {"name": "CRITICAL", "level": logging.CRITICAL, "color": "01;95"}, 
]

class ColorFormatter(logging.Formatter):
    def format(self, record):
        log_colors = {
            color["name"]: f"\033[{color['color']}m" for color in logger_config
        }
        reset_color = "\033[0m"
        color = log_colors.get(record.levelname, "")

        log_fmt = (
            f"{color}%(asctime)s - %(name)s - %(levelname)s - %(message)s{reset_color}"
        )
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(ColorFormatter())

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(ColorFormatter())

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

def log(level, message):
    """Log a message with a specific level."""
    if isinstance(level, str):
        level = getattr(logging, level.upper())
    logger.log(level, message)
