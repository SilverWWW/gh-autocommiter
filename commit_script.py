import subprocess, os, random
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

my_username = "SilverWWW"
my_email = "wsilver222@gmail.com"
repo_name = "gh-autocommiter"

PAT = os.getenv("GHPAT")
if not PAT:
    raise ValueError("Personal Access Token (PAT) not found in environment variables.")


subprocess.run(["git", "config", "--global", "user.name", my_username])
subprocess.run(["git", "config", "--global", "user.email", my_email])

num_commits = random.randint(1,5)

file_path = "commits.txt"
commit_messages = [f"Automated commit #{i+1} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}" for i in range(num_commits)]    

for i, commit_message in enumerate(commit_messages):
   
    with open(file_path, "a") as file:
        file.write(f"{commit_message}\n")
        
        if i == num_commits - 1:
            file.write("\n")


    subprocess.run(["git", "add", file_path])
    try:
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
    except subprocess.CalledProcessError:
        print("No changes to commit.")

repo_url = f"https://{PAT}@github.com/{my_username}/{repo_name}.git"
subprocess.run(["git", "remote", "set-url", "origin", repo_url])
try:
    subprocess.run(["git", "push"], check=True)
except subprocess.CalledProcessError:
    print("Failed to push changes.")