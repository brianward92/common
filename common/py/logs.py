from datetime import datetime, timezone
import logging
from math import ceil, log10
import sys


class CustomFormatter(logging.Formatter):
    """Custom Formatter for adding colors and extra details to logs."""

    # Define log colors
    grey = "\x1b[38;5;246m"
    green = "\x1b[32;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"  # ANSI reset code to reset text formatting

    format = "%(utc_time)s UTC :: %(pathname)s :: %(line_info)s :: %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }
    LONG_LINE_LEN = 1000
    LONG_LINE_MRK = "LINF"
    LINE_INFO_PRL = 1 + ceil(log10(LONG_LINE_LEN))
    assert (
        len(LONG_LINE_MRK) == LINE_INFO_PRL
    ), f"Bad long line marker ({LONG_LINE_MRK}) for line info print length ({LINE_INFO_PRL})"

    def format(self, record):
        utc_time = datetime.fromtimestamp(record.created, tz=timezone.utc)
        record.utc_time = utc_time.strftime("%Y-%m-%d %H:%M:%S") + ",%03d" % (
            utc_time.microsecond // 1000
        )

        # Format the line number with the custom requirement
        if record.lineno >= self.LONG_LINE_LEN:
            record.line_info = self.LONG_LINE_MRK
        else:
            x = f"L{record.lineno}"
            x = " " * (self.LINE_INFO_PRL - len(x)) + x
            record.line_info = x

        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


IS_LOGGING_CONFIGURED = False


def setup_logging():
    # Only Needs to Be Done Once
    global IS_LOGGING_CONFIGURED
    if IS_LOGGING_CONFIGURED:
        return
    # Base Logger
    logging.getLogger("selectors").setLevel(logging.INFO)
    logging.getLogger("urllib3").setLevel(logging.INFO)
    logging.getLogger("matplotlib").setLevel(logging.INFO)
    logging.getLogger("asyncio").setLevel(logging.INFO)
    # Config
    handler = logging.StreamHandler(sys.stdout)  # where to ? / base handle
    handler.setFormatter(CustomFormatter())  # customizations
    logging.basicConfig(level=logging.DEBUG, handlers=[handler])  # pass handle
    logging.captureWarnings(True)
    IS_LOGGING_CONFIGURED = True
    return


def get_logger():
    setup_logging()
    return logging.getLogger()
