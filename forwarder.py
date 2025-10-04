# forwarder.py
# Developer: REDDOT 💻🔥
# Description:
#  ├─ Forwards every message from topic 74 in @WURKDOTFUN to your private group
#  ├─ Sends a rich welcome message with inline button and image
#  └─ Fully Termux-compatible for 24/7 background use

from telethon import TelegramClient, events, Button
import asyncio

# ─────────────────────────────────────────────
# 🔧 CONFIG
api_id = 26172025
api_hash = "c3185b37a8e1acc6f38f153cf5239c"

SOURCE_CHAT = -1003147412716      # wurkdotfun forum
SOURCE_TOPIC = 74                  # target topic
DESTINATION_CHAT = -1002583928917  # your group
WELCOME_IMAGE = "https://i.imgur.com/WJzqI0C.png"  # example image
# ─────────────────────────────────────────────

client = TelegramClient("user_session", api_id, api_hash)


async def send_welcome():
    """Send welcome message with inline button and image"""
    try:
        caption = (
            "👋 **Welcome to Just A $WURKING Boy!**\n\n"
            "💡 Auto-forward system by **Dev REDDOT** is now active.\n"
            "🔁 Every new message from @WURKDOTFUN topic 74 will appear here automatically.\n\n"
            "⚙️ _Stay tuned and WURK smart!_"
        )
        buttons = [
            [Button.url("🔥 Visit WURKDOTFUN", "https://t.me/WURKDOTFUN/74")],
            [Button.url("💻 Dev REDDOT", "https://t.me/REDDOT_UPDATES")]
        ]

        await client.send_file(
            DESTINATION_CHAT,
            file=WELCOME_IMAGE,
            caption=caption,
            buttons=buttons,
            link_preview=False,
        )
        print("✅ Welcome message sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send welcome: {e}")


@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def forward_from_topic(event):
    """Forward messages from specific topic"""
    try:
        # filter only messages from the correct topic
        if getattr(event.message, "reply_to", None) and \
           getattr(event.message.reply_to, "forum_topic_id", None) == SOURCE_TOPIC:

            # Forward preserving text, media and buttons
            await client.send_message(
                DESTINATION_CHAT,
                message=event.message.message or "",
                buttons=event.message.buttons,
                file=event.message.media or None,
                link_preview=False,
            )
            print("📩 Message forwarded successfully.")
    except Exception as e:
        print(f"❌ Error forwarding message: {e}")


async def main():
    print("✅ User client started")
    await send_welcome()
    print(f"📡 Listening for new messages from topic {SOURCE_TOPIC}...")
    await client.run_until_disconnected()


if __name__ == "__main__":
    client.start()
    asyncio.run(main())
