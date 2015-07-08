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


## Solving Levels

You can run the solution for all levels with

    $ python3.4 solve.py
    
Or solve a single level, with:

    $ python3.4 solve.py 0
    
Or solve range or levels with:

    $ python3.4 solve.py 0 10
    
Running the solution will prompt to open the next level page in the browser. When username/password are required,
they are printed to the console before prompting to open. Various output from the solutions are typically printed 
and any images that are generated are typically opened for preview.

