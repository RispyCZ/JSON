from main import load_json_file
import json
if __name__ == "__main__":
    zaci = load_json_file("zaci.json")
    new_zaci = []
    for random_id, zak in enumerate(zaci["zaci"]):
        new_zak = {"id": random_id+1}
        new_zak.update(zak)
        new_zaci.append(new_zak)

    f = open("zaci.json", "w", encoding="utf-8")
    json.dump({"zaci": new_zaci}, f, indent=4, sort_keys=True, ensure_ascii=False)
    f.close()