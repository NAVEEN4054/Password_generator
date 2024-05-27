# Password Generator

## Introduction

Welcome to the Password Generator! This command-line tool helps you create secure and random passwords of specified lengths. With options to include uppercase letters, lowercase letters, digits, and special characters, you can ensure your passwords are both strong and unique.

## Features

- **Custom Lengths**: Generate passwords of specified lengths.
- **Character Variety**: Include uppercase letters, lowercase letters, digits, and special characters.
- **Randomness**: Each password is randomly generated and shuffled for maximum security.
- **Multiple Passwords**: Generate multiple passwords in a single run.

## Getting Started

### Prerequisites

- Python 3.x

### How to Use

1. **Download the Script**: Save the following code to a file named `password_generator.py`.

2. **Run the Script**: Open your terminal or command prompt, navigate to the directory containing the script, and run:

    ```bash
    python password_generator.py
    ```

3. **Follow the Prompts**: Enter the required information when prompted.

### Example Session

1. **Minimum Length Requirement**: The script ensures that each password is at least 3 characters long.

    ```plaintext
    Minimum length of password should be 3
    ```

2. **Number of Passwords**: Enter how many passwords you want to generate.

    ```plaintext
    How many passwords do you want to generate? 3
    ```

3. **Password Lengths**: Specify the length of each password. If the length is less than 3, a warning will be displayed.

    ```plaintext
    Enter the length of password #1: 8
    Enter the length of password #2: 5
    Enter the length of password #3: 2
    ```

4. **Generated Passwords**: The script generates and displays the passwords.

    ```plaintext
    password #1 = h@6P%vN2
    password #2 = a9Z@w
    spooky choice! length of password #3 is less than minimum length
    ```

## Code Explanation

### Imports and Constants

The script imports the `random` module and defines character sets for uppercase, lowercase, digits, and special characters.

### Password Generation Function

The add_upper function generates the required passwords. It uses nested loops to create each password character by character, shuffles the characters to enhance randomness, and then stores the results.

### User Input and Execution

The script prompts the user for the number of passwords and their lengths. It ensures that each password meets the minimum length requirement.

## Contributions

If you have suggestions for improvements or find any issues, please feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
