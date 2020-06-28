from collections import Counter
#Counter with lists
lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
Counter(lst)
print("Counter list.....",Counter(lst))
	
#Counter with strings
Counter('aabsbsbsbhshhbbsbs')
print("Counter list.....",Counter('aabsbsbsbhshhbbsbs'))

#Counter with words in a sentence
s = 'How many times does each word show up in this sentence word times each each word'
words = s.split()
Counter(words)
print("Words List.....",Counter(words))


# Methods with Counter()
c = Counter(words)
c.most_common(2)
print("Common List.....",c.most_common(4))

