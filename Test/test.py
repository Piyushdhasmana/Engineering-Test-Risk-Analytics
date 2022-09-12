import unittest
import os 
import src
import pandas as pd
from src.main import Setup

try : 
    import Output
    OUTPUT_DIR_PATH = "Output/combined.csv"
except :
    "No as such module present: Try to run the main file first"
    


DIR_PATH  = "Engineering Test Files"

class functional_testing(unittest.TestCase):
    
    def test_Asia_directory(self):
        initials = "asia"
        listing =  Setup().Asia_directory()
        self.assertTrue(all([file.startswith(initials)  for file in listing]))
        

    def test_Na_directory(self):
        initials = "na"
        listing =  Setup().Na_directory()
        self.assertTrue(all([file.startswith(initials)  for file in listing]))
        
        
    def test_data_transverse(self):
        temporary_df = pd.DataFrame({"Source IP": ["0.0.0.0","0.0.0.111"], "Environment": ["NA Prod", "Asia_prod"]})
        main_df = pd.read_csv(OUTPUT_DIR_PATH)
        self.assertTrue(tuple(temporary_df.columns), tuple(main_df.columns))
        
    def test_concat_dataframe_concat(self):
        temporary_df1 = pd.DataFrame({"Source IP": ["0.0.0.0","0.0.0.111"], "Environment": ["NA Prod", "NA Prod"]})
        temporary_df2 = pd.DataFrame({"Source IP": ["0.2.021.20","10.02.04.111"], "Environment": ["Asia_prod", "Asia_prod"]})
        temp_merge = pd.DataFrame({"Source IP": ["0.0.0.0","0.0.0.111","0.2.021.20","10.02.04.111"], 
                                   "Environment": ["NA Prod", "NA Prod", "Asia_prod", "Asia_prod"]})

        output = Setup().dataframe_concat(temporary_df1,temporary_df2)
        self.assertTrue(temp_merge.equals(output))
        
        
        
        
        
        
        
        
        
        
    