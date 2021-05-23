import pandas as pd
import ast
import altair as alt
from vega_datasets import data

filename = "data/insolvencias_2021.04.20"
export_file = "img/insolvencias_monthly_2021.04.20"

print("Reading " + filename + ".csv")

#Read the file
df = pd.read_csv(filename + '.csv', low_memory = False)
#Get the date and sort
df["day"]= [x[:7] for x in df["date"]]
df.sort_values(by = ["day"],inplace = True)
#Groupby monthly count
df_dates = pd.DataFrame(df.groupby(['day']).size()).reset_index("day")
#Rename columns
df_dates_cn = df_dates.rename(columns = {0:"recuento_insolvencias", "day":"month"})

###   GENERATE BASIC PLOT   ###
chart = alt.Chart(df_dates_cn).mark_line().encode(
    x='month:T',
    y='recuento_insolvencias:Q'
).properties(
    width=800,
    height=300
)
chart.save(export_file + '_basic.html')
print("Basic plot has been successfully saved at " + export_file + '_basic.html')


###   GENERATE INTERACTIVE PLOT   ###
source = df_dates_cn

# Create a selection that chooses the nearest point & selects based on x-value
nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['month'], empty='none')

# The basic line
line = alt.Chart(source).mark_line(interpolate='basis').encode(
    x='month:T',
    y='recuento_insolvencias:Q'
)

# Transparent selectors across the chart. This is what tells us
# the x-value of the cursor
selectors = alt.Chart(source).mark_point().encode(
    x='month:T',
    opacity=alt.value(0),
).add_selection(
    nearest
)

# Draw points on the line, and highlight based on selection
points = line.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)

# Draw text labels near the points, and highlight based on selection
text = line.mark_text(align='left', dx=2, dy=-2).encode(
    text=alt.condition(nearest, 'recuento_insolvencias:Q', alt.value(' '))
)

# Draw a rule at the location of the selection
rules = alt.Chart(source).mark_rule(color='gray').encode(
    x='month:T',
).transform_filter(
    nearest
)

# Put the five layers into a chart and bind the data
chart2 = alt.layer(
    line, selectors, points, rules, text
).properties(
    width=600, height=300
)

chart2.save(export_file + '_interactive.html')
print("Interactive plot has been successfully saved at " + export_file + '_interactive.html')



###    GENERATE INTERACTIVE CHANGING TOOLTIP      ###

source = df_dates_cn

# Create a selection that chooses the nearest point & selects based on x-value
nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['month'], empty='none')

# The basic line
line = alt.Chart(source).mark_line(interpolate='basis').encode(
    x='month:O',
    y='recuento_insolvencias:Q'
)

# Transparent selectors across the chart. This is what tells us
# the x-value of the cursor
selectors = alt.Chart(source).mark_point().encode(
    x='month:O',
    opacity=alt.value(0),
).add_selection(
    nearest
)

# Draw points on the line, and highlight based on selection
points = line.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)

# Draw text labels near the points, and highlight based on selection
text = line.mark_text(align='left', dx=2, dy=-2).encode(
    text=alt.condition(nearest, 'month:O', alt.value(' '))
)

# Draw a rule at the location of the selection
rules = alt.Chart(source).mark_rule(color='gray').encode(
    x='month:O',
).transform_filter(
    nearest
)

# Put the five layers into a chart and bind the data
chart3 = alt.layer(
    line, selectors, points, rules, text
).properties(
    width=600, height=300
)

chart3.save(export_file + '_interactive_text.html')
print("Interactive plot has been successfully saved at " + export_file + '_interactive_text.html')
