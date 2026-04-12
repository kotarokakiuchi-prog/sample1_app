import json
import os
import sys

FILENAME = 'todo.json'

# 保存用のファイルが存在しない場合は自動で作成
if not os.path.exists(FILENAME):
    with open(FILENAME, 'w') as f:
        json.dump([], f)

# リストの読み込み
def load_list():
    with open(FILENAME, 'r') as f:
        return json.load(f)
    
# リストへの書き込み
def write_list(list):
    with open(FILENAME, 'w') as f:
        json.dump(list , f, indent =4, ensure_ascii =False)

# タスクの追加
def add_list(task):
    list = load_list()
    if {"task": task} in list:
        print('そのタスクは既に書き込まれています')
    else:
        list.append({"task": task})
        write_list(list)
        print('タスクを追加しました')

# タスクの削除
def delete_list(task):
    list = load_list()
    if {"task": task} in list:
        list.remove({"task": task})
        write_list(list)
        print('タスクを削除しました')
    else:
        print('そのタスクは存在しません')

# タスクの表示
def print_list():
    list = load_list()
    if not list:
        print('タスクが登録されていません')
    else:
        print('登録されているタスクは以下の通りです')
        for i,t in enumerate(list):
            print(f"{i}: {t['task']}")


command = '0'

while command != '4':
    print('機能を選んでください')
    command = input('1：タスク登録, 2：タスク削除, 3：タスク表示, 4：終了 -> ')
    print()

    if command == '1':
        task = input('登録するタスクを入力してください：')
        add_list(task)
        print()

    elif command == '2':
        task = input('削除するタスクを入力してください：')
        delete_list(task)
        print()

    elif command == '3':
        print_list()
        print()

    else:
        print('終了します')
        sys.exit(0)