import json
import re
import os

data = {}
master_dict = {}
final_genres = ['Romance', 'Drama', 'Horror', 'Comedy', 'Science Fiction']
all_genres = []
romance_count = 0
comedy_count = 0
drama_count = 0
scifi_count = 0
horror_count = 0

with open("MovieSummaries/plot_summaries.txt", "r", encoding="latin1") as f_plots:
    plots = f_plots.readlines()
    for line in plots:
        id = line.split("\t")[0]
        plot_data = line.split("\t")[1]
        re.sub('[^A-Za-z0-9]+', ' ', plot_data)
        if id not in data:
            data[id] = plot_data

with open("MovieSummaries/movie.metadata.tsv", "r", encoding="latin1") as f_metadata:
    movie_data = f_metadata.readlines()
    for line in movie_data:
        data_value = []
        movie_genres = []
        id = line.split("\t")[0]
        if id in data:
            movie_name = line.split("\t")[2]
            genres = line.split("\t")[-1].strip()
            if genres != "{}":
                genre_list = genres.split(",")
                for each in genre_list:
                    name = each.split(":")[1].replace("\"", "").replace("}", "")
                    name = name.replace(" Film", "").replace(" film", "").strip()
                    if name in final_genres:
                        movie_genres.append(name)  #appends genre name [2] onwards
                if len(movie_genres) != 0:
                    data_value.append(movie_name)  # appends movie name [0]
                    data_value.append(data[id])  # appends plot to data_value [1]
                    data_value.append(movie_genres)
                    if id not in master_dict:
                        master_dict[id] = data_value

with open("dict.txt", "w", encoding="latin1") as output:
    json_data = json.dumps(master_dict)
    output.write(json_data)


for movie_id in master_dict.keys():
    movie_name = master_dict[movie_id][0]
    movie_genres = master_dict[movie_id][2:]
    movie_plot = master_dict[movie_id][1]
    file_name = str(movie_id) + str("_") + str(movie_name)
    for genre in movie_genres[0]:
        file_name += str("_") + str(genre)
   
    file_name = re.sub(r"[\s+\\\/]", '_', file_name)
    file_name = re.sub(r"\W", '_', file_name)
    file_name += str(".txt")
    if "Romance" in file_name:
        romance_count += 1
        if romance_count >= 2000:
            final_file_name = str("Data/Test/") + str(file_name)
            os.makedirs(os.path.dirname("Data/Test/"), exist_ok=True)
        else:
            final_file_name = str("Data/Train/Romance/") + str(file_name)
            os.makedirs(os.path.dirname("Data/Train/Romance/"), exist_ok=True)
        print(final_file_name)
        with open(final_file_name, "w+", encoding="latin1") as f:
            f.write(movie_plot)

    if "Comedy" in file_name:
        comedy_count += 1
        if comedy_count >= 3643:
            final_file_name = str("Data/Test/") + str(file_name)
            os.makedirs(os.path.dirname("Data/Test/"), exist_ok=True)
        else:
            final_file_name = str("Data/Train/Comedy/") + str(file_name)
            os.makedirs(os.path.dirname("Data/Train/Comedy/"), exist_ok=True)
        #sprint(final_file_name)
        with open(final_file_name, "w+", encoding="latin1") as f:
            f.write(movie_plot)

    if "Drama" in file_name:
        drama_count += 1
        if drama_count >= 5742:
            final_file_name = str("Data/Test/") + str(file_name)
            os.makedirs(os.path.dirname("Data/Test/"), exist_ok=True)
        else:
            final_file_name = str("Data/Train/Drama/") + str(file_name)
            os.makedirs(os.path.dirname("Data/Train/Drama/"), exist_ok=True)
        print(final_file_name)
        with open(final_file_name, "w+", encoding="latin1") as f:
            f.write(movie_plot)

    if "Science_Fiction" in file_name:
        scifi_count += 1
        if scifi_count >= 700:
            final_file_name = str("Data/Test/") + str(file_name)
            os.makedirs(os.path.dirname("Data/Test/"), exist_ok=True)
        else:
            final_file_name = str("Data/Train/Science_Fiction/") + str(file_name)
            os.makedirs(os.path.dirname("Data/Train/Science_Fiction/"), exist_ok=True)
        print(final_file_name)
        with open(final_file_name, "w+", encoding="latin1") as f:
            f.write(movie_plot)

    if "Horror" in file_name:
        horror_count += 1
        if horror_count >= 1225:
            final_file_name = str("Data/Test/") + str(file_name)
            os.makedirs(os.path.dirname("Data/Test/"), exist_ok=True)
        else:
            final_file_name = str("Data/Train/Horror/") + str(file_name)
            os.makedirs(os.path.dirname("Data/Train/Horror/"), exist_ok=True)
        print(final_file_name)
        with open(final_file_name, "w+", encoding="latin1") as f:
            f.write(movie_plot)


print("Romance = " + str(romance_count),  str(romance_count*0.3))
print("Comedy = " + str(comedy_count),  str(comedy_count*0.3))
print("Drama = " + str(drama_count),  str(drama_count*0.3))
print("Horror = " + str(horror_count), str(horror_count*0.3))
print("SciFi = " + str(scifi_count),  str(scifi_count*0.3))


"""
Romance = 6669 2000.6999999999998
Comedy = 12143 3642.9
Drama = 19140 5742.0
Horror = 4084 1225.2
SciFi = 2339 701.6999999999999
"""