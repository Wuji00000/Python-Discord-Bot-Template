🤖Python - AI Powered Discord Bot Template

A modern, modular Discord bot template built with `discord.py` This project serves as a robust starting point for creating intelligent and interactive Discord bots.

## 🌟 Features

* **🧠 AI Chat:** Natural conversation capabilities using ai(`/Talk`).
* **🛡️ Moderation:** Essential moderation tools (`/kick`, `/ban`).
* **🛠️ Utilities:** Bulk message deletion (`/delete_message`) and latency check (`/ms_test`).
* **⚙️ Modular Architecture:** Built using Discord's Cog system for easy scalability.

## 🚀 Installation

### 1. Clone the Repository
Open your terminal and run the following command to download the project:
```bash
git clone [https://github.com/Wuji00000/Python-Discord-Bot-Template.git](https://github.com/Wuji00000/Python-Discord-Bot-Template.git)
cd Python-Discord-Bot-Template
2. Install Dependencies
Install the required Python libraries using pip:

Bash

pip install -r requirements.txt
3. Configuration
Rename the .env.example file to .env.

Open the .env file and paste your credentials:

DISCORD_TOKEN: Get it from the Discord Developer Portal.

GEMINI_API_KEY: Get it from Google AI Studio.

4. Run the Bot
Start the bot with the following command:

Bash

python main.py
📂 Project Structure
main.py: The entry point. Handles extension loading and global command syncing.

commands/: Contains all bot modules (Cogs).

gemini.py: AI integration logic.

mod.py: Moderation commands (Kick, Ban).

general.py: System status and ping.

clear.py: Utility commands.

🤝 Contributing
Feel free to fork this project, submit pull requests, or open issues if you find any bugs.

Created by Wuji00000
