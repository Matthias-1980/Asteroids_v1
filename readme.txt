source venv/bin/activate
is how to activate the virtual environment.
---------------------------------------------------------------------
Installation of virtual environment that is required for game to run

We are going to be using pygame and a virtual environment to develop our game.

Pygame

Pygame is a module for developing games using Python. It provides simple functions and methods for us to easily draw images within a GUI window and handle user input.

Virtual Environment (venv)

Virtual environments are Python's way to keep dependencies (e.g. the pygame module) separate from other projects on our machine. For example, we need pygame version 2 for this project, but another project on your computer might require version 1.

As a best practice, each Python project on your machine should have its own virtual environment to keep them isolated from each other.

Assignment

    Create a new directory and Git repository for this project somewhere on your computer.
    Create a virtual environment at the top level of your project directory
    Obviously if you downloaded this from Github then you do not need to do any of these steps except make the virtual environment:

python3 -m venv venv

    Activate the virtual environment:

source venv/bin/activate

You should see (venv) at the beginning of your terminal prompt, for example:

(venv) user-name@MacBook-Pro-2 asteroids %

Note: make sure that your virtual environment is activated when running the game or using the bootdev CLI.

    Create a file called requirements.txt in the top level of your project directory with the following contents:

pygame==2.6.0

This tells Python that this project requires pygame version 2.6.0.

    Install the requirements:

pip install -r requirements.txt

pip is Python's package manager. It will install the pygame module into the virtual environment you created.

    Make sure pygame is installed:

python3 -m pygame


