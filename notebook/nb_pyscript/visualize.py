import plotly.express as px

def pie_chart(data, feature, colors, hole=0.3, title="Distribution of feature", font_size=14):
    target_instance = data[feature].value_counts().to_frame()
    target_instance = target_instance.reset_index()
    target_instance = target_instance.rename(columns={'count':'Total Count'})

    fig = px.pie(target_instance, values="Total Count", names=feature, color_discrete_sequence=colors, hole=hole, title=title)

    fig.update_traces(textfont_size=font_size)

    return fig

def bar_chart(data, x, groupby_feature, colors, title="Distribution of feature of different categories", annotation_text=False):
    temp_df = data.groupby([x, groupby_feature]).size().reset_index()
    temp_df = temp_df.rename(columns={0:"Total Count"})

    # Take the total count of `feature` column
    feature_count = temp_df.groupby([x]).sum()['Total Count']
    percentages = [round(elm/sum(feature_count) * 100, 1) for elm in feature_count]

    # Draw a bar that shows the distribution of feature x for different groupby_feature
    fig = px.bar(temp_df, 
                 x=x, 
                 y="Total Count", 
                 color=groupby_feature, 
                 barmode="group",
                 color_discrete_sequence=colors, 
                 title=title)

    if annotation_text:
        cat_str = ""
        num_str = ""

        # Build the categorical string
        categories = data[x].unique()
        for i, cat in enumerate(categories):
            if i==len(categories)-2:
                cat_str += f"{cat} & "
            elif i==len(categories)-1:
                cat_str += f"{cat}"
            else:
                cat_str += f"{cat}, "

        # Build the numerical string
        for i, per in enumerate(percentages):
            if i==len(percentages)-2:
                num_str += f"{per}% & "
            elif i==len(percentages)-1:
                num_str += f"{per}%"
            else:
                num_str += f"{per}%, "

        fig.add_annotation(text=f"Distribution of {x} for values {cat_str}<br> is {num_str} respectively.", 
                           x=1.4, 
                           y=1.3, 
                           xref="paper", 
                           yref="paper", 
                           align="left", 
                           showarrow=False, 
                           bordercolor="black", 
                           borderwidth=1, 
                           font=dict(
                               size=16, 
                               color="#333"))
        
        fig.update_layout(margin=dict(r=400))

    return fig