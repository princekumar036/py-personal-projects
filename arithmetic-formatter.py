
def solve_problems(no1, no2, op):
    if op == "+":
        return int(no1) + int(no2)
    elif op == "-":
        return int(no1) - int(no2)

def display_problems(prob_list):
    for i in range(len(prob_list)):
        print("{:>6}".format(prob_list[i].split(" ")[0]), end="    ")
    print("")
    for i in range(len(prob_list)):
        print("{}".format(prob_list[i].split(" ")[1]), end=" ")
        print("{:>4}".format(prob_list[i].split(" ")[2]), end="    ")
    print("")
    print("------    " * len(prob_list))

def display_solutions(prob_list):
    for prob in prob_list:
        prob_elem = prob.split(" ")
        print("{:6}".format(solve_problems(prob_elem[0], prob_elem[2], prob_elem[1])),  end="    ")
        

def arithmetic_arranger(prob_list, solve=False):
    display_problems(prob_list)
    if solve == True:
        display_solutions(prob_list)

arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)