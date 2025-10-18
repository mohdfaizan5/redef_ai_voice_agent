from dotenv import load_dotenv
from supabase import create_client, Client
import os
load_dotenv(".env.local")


access_token='Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IkQ2Q3o0eFhKMkxjd2pkTkUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2hvb3ZzZGRoZWNvcG9ha25pYmxjLnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiJlZTc5ZTY4OC04MWViLTQ1MjctOGJkYy04MThlMjRiNmQ5MmUiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzYwNzk5Nzg3LCJpYXQiOjE3NjA3OTYxODcsImVtYWlsIjoibW9oZGZhaXphbjEzMTIzQGdtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZW1haWwiLCJwcm92aWRlcnMiOlsiZW1haWwiXX0sInVzZXJfbWV0YWRhdGEiOnsiZW1haWwiOiJtb2hkZmFpemFuMTMxMjNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBob25lX3ZlcmlmaWVkIjpmYWxzZSwic3ViIjoiZWU3OWU2ODgtODFlYi00NTI3LThiZGMtODE4ZTI0YjZkOTJlIn0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoicGFzc3dvcmQiLCJ0aW1lc3RhbXAiOjE3NjA3OTYxODd9XSwic2Vzc2lvbl9pZCI6ImVjMDFlM2NlLWMzZDgtNDlhYi1iMzg4LTA0ZWJmYTRhNjk3YyIsImlzX2Fub255bW91cyI6ZmFsc2V9.FXb57Gfm891PcCzZXvIBjCWqVgPDxXghYhRFMTgNgSs'
refresh_token='yciy7udn5vr4'
# print(type(access_token), access_token)

# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_ANON_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))


# now RLS policies will apply for that user
user_id = "ee79e688-81eb-4527-8bdc-818e24b6d92e"
data = supabase.table("pomodoros").select('focus_time').execute()

d = [{'focus_time': 301}, {'focus_time': 301}, {'focus_time': 2324}, {'focus_time': 3}, {'focus_time': 2}, {'focus_time': 1}, {'focus_time': 3}, {'focus_time': 71}, {'focus_time': 2}, {'focus_time': 2}, {'focus_time': 7}, {'focus_time': 113}, {'focus_time': 1}, {'focus_time': 6}, {'focus_time': 1}, {'focus_time': 48}, {'focus_time': 2}, {'focus_time': 2}, {'focus_time': 2}, {'focus_time': 400}, {'focus_time': 1}, {'focus_time': 301}, {'focus_time': 3}, {'focus_time': 4}, {'focus_time': 3}, {'focus_time': 61}, {'focus_time': 61}, {'focus_time': 61}, {'focus_time': 175}, {'focus_time': 9}, {'focus_time': 3}, {'focus_time': 2}, {'focus_time': 1}, {'focus_time': 61}, {'focus_time': 1792}, {'focus_time': 301}, {'focus_time': 1501}, {'focus_time': 1501}, {'focus_time': 1501}, {'focus_time': 1}, {'focus_time': 901}, {'focus_time': 1436}, {'focus_time': 1}, {'focus_time': 1}, {'focus_time': 948}, {'focus_time': 178}, {'focus_time': 2}, {'focus_time': 301}, {'focus_time': 301}, {'focus_time': 10}, {'focus_time': 2}, {'focus_time': 87}, {'focus_time': 1}, {'focus_time': 1}, {'focus_time': 2}, {'focus_time': 1}, {'focus_time': 301}, {'focus_time': 301}, {'focus_time': 301}, {'focus_time': 6}, {'focus_time': 1}, {'focus_time': 3}, {'focus_time': 901}, {'focus_time': 27}]
print(type(data.data), data)

total = 0
for a in data.data:
    total += a['focus_time']
print(total)

# data = supabase.table("tasks").select("id,name,category").eq("is_completed", False).limit(5).execute()
print(data)