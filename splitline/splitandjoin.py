def split_and_join(line):
    newline = line.split(" ")
    print(newline)
    newline = '-'.join(newline)
    return print(newline)

string = 'This is a new line'
split_and_join(string)
