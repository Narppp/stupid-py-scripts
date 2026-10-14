# commit stupid

import subprocess
import random
import sys

# list of bullying message
messages: list[str] = ["wait this is actually good???",
                 "commiting another project that won't be seen by recruiters...",
                 "bugfix that'll come back tomorrow :)",
                 "changed one thing and called it productive",
                 "committed 769 times in 6 minutes"];

def run_command(command: list[str]) -> str:
    """return the command if gud"""
    
    command_result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True);

    return command_result.stdout.strip();

def check_status() -> bool:
    """check if command is actually valid, return False if nah"""
    output: str = run_command(["git", "status", "--porcelain"]);

    return len(output) > 0;

def main() -> None:
    print("lemme see if this is actually a valid repo..");
    if not check_status():
        print("YOU STUPID ASS CREATE YOUR REPO FIRST OR ATLEAST ADD CHANGES");
        sys.exit(1);
    
    chosen_message: str = random.choice(messages);
    print(f"chosen message: {chosen_message}");

    command_output: str = run_command(["git", "commit", "-m", chosen_message]);

    print(command_output);
    print("commit successfully, now go away");

if __name__ == "__main__":
    main();
