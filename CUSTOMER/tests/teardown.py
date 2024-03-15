import os
import supabase
from dotenv import load_dotenv


load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
supabase_client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

def display_all_users():
    
    data = supabase_client.auth.sign_in_with_password({"email": "nrct5@zprodev.com", "password": "Test@123"})

    
    res = supabase_client.auth.get_user()
    #response = supabase_client.table("Customer").select().execute()
    #print (f"Row Count: {response.count}")


display_all_users()