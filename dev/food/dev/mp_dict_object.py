import multiprocessing
# import ast
import json

# def modify_json(input_json, output_dict):
#     ps = input_json
#     output_dict = ast.literal_eval(ps)
#     print('from within worker function ')
#     print(output_dict)
    
# def multi_product_jsonl():
#     j = "{'a': '1', 'b': '2', 'c': '3'}"

#     output_dict = multiprocessing.Manager().dict()
#     p = multiprocessing.Process(target=modify_json, args= (j, output_dict))
#     p.start()
#     p.join(5) # wait x seconds to timeout
#     print(output_dict)
#     if p.is_alive():
#         print("modification timed out")
#         p.terminate()
#         p.join()

#     print('from outside worker function ')
    

# def main():
#     multi_product_jsonl()

# if __name__ == '__main__':
#     main()
#     '''
#     '''



# def f(input_json, output_dict):
#     ps = json.dumps(input_json)
#     output_dict = json.loads(ps)
#     print(output_dict)

# def final():
#     input_json = {'a': '2', 'b': 3}
#     output_dict = multiprocessing.Manager().dict()


#     p = multiprocessing.Process(target=f, args=(input_json,output_dict))
#     p.start()
#     p.join()

#     print(output_dict)


# def f(input_json, output_dict):
#     ps = input_json
#     output_dict = ps
#     print(ps)
#     print(output_dict)

# def final():
#     input_json = {'a': '2', 'b': 3}
#     output_dict = multiprocessing.Manager().dict()

#     p = multiprocessing.Process(target=f, args=(input_json,output_dict))
#     p.start()
#     p.join()
#     print(output_dict)

# def f(input_json, output_dict):
#     ps = input_json
#     output_dict = {}
#     output_dict = ps
#     print(ps)
#     print(output_dict)

# def final():
#     input_json = {'a': '2', 'b': 3}
#     output_dict = multiprocessing.Manager().dict()

#     p = multiprocessing.Process(target=f, args=(input_json,output_dict))
#     p.start()
    
#     p.join()
#     print(output_dict)

# problem
# Timeout a function with dictionary input and output 

# def f(input, output):
#     # ps = json.dumps(input)
#     # output = json.loads(ps)
#     output['c'] = input
    
#     print(output)

# def final():
#     input = {'a': '1', 'b': '2'}
#     output = multiprocessing.Manager().dict()

#     # args must serializable by pickle, convert python objects into format that can deconstructed and reconstructed in another script
#     p = multiprocessing.Process(target=f, args=(input,output)) 
#     p.start()
#     p.join()
#     print(output)

# def f(ip, op):
#     ps = ip
#     op['b'] = ps
#     print(ps)
#     print(op)

# def final():
#     ip = {'a': '2', 'b': 3}
#     op = multiprocessing.Manager().dict()

#     p = multiprocessing.Process(target=f, args=(ip,op))
#     p.start()
#     p.join()
#     print(op)




# def main():
#     final()

# if __name__ == '__main__':
#     main()

# args must serializable by pickle, convert python objects into format that can deconstructed and reconstructed in another script


# def f(input, output):
#     print(f"{multiprocessing.current_process().name}: {output}")
#     ps = json.dumps(input)
#     a = output['d']
#     a = json.loads(ps)
#     output = a

#     # output = input
#     # d['a'] = {1:3}
#     print(f"{multiprocessing.current_process().name}: {output}")

# if __name__ == '__main__':
#     with multiprocessing.Manager() as manager:
#         output = manager.dict({'d': '5'})
#         input = {'a': '1', 'b': '2'}
#         print(f"{multiprocessing.current_process().name}: {output}")

#         p = multiprocessing.Process(target=f, args=(input, output)) 
#         p.start()
#         p.join()
#         output = dict(output)
#     print(f"{multiprocessing.current_process().name}: {output}")




# def f(ip, op):
#     ps = json.dumps(ip)
#     op['b'] = json.loads(ps)
#     print(ps)
#     print(op)

# if __name__ == '__main__':
#     ip = {'a': '2', 'b': 3}
#     op = multiprocessing.Manager().dict()

#     p = multiprocessing.Process(target=f, args=(ip,op))
#     p.start()
#     p.join()
#     print(op['b'])


# def f(ip, queue):
#     ps = json.dumps(ip)
#     queue.put(json.loads(ps))


# if __name__ == '__main__':
#     ip = {'a': '2', 'b': 3}
#     queue = multiprocessing.Queue()

#     p = multiprocessing.Process(target=f, args=(ip,queue))
#     p.start()
#     p.join()
#     print(queue.get())

def f(ip, queue):
    ps = json.dumps(ip)
    queue.put(json.loads(ps))

def final():
    for _ in range(3):
        ip = {'a': '2', 'b': 3}
        queue = multiprocessing.Queue()

        p = multiprocessing.Process(target=f, args=(ip,queue))
        p.start()
        p.join(10)
        print(queue.get())

        if p.is_alive():
            print("modification timed out")
            p.terminate()
            p.join()

if __name__ == '__main__':
    final()