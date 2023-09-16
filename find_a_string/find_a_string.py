def count_substring(string, sub_string):
    count = 0
    for i in range(0, string):
        if sub_string in string:
            count = count + 1
    return count


count_substring("ABCDCDC", "CDC")
