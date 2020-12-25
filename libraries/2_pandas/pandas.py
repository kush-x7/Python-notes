import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])             -->type (data["temp"])  --> series


#whole table is like excel is dataframe
#single coloum is series

data_dict = data.to_dict()
print(data_dict)


temp_list =data["temp"].to_list|()
print(len(tem))
