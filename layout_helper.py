from dash import dcc, html
import dash_bootstrap_components as dbc
import api_helper as help



# Wallet title
wallet_head = html.H2('Portfolio', className="text-center mb-4"),

# Wallet Buttons
buy_button = dbc.Button(id='buy_b', children=['Buy'], color="primary", n_clicks=0)
sell_button = dbc.Button(id='sell_b', children=['Sell'], color="primary", n_clicks=0)
reset_btn = dbc.Button(id='reset', children=['Reset'], color="dark")
refresh_btn = dbc.Button(id='refresh', children='Refresh', color='light')
USD_bal = dbc.InputGroup(
            [
                dbc.InputGroupText("$"),
                dbc.Input(id="bank", placeholder="Initial Balance", type="number", debounce=True),
            ]
        )
wallet_bal = html.P(id="bal", children="Wallet Balance: $0.00")



# Building buy form
buy_coin_dropdown = dcc.Dropdown(
            id="coins_buy",
            options=help.optionList,
            value='BTC/USD',
            clearable=True,
            style={'width': "100px"}
        ),
price_buy = dbc.InputGroup(
            [
                dbc.InputGroupText("$"),
                dbc.Input(id="price_buy", placeholder="Amount", type="number"),
                dbc.InputGroupText(".00"),
            ]
        )
buy_submit = dbc.Button(id="buy_submit", children="Submit", color="success")

# Layout
row1 = dbc.Row(dbc.Col(wallet_head))
row2 = dbc.Row(
    [
        dbc.Col(buy_button, width=1), 
        dbc.Col(sell_button, width=1),
        dbc.Col(reset_btn, width=1),
        dbc.Col(refresh_btn, width=1),
        dbc.Col(html.P("Bank Balance:"), width=1, style={"padding": "5px 0"}),
        dbc.Col(USD_bal, width=2),
        dbc.Col(wallet_bal, width=0, style={"padding": "5px 0"})
    ],
    className="mb-4")
buy_row = dbc.Row(
            [
                dbc.Col(children=buy_coin_dropdown, width="auto", className="me-3"), 
                dbc.Col(children=price_buy, width="auto", className="me-3"),
                dbc.Col(children=buy_submit, width="auto")
            ], 
            className="g-2"
        )

buy_form_div = html.Div(id="buy_div", children=[buy_row], hidden=True, className="mb-4", style={'width': "auto"})