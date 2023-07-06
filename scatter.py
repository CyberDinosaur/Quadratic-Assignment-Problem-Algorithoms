import pandas as pd
import altair as alt

data = {
    'Algorithm': ['ts_20', 'ts_50', 
                  'ils_2-opt', 'ils_3-opt', 'ils_4-opt',
                  'ga_tournament', 'ga_roulette_wheel'],
    'Time(s)': [547.177774, 540.578225, 
                618.473354, 31.371288, 44.913609,
                2807.842844, 2766.687726],
    'Best_objective_value': [21731166, 21690850, 
                             21531286, 22178180, 22429246,
                             21417980, 21492098]
}
df = pd.DataFrame(data)

color_scheme = 'category20'

chart = alt.Chart(df).mark_circle(size=100).encode(
    x='Time(s)',
    y=alt.Y('Best_objective_value', scale=alt.Scale(domain=(21200000, 22600000))),
    color=alt.Color('Algorithm', scale=alt.Scale(scheme=color_scheme)),
    tooltip=['Algorithm']
).properties(
    title='Algorithm Performance',
    width=400,
    height=300
)

# 保存图表
chart.save('./pic/scatter.html', scale_factor=2.0)
