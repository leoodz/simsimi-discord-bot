<div style="display: inline_block">
  <img align="center" alt="Discord" src="https://github.com/leoodz/discordsimsimi/blob/main/Images/discord_logo.png" width="150" height="150">
  <img align="center" alt="Simsimi" src="https://github.com/leoodz/discordsimsimi/blob/main/Images/Logo%20Simsimi.png" width="150" height="150">
  
</div>

# <> BOT DISCORD + SIMSIMI  

It is a script that implements a chat-bot API [Simsimi](https://www.simsimi.com/) in a bot associated with the [Discord](https://discord.com/) platform.  
  
## Instructions:

- First, you must create an application (bot) in Discord. To do this, use the platform's development site: https://discord.com/developers/applications

- Install **requirement** library:
```
pip install -r requirement
```
Change the example.env to .env and fill in the infomation

- The file [main.py](https://github.com/leoodz/discordsimsimi/blob/main/main.py) contains all the bot's schematics. In this one, you must modify two objects:

    [channels (list)](https://github.com/leoodz/discordsimsimi/blob/01fb7c2ae741aad65395eecc99822f8aea27a5fc/main.py#L10) = Add to the list the channels that simsimi integration can respond to;

    [TOKEN (str)](https://github.com/leoodz/discordsimsimi/blob/a60bd59b0e6e6ff9b7ce79e746ae3f2dbe65641d/main.py#L29) = Insert the TOKEN of the bot.

- In the file [simsimi.py](https://github.com/leoodz/discordsimsimi/blob/main/simsimi.py) there is a function that performs the integration of the message required in the discord with the Simsimi API.

------------------------------------------------- -------------------

## Working example:
<a>
  <img align="center" alt="Example" src="https://github.com/leoodz/discordsimsimi/blob/main/Images/testes.png" width="350" height="350">
</a>