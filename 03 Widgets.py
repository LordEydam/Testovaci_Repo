import ipywidgets as widgets

widgets.IntProgress(
    value=7,
    min=0,
    max=10,
    step=1,
    description="Popisok",
    bar_style='',
    style={'bar_color': 'red'},
    orientation='horizontal'
)