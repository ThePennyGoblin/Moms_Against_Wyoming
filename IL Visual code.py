# Adjusting the legend to be more opaque, so the 60-Day line does not show through

fig, ax = plt.subplots(figsize=(8, 5))  # Keeping reduced width

# Setting up x limits for the timeline, representing days
ax.set_xlim(0, 70)
ax.set_ylim(0, 3)

# Removing y ticks and labels for simplicity
ax.set_yticks([])

# Adding title
ax.set_title("MLB Injured Lists Timeline", fontsize=14, fontweight='bold')

# Drawing horizontal lines representing the time periods for each IL
ax.hlines(y=2.5, xmin=0, xmax=7, color='lightblue', linewidth=8, label="7-Day IL")
ax.hlines(y=1.5, xmin=0, xmax=10, color='lightgreen', linewidth=8, label="10-Day IL")
ax.hlines(y=0.5, xmin=0, xmax=15, color='lightcoral', linewidth=8, label="15-Day IL")
ax.hlines(y=-0.5, xmin=0, xmax=60, color='gold', linewidth=8, label="60-Day IL")

# Adding labels to each injured list line
ax.text(1, 2.7, "7-Day IL (concussions)", fontsize=10, verticalalignment='center')
ax.text(1, 1.7, "10-Day IL (position players)", fontsize=10, verticalalignment='center')
ax.text(1, 0.7, "15-Day IL (pitchers, two-way players)", fontsize=10, verticalalignment='center')
ax.text(1, -0.3, "60-Day IL (all players, 40-man roster)", fontsize=10, verticalalignment='center', fontweight='bold')

# Adding details about backdating rules with small markers
ax.plot([6, 7], [2.5, 2.5], color='black', marker='o', markersize=5, label='Max backdating')
ax.plot([7, 10], [1.5, 1.5], color='black', marker='o', markersize=5)
ax.plot([12, 15], [0.5, 0.5], color='black', marker='o', markersize=5)

# Adding a distinct line across for the 60-Day IL for visual clarity
ax.vlines(x=60, ymin=-0.8, ymax=2.8, color='gold', linewidth=2, linestyle="--", label='60-Day Mark')

# Creating a more opaque legend
legend = ax.legend(loc='upper right', frameon=True)
legend.get_frame().set_alpha(0.9)  # Making the legend more opaque

# Display the timeline
plt.tight_layout()
plt.show()
