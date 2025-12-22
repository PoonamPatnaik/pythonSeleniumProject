#demo_file = open('demo.txt')
# print(demo_file.read())
# demo_file.close()

with open('demo.txt','r') as reader:
    my_file = reader.readlines()
    rev_my_file = reversed(my_file)
    print(rev_my_file)
    with open('demo.txt','w') as writer:
        for line in rev_my_file :
            writer.write(line)
        demo_file = open('demo.txt')
        print(demo_file.read())

