def count(word,letter):

    count = 0
    for search in word:
        if search == letter:
        	count = count + 1
    print count

fruit="banana"
letter="1"

count(fruit,letter)