import pandas as pd
import matplotlib.pyplot as plt



class DataVisulaizingTool:
    def __init__(self , file) -> None:
        self.file = file


    def get_data(self) -> object:
        data = pd.read_csv(self.file)
        return data
    
    # histogram of teenagers

    def histogram(self , func)-> None:
    
        matplotlib.pyplot.hist(func['Range_preg'])
        matplotlib.pyplot.title("Teenage pregnancy")
        matplotlib.pyplot.show()



def main():
    vfx_Tool =  DataVisulaizingTool("Teenage_pregnancy.csv")
    # showing the graph
    vfx_Tool.histogram(DataVisulaizingTool.get_data(vfx_Tool))




if __name__=="__main__":
    main()