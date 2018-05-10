import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import numpy as np

app = dash.Dash(__name__)
server = app.server

mapbox_access_token = 'pk.eyJ1IjoiZ2lsdHJhcG8iLCJhIjoiY2o4eWJyNzY4MXQ1ZDJ3b2JsZHZxb3N0ciJ9.MROnmydnXtfjqjIBtC-P5g'

app.css.append_css({
    'external_url': (
        'https://cdn.rawgit.com/chriddyp/0247653a7c52feb4c48437e1c1837f75'
        '/raw/a68333b876edaf62df2efa7bac0e9b3613258851/dash.css'
    )
})

app.layout = html.Div(children=[
    html.Div([
        dcc.Dropdown(
        id='type',
        options=[{'label': i, 'value': i} for i in ['Other', 'Streets_&_Sidewalks','Parking_&_Vehicles',
                                                    'Noise','Transportation', 'Not_a_complaint',
                                                    'Public_Health_&_Safety','Plumbing', 'Heating']],
        value='Noise',
        ),
        dcc.Graph(id= "chart"),
        dcc.Slider(
            id='day_slider',
            min=1,
            max=31,
            marks={i: i for i in range(1, 32)},
            value=15),
        dcc.Graph(id= "mapbox", animate=True),
    ])
])

@app.callback(
    dash.dependencies.Output('chart', 'figure'),
    [dash.dependencies.Input('type', 'value')])
def create_chart(type):
    query = "SELECT%20created_date,%20count(*)%20FROM%20bc1561.complaints_2015_05%20Where%20category%20=%20'{0}'%20group%20by%20created_date%20order%20by%20created_date".format(type)
    url = 'https://bc1561.carto.com/api/v2/sql?q={}&format=csv&api_key=b909c5c6fadec823ce2a1160321a699d96880811'.format(query)
    dt = pd.read_csv(url)
    actual = dt['count'].tolist()
    trend = pd.rolling_mean(dt['count'], 7).tolist()
    traces = [
        {'x':dt.created_date.tolist(),
         'y':actual,
         'type': 'line',
         'name':'actual',
         'color': 'red'},
         {'x':dt.created_date.tolist(),
          'y':trend,
          'type': 'line',
          'name':'trend',
          'color': 'blue'}
          ]
    return{
        'data': traces,
        'layout': {
            'title': 'Time series plot for {} complaint'.format(type),
            }
        }



@app.callback(
    dash.dependencies.Output('mapbox', 'figure'),
    [dash.dependencies.Input('day_slider', 'value'),
    dash.dependencies.Input('type', 'value')])
def update_map(day, type):
    query = "SELECT%20longitude,latitude%20FROM%20bc1561.complaints_2015_05%20Where%20to_char(created_date,'DD')%20=%20'{0}'%20and%20category%20=%20'{1}'%20".format(day, type)
    url = 'https://bc1561.carto.com/api/v2/sql?q={}&format=csv&api_key=b909c5c6fadec823ce2a1160321a699d96880811'.format(query)
    dt = pd.read_csv(url)
    data = [go.Scattermapbox(
        lat=dt.latitude.tolist(),
        lon=dt.longitude.tolist(),
        mode='markers',
        marker=dict(
            size=9,
            opacity = 0.7
        ),
            )]
    layout = go.Layout(
        title='scatter map for {} complaints for 2015/05/{}'.format(type, day),
        autosize=True,
        height=1000,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(lat = 40.758896, lon = -73.985130),
            pitch=0,
            zoom=11
        ),
        )
    fig = dict(data=data, layout=layout)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
