
# pip install google-cloud-translate
# from google.cloud import translate


# def translate_text(text, project_id="YOUR_PROJECT_ID"):
    

#     client = translate.TranslationServiceClient()

#     location = "global"

#     parent = f"projects/{project_id}/locations/{location}"

#     response = client.translate_text(
#         request={
#             "parent": parent,
#             "contents": [text],
#             "mime_type": "text/plain",  
#             "source_language_code": "en-US",
#             "target_language_code": "fr",
#         }
#     )

#     for translation in response.translations:
#         print("Translated text: {}".format(translation.translated_text))

from requests import get

ip = get('https://api.ipify.org').text
print ('My public IP address is:', ip)