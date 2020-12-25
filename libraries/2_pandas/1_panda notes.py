1 ->data frame -->  |--|---|----|  --> whole excel table is refereed as data frame
                |--|---|----|

2 ->series     -->  |---|   --> single column
                |---|

3 ->import pandas

    data = pandas.read_csv("filename.csv")

    data.to_dict()     -->after reading it will convert the data in dictionary form


4 ->import pandas

    data = pandas.read_csv("filename.csv")

    data["temp"].to_list()    -->it will select the column and change to list

5 ->selecting column    ||
                        \/
   print(data["temp"])
        or
   print(data.temp)

6 --> selecting rows

    data[data.day =="monday"]  -->will print all row

7 --> create a data frame from scrtatch

   data_dict ={
   "students": ["any", "james"],
   "scores": [25, 26 ]
   }

   data = pandas.DataFrame(data_dict)
   data.to_csv("new file name .csv")
