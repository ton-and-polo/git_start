from argparse import ArgumentParser
from os import getenv, getcwd, path, mkdir, chdir, listdir, system
from github import Github
from dotenv import load_dotenv


parser = ArgumentParser()
parser.add_argument('--repo', default='new_project', required=False)

# Pars args and env variables:
args = parser.parse_args()
load_dotenv()

# Configs:
PROJECT_NAME = args.repo
USER = getenv('USER_NAME')
PASSWORD = getenv('USER_PASSWORD')
TOKEN = getenv('GITHUB_ACCESS_TOKEN')
# GitHub configs:
GITHUB = Github(USER, PASSWORD)
GITHUB_USER = GITHUB.get_user()


def create_directory(name: str) -> None:
    path_ = path.join(getcwd(), name)
    mkdir(path_)
    chdir(path_)


def first_commit():
    # Commit configs:
    to_null = '1>/dev/null'
    commit_message = 'First commit'

    system(f'git init {to_null}')
    system('touch README.md .gitignore')
    system(f'git add --all {to_null}')
    system(f'git commit -am "{commit_message}" {to_null}')


if PROJECT_NAME not in set(listdir(getcwd())):
    # Local changes:
    create_directory(PROJECT_NAME)
    first_commit()

    # Remote changes:
    # TODO: create remote repository, add remote and push changes!

else:
    print(f'Directory \'{PROJECT_NAME}\' already exists. Try new name!')



