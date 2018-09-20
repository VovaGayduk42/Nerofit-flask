from flask_table import Table, Col


class Results(Table):
    id = Col('id', show=False)
    mass = Col('Вес')
    chest = Col('Грудь')
    waist = Col('Талия')
    buttock = Col('Ягодицы')
    left_hand = Col('Левая рука')
    left_bedro = Col('Левое бедро')
    left_golen = Col('Левая голень')
    right_hand = Col('Правая рука')
    right_bedro = Col('Правое бедро')
    right_golen = Col('Правая голень')