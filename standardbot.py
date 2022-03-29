from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

print('Bot Started')

# Write message when /start is activated in chat
def on_start(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text="@#$$#$#@$#@")

# Write message, given an input 
def on_message(update, context):
	chat = update.effective_chat
	text = update.message.text
	try:
		number = float(text) # convert string to float 
		soms = number * 80.34
		message = "$%.2f" % (num)
		context.bot.send_message(chat_id=chat.id, text=message)
	except:
		context.bot.send_message(chat_id=chat.id, text="Напишите число для перевода")

token = ""
updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("telephone", on_start))  # command /X activation
dispatcher.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()
