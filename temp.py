from dotenv import load_dotenv
from supabase import create_client, Client
import os
load_dotenv(".env.local")


access_token='Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IkQ2Q3o0eFhKMkxjd2pkTkUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2hvb3ZzZGRoZWNvcG9ha25pYmxjLnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiJlZTc5ZTY4OC04MWViLTQ1MjctOGJkYy04MThlMjRiNmQ5MmUiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzYwNzk5Nzg3LCJpYXQiOjE3NjA3OTYxODcsImVtYWlsIjoibW9oZGZhaXphbjEzMTIzQGdtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZW1haWwiLCJwcm92aWRlcnMiOlsiZW1haWwiXX0sInVzZXJfbWV0YWRhdGEiOnsiZW1haWwiOiJtb2hkZmFpemFuMTMxMjNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBob25lX3ZlcmlmaWVkIjpmYWxzZSwic3ViIjoiZWU3OWU2ODgtODFlYi00NTI3LThiZGMtODE4ZTI0YjZkOTJlIn0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoicGFzc3dvcmQiLCJ0aW1lc3RhbXAiOjE3NjA3OTYxODd9XSwic2Vzc2lvbl9pZCI6ImVjMDFlM2NlLWMzZDgtNDlhYi1iMzg4LTA0ZWJmYTRhNjk3YyIsImlzX2Fub255bW91cyI6ZmFsc2V9.FXb57Gfm891PcCzZXvIBjCWqVgPDxXghYhRFMTgNgSs'
refresh_token='yciy7udn5vr4'
# print(type(access_token), access_token)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)


# this tells supabase-py which user session to act as
supabase.auth.set_session(access_token=access_token, refresh_token=refresh_token)

# now RLS policies will apply for that user
user_id = "ee79e688-81eb-4527-8bdc-818e24b6d92e"
response = supabase.table("habit").select("*").eq("user_id", user_id).execute()

print(response)

# response = supabase.auth.sign_in_with_password(
#     {
#         "email": "mohdfaizan13123@gmail.com",
#         "password": "password",
#     }
# )

print(response)


# result = supabase.rpc('get_all_tables').execute()
# print(result.data)   

"""
user=User(id='ee79e688-81eb-4527-8bdc-818e24b6d92e', app_metadata={'provider': 'email', 'providers': ['email']}, user_metadata={'email': 'mohdfaizan13123@gmail.com', 'email_verified': 
True, 'phone_verified': False, 'sub': 'ee79e688-81eb-4527-8bdc-818e24b6d92e'}, aud='authenticated', confirmation_sent_at=None, recovery_sent_at=None, email_change_sent_at=None, new_email=None, new_phone=None, invited_at=None, action_link=None, email='mohdfaizan13123@gmail.com', phone='', created_at=datetime.datetime(2025, 10, 16, 4, 19, 54, 362525, tzinfo=TzInfo(0)), confirmed_at=datetime.datetime(2025, 10, 16, 4, 19, 54, 408493, tzinfo=TzInfo(0)), email_confirmed_at=datetime.datetime(2025, 10, 16, 4, 19, 54, 408493, tzinfo=TzInfo(0)), phone_confirmed_at=None, last_sign_in_at=datetime.datetime(2025, 10, 18, 14, 3, 7, 164258, tzinfo=TzInfo(0)), role='authenticated', updated_at=datetime.datetime(2025, 10, 18, 14, 3, 7, 189824, tzinfo=TzInfo(0)), identities=[UserIdentity(id='ee79e688-81eb-4527-8bdc-818e24b6d92e', identity_id='2549adb2-73e9-4a0f-a0d5-082ee9527dbf', user_id='ee79e688-81eb-4527-8bdc-818e24b6d92e', identity_data={'email': 'mohdfaizan13123@gmail.com', 'email_verified': False, 'phone_verified': False, 'sub': 'ee79e688-81eb-4527-8bdc-818e24b6d92e'}, provider='email', created_at=datetime.datetime(2025, 10, 16, 4, 19, 54, 395544, tzinfo=TzInfo(0)), last_sign_in_at=datetime.datetime(2025, 10, 16, 4, 19, 54, 395490, tzinfo=TzInfo(0)), updated_at=datetime.datetime(2025, 10, 16, 4, 19, 54, 395544, tzinfo=TzInfo(0)))], is_anonymous=False, factors=None) session=Session(provider_token=None, provider_refresh_token=None, 
access_token='eyJhbGciOiJIUzI1NiIsImtpZCI6IkQ2Q3o0eFhKMkxjd2pkTkUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2hvb3ZzZGRoZWNvcG9ha25pYmxjLnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiJlZTc5ZTY4OC04MWViLTQ1MjctOGJkYy04MThlMjRiNmQ5MmUiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzYwNzk5Nzg3LCJpYXQiOjE3NjA3OTYxODcsImVtYWlsIjoibW9oZGZhaXphbjEzMTIzQGdtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZW1haWwiLCJwcm92aWRlcnMiOlsiZW1haWwiXX0sInVzZXJfbWV0YWRhdGEiOnsiZW1haWwiOiJtb2hkZmFpemFuMTMxMjNAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBob25lX3ZlcmlmaWVkIjpmYWxzZSwic3ViIjoiZWU3OWU2ODgtODFlYi00NTI3LThiZGMtODE4ZTI0YjZkOTJlIn0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoicGFzc3dvcmQiLCJ0aW1lc3RhbXAiOjE3NjA3OTYxODd9XSwic2Vzc2lvbl9pZCI6ImVjMDFlM2NlLWMzZDgtNDlhYi1iMzg4LTA0ZWJmYTRhNjk3YyIsImlzX2Fub255bW91cyI6ZmFsc2V9.FXb57Gfm891PcCzZXvIBjCWqVgPDxXghYhRFMTgNgSs',
 refresh_token='yciy7udn5vr4',
  expires_in=3600, expires_at=1760799787, token_type='bearer', user=User(id='ee79e688-81eb-4527-8bdc-818e24b6d92e', app_metadata={'provider': 'email', 'providers': ['email']}, user_metadata={'email': 'mohdfaizan13123@gmail.com', 'email_verified': True, 'phone_verified': False, 'sub': 'ee79e688-81eb-4527-8bdc-818e24b6d92e'}, aud='authenticated', confirmation_sent_at=None, recovery_sent_at=None, email_change_sent_at=None, new_email=None, new_phone=None, invited_at=None, action_link=None, 
email='mohdfaizan13123@gmail.com', phone='', created_at=datetime.datetime(2025, 10, 16, 4, 19, 54, 362525, tzinfo=TzInfo(0)), confirmed_at=datetime.datetime(2025, 10, 16, 4, 19, 54, 408493, tzinfo=TzInfo(0)), email_confirmed_at=datetime.datetime(2025, 10, 16, 4, 19, 54, 408493, tzinfo=TzInfo(0)), phone_confirmed_at=None, last_sign_in_at=datetime.datetime(2025, 10, 18, 14, 3, 7, 164258, tzinfo=TzInfo(0)), role='authenticated', updated_at=datetime.datetime(2025, 10, 18, 14, 3, 7, 189824, tzinfo=TzInfo(0)), identities=[UserIdentity(id='ee79e688-81eb-4527-8bdc-818e24b6d92e', identity_id='2549adb2-73e9-4a0f-a0d5-082ee9527dbf', user_id='ee79e688-81eb-4527-8bdc-818e24b6d92e', identity_data={'email': 'mohdfaizan13123@gmail.com', 'email_verified': False, 'phone_verified': False, 'sub': 'ee79e688-81eb-4527-8bdc-818e24b6d92e'}, provider='email', created_at=datetime.datetime(2025, 10, 16, 4, 19, 54, 395544, tzinfo=TzInfo(0)), last_sign_in_at=datetime.datetime(2025, 10, 16, 4, 19, 54, 395490, tzinfo=TzInfo(0)), updated_at=datetime.datetime(2025, 10, 16, 4, 19, 54, 395544, tzinfo=TzInfo(0)))], is_anonymous=False, factors=None))"""



 # @function_tool
    # async def list_tasks(self):
    #     """Fetch a list of users tasks left """
    #     user_id = "01711181-d5f2-48ae-bf1e-ef7ad99f752a"
    #     try:
          # data = supabase.table("tasks").select("id,name,category").eq("is_completed", False).limit(5).execute()
    #         print(f"\n\n{data}\n\n")
    #         if not data.data:
    #             return "No tasks found in the database."
    #         return f"Found {len(data.data)} tasks. Example: {data.data}"
    #     except Exception as e:
    #         return f"Error fetching tasks: {str(e)}"



"""
tasks

✅ Basic agent
⬛ tasks
    ⬛ fetch_tasks
    ⬛ update tasks
    ⬛ create_tasks
    ⬛ delete tasks
⬛ habits
    ⬛ fetch_tasks
    ⬛ update tasks
⬛ deepwork
    ⬛ fetch_tasks


"""