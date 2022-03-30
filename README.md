Two approaches to utilise Telegram Bots:
- <code>request</code> library
- <code>python-telegram-bot</code> library

Some Notes:
- <code>Request</code> library allows the utilisation of bots straight from python without chat commands

Some Uses:
- Remotely post content to a group using python & store data content found in <code>response.text</code> (when using <code>request</code> library), so the data can be passed on and utilised for analysis etc

Bot Related Information:
- Bots need to be created using the Telegram @BotFather chat & commands
- <code>chat_id</code> can be confirmed by inviting @getidsbot to the group
- <code>bot_id</code> is the authentication code of each bot, created by a Telegram user; ie. all created bots are tied to a username
