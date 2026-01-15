<div align="center">
  
  ![License](https://img.shields.io/github/license/[KULLANICI_ADIN]/[REPO_ADIN]?style=for-the-badge&color=blue)
  ![Python](https://img.shields.io/badge/Python-3.10%2B-yellow?style=for-the-badge&logo=python&logoColor=white)
  ![Discord.py](https://img.shields.io/badge/Discord.py-2.0%2B-5865F2?style=for-the-badge&logo=discord&logoColor=white)
  ![AI Powered](https://img.shields.io/badge/AI-Groq%20%2F%20Llama%203-orange?style=for-the-badge&logo=openai&logoColor=white)
  ![Maintenance](https://img.shields.io/badge/Maintained-Yes-green?style=for-the-badge)
  ![OS](https://img.shields.io/badge/OS-Linux%20%2F%20Windows-lightgrey?style=for-the-badge&logo=linux&logoColor=black)

  ![Release](https://img.shields.io/github/v/release/[KULLANICI_ADIN]/[REPO_ADIN]?style=for-the-badge&color=red)

</div>

---
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
git clone https://github.com/Wuji00000/Python-Discord-Bot-Template.git
cd Python-Discord-Bot-Template
```
### 2. Install Dependencies
Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```
### 3. Configuration
Rename the .env.example file to .env.

Open the .env file and paste your credentials:

DISCORD_TOKEN: Get it from the Discord Developer Portal.

Ai_API_KEY: Get it from somewhere if you need to talk

### 4. Run the Bot
Start the bot with the following command:

```bash
python main.py
```
📂 Project Structure
main.py: The entry point. Handles extension loading and global command syncing.

commands/: Contains all bot modules (Cogs).

mod.py: Moderation commands (Kick, Ban).

general.py: System status and ping.

clear.py: Utility commands.

🤝 Contributing
Feel free to fork this project, submit pull requests, or open issues if you find any bugs.

Created by Wuji00000
