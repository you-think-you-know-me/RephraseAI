import os
import requests
import pyocr
import pyocr.builders
from PIL import Image

# Initialize the OCR tool with the Cuneiform engine
tool = pyocr.get_available_tools()[0]
lang = 'eng'
tool_builder = pyocr.builders.TextBuilder()
tool_builder.tesseract_layout = 6
tool_builder.tesseract_char_whitelist = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
tool_builder.tesseract_config = '--psm 1'
tool_builder.tesseract_pagesegmode = 'single_word'
tool_builder.cuneiform_params = ['-f', 'text']

# Open the image file
with Image.open('resume.jpg') as img:
    # Read the text from the image using pyocr
    text = tool.image_to_string(img, lang=lang, builder=tool_builder)
    # Print the text
    print(text)



bearer_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhNcHdjdFl4YWlRdWg4Y0M0ejN0UCJ9.eyJpc3MiOiJodHRwczovL2F1dGgucmVwaHJhc2UuYWkvIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDE0NzIyODU2NjU5OTMyMDI0NDMiLCJhdWQiOlsiaHR0cHM6Ly9kaXkucmVwaHJhc2UuYWkvYXV0aDAiLCJodHRwczovL3JlcGhyYXNlYWktcHJvZC51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjc5NzQ3NzYzLCJleHAiOjE2Nzk4MzQxNjMsImF6cCI6IjNLVTVqdkVxV0pCQ1VLblBYMjZvbmFTUHkzakozMEo0Iiwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSByZWFkOnJlcGhyYXNlLmFpIGFsbDpkaXkgcmVhZDpyZXBocmFzZS5haSJ9.omlhFuvLtgUp30ihi7OnYb1oESItjDoimLYbmXrUs8fvXDnrGRT7ShzUNGfm15ZDaCojWRhYeF4fB5UYjDYDVi3pDp2kpN-LcUCAmYuz2xeN57cUT4g0NLDHgfhTckyyU38yQRWg0TXDM12Je_4ENZJ_9dEmIsHgryFoRZ5bYxoz-AZr0EPb_Squ6PL5qLuiF4fOAkCw-oDCiJ8_XGhYvd5SBcxjNJeLUZ1kO8eJixx546aKNd1EDPi8lnZ5vwonakJukcOEikNkpGAVqcGkJEy_6YZNUkzDJawMucnLIl6uvLBqi7K-tqk5slunVA6scd10ZARC6p8fYMY7XudfZw"

url = "https://personalized-brand.api.rephrase.ai/v2/campaign/create"

payload = {
    "videoDimension": {"height": 1080, "width": 1920},
    "scenes": [
        {
            "elements": [
                {
                    "style": {
                        "height": "100%",
                        "width": "100%",
                        "position": "absolute",
                        "zIndex": 1,
                    },
                    "asset": {
                        "kind": "Image",
                        "use": "Background",
                        "url": "https://th.bing.com/th/id/R.ea86a53f02071f2f0d9bf860338fc0be?rik=EEg77DkznmsYfw&riu=http%3a%2f%2fgetwallpapers.com%2fwallpaper%2ffull%2f3%2ff%2f1%2f295080.jpg&ehk=cnMZI7piskSd00X4J9jwOS58CrgUclD0fJwZRz7I8Lg%3d&risl=&pid=ImgRaw&r=0",
                    },
                },
                {
                    "style": {
                        "position": "absolute",
                        "zIndex": 2,
                        "bottom": "0em",
                        "objectFit": "cover",
                        "height": "37.5em",
                        "width": "66.66666666666667em",
                        "left": "16.666666666666664em",
                    },
                    "asset": {
                        "kind": "Spokesperson",
                        "spokespersonVideo": {
                            "output_params": {
                                "video": {
                                    "resolution": {"height": 720, "width": 1280},
                                    "background": {"alpha": 0},
                                    "crop": {"preset": "MS"},
                                }
                            },
                            "model": "danielle_pettee_look_2_nt_aug_2022",
                            "voiceId": "7bc739a4-7abc-46db-bc75-e24b6f899fa9__005",
                            "gender": "female",
                            "transcript": "<speak>{}</speak>".format(text),
                            "transcript_type": "ssml_limited",
                        },
                    },
                },
            ]
        },
    ],
    "title": "Into to MJ",
    "thumbnailUrl": "https://blog.siriusxm.com/wp-content/uploads/2022/11/MichaelJacksonChannel-1117.jpg",
}
headers = {
    "accept": "application/json",
    "Authorization": bearer_token,
    "content-type": "application/json",
}

response = requests.post(url, json=payload, headers=headers)

print(f"CAMPAIGN_ID= {response.text}")