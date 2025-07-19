
# TyZe - Your Personal Desktop Assistant 🤖

Welcome to TyZe, a command-line based chatbot assistant built in Python. TyZe is designed to help you with everyday tasks like opening websites, searching the web, controlling your system volume, and launching applications, all from the comfort of your terminal.

## ✨ Features

* **Personalized Greetings:** Greets you according to the time of day.

* **Tells Time & Date:** Provides the current time and date on request.

* **Web Browse:** * Opens single or multiple websites (e.g., `open google and wikipedia`).
    * Performs Google searches directly from the terminal.
    * Searches for videos on YouTube.
    * Plays YouTube videos directly.

* **Application Control:**
    * Opens local applications installed on your computer (e.g., `open chrome`).
    * Closes running applications.

* **System Control:**
    * Mutes/unmutes system volume.
    * Increases or decreases system volume.

* **Interactive Chat:** Responds to simple conversational cues like "hello", "what is your name", and "thank you".

## 🛠️ Installation & Setup

Follow these steps to set up and run TyZe on your local machine.

### Prerequisites

* [Python 3.7+](https://www.python.org/downloads/)

* An active internet connection (for downloading dependencies and for web-based features).

### Step-by-Step Guide

1.  **Clone the Repository**
    ```sh
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create a Virtual Environment (Recommended)**
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    Create a file named `requirements.txt` in the project directory and paste the following lines into it:
    ```txt
    nltk
    AppOpener
    pywhatkit
    beautifulsoup4
    requests
    keyboard
    ```
    Now, run the following command in your terminal to install all the required packages:
    ```sh
    pip install -r requirements.txt
    ```
    The script will automatically download the necessary `punkt` tokenizer from NLTK on its first run.

## 🚀 How to Run

1.  Open your terminal or command prompt.
2.  Navigate to the project directory.
3.  Run the script using the following command:
    ```sh
    python your_script_name.py
    ```
    *(Replace `your_script_name.py` with the actual name of your Python file.)*

4.  The assistant will first ask for your name to personalize the experience. After that, you can start giving it commands!

## 📝 Usage & Commands

Here is a list of commands you can use with TyZe:

| Command Category      | Example Command                               | Description                                                 |
| :-------------------- | :-------------------------------------------- | :---------------------------------------------------------- |
| **Open Website(s)** | `open google` or `open youtube and wikipedia` | Opens one or more websites in your default browser.         |
| **Google Search** | `google search history of python`             | Performs a search on Google.                                |
| **Youtube** | `Youtube funny cat videos`             | Searches for videos on YouTube.                             |
| **Play on YouTube** | `play never gonna give you up`                | Plays the first video result for the query on YouTube.      |
| **Open Application** | `open chrome` or `open notepad`               | Opens a local application installed on your computer.       |
| **Close Application** | `close chrome`                                | Closes the specified application if it's running.           |
| **System Control** | `system volume up` or `system mute`           | Controls your computer's master volume.                     |
| **Get Time/Date** | `what's the time?` or `today's date`          | Provides the current system time or date.                   |
| **Exit Assistant** | `bye`, `exit`, `quit`                         | Terminates the assistant.                                   |

### ⚠️ Important Notes

* **Administrator Privileges:** The `keyboard` library, used for system volume control, may require you to run the script with administrator or root privileges to function correctly.
    * On Windows, you can do this by opening your Command Prompt or PowerShell as an Administrator.
    * On macOS/Linux, you may need to run the script with `sudo`.
* **Application Control:** The success of opening and closing applications depends on the `AppOpener` library and can vary based on your operating system and how applications are installed.
