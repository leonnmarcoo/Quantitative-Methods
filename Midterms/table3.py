import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

disadvantaged_groups = [
    'Persons with disability',
    'Senior citizens with ID',
    'Members who are solo parents'
]
populations = [4, 33, 5]

labels = ['Male', 'Female']
pwd_population = [2, 2]
senior_citizen_population = [18, 15]
solo_parents_population = [0, 5]

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
    'Disadvantage Groups',
    fontweight='bold'
)
ax_bar.set_ylabel(
    'Population',
    fontweight='bold'
)
ax_bar.set_ylim(0, max(populations) * 1.15)
ax_bar.set_title('Total Population of the Disadvantage Groups',
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
    pwd_population,
    labels=labels,
    autopct=make_autopct(pwd_population),
    startangle=90,
    colors=pie_colors
)
ax_pie1.axis('equal')
ax_pie1.set_title(
    'Male vs Female: Persons\nwith disability',
    y=-0.1,
    fontweight='bold'

)

ax_pie2 = fig.add_subplot(gs[1, 1])
ax_pie2.pie(
    senior_citizen_population,
    labels=labels,
    autopct=make_autopct(senior_citizen_population),
    startangle=90,
    colors=pie_colors
)
ax_pie2.axis('equal')
ax_pie2.set_title(
    'Male vs Female: Senior\ncitizens with ID',
    y=-0.1,
    fontweight='bold'
)

ax_pie3 = fig.add_subplot(gs[1, 2])
ax_pie3.pie(
    solo_parents_population,
    labels=labels,
    autopct=make_autopct(solo_parents_population),
    startangle=90,
    colors=pie_colors
)
ax_pie3.axis('equal')
ax_pie3.set_title(
    'Male vs Female: Members\nwho are solo parents',
    y=-0.1,
    fontweight='bold'
)

fig.suptitle(
    'Table 3: Disadvantaged Groups',
    fontsize=16,
    fontweight='bold'
)
plt.tight_layout(rect=[0, 0, 1, 0.93])

plt.show()