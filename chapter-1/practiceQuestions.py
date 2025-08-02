# Practice Questions

# 1. Which of the following are operators, and which are values?
# * -> operator
# 'hello' -> value
# -88.8 -> value
# - -> operator
# / -> operator
# + -> operator
# 5 -> value

# 2. Which of the following is a variable, and which is a string?
# spam -> variable
# 'spam' -> string

# 3. Name three data types. -> string,boolean,integer

# 4. What is an expression made up of? What do all expressions do? 
# -> expressions are made up of operator and operands (values and operators). They do arithmetic operation, and many more

# 5. This chapter introduced assignment statements, like spam = 10. What is
# the difference between an expression and a statement?
# -> expression perform an task like arithmetic problem (2+3,2*5) and statement defines that this variable having this value (a = 2)

# 6. What does the variable bacon contain after the following code runs?
# bacon = 20
# bacon + 1
# -> bacon will be 21

# 7. What should the following two expressions evaluate to?
# 'spam' + 'spamspam'
# 'spam' * 3
# -> the following expressions evaluate like:- 1) spamspamspam , 2) spamspamspam

# 8. Why is eggs a valid variable name while 100 is invalid?
# ->  because the variables should not be start from numeric value

# 9. What three functions can be used to get the integer, floating-point
# number, or string version of a value?
# -> int(), float() and str() is used to get the integer, floating-point
# number, or string version of a value

# 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'
# -> Because 99 is integer and integer is not be able to concat with string therefor this expression throw an error.
# -> To fix this error we have to wrap 99 into str() function to convert the integer into string like:- 'I have eaten ' + str(99) + ' burritos.'