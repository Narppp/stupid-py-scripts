# helpful fr

import random
import sys

err_messages: list[str] = ["i think something happened idk",
                           "oh no an error occurred on line 10000000000000000000000",
                           "skill issue",
                           "i told you to check your code but you ran it again",
                           "no pain no gain"]

def dumb_err_msg(exc_type, exc_value, exc_traceback):
    output_msg: str = random.choice(err_messages);
    print(output_msg);
    sys.exit(1);

sys.excepthook = dumb_err_msg

print(sadfasdf);
