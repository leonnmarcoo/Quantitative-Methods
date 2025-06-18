import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

labor_force_group = [
    'Employed members of the labor force',
    'Unemployed members of the labor force',
    'Underemployed workers'
]
populations = [236, 8, 31]

labels = ['Male', 'Female']
employed_population = [170, 66]
unemployed_population = [5, 3]
underemployed_population = [24, 7]

fig = plt.figure(figsize=(10, 8))
gs = GridSpec(2, 3, figure=fig)

ax_bar = fig.add_subplot(gs[0, :])
bars = ax_bar.bar(labor_force_group, populations, color='#FDB45C')
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
    'Labor Force Group',
    fontweight='bold'
)
ax_bar.set_ylabel(
    'Population',
    fontweight='bold'
)
ax_bar.set_ylim(0, max(populations) * 1.15)
ax_bar.set_title('Total Population of the Labor Force',
                 fontweight='bold'
)

pie_colors = ['#FDB45C', '#F7464A']

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return f'{val} ({pct:.1f}%)'
    return my_autopct

ax_pie1 = fig.add_subplot(gs[1, 0])
ax_pie1.pie(
    employed_population,
    labels=labels,
    autopct=make_autopct(employed_population),
    startangle=90,
    colors=pie_colors
)
ax_pie1.axis('equal')
ax_pie1.set_title(
    'Male vs Female: Employed\nmembers of the labor force',
    y=-0.2,
    fontweight='bold'

)

ax_pie2 = fig.add_subplot(gs[1, 1])
ax_pie2.pie(
    unemployed_population,
    labels=labels,
    autopct=make_autopct(unemployed_population),
    startangle=90,
    colors=pie_colors
)
ax_pie2.axis('equal')
ax_pie2.set_title(
    'Male vs Female: Unemployed\nmembers of the labor force',
    y=-0.2,
    fontweight='bold'
)

ax_pie3 = fig.add_subplot(gs[1, 2])
ax_pie3.pie(
    underemployed_population,
    labels=labels,
    autopct=make_autopct(underemployed_population),
    startangle=90,
    colors=pie_colors
)
ax_pie3.axis('equal')
ax_pie3.set_title(
    'Male vs Female: Underemployed\nworkers',
    y=-0.2,
    fontweight='bold'
)

fig.suptitle(
    'Table 2.3: Labor Force',
    fontsize=16,
    fontweight='bold'
)
plt.tight_layout(rect=[0, 0, 1, 0.93])

plt.show()