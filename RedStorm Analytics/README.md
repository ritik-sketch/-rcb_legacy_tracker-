**RCB Legacy Tracer & Redstrom Analysis — Cricket Analytics Portfolio**

This project began as a deep dive into Virat Kohli’s IPL journey with Royal Challengers Bangalore, and gradually expanded into a broader cricket analytics dashboard. It now includes player-level, team-level, and league-wide comparisons — covering centuries, match impact, and career trajectories of top IPL performers.

I built this project to sharpen my Python skills, improve my portfolio presentation, and tell compelling stories through cricket data.

---

##  Folder Structure
rcb_legacy_tracer/ ├── data/                  # Raw and cleaned CSVs ├── visuals/               # All saved .png graphs ├── utils/                 # Custom plotting functions ├── notebooks/             # Jupyter notebooks (e.g. cricket.ipynb) └── README.md              # Project summary
redstrom_analysis/ ├── data/                  # Extended player/team stats ├── visuals/               # Global or cross-team comparisons ├── notebooks/             # Advanced comparisons (e.g. Kohli vs Rohit)

---

##  Key Features

###  Kohli Year-wise Performance
- Aggregated runs, average, and strike rate from 2008–2024
- Modular plotting function with clean visuals

###  Kohli vs Rohit Century Comparison
- Bar chart showing IPL century dominance

###  Team-Level Century Analysis
- Top 10 IPL teams ranked by total centuries
- Highlights batting-heavy franchises

###  Kohli vs All-Time IPL Century Leaders
- Comparison with Buttler, Gayle, KL Rahul, etc.

###  Modular Codebase
- Plotting functions stored in `kohli_plot_utils.py` and `team_plot_utils.py`
- Reusable across players and metrics

---

Technologies Used

- **Python** (Pandas, Matplotlib)
- **Jupyter Notebook** for analysis and storytelling
- **Modular scripting** with `.py` utility files
- **Data cleaning** using `pd.to_numeric()` and `pd.to_datetime()`
- **Visual storytelling** with `.png` exports for GitHub and interviews

---

# How to Run This Project

# 1. Clone the Repository

```bash
git clone https://github.com/your-username/rcb-legacy-tracer.git
cd rcb_legacy_tracer

Install Dependencies
pip install -r requirements.txt


3. Launch Jupyter Notebook
jupyter notebook notebooks/cricket.ipynb


4. Run Cells Step-by-Step
- Start with Kohli analysis
- Move to team-level comparisons
- Explore century leader visuals
- All graphs will be saved in visuals/ folder


Requirements
pandas
matplotlib


You can install them manually if needed:
pip install pandas matplotlib


 What I Learned
- How to modularize plotting logic for clean reuse
- How to structure notebooks for recruiter readability
- How to extract insights from raw cricket data
- How to present visuals that tell a story — not just numbers
