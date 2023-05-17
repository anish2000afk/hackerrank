string = input()
int_pos, char = input().split()
int_pos = int(int_pos)
def mutate_string(string, int_pos, char):
    l = list(string)
    l[int_pos] = char
    string = ''.join(l)
    print(string)

mutate_string(string, int_pos, char)
