import plotly.express as px

def pie_chart(data, feature, colors, hole, title):
    target_instance = data[feature].value_counts().to_frame()
    target_instance = target_instance.reset_index()
    target_instance = target_instance.rename(columns={'count':'Total Count'})

    fig = px.pie(target_instance, values="Total Count", names=feature, color_discrete_sequence=colors, hole=hole, title=title)

    return fig

def bar_chart(data, ):
    pass