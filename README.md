# Lightning McQueen To-Do List

## Description

A terminal-based to-do list app themed around CARS, styled as Lightning McQueen's personal task tracker. The app greets you like Doc Hudson would greet McQueen. Calling you "Champ" throughout and helps you manage your racing (reallife) 
to-do list right from the terminal. Tasks are saved locally so your list is still there the next time you fire up the engine.

## Features

- **Add a task** - getting ready for the race
- **View your to-do list** - see tasks split into two categories: Pending and Done
- **Mark a task as completed** - move a task from Pending to Done once you've crossed the finish line on it
- **Remove a task** - take a task off the list entirely
- **Persistent storage** - tasks are automatically saved to a local "tasks.txt" file, so nothing's lost between runs
- **Color-coded terminal output** - McQueen's paint job
- **Input validation** - blank tasks and invalid menu choices are caught and rejected with a friendly reminder

## Requirements

- Python 3.x
- built entirely with the Python standard library
- A terminal that supports ANSI color codes

## How to Run

```bash
python toDoList.py
```

## Usage

On launch, you'll see a menu with the following options:

```
1 - Add a task
2 - View my to-do list
3 - Mark task as completed
4 - Remove a task
5 - Quit
```

Enter the number for the action you want, and follow the prompts.

## How Tasks Are Stored

Tasks are saved in a plain text file named "tasks.txt", created automatically next to the script. The format is simple:

- Tasks that are not done yet are written as they are one task per line
- Tasks that are done have [DONE] added at the beginning

Example "tasks.txt":
```
Get new tires before the race
[DONE] Wax the paint job
[DONE] Check oil levels
```

The file is read when the app starts and rewritten every time a task is added, completed, or removed.

## Challenges & How They Were Solved

- **Empty task submissions:** This was fixed by removing any spaces from the input and checking if the task is empty before adding it. If it is empty the user get that they cann't add a task.
- **Invalid task numbers when marking/removing tasks:** This was solved with a function called "getValidTaskNumber()". This function keeps asking for a task number until it gets an one.

