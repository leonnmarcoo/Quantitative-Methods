import matplotlib.pyplot as plt
import textwrap

age_groups = [
    'Children 6-11 years old not attending elementary',
    'Children 6-12 years old not attending elementary',
    'Children 12-15 years old not attending high school',
    'Children 13-16 years old attending high school',
    'Children 6-15 years old attending school',
    'Children 6-16 years old attending school',

]
populations = [2, 10, 13, 11, 9, 10]

wrapped_labels = [
    "\n".join(textwrap.wrap(label, 23))
    for label in age_groups
]

fig, (ax_bar) = plt.subplots(figsize=(12, 5))

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

fig.suptitle(
    'Table 1.5: Demographic Breakdown of Cases under Basic Education',
    fontsize=16,
    fontweight='bold'
)

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()