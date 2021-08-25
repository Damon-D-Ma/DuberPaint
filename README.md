# Drawing-Program

## Description
A probably networked drawing program made with a fun fun language PyFUN (Python)

## Usage
1. Create a folder called `out` in the root directory. This is where all the exported images will go.
2. Run `/scripts/installreqs.bat` to install all requirements
3. Run `server.py` for server (or someone else's server instance), run `client.py` to connect to server.
4. Connect on port 5000

## Code Checking
Run `./scripts/checkcode.bat` on Windows to check code.

## TODO
- [X] start the code
- [X] figure out threading in Python
- [ ] Log in error handling
- [X] Handle networking protocols
- [X] Shape marking
- [X] Server Functions
- [X] Create the interface of the main screen
- [X] User input to draw things
- [X] Actual drawing program
- [X] Function to plot shapes on the board
- [X] send board info to client on join
  - [X] store board content in board class
  - [X] send each shape/brush mark to client with a bit of delay
- [ ] make entire thing functional + testing
- [ ] take camera input (if we ever manage to finish)
