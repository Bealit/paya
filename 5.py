def G_to_J(gy,gm, gd):
    #see if the year is leap or not and assign the mounth length
    if gy % 4 == 0:
        g_m_d = [31,31,31,31,31,31,30,30,30,30,30,30]
    else:
        g_m_d = [31,31,31,31,31,31,30,30,30,30,30,29]
    #mounth length in Jalali
    #days from the start of the calender (gregorian)
    days_from_start_g = gd + sum([g_m_d[i] for i in range(gm-1)]) + gy*365 + gy//4 - (gy//100) + (gy//400)
    #days from the start of the calender (jalali)
    days_from_start_j = days_from_start_g + 226894
    jy,jm,jd = 0,1,0
    # find years
    while days_from_start_j >= 365:
        days_from_start_j -= 365
        jy += 1
        if jy % 400 == 0 or (jy % 100 != 0 and jy % 4 == 0):
            days_from_start_j -= 1
    if jy % 400 == 0 or (jy % 100 != 0 and jy % 4 == 0):
        j_m_d = [31,29,31,30,31,30,31,31,30,31,30,31,0]
    else:
        j_m_d = [31,28,31,30,31,30,31,31,30,31,30,31,0]
    #find mounth
    for m in range(12): #simulating Do While
        if j_m_d[m] > days_from_start_j:
            break
        days_from_start_j -= j_m_d[jm]
        jm+=1
    jd = days_from_start_j 
    
    return jy,jm,jd

print(G_to_J(*map(int,input().split('/'))))



        
    