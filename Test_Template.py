correct =0
wrong = 0
is_funcs = False # Prevent test_func from printing result after single test when testing multiple functions

def show_test(func_str, result, expect):
    output = ""
    result = str(result)
    expect = str(expect)
    if expect == result:
        output +=  "True --> "
        global correct
        correct += 1
    else:
        output += "False *** "
        global wrong
        wrong += 1 
    output += "Ran {}: {} | expects {}".format(func_str, result, expect)
    print(output)

def show_run_func(func_str):
    print("    Ran " + str(func_str) )

def show_result():
    output = "Correct: {}, Wrong: {}, Total: {}".format(correct, wrong, correct+wrong)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(output)
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

def test_funcs(lst_of_funcs):
    global correct, wrong, is_funcs
    correct, wrong, is_funcs = 0,0, True
    for func in lst_of_funcs:
        print(func)
        func()
        print("")
    show_result()
    is_funcs = False

def test_func(func, form):
    if is_funcs == False:
        global correct, wrong
        correct, wrong = 0,0
    try:
        func(form)
    except TypeError:
        func()
    print('')
    if is_funcs == False:
        show_result()

def test_decorator(func):
    return lambda form='grid' : test_func(func, form)