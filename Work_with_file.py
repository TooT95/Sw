
def open_files_command():
    f = open("command.txt","r")
    string = f.read()
    f.close()
    return string

def write_in_command(string):
    f = open("command.txt","w")
    f.write(string)
    f.close()