print ('Start learning')
print ('-------------------------')
from openai import AzureOpenAI
 
 
# client = AzureOpenAI(
#                 api_key = "66314cfa0b174ee98f65e0395dc892aa",  
#                 api_version = "2024-02-01",
#                 azure_endpoint = "https://openai-test-odf.openai.azure.com/"
#                 )
client = AzureOpenAI(
                api_key = "c8798953ef2941f29b29e020a767251d",  
                api_version = "2024-05-01-preview",
                azure_endpoint = "https://commentary-automation-poc.openai.azure.com/"
                )
messages=[{"role": "user", "content": "what is capital of India? and give 10 lines with headers of India's capital; headers in bullet and red color"}]
response = client.chat.completions.create(model='commentary-automation-gpt-35-turbo',
                                           messages=messages, temperature=0.0001)
final_response = response.choices[0].message.content
print(f"Successfully processed text_content: {final_response}")