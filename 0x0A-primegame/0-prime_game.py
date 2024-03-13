#!/usr/bin/python3
"""
Prime Game
"""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    if max(nums) > 10000 or x > 10000:
        return None

    def play_game(n):
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        turn = 0
        while primes:
            if turn == 0:
                choice = max(primes)
            else:
                choice = min(primes)
            primes = [p for p in primes if p % choice != 0]
            turn = 1 - turn
        return turn

    maria_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == 0:
            maria_wins += 1
    if maria_wins == len(nums):
        return "Maria"
    elif maria_wins > len(nums):
        return "Maria"
    elif maria_wins < len(nums):
        return "Ben"
    else:
        return None
