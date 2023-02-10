# 퍼펙트 셔플
from sys import stdin
stdin = open("input_3499.txt")
input = stdin.readline

def perfect_shuffle(ls, num_cards):
    half = (num_cards + 1) // 2
    ls[::2], ls[1::2] = ls[:half], ls[half:]
    return ls

for i in range(int(input())):
    num_cards = int(input())
    deck = input().split()
    print(f"#{i + 1}", *perfect_shuffle(deck, num_cards))