# 🔐 System Unlock and Reset Script

Welcome to the **System Unlock and Reset Script**, a simple yet effective Python script that lets you create a personal lock for your system. With customizable security questions and an easy reset process, this script is your go-to solution for basic system security.

## 🌟 Features

- **Custom Lock Creation**: Set your own Birthday Date, Pet Name, and Favorite Color as your security keys.
- **Unlock System**: Access your system by answering a series of prompts.
- **Reset Mechanism**: Forgot your keys? Reset the system using a custom security question.

## 🛠️ Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- No additional libraries needed.

### 🚀 Running the Script

1. **Save the script** as `system_unlock.py` (or any name you like).
2. **Open your terminal/command prompt**.
3. **Navigate to the directory** where your script is saved.
4. **Run the script** with the following command:

    ```bash
    python system_unlock.py
    ```

## 📜 Script Overview

The script guides you through a series of user inputs to set up a personal lock and provides a reset option if needed.

### 🎯 Key Components

#### User Prompts

- **Initial Setup**: 
  - Enter your **Birthday Date**, **Pet Name**, and **Favorite Color** to create your lock.
  
- **Unlock Process**:
  - Unlock the system by answering the security prompts. Start with your Birthday Date, followed by your Pet Name and Favorite Color if needed.

#### Reset Functionality

- **System Reset**:
  - If you fail to unlock the system, answer your custom security question to reset it.
  - A correct answer resets the system successfully; otherwise, you’ll be prompted to try again.

## 👀 Example Usage

Here's a glimpse of how the script works:

```python
Welcome! 
To your system 
Create your lock- 
Kindly feed the answer:-
What is your Birthday_Date ? 
Enter: 12-12-2000

What is your Pet Name ? 
Enter: Fluffy

What is your Favourite Color ? 
Enter: Blue

Now, please feed reset system Question-Answer:- 
Enter Question: What is your mother's maiden name?
Enter Answer: Smith

Welcome to your system 
Unlock the system! 
What is your Birthday_Date ? 
Enter: 12-12-2000
# Output: correct \n opened successfully
