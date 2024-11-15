import argparse
import datetime
import os
import platform
import shutil
import subprocess


from common.py import logs

log = logs.get_logger()


def create_parser():
    parser = argparse.ArgumentParser(description="Opens or creates journal tex file.")
    parser.add_argument("--year", "-y", type=int)
    parser.add_argument("--month", "-m", type=int)
    default_journal_path = os.path.expanduser("~/doc/journal")
    parser.add_argument("--path", "-p", default=default_journal_path)
    parser.add_argument("--open", "-o", action="store_true")
    return parser


if __name__ == "__main__":

    # Parser, Args
    parser = create_parser()
    args = parser.parse_args()
    year = args.year
    month = args.month
    do_open = args.open
    if year is None:
        print("Year:", end=" ")
        year = int(input())
    if month is None:
        print("Month:", end=" ")
        month = int(input())
    path = args.path
    log.info(f"Opening journal for {year=} and {month=} at {path=}.")

    # Format Year/Month Directory
    try:
        yyyymm = datetime.date(year, month, 1).strftime(f"%Y{os.path.sep}%m")
    except:
        raise ValueError(f"Cannot format inputs {year=}, {month=}!")

    # Assert Template
    template = os.path.join(path, "main.tex")
    assert os.path.exists(template), f"Expected template file at {template}."

    # Copy Template if Needed
    journal = os.path.join(path, yyyymm, "main.tex")
    if not os.path.exists(journal):
        os.makedirs(os.path.dirname(journal), exist_ok=True)
        shutil.copy(template, journal)
        log.info(f"No journal at {journal}, copied from {template}.")
    else:
        log.info(f"Found existing journal at {journal}.")

    # Open It
    plat = platform.system()
    if plat == "Windows":
        if do_open:
            subprocess.call(["notepad", journal])
        else:
            os.startfile(journal)
        log.info(f"Opened {journal} on Windows.")
    elif plat == "Darwin":
        if do_open:
            subprocess.call(["vim", journal])
        else:
            subprocess.call(("open", journal))
        log.info(f"Opened {journal} on Mac.")
    else:
        if do_open:
            subprocess.call(["vim", journal])
        else:
            subprocess.call(("xdg-open", journal))
        log.info(f"Opened {journal} on Linux.")
