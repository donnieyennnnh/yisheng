from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6471769794:AAFVjH1vvF7Or0PeCBWvjcwHIr7xE6utCSM'
BOT_USERNAME: Final = '@wpmStore_bot'



async def Yishengangry_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('你很 fuck eh')


async def flappu_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.replys_text('@flappu come to wpn store!')


async def ooihurryup_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('ooi 快点 lah ')

async def bruh_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('你会不会的!')


#Handle responses

def handle_response(text:str) -> str:
    processed: str = text.lower()

    if 'who is going wpn store' in processed:
        return '@Flappuu come wpn store now! 💀💀'
    
    if 'you need any gunners for servicing tmr?' in processed:
        return 'I need @IlIIlIIlIIlIllIlIIl @Gerardtay @Flappuu come wpn store asap!'
   

    return '你会不会的!'

#Handle message (whether is priv or group)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type #inform u whether group chat or priv
    text: str = update.message.text #message incoming that we can process 

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}')      

    if message_type == 'group': # for group
        if BOT_USERNAME in text:
            new_text:str = text.replace(BOT_USERNAME, '').strip()
            response:str = handle_response(new_text)
        else:
            return
        
    elif message_type == 'supergroup': # for supergroup
        if BOT_USERNAME in text:
            new_text:str = text.replace(BOT_USERNAME, '').strip()
            response:str = handle_response(new_text)
        else:
            return
    
    else:
        response:str = handle_response(text) #for priv chat

    print('Bot:', response) #for debugging

    await update.message.reply_text(response) # reply with new response



async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')



if __name__ == '__main__':
    print('starting bot......')
    app = Application.builder().token(TOKEN).build()


    #Commands

    
    app.add_handler(CommandHandler('flappu',flappu_command))
  
    app.add_handler(CommandHandler('Yishengangry', Yishengangry_command))
    app.add_handler(CommandHandler('bruh',bruh_command))
    app.add_handler(CommandHandler('hurryup',ooihurryup_command))


    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #errors

    app.add_error_handler(error)

    #polls the bot
    print("Polling...")
    app.run_polling(poll_interval=1.0) #tells programme how often to check for update