data = []
for i, line in enumerate(file('birthdays.csv')):
    if i==0: continue    # skip the header
    line = line.strip()  # remove the newline
    first, last, age, weight, height, birthday = line.split(',')
    d = dict(first=first, last=last, age=int(age),
             weight=float(weight), height=float(height),
             birthday=birthday)
    data.append(d)

print(data)
