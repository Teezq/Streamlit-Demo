from github import Github
import os

# Replace these values with your own
github_token = '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'
repo_name = 'Teezq/Streamlit-Demo'
local_folder_path = 'C:/Users/ZhenQuanTee/PycharmProjects/pythonProject'

# Initialize the GitHub instance using your personal access token
g = Github(github_token)

# Get the repository
repo = g.get_repo(repo_name)

# List all files in the local folder
files_to_upload = [f for f in os.listdir(local_folder_path) if os.path.isfile(os.path.join(local_folder_path, f))]

# Upload each file to the repository by first deleting the existing file (if it exists)
for file_name in files_to_upload:
    file_path = os.path.join(local_folder_path, file_name)
    with open(file_path, 'rb') as file:
        content = file.read()

    # Specify the path in the repository where the file will be uploaded/updated
    github_file_path = f'data/{file_name}'  # Change this to your desired path

    try:
        existing_file = repo.get_contents(github_file_path)
        repo.delete_file(existing_file.path, f'Delete {file_name}', existing_file.sha, branch='main')
        print(f'Deleted existing {file_name} in GitHub repository.')

    except Exception:
        pass

    # Create a new file
    repo.create_file(github_file_path, f'Upload {file_name}', content, branch='main')
    print(f'Uploaded {file_name} to GitHub repository.')

print('All files uploaded/updated to GitHub repository successfully!')