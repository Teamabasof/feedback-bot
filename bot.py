# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [feedback-bot] (https://github.com/sanila2007/feedback-bot)

# Read GNU General Public License v3.0: https://github.com/sanila2007/feedback-bot/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I'm doing these things for free and open source
# Star and fork and enjoy!


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ForceReply

from helper import buttons, messages
from plugins import date_info, ratings
from Captcha import captcha_buttons, captcha_text

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
import datetime
from config import Config

bot = Client(
    "bot",
    api_id=7263889,
    api_hash="89c452ed35062d2d31922e6d8d069c90",
    bot_token="2031117879:AAFVvpmYOPo2u5qRJJTqG0OTp2DLIRu1rEw"
)


# START MESSAGE

@bot.on_message(filters.command("start") & filters.private)
def command1(bot, message):
    text = "ReplyKeyboard istifadə edin..."
    reply_markup = ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    bot.send_photo(message.chat.id, "https://telegra.ph/file/f7dc9203585394d0595b1.jpg",
                   caption=messages.START_TEXT_CAPTION_TEXT),
    bot.send_message(Config.LOG_CHANNEL,
                     f"Yeni istifadəçi!\n\n◉ İstifadəçi - {message.from_user.first_name}\n◉ Qoşulma vaxtı - {date_info.POSTED_TIME}\n◉ Qoşulma tarixi - {date_info.POSTED_DATE}")
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# Learn bots section

@bot.on_message(filters.regex("Botları öyrənin"))
def reply_to_Learn_Bots(bot, message):
    text = messages.LEARN_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.LEARN_REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# Restricted Stickers!!

@bot.on_message(filters.sticker)
async def restric_sticker(bot, message):
    bot.send_message(message.chat.id, "Oops!\n\nStickers has been restricted")


@bot.on_message(filters.regex("UserTaggerBot💖"))
def reply_to_utube(bot, message):
    bot.send_message(message.chat.id, "Telegram tag botu!!")
    bot.send_photo(message.chat.id, "Telegram tag botu @UserTaggerAz_bot Telegram uzre Qrup və Kanallar da tag prosessin edir")


@bot.on_message((filters.regex("Musiqi Bot🤖💖")))
def reply_to_s_ong(bot, message):
    bot.send_message(message.chat.id, "Bot yaxinda hazir olacaq!")
    bot.send_photo(message.chat.id, "BOT yaxinda sizlerle olacaq")


@bot.on_message((filters.regex("Yeni Bot🤖💖")))
def reply_to_s_ong(bot, message):
    bot.send_message(message.chat.id, "Yeni bot hazirliq prosessinde di!!!")


# About bot section

@bot.on_message(filters.regex("BOT HAQQINDA🤖"))
def reply_to_AboutBot(bot, message):
    bot.send_message(message.chat.id, "<ins>**Bot haqqında**</ins>\n\n"
                                      "Adı: <a href=https://t.me/TEAMABASOFASISSTAN_bot>TEAMABASOF ASİSSTAN ✨</a>\n\n"
                                      "Yaradılma tarixi: 06/20/2022🎂\n\n"
                                      "Ən son versiya:  v0.8.0\n\n"
                                      "Dil: <a href=www.python.org>Python</a>\n\n"
                                      "Framework: <a href=https://docs.pyrogram.org/>Pyrogram</a>\n\n"
                                      "Server: <a href=https://heroku.com>Heroku</a>\n\n"
                                      "Sahib: <a href=https://t.me/TTteamabasof\n\n</a>"
                                      "Mənbə: 🔓\n\n", disable_web_page_preview=True)


# Contact section

@bot.on_message(filters.regex("Contact 📞"))
def reply_to_Contact(bot, message):
    bot.send_message(message.chat.id, messages.CONTACT_TEXT)


# About Developer

@bot.on_message(filters.regex("Sahibim haqdda melumat"))
def reply_to_About(bot, message):
    bot.send_message(message.chat.id,
                     "**<ins>Sahibim haqdda melumat</ins>**\n\n""❖ Adı: ``Abasov Rəhim``\n\n""❖ Yaş : 16 İl (2022\n\n""❖ Ad günü : 03.27.2006\n\n""❖ Kimdən : TEAMABASOF🇦🇿\n\n""❖ Bacarıqlar : Proqramist , Usta\n\n""❖ Ambisiya : Proqram mühəndisi olun\n\n""❖ Dillər : Python, HTML, CSS\n\n❖ Hələ də Öyrənmək : C++, JS, Java")


# Home

@bot.on_message(filters.regex("Ana Menu"))
def greet(bot, message):
    text = messages.REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True

    )
@bot.on_message(filters.regex("Bitirin"))
def reply_finish(bot, message):
    bot.send_message(message.chat.id, messages.REPLY_MESSAGE, reply_markup=ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, resize_keyboard=True, one_time_keyboard=False))

# Feedbacks section

@bot.on_message(filters.regex("Feedback"))
def reply_to_Feedback(bot, message):
    text = messages.FEEDBACK_REPLY_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.FEEDBACK_REPLY_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


# Credits

@bot.on_message(filters.regex("Kreditlər"))
def reply_to_Credits(bot, message):
    text = messages.CREDITS_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.HOME_BUTTON_CR, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )




# Changelog Section

@bot.on_message(filters.regex("Dəyişikliklər qeydi"))
def reply_to_Changelog(bot, message):
    reply_markup = ReplyKeyboardMarkup(buttons.HOME_BUTTON_CR, resize_keyboard=True, one_time_keyboard=False)
    bot.send_message(message.chat.id, messages.CHANGELOG_TEXT, disable_web_page_preview=True, reply_markup=reply_markup)


# Assistant Bot Feedback/Report bugs centre

@bot.on_message(filters.regex("UserTaggerBot"))
def reply_to_Assistant(bot, message):
    reply_markup = ForceReply(message.chat.id)
    bot.send_message(message.chat.id, messages.SANILA_ASSISTANT_TEXT,
                     reply_markup=reply_markup
                     , disable_web_page_preview=True)


# Reporting area - Song Downloader bot

@bot.on_message(filters.regex("Yebi Bot"))
def reply_to_Song(bot, message):
    reply_markup = ForceReply(message.chat.id)
    text = messages.SONG_DOWNLOADER_TEXT
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# Rating bots

@bot.on_message(filters.regex("Botu qiymətləndirin"))
def reply_to_rate_bots(bot, message):
    text = ratings.RATINGS_TEXT
    reply_markup = ReplyKeyboardMarkup(ratings.RATINGS_BUTTONS, resize_keyboard=True, one_time_keyboard=False)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# Rating bots

@bot.on_message(filters.regex("Assistant Bot"))
def reply_to_rating_assistant(bot, message):
    bot.send_poll(message.chat.id, "TEAMABASOF ASİSSTAN Bota nece ulduz ses verersiz?",
                  ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    bot.send_message(message.chat.id,
                     "**İstifadəçilərin məxfiliyinə görə nə sizin reytinqləriniz, nə də digər reytinqlər heç kimi görə bilməz.** yenidən gəldiyiniz zaman reytinqləriniz **sıfırlanacaq** "
                     "lakin bu reytinqlər admin ilə paylaşılacaq.**")


@bot.on_message(filters.regex("UserTaggerBot"))
def reply_to_rating_assistant(bot, message):
    bot.send_poll(message.chat.id, "UserTaggerBot nece ulduz ses verersiz?",
                  ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    bot.send_message(message.chat.id,
                     "**İstifadəçilərin məxfiliyinə görə nə sizin reytinqləriniz, nə də digər reytinqlər heç kimi görə bilməz.** Siz onları qiymətləndirmək üçün buraya yenidən gəldiyiniz zaman reytinqləriniz **sıfırlanacaq** "
                     "lakin bu reytinqlər admin ilə paylaşılacaq.**")


@bot.on_message(filters.regex("Musiqi Bot"))
def reply_to_rating_assistant(bot, message):
    bot.send_poll(message.chat.id, "Musiqi bot nece ulduz ses verersiz?",
                  ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    bot.send_message(message.chat.id,
                     "**İstifadəçilərin məxfiliyinə görə nə sizin reytinqləriniz, nə də digər reytinqlər heç kimi görə bilməz.** Siz onları qiymətləndirmək üçün buraya yenidən gəldiyiniz zaman reytinqləriniz **sıfırlanacaq** "
                     "lakin bu reytinqlər admin ilə paylaşılacaq.**")


@bot.on_message(filters.regex("Song Bot"))
async def reply_to_rating_assistant(bot, message):
    await bot.send_poll(message.chat.id, "How many stars would you like to give to Song Download Bot?",
                        ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    await bot.send_message(message.chat.id,
                           "**İstifadəçilərin məxfiliyinə görə nə sizin reytinqləriniz, nə də digər reytinqlər heç kimi görə bilməz.** Siz onları qiymətləndirmək üçün buraya yenidən gəldiyiniz zaman reytinqləriniz **sıfırlanacaq** "
                     "lakin bu reytinqlər admin ilə paylaşılacaq.**")


# Reporting area - Torrent downloader bot

@bot.on_message(filters.regex("UserTaggerBot"))
def reply_to_Torrent(bot, message):
    reply_markup = ForceReply(message.chat.id)
    text = messages.TORRENT_DOWNLOADER_TEXT
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# Reporting area - Youtube video downloader bot

@bot.on_message(filters.regex("Musiqi Bot"))
def reply_to_Youtube(bot, message):
    text = messages.YOUTUBE_VIDEO_DOWNLOADER_TEXT
    reply_markup = ForceReply(message.chat.id)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


@bot.on_message(filters.private & filters.command("captcha"))
def captch(bot, message):
    text = captcha_text.CAPTCHA_TEX_T
    reply_markup = InlineKeyboardMarkup(captcha_buttons.CAPTCHA_BUTT_ONS)
    bot.send_photo(message.chat.id, "https://telegra.ph/file/f54447d286c02e3f18070.jpg")
    message.reply(
        text=text,
        reply_markup=reply_markup
    )




@bot.on_message(filters.private)
def fbb(bot, message):
    tet = f"**<u>Əlaqə məlumatı</u>**\n\nMesaj - `{message.text}`\nSözlərin sayı - {message.text.split()}\nGöndərən- {message.from_user.first_name}\nİsdifadəçi ID - {message.from_user.id}\nİstifadəçi adı - @{message.chat.username}\nDil - {message.from_user.language_code}\nSöhbət növü - {message.chat.type}\nGöndərmə tarixi - {date_info.POSTED_DATE}\nGöndərmə vaxtı - {date_info.POSTED_TIME}\nCavab tarixi - {date_info.DATE_OF_REPLY}\n\n<i>*Daha çox rəy əlavə edin və ya bu prosesi başa çatdırmaq üçün başa vurun!</i>"
    reply_markup = ReplyKeyboardMarkup(buttons.FINISH_FEEDBACK_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=tet,
        reply_markup=reply_markup,
        quote=True
    )

    bot.send_message(Config.FEEDBACK_CHANNEL, "**Yeni rəy mövcuddur!**\n\n" + tet)


@bot.on_callback_query()
def callback_query(Client, CallbackQuery):
    if CallbackQuery.data == "🧊":
        CallbackQuery.edit_message_text(
            captcha_text.PASS_CAPTCHA
        )

    elif CallbackQuery.data == "❌":
        CallbackQuery.edit_message_text(
            captcha_text.MULTY_FAIL,
            reply_markup=InlineKeyboardMarkup(captcha_buttons.RELOAD_CAPTCHA)
        ),

    elif CallbackQuery.data == "📩" or "🔥" or "🌭" or "🚑" or "🚡" or "💡" or "🔎" or "📈" or "🎆" or "🎎" or "🍧" or "⛑" or "🪀" or "🧸":
        CallbackQuery.edit_message_text(
            captcha_text.FAIL_CAPTCHA,
            reply_markup=InlineKeyboardMarkup(captcha_buttons.WRONG_CAPTCHA)
        )


print("Bot Aktivdir📶✨")

bot.run()
