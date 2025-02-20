import pandas as pd
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use("Agg") 
matplotlib.use("TkAgg")


df = pd.read_csv("Teenage_pregnancy.csv")
print(df.columns)
class DataVisualizingTool:
    def __init__(self, file) -> None:
        self.file = file

    def get_data(self) -> object:
        data = pd.read_csv(self.file)
        return data

    # histogram of teenagers
    def histogram(self, func) -> None:
        print("Available columns:", func.columns)
        plt.hist(func['Age Range'])  # Use the correct column
        plt.title("Teenage Pregnancy")
        plt.show()
        # or 
        plt.savefig("histogram.png")


def main():
    vfx_Tool = DataVisualizingTool("Teenage_pregnancy.csv")
    # Showing the graph
    vfx_Tool.histogram(vfx_Tool.get_data())


if __name__ == "__main__":
    main()
