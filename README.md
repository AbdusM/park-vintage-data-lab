# Park Vintage Data Lab
**GitHub repo:** https://github.com/AbdusM/park-vintage-data-lab

Park Vintage is a small clothing store with messy inventory and sales data.

Your job is to help the owner answer practical business questions using the command line, Python, SQL, Jupyter notebooks, GitHub, and Codex.

This project is designed for beginners. You do not need to know Python, SQL, or the terminal before starting.

## What this project is

Park Vintage Data Lab is a guided, beginner-friendly project for learning essential data workflows in one place.

You will move through realistic tasks like cleaning inventory data, joining sales with products, running SQL, and writing a short business report.

## Who this is for

- Beginners learning command line basics
- People learning Python, pandas, and SQL at the same time
- Early analysts building portfolio projects
- Mentors teaching intro data workflows

## The story: Park Vintage

Park Vintage sells vintage clothing from limited stock. Data comes from three sources:

- Inventory records
- Sales transactions
- Product and customer metadata

The store owner wants answers to questions like:

- What is selling the best?
- What is overstocked?
- Where are margins healthy or weak?

## What you will learn

- Navigate folders in the terminal
- Set up and use a Python virtual environment
- Install dependencies
- Use JupyterLab
- Load and inspect CSV files with pandas
- Make simple charts in a notebook
- Run SQL queries against SQLite
- Build small scripts and notebooks
- Work with Git checkpoints
- Use Codex safely in your workflow

## What you need installed

You need:

- Python 3.10+
- Git
- `npm` (for Codex install) or Homebrew on macOS
- Internet access for package installation

## Step 1: Download the project

```bash
# macOS/Linux
git clone https://github.com/AbdusM/park-vintage-data-lab.git
cd park-vintage-data-lab
```

```powershell
# Windows
git clone https://github.com/AbdusM/park-vintage-data-lab.git
cd park-vintage-data-lab
```

## Step 2: Learn basic terminal commands

From inside the project folder, try:

```bash
pwd
ls
cd data
ls
cd raw
ls
cd ../..
```

## Step 3: Set up Python

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Step 4: Launch JupyterLab

```bash
jupyter lab
```

You should see the notebook files in `notebooks/`.

## Step 5: Explore the inventory data

Open `notebooks/02_python_inventory_basics.ipynb` and load `data/raw/inventory.csv`.

## Step 6: Run your first SQL query

Open `notebooks/04_sql_for_store_data.ipynb`.

## Install Codex in your terminal

```bash
npm i -g @openai/codex
codex
```

Alternative:

```bash
brew install codex
codex
```

Create a local checkpoint before asking Codex to edit files:

```bash
git status
git add .
git commit -m "Checkpoint before using Codex"
```

Codex can edit files in your project, so make a Git checkpoint before and after using it.

## Use Codex safely

- Ask for explanations before changes.
- Ask for line-by-line walkthroughs.
- Use small prompts and review every diff.
- Commit only what you want to keep.

## Review Codex changes

```bash
git diff
```

## Beginner Codex prompts

```text
Explain this project to me like I am new to Python, SQL, and the command line.

Explain what src/clean_inventory.py does, line by line.

Add beginner-friendly comments to src/clean_inventory.py.

Create a new SQL query that shows sales by brand.

Review my report and suggest clearer business recommendations.
```

## Practice missions

### Mission 0: Project setup

- Clone repository
- Create virtual environment
- Install requirements
- Launch JupyterLab

Acceptance criteria:

- Learner can open the repo folder
- Learner can run JupyterLab
- Learner can open the first notebook

### Mission 1: Learn terminal navigation

Find `data/raw/inventory.csv` using only terminal commands.

### Mission 2: Load inventory data with Python

Use `notebooks/02_python_inventory_basics.ipynb`.

### Mission 3: Analyze sales

Use `notebooks/03_sales_analysis_with_pandas.ipynb`. This notebook includes an optional first chart using `matplotlib`.

### Mission 4: Learn SQL with store data

Use files in `sql/` and `notebooks/04_sql_for_store_data.ipynb`.

### Mission 5: Build ETL pipeline

Run `src/clean_inventory.py`.

### Mission 6: Build a simple report

Create `reports/my_first_park_vintage_report.md` using at least three findings.

### Mission 7: Use Codex safely

Review a file, request a small enhancement, then use `git diff` and commit accepted changes.

## How to know you are done

- You can create environment and launch JupyterLab
- You can load a CSV and show `.head()` and `.shape`
- You can run one SQL query
- You can build a SQLite database
- You can write a short markdown report
- You can install and run `codex`
- You can review and commit changes from Codex safely

## Contributing

See `CONTRIBUTING.md`.

## Good first issues

- Add a SQL exercise for sales by brand
- Improve Windows setup notes for older systems
- Add a glossary for terminal commands
- Add screenshots for JupyterLab setup
- Add a short notebook on profit margin
