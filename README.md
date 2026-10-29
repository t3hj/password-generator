# 🔐 Password Generator

A simple and customizable password generator with a graphical user interface (GUI) built using Python and `tkinter`. This application allows users to generate secure passwords based on selected criteria, save them to a file, and set expiration reminders.

## ✨ Features

- 🔑 Generate passwords with customizable length and character types (letters, digits, punctuation).
- ⚙️ Dynamic fields for minimum character counts.
- 📊 Password strength indicator.
- 📋 Copy generated passwords to clipboard.
- 💾 Save generated passwords to a file with timestamps.
- ⏰ Set expiration reminders for passwords.

## 📦 Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/t3hj/password-generator.git
    cd password-generator
    ```

2. **Create a virtual environment (optional but recommended):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## 🚀 Usage

1. **Run the application:**
    ```sh
    python main.py
    ```

2. **Use the GUI to generate passwords:**
    - Enter the desired password length.
    - Select the character types to include (letters, digits, punctuation).
    - Specify minimum counts for each character type if needed.
    - Click "Generate Password" to create a password.
    - Use the "Copy to Clipboard" button to copy the password.
    - Use the "Save Password" button to save the password to a file.

## 📂 Directory Structure

```
password-generator/
│
├── main.py
├── password_generator/
│   ├── __init__.py
│   ├── generate_password.py
│   ├── save_password.py
│   └── expiration_reminder.py
├── requirements.txt
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🙏 Acknowledgements

- Inspired by various password generator tools and tutorials.
- Built with Python and `tkinter`.


## Browser demo

Hosted demo: https://t3hj.github.io/portfolio-website/demos/password-generator/

The `web/` directory contains a browser adaptation of this desktop project. The original implementation remains unchanged. This demo focuses on the core interactive features; it does not run the Python/Java desktop runtime.

Serve `web/` with a static web server for local preview. The hosted copy is deployed through the portfolio's existing GitHub Pages site; enabling Pages on this repository is optional.

