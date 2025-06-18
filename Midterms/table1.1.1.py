import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

age_groups = [
    'Children 0–5 years',
    'Members 6–16 years',
    'Members 17+ years'
]
populations = [64, 145, 374]

labels = ['Male', 'Female']
children_counts = [34, 30]
members_counts = [71, 74]

fig = plt.figure(figsize=(10, 8))
gs = GridSpec(2, 2, figure=fig)

ax_bar = fig.add_subplot(gs[0, :])
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
ax_bar.set_title('Total Population',
                 fontweight='bold'
)

ax_pie1 = fig.add_subplot(gs[1, 0]) 

pie_colors = ['#FDB45C', '#F7464A']

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return f'{val} ({pct:.1f}%)'
    return my_autopct

ax_pie1.pie(
    children_counts,
    labels=labels,
    autopct=make_autopct(children_counts),
    startangle=90,
    colors=pie_colors
)
ax_pie1.axis('equal')
ax_pie1.set_title(
    'Male vs Female: Children 0–5 years',
    y=-0.1,
    fontweight='bold'

)

ax_pie2 = fig.add_subplot(gs[1, 1])
ax_pie2.pie(
    members_counts,
    labels=labels,
    autopct=make_autopct(members_counts),
    startangle=90,
    colors=pie_colors
)
ax_pie2.axis('equal')
ax_pie2.set_title(
    'Male vs Female: Members 6–16 years',
    y=-0.1,
    fontweight='bold'
)

fig.suptitle(
    'Table 1.1.1: Demographic Breakdown of Population',
    fontsize=16,
    fontweight='bold'
)
plt.tight_layout(rect=[0, 0, 1, 0.93])

plt.show()