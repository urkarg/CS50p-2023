def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        raw_date = input("Date: ").strip()
        try:
            month, day, year = raw_date.split()
            if len(day) == 1 or (len(day)==2 and day[1] != ','):
                continue
            else:
                day = int(day.removesuffix(","))
            try:
                month = months.index(month)+1
            except:
                continue
        except ValueError:
            try:
                month, day, year = raw_date.split(sep="/")
                month = int(month)
                day = int(day)
                year = int(year)
            except:
                continue
        if day > 31 or month > 12:
            continue
        break
    print(f"{year}-{month:02}-{day:02}")

main ()