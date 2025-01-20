# BroccoliBottle

**A smarter, privacy-first productivity assistant** that dynamically generates actionable, goal-driven tasks. Designed for high-performance individuals, BroccoliBottle integrates seamlessly with Markdown-based tools like Obsidian and runs entirely offline using Microsoft Phi-4 via Ollama.

---

## **Features**

- **Privacy-First:** Runs completely offline using Phi-4 (SLM model) via Ollama.
- **Goal-Driven Task Suggestions:** Dynamically generates tasks based on your long-term goals.
- **Lightweight and Customizable:** Works out of the box or can be easily configured for specific workflows.
- **Markdown-Based:** Uses a simple, human-readable `tasks.md` file for seamless integration with tools like Obsidian.
- **Silent Automation:** Append goal-aligned tasks to your list without intrusive notifications.

---

## **System Requirements**

To run BroccoliBottle, your system must meet the following requirements:

### **Operating System:**
- macOS (tested and supported)

### **Hardware:**
- Minimum 16GB of RAM (recommended for running Phi-4 effectively)
- A CPU capable of handling large language model computations (e.g., M1/M2 Mac or equivalent)

### **Software:**
- **Python 3.9+**
- **Ollama:** Installable via Homebrew for running Phi-4 locally
  ```bash
  brew install ollama
  ```

---

## **Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/willreal/BroccoliBottle.git
   cd BroccoliBottle
   ```

2. **Install Dependencies**
   Ensure you have Ollama installed and the Phi-4 model downloaded:
   ```bash
   brew install ollama
   ollama pull phi4
   ```

3. **Run the Script**
   ```bash
   python3 broccoli_bottle.py
   ```

   The script will initialize a `tasks.md` file in the same directory as the script if it doesn’t already exist.

---

## **Customizing the File Path**

If you prefer to use a custom file location (e.g., a file within Obsidian), update the `TASK_FILE` variable in the `broccoli_bottle.py` script:

```python
TASK_FILE = "/path/to/your/custom/tasks.md"
```

---

## **Automating the Script**

You can automate the script to run at regular intervals, such as every day at 8 AM, every Monday, or whenever you launch Obsidian.

### **Option 1: Automate with `cron` (macOS)**

1. Open the `crontab` editor:
   ```bash
   crontab -e
   ```

2. Add a line to schedule the script. For example:
   - Run every day at 8 AM:
     ```bash
     0 8 * * * /usr/bin/python3 /path/to/broccoli_bottle.py
     ```
   - Run every weekday at 8 AM:
     ```bash
     0 8 * * 1-5 /usr/bin/python3 /path/to/broccoli_bottle.py
     ```
   - Run every Monday at 8 AM:
     ```bash
     0 8 * * 1 /usr/bin/python3 /path/to/broccoli_bottle.py
     ```

### **Option 2: Automate on Obsidian Launch**
Use tools like **Keyboard Maestro** or **Automator** to trigger the script when Obsidian is launched. This is particularly useful for those who prefer task updates only when using Obsidian.

---

## **Example `tasks.md` File**

```markdown
# 📅 Daily Tasks
- [ ] e.g. Run 4km today on the treadmill.
- [ ] Write your personal tasks here to stay organized.
- [ ] BroccoliBottle will also automatically suggest up to 3 tasks (or enough to reach 6 total).
- [ ] Stay consistent and check off tasks as you complete them.

# 🎯 Goals
- e.g. Train to run a 10km trail by summer.
- Define specific and clear goals to guide BroccoliBottle's suggestions.
- The more detailed your goals, the better the recommendations.
- Use this section to give BroccoliBottle context for your priorities.
```

---

## **How It Works**

1. **Initialization:** On the first run, BroccoliBottle creates a `tasks.md` file if it doesn’t exist.
2. **Task Suggestions:** Generates up to 3 new tasks based on your defined goals (or enough to reach 6 total tasks).
3. **Goal Alignment:** Dynamically creates suggestions directly tied to your long-term goals, avoiding redundancy.

---

## **Contributing**

Contributions are welcome! If you’d like to improve BroccoliBottle, feel free to open a pull request or submit an issue.

---

## **License**

This project is licensed under the MIT License.

---

## **Why BroccoliBottle?**

Unlike existing tools like OpenAI’s ChatGPT with Tasks, BroccoliBottle is:
- **Private:** Runs entirely offline.
- **Goal-Oriented:** Suggestions are based on your personal priorities, not generic prompts.
- **Efficient:** Lightweight and runs locally without unnecessary bloat.

---

With BroccoliBottle, your productivity stays smart, private, and focused.
