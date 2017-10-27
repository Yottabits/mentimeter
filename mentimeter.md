Mentimeter findings
===================

Ask for question id url: govote.at/?id=XX-XX-XX
Response: ID of the question: govote.at/YYYYYY (in Hex probably)

To vote:
Send POST Request to: govote.at/questions
With at least in Header: Cookies: ct=0 (or other number, not sure if every number works though.)
And this data: 'code' and 'value', the values can be obtained from the webpage above.
