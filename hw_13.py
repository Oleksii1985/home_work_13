import json


def main():

    def some_func(*args, **kwargs):
        result = {}
        list_ = []
        list_4 = []
        kol = 0
        for i in args:
            list_4.append(i)
            if kol < int(len(args) / len(kwargs)) - 1:
                kol += 1
                continue
            list_.append(list_4)
            list_4 = []
            kol = 0

        index_ = 0
        for k, v in kwargs.items():
            result[v] = list_[index_]
            index_ += 1
        return result

    def load_dict(some_dict, json_path):
        try:
            with open(json_path, "r")as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(json_path, "w")as file:
                json.dump(results, file, indent=1)
        else:
            data.update(results)
            with open(json_path, "w") as file:
                json.dump(data, file, indent=1)

    results = some_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                        name="name", make="make", good="good", done="done", ok="ok")

    load_dict(results, json_path="./total.json")


if __name__ == "__main__":
    main()
