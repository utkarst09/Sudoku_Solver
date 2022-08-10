# Sudoku_Solver
Python application to solve Sudoku puzzle from an image of an unsolved puzzle and overlay solution on to real image.

The project is divided into Four parts

**Part One: Digit Classification Model**

Build and train a neural network on the Chars74K image dataset for digits. This will be further used in classifying the digits in the image.

Part Two: Detecting And Reading The Sudoku From An Image

Identify the sudoku puzzle in an image using OpenCV-library. Classify the digits in the detected sudoku puzzle using the model made in part one. Getting the values of the cells in the sudoku in for of array.

Part Three: Solving The Puzzle

The array is converted into matrix. The given puzzle is are solved using Backtracking.

Part Four: Overlaying The Solution On The Real Image

The corresponding result of the puzzle is overlayed on the input puzzle image.
