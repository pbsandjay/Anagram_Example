f = open('words.txt','r')

dictionary = {}

for line in f:
    sortWord = "".join(sorted(line.strip()))
    if not dictionary.has_key(sortWord):
        dictionary[sortWord] = [line]
    else:
        dictionary[sortWord].append(line)

while 1:
    userWD = raw_input("Please enter a word so I may search for the anagram\n")
    sortedUW = "".join(sorted(userWD))


#print sortedUW
    if dictionary.get(sortedUW) is not None:
        print "The anagram of " + userWD + " are... "
        for word in dictionary.get(sortedUW):
            print word
    else:
        print "I couldn't find an anagram of " + userWD + " womp womp"