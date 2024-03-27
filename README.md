# Tic-Tac-Toe Game Engine with AI Opponent
![tic-tac-toe](https://github.com/JuanAKAJuan/tic-tac-toe-game-engine/assets/64856243/20acf70f-0329-4c3e-80b5-72e2643d02ea)

Make a virtual environment using the command line if your editor doesn't already
give you the option to create one.
```Shell
$ cd tic-tac-toe/
$ python3 -m venv venv/
```

Use these commands to enter the virtual environment and using the "--editable" flag,
the Python interpreter will import the functions and classes as the project is
being worked on instead of having to rebuild and install the library every time
a change is made.
```Shell
$ source venv/bin/activate
$ python3 -m pip install --editable library/
```

In order to start the game, it must be decided who is going to play. If you want
to have two people play against each other, use the following command inside of the
*frontends/* directory.
```Shell
(venv) $ python3 -m console -X human -O human
```

The -X and -O are the starting marks for each player. These can be interchanged
as long there are no duplicate marks. To change the players from humans to
computers, change the **human** to **random**. By changing both human values
to random, you can watch as two computers face each other with "random" choices.
You can also have the AI opponent play by changing one or both of the values to **minimax**.
