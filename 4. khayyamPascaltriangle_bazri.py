n = int(input("Please enter the number of rows: "))
rows = [[1], [1, 1]]
for i in range(n-2):
    thisRow = [1]
    for j in range(i+1):
        thisRow.append(rows[i+1][j]+rows[i+1][j+1])
    thisRow.append(1)
    rows.append(thisRow)
rows = rows[:n]
tmp = str(rows)
output=""
for i in rows:
    thisLine=""
    for j in range(len(i)):
        thisLine+=str(int(i[j]))+" "


    output+=thisLine.center(len(str(rows[-1]))-len(rows[-1]))+"\n"

print(output)
