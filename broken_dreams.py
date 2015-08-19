#broken_dreams.py

import argparse
import random
import sys

def get_ideas(n, ideas):
    
    chosen_ideas = random.sample(ideas, n)
    random.shuffle(chosen_ideas)
    return chosen_ideas
	    

if __name__ == "__main__":   
   
    parser = argparse.ArgumentParser(description='Get ideas from the Wastebasket of Broken Dreams')
    parser.add_argument('-n', '--number', type=int, default=2, 
                        help="Number of ideas to return." )
    parser.add_argument('-f', '--file', default="ideas.txt",
                        help="File of ideas to put into the basket.") 
    args = parser.parse_args() 

    ideas = []
    with open(args.file) as fd:
        for line in fd:
            ideas.append(line.strip().lstrip())

    if len(ideas) < args.number:
        msg = "Not enough ideas in the waste basket."
    else:
        items = get_ideas(args.number, ideas)
        msg = """
Your ideas from the wastebasket of broken dreams are:
%s.
Ready. Set. ART!
""" % (', '.join(items))

    raw_input(msg + "(Push Enter to Close)")

