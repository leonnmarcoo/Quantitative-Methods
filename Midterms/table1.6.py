import matplotlib.pyplot as plt
import textwrap

house_groups = [
    'Households with income below poverty threshold',
    'Households with income below food threshold',
    'Households who experienced food shortage',
    'Unemployed members of the labor force',
    'Households with income above the poverty threshold'
]
magnitude = [91, 54, 0, 7, 15]

wrapped_labels = [
    "\n".join(textwrap.wrap(label, 25))
    for label in house_groups
]

fig, (ax_bar) = plt.subplots(figsize=(12, 5))

bars = ax_bar.bar(wrapped_labels, magnitude, color='#FDB45C')
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
    'Number of Household',
    fontweight='bold'
)
ax_bar.set_ylim(0, max(5, max(magnitude) * 1.15))
ax_bar.set_title(
    'Total Number of Cases',
    fontweight='bold'
)

fig.suptitle(
    'Table 1.6: Demographic Breakdown of Cases under Income and Livelihood',
    fontsize=16,
    fontweight='bold'
)

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()