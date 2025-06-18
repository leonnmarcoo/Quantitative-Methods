import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import textwrap

h_n_groups = [
    'Children under 5 years old who died',
    'Women who died due to pregnancy related-causes',
    'Malnourished children 0-5 years old',
    'People with normal health and nutrition satatus'
]
populations = [0, 0, 3, 580]

labels = ['Male', 'Female']
members_counts = [1, 2]

wrapped_labels = [
    "\n".join(textwrap.wrap(label, 15))
    for label in h_n_groups
]

fig, (ax_bar, ax_pie) = plt.subplots(1, 2, figsize=(12, 5))

bars = ax_bar.bar(wrapped_labels, populations, color='#FDB45C')
for bar in bars:
    height = bar.get_height()
    if height > 0:
        ax_bar.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.1,
            f'{height}',
            ha='center',
            va='bottom'
        )
ax_bar.set_xlabel(
    'Cases',
    fontweight='bold'
)
ax_bar.set_ylabel(
    'Number of Cases',
    fontweight='bold'
)
ax_bar.set_ylim(0, max(5, max(populations) * 1.15))
ax_bar.set_title(
    'Total Number of Cases',
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
    'Male vs Female: Case of\nMalnourished Children 0-5 Years Old',
    y=-0.2,
    fontweight='bold'
)

fig.suptitle(
    'Table 1.2: Demographic Breakdown of Cases under Health and Nutrition',
    fontsize=16,
    fontweight='bold'
)

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()