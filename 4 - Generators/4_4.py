def gen_secs():
    sec = range(0, 60)
    for i in sec:
        yield i


def gen_minutes():
    min = range(0, 60)
    for i in min:
        yield i


def gen_hours():
    hour = range(0, 24)
    for i in hour:
        yield i


def gen_time():
    for i in gen_hours():
        for j in gen_minutes():
            for k in gen_secs():
                yield "%02d:%02d:%02d" % (i, j, k)


def gen_years(start=2019):
    while True:
        yield start
        start += 1


def gen_months():
    month = range(1, 13)
    for i in month:
        yield i


def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31,
        2: 29 if leap_year else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    for i in range(month, days_in_month[month+1]):
        yield i


def gen_date():
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month):
                for time in gen_time():
                    yield "%02d/%02d/%02d" % (day, month, year) + " " + time


def main():
    date_gen = gen_date()

    counter = 1
    for i in date_gen:
        if counter == 1000000:
            print(next(date_gen))
            counter = 1
        counter += 1


if __name__ == '__main__':
    main()
