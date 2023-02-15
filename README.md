# cs-111-Mastermind
An honest attempt turn the boardgame Mastermind into an interactive python game with (limited) graphics

### Instructions for the Game:

If you choose to be codebreaker, you will have 10 chances to guess the masterlist the computer has chosen.
This list will contain four colors chosen out of the following: ["red", "blue", "yellow", "green", "magenta", "cyan"]

For each color you guess correctly but in the wrong position, you will receive a white feedback.

For each color you guess in the correct position, you will receive a black feedback.

The feedback will be presented in a random order.

If you choose to be mastermind, you will input four colors from ["red", "blue", "yellow", "green", "magenta", "cyan"] and the computer will have 10 chances to guess correctly.

After each guess, give the computer feedback according to the same rules as above in a comma separated list.

Only give feedback for correct colors.

For example: "white, white, black" would be three correct colors with one in the right position.

