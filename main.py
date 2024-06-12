import random

HEADS = "heads"
TAILS = "tails"
COIN_VALUES = [HEADS, TAILS]


def flip_coin():
    return random.choice(COIN_VALUES)


def play_martingale(*, starting_funds: int, min_bet: int, max_bet: int) -> int:
    step_to_lose = 0
    current_funds = starting_funds
    current_bet = min_bet

    while current_funds > 0:
        print("===========")
        step_to_lose += 1
        current_funds -= current_bet
        print(f"{current_funds=}, {current_bet=}")
        flipped_coin_value = flip_coin()
        if flipped_coin_value == HEADS:
            win = current_bet * 2
            current_funds += win
            current_bet = min_bet
        else:
            print("loose")
            current_bet *= 2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds
    return step_to_lose


print(play_martingale(starting_funds=100, min_bet=1, max_bet=100))

