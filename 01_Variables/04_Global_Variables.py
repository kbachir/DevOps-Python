pass #  Only needed if empty


""" 

Global variables: 

'shadows name from somewhere else' means its not the same variable, just has the same name. 'shadowing the name'.
local_variable (within) the function not used...

put the word gloval in front of the variable name. Local variables are only in use inside my_functions, global variables 
will allow you to set a variable for the entire programme.

Big issue is that if you rename the global variable, the code may break in other places as global variables are
more entrenched. 

Scope:




"""

x = 1
y = 2

print(x, y)
#  2) here, the variables that print function will call are 1 and 2. The local scope x, y are shadows of the outside
#  of the variable.

def local_scope():

    x = 500
    y = 700

    return x, y #  3)

local_scope()
print(x, y)  # 1) x, y are not defined. Only part of local_Scope.

#  3) if you then add return x, y into the function and define the function as a variable:

print(x, y)

z = local_scope()

print(local_scope())
print(z)


# ========================================== #

def local_Scope2():

    if x == 1:
        print("YES")
        x = 6  #  You cannot change variables within my_functions, you can only reference them.

local_Scope2()