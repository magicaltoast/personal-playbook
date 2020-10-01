import json
import os


fixed_gallery = {
    "serviceUrl": "https://marketplace.visualstudio.com/_apis/public/gallery",
    "itemUrl": "https://marketplace.visualstudio.com/items"
}

with open("/usr/share/vscodium-bin/resources/app/product.json","r") as file:
    file_json = json.loads(file.read())

    print(file_json["extensionsGallery"])

    file_json["extensionsGallery"] = fixed_gallery

    print(file_json["extensionsGallery"])

    result = json.dumps(file_json)

with open("/usr/share/vscodium-bin/resources/app/product1.json","w+") as file:
    file.write(result)

os.remove("/usr/share/vscodium-bin/resources/app/product.json")
os.rename("/usr/share/vscodium-bin/resources/app/product1.json","/usr/share/vscodium-bin/resources/app/product.json")