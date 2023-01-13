def run_timing():
    """Asks user to repeatedly enter minutes ran.
    Prints average time and number of runs.
    """

    number_of_runs = 0
    total_time = 0
    one_run = True
    while True:
        one_run = input("Enter 10km run time: ")
               
        number_of_runs += 1
        total_time += float(one_run)
    
    average_time = total_time / number_of_runs
    
    print(f"Average of {average_time}, over {number_of_runs} runs")

run_timing()