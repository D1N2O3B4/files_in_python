file_var = open("data.txt","r")

read_contents = file_var.read()

file_var.close()

print(read_contents)

sentence = input("Type anything here:\n")

file_var = open("data.txt","w")
file_var.write(sentence)
file_var.close()