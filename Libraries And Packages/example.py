import datetime

r"""
This script creates an empty file.
"""


filename=datetime.datetime.now()

#create empty file
def create_file():
    """ This Function Creates an empty File """
    with open(filename.strftime("%Y-%m-%d-%H-%M")+ "w") as file:
        file.write("") #writing empty string
