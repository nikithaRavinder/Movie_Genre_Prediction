import sys
import os
import json

#data = {"id": {"name": "", "plot": "", "genres": []}}
data = {}
data_value = []
master_dict = {}
genre_name_list =


with open("MovieSummaries/plot_summaries.txt", "r") as f_plots:
    plots = f_plots.readlines()
    for line in plots:
        id = line.split("\t")[0]
        plot_data = line.split("\t")[1]
        if id not in data:
            data[id] = plot_data
    #print(data)

with open("MovieSummaries/movie.metadata.tsv", "r") as f_genre:
    genres = f_genre.readlines()
    for line in genres:
        id = line.split("\t")[0]
        movie_name = line.split("\t")[2]
        data_value.append(movie_name) # appends movie name
        genres = line.split("\t")[-1].replace("{}", "")
        #print(type(genres))
        if len(genres) > 10:
            genre_list = genres.split(",")
            #print(genre_list)
            for each in genre_list:
                name = each.split(":")[1]
                if "}" in name:
                    name.replace("}", "")
                data_value.append(name)  #appends genre name
        if id in data:
            data_value.append(data[id]) #appends plot to data_value
        if id not in master_dict:
            master_dict[id] = data_value

# string = ""
# for key in master_dict:
#     string += str(key) + ": " + str(master_dict[key])
#
# print(string)

# with open("dict.txt", "w") as output:
#     json_data = json.dumps(master_dict)
#     output.write(json_data)








