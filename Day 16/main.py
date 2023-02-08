# from turtle import Turtle, Screen
# ze = Turtle()
# ze.color("blue ")
# ze.shape("turtle")
#
# minha_tela = Screen()
# print(minha_tela.canvheight)
# minha_tela.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electrict", "Water", "Fire"])

table.align = "l"
table.border = True
table.header_style = "upper"
print(table)