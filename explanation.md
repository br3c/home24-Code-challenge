# How I solved the task

I used the argparse module to define command-line arguments, which the user can use to define the height of the tree and whether it should have a star drawn on top of it.

To get the alignment right, the program calculates the widest layer of the tree.

This "offset" is later used to center all layers of the tree.

If the user runs the code with the star-flag, a star will be printed out first, otherwise the programm proceeds with the next step.

Next, a for-loop will run for each layer of the tree and increments each layer by 2 "leafs". (the amount of layers is determinated by the height of the tree)

In the end, the stem will be printed out, aligned to the middle of the tree.