def day_of_week(d, m, y):
    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if m <= 2:
        m += 12
        y -= 1
    day = (((13 * m + 3) // 5 + d + y + (y // 4) - (y // 100) + (y // 400)) % 7)
    return day_names[int(day)]


# def main():
#     print(day_of_week(23, 1, 2010))
#
#
# main()
