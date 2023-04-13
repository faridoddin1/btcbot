import requests
import os
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Crypto Price Bot! Enter '/price <currency_name>' to get the current price of a cryptocurrency.")

def price(update, context):
    currency_name = context.args[0].upper()
    url = f"https://min-api.cryptocompare.com/data/price?fsym={currency_name}&tsyms=USD"
    response = requests.get(url)
    if response.status_code == 200:
        price = response.json()["USD"]
        message = f"The price of {currency_name} is currently ${price:.2f}"
    else:
        message = "Error occurred while getting price data."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

if __name__ == '__main__':
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token=os.environ['6297581881:AAHatEyDRmWNAKj3ntzalEuHEttlBcFB7WA'], use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handlers
    start_handler = CommandHandler('start', start)
    price_handler = CommandHandler('price', price)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(price_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

