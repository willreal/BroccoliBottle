# BroccoliBottle

**A local, privacy-first productivity SLM task taskbook** that dynamically generates actionable, goal-driven tasks. BroccoliBottle integrates seamlessly with **Markdown-based tools like Obsidian** and runs entirely offline using Microsoft Phi-4 14B via Ollama.

BroccoliBottle is compact, versatile, and packed with value—helping you stay focused and healthy in your productivity habits. Unlike ChatGPT with Tasks, which currently falls short in many ways, BroccoliBottle goes beyond predefined, static prompts. ChatGPT with Tasks simply runs a preset script intermittently, sending intrusive emails or notifications, and worse, it consumes your precious usage tokens with every run. In contrast, BroccoliBottle is open-source, completely offline, and genuinely actionable—it doesn’t just suggest tasks, it actively updates your tasks.md file, seamlessly integrating into your workflow without interruptions or hidden costs. It’s productivity done right: smarter, quieter, and fully under your control.

![SCR-20250120-bqgw](https://github.com/user-attachments/assets/11cfb049-9d49-4d02-b051-5ee3294fb739)

---

## Features

- **Privacy-First:** Runs completely offline using Phi-4 (SLM model) via Ollama.
- **Goal-Driven Task Suggestions:** Dynamically generates tasks tailored to your long-term goals, avoiding redundancy.
- **Lightweight and Customizable:** Works out of the box or can be easily adapted to your needs.
- **Markdown-Based:** Uses a simple, human-readable `tasks.md` file that integrates perfectly with **Obsidian**, the app we recommend for a clean, organized workflow.
- **Silent Automation:** Adds goal-aligned tasks without intrusive notifications.

---

## System Requirements

To run BroccoliBottle, your system must meet the following requirements:

### Operating System:
- macOS (tested and supported)

### Hardware:
- Minimum 16GB of RAM (recommended for running Phi-4 effectively)
- A CPU capable of handling large language model computations (e.g., M1/M2 Mac or equivalent)

### Software:
- **Python 3.9+**
- **Ollama:** Installable via Homebrew for running Phi-4 locally
  ```bash
  brew install ollama
  ```

---

## Installation

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

   The script will initialize a `tasks.md` file in the same directory if it doesn’t already exist.

---

## Why We Recommend Obsidian

Obsidian is like the perfect companion to BroccoliBottle—it organizes your thoughts, tasks, and goals effortlessly, all within a Markdown-based ecosystem. With BroccoliBottle’s simple `tasks.md` file, you can seamlessly integrate your tasks into Obsidian’s clean and intuitive interface.

Download Obsidian for free at [obsidian.md](https://obsidian.md) and start enjoying the healthiness of organized productivity.

---

## Automating BroccoliBottle

Make life even easier by automating BroccoliBottle to run on a schedule—so it silently updates your tasks when you need it most.

### Option 1: Automate with `cron` (macOS)

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

### Option 2: Automate on Obsidian Launch
Use tools like **Keyboard Maestro** or **Automator** to trigger the script when Obsidian is launched. Imagine opening Obsidian and having your tasks automatically updated—it’s like starting your day with a fresh, organized plan.

---

## Example `tasks.md` File

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

## How It Works

1. **Initialization:** On the first run, BroccoliBottle creates a `tasks.md` file if one doesn’t already exist.
2. **Task Suggestions:** Dynamically generates up to 3 tasks based on your defined goals (or enough to reach 6 total tasks).
3. **Goal Alignment:** Creates suggestions directly tied to your long-term priorities—never random, always actionable.

---

## BroccoliBottle Philosophy

Why "BroccoliBottle"? Because it’s:

- **Nutritious for your productivity:** Like broccoli for your body, BroccoliBottle keeps your workflow healthy and goal-driven.
- **Compact and contained:** A bottle holds everything together neatly, just like how BroccoliBottle keeps your tasks and goals in one organized place.
- **Fresh and versatile:** Whether it’s a quick sip of focus or a full meal of productivity, BroccoliBottle adapts to your needs, just like broccoli in any recipe.
- **Sustainable and self-sufficient:** BroccoliBottle runs offline, just like a reusable bottle that keeps your resources in check.

Think of BroccoliBottle as the perfect blend of structure (the bottle) and growth (the broccoli), giving you everything you need to stay productive and organized without waste.  

---

## Contributing

Contributions are welcome! Whether you’d like to add features, fix bugs, or suggest improvements, feel free to open a pull request or issue.

---

## License

This project is licensed under the MIT License.

---

## Why BroccoliBottle?

Unlike existing tools like OpenAI’s ChatGPT with Tasks, BroccoliBottle is:
- **Private:** Runs entirely offline.
- **Goal-Oriented:** Suggestions are personalized to your priorities, not generic prompts.
- **Efficient:** Lightweight, local execution without unnecessary bloat.

---

With BroccoliBottle, your productivity is smart, private, and healthy.

---
