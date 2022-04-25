global_variable = "I am a Global variable"

def check_if_its_global_or_not():
    global global_variable
    global_variable = "NO, you're not a Global variable"
    print(global_variable)

print(global_variable) 

check_if_its_global_or_not()