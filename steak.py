import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set consistent look for all charts
sns.set_theme(style="whitegrid")

# Load and clean the data
df = pd.read_csv("steak.csv")
df = df.iloc[1:].copy() # Drop the first row which contains survey sub-headers

# Focus on the two categorical variables
col_steak = 'How do you like your steak prepared?'
col_gender = 'Gender'
df_clean = df.dropna(subset=[col_steak, col_gender]).copy()

# Order the categories logically
steak_order = ["Rare", "Medium rare", "Medium", "Medium Well", "Well"]
df_clean[col_steak] = pd.Categorical(df_clean[col_steak], categories=steak_order)

# Generate a relative frequency table (%) to ensure a fair comparison
rel_pct = (pd.crosstab(df_clean[col_steak], df_clean[col_gender], normalize="columns") * 100).round(1)

# Reshape the relative frequency table for seaborn
rel_long = (
    rel_pct
    .reset_index()
    .melt(id_vars=col_steak, var_name="Gender", value_name="percent")
)

# Print the analysis findings to the terminal
print("--- RELATIVE FREQUENCY (%) ---")
print(rel_pct)
print("\n--- CONCLUSION ---")
print("Both genders share a very similar preference for 'Medium rare' steak, which is the mode for both groups.")
print("However, males have a noticeably higher share of respondents who prefer 'Medium' steak.")
print("Conversely, females have a higher relative frequency for 'Well' done and 'Medium Well' steaks.")

# Generate and display the grouped bar chart
plt.figure(figsize=(10, 6))
ax = sns.barplot(
    data=rel_long, x=col_steak, y="percent",
    hue="Gender", order=steak_order,
    hue_order=["Female", "Male"],
    palette="Set2"
)
ax.set_title("Preferred Steak Preparation by Gender — RELATIVE FREQUENCY")
ax.set_xlabel("Steak Preparation")
ax.set_ylabel("Percent of respondents (%)")
ax.legend(title="Gender")
plt.tight_layout()

# Save the chart image to the working directory
plt.savefig("steak_preparation_by_gender.png", dpi=200, bbox_inches="tight")

# Show the plot
plt.show()


