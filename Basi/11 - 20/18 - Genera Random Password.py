# Use an import statement at the top
from random import randint

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password(word_list):
    max = len(word_list)-1
    password="{}{}{}".format(word_list[randint(0,max)],word_list[randint(0,max)],word_list[randint(0,max)])
    return password

print(generate_password(word_list))
print(generate_password(word_list))

"""
SOLUZIONE UDACITY
"""


def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
#OR

def generate_password():
    return str().join(random.sample(word_list,3))
