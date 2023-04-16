# Hacknite23-Stumble Guys
AIM-Our aim was to develop a game known as space invaders in which a person has to enter his username first,then select difficulty level and

        MAIN MENU
                1.)We have a PLay button which when pressed redirects you to a screen which displays a screen to select difficulty
                2.)We have a Rankings button which when pressed redirects you to a screen which displays the top 5 high scores in each difficulty level , 
                we do this by storing all the data into a file and reading the file when we display the high scores 
                3.)Lastly we have a Quit button which quits the game
                
        GAME
                -Depending on the difficulty selected by the user in the aforementioned screen , The difficulty level is set
                -After the difficulty has been selected the game ask for the users username which it uses to store the scores of the player. Privacy is our                     upmost concern and be rest assured that we would never sell you data to any outside third parties
                -On the top left corner of the screen the game shows your current score and the highest score for the current difficulty rating
                -On the top right corner of the screen the game shows you two buttons :
                        1.)Pause: It pauses the game and stays paused until the user presses C whereby it resumes
                        2.)Exit: It exits the game and displays a game over screen , The game over screen displays the score and if the user presses Space                            it starts a new game
                        but if the user presses Esc button it takes them to a confirm exit page . This page has option to confirm and cancel
                -After Every 10 points the speed of the enemies increase 
                -After Every 15 points there appears an slow down orb in a random location on the screen which when shot decreases the speed of the enemies
                -The player might accidently close the game  , to prevent this , After the game has loaded there is a confirm exit page which appears                           everytime  

        REQUIREMENTS
                -pygame,threading,math,random,pygame_gui,sys,pygame-menu
