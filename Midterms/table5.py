import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import textwrap

disaster_groups = [
    'Households who experienced more frequent flooding',
    'Households who experienced more frequent droughts',
    'Households who experienced decrease in water supply',
    'Households who experienced more frequent brownouts',
    'Households who experienced moving out leaving previous dwelling unit because of any calamity'
]
populations = [0, 31, 17, 70, 0]

wrapped_labels = [
    "\n".join(textwrap.wrap(label, 30))
    for label in disaster_groups
]

labels = ['Affected', 'Not Affected']
flooding_population = [0, 167]
droughts_population = [31, 136]
decrease_water_population = [17, 150]
brownout_population = [70, 97]
moving_out_population = [0, 167]

fig = plt.figure(figsize=(16, 8), constrained_layout=True)
gs = GridSpec(2, 5, figure=fig, height_ratios=[3, 2])

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
ax_bar.set_title('Total Population of Disaster-vulnerable Household',
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
    flooding_population,
    labels=labels,
    autopct=make_autopct(flooding_population),
    startangle=90,
    colors=pie_colors
)
ax_pie1.axis('equal')
ax_pie1.set_title(
    'Affected vs Not Affected:\nFrequent flooding',
    y=-0.1,
    fontsize=10,
    fontweight='bold'

)

ax_pie2 = fig.add_subplot(gs[1, 1])
ax_pie2.pie(
    droughts_population,
    labels=labels,
    autopct=make_autopct(droughts_population),
    startangle=90,
    colors=pie_colors

)
ax_pie2.axis('equal')
ax_pie2.set_title(
    'Affected vs Not Affected:\nFrequent droughts',
    y=-0.1,
    fontsize=10,
    fontweight='bold'
)

ax_pie3 = fig.add_subplot(gs[1, 2])
ax_pie3.pie(
    decrease_water_population,
    labels=labels,
    autopct=make_autopct(decrease_water_population),
    startangle=90,
    colors=pie_colors
)

ax_pie3.axis('equal')
ax_pie3.set_title(
    'Affected vs Not Affected:\nDecrease in water supply',
    fontsize=10,
    y=-0.1,
    fontweight='bold'
)

ax_pie4 = fig.add_subplot(gs[1, 3])
ax_pie4.pie(
    brownout_population,
    labels=labels,
    autopct=make_autopct(brownout_population),
    startangle=90,
    colors=pie_colors
)
ax_pie4.axis('equal')
ax_pie4.set_title(
    'Affected vs Not Affected:\nFrequent brownouts',
    y=-0.1,
    fontsize=10,
    fontweight='bold'
)

ax_pie5 = fig.add_subplot(gs[1, 4])
ax_pie5.pie(
    moving_out_population,
    labels=labels,
    autopct=make_autopct(moving_out_population),
    startangle=90,
    colors=pie_colors
)
ax_pie5.axis('equal')
ax_pie5.set_title(
    'Affected vs Not Affected:\nMoving out because\nof any calamity',
    y=-0.1,
    fontsize=10,
    fontweight='bold'
)

fig.suptitle(
    'Table 5: Disaster-vulnerable Household',
    fontsize=16,
    fontweight='bold'
)

plt.show()