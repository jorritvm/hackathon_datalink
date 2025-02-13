from shiny import App, ui, render
from shinyswatch import theme

# UI
def preview_data_content():
    return ui.div(
        ui.h6("Select a start and end date to preview data"),
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
            col_widths = [3, 3, 3, 1, 1],
        ),

        ui.p("This is the content for the Preview Data tab."),
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
        ui.card_body(ui.p("<<< Go back to Active power schedule")),
        ui.card_header("Delivery Point Schedule"),
        ui.layout_columns(
            ui.navset_tab(
                ui.nav_panel("Preview data", preview_data_content()),
                ui.nav_panel("Overview", "Panel B content"),
                ui.nav_panel("Create Query", "Panel C content"),
            ),
            ui.navset_tab(
                ui.nav_panel("Export", export_content()),
                ui.nav_panel("API", "api"),
                ui.nav_panel("Python", "python"),
            ),
            col_widths=[9, 3],
        ),
    ),
    theme=theme.united

)


# SERVER
def server(input, output, session):
    pass


#     @output
#     @render.plot(alt="Solar power barchart")
#     def plot_year():
#         df = get_generation_per_year()
#         bars = plt.bar(df.time, df.solar)
#         plt.bar_label(bars)
#         plt.xlabel('Year')
#         plt.ylabel('Generation (kWh)')
#
#     @output
#     @render.plot(alt="Solar power barchart")
#     def plot_month():
#         df = get_generation_per_month(input.sl_month_year())
#         bars = plt.bar(df.time, df.solar)
#         plt.bar_label(bars)
#         plt.xlabel('Month')
#         plt.ylabel('Generation (kWh)')
#
#     @output
#     @render.plot(alt="Solar power barchart")
#     def plot_day():
#         df = get_generation_per_day(input.sl_day_year(),
#                                     input.sl_day_month())
#         bars = plt.bar(df.time, df.solar)
#         plt.bar_label(bars)
#         plt.xlabel('Day')
#         plt.ylabel('Generation (kWh)')

app = App(app_ui, server, debug=True)
