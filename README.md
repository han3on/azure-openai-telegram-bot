# Azure OpenAI Bot for Telegram

## 🐱 Introduction

Azure OpenAI Bot for Telegram is implemented with [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/) . The Telegram integration framework is based on [python-telegram-bot](https://python-telegram-bot.org).

## 👷 Deploy Your Own

### Preparation

1. Create a Telegram Bot by [@BotFather](https://t.me/BotFather) and get the token.
2. Create an Azure account and get the API key and endpoint.
3. A Linux VM or a server with Python 3 is needed to run the Bot.
4. A practical Internet environment is required.
5. (Optional) [FFmpeg](https://ffmpeg.org) is required for the Bot to handle voice messages with Whisper. If you are not interested in using voice messages, you don't need to install it and **must set `enable_voice` in the config file to False**.
6. (Optional) [Azure TTS SDK](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstarts/setup-platform?pivots=programming-language-python&tabs=linux) is required for the Bot to reply with voice messages.

### Installation

1. Git clone from main branch or download the latest release [Source code](https://github.com/han3on/azure-openai-telegram-bot) file and install the dependencies.

```bash
git clone https://github.com/han3on/azure-openai-telegram-bot.git
cd azure-openai-telegram-bot
pip install -r requirements.txt
```

2. Create a config file to manage the Bot.

The config file includes sensitive information, such as telegram_token, openai_api_key, openai_api_endpoint and openai_api_deployment_name, we only release the corresponding template `config.json.template`. Therefore, you need to create a new `config.json` file by replacing the relative fields in the template with your own.

```bash
cp config.json.template config.json
```

**Recommended:** You should keep `config.json.template` unmodified because the Bot needs to read default configuration values from it. For backward compatibility, it is highly recommended to check the template for newly added parameters when you update to a new version.

3. Run the Bot with `start_bot.sh` and try talk to it. You can also use docker to run the Bot.

```bash
# First, make sure you are in the root directory of the project,
# aka <your_download_location>/azure-openai-telegram-bot
bash ./bin/start_bot.sh # start the Bot

To clear ChatGPT conversation context and restart the Bot, run shell script `restart_bot.sh`. To shut down the Bot, run `stop_bot.sh`.

```bash
bash ./bin/restart_bot.sh # restart the Bot
bash ./bin/stop_bot.sh # stop the Bot
```

Up to now, you have successfully deployed the Bot.

### Usage

The Bot works in both personal and group chat of Telegram.
In a personal chat, simply send a message to the Bot and it will reply to you.
In a group chat, use the `/chat` to invoke the Bot. 

In a personal chat with a contact, use `@your_bot_name <your messages>` to invoke the Bot with Telegram inline mode. Both you and your contact can see the Bot's reply in the chat. 

1. The following commands are supported:

- `/start`: Start the Bot.
- `/role <prompt>`: Set role for conversation.
- `/chat` : Invoke the Bot in group chat.
- `/clear`: Clear the conversation context.
- `/getid`: Get your Telegram user ID.

(Optinal) You can set them up as Telegram Bot command, see [here](https://core.telegram.org/bots/tutorial#creating-your-command).

2. Inline mode

To enable inline mode, see [here](https://core.telegram.org/bots/api#inline-mode). 

Type `/mybots` > Your_Bot_Name > Bot Settings > Inline Feedback, you must set the `Inline Feedback` to 100%.

## 🪪 License

[MIT](LICENSE.md)
