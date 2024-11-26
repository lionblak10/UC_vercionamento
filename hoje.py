i = 0
n1 = [int(input(f"Digite o número {i+1}: ")) for i in range(10)]   

for i in range(len(n1)):
    if n1[i] % 2 == 0:
        n1[i] = "coco"

        quantidade_coco = n1.count("coco")
        print(f"Quantidade de 'coco' no array: {quantidade_coco}")