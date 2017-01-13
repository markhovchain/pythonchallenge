# Python Challenge Solutions

*SPOILER ALERT*: These are my solutions to the [Python Challenge](http://www.pythonchallenge.com)

## Dependencies

Most of these solutions only work with Python 3. 

Level 7 uses the pypng module:

    $ pip-3.4 install pypng
    
Level 11 and many others use the python imaging library (PIL) module: pillow:

    $ pip-3.4 install pillow
    
Level 30 uses matplotlib to visualize the data.

*NB: I have only tested this on OS X Yosemite.*

## Project Structure

The solution for each level is in file names level<number>.py. The `img` dir contains various input and output files
produced and consumed by the solutions. A few help modules are use across solutions, or containing functions that may
be useful outside this project.
  
## Solving Levels

The `solve.py` module can be used to solve one or more levels. See:

    $ python3.4 solve.py help

You can run the solution for all levels with

    $ python3.4 solve.py
    
Or solve a single level, for example level 0 with:

    $ python3.4 solve.py 0
    
Or:

     $ python3.4 level0.py    
    
Or solve range of levels with:

    $ python3.4 solve.py 0 10
    
Running the solution will prompt the user to open the next level page in the browser. When username/password are required,
they are printed to the console before prompting to open. Various output from the solutions are typically printed 
and any images that are generated are typically opened for preview.

