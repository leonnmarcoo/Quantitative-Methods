import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

population_group = [
    'Total Population',
    'Resident Population'
]
populations = [605, 583]

labels = ['Male', 'Female']
total_population_count = [302, 303]
resident_population_count = [298, 285]

fig = plt.figure(figsize=(10, 8))
gs = GridSpec(2, 2, figure=fig)

ax_bar = fig.add_subplot(gs[0, :])
bars = ax_bar.bar(population_group, populations, color='#FDB45C')
for bar in bars:
    height = bar.get_height()
    ax_bar.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.1,
        f'{height}',
        ha='center',
        va='bottom'
    )

ax_bar.set_xlabel(
    'Population Group',
    fontweight='bold'
)
ax_bar.set_ylabel(
    'Population',
    fontweight='bold'
)
ax_bar.set_ylim(0, max(populations) * 1.15)
ax_bar.set_title('Total Population vs Resident Population',
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
    total_population_count,
    labels=labels,
    autopct=make_autopct(total_population_count),
    startangle=90,
    colors=pie_colors
)
ax_pie1.axis('equal')
ax_pie1.set_title(
    'Male vs Female: Total Population',
    y=-0.1,
    fontweight='bold'

)

ax_pie2 = fig.add_subplot(gs[1, 1])
ax_pie2.pie(
    resident_population_count,
    labels=labels,
    autopct=make_autopct(resident_population_count),
    startangle=90,
    colors=pie_colors
)
ax_pie2.axis('equal')
ax_pie2.set_title(
    'Male vs Female: Resident Population',
    y=-0.1,
    fontweight='bold'
)

fig.suptitle(
    'Table 2.1: Demographic Breakdown of Total Population & Resident Population',
    fontsize=16,
    fontweight='bold'
)
plt.tight_layout(rect=[0, 0, 1, 0.93])

plt.show()