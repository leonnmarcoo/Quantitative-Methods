import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

disadvantaged_groups = [
    'Households engaged in agriculture',
    'Households engaged in livestock raising',
    'Households engaged in fishing'
]
populations = [88, 24, 0]

labels = ['Engaged', 'Not Engaged']
agriculture_population = [88, 79]
livestock_raising_population = [24, 143]
fishing_population = [0, 167]

fig = plt.figure(figsize=(10, 8))
gs = GridSpec(2, 3, figure=fig)

ax_bar = fig.add_subplot(gs[0, :])
bars = ax_bar.bar(disadvantaged_groups, populations, color='#FDB45C')
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
    'Household Groups',
    fontweight='bold'
)
ax_bar.set_ylabel(
    'Number of Household',
    fontweight='bold'
)
ax_bar.set_ylim(0, max(populations) * 1.15)
ax_bar.set_title('Total Population of Livelihhod Household',
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
    agriculture_population,
    labels=labels,
    autopct=make_autopct(agriculture_population),
    startangle=90,
    colors=pie_colors
)
ax_pie1.axis('equal')
ax_pie1.set_title(
    'Engaged vs Not Engaged:\nHouseholds engaged in\nagriculture',
    y=-0.3,
    fontweight='bold'
)

ax_pie2 = fig.add_subplot(gs[1, 1])
ax_pie2.pie(
    livestock_raising_population,
    labels=labels,
    autopct=make_autopct(livestock_raising_population),
    startangle=90,
    colors=pie_colors
)
ax_pie2.axis('equal')
ax_pie2.set_title(
    'Engaged vs Not Engaged:\nHouseholds engaged in\nlivestock raising',
    y=-0.3,
    fontweight='bold'
)

ax_pie3 = fig.add_subplot(gs[1, 2])
ax_pie3.pie(
    fishing_population,
    labels=labels,
    autopct=make_autopct(fishing_population),
    startangle=90,
    colors=pie_colors
)
ax_pie3.axis('equal')
ax_pie3.set_title(
    'Engaged vs Not Engaged:\nHouseholds engaged in\nfishing',
    y=-0.3,
    fontweight='bold'
)

fig.suptitle(
    'Table 4: Livelihood',
    fontsize=16,
    fontweight='bold'
)
plt.tight_layout(rect=[0, 0, 1, 0.93])

plt.show()