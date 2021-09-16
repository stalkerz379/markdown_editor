# markdown_editor

## Stage 1: Meet the markdown!
Markdown is a special plain text formatting language that is extremely popular among developers. It is used in documents, research articles, Github README files, and other things. 

## Stage 2: How do I use it?
### Description
Let's go through it one more time and recall the basic features:

- plain — a normal text without any formatting
- **bold**/*italic* — self-explanatory
- `inline-code` — for example, `python editor.py`
- link — for example, [google.com](https://www.google.com/)
- header — look at the header of this stage.
- unordered-list — this very list is an example of an unordered list
- ordered-list — a list with enumerated elements
- new-line — switches to the next line

In this stage, you need to implement these features in your editor. Let's also add special commands to our tool:

- [x] `!help` — prints available syntax commands.
- [x] `!done` — saves the markdown and exits the app.

### Objectives
Implement the help function that will print available syntax commands, which we have indicated above, as well as the special commands. When called, it should print the following:

- [x] `Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line`
- [x] `Special commands: !help !done`
- [x] Implement the `exit` function that exits the editor without saving.
- [x] Ask a user for input:
    - [x] `Choose a formatter:`
    - [x] `!help` prints the help page, `!done` exits the editor.
- [x] If the input contains one of the correct formatters `(plain, bold, italic, etc.)`, ask for the input once again.
- [x] If the input contains no formatters or unknown command is sent, print the following message and ask for input again: `Unknown formatting type or command`

## Stage 3: Text formatting

### Objectives
- [x] Implement a separate function for each of the formatters. 
- The program should work in the following way:
    - [x] Ask a user to input a formatter.
    - [x] If the formatter doesn't exist, print the following error message: `Unknown formatting type or command`
    - [x] Ask a user to input a text that will be applied to the formatter: `Text: <user's input>`.
    - [x] Save the text with the chosen formatter applied to it and print the markdown. Each time you should print out the whole text in markdown accumulated so far.

Different formatters may require different inputs.

The new-line formatter does not require text input.

`Plain, bold, italic, and inline-code formatters` require only text input, and should **not add an extra space or line break at the end**:
>Text: > Some text

Headers require a level and text. A level is a number from 1 to 6. Don't forget to check it too: if it is out of bounds, print the corresponding error: `The level should be within the range of 1 to 6`. Also, remember that a heading automatically adds a new line in the end.

>Level: > 4

>Text: > Hello World!

Link requires a label and a URL:

>Label: > Tutorial

>URL: > https://www.markdownguide.org/basic-syntax/

## Stage 4: Ordered and unordered lists

### Objectives

Implement the ordered-list and unordered-list formatters. 

   >Number of rows: > 3
    Row #1: > First element
    Row #2: > Second element
    Row #3: > Third element

## Stage 5: Save the results

### Description

By this moment, our program can recognize some of the formatters and special commands, it can also print the results and exit. We need to implement yet another very useful feature — the ability to save the text to a file.

### Objectives
Modify your `done` function that was implemented in the second stage. Apart from exiting the program, it should save the final result of a session to a file, let's call it `output.md`. Create this file in the program directory. If it already exists, overwrite this file. The file should include the result of the last session.