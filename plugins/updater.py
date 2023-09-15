#mrismanaziz

import os
import sys
from os import environ, execle, system

from bot import Bot
from git import Repo
from git.exc import InvalidGitRepositoryError
from pyrogram import Client, filters
from pyrogram.types import Message

from config import ADMINS, LOGGER


def gen_chlog(repo, diff):
    up_repo = Repo().remotes[0].config_reader.get("url").replace(".git", "")
    ac_br = repo.active_branch.name
    ch_log = ""
    tldr_log = ""
    ch = f"Update for <a href={up_repo}/tree/{ac_br}>[{ac_br}]</a>:"
    ch_tl = f"Updates for {ac_br}:"
    d_form = "%d/%m/%y | %H:%M"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"\n{c.count()} [{c.committed_datetime.strftime(d_form)}]\n"
            f"<a href={up_repo.rstrip('/')}/commit/{c}>[{c.summary}]</a> {c.author}"
        )
        tldr_log += f"\n{c.count()} [{c.committed_datetime.strftime(d_form)}]\n[{c.summary}] {c.author}"
    if ch_log:
        return str(ch + ch_log), str(ch_tl + tldr_log)
    return ch_log, tldr_log


def updater():
    try:
        repo = Repo()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", UPSTREAM)
        origin.fetch()
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)
    ac_br = repo.active_branch.name
    if "upstream" in repo.remotes:
        ups_rem = repo.remote("upstream")
    else:
        ups_rem = repo.create_remote("upstream", UPSTREAM)
    ups_rem.fetch(ac_br)
    changelog, tl_chnglog = gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    return bool(changelog)


@Bot.on_message(filters.command("update") & filters.user(ADMINS))
async def update_bot(_, message: Message):
    message.chat.id
    msg = await message.reply_text("...")
    update_avail = updater()
    if update_avail:
        await msg.edit("Updated!")
        system("git reset && git pull --rebase -f && pip3 install --no-cache-dir -r requirements.txt")
        execle(sys.executable, sys.executable, "main.py", environ)
        return
    await msg.edit("Updated!")


@Bot.on_message(filters.command("restart") & filters.user(ADMINS))
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply_text("...")
        LOGGER(__name__).info("Bot Restarted!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("Bot Restarted!")
    os.system(f"kill -9 {os.getpid()} && python main.py")
