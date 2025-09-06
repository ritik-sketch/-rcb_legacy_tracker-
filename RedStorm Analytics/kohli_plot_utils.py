import matplotlib.pyplot as plt

def plot_kohli_yearly_performance(df, save_path="visuals/kohli_performance.png"):
    """
    Plots Virat Kohli's IPL performance from 2008 to 2024.
    Shows total runs, batting average, and strike rate per year.
    
    Parameters:
    df (DataFrame): Year-wise Kohli stats
    save_path (str): Path to save the output .png file
    """
    plt.figure(figsize=(10,6))
    plt.plot(df['Year'], df['Runs_Scored'], label='Runs', marker='o')
    plt.plot(df['Year'], df['Batting_Average'], label='Average', marker='s')
    plt.plot(df['Year'], df['Batting_Strike_Rate'], label='Strike Rate', marker='^')
    plt.title("Virat Kohli Year-wise Performance (2008–2024)")
    plt.xlabel("Year")
    plt.ylabel("Stats")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()