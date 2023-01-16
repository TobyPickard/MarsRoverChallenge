# MarsRoverChallenge

There are two methods for running this script. 
-  Putting your grid size and inputs into the `robotInstructions.txt` file, in the correct format, and choosing option `(1)` when prompted by the script. The rest is automatic. 
-  If option `(2)` is chosen the script will continue to prompt the user for the necessarry information until the user has added all the robots that they want. i.e grid size and instructions. 

**Note** - Due to a lack of time, the script is not as robust as I would have liked, so if you add any robots to the `robotInstructions.txt` file or when choosing option `(2)` be sure to include all the spaces or the script will throw errors.<br>
Examples of the correct format include: <br>
For grid size: <br>
5 5 <<<< This is correct <br>
5,5 <<<< This will not work <br>

For robot instructions: <br>
(1, 2, N) LRFRL <<< This is correct <br>
(1,2,W) LRLR <<< This will not work

 ## What would I add next? 
- Further testing, as I only had time to add testing for afew of the functions
- I would split up afew of the functions so they could be abit more readable. I think that there is abit too much indentation in the `compute_positions` function for example
- Improving the robustness of the user inputs. Currently even a slight deviation from the perfect input will result in an error being thrown. This is not ideal. A possible way to do this would be to use regular expressions be abit more robust with how it reads the inputs.
- Add some logic to clear the terminal for each of the menus 


