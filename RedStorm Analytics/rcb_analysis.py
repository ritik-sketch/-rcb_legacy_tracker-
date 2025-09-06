import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/cricket_data_2025.csv")


rcb_df = df[df['Team_Name'] == 'Royal Challengers Bangalore']


top_rcb = rcb_df.groupby('Player_Name')['Runs_Scored'].sum().sort_values(ascending=False).head(10)


plt.figure(figsize=(10,6))
top_rcb.plot(kind='bar', color='crimson')
plt.title("Top 10 RCB Run Scorers (2008–2025)")
plt.xlabel("Player Name")
plt.ylabel("Total Runs")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y')
plt.savefig("visuals/top_rcb_scorers.png")
plt.show()


top_wickets = rcb_df.groupby('Player_Name')['Wickets_Taken'].sum().sort_values(ascending=False).head(10)


plt.figure(figsize=(10,6))
top_wickets.plot(kind='bar', color='darkblue')
plt.title("Top 10 RCB Wicket Takers (2008–2025)")
plt.xlabel("Player Name")
plt.ylabel("Total Wickets")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y')
plt.savefig("visuals/top_rcb_wicket_takers.png")
plt.show()


rcb_centuries = rcb_df.groupby('Player_Name')['Centuries'].sum().sort_values(ascending=False).head(10)


plt.figure(figsize=(10,6))
rcb_centuries.plot(kind='bar', color='orange')
plt.title("Top 10 RCB Century Makers")
plt.xlabel("Player Name")
plt.ylabel("Total Centuries")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y')
plt.savefig("visuals/centuries_comparison.png")
plt.show()