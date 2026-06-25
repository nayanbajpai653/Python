# String methods 
a = "!! Hello world !! Bye"
print(len(a))
print(a.upper())
print(a.lower())
print(a.strip("!")) # remove ! from string
print(a.rsplit("!")) # remove ! from end
print(a.split(" ")) # make list of each elements 
print(a.replace("Bye", "By")) # replace to new word

Heading = "this iS a heAding"
print(Heading.capitalize()) # converts frist word in upper case and all remain are become lower case

str = "This is a string"
print(len(str))
print((str.center(32)))
print(len(str.center(32)))

print(a.count('!!')) # count ! in string

str1 = "Welome to the world of Python !!!"
print(str1.endswith("!!!")) # check is string end with !
print(str1.endswith("to" , 4 , 10)) # from index 4 to index 10 check 'to' is present or not
 
str2 = "He's name is Stive. He is an awesome guy."
print(str2.find("is")) # first occurance of the word
print(str2.index("is")) # in which index it come first 

# print(str2.index("ishh")) # This will raise an error because it is not present

str3 = "Thisisastringwithalotofspaces"
print(str3.isalnum()) # gives False/True if spaces are there
str4 = "Welcome"
print(str4.isalpha()) # gives False/True if only alphabets are there

str5 = "hello world"
print(str5.islower()) #gives False/True if all characters are in lower case

str6 = "We are in 2024"
print(str6.isprintable()) #gives False/True if all characters are printable or not

str7 = "   "
print(str7.isspace()) #gives False/True if all characters are spaces

str8 = "This Is A Heading"
print(str8.istitle()) #gives False/True if all words are capitalized

str9 = "Python is a programming language"
print(str9.startswith("Python")) #gives False/True if string starts with given substring

str10 = "Python is a Interpreted language"
print(str10.swapcase()) #swaps the case of each character

str11 = "Den is a good men . Den is a good player"
print(str11.title()) #capitalizes the first letter of each word 