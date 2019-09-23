import telebot
import requests

from pydub import AudioSegment  

TELEGRAM_API_TOKEN = "654008532:AAEBsuX3eNl9kZS4docnfhtmpL89K28mYZM"
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)
DOWNLOAD_URL = "https://api.telegram.org/file/bot{token}".format(token=TELEGRAM_API_TOKEN)

@bot.message_handler(content_types=['voice'])
def handle_audio(message):
	
    #get audio file from message
    voice_message = message.voice

    #get audio download link 
    audio_path = bot.get_file(voice_message.file_id).file_path
    audio_download_link = DOWNLOAD_URL+audio_path

    # download audio file
    audio_file = requests.get(audio_download_link)
    audio_file_name = "audio.ogg"

    # save audio locally
    open(audio_file_name, 'wb').write(audio_file.content)

    # convert .OGG audio to .WAV
    AudioSegment.from_file(audio_file_name).export("audio.wav", format="wav")
    sound = AudioSegment.from_wav("audio.wav")
    sound = sound.set_channels(1)
    sound.export("audio.wav", format="wav")

bot.polling()