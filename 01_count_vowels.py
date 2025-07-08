import requests

def countVowels(word):
    vowels="aeiou"
    count-0;
    for char in word:
        if char.lower() in vowels:
            count+=1
    return count


#api call request
def count_completed_tasks():
    url="https://jsonplaceholder.typicode.com/todos"
    response=requests.get(url)
    data = response.json()

    completed=0
    for task in data:
        if task["completed"]:
            completed +=1

    return completed
print (count_completed_tasks())








