import subprocess
import os

# 🚨 IMPORTANT: Customize the file path below if you want to use a specific file location.
# If you're using Obsidian or another app, replace the value of `TASK_FILE` with the full file path to your desired tasks.md file.
# Example for Obsidian:
# TASK_FILE = "/Users/yourusername/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian Vault/tasks.md"
# Otherwise, the script will create a file named "tasks.md" in the same folder as this script.

TASK_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.md")  # Default location (same as script)

def initialize_task_file():
    """
    Initializes the tasks file with a structured template if it doesn't exist or is empty.
    Provides embedded guidance within tasks and goals to help the user understand how to use BroccoliBottle.
    """
    if not os.path.exists(TASK_FILE) or os.stat(TASK_FILE).st_size == 0:
        default_content = (
            "# 📅 Daily Tasks\n"
            "- [ ] e.g. Run 4km today on the treadmill.\n"
            "- [ ] Write your personal tasks here to stay organized.\n"
            "- [ ] BroccoliBottle will also automatically suggest up to 3 tasks (or enough to reach 6 total).\n"
            "- [ ] Stay consistent and check off tasks as you complete them.\n\n"
            "# 🎯 Goals\n"
            "- e.g. Train to run a 10km trail by summer.\n"
            "- Define specific and clear goals to guide BroccoliBottle's suggestions.\n"
            "- The more detailed your goals, the better the recommendations.\n"
            "- Use this section to give BroccoliBottle context for your priorities.\n"
        )
        with open(TASK_FILE, "w") as file:
            file.write(default_content)
        print(f"📂 tasks.md initialized at {TASK_FILE}. Add your tasks and goals to begin.")
        exit()  # ✅ Prevent task generation on the first run

def read_tasks():
    """Reads and returns the content of the tasks file."""
    with open(TASK_FILE, "r") as file:
        return file.read()

def extract_existing_tasks(content):
    """
    Extracts and classifies existing tasks from the 'Daily Tasks' section.
    Separates user tasks from BroccoliBottle-generated tasks and tracks completion status.
    """
    try:
        tasks_section = content.split("# 📅 Daily Tasks")[1].split("# 🎯 Goals")[0]
    except IndexError:
        tasks_section = ""
    lines = tasks_section.strip().split("\n")
    
    user_tasks_incomplete = []
    user_tasks_complete = []
    bb_tasks_incomplete = []
    bb_tasks_complete = []

    for line in lines:
        task = line.strip("- [ ]").strip("- [x]").strip("⛯ ").strip()
        if line.startswith("- [ ] ⛯"):
            bb_tasks_incomplete.append(task)
        elif line.startswith("- [x] ⛯"):
            bb_tasks_complete.append(task)
        elif line.startswith("- [ ]"):
            user_tasks_incomplete.append(task)
        elif line.startswith("- [x]"):
            user_tasks_complete.append(task)
    
    return {
        "user_incomplete": user_tasks_incomplete,
        "user_complete": user_tasks_complete,
        "bb_incomplete": bb_tasks_incomplete,
        "bb_complete": bb_tasks_complete
    }

def extract_goals(content):
    """Extracts user-defined goals from the 'Goals' section."""
    try:
        goals_section = content.split("# 🎯 Goals")[1]
    except IndexError:
        goals_section = ""
    return [line.strip("- ").strip() for line in goals_section.strip().split("\n") if line.startswith("-")]

def generate_suggestions(goals, tasks, tasks_needed):
    """
    Generates up to 'tasks_needed' context-aware, actionable tasks related to the user's goals.
    Ensures tasks are directly linked to goals and avoids duplication.
    """
    prompt = (
        f"Generate exactly {tasks_needed} highly specific and actionable tasks that directly advance the following goals: {', '.join(goals)}. "
        f"Exclude any generic, vague, loosely related, or redundant tasks. "
        f"Prioritize avoiding tasks similar to these important user-inputted tasks: {', '.join(tasks['user_incomplete'])}. "
        f"Also avoid suggesting tasks similar to these BroccoliBottle-generated tasks: {', '.join(tasks['bb_incomplete'])}. "
        "Each task must be concise, actionable within a day, and designed for individual action. "
        "Focus on logical progression and measurable outcomes. "
        "Ensure no numbering is present in the output. "
        "Only output plain text, one task per line, with no formatting or extra comments."
    )

    result = subprocess.run(
        ["ollama", "run", "phi4"],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode().strip()

def update_task_file(content, suggestions):
    """
    Appends newly generated tasks to the 'Daily Tasks' section, formatted consistently with '⛯'.
    """
    try:
        tasks_section, goals_section = content.split("# 🎯 Goals")
    except ValueError:
        tasks_section = content
        goals_section = ""

    cleaned_suggestions = [task.strip() for task in suggestions.split("\n") if task.strip()]
    formatted_suggestions = "\n".join(f"- [ ] ⛯ {task}" for task in cleaned_suggestions)

    updated_tasks = tasks_section.strip() + "\n" + formatted_suggestions
    updated_content = updated_tasks + "\n# 🎯 Goals" + goals_section

    with open(TASK_FILE, "w") as file:
        file.write(updated_content)

def main():
    """
    Main script workflow:
    1. Initializes the task file if missing or empty.
    2. Reads existing tasks and goals.
    3. Determines the number of new tasks to generate (up to 3 or to reach 6 total).
    4. Generates and appends new tasks if necessary.
    """
    initialize_task_file()  # ✅ Initialize the file if needed and exit
    content = read_tasks()
    tasks = extract_existing_tasks(content)
    goals = extract_goals(content)

    total_incomplete_tasks = len(tasks["user_incomplete"]) + len(tasks["bb_incomplete"])
    tasks_needed = min(6 - total_incomplete_tasks, 3)

    if tasks_needed > 0:
        suggestions = generate_suggestions(goals, tasks, tasks_needed)
        update_task_file(content, suggestions)

if __name__ == "__main__":
    main()
