# Logging in Python

## Achieving Custom Formatting

When creating your own logging module in Python, it is essential to understand that the base formatting from the standard library (STL) `logging` module resides in `logging.Formatter`. You can customize this formatting by subclassing `logging.Formatter`, as shown below:

```python
class CustomFormatter(logging.Formatter):
    ...
```
In subsequent sections we show the part of the definition of `CustomFormatter` that is relevant together with this header, omitting other parts of the definition that are not being discussed.

#### Applying Custom Formatting
Formatters are then passed in when we set up the logging style. This is an "at most one time" thing as it needs to be done the first time we create a `logger` and never again. Hence, we use a global state here to capture whether or not that's been done.
```
IS_LOGGING_CONFIGURED = False
def setup_logging():
    # Only Needs to Be Done Once
    global IS_LOGGING_CONFIGURED
    if IS_LOGGING_CONFIGURED:
        return
    # Base Logger
    logging.getLogger("selectors").setLevel(logging.WARNING)
    # Config
    handler = logging.StreamHandler(sys.stdout) # where to ? / base handle
    handler.setFormatter(CustomFormatter()) # customizations
    logging.basicConfig(level=logging.DEBUG, handlers=[handler]) # pass handle
    logging.captureWarnings(True)
    IS_LOGGING_CONFIGURED = True
```
Not running this all the time gives users the option to do this import `from common.py import logs` "for free" since it won't run. Capturing it in a function cleans up any output to the console made by those commands.

## Message Structure

This is a nice message structure that shows the UTC time, where the code is running, what line is being messaged about, and a message to aid in understanding the message type.
```python
class CustomFormatter(logging.Formatter):
    format = "%(utc_time)s UTC :: %(pathname)s :: %(line_info)s :: %(message)s"

    ...
```
In this custom format, only `message` and `pathname` are available directly. We will need to construct `utc_time` and `line_info` directly.

## Color and Output Formats
To enhance the readability of log messages, you can add colors and custom output formats. This is achieved using `ANSI` escape codes to add colors to different log levels (`DEBUG, INFO, WARNING, ERROR, CRITICAL`). Here's an example of how to define a custom formatter with colored output:

```python
class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;5;246m"
    green = "\x1b[32;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    ...
```
For now simply note that the colors are paired with the various message types.

#### `reset`
The `reset` variable contains the `ANSI` escape code `"\x1b[0m"`, which resets all formatting attributes (like color) back to their default values. This is crucial to ensure that the colored formatting only affects the specific log message and not any subsequent text in the terminal. The format definitions like
```python
logging.INFO: green + format + reset,
```
mean "for an `info` message, `python` sends the $\texttt{\textcolor{green}{green}}$ color indicator to `STDOUT`, then the formatted message, then the `reset` indicator to revert that stateful change."

## Line Number
A neat way to format line numbers is as follows:

```
  L1
 L12
L123
LINF
```
In particular, line numbers of at most three digits are prefixed with the character `L` and right justified to always be strings of length four. If the line number is four digits or more (i.e., the line number is `>= 1000`), we show `LINF`.

To achieve this, you need to override the `format` method in `CustomFormatter`. This method takes a `record` of data about the log message and is called before that message appears. Conveniently, the typical `record` object provides access to the line number via `record.lineno`. Here is an example of how to create a customized string for line numbers:

```python
class CustomFormatter(logging.Formatter):
    LONG_LINE_LEN = 1000
    LONG_LINE_MRK = "LINF"
    LINE_INFO_PRL = 1 + ceil(log10(LONG_LINE_LEN))
    assert (
        len(LONG_LINE_MRK) == LINE_INFO_PRL
    ), f"Bad long line marker ({LONG_LINE_MRK}) for line info print length ({LINE_INFO_PRL})"

    def format(self, record):
        if record.lineno >= self.LONG_LINE_LEN:
            record.line_info = self.LONG_LINE_MRK
        else:
            x = f"L{record.lineno}"
            x = " " * (self.LINE_INFO_PRL - len(x)) + x
            record.line_info = x

        ...
```
Note that with our `LONG_LINE_LEN=1000` then anything `>=1000` is going to be `LINF`, which is four characters long and saved in `LONG_LINE_MRK`. It is a convenience that `1+ceil(log10(LONG_LINE_LEN))` would in general work out to include the additional character for the `L`. If `LONG_LINE_LEN` is in `(10**(k-1), 10**k]` then `10**(k-1) < LONG_LINE_LEN <= 10**k` and `k-1 < log10(LONG_LINE_LEN) <= k`. That implies again that `ceil(log10(LONG_LINE_LEN))=1+k`. We would need at most `k` characters to get the display right for the number part, `+1` always for the `L`, then the format method adjusts to get to exactly `k+1`.

Then we just need to construct the value of `line_info` variable in order to get a good display out.

## UTC Timestamps
To include timestamps in UTC with millisecond precision, you need to manually format the time within the format method. The `asctime` field is a special macro in the `logging` module, so you should create your own `utc_time` field:

```python
class CustomFormatter(logging.Formatter):
    def format(self, record):
        utc_time = datetime.fromtimestamp(record.created, tz=timezone.utc)
        record.utc_time = utc_time.strftime("%Y-%m-%d %H:%M:%S") + ",%03d" % (utc_time.microsecond // 1000)

        ...
```
This gives us access to an attribute `.utc_time` which can be displayed in the log message.

## Additional Considerations

#### Extending for `Windows` Users
The current implementation uses `ANSI` escape codes for colored output, which may not work natively on `Windows` terminals. To extend this functionality for `Windows` users, you can use the `colorama` library. This requires a code change, not just a configuration change. The logging will work as is on `Windows`, but without color, unless `colorama` is used.

Here is how you can modify the code to support colors on `Windows`:

1. Install `colorama`.
2. Import it as `import colorama`.
3. Call `colorama.init()` in `setup_logging`.

This hasn't been tested so I won't include it.
