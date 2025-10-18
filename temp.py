from dotenv import load_dotenv
from supabase import create_client, Client
import os

load_dotenv(".env.local")
supabase: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

data = supabase.table("users").select("email").execute()

print(data)


# result = supabase.rpc('get_all_tables').execute()
# print(result.data)   