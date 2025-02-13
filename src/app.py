from shiny import App, ui, render, reactive
from shinyswatch import theme
from random_data import get_data
import pandas as pd

# load fake data
data = get_data()

# UI
def preview_data_content():
    return ui.div(
        ui.markdown("**Select a start and end date to preview data**"),
        ui.layout_columns(
            ui.input_date("start_date", "Start Date", value="2024-11-17"),
            ui.input_date("end_date", "End Date", value="2024-11-20"),
            ui.input_select(
                "select_tz",
                "Time Zone",
                {"0": "London", "+1": "Brussels"},
            ),
            ui.input_action_button("reset_button", "Reset"),
            ui.input_action_button("apply_button", "Apply", class_="accent-button"),
            col_widths = [2, 2, 2, 2, 2],
        ),

        ui.output_data_frame("filtered_data")
    )

def export_content():
    return ui.div(
        ui.h6("Download the selected data in CSV format"),
        ui.input_action_button("download_button", "Export Data"),
    )


# main layout for the page
app_ui = ui.page_fluid(
    ui.include_css("styles.css"),
    ui.panel_title(title="Search Data"),
    ui.h6("Home / Active Power Schedule / Delivery Point Schedule"),
    ui.card(
        ui.card_header("Delivery Point Schedule"),
        ui.layout_columns(
            ui.navset_tab(
                ui.nav_panel("Preview data", preview_data_content()),
                ui.nav_panel("Overview", "Coming soon..."),
                ui.nav_panel("Create Query", "Coming soon..."),
            ),
            ui.navset_tab(
                ui.nav_panel("Export", export_content()),
                ui.nav_panel("API", "Coming soon..."),
                ui.nav_panel("Python", "Coming soon..."),
            ),
            col_widths=[9, 3],
        ),
    ),
    theme=theme.united

)


# SERVER
def server(input, output, session):

    @render.data_frame
    @reactive.event(input.apply_button)
    def filtered_data():
        start_date = pd.to_datetime(input.start_date()).tz_localize('UTC')
        end_date = pd.to_datetime(input.end_date()).tz_localize('UTC')
        df = pd.DataFrame(data)
        dff = df.copy()
        dff['date_utc'] = pd.to_datetime(dff['date_utc'])
        dff = dff[(dff['date_utc'] >= start_date) & (dff['date_utc'] <= end_date)]
        return render.DataGrid(dff)



    # @render.data_frame
    # def fake_data():
    #     df = pd.DataFrame(data)
    #     return render.DataGrid(df)


app = App(app_ui, server, debug=True)

