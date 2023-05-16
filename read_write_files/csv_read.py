with open("files_in_python/csv_data.txt","r") as read:
    read_content = read.readlines()

read_content = [i.strip() for i in read_content[1:]]

for i in read_content:
    i = i.split(",")
    print(i)
    name = i[0]
    age = i[1]
    school = i[2]
    course = i[3]
    print(f"{name} is a {age} year old student from {school} studying {course}")
