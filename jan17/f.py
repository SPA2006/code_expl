# common counter
total = 0


def move(player, number):
    global total
    if player == "Петя":
        total += number
    elif player == "Ваня":
        total -= number


def game_over():
    if total > 0:
        return "Петя"
    elif total < 0:
        return "Ваня"
    else:
        return "Ничья"
