def main():
    meal_time = input("What time is it? ")
    format_time = convert(meal_time)
    if format_time >= 7.0 and format_time <= 8.0 and format_times.endswit:
        print("breakfast time")
    if format_time >= 12.0 and format_time <= 13.0:
        print("lunch time")
    if format_time >= 18.0 and format_time <= 19.0:
        print("dinner time")


def convert(time):
    hours, minute = time.split(":")
    minute = float(minute) / 60
    hours = float(hours)
    return minute + hours



if __name__ == "__main__":
    main()


# Support for 12 hr format.

def main():
    meal_time = input("What time is it? ")
    format_time = convert(meal_time)
    if format_time >= 7.0 and format_time <= 8.0:
        print("breakfast time")
    if format_time >= 12.0 and format_time <= 13.0:
        print("lunch time")
    if format_time >= 18.0 and format_time <= 19.0:
        print("dinner time")


def convert(time):

    if "AM" in time or "PM" in time:
        hours, minute_with_meridian = time.split(":")
        minute, Meridian = minute_with_meridian.split(" ")
        minute = float(minute) / 60
        hours = float(hours)

        if Meridian == "AM" and hours != 12:
            hours += 12
        elif Meridian == "PM" and hours == 12:
            hours = 0
        return minute + hours

    else:
        hours, minute = time.split(":")
        minute = float(minute) / 60
        hours = float(hours)
        return minute + hours

if __name__ == "__main__":
    main()



