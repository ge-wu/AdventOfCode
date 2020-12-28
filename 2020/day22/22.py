def read_file():
    data = []
    with open("./22.input") as file:
        for line in file:
            data.append(line.strip())
    data.remove("Player 1:")
    data.remove("Player 2:")
    data.remove('')
    return list(map(int, data))


def get_deck_value(cards):
    n = len(cards)
    return sum(cards[n - i] * i for i in range(n, 0, -1))


def game_play(p1, p2):
    while p1 and p2:
        a, b, = p1.pop(0), p2.pop(0)
        if a > b:
            p1.extend([a, b])
        else:
            p2.extend([b, a])
    return p1 if p1 else p2


def recursive_game_play(p1, p2):
    def helper(deck1, deck2):
        memo = set()
        while deck1 and deck2:
            if (tuple(deck1), tuple(deck2)) in memo:
                return 1
            memo.add((tuple(deck1), tuple(deck2)))

            a, b = deck1.pop(0), deck2.pop(0)
            if a <= len(deck1) and b <= len(deck2):
                winner = helper(deck1[:a], deck2[:b])
                if winner:
                    deck1.extend([a, b])
                else:
                    deck2.extend([b, a])
            else:
                if a > b:
                    deck1.extend([a, b])
                else:
                    deck2.extend([b, a])
        return 1 if deck1 else 0
    return p1 if helper(p1, p2) else p2


def runner():
    data = read_file()
    n = len(data)
    deck1 = list(map(int, data[:n // 2]))
    deck2 = list(map(int, data[n // 2:]))

    deck1_copy = deck1[:]
    deck2_copy = deck2[:]

    winner = game_play(deck1, deck2)
    recursive_winner = recursive_game_play(deck1_copy, deck2_copy)

    winner_val = get_deck_value(winner)
    recursive_winner_val = get_deck_value(recursive_winner)

    print("Part 1:", winner_val)
    print("Part 2:", recursive_winner_val)


if __name__ == '__main__':
    runner()
