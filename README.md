# CS340_Dashboard_Project
CS 340 DASHBOARD PROJECT README

About the Dashboard Project
The Grazioso Salvare Dashboard is an interactive data visualization and management tool developed to help analyze and filter data from the Austin Animal Center Outcomes dataset. It uses MongoDB as the backend data source and Dash (a Python-based web framework) as the front-end interface to present real-time, filterable data. This dashboard provides data tables, geolocation charts, and other dynamic visualizations that respond to user interactions, enabling efficient tracking of rescue types, animal outcomes, and adoption trends.

Motivation
Grazioso Salvare required an intuitive and responsive dashboard to explore large sets of animal outcomes data without manually querying MongoDB. The goal was to create a client-friendly interface that could visualize rescue operations, identify adoption trends, and locate animals based on outcome types. The dashboard consolidates data analytics and visualization into a single web application that updates dynamically as users apply filters.

Getting Started
To get a local copy running in Codio or another environment:
1.	Ensure MongoDB is installed and running.
o	MongoDB is preinstalled in Codio.
o	Confirm the aac database exists and contains the animals collection with the Austin Animal Center Outcomes dataset.
2.	Verify that the aacuser account exists with readWrite access to the aac database.
o	Note the username and password for database authentication in the CRUD module.
3.	Download or navigate to the following project files:
o	CRUD_Python_Module.py – Python class handling Create, Read, Update, and Delete operations
o	ProjectTwoDashboard.ipynb – Jupyter Notebook containing the dashboard code
o	Grazioso_Salvare_Logo.png – Logo image used in the dashboard header

Installation
•	Python 3.x – Required to run Dash and MongoDB operations.
•	Dash – Framework for building interactive web dashboards (pip install dash).
•	Plotly – Library for charting and geolocation visualization (pip install plotly).
•	PyMongo – MongoDB driver for Python (pip install pymongo).
•	Pandas – For data manipulation and filtering (pip install pandas).

Usage
Code Example
from CRUD_Python_Module import CRUD
from dash import Dash, dash_table, dcc, html, Input, Output

# Database connection
crud = CRUD("aacuser", "NewPassword123", "aac")

# Retrieve all records
data = crud.read({}, "animals")

# Initialize Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.Img(src="assets/Grazioso_Salvare_Logo.png", style={"height": "80px"}),
    html.H1("Grazioso Salvare Animal Outcomes Dashboard"),
    dcc.Dropdown(
        id='filter-dropdown',
        options=[
            {'label': 'Water Rescue', 'value': 'Water Rescue'},
            {'label': 'Mountain or Wilderness Rescue', 'value': 'Mountain or Wilderness Rescue'},
            {'label': 'Disaster or Individual Tracking', 'value': 'Disaster or Individual Tracking'},
            {'label': 'Reset', 'value': 'Reset'}
        ],
        placeholder="Select a Rescue Type"
    ),
    dash_table.DataTable(id='datatable-id', data=data),
    dcc.Graph(id='map-id')
])

if __name__ == '__main__':
    app.run_server(debug=True)

Tests
1.	Run the dashboard: Open and run the ProjectTwoDashboard.ipynb file in Jupyter Lab or Codio to launch the dashboard. The dashboard will open in a browser window with the Grazioso Salvare logo and a unique identifier displaying the developer name (“Thalia Stafford”).
2.	Verify the starting state: Confirm that the unfiltered data table loads successfully and displays all animal outcome records from MongoDB.
3.	Test each filter: Use the interactive dropdown to select each of the following filters and verify that both the data table and charts update dynamically:
a.	Water Rescue
b.	Mountain or Wilderness Rescue
c.	Disaster or Individual Tracking
4.	Test the reset option: Choose “Reset” to confirm the dashboard returns to its original, unfiltered view.
5.	Confirm chart responsiveness: Check that the geolocation chart and secondary chart refresh automatically with each selection.
6.	Screenshots/Screencast: Capture four screenshots (or one screencast) showing each filter result and the reset view, ensuring your logo and identifier are visible in each one.

Screenshots
     

Roadmap/Features 
•	Callback errors with NoneType data: Occurred when filters returned no data. Fixed by adding checks to handle empty or missing results before rendering.
•	Data formatting for Dash DataTable: Adjusted MongoDB cursor data to a list of dictionaries to ensure compatibility.
•	Dynamic updates not triggering: Corrected callback structure to properly link input and output components.
Reflection
How do you write programs that are maintainable, readable, and adaptable?
Writing maintainable, readable, and adaptable programs starts with using modular code design and clear documentation. In this project, the CRUD Python module made the database interactions reusable and easy to understand by separating data logic from the dashboard interface. This structure improved organization and simplified debugging. The advantage of working this way was that when I needed to change or reuse database operations, I could do so without editing the entire dashboard. This CRUD module could also be adapted for other projects that use MongoDB, such as data tracking systems or client analytics dashboards.

How do you approach a problem as a computer scientist?
I approach problems by breaking them down into smaller, testable components and focusing on functionality first before refining presentation. For the Grazioso Salvare project, I started by connecting MongoDB to Python through the CRUD module to confirm data retrieval. Then I built out the dashboard visuals in Dash step by step, testing each feature as I added it. Compared to previous projects, this one required more integration between database and front-end components, so I used iterative testing to make sure the callbacks worked correctly. In the future, I would use this same modular, test-driven approach to build scalable database solutions for different client needs.

What do computer scientists do, and why does it matter?
Computer scientists design and develop solutions that make data accessible, interactive, and meaningful. In this project, my work directly supported a company’s ability to make data-driven decisions—helping Grazioso Salvare identify adoption patterns, rescue types, and trends faster than manual analysis. Projects like this matter because they turn large, static datasets into tools that improve operations and decision-making, which ultimately increases efficiency and impact for real-world organizations.


Contact
Thalia Stafford
