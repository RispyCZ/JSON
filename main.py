import json
from prettytable import PrettyTable


def load_json_file(filename: str):
    f = open(filename, "r", encoding="utf-8")
    data = json.load(f)
    f.close()
    return data


def list_json_file(filename: str):
    zaci = load_json_file(filename)
    tabulka = PrettyTable()
    tabulka.field_names = ["ID", "Jméno", "Příjmení", "Třída"]

    for zak in zaci["zaci"]:
        tabulka.add_row([zak["id"], zak["jmeno"], zak["prijmeni"], zak["trida"]])

    print(tabulka.get_string())


def print_help():
    print("Edupage 2.0")
    print(f"1) Vypis žáku\t 2) Přidat žáka")


def add_to_json_file(values: dict, filename: str):
    data = load_json_file(filename)
    zaci = list(data["zaci"])
    zaci.append(values)
    zaci_json = {"zaci": zaci}
    f = open(filename, "w", encoding="utf-8")
    json.dump(dict(zaci_json), f, indent=4, sort_keys=True, ensure_ascii=False)
    f.close()


if __name__ == "__main__":
    while True:
        print_help()
        match int(input("Vyberte jednu z možností: ")):
            case 1:
                list_json_file("zaci.json")
            case 2:
                add_to_json_file(
                    {"jmeno": input("Jméno: "), "prijmeni": input("Příjmení: "), "trida": input("Třída: ")},
                    "zaci.json")
                # add_to_json_file({"jmeno": "Petr", "prijmeni": "Václavek", "trida": "None"}, "zaci.json")
        print_help()
