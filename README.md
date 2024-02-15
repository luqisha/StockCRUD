This is a basic Django web-app for demonstrating reading and visualizing stock market data from a JSON file. This app utilizes **Plotly** for interactive visualization of price and volumes of stocks stored in the database database.

### Endpoints:
- ``/jsonModel/`` : This endpoint can be used for accessing the **jsonModel** version of the application. It will load data from the JSON file and render the tabular visualization.
- ``/sqlModel/`` : Similar to the previous endpoint, this one is for accesing the **sqlModel** version of the application. It fetches all the stock data from the SQLite database and rendering the tabuler representation along with options for visualizing the plots of a specific stock. The home page also points to this same endpoint.
- ``/sqlModel/trade_code_here`` : This endpoint allows for accessing specific stock data based on the trade code provided in the URL. It fetches the data available in SQLite database for the specified stock and renders an interactive chart for closing price and volume.

### Takeaways:
- Learned Django project structure including models, views, templates, and urlpattterns.
- Learned about ORM queries and and data migrations.
- Worked with Plotly to create interactive charts.
- Deployed a Django web-app on a cloud service.

### Dependencies:
- Django 5.0
- Plotly 5.18.0
