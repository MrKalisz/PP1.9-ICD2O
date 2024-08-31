# Lesson plan
  
methods to teach:

lower()
upper()

len(value)
var.index(value)

splicing
var[start:end]

Example Lesson:

'''
	Lesson: String Manipulation
	Author: Mr. Kalisz
	Date Created: September 24, 2021
	Date Last Modified: February 22, 2021
'''

#Functions

#A procedure that returns one thing
#Examples: print(value), input(prompt)

#Always defined by the fact that they have brackets after their name
#They are built in to the programming language (you don't have to define them yourself)

#Method - A procedure associated with an object that returns one thing

#lower()
#upper()
#index()
#len()
#splicing

#var means variable
#var.lower() - take a string and return a copy of the string with all lowercase letters

#Method

word = "Hello World"
lowerWord = word.lower() #does not replace the original

print(word) #print("Hello World")
print(lowerWord) #print("hello world")


#var means variable
#var.upper() - take a string and return a copy of the string with all UPPERCASE letters

#Method

word = "Hello World 123"
upperWord = word.upper() #does not replace the original

print(word) #print("Hello World")
print(upperWord) #print("HELLO WORLD")

#Both are very useful for comparing to input and ignoring their casing (upper or lower case)

#var.index(subString)
#Return the first index(location) of the subString inside the variable string

#Method

word = "spaghetti"
index = word.index("e")
#index = word.index("t") #first occurance
#index = word.index("spa") #first index of match
#index = word.index("z") #error if the value doesn't exist
print(index)

#indexes always start at 0

#spaghetti
#012345678

#len(value) - return the length of the value

#Function

length = len(word)
print(length)

#Splicing

#Uses the indexes of the string to create copy of the original string as a new substring

#stringVar[startingIndex: endingIndex]

#startingIndex is included in the new word (inclusive)
#endingIndex is not included in the new word (exclusive)

word = "Hello World"

#Hello World
#012345678910

#newWord = word[3:8]
#lo Wo
#newWord = word[3:11]
#lo World
#newWord = word[3:50] #Any index past the last one will go to the end of the word
#newWord = word[4:] #Goes from the startingIndex to the end of the word
#o World
#newWord = word[:5]
#Hello
#newWord = word[2:-1] #llo Worl
#Negative Numbers count backward from the end of the world
#-1 is the last letter, -2 is the second last letter, etc
#newWord = word[5:5] #Nothing (endingIndex is excluded) -> empty string
newWord = word[-3:5] #if the start point overlaps the ending point it returns an empty string
print(word)
print(newWord)