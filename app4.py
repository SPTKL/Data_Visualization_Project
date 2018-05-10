import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import urllib.request, json
import numpy as np

app = dash.Dash()

#load geojson
with urllib.request.urlopen('https://raw.githubusercontent.com/hvo/datasets/master/nyc_zip.geojson') as url:
    data = json.loads(url.read().decode())

mapbox_access_token = 'pk.eyJ1IjoiZ2lsdHJhcG8iLCJhIjoiY2o4eWJyNzY4MXQ1ZDJ3b2JsZHZxb3N0ciJ9.MROnmydnXtfjqjIBtC-P5g'

app.css.append_css({
    'external_url': (
        'https://cdn.rawgit.com/chriddyp/0247653a7c52feb4c48437e1c1837f75'
        '/raw/a68333b876edaf62df2efa7bac0e9b3613258851/dash.css'
    )
})

app.layout = html.Div(children=[
    html.H1(children='Data Visualization Project',
            style={
            'textAlign': 'center',
            'color': 'black'
        }),
    dcc.Markdown('''
    #### Visualizing time series of 311 complaint types in different zipcode area in New York City
    '''.replace('  ', ''), className='container',
    containerProps={'style': {'textAlign': 'center','maxWidth': '850px'}}),

    html.Div([
        dcc.Dropdown(
        id='zipcode_dropdown',
        options=[{'label': i, 'value': i} for i in [10001.0,10002.0,10003.0,10004.0,10005.0,10006.0,10007.0, 10008.0,10009.0, 10010.0, 10011.0, 10012.0, 10013.0, 10014.0, 10016.0, 10017.0, 10018.0, 10019.0, 10020.0, 10021.0, 10022.0, 10023.0, 10024.0, 10025.0, 10026.0, 10027.0, 10028.0,
         10029.0, 10030.0, 10031.0, 10032.0, 10033.0, 10034.0, 10035.0, 10036.0, 10037.0, 10038.0, 10039.0, 10040.0, 10041.0, 10044.0, 10045.0, 10048.0, 10055.0, 10065.0, 10069.0, 10075.0, 10101.0, 10103.0, 10104.0, 10105.0, 10106.0, 10107.0, 10110.0, 10111.0, 10112.0, 10115.0, 10116.0,
          10118.0, 10119.0, 10120.0, 10121.0, 10122.0, 10123.0, 10128.0, 10129.0, 10134.0, 10151.0, 10152.0, 10153.0, 10154.0, 10155.0, 10158.0, 10159.0, 10162.0, 10165.0, 10166.0, 10167.0, 10168.0, 10169.0, 10170.0, 10171.0, 10172.0, 10173.0, 10174.0, 10176.0, 10177.0, 10178.0, 10179.0,
          10224.0, 10270.0, 10271.0, 10278.0, 10279.0, 10280.0, 10281.0, 10282.0, 10301.0, 10302.0, 10303.0, 10304.0, 10305.0, 10306.0, 10307.0, 10308.0, 10309.0, 10310.0, 10312.0, 10314.0, 10318.0, 10367.0, 10412.0, 10435.0, 10444.0, 10450.0, 10451.0, 10452.0, 10453.0, 10454.0, 10455.0,
          10456.0, 10457.0, 10458.0, 10459.0, 10460.0, 10461.0, 10462.0, 10463.0, 10464.0, 10465.0, 10466.0, 10467.0, 10468.0, 10469.0, 10470.0, 10471.0, 10472.0, 10473.0, 10474.0, 10475.0, 10476.0, 10501.0, 10502.0, 10504.0, 10506.0, 10507.0, 10510.0, 10514.0, 10516.0, 10520.0, 10522.0,
          10523.0, 10526.0, 10528.0, 10530.0, 10532.0, 10533.0, 10536.0, 10538.0, 10543.0, 10548.0, 10549.0, 10550.0, 10552.0, 10553.0, 10561.0, 10562.0, 10566.0, 10567.0, 10568.0, 10572.0, 10573.0, 10576.0, 10577.0, 10580.0, 10582.0, 10583.0, 10589.0, 10590.0, 10591.0, 10594.0, 10595.0,
          10598.0, 10601.0, 10603.0, 10604.0, 10605.0, 10606.0, 10610.0, 10701.0, 10703.0, 10704.0, 10705.0, 10706.0, 10707.0, 10708.0, 10709.0, 10710.0, 10750.0, 10801.0, 10803.0, 10804.0, 10805.0, 10913.0, 10916.0, 10917.0, 10921.0, 10940.0, 10950.0, 10951.0, 10952.0, 10954.0, 10956.0,
          10960.0, 10962.0, 10964.0, 10965.0, 10968.0, 10977.0, 10980.0, 10984.0, 10987.0, 10989.0, 10994.0, 11001.0, 11003.0, 11004.0, 11005.0, 11008.0, 11010.0, 11011.0, 11012.0, 11020.0, 11021.0, 11023.0, 11024.0, 11027.0, 11030.0, 11031.0, 11040.0, 11042.0, 11050.0, 11054.0, 11096.0,
          11101.0, 11102.0, 11103.0, 11104.0, 11105.0, 11106.0, 11109.0, 11111.0, 11122.0, 11201.0, 11203.0, 11204.0, 11205.0, 11206.0, 11207.0, 11208.0, 11209.0, 11210.0, 11211.0, 11212.0, 11213.0, 11214.0, 11215.0, 11216.0, 11217.0, 11218.0, 11219.0, 11220.0, 11221.0, 11222.0, 11223.0,
          11224.0, 11225.0, 11226.0, 11228.0, 11229.0, 11230.0, 11231.0, 11232.0, 11233.0, 11234.0, 11235.0, 11236.0, 11237.0, 11238.0, 11239.0, 11241.0, 11242.0, 11243.0, 11249.0, 11251.0, 11253.0, 11317.0, 11354.0, 11355.0, 11356.0, 11357.0, 11358.0, 11359.0, 11360.0, 11361.0, 11362.0,
          11363.0, 11364.0, 11365.0, 11366.0, 11367.0, 11368.0, 11369.0, 11370.0, 11371.0, 11372.0, 11373.0, 11374.0, 11375.0, 11377.0, 11378.0, 11379.0, 11385.0, 11405.0, 11411.0, 11412.0, 11413.0, 11414.0, 11415.0, 11416.0, 11417.0, 11418.0, 11419.0, 11420.0, 11421.0, 11422.0, 11423.0,
          11426.0, 11427.0, 11428.0, 11429.0, 11430.0, 11432.0, 11433.0, 11434.0, 11435.0, 11436.0, 11451.0, 11452.0, 11501.0, 11507.0, 11509.0, 11510.0, 11514.0, 11516.0, 11518.0, 11520.0, 11526.0, 11528.0, 11530.0, 11542.0, 11543.0, 11545.0, 11549.0, 11550.0, 11552.0, 11553.0, 11554.0,
          11556.0, 11557.0, 11558.0, 11559.0, 11560.0, 11561.0, 11563.0, 11565.0, 11566.0, 11568.0, 11569.0, 11570.0, 11571.0, 11572.0, 11575.0, 11576.0, 11577.0, 11579.0, 11580.0, 11581.0, 11583.0, 11590.0, 11596.0, 11597.0, 11598.0, 11691.0, 11692.0, 11693.0, 11694.0, 11695.0, 11697.0,
          11701.0, 11702.0, 11703.0, 11704.0, 11706.0, 11710.0, 11713.0, 11714.0, 11716.0, 11717.0, 11719.0, 11720.0, 11721.0, 11722.0, 11723.0, 11724.0, 11725.0, 11726.0, 11729.0, 11730.0, 11731.0, 11732.0, 11733.0, 11735.0, 11739.0, 11741.0, 11742.0, 11743.0, 11746.0, 11747.0, 11749.0,
          11753.0, 11754.0, 11755.0, 11756.0, 11757.0, 11758.0, 11762.0, 11766.0, 11767.0, 11768.0, 11771.0, 11772.0, 11776.0, 11777.0, 11778.0, 11779.0, 11780.0, 11782.0, 11783.0, 11784.0, 11787.0, 11788.0, 11790.0, 11791.0, 11792.0, 11793.0, 11794.0, 11795.0, 11797.0, 11798.0, 11801.0,
          11803.0, 11804.0, 11841.0, 11901.0, 11949.0, 11950.0, 11959.0]],
        value=11201,
        ),
        dcc.RadioItems(
            id='analysis',
            options=[{'label': i, 'value': i} for i in ['actual', 'trend']],
            value='actual',
            labelStyle={'display': 'inline-block'}),
        ],
            style={'width': '49%', 'display': 'inline-block'}),

        html.Div([
            dcc.Graph(id='chart-container'),
            dcc.Slider(
                id='year_slider',
                min=2010,
                max=2018,
                marks={i: '{}'.format(i) for i in range(2010, 2019)},
                value=2016),
            dcc.Graph(id= "mapbox", animate=True),
            ])
    ])

@app.callback(
    dash.dependencies.Output('chart-container', 'figure'),
    [dash.dependencies.Input('zipcode_dropdown', 'value'),
    dash.dependencies.Input('year_slider', 'value'),
    dash.dependencies.Input('analysis', 'value')])
def update_output(zipcode, year, analysis):
    query = 'SELECT%20*%20FROM%20bc1561.zip_month_cate_year%20WHERE%20incident_zip={0}%20AND%20year={1}'.format(zipcode,year)
    url = 'https://bc1561.carto.com/api/v2/sql?q={}&format=csv&api_key=b909c5c6fadec823ce2a1160321a699d96880811'.format(query)
    traces = []
    dff = pd.read_csv(url)
    for c in list(dff.category.unique()):
        if analysis == 'actual':
            y = list(dff[dff.category == c]['count'])
        else:
            y = list(pd.rolling_mean(dff[dff.category == c]['count'], 4))
        traces.append({
        'x':list(dff.year_month.unique()),
        'y':y,
        'type': 'line',
        'name': c
        })
    return{
        'data': traces,
        'layout': {
            'title': 'Complaint counts by Category in Zipcode {0} in year {1}'.format(zipcode, year),
            'height': 800,
            'width': 1000}}

@app.callback(
    dash.dependencies.Output('mapbox', 'figure'),
    [dash.dependencies.Input('year_slider', 'value')])
def update_map(year):
    query = 'SELECT%20incident_zip,%20sum(count)%20FROM%20bc1561.zip_month_cate_year%20where%20year={}%20group%20by%20incident_zip'.format(year)
    url = 'https://bc1561.carto.com/api/v2/sql?q={}&format=csv&api_key=b909c5c6fadec823ce2a1160321a699d96880811'.format(query)
    dt = pd.read_csv(url)
    dt['bins'] = pd.cut(dt['sum'], bins = 20, labels = list(range(20)))
    def get_color(zipcode):
        try:
            b = dt[dt.incident_zip == float(zipcode)]['bins'].tolist()[0]
            converted = round(255 - b*12.75)
            color = 'rgb(255, {}, {})'.format(converted, converted)
        except (KeyError,IndexError):
            color = 'rgb(255, 255, 255)'
        return color
    return{
        "data": [{
              "type": "scattermapbox",
              "lat": [47.751569],
              "lon": [1.675063],
              "mode": "markers",
        }],
        "layout": dict(
            autosize = True,
            hovermode = "closest",
            margin = dict(l = 0, r = 0, t = 0, b = 0),
            mapbox = dict(
                accesstoken = mapbox_access_token,
                bearing = 0,
                center = dict(lat = 40.758896, lon = -73.985130),
                style = "light",
                pitch = 0,
                zoom = 9,
                layers = [{
                    'sourcetype' : 'geojson',
                    'source' : data['features'][i],
                    'color' : get_color(data['features'][i]['properties']['zipcode']),
                    'type' : 'fill',
                    'opacity': 0.7} for i in range(len(data['features']))]
            )
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)
