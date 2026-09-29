# Getting Started

This repository contains the basic structure for your Games That Teach project.

Your first goal is not to build the whole game. Instead, it is to get a basic version running with multiple game screens.

## 1. Explore the Starter Files

### `main.py`
Controls the overall flow of the program and keeps track of the current game state.

### `settings.py`
Stores constants used throughout the game, such as screen size and frame rate.

### `start_screen.py`
Contains the functions for the start screen.

### `game_screen.py`
Contains the functions for the main gameplay screen.

### `game_over_screen.py`
Contains the functions for the end-of-game screen.

### `assets/`
Stores images, sounds, and other game resources.

### `planning/`
Contains a PDF of your project plan.

---

## 2. Run the Starter Game


### Set up the Virtual Environment
Run the following commands in a terminal window. This sets up a virtual environment that pulls in the packages you need and will ensure that your environment is good to go without having to worry about installing packages system-wide.

### Windows
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Mac / Linux
```
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
```

## Run
### In VS Code
Push the **run** button to run the game in VS Code.

### In a Web browser
At the terminal type `pygbag .` (make sure to include the dot) It should give you a URL to click. It is usually [http://localhost:8000](http://localhost:8000)


## 3. Create GitHub Issues for Features
Spend some time creating GitHub Issues for features that will get you to a finished product. While features could be art work **make sure to include some code with it as well**. You are all responsible for coding in addition to creating artwork. 

Use the following markdown template for issues. For the branch terminology, use groups like `core`, `feature`, `fix`.

```
## 1. Finish start screen
### Branch: `core/start-screen`
- [ ] Background is completely black
- [ ] Game logo correctly renders
- [ ] Instructions render in white and are centered in middle of screen
- [ ] Game stays on start screen until **SPACE** key is pressed
- [ ] Pressing the **SPACE** key takes the game to the playing mode
```

## 4. Turn on Branch Protection for `main`
Right now, anyone can merge in a pull request. Branch protection will prevent PRs from being merged without review.

1. Go to Settings, Branches, Add branch ruleset
2. Name the ruleset `PR Review Required for main`.
3. Change enforcement status to `Active`.
4. Leave Bypass list blank
5. Under target branches, click Add target, Include by pattern. Type `main`.
6. Under Branch rules, check `Restrict deletions`, `Require a pull request before merging` (set required approvals to 1), `Require approval of the most recent reviewable push`, `Require conversation resolution before merging`, and `Block force pushes`. 
7. Click Create

## 5. Implement Features
To implement a feature:
1. Create a branch following the branch name in the GitHub Issue.
2. In VS Code switch to the new branch.
3. Implement the code and test it thoroughly to ensure it works.
4. Commit and push your code to the branch.
5. Create a Pull Request (PR) that is formatted like the following:
```
Closes #X 

Added xxxx. Tested locally and with pygbag.
```
X refers to the issue number it closes, and it will auto-close the issue when it is merged.

6. Ask someone else to review your PR and merge it into the `main` branch. Delete the branch when finished.
