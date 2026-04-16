import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Read the CSV file
df = pd.read_csv("health_data.csv")

print("Dataset loaded successfully!")
print(f"Shape: {df.shape}")
print(df.head())

# Map gender to numeric for scatter plotting
df['gender_numeric'] = df['Gender'].map({'Male': 1, 'Female': 0})

# Create a figure with 5 subplots (arranged in 2 rows, 3 columns)
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle("Health Data - Scatter Plots", fontsize=16, fontweight='bold')

# Color map for gender
colors = df['Gender'].map({'Male': 'steelblue', 'Female': 'salmon'})

#Weight vs Height
axes[0, 0].scatter(df['Height'], df['Weight'], c=colors, alpha=0.6, edgecolors='k', linewidths=0.4)
axes[0, 0].set_xlabel("Height")
axes[0, 0].set_ylabel("Weight")
axes[0, 0].set_title("Weight vs Height")

#Age vs Weight
axes[0, 1].scatter(df['Age'], df['Weight'], c=colors, alpha=0.6, edgecolors='k', linewidths=0.4)
axes[0, 1].set_xlabel("Age")
axes[0, 1].set_ylabel("Weight")
axes[0, 1].set_title("Age vs Weight")

#Height vs Age
axes[0, 2].scatter(df['Age'], df['Height'], c=colors, alpha=0.6, edgecolors='k', linewidths=0.4)
axes[0, 2].set_xlabel("Age")
axes[0, 2].set_ylabel("Height")
axes[0, 2].set_title("Height vs Age")

#Gender vs Height
axes[1, 0].scatter(df['gender_numeric'], df['Height'], c=colors, alpha=0.6, edgecolors='k', linewidths=0.4)
axes[1, 0].set_xlabel("Gender (0=Female, 1=Male)")
axes[1, 0].set_ylabel("Height")
axes[1, 0].set_title("Gender vs Height")
axes[1, 0].set_xticks([0, 1])
axes[1, 0].set_xticklabels(['Female', 'Male'])

#Gender vs Weight
axes[1, 1].scatter(df['gender_numeric'], df['Weight'], c=colors, alpha=0.6, edgecolors='k', linewidths=0.4)
axes[1, 1].set_xlabel("Gender (0=Female, 1=Male)")
axes[1, 1].set_ylabel("Weight")
axes[1, 1].set_title("Gender vs Weight")
axes[1, 1].set_xticks([0, 1])
axes[1, 1].set_xticklabels(['Female', 'Male'])

# Legend for gender colors
from matplotlib.lines import Line2D # type: ignore
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='steelblue', markersize=8, label='Male'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='salmon', markersize=8, label='Female')
]
fig.legend(handles=legend_elements, loc='lower right', fontsize=11)

# Hide unused 6th subplot
axes[1, 2].set_visible(False)

plt.tight_layout()
plt.savefig("health_scatter_plots.png", dpi=150, bbox_inches='tight')
plt.show()
print("Scatter plots saved as 'health_scatter_plots.png'")