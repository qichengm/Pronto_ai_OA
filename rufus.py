import subprocess
import datetime

def main(git_dir):
    # Get the active branch
    branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=git_dir, capture_output=True)
    print("active branch: ", branch.stdout.decode().strip())

    # Check if repository files have been modified
    modified = subprocess.run(["git", "status", "--porcelain"], cwd=git_dir, capture_output=True)
    print("local changes: ", bool(modified.stdout))

    # Check if current head commit was authored in the last week
    commit = subprocess.run(["git", "log", "-1", "--pretty=format:'%ai'"], cwd=git_dir, capture_output=True)
    commit_date = datetime.datetime.strptime(commit.stdout.decode().strip("'"), "%Y-%m-%d %H:%M:%S %z")
    print("recent commit: ", (datetime.datetime.now() - commit_date.replace(tzinfo=None)).days < 7)

    # Check if current head commit was authored by Rufus
    author = subprocess.run(["git", "log", "-1", "--pretty=format:'%an'"], cwd=git_dir, capture_output=True)
    print("blame Rufus: ", author.stdout.decode().strip("'") == "Rufus")

if __name__ == "__main__":
    path = input("Please enter the git directory path\n")
    main(path)
