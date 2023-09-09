# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import(
    FORCE_SUB_1,
    FORCE_SUB_2,
    FORCE_SUB_3,
    FORCE_SUB_4
)
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not (FORCE_SUB_1 and FORCE_SUB_2 and FORCE_SUB_3 and FORCE_SUB_4):
        buttons = [
            [
                InlineKeyboardButton(text="Help & Commands", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="Close", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_1 and not FORCE_SUB_2 and not FORCE_SUB_3 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="Join 1", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="Help & Commands", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="Close", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_2 and not FORCE_SUB_3 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="Join 1", url=client.invitelink),
                InlineKeyboardButton(text="Join 2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="Help & Commands", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="Close", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_2 and FORCE_SUB_3 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="Join 1", url=client.invitelink),
                InlineKeyboardButton(text="Join 2", url=client.invitelink2),
                InlineKeyboardButton(text="Join 3", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="Help & Commands", callback_data="help"),
            ],
            [InlineKeyboardButton(text="Close", callback_data="close")],
        ]
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_2 and FORCE_SUB_3 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="Join 1", url=client.invitelink),
                InlineKeyboardButton(text="Join 2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="Join 3", url=client.invitelink3),
                InlineKeyboardButton(text="Join 4", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="Help & Commands", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="Close", callback_data="close"),
            ],
        ]
        return buttons


def fsub_button(client, message):
    if FORCE_SUB_1 and not FORCE_SUB_2 and not FORCE_SUB_3 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="Join 1", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_2 and not FORCE_SUB_3 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="Join 1", url=client.invitelink),
                InlineKeyboardButton(text="Join 2", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_2 and FORCE_SUB_3 and not FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="Join 1", url=client.invitelink),
                InlineKeyboardButton(text="Join 2", url=client.invitelink2),
                InlineKeyboardButton(text="Join 3", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_1 and FORCE_SUB_2 and FORCE_SUB_3 and FORCE_SUB_4:
        buttons = [
            [
                InlineKeyboardButton(text="Join 1", url=client.invitelink),
                InlineKeyboardButton(text="Join 2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="Join 3", url=client.invitelink3),
                InlineKeyboardButton(text="Join 4", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Coba Lagi",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
