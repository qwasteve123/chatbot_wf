import json
import requests
from jp_characters import zen_to_hankaku


def find_in_word_dict(text=None,id=None):
    url = "http://127.0.0.1:50021/user_dict"
    response = response = requests.get(url)
    word_dict = json.loads(response.content)

    if response.ok:
        print("successful access.")
    else:
        print("Error in access.")

    word_found = 0
    if not text:
        if id in word_dict:
            print(f"uuid : {id}")
            for key, item in word_dict[id].items():
                print(f"{key} : {item}")
            word_found +=1
            print("#######################################")
    elif not id:
        for uuid, word in word_dict.items():
            if text in zen_to_hankaku(word['surface']):
                print(f"uuid : {uuid}")
                for key, item in word.items():
                    print(f"{key} : {item}")
                word_found +=1
                print("#######################################")
    print(f"Total of {word_found} words are found in word dict.")

def add_to_word_dict(data):
    url = "http://127.0.0.1:50021/user_dict_word"

    uuid = response = requests.post(url,params=data)

    print(response.status_code)
    if response.ok:
        print("User dictionary word updated successfully.")
        print(uuid)
    else:
        print("Error updating user dictionary word.")

def remove_from_word_dict(uuid):
    url = "http://127.0.0.1:50021/user_dict_word/"+uuid

    response = requests.get(url)
    response = requests.delete(url)

    print(response.status_code)
    if response.ok:
        print("User dictionary word removed successfully.")
        print(uuid)
    else:
        print("Fail to remove word.")

if __name__ =="__main__":
    
    # data = (
    #     ("surface", "jump"),
    #     ("pronunciation", "ジャンプ"),
    #     ("accent_type", "3")
    # )
    # add_to_word_dict(data)

    # find_in_word_dict("jump")

    remove_from_word_dict("93d765c2-dee1-48a1-9ad6-2336b9fbf680")




