from dotenv import load_dotenv
load_dotenv()

from openai import AsyncOpenAI
import requests
import pprint

client = AsyncOpenAI()

import json

system_message = """
You are an AI assistant specializing in helping users search for awards on nsf.gov (National Science Foundation website). Your role is to act as a knowledgeable, friendly, and human-like helper. Use the information provided in the <KNOWLEDGE> tags to assist users with their NSF award searches.

<KNOWLEDGE>
General Search Tips
Detailed information is available on Simple Search, Advanced Search and Wildcard Searches

Viewing Results
By default, search results are displayed in list format. You can switch to a tabular view of the data by clicking on the "Table" icon at the top of the results list.
In table view, you can select which columns to display by using the "Customize Columns" feature.

What does the "Relevance" score mean?
Relevance is a score assigned by the search engine. It is based on how frequently the query terms appears in the document as well as other factors. The score is given in comparison to other documents found by the search.

Exporting Results
Up to 3,000 results can be immediately exported in one of the supported formats (CSV, XML, Excel and Text). If you have sorted the result set (e.g. by award number or dollar amount), that order will be preserved in the export.
For searches returning more than 3,000 results, you can also get a complete set of results (XML format only), by selecting the "Export All" feature. Because this file can be very large, processing takes place in off-hours. Please enter your email address to be sent a link when the export file is ready for download. Your email address will not be used for any other purpose. Awards made in a given calendar year are available on the Download Awards page.

Recovery Act (ARRA) Awards
To find Recovery Act awards, click on the "ARRA Awards" link on the Popular Searches page.

Copyright
Award data posted on the NSF web site, including award abstract text, is in the public domain and not subject to copyright. Publications and conference proceedings listed as resulting from an award are subject to copyright as indicated by the publisher.

Obtaining copies of proposals
The Award Search provides only the abstracts for awards. The proposals themselves are the confidential intellectual property of the submitting organizations. The easiest way to get a copy of a proposal is to contact the primary investigator for the award and ask that person if he or she will share it with you. Example proposals are available in NSF's FastLane demo system.

Cookies
This application uses session cookies to "remember" search values as individual users navigate between the various search tabs. The session variables are used only for the duration of the individual session and only for navigation within the application. No personally identifiable information is collected, and no information is retained by NSF after the session is complete. All information will be handled in accordance with the NSF Privacy Policy.

Browser Compatibility
The application is compatible with Internet Explorer versions 7 and above, Mozilla Firefox versions 3.6 and above and Safari versions 5 and above.

No Results on the Last Page
Our search engine predicts the total number of results and is accurate up to the first 3,000 results. Past that number, the results might vary by a small margin. If you don't find results on the last page, please click on the Previous page for results.

My old bookmark doesn't work
If you are trying to access a bookmark from the previous version of the application, please note that the application has been revamped and some of the searches have either been discontinued or modified to serve you better. Please bookmark the links from this version of the application for future access.

How do I search for multiple award numbers?
Enter the numbers into the form on the Simple search page. The numbers should be separated by spaces, not commas.

More Help
If you are not getting the results you expect, please use the comment form to give us much detail as you can about the search you are performing. We will try to resolve the problem for you. If you want to be contacted on your issue, please provide your email address.

Public Access requirement
Per NSF's Public Access Plan , journals submitted in the NSF Public Access Repository (NSF-PAR) will be displayed on the Award detail section. A link to view the citations details via NSF-PAR will be provided. If the journal is available electronically from the publisher, the Digital Object Identifier (DOI) hyperlink will also be available for the publisher-maintained site. For additional information on Public Access, please refer to Public Access FAQs .

Simple Search
Simple search searches on multiple fields associated with an award. This search is not case sensitive; searching for "Biology" or "biology" yields the same results. For an exact keyword or phrase search, enclose the search term(s) in double quotes. Keywords such as "the", "and", "of", "a" are ignored in free text searches. The search will accept alphabetic and numeric characters, as well as spaces and these punctuation marks: " , ( ) - / \ & : . ', plus the use of the wildcard characters * and ?. For more details, please see the section on performing wildcard searches. Simple search performs search on the following data fields:
* Award Number
* Award Title
* NSF Organization Abbreviation and Full Name
* Award Start Date and Award End Date
* Award Amount
* Award Instrument
* Program Officer First Name and Last Name
* Abstract
* Initial and Last Amendment Date
* Principal Investigator/ Co PI Name and email address
* Institution Name, Address (Street, City, State, Zip Code) and Phone Number
* Country
* Field of Application description text
* Program Name
* Program Element Code and Description
* Program Reference Code and Description


Wildcard Searches
Keyword and Program Officer searches which do not contain any numeric characters:
* You can use the asterisk (*) at the beginning or the end of a search term, or both. Examples: "bio*" will find "biology " and "biodegradable"; "*bio" will find "nano-biology", *bio* will find all three of these words.
* You can replace a single character with a question mark (?). For example, c?ll will return results for "call", "calling", "cell", "cellular", "cull".
Keyword searches which are entirely numeric:
* You can use the asterisk (*) only at the end of a search term. Examples: searches are 098*, 123*. (Wildcards are not currently in supported for searches that combine letters and numbers, such as "A123*.)
Lookup screen searches:
* You can use the asterisk (*) as well as the '%' wildcard, which finds matches at word boundaries. For example, "John%" will find "St. Johns" but not "Upjohn".

Advanced Search
This search is not case sensitive; searching for "Biology" or "biology" yields the same results. The First Name, Last Name, Organization and Program text boxes will accept alphabetic and numeric characters, as well as spaces and these punctuation marks: " , ( ) - / \ & : . '. The Keyword field and Program Officer field allow all of these characters plus the use of the wildcard characters * and ?. For more details, please see the section on performing wildcard searches. NSF uses program element codes and program reference codes to track which NSF programs funded specific awards. The most accurate search results are obtained when searching by an exact program name or code. For NSF-wide programs such as CAREER or REU, a reference code search provides the most accurate results. The advanced search form provides a lookup function to find and then search by program name, element code or reference code. If you are unsure of the exact program name, a wildcard search will provide a list of all possible matches, or you can browse an A-Z list of program names. Please see the instructions on the lookup screen to perform this search. Another way to search by program is to broaden your initial search to bring in results from several programs. Look for the desired program name in the results list (note: use "Table" view) and click on the program name to repeat the search for the exact program name. Help for individual fields can be accessed by mousing over the icon preceding the field name. Lookups for individual fields can be accessed by clicking on the icon to the left of the search field.

Boolean Searches
The simple search field and the keyword field support the following Boolean searches:
* AND
* NOT
* OR

AND The AND binary operator ensures that every award returned contains all the terms. For e.g. *cat AND dog* will ensure that all the awards returned have the terms *cat* and *dog* in it.
NOT The NOT unary operator ensures that every award returned exculdes the term following *NOT*. For e.g. *cat NOT dog* will ensure that all the awards returned have the term *cat* and not the term *dog*
OR The OR binary operator ensure that atleast one of the terms is included in the award. For e.g. *cat OR dog* will ensure that all the awards returned will have at least one of the terms *cat*, *dog*
Note: All the boolean search operators are case sensitive and have to be all capitalized.
</KNOWLEDGE>

Guidelines for interacting with users:

1. Greet users warmly and ask how you can assist them with their NSF award search.
2. Use the information in the <KNOWLEDGE> tags to provide accurate and helpful responses.
3. Offer step-by-step guidance on how to perform searches, explaining each step clearly.
4. Use natural language and a conversational tone, avoiding overly technical jargon unless necessary.
5. Show empathy and patience, especially when users are struggling or frustrated.
6. Suggest relevant search terms or filters based on the user's research interests.
7. Explain the meaning of different award types or NSF-specific terminology when relevant.
8. If unable to directly access nsf.gov, clearly state that you're providing general guidance based on your knowledge of the website.
9. After providing search advice, ask if the user found what they were looking for or if they need further assistance.

Remember, your goal is to make the NSF award search process as smooth and effective as possible while maintaining a friendly, human-like interaction.
"""

functions = [
            {
                "type": "function",
                "function": {
                    "name": "search_awards",
                    "description": "Search for awards using various criteria from NSF and NASA databases. Parameters not provided will default to empty strings. Only call this function once per user message.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "keyword": {
                                "type": "string",
                                "description": "Keywords to search for",
                                "default": ""
                            },
                            "id": {
                                "type": "string",
                                "description": "Award unique identifier (ex. 1336650). Required if ProjectOutcomes is requested for an award resource.",
                                "default": ""
                            },
                            "agency": {
                                "type": "string",
                                "enum": ["NSF", "NASA", ""],
                                "description": "Agency name",
                                "default": ""
                            },
                            "awardeeCity": {
                                "type": "string",
                                "description": "Awardee city name (ex. Arlington)",
                                "default": ""
                            },
                            "awardeeCountryCode": {
                                "type": "string",
                                "enum": ["AU", "BD", "BR", "CA", "GM", "SW", "SZ", "UK", "US", "USA", ""],
                                "description": "Awardee country code",
                                "default": ""
                            },
                            "awardeeDistrictCode": {
                                "type": "string",
                                "description": "Awardee congressional district code (ex. VA01,NY22)",
                                "default": ""
                            },
                            "awardeeName": {
                                "type": "string",
                                "description": "Name of the entity receiving award (ex. 'university+of+south+florida')",
                                "default": ""
                            },
                            "awardeeStateCode": {
                                "type": "string",
                                "description": "Abbreviation of the awardee state (ex. VA)",
                                "default": ""
                            },
                            "awardeeZipCode": {
                                "type": "string",
                                "description": "9 digit awardee zip code with the pattern of 5 digit + 4 (ex. 231730001)",
                                "default": ""
                            },
                            "cfdaNumber": {
                                "type": "string",
                                "enum": ["43.001", "43.002", "43.003", "43.007", "43.008", "43.009", "47.041", "47.049", "47.050", "47.070", "47.074", "47.075", "47.076", "47.078", "47.079", "47.080", "47.081", ""],
                                "description": "Catalog of Federal Domestic Assistance (CFDA) number",
                                "default": ""
                            },
                            "coPDPI": {
                                "type": "string",
                                "description": "Co-Principal Investigator Name (ex. Christopher)",
                                "default": ""
                            },
                            "dateStart": {
                                "type": "string",
                                "description": "Start date for award date to search (mm/dd/yyyy)",
                                "default": ""
                            },
                            "dateEnd": {
                                "type": "string",
                                "description": "End date for award date to search (mm/dd/yyyy)",
                                "default": ""
                            },
                            "startDateStart": {
                                "type": "string",
                                "description": "Start date for award start date to search (mm/dd/yyyy)",
                                "default": ""
                            },
                            "startDateEnd": {
                                "type": "string",
                                "description": "End date for award start date to search (mm/dd/yyyy)",
                                "default": ""
                            },
                            "expDateStart": {
                                "type": "string",
                                "description": "Start date for award expiration date to search (mm/dd/yyyy)",
                                "default": ""
                            },
                            "expDateEnd": {
                                "type": "string",
                                "description": "End date for award expiration date to search (mm/dd/yyyy)",
                                "default": ""
                            },
                            "estimatedTotalAmtFrom": {
                                "type": "string",
                                "description": "Minimum estimated total amount",
                                "default": ""
                            },
                            "estimatedTotalAmtTo": {
                                "type": "string",
                                "description": "Maximum estimated total amount",
                                "default": ""
                            },
                            "fundsObligatedAmtFrom": {
                                "type": "string",
                                "description": "Minimum funds obligated amount",
                                "default": ""
                            },
                            "fundsObligatedAmtTo": {
                                "type": "string",
                                "description": "Maximum funds obligated amount",
                                "default": ""
                            },
                            "ueiNumber": {
                                "type": "string",
                                "description": "Unique Identifier of Entity (ex. F2VSMAKDH8Z7)",
                                "default": ""
                            },
                            "fundProgramName": {
                                "type": "string",
                                "description": "Fund Program Name (ex. 'ANTARCTIC+COORDINATION')",
                                "default": ""
                            },
                            "parentUeiNumber": {
                                "type": "string",
                                "description": "Unique Identifier of Parent Entity (ex. JBG7T7RXQ2B7)",
                                "default": ""
                            },
                            "pdPIName": {
                                "type": "string",
                                "description": "Project Director/Principal Investigator Name (ex. 'SUMNET+STARFIELD')",
                                "default": ""
                            },
                            "perfCity": {
                                "type": "string",
                                "description": "Performance City Name (ex. Arlington)",
                                "default": ""
                            },
                            "perfCountryCode": {
                                "type": "string",
                                "enum": ["AU", "BD", "BR", "CA", "GM", "SW", "SZ", "UK", "US", "USA", ""],
                                "description": "Performance country code",
                                "default": ""
                            },
                            "perfDistrictCode": {
                                "type": "string",
                                "description": "Performance congressional district code (ex. VA01,NY22)",
                                "default": ""
                            },
                            "perfLocation": {
                                "type": "string",
                                "description": "Performance location name (ex. 'university+of+south+florida')",
                                "default": ""
                            },
                            "perfStateCode": {
                                "type": "string",
                                "description": "Performance State Code (ex. VA)",
                                "default": ""
                            },
                            "perfZipCode": {
                                "type": "string",
                                "description": "9 digit performance zip code with the pattern of 5 digit + 4 (ex. 231730001)",
                                "default": ""
                            },
                            "poName": {
                                "type": "string",
                                "description": "Program Officer Name (ex. 'Hamos+Rick')",
                                "default": ""
                            },
                            "primaryProgram": {
                                "type": "string",
                                "description": "Comma separated numbers that include FUND_SYMB_ID to return FUND Code + FUND Name (ex. 040106, 040107)",
                                "default": ""
                            },
                            "transType": {
                                "type": "string",
                                "enum": ["BOA/Task Order", "Continuing Grant", "Contract", "Contract Interagency Agreement", "Cooperative Agreement", "Fellowship", "Fixed Price Award", "GAA", "Interagency Agreement", "Standard Grant", ""],
                                "description": "Transaction Type",
                                "default": ""
                            }
                        },
                        "required": []
                    }
                }
            }
        ]

def search_awards(params):
  clean = {}
  for key in params.keys():
    if params[key] != "":
      clean[key] = params[key]
  r = requests.get('http://api.nsf.gov/services/v1/awards.json', params=clean)
  response = r.json()
  if isinstance(response, dict):
    return json.dumps(response)
  else:
    return json.dumps({"error": "Unexpected response format", "data": response})


async def process_text(prev_messages):
    messages=[
            {"role": "system", "content": system_message},
            *prev_messages
        ]
    result = await client.chat.completions.create(
        model="gpt-4o",
        tool_choice="auto",
        tools=functions,
        messages=messages
    )
    response_message = result.choices[0].message
    tool_calls = result.choices[0].message.tool_calls
    if tool_calls:
        available_functions = {
            "search_awards": search_awards,
        }  # only one function in this example, but you can have multiple
        messages.append(response_message) 
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = tool_call.function.arguments
            function_response = function_to_call(
                json.loads(function_args)
            )
            yield {"event": "search_result",  "content": function_response}
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": json.dumps(function_response),
                }
            )  # extend conversation with function response
        second_response = await client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )  # get a new response from the model where it can see the function response
        yield {"event": "chat", "content": second_response.choices[0].message.content}
    else:
        yield {"event": "chat", "content": response_message.content}