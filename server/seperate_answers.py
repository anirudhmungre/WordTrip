from tqdm import tqdm

num_answers = 3
file_name = str(num_answers) + 'Answers'

def isAnagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return (str1_list == str2_list)

all_words = []
with open('./words/wordlist.txt', 'r') as f:
    all_words = [line.strip().upper() for line in f]

files = [open('./words/2Answers.txt', 'w'), open('./words/3Answers.txt', 'w'), open('./words/4Answers.txt', 'w'), open('./words/5+Answers.txt', 'w')]
for i in tqdm(all_words):
    a = [ans for ans in all_words if isAnagram(i, ans)]
    if (len(a) > 1 and len(a) < 5):
        files[len(a)-2].write(i + '\n')
        # print(f"WRITING: {i}")
    elif(len(a) > 4):
        files[3].write(i + '\n')


files[0].close()
files[1].close()
files[2].close()
files[3].close()