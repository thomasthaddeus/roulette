"""Betting strategies for Roulette and plots associated with the strategies"""

import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc={"figure.figsize": (11.7, 8.27)})


def main():
    """Main function"""
    bankroll = 100
    always_red(bankroll)
    print(plot_table1())
    martingale(bankroll)
    fibonacci_strategy(bankroll)
    print(plot_table2())
    print(plot_table3())


def always_red(bankroll):
    """Returns the strategy for betting red every time"""
    bankroll = 100
    pockets = ["Red"] * 18 + ["Black"] * 18 + ["Green"] * 2
    bankroll_history = []
    while bankroll > 0:
        roll = random.choice(pockets)
        if roll == "Red":
            bankroll += 1
        else:
            bankroll -= 1
        bankroll_history.append(bankroll)
    return bankroll_history


def martingale(bankroll):
    """Returns the strategy for using martingale in Roulette every time"""
    bet = 0.01
    pockets = ["Red"] * 18 + ["Black"] * 18 + ["Green"] * 2
    bankroll_history = []
    while bankroll > 0:
        if bet > bankroll:
            bet = bankroll
        roll = random.choice(pockets)
        if roll == "Red":
            bankroll += bet
            bet = 0.01
        else:
            bankroll -= bet
            bet *= 2
        bankroll_history.append(bankroll)
    return bankroll_history


def fibonacci(num):
    """Returns the fibonacci sequence"""
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def fibonacci_strategy(bankroll):
    """Returns the fibonacci sequence as an algorithm"""
    fibonacci_number = 1
    pockets = ["Red"] * 18 + ["Black"] * 18 + ["Green"] * 2
    bankroll_history = []
    while bankroll > 0:
        bet = fibonacci(fibonacci_number) * 0.01
        if bet > bankroll:
            bet = bankroll
        roll = random.choice(pockets)
        if roll == "Red":
            bankroll += bet
            fibonacci_number = max(fibonacci_number - 2, 1)
        else:
            bankroll -= bet
            fibonacci_number += 1
        bankroll_history.append(bankroll)
    return bankroll_history


def plot_table1():
    """Plots the results of the algorithm."""
    for i in range(4):
        plt.plot(always_red(bankroll=100), linewidth=2)

    plt.xlabel("Number of Games", fontsize=18, fontweight="bold")
    plt.ylabel("Bankroll", fontsize=18, fontweight="bold")
    plt.xticks(fontsize=16, fontweight="bold")
    plt.yticks(fontsize=16, fontweight="bold")
    plt.title("Bankroll Over Time", fontsize=22, fontweight="bold")


def plot_table2():
    """Plots the results of the marting algorithm."""
    for i in range(4):
        plt.plot(martingale(bankroll=100), linewidth=2)

    plt.xlabel("Number of Games", fontsize=18, fontweight="bold")
    plt.ylabel("Bankroll", fontsize=18, fontweight="bold")
    plt.xticks(fontsize=16, fontweight="bold")
    plt.yticks(fontsize=16, fontweight="bold")
    plt.title("Bankroll Over Time", fontsize=22, fontweight="bold")


def plot_table3():
    """Plots the results of the fibonacci_number"""
    for i in range(4):
        plt.plot(fibonacci_strategy(bankroll=100), linewidth=2)

    plt.xlabel("Number of Games", fontsize=18, fontweight="bold")
    plt.ylabel("Bankroll", fontsize=18, fontweight="bold")
    plt.xticks(fontsize=16, fontweight="bold")
    plt.yticks(fontsize=16, fontweight="bold")
    plt.title("Bankroll Over Time", fontsize=22, fontweight="bold")


if __name__ == "__main__":
    main()
