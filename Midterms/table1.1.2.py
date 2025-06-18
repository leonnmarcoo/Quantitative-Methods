import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

age_groups = [
    'Members 9 years old and below',
    'Members 10 years old and above'
]
populations = [127, 456]

labels = ['Male', 'Female']
members_counts = [233, 223]

fig, (ax_bar, ax_pie) = plt.subplots(1, 2, figsize=(12, 5))

bars = ax_bar.bar(age_groups, populations, color='#FDB45C')
for bar in bars:
    height = bar.get_height()
    ax_bar.text(
        bar.get_x() + bar.get_width() / 2,
        height + 5,
        f'{height}',
        ha='center',
        va='bottom'
    )
ax_bar.set_xlabel(
    'Age Group',
    fontweight='bold'
)
ax_bar.set_ylabel(
    'Population',
    fontweight='bold'
)
ax_bar.set_ylim(0, max(populations) * 1.15)
ax_bar.set_title(
    'Total Population',
    fontweight='bold'
)

pie_colors = ['#FDB45C', '#F7464A']

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return f'{val} ({pct:.1f}%)'
    return my_autopct

ax_pie.pie(
    members_counts,
    labels=labels,
    autopct=make_autopct(members_counts),
    startangle=90,
    colors=pie_colors
)
ax_pie.axis('equal')
ax_pie.set_title(
    'Male vs Female Members: 10 years old and above',
    y=-0.1,
    fontweight='bold'
)

fig.suptitle(
    'Table 1.1.2: Demographic Breakdown of Members 10 years old and above',
    fontsize=16,
    fontweight='bold'
)

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()