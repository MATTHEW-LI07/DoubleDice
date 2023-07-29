'''Antonia and David are playing a game.
Each player starts with 100 points.
The game uses standard six-sided dice and is played in rounds. During one round, each player
rolls one die. The player with the lower roll loses the number of points shown on the higher die. If
both players roll the same number, no points are lost by either player.
Write a program to determine the final scores.
Input Specification
The first line of input contains the integer n (1 ≤ n ≤ 15), which is the number of rounds that
will be played. On each of the next n lines, will be two integers: the roll of Antonia for that round,
followed by a space, followed by the roll of David for that round. Each roll will be an integer
between 1 and 6 (inclusive).
Output Specification
The output will consist of two lines. On the first line, output the number of points that Antonia has
after all rounds have been played. On the second line, output the number of points that David has
after all rounds have been played.'''



def play_game(rounds):
    antonia_points = 100
    david_points = 100

    for _ in range(rounds):
        antonia_roll, david_roll = map(int, input().split())

        if antonia_roll < david_roll:
            antonia_points -= david_roll
        elif antonia_roll > david_roll:
            david_points -= antonia_roll

    return antonia_points, david_points


# Read the number of rounds from input
n = int(input("Enter the number of rounds: "))

# Play the game and get the final scores
antonia_score, david_score = play_game(n)

# Print the final scores
print("Antonia's score:", antonia_score)
print("David's score:", david_score)

