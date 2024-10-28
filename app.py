import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from palmerpenguins import load_penguins
from shiny import App, ui, render

# Load the Palmer Penguins dataset
penguins = load_penguins()

# Define the input logic (via setting up the app's UI), and
# Store is as a UI object by assigning it to a variable
app_ui = ui.page_fluid(
    # Add a page Title
    ui.h2("PyShiny App with Plot"),
    # Input slider for selecting the number of bins
    ui.input_slider("selected_number_of_bins", "Number of Bins", min=1, max=100, value=20),
    # Output placeholders for plots
    ui.output_plot("histogram"),
    ui.output_plot("penguin_scatter")
)

# Define the output logic (via defining the server function)
def server(input, output, session):
    @output()
    @render.plot
    def histogram():
        # Generate random data for the histogram
        np.random.seed(109)
        data = 100 + 15 * np.random.randn(690)
        # Create histogram with the specified number of bins
        num_bins = input.selected_number_of_bins()
        plt.hist(data, bins=num_bins, density=True, alpha=0.7, color='mediumorchid')
        # Add labels and title
        plt.title('Histogram of Random Data') # Set title
        plt.xlabel('Value')                  # X-axis label
        plt.ylabel('Density')                # Y-axis label
        

    @output()
    @render.plot
    def penguin_scatter():
        # Create a scatter plot of penguin data
        plt.figure(figsize=(8, 5))
        sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='species', palette= 'inferno', alpha=0.7)
        plt.title('Penguin Bill Dimensions')
        plt.xlabel('Bill Length (mm)')       # X-axis label
        plt.ylabel('Bill Depth (mm)')        # Y-axis label
        plt.grid(True)

# Combine the UI object and server logic into an app
app = App(app_ui, server)

# Run the app
if __name__ == "__main__":
    app.run()
