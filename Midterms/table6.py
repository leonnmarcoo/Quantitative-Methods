import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import textwrap

economic_activity_groups = [
    'Engaged in crop farming and gardening',
    'Engaged in livestock/poultry',
    'Engaged in fishing',
    'Engaged in forestry',
    'Engaged in wholesale/retail',
    'Engaged in manufacturing',
    'Engaged in community, social & personal service',
    'Engaged in transportation, storage & communication',
    'Engaged in mining & quarrying',
    'Engaged in construction',
    'Other activities'
]
populations = [88, 24, 0, 0, 3, 0, 0, 1, 0, 0, 1]

wrapped_labels = [
    "\n".join(textwrap.wrap(label, 20))
    for label in economic_activity_groups
]

labels = ['Engaged', 'Not Engaged']
gardening_population = [88, 79]
poultry_population = [24, 143]
fishing_population = [0, 167]
forestry_population = [0, 167]
retail_population = [3, 164]
manufacturing_population = [0, 167]
community_population = [0, 167]
transportation_population = [1, 166]
mining_population = [0, 167]
construction_population = [0, 167]
other_population = [1, 166]

fig = plt.figure(figsize=(16, 10), constrained_layout=True)
gs = GridSpec(3, 6, figure=fig, height_ratios=[2.5, 2, 2])

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
ax_bar.set_title('Total Population of Economic Activity',
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
    gardening_population,
    labels=labels,
    autopct=make_autopct(gardening_population),
    startangle=90,
    colors=pie_colors
)
ax_pie1.axis('equal')
ax_pie1.set_title(
    'Engaged vs Not Engaged:\nCrop farming and gardening',
    y=-0.2,
    fontsize=10,
    fontweight='bold'

)

ax_pie2 = fig.add_subplot(gs[1, 1])
ax_pie2.pie(
    poultry_population,
    labels=labels,
    autopct=make_autopct(poultry_population),
    startangle=90,
    colors=pie_colors
)
ax_pie2.axis('equal')
ax_pie2.set_title(
    'Engaged vs Not Engaged:\nLivestock/poultry',
    y=-0.2,
    fontsize=10,
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
    'Engaged vs Not Engaged:\nFishing',
    fontsize=10,
    y=-0.2,
    fontweight='bold'
)

ax_pie4 = fig.add_subplot(gs[1, 3])
ax_pie4.pie(
    forestry_population,
    labels=labels,
    autopct=make_autopct(forestry_population),
    startangle=90,
    colors=pie_colors
)
ax_pie4.axis('equal')
ax_pie4.set_title(
    'Engaged vs Not Engaged:\nForestry',
    y=-0.2,
    fontsize=10,
    fontweight='bold'
)

ax_pie5 = fig.add_subplot(gs[1, 4])
ax_pie5.pie(
    retail_population,
    labels=labels,
    autopct=make_autopct(retail_population),
    startangle=90,
    colors=pie_colors
)
ax_pie5.axis('equal')
ax_pie5.set_title(
    'Engaged vs Not Engaged:\nWholesale/retail',
    y=-0.2,
    fontsize=10,
    fontweight='bold'
)

ax_pie6 = fig.add_subplot(gs[1, 5])
ax_pie6.pie(
    manufacturing_population,
    labels=labels,
    autopct=make_autopct(manufacturing_population),
    startangle=90,
    colors=pie_colors
)
ax_pie6.axis('equal')
ax_pie6.set_title(
    'Engaged vs Not Engaged:\nManufacturing',
    y=-0.2,
    fontsize=10,
    fontweight='bold'
)

ax_pie7 = fig.add_subplot(gs[2, 0])
ax_pie7.pie(
    community_population,
    labels=labels,
    autopct=make_autopct(community_population),
    startangle=90,
    colors=pie_colors
)
ax_pie7.axis('equal')
ax_pie7.set_title(
    'Engaged vs Not Engaged:\nCommunity, social\n& personal service',
    y=-0.2,
    fontsize=10,
    fontweight='bold'
)

ax_pie8 = fig.add_subplot(gs[2, 1])
ax_pie8.pie(
    transportation_population,
    labels=labels,
    autopct=make_autopct(transportation_population),
    startangle=90,
    colors=pie_colors
)
ax_pie8.axis('equal')
ax_pie8.set_title(
    'Engaged vs Not Engaged:\nTransportation, storage\n& communication',
    y=-0.2,
    fontsize=10,
    fontweight='bold'
)

ax_pie9 = fig.add_subplot(gs[2, 2])
ax_pie9.pie(
    mining_population,
    labels=labels,
    autopct=make_autopct(mining_population),
    startangle=90,
    colors=pie_colors
)
ax_pie9.axis('equal')
ax_pie9.set_title(
    'Engaged vs Not Engaged:\nMining and quarrying',
    y=-0.2,
    fontsize=10,
    fontweight='bold'
)

ax_pie10 = fig.add_subplot(gs[2, 3])
ax_pie10.pie(
    construction_population,
    labels=labels,
    autopct=make_autopct(construction_population),
    startangle=90,
    colors=pie_colors
)
ax_pie10.axis('equal')
ax_pie10.set_title(
    'Engaged vs Not Engaged:\nConstruction',
    y=-0.2,
    fontsize=10,
    fontweight='bold'
)

ax_pie11 = fig.add_subplot(gs[2, 4])
ax_pie11.pie(
    other_population,
    labels=labels,
    autopct=make_autopct(other_population),
    startangle=90,
    colors=pie_colors
)
ax_pie11.axis('equal')
ax_pie11.set_title(
    'Engaged vs Not Engaged:\nOther activities',
    y=-0.2,
    fontsize=10,
    fontweight='bold'
)

fig.suptitle(
    'Table 6: Economic Activity',
    fontsize=16,
    fontweight='bold'
)

plt.show()