# Explicit
"""
The conversion of one data type into another data type, done via developer or programer 
"""
string = "654"  
number = 45
convert = int(string)   # if a strring is not a valid integer it through a error when converting it manually  
sum = convert + number
print("total: ", sum) # converting string into integer manually

# Implicit
''' 
python converts lower data into higher data type itself  
'''
integer = 684
float = 156.5
sum = integer + float
print("Total:", sum) # converst the value into float

"""
Type Hierarchy (Low → High)
bool  →  int  →  float  →  complex
int → complex
float → complex
bool → int
bool → float
"""