# ap-create-task-2020
This was my AP CSP create task submission in freshman year. The key was keeping it simple and not overcomplicating it to meet the rubric. You don't get points for making something overly complex. Something simple as block code would work too, but in my case, I created a tic tac toe game against the computer. 

Here's the link to my video: https://drive.google.com/file/d/1MacDNLEYJ2W7HgWsTq64aXSz8PFuv8-k/view?usp=sharing

Here is what I wrote on the write-up below:
3 a. Provide a written response that does all three of the following: Approx. 150 words (for all subparts of 3a combined)
i. Describes the overall purpose of the program
I created a tic-tac-toe game with Python where the user plays the computer, using a dictionary to organize the game and verify wins, ties, and losses. The computer places markers randomly (with a list carrying the available spaces) to the board, and allows the user to input their marker. The board is displayed every round until the game ends with a message.

ii. Describes what functionality of the program is demonstrated in the video
The player enters a number corresponding to placements on the board as input. If the spot isn't empty, the user is prompted to try again through the terminal. The computer randomly selects an empty slot to put its counter down. Next, the program checks if there are wins/ties, and loops the program till the game ends.

iii. Describes the input and output of the program demonstrated in the video
Players enter a number corresponding to placements on the board as input, while the computer plays back with randomly selected markers, visually outputted to the terminal as a digital game board.

3 b. Capture and paste two program code segments you developed during the administration of this task that contain a list (or other collection type) being used to manage complexity in your program. Approx. 200 words (for all subparts of 3b combined, exclusive of program code) 
i. The first program code segment must show how data have been stored in the list. 

ii. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose. 


Then, provide a written response that does all three of the following: 

iii. Identifies the name of the list being used in this response 
The dictionary is “ttt_board” an eligible data collection type.

iv. Describes what the data contained in the list represent in your program 
The dictionary maps location on the board (with key-pair) to corresponding gameboard value, (empty/‘X’/‘O’) as per game plays with visual tic-tac-toe organization. The key-pair is the number that corresponds to board placement. The value-pair is what marker the placement holds, displayed to the user.

v. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list.
The dictionary allows the program to check for wins easily, with what value (empty/‘X’/‘O’) is stored where on the board through key-value pairs. The key is both the location on the board and user input, while the value-pair is used in if-statements for checking wins. The dictionary arrangement also allows the program to verify if boxes are empty, by comparing with the key of the dictionary as verification. This makes sure the program doesn't override previously placed markers. Without the dictionary, it would be hard to check if the squares lined up in tic-tac-toe win fashion. The ease of checking marker placement through pulling the key of these values, which lines up with the user input simplifies the process. There is no simpler way to verify wins without the use of dictionaries.

3 c. Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure. Approx. 200 words (for all subparts of 3c combined, exclusive of
program code)
i. The first program code segment must be a student-developed procedure that:
□ Defines the procedure’s name and return type (if necessary)
□ Contains and uses one or more parameters that have an effect
on the functionality of the procedure
□ Implements an algorithm that includes sequencing, selection,
and iteration

ii. The second program code segment must show where your student-developed procedure is being called in your program.

Then, provide a written response that does both of the following:
iii. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program
This function controls computer and user plays, checks for ties/wins, switches between turns, and displays gameboard output to the terminal. This controls how the player sends input and the computer interaction while checking for wins.

iv. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.
Since the function restarts the count increment variable every time it's called, it starts with a for loop of 10 for the 9 spaces on the board. The count variable verifies ties. This is the iteration. Depending on the first parameter, different portions of the function are triggered with if-statements, either computer-play or user-play, which matters as the user enters numerical input while the computer selects randomly from a list, the second parameter. The user-play if-statement checks to make sure the spot's empty, then validates as user turn. The computer-play if-statement pulls a random number that corresponds to key-pairs on the dictionary. From there, both lead to a series of nested if-statements due to sequencing which scans the dictionary for wins, possible due to the key-pairs. Each if-statement in this section leads to the program ending with a victory message and gameboards per step. Once exited from the nested if-statements, the turn variable is switched to the opposing player to switch turns. 


3 d. Provide a written response that does all three of the following: Approx. 200 words (for all subparts of 3d combined) 

i. Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute. 
First call: First call is place_counter('X',computer_choices).

Second call: Second call is place_counter('O',computer_choices).

ii. Describes what condition(s) is being tested by each call to the procedure 
Condition(s) tested by the first call: 
In place_counter('X',computer_choices), the program checks what is being passed for the first argument, turn, which is "X", triggering the player's turn if-statement sequence.

Condition(s) tested by the second call:
In place_counter('O',computer_choices), the program checks what is being passed for the first argument, turn, which is "O", triggering the computer's turn if-statement sequence.

iii. Identifies the result of each call 
Result of the first call: 
It's the user's turn since the first parameter was "X" and thus the program prompts for input. Using the numerical input stored as the variable move, the next nested if-statement uses move as the key pair and checks to make sure the corresponding value is empty. This means the slot's open on the board, and the user's turn is valid. The value of the key-pair is removed from the available_computer_slots list, which the computer uses for its plays. A series of if-statements check for wins and then switches.

Result of the second call:
Since it's computer's turn due to first parameter of "O", a random element of the available_computer_slots list is chosen as the turn. This correlates to the key-pair off the dictionary, and is set to equal the turn variable. The element is removed from available_computer_slots, and a series of if-statements checks wins/ties, switching to user.
