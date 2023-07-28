import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pdfkit
import os
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

# Function to generate and save the PDF
def save_as_pdf():
    # options = {
    #     'page-size': 'Letter',
    #     'orientation': 'Landscape',  # Set 'Portrait' for portrait mode
    #     'quiet': '',
    # }
    # pdfkit.from_file('/static/index.html', options=options)
    options = {
        'page-size': 'Letter',  # Page size (e.g., 'A4', 'Letter', 'Legal', etc.)
        'orientation': 'Portrait',  # Page orientation ('Portrait' or 'Landscape')
        'margin-top': '0.75in',  # Top margin of the page
        'margin-right': '0.75in',  # Right margin of the page
        'margin-bottom': '0.75in',  # Bottom margin of the page
        'margin-left': '0.75in',  # Left margin of the page
        'encoding': "UTF-8",  # Character encoding for the HTML content
        'no-outline': None,  # Disable outline (table of contents)
        'quiet': '',  # Suppress wkhtmltopdf output in the console
        'footer-right': '[page]',  # Footer content (use '[page]' for page number)
        'footer-font-size': '10',  # Font size for the footer
        'footer-spacing': '5',  # Spacing between footer and content (in mm)
        'header-right': 'My Header',  # Header content (can be left, right, or center)
        'header-font-size': '12',  # Font size for the header
        'header-spacing': '5',  # Spacing between header and content (in mm)
        'disable-smart-shrinking': None,  # Disable the smart shrinking of the content
    }

    html_file_path = os.path.abspath('index.html')
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Users\lenevo\Desktop\wkhtmltox-0.12.6-1.msvc2015-win64.exe")
    pdfkit.from_file(html_file_path, 'resume.pdf', options=options, configuration=config)
    pdfkit.from_file('index.html', 'resume.pdf', options=options, configuration=config)

    with open('index.html', 'r') as file:
        html_content = file.read()

    pdfkit.from_string(html_content, 'resume.pdf', options=options, configuration=config)


# HTML content for the download button
download_button = dbc.Button(
    "Download as PDF",
    id="download-button",
    color="primary",
    className="mb-3",
    n_clicks=0
)

# Callback to trigger the PDF generation when the button is clicked
@app.callback(
    dash.dependencies.Output('download-button', 'n_clicks'),
    dash.dependencies.Input('download-button', 'n_clicks')
)
def generate_pdf(n_clicks):
    print("I am Working")
    if n_clicks > 0:
        # save_as_pdf()
      pass
    return n_clicks

app.layout = html.Div(
    style = {'padding': '10px'},  # Add padding to the main content wrapper
    children = [
        html.Nav(
            className="navbar navbar-expand-lg bg-dark",
            **{
                "data-bs-theme": "dark",
            },
            children=[
                html.Div(
                    className="container-fluid",
                    children=[
                        html.Img(
                            src="Siddiq.jpg",  # Replace with the correct image path
                            style={'height': '60px', 'float': 'right'}
                        ),
                        html.A(
                            className="navbar-brand",
                            href="#",

                            style={'textAlign': 'center'}
                        ),

                    ]
                )
            ]
        ),

    dcc.Markdown('# Siddiq Bin Salam', style={'textAlign':'center'}),
    dcc.Markdown('Riyadh, Saudi Arabia', style={'textAlign': 'center'}),

    dcc.Markdown('### Professional Summary', style={'textAlign': 'center'}),
    html.Hr(),
    dcc.Markdown('Motivated and results-driven Sr Data analyst and Reporting Consultant with over 10 years of experience.\n'
                 ' Skilled in working under pressure and adapting to new situations and challenges to meet Company goals . '
                 'Professional Data Analyst committed to improving data quality and usage through focused exploration.\n '
                 'Completes tasks quickly with meticulous attention to detail, maintaining integrity. '
                 'Strives to increase insight across reporting and delivery using varied extraction and analysis tools..',
                 style={'textAlign': 'center', 'white-space': 'pre'}),

    dcc.Markdown('### Skills', style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            * Advanced Python Knowledge 
            * Microsoft Power BI
            * Automation through SQL/Python (Pandas, Numpy)
            * Data Visualization in Power BI
            * Python Basics for Data Science
            * Data Visualization through Python Libraries (Matplotlib, Seaborn, Plotly, ggplot,Dash)
            ''')
        ], width={"size": 3, "offset": 1}),
        dbc.Col([
            dcc.Markdown('''
            * Data Cleansing through DAX/SQL/Python/Excel
            * Server Reporting Services (SSRS)
            * Advanced PL/SQL
            * Good Understanding of ETL
            * Azure DP 900 Trained
            ''')
        ], width=3)
    ], justify='center'),

dcc.Markdown('### Certifications', style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            * Microsoft Power BI Certification number: I763-1885
            * SkillUp Azure Fundamentals: Certification number: 3041481
            * Microsoft Azure Fundamentals Certified
            * Udamy 100 Days of Coding Certified
            
            ''')
        ], width={"size": 3, "offset": 1}),
        dbc.Col([
            dcc.Markdown('''
            
            ''')
        ], width=3)
    ], justify='center'),

    dcc.Markdown('### Work History', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('May 2017 - Current', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Sr Data Analyst & Reporting Consultant \n'
                         'STC,Riyadh,SA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    "Create visually compelling and informative data visualizations, charts, and graphs to effectively communicate data insights and trends."),
                html.Li(
                    "Design and develop interactive dashboards and reports that allow users to explore and interact with data."),
                html.Li("Collaborate with different departments to comprehend appropriate requirements."),
                html.Li(
                    "Apply data visualization best practices and design principles to ensure clarity, accuracy, and usability of visualizations."),
                html.Li(
                    "Transform complex data sets into visually appealing and easy-to-understand visual representations."),
                html.Li(
                    "Use data visualization tools and software, such as Power BI or Python libraries (Dash,Matplotlib, Seaborn, Plotly), to create visualizations."),
                html.Li(
                    "Conduct data analysis and exploration to identify patterns, trends, and insights that can be effectively communicated through visualizations."),
                html.Li(
                    "Collaborate with cross-functional teams to integrate data visualizations into reports, presentations, and business applications."),
                html.Li(
                    "Present and communicate data visualizations and insights to both technical and non-technical stakeholders."),
                html.Li("Build automated reports and dashboards with the help of Power BI and other reporting tools."),
                html.Li("Data storage, collection, and data cleaning in SQL/Python/DAX."),
                html.Li("Automation of reporting using Python/SQL server and Microsoft Office."),
                html.Li(
                    "Produced detailed and relevant reports for analyzing daily, weekly, and monthly trends of main KPIs of the network using Power BI and advanced Excel functions."),
                html.Li("Maintaining SQL DB and connecting Python to SQL to import and export data."),
                html.Li(
                    "Responsible for sending daily, weekly, monthly, evaluation, and major event reports to relevant stakeholders."),
                html.Li(
                    "Responsible for designing dashboards for higher management displaying main KPIs and insights for major events to ensure network stability using Power BI and Python.")
            ])
        ], width=10)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('Oct 2014 - Apr 2017',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Performance and Reporting Engineer \n'
                         'STC/Zain, Huawei, Riyadh,SA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    "Performed initial optimization of newly deployed sites to ensure smooth network integration and generated visual reports showcasing optimization results."),
                html.Li(
                    "Planned and optimized major Key Performance Indicators (KPIs) of cells to enhance network performance."),
                html.Li(
                    "Monitored KPIs and analyzed data to identify underperforming cells and take corrective actions."),
                html.Li("Implemented new features and parameters to optimize network performance."),
                html.Li(
                    "Determined the best possible configuration for antenna height, tilts, and azimuths for all cells/sectors in the network."),
                html.Li("Optimized antenna parameters to achieve better coverage and throughput."),
                html.Li(
                    "Collaborated with the integration team to ensure newly integrated sites met agreed contractual KPIs and parameters."),
                html.Li(
                    "Analyzed drive plots and log files of different sites to identify network issues and areas for improvement."),
                html.Li(
                    "Conducted data analysis to evaluate the performance of integrated sites and suggest improvements."),
                html.Li("Managed a team of 8 DT field engineers, overseeing their performance and activities."),
                html.Li(
                    "Performed data analysis on network performance data, drive test results, log files, and other relevant data sources."),
                html.Li(
                    "Extracted actionable insights, trends, and patterns from the data to support decision-making and optimization efforts.")
            ])
        ], width=10)
    ], justify='center'),

    dcc.Markdown('### Education', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2012',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('MS in Computer and Communications Systems\n'
                         'Staffordshire, United Kingdom (Staffordshire University)',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=10)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2009',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Bachelor of Engineering\n'
                         'India (JNTU University)',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=10)
    ], justify='center'),

    dcc.Markdown('### Personal Information', style={'textAlign': 'center'}),
        html.Hr(),

        dbc.Row([
            dbc.Col([
                dcc.Markdown('Details',
                             style={'textAlign': 'center'})
            ], width=2),
            dbc.Col([
                dcc.Markdown('email address : siddiqbinsalam@gmail\n'
                             'Mobile phone : 0533165167\n'
                             'Portfolio : [Link to Portfolio](https://siddiqbinsalam.github.io/siddiq_bin_salam_resume/#)',
                             style={'white-space': 'pre'},
                             className='ms-3'),
            ], width=10)
        ], justify='center'),

    download_button,
])

if __name__ == '__main__':
    app.run_server(debug=False)