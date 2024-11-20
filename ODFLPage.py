from openai import AzureOpenAI
import time

 
class Extraction:
    def __init__(self):
        self.client = AzureOpenAI(
                api_key = "66314cfa0b174ee98f65e0395dc892aa",  
                api_version = "2024-02-01",
                azure_endpoint = "https://openai-test-odf.openai.azure.com/"
                )
       
    def get_text_queries_response(self, client, text_content):
        try:
            messages = self.get_prompt(text_content)
            response = client.chat.completions.create(
                model='openai-test-odf', messages=messages, temperature=0.0001
            )
            final_response = response.choices[0].message.content
            #print(f"Successfully processed text_content: {text_content}")
            return final_response
        except Exception as err:
            print(f"Error occurred while calling Azure OpenAI: {err}")
            time.sleep(10)
            return self.get_text_queries_response(client, text_content)
   
    def get_prompt(self,text_content):
        messages =[
 
            {"role": "assistant", "content": f"""You are an assistant tasked to answer the queries related to the context given: {text_content}.
                What is Company Name?
                What is Address line 1?
                What is Suburb?
                What is State?
                What is Post Code?
                What is Country Name?
                What is GnF Code?
                What is Input Tax Credit?
                If there is any criminal offence within past 5 years?
                If there is any liablity for any civil offence or pecuniary penalty (exceeding $5,000)?
                Have the customer been involved in a company or business which became insolvent or subject to any form of insolvency administration (e.g. liquidation or receivership)?
                Have the customer had an insurance policy cancelled, declined or terms imposed?
                Have the customer ever been declared bankrupt?
                What is Insured Name?
                What is Add Loss Value?
                What is the Occupation?
                What is Business Establishment year?
                What is Annual Turnover?
                Give number of full Full Time Employees
                Give number of Part Time Employees
                What is State name?
                What is percentage of turnover?
                What is approximate state turnover?
                What is Stamp Duty Exemption Number?
                What is Zone Name?
                What is Location Type?
                Give Occupation Description.
                What is GNAF Code?
                What is Sum Insured for Building(s)?
                What is Sum Insured for Contents?
                Check for storm.
                What is Sum Insured for Contents - including stock for Theft?
                What is Glass Cover Type?
                What is Glass Sum Insured?
                What is Number Of Employees?
                What is Number of Directors?
                Has the business or any director who will receive protection under this section had any prevoius tax audits?
                What is Excess Amount?
                Is Property in physical or legal care, custody or control of customer?
                Are there Exports to USA/Canada?
                What are Annual Gross Profits?
                What are Annual Gross Revenue?
                What is Loss of Rent Receivable?
                Do the customer want to add Interested Party?
                Instructions:
                1. For each field above if its answer is not mentioned in text then provide answer 'Not Available'.
                2. Any field above is not available in text then provide answer 'not available in OCR'.
                3. For fields whose answer is yes and no, if not able to find answer, search for the answer in complete line of text or two lines.
                4. For fields whose answer is yes and no, search for 'selected' or 'unselected' in front of yes and no. If 'selected' is present in front of yes then answer is yes otherwise no.
                5. When searching company name, search in first line of text.Company Name are mostly the first 3 words of text.
                6. When searching for occupation, under Business Details section search for keyword 'business'.
                7. When searching for Business Establishment year, under Situation Details section search for keyword 'year built'.
                8. When searching- Building Sum Insured and Content Sum Insured, after 'Business Property' keyword search for keyword 'Sum Insured' and after this keyword search for 'Building(s)' and 'Contents'.
                9. When searching Excess Amount, search for all selected Excess Amount given in the text. Give all Excess Amount.
                10. When searching Exports to USA/Canada, search for keyword 'USA/Canada Exports'. Answer in Yes, No or Not available
                11. For field 'Do the customer want to add Interested Party', give answer in Yes or No.
        """}
 
        ]
        return messages
   
    def get_gpt_response(self, text_content):
        print("get_gpt_response start")
        try:
            text_response = self.get_text_queries_response(self.client, text_content)
            print(f"get_gpt_response successfully returned: {text_response}")
            return text_response
        except Exception as err:
            print(f"Error occurred in get_gpt_response: {err}")
            raise err
text_content = '''Community Broker Network
Business Pack Insurance Application Form
 Please answer all questions. Blanks and/or dashes, or answers "known to underwriters or brokers" or "N/A" are not
acceptable and will delay processing of this application.
 If there is insufficient room to complete a question, please attach a signed & dated addendum.
 Any documents attached to the proposal form part of this application.
 Where appropriate, please tick the yes or no box which best indicates your reply.
1. Your Details
1.1. Period Insurance
Start Date 16/03/2024 Expiry Date 16/03/2025 Effective Date 16/03/2024
1.2. Insured
Insured Name
Jacaranda Medical Centre Alstonville Pty Ltd
Trading Name
What is your web site address?
What is your Input Tax Credit? 0
What is your ABN?
Are you exempt from stamp duty? X Yes No If Yes, specify number: NSWSmallBus
Address Line 1
13 Commercial Road
Address Line 2
Suburb ALSTONVILLE State NSW Post Code 2477
1.3. Duty of Disclosure
Have you or any partner(s) or director(s) of the business:
(1) Ever had an insurance policy cancelled, declined or terms imposed? Yes X No
Date Description
(2) Ever been declared bankrupt? Yes X No
Date Description
(3) Ever been involved in a company or business which became insolvent or subject
to any form of insolvency or voluntary administration (e.g. liquidation or
receivership)?
Yes X No
Date Description
Printed date 12/03/24 Document template version: 2.43.00.00 Page 2 of 19
(4) Been convicted of any criminal offence within the past 5 years (other than minor
traffic convictions)? Yes X No
Date Description
(5) Been liable for any civil offence or pecuniary penalty (exceeding $5,000)? Yes X No
Date Description
(6) Any other matters you should disclose? Yes X No
Date Description
1.4. Claims Experience
Have you had any claims in the last 3 years under the sections to be insured? Yes X No
Claim # 1
Sections
Business Property Business Interruption
Theft Money
Machinery Breakdown Electronic Equipment
Public and Products Liability Glass
General Property Employee Dishonesty
Goods In Transit Management Liability'''
get_extract_obj = Extraction()      
text_response = get_extract_obj.get_gpt_response(text_content)
print("%%%%%",text_response)