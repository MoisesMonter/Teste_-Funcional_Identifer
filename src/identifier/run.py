# from identifier import Identifier
from fake import *
if __name__ == "__main__":
    x="ola123"
    info = Identifier(x)

    if info.is_string():
        print("o valor: ",x," é uma string")
    else:
        print("o valor: ",x," nõa é uma string")