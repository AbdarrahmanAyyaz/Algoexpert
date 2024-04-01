# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def tournamentWinner(competitions, results):
    # Write your code here.

    # teams are facing off each other
    # only two teams face each other at one time
    # no ties and there is always a winner
    # need to write a function that will return the winner of the tournament
    # Write your code here.

    winners = []

    for i in range(len(competitions)):

        if results[i] == 0:
            winners.append(competitions[i][1])

        else:
            winners.append(competitions[i][0])

    final_winner = max(set(winners), key=winners.count)

    return final_winner
    # added winners to a set to ensure no duplicates
    # checking the count to see which team won

# if i had more time i will look more into in to dictionaries and use those

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
