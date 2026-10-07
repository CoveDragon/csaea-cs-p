#KEY CONCEPTS: math operators: +, -, *, /, //, %, **

add = 743543 + 24
print("Sum:", add)

subtract = 43 - 4
print("Difference:", subtract)

multiply = 7 * 2
print("Product:", multiply)

float_divide = 10 / 3
print("Float division:", float_divide)

integer_divide = 7//2
print("integer_division", integer_divide)

mod = 7 % 2
print("Modulus: ", mod)

exponent = 7 ** 2
print("Exponent:", exponent)

# PEMDAS (parentheses, exponents, multiplication, division, addition, subtraction)

result1 = 2 + 3 * 4 
print("Result 1:", result1)

result2 = 2 ** 3 * 4
print("Result 2:", result2)

result3 = 5 + 2 ** 3 * (4 - 1)
print("Result 3:", result3)

# Challenge 1: Rectangle Area  
# Calculate the area of a rectangle with a width of 8 and a height of 5. 

Width = 5
Height = 8 
Result = Width * Height
print(Result)

# Challenge 2: Circle Area  
# Use the formula πr² to calculate the area of a circle with radius 7. 
# (Use 3.14 for π.)  

Pi = 3.14
Radius = 7
Result = Pi * Radius ** 2
print(Result)

# Challenge 3: Shopping Total  
# A book costs $12.99 and a notebook costs $3.50.  
# Calculate the total cost for 3 books and 4 notebooks.  
# Print the result in this format: 
#     Book: <$ cost of book>
#     Notebook: <$ cost of notebook>
#     Total: <$>

Book = 12.99
Notebook = 3.50
BookNumber = 3
NoteBookNumber = 4
BookPrice = Book * BookNumber
NotebookPrice = Notebook * 4

Total = (BookNumber * Book) + (NoteBookNumber * Notebook)
print(f"\t\tRECIPT:\n\n/////////////////////////////////////\n\tBook: ${Book}*{BookNumber} = ${BookPrice}\n\n\tNotebook: $${Notebook}*{NoteBookNumber} = ${NotebookPrice}\n\n\tTotal: ${Total}")

# Challenge 4: Even or Odd  
# Use the modulus operator to check if the number 57 is even or odd. 
# Bonus: use a conditional to print "Even" if it is even, and "Odd" if it is odd.

Number = 57
IsEven = 57 % 2
print()

if IsEven == 0:
    print(Number, "is Even!")
else:
    print(Number, "is Odd!")