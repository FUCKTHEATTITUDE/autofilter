import subprocess
from asyncio import Lock
from re import findall
from pyrogram import Client, filters

@Client.on_message(filters.command("ping") & ~filters.edited)
async def ping_handler(_, message):
    PING_LOCK = Lock()
    m = await message.relpy_text("Pinging datacenters...")
    async with PING_LOCK:
        ips = {
            "dc1": "149.154.175.53",
            "dc2": "149.154.167.51",
            "dc3": "149.154.175.100",
            "dc4": "149.154.167.91",
            "dc5": "91.108.56.130",
        }
        text = "**Pings:**\n"

        for dc, ip in ips.items():
            try:
                shell = subprocess.run(
                    ["ping", "-c", "1", "-W", "2", ip],
                    text=True,
                    check=True,
                    capture_output=True
                )
                resp_time = findall(r"time=.+m?s", shell.stdout, re.MULTILINE)[
                    0].replace(
                    "time=", ""
                )

                text += f"    **{dc.upper()}:** {resp_time} ✅\n"
            except Exception:
                # There's a cross emoji here, but it's invisible.
                text += f"    **{dc.upper}:** ❌\n"
        await m.edit(text)
