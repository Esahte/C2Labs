def days_in_month(month):
    month_days = [('January', [31]), ('February', [28, 29]), ('March', [31]),
                  ('April', [30]), ('May', [31]), ('June', [30]), ('July', [31]),
                  ('August', [31]), ('September', [30]), ('October', [31]),
                  ('November', [30]), ('December', [31])]
    for i in month_days:
        for x in i:
            if x == month:
                return i[1]
    return 'empty list'


# def main():
#     print(days_in_month('December'))
#
#
# main()
