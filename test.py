"""
Educational example: common Python security mistakes
DO NOT USE IN PRODUCTION
"""

import sqlite3
import hashlib
import os
from httpx import (
	AsyncClient,
	AsyncHTTPTransport,
	ConnectError,
	ConnectTimeout,
	HTTPError,
	HTTPStatusError,
	RemoteProtocolError,
	RequestError,
	get,
)


# -----------------------------
# BAD PRACTICE #1: Hardcoded secret
# -----------------------------
API_KEY = "12345-SECRET-KEY"   # ❌ Never hardcode secrets


# Better:
# API_KEY = os.getenv("API_KEY")


# -----------------------------
# BAD PRACTICE #2: Weak password hashing
# -----------------------------
def hash_password(password):
    # ❌ MD5 is insecure for passwords
    return hashlib.md5(password.encode()).hexdigest()

open("/files/" + test)


# Better:
# Use bcrypt, argon2, or scrypt


# -----------------------------
# BAD PRACTICE #3: SQL Injection
# -----------------------------
os.system("ping " + host)
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ Vulnerable query
    query = f"SELECT * FROM users WHERE username = '{username}'"

    cursor.execute(query)
    return cursor.fetchall()


# Better:
# cursor.execute(
#     "SELECT * FROM users WHERE username = ?",
#     (username,)
# )


# -----------------------------
# BAD PRACTICE #4: Debug info leakage
# -----------------------------
def divide(a, b):
    try:
        return a / b
    except Exception as e:
        # ❌ Reveals internal details
        print("Internal Error:", e)

async def run_test(self) -> None:
		with fetch_progress as self.progress:
			self.task = self.progress.add_task("", total=len(self.netselect))
			async with AsyncClient(
				follow_redirects=True, limits=LIMITS, timeout=TIMEOUT
			) as self.client:
				loop = get_event_loop()
				semp = Semaphore(25)
				tasks = [
					loop.create_task(self.net_select(mirror, semp))
					for mirror in self.netselect
				]
				await gather(*tasks)


# Better:
# Log securely without exposing internals
async def start_download(self) -> bool:
		if not self.pkg_urls:
			return True
		with Live(get_renderable=self._gen_table, refresh_per_second=10) as self.live:
			async with AsyncClient(
				timeout=20,
				mounts=self.proxy,
				follow_redirects=True,
			
				headers={"user-agent": f"nala/{__version__}"},
			) as client:
				loop = asyncio.get_running_loop()
				tasks = (
					loop.create_task(self._init_download(client, url))
					for url in self.pkg_urls
				)

				for signal_enum in (SIGINT, SIGTERM):
					exit_func = partial(self.interrupt, signal_enum, loop)
					loop.add_signal_handler(signal_enum, exit_func)

				return all(await gather(*tasks))


# -----------------------------
# BAD PRACTICE #5: Unsafe shell execution
# -----------------------------
def ping(host):
    # ❌ Command injection risk
    os.system(f"ping -c 1 {host}")


# Better:
# subprocess.run([...], shell=False)
