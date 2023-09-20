from googleapiclient.discovery import build
import telebot

from local import *

bot = telebot.TeleBot(BOT_TOKEN)


def get_latest_videos():
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(
        part='snippet',
        channelId=YOUTUBE_CHANNEL_ID,
        maxResults=1,
        order='date'
    )
    response = request.execute()
    videos = response.get('items', [])
    return videos


@bot.message_handler(commands=['latestvideos'])
def send_latest_videos(message):
    videos = get_latest_videos()
    if videos:
        for video in videos:
            video_id = video['id']['videoId']
            video_url = f'https://www.youtube.com/watch?v={video_id}'
            video_title = video['snippet']['title']
            bot.send_message(message.chat.id, f'{video_title}\n{video_url}')
    else:
        bot.send_message(message.chat.id, 'На жаль, нові відео відсутні.')
