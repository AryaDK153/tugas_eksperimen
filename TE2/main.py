from vertex_cover_dp import minSizeVertexCover as dp_mvc
from maketree import maketree
from BnB_Edited import main as bnb_mvc
from timeit import timeit
# from memory_profiler import memory_usage
import tracemalloc
import ast
from adapt_to_graph import adapt

'''ONLY FOR TESTING WHETHER THE CODES WORK'''

while True:
    data_source = input("press 1 for dataset.txt | press 2 for generate new\nAnswer: ")
    if data_source == "1":
        # print(f"adj_list is list? {isinstance(adj_list, list)}")
        while True:            
            method = input("1 for DP | 2 for BnB\nAnswer: ")
            if method == "1":
                print("\n# MVC with Dynamic Programming #")
                
                datas = open("TE2\dataset.txt", "r")
                i = int(input("1 for Small (10^4 vertex) | 2 for Medium (10^5 vertex) | 3 for Big (10^6 vertex)\nAnswer: "))
                if i == 1:
                    size = "10^4"
                elif i == 2:
                    size = "10^5"
                    datas.readline()
                elif i == 3:
                    size = "10^6"
                    for j in range(2):
                        datas.readline()
                print(f"========================== Dataset #{i}: {size} ==========================")
                data = datas.readline()
                # print(f"\n# Adjacency List #\n{data}")
                adj_list = ast.literal_eval(data)

                tracemalloc.start()
                print("\nalgorithm runtime =", timeit(lambda: dp_mvc(adj_list, len(adj_list)), number=1))
                print(tracemalloc.take_snapshot().statistics('traceback')[0].size / (1024 * 1024))
                # print("\nalgorithm mem usage =", max(memory_usage(dp_mvc(adj_list, len(adj_list)))))
                datas.close()
                break
            elif method == "2":
                i = int(input("1 for Small (10^4 vertex) | 2 for Medium (10^5 vertex) | 3 for Big (10^6 vertex)\nAnswer: "))
                if i == 1:
                    size = 100
                elif i == 2:
                    size = 300
                elif i == 3:
                    size = 900
                print(f"========================== Dataset #{i}: {size} ==========================")
                print("\n# MVC with Branch and Bound #") 
                print("\nalgorithm runtime =", timeit(lambda: bnb_mvc(f"TE2\BnBDataset_size{size}.graph", 200), number=1))
                # print("\nalgorithm mem usage =", max(memory_usage(bnb_mvc(adj_list))))
                break
            else:
                print("Wrong input! Please Try Again\n\n")
        
        break
    elif data_source == "2":
        while True:
            try:
                adj_list = maketree(int(input("Insert Dataset Length: ")))
                # adj_list = [[1, 4], [0, 2, 3], [1], [1], [0]]     # Dataset yang digunakan sebagai contoh pada bagian deskripsi laporan eksperimen
                print(f"\n# Adjacency List #\n{adj_list}")
                file = open("TE2\temp_dataset.txt", "w")
                file.write(adj_list)
                file.close()
                break
            except ValueError:
                print("Wrong input type! Please Try Again\n\n")
        
        while True:
            method = input("1 for DP | 2 for BnB\nAnswer: ")
            if method == "1":
                print("\n# MVC with Dynamic Programming #")
                print("\nalgorithm runtime =", timeit(lambda: dp_mvc(adj_list, len(adj_list)), number=1))
                # print("\nalgorithm mem usage =", max(memory_usage(dp_mvc(adj_list, len(adj_list)))))
                break
            elif method == "2":
                adapt("TE2\temp_dataset.txt", [len(adj_list)])
                print("\n# MVC with Branch and Bound #")
                print("\nalgorithm runtime =", timeit(lambda: bnb_mvc(f"TE2\BnBDataset_size{len(adj_list)}.graph", 200), number=1))
                # print("\nalgorithm mem usage =", max(memory_usage(bnb_mvc(adj_list))))
                break
            else:
                print("Wrong input! Please Try Again\n\n")
        break
    print("Unknown Input! Please Try Again\n\n")