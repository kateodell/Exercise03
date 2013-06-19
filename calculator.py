   # No setup
   # repeat forever:
   while True:
        # read input
        problem = raw_input()
        # tokenize input
        tokens = problem.split(" ")

        # if the first token is 'q', quit
        if tokens[0] == "q":
        	
        # otherwise decide which math function to call based on the tokens we read