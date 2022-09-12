import os
import pandas as pd
from pathlib import Path

DIR_PATH  = "Engineering Test Files"


class Setup():
    """ 
        This Particular class is used for following reasons 
        - standardizing the directory components in which csv file are present,
        - creating an output dir if not present
        - merging the dataframes together
    """
    for file in os.listdir(DIR_PATH):
        os.rename(os.path.join(DIR_PATH,file.strip()), os.path.join(DIR_PATH,file.lower()))
        
    files = [file for file in os.listdir(DIR_PATH)]

    
    def Asia_directory(self):
        """
        Returns: The list of all the asia specific_files of the main directory 
        """

        Asia_dir = [file for file in self.files if file.startswith("asia")]
        return Asia_dir

    def Na_directory(self):
        """
        Returns: The list of all the NA specific_files of the main directory 
        """

        Na_dir = [file for file in self.files if file.startswith("na")]
        return Na_dir
    
    @staticmethod
    def dataframe_concat(df_1, df_2):
        """
        concatenate the dataframe together

        Args:
            df_1 (_type_): dataframe A
            df_2 (_type_): dataframe B

        Returns:
            _type_: A single concatenated dataframe
        """
        merge_df = pd.concat([df_1,df_2],ignore_index = True)
        return merge_df
    
    @staticmethod
    def saving_output(df):
        """
        Saves the dataframe as csv in specific directory
        """
        outdir = './Output'
        if not os.path.exists(outdir):
            os.mkdir(outdir)
        return df.to_csv("Output/combined.csv", index = False)
        

def data_transverse():
    Asia_dir = Setup().Asia_directory()
    Na_dir = Setup().Na_directory()

    asia = []
    for file in Asia_dir:
        try:
            Asia_dataframe=pd.read_csv(os.path.join(DIR_PATH,file) ,index_col=None)
        except IOError:
            print("File can't be open either it is not a csv file or file is corrupt.")
            continue

        Asia_dataframe.rename(columns={Asia_dataframe.columns[0]: 'Source IP'}, inplace=True)
        asia.append(Asia_dataframe["Source IP"])    
    asia = pd.DataFrame(pd.concat(asia))
    asia["Environment"] = "Asia Prod"
    
      
    na = []
    for file in Na_dir:
        try :
            Na_dataframe = pd.read_csv(os.path.join(DIR_PATH,file) ,index_col=None)
        except IOError:
            print("File can't be open either it is not a csv file or file is corrupt.")
            continue
        
        Na_dataframe.rename(columns={Na_dataframe.columns[0]: 'Source IP'}, inplace = True)
        na.append(Na_dataframe["Source IP"])
    na = pd.DataFrame(pd.concat(na))
    na["Environment"] = "NA Prod"
    

    consolidated_df = Setup().dataframe_concat(asia, na)
    return Setup().saving_output(consolidated_df)


if __name__ == "__main__":
    try :
        data_transverse()
        print ("Your programme has been executed successfully")
    except:
        print("Something went wrong")