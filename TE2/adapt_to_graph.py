import ast
# # Run file to copy and turn newly created tree from .txt (for DP) to .graph (for BnB)
def adapt(source, sizes = [100, 300, 900]):
    source_file = open(source, "r")
    
    for size in sizes:   # small:first 100 vertex, medium:first 300 vertex, big:first 900 vertex
        data = source_file.readline()
        adj_list = ast.literal_eval(data)[:size]
        save_file = open(f"TE2\BnBDataset_size{size}.graph", "w")
        to_save = ''
        number_of_edges = 0
        for i in range(size):
            for adj in adj_list[i]:
                if adj < size:
                    to_save += f'{adj}'
                    if i < adj:
                        number_of_edges += 1
                if adj != adj_list[i][-1]:
                    to_save += ' '
                else:
                    to_save += '\n'
        to_save = f'{size} {number_of_edges} 0' + '\n' + to_save
        save_file.write(to_save)
        save_file.close()
    source_file.close()
    print("Translated")
if __name__ == "__main__":
    adapt("TE2\dataset.txt")