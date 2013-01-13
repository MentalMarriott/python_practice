from sys import argv

script, words = argv

#pass letters from word and convert with one space added
def to_morse(letter):
	return{
		'a' : ".-",
	        'b' : "-...",
		'c' : "-.-.",
		'd' : "-..",
		'e' : ".",
		'f' : "..-",
		'g' : "--.",
		'h' : "....",
		'i' : "..",
		'j' : ".---",
		'k' : "-.-",
		'l' : ".-..",
		'm' : "--",
		'n' : "-.",
		'o' : "---",
		'p' : ".--.",
		'q' : "--.-",
		'r' : ".-.",
		's' : "...",
		't' : "-",
		'u' : "..-",
		'v' : "...-",
		'w' : ".--",
		'x' : "-..-",
		'y' : "-.--",
		'z' : "--..",
		'1' : ".----",
		'2' : "..---",
		'3' : "...--",
		'4' : "....-",
		'5' : ".....",
		'6' : "-....",
		'7' : "--...",
		'8' : "---..",
		'9' : "----.",
		'0' : "-----",
		'_' : "_",
	}[letter]
	#print "%c" % letter

print "The words you entered was %s\n" % words

print "This in morse code is: "

word_letter_list = list(words)

for letter in word_letter_list:
	print to_morse(letter) + " = %c " %letter

