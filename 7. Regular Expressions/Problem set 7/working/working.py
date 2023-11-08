import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    hour = f"(([1-9]|1[0-2])(:([0-5][0-9])|(60))? (AM|PM))"
    if time := re.search(rf"^{hour} to {hour}$", s):
        h1 = convert_hour(time.group(1), time.group(2))
        h2 = convert_hour(time.group(7), time.group(8))
        m1 = convert_minutes(time.group(3))
        m2 = convert_minutes(time.group(9))
        return f"{h1:02}:{m1} to {h2:02}:{m2}"
    else:
        raise ValueError


def convert_minutes(minutes):
    if minutes == None:
        return "00"
    else:
        return minutes.strip(":")


def convert_hour(hour_bef_conv, hour_aft_conv):
    if hour_bef_conv.endswith("AM") and hour_aft_conv == "12":
        return "00"
    elif hour_bef_conv.endswith("PM") and hour_aft_conv != "12":
        return int(hour_aft_conv) + 12
    else:
        return int(hour_aft_conv)


if __name__ == "__main__":
    main()