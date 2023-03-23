punctuationmarks = [".", ",", ":", ";", "(", ")", '“', "”", "’", "-", "—", "?", "!", "…", "*", "[", "]", "$"]
infile = open("Week2\greatgatsby.txt", encoding="utf-8")
outfile = open("Week2\gatsbyOut.txt", "w")
words_dictionary = {}
word_count = 0


for line in infile:
    longest_word = ""

    line = line.rstrip().lower()
    
    for mark in punctuationmarks:
        line = line.replace(mark, "")
    #print(line)

    words = line.split()
    #print(words)
    
    for word in words:
        #print(word)

        if len(word) > len(longest_word):
            longest_word = word

        if word in words_dictionary:
            words_dictionary[word] += 1
        else:
            words_dictionary[word] = 1
    print(words)

           
    
    print("Longest word is : " + longest_word)
    print(word, file=outfile)

infile.close()
outfile.close()

print(words_dictionary)

for entry in sorted(words_dictionary, key=words_dictionary.get, reverse=True):
   print(f"{entry} : {words_dictionary[entry]}")