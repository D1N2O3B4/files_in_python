from utils.oper import read_file,save_content

edit = save_content("importing/data/data.txt","We were on a bridge near West gate \nbut we saw you jumping into the lake \nhow did you manage the fall bro")

read = read_file("importing/data/data.txt")
print(read)