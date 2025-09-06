##RCB Legacy Tracker & RedStorm Analysis — Cricket Analytics Portfolio

#  RCB Legacy Tracker

**Author:** [ritik-sketch](https://github.com/ritik-sketch)  
**GitHub Profile:** https://github.com/ritik-sketch
---

📌 Created by [ritik-sketch](https://github.com/ritik-sketch) 

[![GitHub Profile](https://img.shields.io/badge/GitHub-ritik--sketch-blue?logo=github)](https://github.com/ritik-sketch) 

##  Live Project

View the live dashboard here:  
 [RCB Legacy Tracker GitHub Pages](https://ritik-sketch.github.io/-rcb_legacy_tracker-/)


📧 Contact: ritikchaturvedi.knp@gmail.com
##  Objective
To analyze Virat Kohli’s IPL journey with RCB and expand into team-level and league-wide cricket insights using Python and MySQL.

##  Dataset
- `cricket_IPL.csv`: Player-level IPL stats
- `player_team_mapping.csv`: Team associations
- Kohli’s year-wise performance (2008–2024)

##  Key Analysis
- Kohli’s peak years and consistency
- Kohli vs Rohit century comparison
- RCB’s top century scorers
- IPL team-wise century leaderboard

##  Visualizations
- `kohli_performance.png`: Line chart of runs, average, strike rate
- `rcb_century_leaders.png`: Bar chart of top RCB scorers
- `ipl_trophy_count.png`: Team-wise trophy comparison
- All visuals saved in `visuals/` folder

##  Tools Used
- Python (Pandas, Matplotlib)
- Jupyter Notebook
- Modular `.py` plotting scripts
- MySQL backend (via SQLAlchemy)

##  How to Run
```bash
git clone https://github.com/ritik-sketch/-rcb_legacy_tracker-.git
cd RedStorm Analytics
pip install -r requirements.txt
jupyter notebook rcb_analysis.ipynb

Start with Kohli analysis
- Move to team-level comparisons
- Explore century leader visuals
- All graphs will be saved in visuals/ folder




##Installation
- Virtual environment setup
- Dependencies: pandas, matplotlib, sqlalchemy, pymysql
- MySQL Workbench for backend storage
Launch Jupyter Notebook
jupyter notebook notebooks/cricket.ipynb




## Problems Faced
- SQLAlchemy connection errors
- DataFrame length mismatches
- CRLF vs LF warnings (Windows line endings)
- Git push blocked due to email privacy (GH007)


## Plot Descriptions
- Kohli graph: Blue = Runs, Orange = Average, Green = Strike Rate
- Century comparison: Kohli vs Rohit vs Gayle vs Buttler
- Team-level bar charts: Sorted by total centuries


## Future Visuals
- Kohli vs opposition breakdown
- RCB win-loss trends
- Interactive dashboard (Streamlit or Plotly)


##What I Learned
- How to modularize plotting logic for clean reuse
- How to structure notebooks for recruiter readability
- How to extract insights from raw cricket data
- How to present visuals that tell a story — not just numbers
