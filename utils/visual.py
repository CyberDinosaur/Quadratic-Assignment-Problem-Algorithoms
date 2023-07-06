import plotly.graph_objects as go
import plotly.offline as pyo
import os

def drawPlot(plot_title, generations, average_results):
    average_trace = go.Scatter(
        x=generations,
        y=average_results,
        line=dict(color='rgb(30,111,255)'),
        mode='lines',
        name='Average',
    )

    data = [average_trace]

    layout = go.Layout(
        title=plot_title,
        paper_bgcolor='rgb(255,255,255)',
        plot_bgcolor='rgb(229,229,229)',
        xaxis=dict(
            gridcolor='rgb(255,255,255)',
            showgrid=True,
            showline=False,
            showticklabels=True,
            tickcolor='rgb(127,127,127)',
            ticks='outside',
            zeroline=False
        ),
        yaxis=dict(
            gridcolor='rgb(255,255,255)',
            showgrid=True,
            showline=False,
            showticklabels=True,
            tickcolor='rgb(127,127,127)',
            ticks='outside',
            zeroline=False
        ),
    )
    fig = go.Figure(data=data, layout=layout)
    
    save_path = 'pic/'  # 替换为指定的路径
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = os.path.join(save_path, 'plot_' + plot_title + '.html')
    
    pyo.plot(fig, filename=file_path)