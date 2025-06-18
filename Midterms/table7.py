import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import textwrap

economic_activity_groups = [
    'Garbage collected',
    'Garbage burned',
    'Garbage composted',
    'Garbage recycled',
    'Garbage segregated',
    'Garbage dumped to closed pit',
    'Garbage dumped to open pit',
    'Other waste management'
]
populations = [11, 40, 97, 83, 75, 13, 87, 0]

wrapped_labels = [
    "\n".join(textwrap.wrap(label, 20))
    for label in economic_activity_groups
]

labels = ['Do', 'Dont']
collected_population = [11, 156]
burned_population = [40, 127]
composted_population = [97, 70]
recycled_population = [83, 84]
segregated_population = [75, 92]
closed_pit_population = [13, 154]
open_pit_population = [87, 80]
other_population = [0, 167]

fig = plt.figure(figsize=(16, 10), constrained_layout=True)
gs = GridSpec(3, 4, figure=fig, height_ratios=[4, 2, 2])

ax_bar = fig.add_subplot(gs[0, :])
bars = ax_bar.bar(wrapped_labels, populations, color='#FDB45C')
for bar in bars:
    height = bar.get_height()
    ax_bar.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0,
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
ax_bar.set_title('Total Population of Waste Management',
                 fontweight='bold'
)

pie_colors = ['#FDB45C', '#F7464A']

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return f'{val} ({pct:.1f}%)'
    return my_autopct

fig.patch.set_facecolor('#FFFFFF')

ax_pie1 = fig.add_subplot(gs[1, 0])
ax_pie1.pie(
    collected_population,
    labels=labels,
    autopct=make_autopct(collected_population),
    startangle=90,
    colors=pie_colors
)
ax_pie1.axis('equal')
ax_pie1.set_title(
    'Do vs Dont:\nGarbage collected',
    y=-0.2,
    fontsize=10,
    fontweight='bold'

)

ax_pie2 = fig.add_subplot(gs[1, 1])
ax_pie2.pie(
    burned_population,
    labels=labels,
    autopct=make_autopct(burned_population),
    startangle=90,
    colors=pie_colors
)
ax_pie2.axis('equal')
ax_pie2.set_title(
    'Do vs Dont:\nGarbage burned',
    y=-0.2,
    fontsize=10,
    fontweight='bold'
)

ax_pie3 = fig.add_subplot(gs[1, 2])
ax_pie3.pie(
    composted_population,
    labels=labels,
    autopct=make_autopct(composted_population),
    startangle=90,
    colors=pie_colors
)

ax_pie3.axis('equal')
ax_pie3.set_title(
    'Do vs Dont:\nGarbage composted',
    fontsize=10,
    y=-0.2,
    fontweight='bold'
)

ax_pie4 = fig.add_subplot(gs[1, 3])
ax_pie4.pie(
    recycled_population,
    labels=labels,
    autopct=make_autopct(recycled_population),
    startangle=90,
    colors=pie_colors
)
ax_pie4.axis('equal')
ax_pie4.set_title(
    'Do vs Dont:\nGarbage recycled',
    y=-0.2,
    fontsize=10,
    fontweight='bold'
)

ax_pie5 = fig.add_subplot(gs[2, 0])
ax_pie5.pie(
    segregated_population,
    labels=labels,
    autopct=make_autopct(segregated_population),
    startangle=90,
    colors=pie_colors
)
ax_pie5.axis('equal')
ax_pie5.set_title(
    'Do vs Dont:\nGarbage segregated',
    y=-0.2,
    fontsize=10,
    fontweight='bold'
)

ax_pie6 = fig.add_subplot(gs[2, 1])
ax_pie6.pie(
    closed_pit_population,
    labels=labels,
    autopct=make_autopct(closed_pit_population),
    startangle=90,
    colors=pie_colors
)
ax_pie6.axis('equal')
ax_pie6.set_title(
    'Do vs Dont:\nGarbage dumped to closed pit',
    y=-0.2,
    fontsize=10,
    fontweight='bold'
)

ax_pie7 = fig.add_subplot(gs[2, 2])
ax_pie7.pie(
    open_pit_population,
    labels=labels,
    autopct=make_autopct(open_pit_population),
    startangle=90,
    colors=pie_colors
)
ax_pie7.axis('equal')
ax_pie7.set_title(
    'Do vs Dont:\nGarbage dumped to open pit',
    y=-0.2,
    fontsize=10,
    fontweight='bold'
)

ax_pie8 = fig.add_subplot(gs[2, 3])
ax_pie8.pie(
    other_population,
    labels=labels,
    autopct=make_autopct(other_population),
    startangle=90,
    colors=pie_colors
)
ax_pie8.axis('equal')
ax_pie8.set_title(
    'Do vs Dont:\nOther waste management',
    y=-0.2,
    fontsize=10,
    fontweight='bold'
)

fig.suptitle(
    'Table 7: Waste Management',
    fontsize=16,
    fontweight='bold'
)

plt.show()