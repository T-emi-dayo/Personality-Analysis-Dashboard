import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, callback, Input, Output


# Loading dataset
df = pd.read_csv("dataset/processed_data.csv")

# INitializing app
app = Dash("Human Personality Dashboard")

feature_columns = df.drop(columns=["Personality"]).columns.tolist()

# Dropdown options
dropdown_options = [{'label': col.replace('_', ' ').title(), 'value': col} for col in feature_columns]

# Defining Graphs

def create_scatterplot(x_axis='Time_spent_Alone', y_axis='Social_event_attendance', color_encode=False):
    fig = px.scatter(df, x=x_axis, y=y_axis,
                     color='Personality' if color_encode else None,
                     hover_name='Personality',
                     title='{} vs. {}'.format(x_axis.replace('_', ' ').title(), y_axis.replace('_', ' ').title()))
    fig.update_layout(height=600, margin={'l': 40, 'b': 40, 't': 60, 'r': 0}, hovermode='closest')
    return fig

def create_boxplot(y_axis='Time_spent_Alone'):
    fig = px.box(df, x='Personality', y=y_axis, color='Personality',
                 title=y_axis.replace('_', ' ').title() + ' by Personality Type',
                 labels={'Personality': 'Personality Type'})
    fig.update_layout(height=600, margin={'l': 40, 'b': 40, 't': 60, 'r': 0})
    return fig

# Widgets
x_axis_dropdown = dcc.Dropdown(
    id="x_axis_selector",
    options=dropdown_options,
    value="Time_spent_Alone",
    clearable=False
)

y_axis_dropdown = dcc.Dropdown(
    id="y_axis_selector", 
    options=dropdown_options,
    value="Social_event_attendance",
    clearable=False
)

color_encode_checkbox = dcc.Checklist(
    id="color_encode_checkbox",
    options=[{"label": "Color by Personality", "value": "Color Encode"}],
    value=[],
    inline=True
)

# App Layout
app.layout = html.Div(
    children=[
        html.H1("Human Personality Dashboard by Introvert and Extrovert",
                style={'textAlign': 'center', 'color': '#2c3e50', 'paddingTop': '20px'}),
        html.Div("Explore relationships between human traits and their personalities (Introvert or Extrovert)",
                 style={'textAlign': 'center', 'marginBottom': '30px', 'color': '#34495e'}),
        html.Div(
            children=[
                html.Label("Select X-Axis for Scatter Plot:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                x_axis_dropdown,
                html.Br(),
                html.Label("Select Y-Axis for Plots:", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                y_axis_dropdown,
                html.Br(),
                color_encode_checkbox,
            ],
            style={
                "width": "99%",
                "padding": "20px",
                "boxShadow": "0 4px 8px 0 rgba(0,0,0,0.2)",
                "borderRadius": "10px",
                "marginBottom": "20px",
                "backgroundColor": "#ffffff"
            }
        ),

        html.Div(
            children=[
                html.Div(
                    children=[
                        dcc.Graph(id="scatter_plot", figure=create_scatterplot())
                    ],
                    style={
                        "display": "inline-block",
                        "width": "49%",
                        "verticalAlign": "top",
                        "padding": "10px",
                        "boxShadow": "0 4px 8px 0 rgba(0,0,0,0.1)", 
                        "borderRadius": "10px",
                        "marginRight": "1%",
                        "backgroundColor": "#ffffff"
                    }
                ),
                html.Div(
                    children=[
                        dcc.Graph(id="box_plot", figure=create_boxplot()) 
                    ],
                    style={
                        "display": "inline-block",
                        "width": "49%",
                        "verticalAlign": "top",
                        "padding": "10px",
                        "boxShadow": "0 4px 8px 0 rgba(0,0,0,0.1)", 
                        "borderRadius": "10px",
                        "backgroundColor": "#ffffff"
                    }
                )
            ],
            style={
                "display": "flex", 
                "justifyContent": "space-between",
                "width": "99%"
            }
        )
    ],
    style={
        'fontFamily': 'Arial, sans-serif',
        'maxWidth': '1400px',
        'margin': 'auto',
        'padding': '20px',
        'backgroundColor': '#f2f2f2'
    }
)

# Callbacks

# Callback for updating the Scatter Plot
@callback(
    Output('scatter_plot', 'figure'),
    Input('x_axis_selector', 'value'),
    Input('y_axis_selector', 'value'),
    Input('color_encode_checkbox', 'value')
)
def update_scatter_plot(selected_x_axis, selected_y_axis, selected_color_encode_values):
    """
    Updates the scatter plot based on user selections from dropdowns and checkbox.
    """
    color_encoded = "Color Encode" in selected_color_encode_values
    return create_scatterplot(x_axis=selected_x_axis, y_axis=selected_y_axis, color_encode=color_encoded)

# Callback for updating the Box Plot
@callback(
    Output('box_plot', 'figure'),
    Input('y_axis_selector', 'value')
)
def update_box_plot(selected_y_axis):
    """
    Updates the box plot based on the Y-axis selection.
    """
    return create_boxplot(y_axis=selected_y_axis)


# Running the app
if __name__ == '__main__':
    app.run(debug=True)
