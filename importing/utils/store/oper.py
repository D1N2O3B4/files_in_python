from ..pear import NotFound

def read_file(file):
    with open(file,"r") as file_var:
        return file_var.read().split("\n")

def save_content(file,content):
    with open(file,"w") as file_var:
        file_var.write(content)

print(__name__)