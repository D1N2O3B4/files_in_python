players = input("List your fav players lets see if they're in the omega list(p.s no spaces after \",\"):\n").split(',')

read_random = open("files_in_python/random.txt","r")

random_content = [i.strip() for i in read_random.readlines()]

read_random.close()

"""Changing to sets for intersection"""
intersect = set(players).intersection(set(random_content))

"""Writing into Similarities"""
write = open("files_in_python/similarites.txt","w")

for i in intersect:
    print(f"We both know {i}")
    write.write(i+"\n")

write.close()