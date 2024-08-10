import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("29343670"))
API_HASH = os.getenv("28010be97096919fe9511f8ddf1bfc54")
SESSION = os.getenv("BQG_v7YAoT-VpN4uG6JQcfxIR79Ry42M6G6GlFD-B7ZkRimJG4y6OpmI8cgTxQZBRbt9l3CjJJOwXdzBcPRyWA13V4YsPXjhdrOEhPSZDpIVBjnSSSC-ymou5Qyzs_nN_3P2njRF0A2_m4c1dlKs59sNMtm-jPEe9Dd370te1yiDoKHN2vAcYizTVNwtdFLQLME_k6_UVQYxIb3E5XHN3Ncz1snvxf-b48MFKsOoN6D3X3T2Z2gVl0i4wf3IeQCgpsvqQKkn2tQ8cvIrfzM9DxWxa7yR7i8djXFamMn8IKHjN6fv1EaWA5_uI3nZ4uU9VcAMH9HKxsvn9Zm0Gf4lHAEyTsIZCAAAAAFJtncVAA")
HNDLR = os.getenv("HNDLR", "/")
SUDO_USERS = list(map(int, os.getenv("6436690546 7013769425").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="EvaMaria"))
call_py = PyTgCalls(bot)
