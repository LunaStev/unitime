# Custom "Universal" Time System based on user's definitions
# 1 second = 100,000,000 units
# 1 day = 10 hours; 1 hour = 100 minutes; 1 minute = 100 seconds
# Calendar: 1 year = 500 days; 1 month = 10 months/year; 1 month = 50 days

from dataclasses import dataclass
from datetime import datetime, timezone
import math

UNITS_PER_SECOND = 100_000_000

SECONDS_PER_SECOND = 1
SECONDS_PER_MINUTE = 100 * SECONDS_PER_SECOND
SECONDS_PER_HOUR = 100 * SECONDS_PER_MINUTE
SECONDS_PER_DAY = 10 * SECONDS_PER_HOUR
DAYS_PER_MONTH = 50
MONTHS_PER_YEAR = 10
DAYS_PER_YEAR = 500
SECONDS_PER_MONTH = DAYS_PER_MONTH * SECONDS_PER_DAY
SECONDS_PER_YEAR = DAYS_PER_YEAR * SECONDS_PER_DAY

# Epoch: 1970-01-01T00:00:00Z maps to 0-01-01 00:00:00 in this calendar
EPOCH = datetime(1970, 1, 1, 0, 0, 0, tzinfo=timezone.utc)

@dataclass
class UniversalDateTime:
    year: int
    month: int  # 1..10
    day: int    # 1..50
    hour: int   # 0..9
    minute: int # 0..99
    second: int # 0..99
    unit: int   # 0..99_999_999 (fractional units within the custom second)

def from_unix_to_universal(unix_seconds: float) -> UniversalDateTime:
    # total seconds since epoch
    total_seconds = int(math.floor(unix_seconds))
    fractional_second = unix_seconds - total_seconds
    
    # compute units inside the current second
    units_in_second = int(round(fractional_second * UNITS_PER_SECOND))
    if units_in_second == UNITS_PER_SECOND:
        # carry over if rounding hits the next second
        total_seconds += 1
        units_in_second = 0

    # break down total_seconds into custom calendar
    years = total_seconds // SECONDS_PER_YEAR
    rem = total_seconds % SECONDS_PER_YEAR

    months = rem // SECONDS_PER_MONTH
    rem = rem % SECONDS_PER_MONTH

    days = rem // SECONDS_PER_DAY
    rem = rem % SECONDS_PER_DAY

    hours = rem // SECONDS_PER_HOUR
    rem = rem % SECONDS_PER_HOUR

    minutes = rem // SECONDS_PER_MINUTE
    rem = rem % SECONDS_PER_MINUTE

    seconds = rem  # 0..99

    # Convert to 1-based day/month for display
    return UniversalDateTime(
        year=years, 
        month=months + 1, 
        day=days + 1, 
        hour=hours, 
        minute=minutes, 
        second=seconds, 
        unit=units_in_second
    )

def to_units_since_epoch(unix_seconds: float) -> int:
    return int(round(unix_seconds * UNITS_PER_SECOND))

def now_universal():
    now_utc = datetime.now(timezone.utc)
    delta = (now_utc - EPOCH).total_seconds()
    udt = from_unix_to_universal(delta)
    total_units = to_units_since_epoch(delta)
    return now_utc, udt, total_units

# Compute and present current universal time
now_utc, udt, total_units = now_universal()

display_str = (
    f"Current UTC: {now_utc.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}Z\n"
    f"Universal Time (custom): "
    f"{udt.year:04d}-{udt.month:02d}-{udt.day:02d} "
    f"{udt.hour:02d}:{udt.minute:02d}:{udt.second:02d} + {udt.unit} units\n"
    f"Total units since epoch (1970-01-01Z): {total_units:,} units\n\n"
    f"Constants:\n"
    f"- 1 second = {UNITS_PER_SECOND:,} units\n"
    f"- 1 minute = 100 seconds = {SECONDS_PER_MINUTE:,} s\n"
    f"- 1 hour = 100 minutes = {SECONDS_PER_HOUR:,} s\n"
    f"- 1 day = 10 hours = {SECONDS_PER_DAY:,} s\n"
    f"- 1 month = 50 days = {SECONDS_PER_MONTH:,} s\n"
    f"- 1 year = 500 days = {SECONDS_PER_YEAR:,} s\n"
)

print(display_str)
print(
    f"Current Universal Time: {udt.year} Year {udt.month} Month {udt.day} Day "
    f"{udt.hour} Hour {udt.minute} Minute {udt.second} Second"
)
