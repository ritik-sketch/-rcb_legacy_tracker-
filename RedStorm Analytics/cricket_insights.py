import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/cricket_data_2025.csv")


top_runs = df.groupby('Player_Name')['Runs_Scored'].sum().sort_values(ascending=False).head(10)


plt.figure(figsize=(10,6))
top_runs.plot(kind='bar', color='green')
plt.title("Top 10 IPL Run Scorers (2008–2025)")
plt.xlabel("Player Name")
plt.ylabel("Total Runs")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y')
plt.savefig("visuals/top_ipl_run_scorers.png")
plt.show()



top_wickets_ipl = df.groupby('Player_Name')['Wickets_Taken'].sum().sort_values(ascending=False).head(10)


plt.figure(figsize=(10,6))
top_wickets_ipl.plot(kind='bar', color='purple')
plt.title("Top 10 IPL Wicket Takers (2008–2025)")
plt.xlabel("Player Name")
plt.ylabel("Total Wickets")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y')
plt.savefig("visuals/top_ipl_wicket_takers.png")
plt.show()



top_wickets_ipl = df.groupby('Player_Name')['Wickets_Taken'].sum().sort_values(ascending=False).head(10)


plt.figure(figsize=(10,6))
top_wickets_ipl.plot(kind='bar', color='purple')
plt.title("Top 10 IPL Wicket Takers (2008–2025)")
plt.xlabel("Player Name")
plt.ylabel("Total Wickets")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y')
plt.savefig("visuals/top_ipl_wicket_takers.png")
plt.show()


team_centuries = df.groupby('Team_Name')['Centuries'].sum().sort_values(ascending=False).head(10)


plt.figure(figsize=(10,6))
team_centuries.plot(kind='bar', color='teal')
plt.title("Top 10 IPL Teams by Total Centuries")
plt.xlabel("Team Name")
plt.ylabel("Total Centuries")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y')
plt.savefig("visuals/ipl_team_centuries.png")
plt.show()