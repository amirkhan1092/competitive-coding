# 500 students

stu = 500
on_off_number = 50
mobile = [True for _ in range(stu+1)]
for i in range(1, on_off_number+1):
    for k in range(i, stu+1, i):
        mobile[i] = not mobile[k]

print('mobile still switch off ',mobile.count(False))
