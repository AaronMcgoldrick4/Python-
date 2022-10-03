word="FFEELL"

def double(word):
    for i in range(len(word)-1):
        if word[i]== word[i+1]:
            return True
        else:
            return False

print(double(word))
