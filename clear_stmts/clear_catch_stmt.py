import csv
import string

input_file = open('d4j_methods_sc_metrics_comments.csv', 'r')
# output_file = open('clear_catch_statements.csv', 'w')
data = csv.reader(input_file)
# writer = csv.writer(output_file,quoting=csv.QUOTE_ALL)# dialect='excel')

stack = []
for line in data:
        source = line[16]
        code = line[18]
        if 'catch' in source:
            catch_index = source.index("catch")
            bracket_index = catch_index
            while not stack:
                if source[bracket_index] == "{":
                     stack.append(0)
                     print(source[bracket_index:])
                else:
                     bracket_index+=1
            while stack:
                if source[bracket_index] == "{":
                    stack.append(0)
                    print(source[bracket_index:])
                elif source[bracket_index] == "}" :
                    stack.pop()
                    print(source[:bracket_index])
                bracket_index+=1
                

input_file.close()
# output_file.close()