import json

data = {}
master_dict = {}

with open("MovieSummaries/plot_summaries.txt", "r") as f_plots:
    plots = f_plots.readlines()
    for line in plots:
        id = line.split("\t")[0]
        plot_data = line.split("\t")[1]
        if id not in data:
            data[id] = plot_data

with open("MovieSummaries/movie.metadata.tsv", "r") as f_metadata:
    movie_data = f_metadata.readlines()
    for line in movie_data:
        data_value = []
        id = line.split("\t")[0]
        if id in data:
            movie_name = line.split("\t")[2]
            data_value.append(movie_name)  # appends movie name
            data_value.append(data[id])  # appends plot to data_value
            genres = line.split("\t")[-1].strip()
            if genres != "{}":
                genre_list = genres.split(",")
                for each in genre_list:
                    name = each.split(":")[1].replace("\"", "").replace("}", "").strip()
                    data_value.append(name)  #appends genre name
            if id not in master_dict:
                master_dict[id] = data_value

with open("dict.txt", "w") as output:
    json_data = json.dumps(master_dict)
    output.write(json_data)








