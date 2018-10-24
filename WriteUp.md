Mini Project 4 Interactive Visualization

Authors: Miguel Castillo II and Bailey Wolfe

Project Overview

The main idea of our project is a piano keyboard that the user interacts with based on keyboard inputs. The minimum viable product is a few keys that are interactive but hard coded for each key value, as opposed to a list or dictionary lookup system. Once the Piano pops up press keys on your keyboard (a through m) and sounds will play and the keys will light up.

Results

Once the file is run, it initializes a piano keyboard with 16 keys.  Our keyboard plays frequencies on the Blues scale.  Using the letter keys a through m, the corresponding key on the keyboard will light up yellow and play a note.

Implementation

The Piano file contains the components of the code that starts and stops the program.  
The Model file creates all of the keys and puts them into a Piano Model, each containing relationships to one another.  This relationship is kept seperate in a list called keys.  The key class sculpts the size, shape, and color of the individual keys, while the class PianoModel calls the Key class to create the list of keys, spaced apart horizontally, effectively creating a keyboard shape.
The Piano file checks whether a key has been pressed by the user.  Once this has been detected, it calls the controller file.  In Controller, it checks which individual key, a through m, has been inputted on the user's computer keyboard.  The function also evaluates if the button being pressed by the button input has been released.  After establishing which letter was pressed, it changes the color of the corresponding key on the keyboard, using the view file.  Then, the Controller file plays a note using the blues_solo file.  Lastly, it pauses and returns to the original state.  
In View, the keys are drawn on the screen.  The keys are drawn automatically white, but if a key is pressed, it is changed to whichever color is input, in our case, yellow.  During this step, it updates the user's display.  
Blues_Solo uses Sonic Pi to output sound based on the beats per minute, number of beats, and the note number.
When figuring out how to change the colors of a specific key, we decided to use a list of the keys' positions, although, the alternative would have been to name each key and call them individually.  We implimented the list by using for loops to iterate through the list of keys to find the position of the intended key.  

Reflection

We put a lot of time into the project early on, because of intial bugs, which helped us complete the project on time.  We could improve the keyboard's queuing system, where keys cannot be played simultaniously.  I wish we would have known how much trouble Sonic Pi would give us as a program.  Much, if not most, of our time was spent debugging this program and implementing it into the code.  Sonic Pi, being the key sound module used for this program made this a hurdle we could not pass without fixing.  Eventually, we were able to get Sonic Pi working on Windows, but not on dual boot.  

We planned to work together on the entire project, instead of working individually then coming together. This stayed constant throughout the project, which was helpful in knowing what new updates were made to the program, having an equal understanding of the code, and keeping track of github pushes.  If we could do things differently, we would have picked a more enjoyable project to create.  
