f = open("twain.txt")
filetext = f.read().lower()

counts = dict()

for i in range(len(filetext) - 1):
    # find the pair; convert to tuple so we can use it as a dictionary key
    if ord(filetext[i]) >= 97 and ord(filetext[i]) <= 122:
        char = filetext[i]
    
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

alph_keys = sorted(counts.keys())
for char in alph_keys:
    count = counts[char]
    if count > 1: # only print characters that occur more than once
        print ' '.join(char) + ": " + str(count)
