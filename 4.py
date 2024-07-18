my,mm, md = map(int,input().split('/'))
def gregorian_to_jalali(year, month, day):
    g_year = year
    g_month = month
    g_day = day

    # محاسبه سال کبیسه در تقویم میلادی
    if (g_year % 4 == 0 and g_year % 100 != 0) or (g_year % 400 == 0):
        g_leap = 1
    else:
        g_leap = 0

    # محاسبه سال کبیسه در تقویم شمسی
    if (g_year % 33 == 1) and ((g_year % 4 == 0 and g_year % 100 != 0) or (g_year % 400 == 0)):
        j_leap = 1
    elif (g_year % 33 == 2) and ((g_year % 4 == 0 and g_year % 100 != 0) or (g_year % 400 == 0)):
        j_leap = 1
    elif (g_year % 33 == 3) and ((g_year % 4 == 0) or (g_year % 400 == 0)):
        j_leap = 1
    else:
        j_leap = 0

    # تبدیل تاریخ میلادی به شمسی
    j_year = g_year - 621
    j_day = (g_day - 8) * 30 + 17209
    j_month = 12 * j_year + 3 // 4
    j_month += g_month + 1
    if j_month > 12:
        j_month -= 12
        j_year += 1
    j_year += j_month // 12
    j_month %= 12

    # محاسبه روز و اصلاح ماه
    if j_month < 7:
        if j_month > 2:
            j_day += (j_month - 1) * 31
        else:
            j_day += (j_month - 1) * 31 - j_leap
    else:
        if j_month > 7:
            j_day += (j_month - 1) * 30
        else:
            j_day += (j_month - 1) * 30 + j_leap

    # اصلاح سال
    if j_day > 366:
        j_day -= 366
        j_year += 1
    elif j_day > 365:
        j_day -= 365

    # بازگشت تاریخ شمسی به صورت tuple
    return (j_year, j_month, j_day)

# تاریخ میلادی را به عنوان یک tuple از سال، ماه و روز وارد کنید
gregorian_date = (my,mm,md)

# تاریخ میلادی را به شمسی تبدیل کنید
jalali_date = gregorian_to_jalali(gregorian_date[0], gregorian_date[1], gregorian_date[2])

# تاریخ شمسی را چاپ کنید
print(jalali_date)
