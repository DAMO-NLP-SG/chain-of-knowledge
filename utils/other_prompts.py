domain_selection_demonstration = """
Follow the below example, select relevant knowledge domains from Available Domains to the Q.
Available Domains: factual, medical, physical, biology

Q: This British racing driver came in third at the 2014 Bahrain GP2 Series round and was born in what year
Relevant domains: factual

Q: Which of the following drugs can be given in renal failure safely?
Relevant domains: medical

Q: Which object has the most thermal energy? 
Relevant domains: factual, physical

Q: Is the following trait inherited or acquired? Barry has a scar on his left ankle. 
Relevant domains: biology

"""


################################
########### HotpotQA ###########
################################

hotpotqa_s1_prompt_demonstration = """
Strictly follow the format of the below examples, provide two rationales before answering the question.
Q: This British racing driver came in third at the 2014 Bahrain GP2 Series round and was born in what year
A: First, at the 2014 Bahrain GP2 Series round, DAMS driver Jolyon Palmer came in third. Second, Jolyon Palmer (born 20 January 1991) is a British racing driver. The answer is 1991.

Q: What band did Antony King work with that formed in 1985 in Manchester?
A: First, Antony King worked as house engineer for Simply Red. Second, Simply Red formed in 1985 in Manchester. The answer is Simply Red.

Q: How many inhabitants were in the city close to where Alberta Ferretti’s studios was located?
A: First, Alberta Ferretti’s studio is near Rimini. Second, Rimini is a city of 146,606 inhabitants. The answer is 146,606.

"""

hotpotqa_s2_edit_prompt_demonstration = """
Strictly follow the format of the below examples. The given sentence may have factual errors, please correct them based on the given external knowledge.
Sentence: the Alpher-Bethe-Gamow paper was invented by Ralph Alpher.
Knowledge: discoverer or inventor of Alpher-Bethe-Famow paper is Ralph Alpher. 
Edited sentence: the Alpher-Bethe-Gamow paper was invented by Ralph Alpher.

Sentence: Ralph Alpher was advised by Hans Bethe.
Knowledge: doctoral advisor of Ralph Alpher is George Gamow.
Edited sentence: Ralph Alpher was advised by George Gamow.

"""

################################
############ Fever #############
################################

#############1-shot#############

fever_s1_prompt_demonstration_1_shot = """
Determine if there is Observation that SUPPORTS or REFUTES a Claim, or if there is NOT ENOUGH INFO. Strictly follow the format of the below examples, provide two rationales before answering the question.
Q: Black Mirror is about society.
A: First, Black Mirror is a British anthology television series. Second, The series uses technology to comment on contemporary social issues. The answer is SUPPORTS.

"""

#############3-shot#############

fever_s1_prompt_demonstration = """
Determine if there is Observation that SUPPORTS or REFUTES a Claim, or if there is NOT ENOUGH INFO. Strictly follow the format of the below examples, provide two rationales before answering the question.
Q: The Gadsden flag was named by Christopher Gadsden.
A: First, The Gadsden flag is named after politician Christopher Gadsden. Second, there is no information on who named the Gadsden flag. The answer is NOT ENOUGH INFO.

Q: Reg Watson is a current television producer.
A: First, Reginald James Watson AM was an Australian television producer and screenwriter. Second, Reginald James Watson AM died on 8 October 2019. The answer is REFUTES.

Q: Black Mirror is about society.
A: First, Black Mirror is a British anthology television series. Second, The series uses technology to comment on contemporary social issues. The answer is SUPPORTS.

"""

fever_s2_edit_prompt_demonstration = """
Strictly follow the format of the below examples. The given sentence may have factual errors, please correct them based on the given external knowledge.
Sentence: Reg Watson was an Australian singer.
Knowledge: Occupation of Reg Watson is Television producer, screenwriter, and executive.
Edited sentence: Reg Watson was an Australian television producer, screenwriter, and executive.

Sentence: The Gadsden flag is named by Christopher Gadsden.
Context: Gadsden flag is designed by Christopher Gadsden.
Edited sentence: The Gadsden flag is designed by Christopher Gadsden, but there is no information on who named it.

Sentence: the Alpher-Bethe-Gamow paper was invented by Ralph Alpher.
Knowledge: discoverer or inventor of Alpher-Bethe-Famow paper is Ralph Alpher. 
Edited sentence: the Alpher-Bethe-Gamow paper was invented by Ralph Alpher.

"""

#############6-shot#############

fever_s1_prompt_demonstration_6_shot = """
Determine if there is Observation that SUPPORTS or REFUTES a Claim, or if there is NOT ENOUGH INFO. Strictly follow the format of the below examples, provide two rationales before answering the question.
Q: The Gadsden flag was named by Christopher Gadsden.
A: First, The Gadsden flag is named after politician Christopher Gadsden. Second, there is no information on who named the Gadsden flag. The answer is NOT ENOUGH INFO.

Q: Reg Watson is a current television producer.
A: First, Reginald James Watson AM was an Australian television producer and screenwriter. Second, Reginald James Watson AM died on 8 October 2019. The answer is REFUTES.

Q: Black Mirror is about society.
A: First, Black Mirror is a British anthology television series. Second, The series uses technology to comment on contemporary social issues. The answer is SUPPORTS.

Q: Shahid Kapoor has acted professionally.
A: First, Shahid Kapoor is an Indian actor who appears in Hindi films. Second, there is no information on how he acted. The answer is NOT ENOUGH INFO.

Q: Sierra Leone's first Bishop was Sir Milton Margai.
A: First, Sir Milton Augustus Strieby Margai PC was a Sierra Leonean medical doctor and politician. Second, there is no information on him being the bishop. The answer is NOT ENOUGH INFO.

Q: True Detective's second season was set in the most populous state of the United States.
A: First, True Detective is an American anthology crime drama television series. Its second season is set in California. Second, California is the most populous U.S. state. The answer is SUPPORTS.

"""

fever_s2_edit_prompt_demonstration_6_shot = """
Strictly follow the format of the below examples. The given sentence may have factual errors, please correct them based on the given external knowledge.
Sentence: Reg Watson was an Australian singer.
Knowledge: Occupation of Reg Watson is Television producer, screenwriter, and executive.
Edited sentence: Reg Watson was an Australian television producer, screenwriter, and executive.

Sentence: The Gadsden flag is named by Christopher Gadsden.
Context: Gadsden flag is designed by Christopher Gadsden.
Edited sentence: The Gadsden flag is designed by Christopher Gadsden, but there is no information on who named it.

Sentence: the Alpher-Bethe-Gamow paper was invented by Ralph Alpher.
Knowledge: discoverer or inventor of Alpher-Bethe-Famow paper is Ralph Alpher. 
Edited sentence: the Alpher-Bethe-Gamow paper was invented by Ralph Alpher.

Sentence: Shahid Kapoor is an Indian actor who appears in Hindi films.
Knowledge: Shahid Kapoor is an Indian actor who appears in Hindi films.
Edited sentence: Shahid Kapoor is an Indian actor who appears in Hindi films.

Sentence: Sir Milton Margai was the Bishop of Sierra Leone.
Knowledge: Sir Milton Augustus Strieby Margai PC (7 December 1895 – 28 April 1964) was a Sierra Leonean medical doctor and politician who served as the country's head of government from 1954 until his death in 1964.[1] He was titled chief minister from 1954 to 1960, and then prime minister from 1961 onwards.
Edited sentence: There is no information on Sir Milton Margai being the Bishop of Sierra Leone.

Sentence: Texas is the most populous U.S. state.
Knowledge: California is a state in the Western United States. With over 38.9 million residents[6] across a total area of approximately 163,696 square miles (423,970 km2),[11] it is the most populous U.S. state, the third-largest U.S. state by area, and the most populated subnational entity in North America.
Edited sentence: California is the most populous U.S. state.

"""

################################
########### FetaQA #############
################################
fetaqa_no_table_demonstration = """
Strictly follow the format of the below example to answer the question.

Q: Who won the 1982 Illinois gubernatorial election, and how many votes was the margin?
A: Thompson prevailed in the 1982 Illinois gubernatorial election by a 5,074 vote margin.

Q: How did Michael and Mario Andretti do?
A: Michael Andretti finished with a run of 214.522 mph, faster than Mario.

Q: How many copies did "Pleasure" sell in 1998 alone, and how long was it the best selling album in Japan?
A: B'z The Best "Pleasure" sold more than 5 million copies in 1998 alone, making it a temporary best-selling album in Japanese music history, until being surpassed by Utada Hikaru's First Love in 1999.

Q: How many passengers can that plane hold?
A: The Tigerair Australia fleet consists of the following aircraft and Virgin Australia announced that the entire A320 fleet will be replaced with Boeing 737-800 aircraft.

Q: When and in what play did Platt appear at the Music Box Theatre?
A: In 2016 and 2017, Platt played in Dear Evan Hansen on Broadway at the Music Box Theatre.

Q: What are the download rates of EUTRAN?
A: EUTRAN has download rates of 299.6 Mbit/s and 150.8 Mbit/s.
"""

fetaqa_standard_demonstration = """
Strictly follow the format of the below example to answer the question.

Table: [['Party', 'Party', 'Candidate', 'Votes', '%', '±'], ['-', 'Republican', 'James R. Thompson (incumbent)', '1,816,101', '49.44', '-'], ['-', 'Democratic', 'Adlai Stevenson III', '1,811,027', '49.30', '-'], ['-', 'Libertarian', 'Bea Armstrong', '24,417', '0.66', '-'], ['-', 'Taxpayers', 'John E. Roche', '22,001', '0.60', '-'], ['-', 'N/A', 'write-ins', '161', '0.00', 'n-a'], ['Majority', 'Majority', 'Majority', '5,074', '0.14', '-'], ['Turnout', 'Turnout', 'Turnout', '3,673,707', '-', '-'], ['-', 'Republican hold', 'Republican hold', 'Swing', '-', '-']]
Q: The table is about Results of 1982 Illinois gubernatorial election. Who won the 1982 Illinois gubernatorial election, and how many votes was the margin?
A: Thompson prevailed in the 1982 Illinois gubernatorial election by a 5,074 vote margin.

Table: [['Finish', 'Start', 'No', 'Name', 'Qual', 'Laps', 'Status'], ['1', '4', '3', 'United States Bobby Rahal', '213.550', '200', '170.722 mph'], ['2', '6', '7', 'United States Kevin Cogan', '211.922', '200', '+1.441 seconds'], ['3', '1', '4', 'United States Rick Mears (W)', '216.828', '200', '+1.881 seconds'], ['4', '8', '5', 'Colombia Roberto Guerrero', '211.576', '200', '+10.558 seconds'], ['5', '9', '30', 'United States Al Unser, Jr.', '211.533', '199', 'Flagged'], ['6', '3', '18', 'United States Michael Andretti', '214.522', '199', 'Flagged'], ['7', '11', '20', 'Brazil Emerson Fittipaldi', '210.237', '199', 'Flagged'], ['8', '12', '21', 'United States Johnny Rutherford (W)', '210.220', '198', 'Flagged'], ['9', '2', '1', 'United States Danny Sullivan (W)', '215.382', '197', 'Flagged']]
Q: The table is about Race box score of 1986 Indianapolis 500. How did Michael and Mario Andretti do?
A: Michael Andretti finished with a run of 214.522 mph, faster than Mario.

Table: [['No.', 'Album', 'Artist', 'Released', 'Chart', 'Sales'], ['1', 'First Love', 'Hikaru Utada', '10 March 1999', '1', '7,672,000'], ['2', 'B\'z The Best "Pleasure"', "B'z", '20 May 1998', '1', '5,136,000'], ['3', 'Review', 'Glay', '1 October 1997', '1', '4,876,000'], ['4', 'Distance', 'Hikaru Utada', '28 March 2001', '1', '4,472,000'], ['5', 'B\'z The Best "Treasure"', "B'z", '20 September 1998', '1', '4,439,000'], ['6', 'A Best', 'Ayumi Hamasaki', '28 March 2001', '1', '4,312,000'], ['7', 'Globe', 'Globe', '31 March 1996', '1', '4,136,000'], ['8', 'Deep River', 'Hikaru Utada', '19 June 2002', '1', '3,605,000'], ['9', 'Umi no Yeah!!', 'Southern All Stars', '25 June 1998', '1', '3,592,000']]
Q: The table is about List of best-selling albums by domestic acts of List of best-selling albums in Japan. How many copies did "Pleasure" sell in 1998 alone, and how long was it the best selling album in Japan?
A: B'z The Best "Pleasure" sold more than 5 million copies in 1998 alone, making it a temporary best-selling album in Japanese music history, until being surpassed by Utada Hikaru's First Love in 1999.

Table: [['Aircraft', 'In Service', 'Orders', 'Passengers', 'Notes'], ['Airbus A320-200', '10', '—', '180', 'All to be replaced by Boeing 737-800. Aircraft to be transferred to Virgin Australia Regional Airlines.'], ['Boeing 737-800', '5', '—', '186', 'Aircraft transferred from Virgin Australia'], ['Total', '15', '-', '-', '-']]
Q: The table is about Fleet of Tigerair Australia. How many passengers can that plane hold?
A: The Tigerair Australia fleet consists of the following aircraft and Virgin Australia announced that the entire A320 fleet will be replaced with Boeing 737-800 aircraft.

Table: [['Year', 'Production', 'Role', 'Venue', 'Notes'], ['2002', 'The Music Man', 'Winthrop Paroo', 'Hollywood Bowl', 'Los Angeles'], ['2004', 'Caroline, or Change', 'Noah Gellman', 'Ahmanson Theatre', 'National tour'], ['2005', 'Dead End', 'Philip Griswald', 'Ahmanson Theatre', 'Regional'], ['2012', 'The Power of Duff', 'Ricky Duff', 'Powerhouse Theatre', 'Regional'], ['2012', 'The Black Suits', 'Chris Thurser', 'Center Theatre Group', 'Regional'], ['2012–2013', 'The Book of Mormon', 'Elder Arnold Cunningham', 'PrivateBank Theatre', 'Chicago'], ['2014–2015', 'The Book of Mormon', 'Elder Arnold Cunningham', "Eugene O'Neill Theatre", 'Broadway'], ['2015', 'Dear Evan Hansen', 'Evan Hansen', 'Arena Stage', 'Washington, D.C.'], ['2016', 'The Secret Garden', 'Dickon', 'David Geffen Hall', '25th anniversary concert']]
Q: The table is about Theatre credits of Ben Platt (actor). When and in what play did Platt appear at the Music Box Theatre?
A: In 2016 and 2017, Platt played in Dear Evan Hansen on Broadway at the Music Box Theatre.

Table: [['User equipment Category', 'Max. L1 data rate Downlink (Mbit/s)', 'Max. number of DL MIMO layers', 'Max. L1 data rate Uplink (Mbit/s)', '3GPP Release'], ['NB1', '0.68', '1', '1.0', 'Rel 13'], ['M1', '1.0', '1', '1.0', 'Rel 13'], ['0', '1.0', '1', '1.0', 'Rel 12'], ['1', '10.3', '1', '5.2', 'Rel 8'], ['2', '51.0', '2', '25.5', 'Rel 8'], ['3', '102.0', '2', '51.0', 'Rel 8'], ['4', '150.8', '2', '51.0', 'Rel 8'], ['5', '299.6', '4', '75.4', 'Rel 8'], ['6', '301.5', '2 or 4', '51.0', 'Rel 10']]
Q: The table is about User Equipment (UE) categories of E-UTRA. What are the download rates of EUTRAN?
A: EUTRAN has download rates of 299.6 Mbit/s and 150.8 Mbit/s.
"""

fetaqa_cot_demonstration = """
Strictly follow the format of the below example to answer the question.

Table: [['Party', 'Party', 'Candidate', 'Votes', '%', '±'], ['-', 'Republican', 'James R. Thompson (incumbent)', '1,816,101', '49.44', '-'], ['-', 'Democratic', 'Adlai Stevenson III', '1,811,027', '49.30', '-'], ['-', 'Libertarian', 'Bea Armstrong', '24,417', '0.66', '-'], ['-', 'Taxpayers', 'John E. Roche', '22,001', '0.60', '-'], ['-', 'N/A', 'write-ins', '161', '0.00', 'n-a'], ['Majority', 'Majority', 'Majority', '5,074', '0.14', '-'], ['Turnout', 'Turnout', 'Turnout', '3,673,707', '-', '-'], ['-', 'Republican hold', 'Republican hold', 'Swing', '-', '-']]
Q: The table is about Results of 1982 Illinois gubernatorial election. Who won the 1982 Illinois gubernatorial election, and how many votes was the margin?
A: First, the major candidates were James R. Thompson and Adlai Stevenson III. James R. Second, Thompson had 1,816,101 votes while Adlai Stevenson III had 1,811,027. Thus, Thompson prevailed in the 1982 Illinois gubernatorial election by a 5,074 vote margin.

Table: [['Finish', 'Start', 'No', 'Name', 'Qual', 'Laps', 'Status'], ['1', '4', '3', 'United States Bobby Rahal', '213.550', '200', '170.722 mph'], ['2', '6', '7', 'United States Kevin Cogan', '211.922', '200', '+1.441 seconds'], ['3', '1', '4', 'United States Rick Mears (W)', '216.828', '200', '+1.881 seconds'], ['4', '8', '5', 'Colombia Roberto Guerrero', '211.576', '200', '+10.558 seconds'], ['5', '9', '30', 'United States Al Unser, Jr.', '211.533', '199', 'Flagged'], ['6', '3', '18', 'United States Michael Andretti', '214.522', '199', 'Flagged'], ['7', '11', '20', 'Brazil Emerson Fittipaldi', '210.237', '199', 'Flagged'], ['8', '12', '21', 'United States Johnny Rutherford (W)', '210.220', '198', 'Flagged'], ['9', '2', '1', 'United States Danny Sullivan (W)', '215.382', '197', 'Flagged']]
Q: The table is about Race box score of 1986 Indianapolis 500. How did Michael and Mario Andretti do?
A: First, Michael and Mario Andretti were both drivers in the 1986 Indianapolis 500 race. Second, Michael had a speed of 214.522 mph while Mario had a speed of 212.300 mph. Thus, Michael Andretti finished with a run of 214.522 mph, faster than Mario.

Table: [['No.', 'Album', 'Artist', 'Released', 'Chart', 'Sales'], ['1', 'First Love', 'Hikaru Utada', '10 March 1999', '1', '7,672,000'], ['2', 'B\'z The Best "Pleasure"', "B'z", '20 May 1998', '1', '5,136,000'], ['3', 'Review', 'Glay', '1 October 1997', '1', '4,876,000'], ['4', 'Distance', 'Hikaru Utada', '28 March 2001', '1', '4,472,000'], ['5', 'B\'z The Best "Treasure"', "B'z", '20 September 1998', '1', '4,439,000'], ['6', 'A Best', 'Ayumi Hamasaki', '28 March 2001', '1', '4,312,000'], ['7', 'Globe', 'Globe', '31 March 1996', '1', '4,136,000'], ['8', 'Deep River', 'Hikaru Utada', '19 June 2002', '1', '3,605,000'], ['9', 'Umi no Yeah!!', 'Southern All Stars', '25 June 1998', '1', '3,592,000']]
Q: The table is about List of best-selling albums by domestic acts of List of best-selling albums in Japan. How many copies did "Pleasure" sell in 1998 alone, and how long was it the best selling album in Japan?
A: First, Pleasure was an album by the Japanese rock duo B'z that sold more than 5,136,000 copies in 1998. Second, it held the top position for 10 months until being surpassed by First Love. Thus, B'z The Best "Pleasure" sold more than 5 million copies in 1998 alone, making it a temporary best-selling album in Japanese music history, until being surpassed by Utada Hikaru's First Love in 1999.

Table: [['Aircraft', 'In Service', 'Orders', 'Passengers', 'Notes'], ['Airbus A320-200', '10', '—', '180', 'All to be replaced by Boeing 737-800. Aircraft to be transferred to Virgin Australia Regional Airlines.'], ['Boeing 737-800', '5', '—', '186', 'Aircraft transferred from Virgin Australia'], ['Total', '15', '-', '-', '-']]
Q: The table is about Fleet of Tigerair Australia. How many passengers can that plane hold?
A: First, Tigerair Australia uses the same planes as Virgin Australia. Second, Virgin Australia will use Boeing 737-800 planes in the future. Thus, The Tigerair Australia fleet consists of the following aircraft and Virgin Australia announced that the entire A320 fleet will be replaced with Boeing 737-800 aircraft.

Table: [['Year', 'Production', 'Role', 'Venue', 'Notes'], ['2002', 'The Music Man', 'Winthrop Paroo', 'Hollywood Bowl', 'Los Angeles'], ['2004', 'Caroline, or Change', 'Noah Gellman', 'Ahmanson Theatre', 'National tour'], ['2005', 'Dead End', 'Philip Griswald', 'Ahmanson Theatre', 'Regional'], ['2012', 'The Power of Duff', 'Ricky Duff', 'Powerhouse Theatre', 'Regional'], ['2012', 'The Black Suits', 'Chris Thurser', 'Center Theatre Group', 'Regional'], ['2012–2013', 'The Book of Mormon', 'Elder Arnold Cunningham', 'PrivateBank Theatre', 'Chicago'], ['2014–2015', 'The Book of Mormon', 'Elder Arnold Cunningham', "Eugene O'Neill Theatre", 'Broadway'], ['2015', 'Dear Evan Hansen', 'Evan Hansen', 'Arena Stage', 'Washington, D.C.'], ['2016', 'The Secret Garden', 'Dickon', 'David Geffen Hall', '25th anniversary concert']]
Q: The table is about Theatre credits of Ben Platt (actor). When and in what play did Platt appear at the Music Box Theatre?
A: First, Ben Platt played in Dear Evan Hansen. Second, Dear Evan Hansen was held at the Music Box Theatre. Thus, In 2016 and 2017, Platt played in Dear Evan Hansen on Broadway at the Music Box Theatre.

Table: [['User equipment Category', 'Max. L1 data rate Downlink (Mbit/s)', 'Max. number of DL MIMO layers', 'Max. L1 data rate Uplink (Mbit/s)', '3GPP Release'], ['NB1', '0.68', '1', '1.0', 'Rel 13'], ['M1', '1.0', '1', '1.0', 'Rel 13'], ['0', '1.0', '1', '1.0', 'Rel 12'], ['1', '10.3', '1', '5.2', 'Rel 8'], ['2', '51.0', '2', '25.5', 'Rel 8'], ['3', '102.0', '2', '51.0', 'Rel 8'], ['4', '150.8', '2', '51.0', 'Rel 8'], ['5', '299.6', '4', '75.4', 'Rel 8'], ['6', '301.5', '2 or 4', '51.0', 'Rel 10']]
Q: The table is about User Equipment (UE) categories of E-UTRA. What are the download rates of EUTRAN?
A: First, EUTRAN has data rate Downlink of 299.6 MBit/s. Second, EUTRAN has data rate Uplink of 150.8 MBit/s. Thus, EUTRAN has download rates of 299.6 Mbit/s and 150.8 Mbit/s.
"""

fetaqa_s1_prompt_demonstration = """
Strictly follow the format of the below examples, provide rationales before answering the question.

Table: [['Party', 'Party', 'Candidate', 'Votes', '%', '±'], ['-', 'Republican', 'James R. Thompson (incumbent)', '1,816,101', '49.44', '-'], ['-', 'Democratic', 'Adlai Stevenson III', '1,811,027', '49.30', '-'], ['-', 'Libertarian', 'Bea Armstrong', '24,417', '0.66', '-'], ['-', 'Taxpayers', 'John E. Roche', '22,001', '0.60', '-'], ['-', 'N/A', 'write-ins', '161', '0.00', 'n-a'], ['Majority', 'Majority', 'Majority', '5,074', '0.14', '-'], ['Turnout', 'Turnout', 'Turnout', '3,673,707', '-', '-'], ['-', 'Republican hold', 'Republican hold', 'Swing', '-', '-']]
Q: The table is about Results of 1982 Illinois gubernatorial election. Who won the 1982 Illinois gubernatorial election, and how many votes was the margin?
A: First, the major candidates were James R. Thompson and Adlai Stevenson III. James R. Second, Thompson had 1,816,101 votes while Adlai Stevenson III had 1,811,027. Thus, Thompson prevailed in the 1982 Illinois gubernatorial election by a 5,074 vote margin.

Table: [['Finish', 'Start', 'No', 'Name', 'Qual', 'Laps', 'Status'], ['1', '4', '3', 'United States Bobby Rahal', '213.550', '200', '170.722 mph'], ['2', '6', '7', 'United States Kevin Cogan', '211.922', '200', '+1.441 seconds'], ['3', '1', '4', 'United States Rick Mears (W)', '216.828', '200', '+1.881 seconds'], ['4', '8', '5', 'Colombia Roberto Guerrero', '211.576', '200', '+10.558 seconds'], ['5', '9', '30', 'United States Al Unser, Jr.', '211.533', '199', 'Flagged'], ['6', '3', '18', 'United States Michael Andretti', '214.522', '199', 'Flagged'], ['7', '11', '20', 'Brazil Emerson Fittipaldi', '210.237', '199', 'Flagged'], ['8', '12', '21', 'United States Johnny Rutherford (W)', '210.220', '198', 'Flagged'], ['9', '2', '1', 'United States Danny Sullivan (W)', '215.382', '197', 'Flagged']]
Q: The table is about Race box score of 1986 Indianapolis 500. How did Michael and Mario Andretti do?
A: First, Michael and Mario Andretti were both drivers in the 1986 Indianapolis 500 race. Second, Michael had a speed of 214.522 mph while Mario had a speed of 212.300 mph. Thus, Michael Andretti finished with a run of 214.522 mph, faster than Mario.

Table: [['No.', 'Album', 'Artist', 'Released', 'Chart', 'Sales'], ['1', 'First Love', 'Hikaru Utada', '10 March 1999', '1', '7,672,000'], ['2', 'B\'z The Best "Pleasure"', "B'z", '20 May 1998', '1', '5,136,000'], ['3', 'Review', 'Glay', '1 October 1997', '1', '4,876,000'], ['4', 'Distance', 'Hikaru Utada', '28 March 2001', '1', '4,472,000'], ['5', 'B\'z The Best "Treasure"', "B'z", '20 September 1998', '1', '4,439,000'], ['6', 'A Best', 'Ayumi Hamasaki', '28 March 2001', '1', '4,312,000'], ['7', 'Globe', 'Globe', '31 March 1996', '1', '4,136,000'], ['8', 'Deep River', 'Hikaru Utada', '19 June 2002', '1', '3,605,000'], ['9', 'Umi no Yeah!!', 'Southern All Stars', '25 June 1998', '1', '3,592,000']]
Q: The table is about List of best-selling albums by domestic acts of List of best-selling albums in Japan. How many copies did "Pleasure" sell in 1998 alone, and how long was it the best selling album in Japan?
A: First, Pleasure was an album by the Japanese rock duo B'z that sold more than 5,136,000 copies in 1998. Second, it held the top position for 10 months until being surpassed by First Love. Thus, B'z The Best "Pleasure" sold more than 5 million copies in 1998 alone, making it a temporary best-selling album in Japanese music history, until being surpassed by Utada Hikaru's First Love in 1999.
"""

fetaqa_s2_edit_prompt_demonstration = """
Strictly follow the format of the below examples. The given sentence may have factual errors, please correct them based on the given external knowledge.

Sentence: Adlai Stevenson III prevailed in the 1982 Illinois gubernatorial election.
Knowledge: successful candidate of 1982 Illinois gubernatorial election is James R. Thompson. 
Edited sentence: James R. Thompson prevailed in the 1982 Illinois gubernatorial election.

Sentence: The 1986 Indianapolis 500 is an motor race event.
Knowledge: sport of 1986 Indianapolis 500 is auto racing.
Edited sentence: The 1986 Indianapolis 500 is an motor race event.

Sentence: The Japanese album Pleasure was performed by Leslie Feist.
Knowledge: performer of B'z The Best "Pleasure" is B'z.
Edited sentence: The Japanese album Pleasure was performed by B'z.
"""

fetaqa_query_demonstration = """
Based on the table and top few rows, provide an SQL query to help answer the question.

Table: [['Party', 'Party', 'Candidate', 'Votes', '%', '±'], ['-', 'Republican', 'James R. Thompson (incumbent)', '1,816,101', '49.44', '-'], ['-', 'Democratic', 'Adlai Stevenson III', '1,811,027', '49.30', '-'], ['-', 'Libertarian', 'Bea Armstrong', '24,417', '0.66', '-'], ['-', 'Taxpayers', 'John E. Roche', '22,001', '0.60', '-'], ['-', 'N/A', 'write-ins', '161', '0.00', 'n-a'], ['Majority', 'Majority', 'Majority', '5,074', '0.14', '-'], ['Turnout', 'Turnout', 'Turnout', '3,673,707', '-', '-'], ['-', 'Republican hold', 'Republican hold', 'Swing', '-', '-']]
Question: The table is about Results of 1982 Illinois gubernatorial election. Who won the 1982 Illinois gubernatorial election, and how many votes was the margin?
Columns: ['Party', 'Party', 'Candidate', 'Votes', '%', '±']
Query: SELECT Candidate, Votes FROM table;

Table: [['Finish', 'Start', 'No', 'Name', 'Qual', 'Laps', 'Status'], ['1', '4', '3', 'United States Bobby Rahal', '213.550', '200', '170.722 mph'], ['2', '6', '7', 'United States Kevin Cogan', '211.922', '200', '+1.441 seconds'], ['3', '1', '4', 'United States Rick Mears (W)', '216.828', '200', '+1.881 seconds'], ['4', '8', '5', 'Colombia Roberto Guerrero', '211.576', '200', '+10.558 seconds'], ['5', '9', '30', 'United States Al Unser, Jr.', '211.533', '199', 'Flagged'], ['6', '3', '18', 'United States Michael Andretti', '214.522', '199', 'Flagged'], ['7', '11', '20', 'Brazil Emerson Fittipaldi', '210.237', '199', 'Flagged'], ['8', '12', '21', 'United States Johnny Rutherford (W)', '210.220', '198', 'Flagged'], ['9', '2', '1', 'United States Danny Sullivan (W)', '215.382', '197', 'Flagged']]
Question: The table is about Race box score of 1986 Indianapolis 500. How did Michael and Mario Andretti do?
Columns: ['Finish', 'Start', 'No', 'Name', 'Qual', 'Laps', 'Status']
Query: SELECT * FROM table WHERE Name LIKE '%Michael%' OR Name LIKE '%Mario Andretti%';

Table: [['No.', 'Album', 'Artist', 'Released', 'Chart', 'Sales'], ['1', 'First Love', 'Hikaru Utada', '10 March 1999', '1', '7,672,000'], ['2', 'B\'z The Best "Pleasure"', "B'z", '20 May 1998', '1', '5,136,000'], ['3', 'Review', 'Glay', '1 October 1997', '1', '4,876,000'], ['4', 'Distance', 'Hikaru Utada', '28 March 2001', '1', '4,472,000'], ['5', 'B\'z The Best "Treasure"', "B'z", '20 September 1998', '1', '4,439,000'], ['6', 'A Best', 'Ayumi Hamasaki', '28 March 2001', '1', '4,312,000'], ['7', 'Globe', 'Globe', '31 March 1996', '1', '4,136,000'], ['8', 'Deep River', 'Hikaru Utada', '19 June 2002', '1', '3,605,000'], ['9', 'Umi no Yeah!!', 'Southern All Stars', '25 June 1998', '1', '3,592,000']]
Question: The table is about List of best-selling albums by domestic acts of List of best-selling albums in Japan. How many copies did "Pleasure" sell in 1998 alone, and how long was it the best selling album in Japan?
Columns: ['No.', 'Album', 'Artist', 'Released', 'Chart', 'Sales']
Query: SELECT Album, Artist, Released, Sales FROM table LIMIT 3;

Table: [['Aircraft', 'In Service', 'Orders', 'Passengers', 'Notes'], ['Airbus A320-200', '10', '—', '180', 'All to be replaced by Boeing 737-800. Aircraft to be transferred to Virgin Australia Regional Airlines.'], ['Boeing 737-800', '5', '—', '186', 'Aircraft transferred from Virgin Australia'], ['Total', '15', '-', '-', '-']]
Question: The table is about Fleet of Tigerair Australia. How many passengers can that plane hold?
Columns: ['Aircraft', 'In Service', 'Orders', 'Passengers', 'Notes']
Query: SELECT Aircraft, Passengers, Notes FROM table;

Table: [['Year', 'Production', 'Role', 'Venue', 'Notes'], ['2002', 'The Music Man', 'Winthrop Paroo', 'Hollywood Bowl', 'Los Angeles'], ['2004', 'Caroline, or Change', 'Noah Gellman', 'Ahmanson Theatre', 'National tour'], ['2005', 'Dead End', 'Philip Griswald', 'Ahmanson Theatre', 'Regional'], ['2012', 'The Power of Duff', 'Ricky Duff', 'Powerhouse Theatre', 'Regional'], ['2012', 'The Black Suits', 'Chris Thurser', 'Center Theatre Group', 'Regional'], ['2012–2013', 'The Book of Mormon', 'Elder Arnold Cunningham', 'PrivateBank Theatre', 'Chicago'], ['2014–2015', 'The Book of Mormon', 'Elder Arnold Cunningham', "Eugene O'Neill Theatre", 'Broadway'], ['2015', 'Dear Evan Hansen', 'Evan Hansen', 'Arena Stage', 'Washington, D.C.'], ['2016', 'The Secret Garden', 'Dickon', 'David Geffen Hall', '25th anniversary concert']]
Question: The table is about Theatre credits of Ben Platt (actor). When and in what play did Platt appear at the Music Box Theatre?
Columns: ['Year', 'Production', 'Role', 'Venue', 'Notes']
Query: SELECT * FROM table WHERE Venue = 'Music Box Theatre';

Table: [['User equipment Category', 'Max. L1 data rate Downlink (Mbit/s)', 'Max. number of DL MIMO layers', 'Max. L1 data rate Uplink (Mbit/s)', '3GPP Release'], ['NB1', '0.68', '1', '1.0', 'Rel 13'], ['M1', '1.0', '1', '1.0', 'Rel 13'], ['0', '1.0', '1', '1.0', 'Rel 12'], ['1', '10.3', '1', '5.2', 'Rel 8'], ['2', '51.0', '2', '25.5', 'Rel 8'], ['3', '102.0', '2', '51.0', 'Rel 8'], ['4', '150.8', '2', '51.0', 'Rel 8'], ['5', '299.6', '4', '75.4', 'Rel 8'], ['6', '301.5', '2 or 4', '51.0', 'Rel 10']]
Question: The table is about User Equipment (UE) categories of E-UTRA. What are the download rates of EUTRAN?
Columns: ['User equipment Category', 'Max. L1 data rate Downlink (Mbit/s)', 'Max. number of DL MIMO layers', 'Max. L1 data rate Uplink (Mbit/s)', '3GPP Release']
Query: SELECT `Max. L1 data rate Downlink (Mbit/s)` FROM table;
"""

fetaqa_query_s2_demonstration = """
Based on the table and top few rows, provide an SQL query to help answer the question.

Table: [['Party', 'Party', 'Candidate', 'Votes', '%', '±'], ['-', 'Republican', 'James R. Thompson (incumbent)', '1,816,101', '49.44', '-'], ['-', 'Democratic', 'Adlai Stevenson III', '1,811,027', '49.30', '-'], ['-', 'Libertarian', 'Bea Armstrong', '24,417', '0.66', '-'], ['-', 'Taxpayers', 'John E. Roche', '22,001', '0.60', '-'], ['-', 'N/A', 'write-ins', '161', '0.00', 'n-a'], ['Majority', 'Majority', 'Majority', '5,074', '0.14', '-'], ['Turnout', 'Turnout', 'Turnout', '3,673,707', '-', '-'], ['-', 'Republican hold', 'Republican hold', 'Swing', '-', '-']]
Question: The table is about Results of 1982 Illinois gubernatorial election. Who won the 1982 Illinois gubernatorial election, and how many votes was the margin?
Query: SELECT Candidate, Votes FROM table;
Result: [['Candidate', 'Votes'], ['James R. Thompson (incumbent)', '1,816,101'], ['Adlai Stevenson III', '1,811,027'], ['Bea Armstrong', '24,417'], ['John E. Roche', '22,001'], ['write-ins', '161'], ['Majority', '5,074'], ['Turnout', '3,673,707'], ['Republican hold', 'Swing']]
Answer: First, the major candidates were James R. Thompson and Adlai Stevenson III. James R. Second, Thompson had 1,816,101 votes while Adlai Stevenson III had 1,811,027. Thus, Thompson prevailed in the 1982 Illinois gubernatorial election by a 5,074 vote margin.

Table: [['Finish', 'Start', 'No', 'Name', 'Qual', 'Laps', 'Status'], ['1', '4', '3', 'United States Bobby Rahal', '213.550', '200', '170.722 mph'], ['2', '6', '7', 'United States Kevin Cogan', '211.922', '200', '+1.441 seconds'], ['3', '1', '4', 'United States Rick Mears (W)', '216.828', '200', '+1.881 seconds'], ['4', '8', '5', 'Colombia Roberto Guerrero', '211.576', '200', '+10.558 seconds'], ['5', '9', '30', 'United States Al Unser, Jr.', '211.533', '199', 'Flagged'], ['6', '3', '18', 'United States Michael Andretti', '214.522', '199', 'Flagged'], ['7', '11', '20', 'Brazil Emerson Fittipaldi', '210.237', '199', 'Flagged'], ['8', '12', '21', 'United States Johnny Rutherford (W)', '210.220', '198', 'Flagged'], ['9', '2', '1', 'United States Danny Sullivan (W)', '215.382', '197', 'Flagged']]
Question: The table is about Race box score of 1986 Indianapolis 500. How did Michael and Mario Andretti do?
Query: SELECT * FROM table WHERE Name LIKE '%Michael%' OR Name LIKE '%Mario Andretti%';
Result: [['Finish', 'Start', 'No', 'Name', 'Qual', 'Laps', 'Status'], [6, 3, 18, 'United States Michael Andretti', 214.522, 199, 'Flagged'], [32, 30, 2, 'United States Mario Andretti (W)', 212.3, 19, 'Ignition']]
Answer: First, Michael and Mario Andretti were both drivers in the 1986 Indianapolis 500 race. Second, Michael had a speed of 214.522 mph while Mario had a speed of 212.300 mph. Thus, Michael Andretti finished with a run of 214.522 mph, faster than Mario.

Table: [['No.', 'Album', 'Artist', 'Released', 'Chart', 'Sales'], ['1', 'First Love', 'Hikaru Utada', '10 March 1999', '1', '7,672,000'], ['2', 'B\'z The Best "Pleasure"', "B'z", '20 May 1998', '1', '5,136,000'], ['3', 'Review', 'Glay', '1 October 1997', '1', '4,876,000'], ['4', 'Distance', 'Hikaru Utada', '28 March 2001', '1', '4,472,000'], ['5', 'B\'z The Best "Treasure"', "B'z", '20 September 1998', '1', '4,439,000'], ['6', 'A Best', 'Ayumi Hamasaki', '28 March 2001', '1', '4,312,000'], ['7', 'Globe', 'Globe', '31 March 1996', '1', '4,136,000'], ['8', 'Deep River', 'Hikaru Utada', '19 June 2002', '1', '3,605,000'], ['9', 'Umi no Yeah!!', 'Southern All Stars', '25 June 1998', '1', '3,592,000']]
Question: The table is about List of best-selling albums by domestic acts of List of best-selling albums in Japan. How many copies did "Pleasure" sell in 1998 alone, and how long was it the best selling album in Japan?
Query: SELECT Album, Artist, Released, Sales FROM table LIMIT 3;
Result: [['Album', 'Artist', 'Released', 'Sales'], ['First Love', 'Hikaru Utada', '10 March 1999', '7,672,000'], ['B\'z The Best "Pleasure"', "B'z", '20 May 1998', '5,136,000'], ['Review', 'Glay', '1 October 1997', '4,876,000']]
Answer: First, Pleasure was an album by the Japanese rock duo B'z that sold more than 5,136,000 copies in 1998. Second, it held the top position for 10 months until being surpassed by First Love. Thus, B'z The Best "Pleasure" sold more than 5 million copies in 1998 alone, making it a temporary best-selling album in Japanese music history, until being surpassed by Utada Hikaru's First Love in 1999.
"""

fetaqa_query_standard_demonstration = """
Based on the table and top few rows, provide an SQL query to help answer the question.

Table: [['Party', 'Party', 'Candidate', 'Votes', '%', '±'], ['-', 'Republican', 'James R. Thompson (incumbent)', '1,816,101', '49.44', '-'], ['-', 'Democratic', 'Adlai Stevenson III', '1,811,027', '49.30', '-'], ['-', 'Libertarian', 'Bea Armstrong', '24,417', '0.66', '-'], ['-', 'Taxpayers', 'John E. Roche', '22,001', '0.60', '-'], ['-', 'N/A', 'write-ins', '161', '0.00', 'n-a'], ['Majority', 'Majority', 'Majority', '5,074', '0.14', '-'], ['Turnout', 'Turnout', 'Turnout', '3,673,707', '-', '-'], ['-', 'Republican hold', 'Republican hold', 'Swing', '-', '-']]
Question: The table is about Results of 1982 Illinois gubernatorial election. Who won the 1982 Illinois gubernatorial election, and how many votes was the margin?
Query: SELECT Candidate, Votes FROM table;
Result: [['Candidate', 'Votes'], ['James R. Thompson (incumbent)', '1,816,101'], ['Adlai Stevenson III', '1,811,027'], ['Bea Armstrong', '24,417'], ['John E. Roche', '22,001'], ['write-ins', '161'], ['Majority', '5,074'], ['Turnout', '3,673,707'], ['Republican hold', 'Swing']]
Answer: Thompson prevailed in the 1982 Illinois gubernatorial election by a 5,074 vote margin.

Table: [['Finish', 'Start', 'No', 'Name', 'Qual', 'Laps', 'Status'], ['1', '4', '3', 'United States Bobby Rahal', '213.550', '200', '170.722 mph'], ['2', '6', '7', 'United States Kevin Cogan', '211.922', '200', '+1.441 seconds'], ['3', '1', '4', 'United States Rick Mears (W)', '216.828', '200', '+1.881 seconds'], ['4', '8', '5', 'Colombia Roberto Guerrero', '211.576', '200', '+10.558 seconds'], ['5', '9', '30', 'United States Al Unser, Jr.', '211.533', '199', 'Flagged'], ['6', '3', '18', 'United States Michael Andretti', '214.522', '199', 'Flagged'], ['7', '11', '20', 'Brazil Emerson Fittipaldi', '210.237', '199', 'Flagged'], ['8', '12', '21', 'United States Johnny Rutherford (W)', '210.220', '198', 'Flagged'], ['9', '2', '1', 'United States Danny Sullivan (W)', '215.382', '197', 'Flagged']]
Question: The table is about Race box score of 1986 Indianapolis 500. How did Michael and Mario Andretti do?
Query: SELECT * FROM table WHERE Name LIKE '%Michael%' OR Name LIKE '%Mario Andretti%';
Result: [['Finish', 'Start', 'No', 'Name', 'Qual', 'Laps', 'Status'], [6, 3, 18, 'United States Michael Andretti', 214.522, 199, 'Flagged'], [32, 30, 2, 'United States Mario Andretti (W)', 212.3, 19, 'Ignition']]
Answer: Michael Andretti finished with a run of 214.522 mph, faster than Mario.

Table: [['No.', 'Album', 'Artist', 'Released', 'Chart', 'Sales'], ['1', 'First Love', 'Hikaru Utada', '10 March 1999', '1', '7,672,000'], ['2', 'B\'z The Best "Pleasure"', "B'z", '20 May 1998', '1', '5,136,000'], ['3', 'Review', 'Glay', '1 October 1997', '1', '4,876,000'], ['4', 'Distance', 'Hikaru Utada', '28 March 2001', '1', '4,472,000'], ['5', 'B\'z The Best "Treasure"', "B'z", '20 September 1998', '1', '4,439,000'], ['6', 'A Best', 'Ayumi Hamasaki', '28 March 2001', '1', '4,312,000'], ['7', 'Globe', 'Globe', '31 March 1996', '1', '4,136,000'], ['8', 'Deep River', 'Hikaru Utada', '19 June 2002', '1', '3,605,000'], ['9', 'Umi no Yeah!!', 'Southern All Stars', '25 June 1998', '1', '3,592,000']]
Question: The table is about List of best-selling albums by domestic acts of List of best-selling albums in Japan. How many copies did "Pleasure" sell in 1998 alone, and how long was it the best selling album in Japan?
Query: SELECT Album, Artist, Released, Sales FROM table LIMIT 3;
Result: [['Album', 'Artist', 'Released', 'Sales'], ['First Love', 'Hikaru Utada', '10 March 1999', '7,672,000'], ['B\'z The Best "Pleasure"', "B'z", '20 May 1998', '5,136,000'], ['Review', 'Glay', '1 October 1997', '4,876,000']]
Answer: B'z The Best "Pleasure" sold more than 5 million copies in 1998 alone, making it a temporary best-selling album in Japanese music history, until being surpassed by Utada Hikaru's First Love in 1999.

Table: [['Aircraft', 'In Service', 'Orders', 'Passengers', 'Notes'], ['Airbus A320-200', '10', '—', '180', 'All to be replaced by Boeing 737-800. Aircraft to be transferred to Virgin Australia Regional Airlines.'], ['Boeing 737-800', '5', '—', '186', 'Aircraft transferred from Virgin Australia'], ['Total', '15', '-', '-', '-']]
Question: The table is about Fleet of Tigerair Australia. How many passengers can that plane hold?
Query: SELECT Aircraft, Passengers, Notes FROM table;
Result: [['Aircraft', 'Passengers', 'Notes'], ['Airbus A320-200', '180', 'All to be replaced by Boeing 737-800. Aircraft to be transferred to Virgin Australia Regional Airlines.'], ['Boeing 737-800', '186', 'Aircraft transferred from Virgin Australia'], ['Total', '-', '-']]
Answer: The Tigerair Australia fleet consists of the following aircraft and Virgin Australia announced that the entire A320 fleet will be replaced with Boeing 737-800 aircraft.

Table: [['Year', 'Production', 'Role', 'Venue', 'Notes'], ['2002', 'The Music Man', 'Winthrop Paroo', 'Hollywood Bowl', 'Los Angeles'], ['2004', 'Caroline, or Change', 'Noah Gellman', 'Ahmanson Theatre', 'National tour'], ['2005', 'Dead End', 'Philip Griswald', 'Ahmanson Theatre', 'Regional'], ['2012', 'The Power of Duff', 'Ricky Duff', 'Powerhouse Theatre', 'Regional'], ['2012', 'The Black Suits', 'Chris Thurser', 'Center Theatre Group', 'Regional'], ['2012–2013', 'The Book of Mormon', 'Elder Arnold Cunningham', 'PrivateBank Theatre', 'Chicago'], ['2014–2015', 'The Book of Mormon', 'Elder Arnold Cunningham', "Eugene O'Neill Theatre", 'Broadway'], ['2015', 'Dear Evan Hansen', 'Evan Hansen', 'Arena Stage', 'Washington, D.C.'], ['2016', 'The Secret Garden', 'Dickon', 'David Geffen Hall', '25th anniversary concert']]
Question: The table is about Theatre credits of Ben Platt (actor). When and in what play did Platt appear at the Music Box Theatre?
Query: SELECT * FROM table WHERE Venue = 'Music Box Theatre';
Result: [['Year', 'Production', 'Role', 'Venue', 'Notes'], ['2016–2017', 'Dear Evan Hansen', 'Evan Hansen', 'Music Box Theatre', 'Broadway']]
Answer: In 2016 and 2017, Platt played in Dear Evan Hansen on Broadway at the Music Box Theatre.

Table: [['User equipment Category', 'Max. L1 data rate Downlink (Mbit/s)', 'Max. number of DL MIMO layers', 'Max. L1 data rate Uplink (Mbit/s)', '3GPP Release'], ['NB1', '0.68', '1', '1.0', 'Rel 13'], ['M1', '1.0', '1', '1.0', 'Rel 13'], ['0', '1.0', '1', '1.0', 'Rel 12'], ['1', '10.3', '1', '5.2', 'Rel 8'], ['2', '51.0', '2', '25.5', 'Rel 8'], ['3', '102.0', '2', '51.0', 'Rel 8'], ['4', '150.8', '2', '51.0', 'Rel 8'], ['5', '299.6', '4', '75.4', 'Rel 8'], ['6', '301.5', '2 or 4', '51.0', 'Rel 10']]
Question: The table is about User Equipment (UE) categories of E-UTRA. What are the download rates of EUTRAN?
Query: SELECT `Max. L1 data rate Downlink (Mbit/s)` FROM table;
Result: [['Max. L1 data rate Downlink (Mbit/s)'], ['0.68'], ['1.0'], ['1.0'], ['10.3'], ['51.0'], ['102.0'], ['150.8'], ['299.6'], ['301.5'], ['301.5'], ['2,998.6'], ['452.2'], ['452.2'], ['603.0'], ['603.0'], ['391.7'], ['391.7'], ['750'], ['979'], ['25,065'], ['1,174'], ['1,566']]
Answer: EUTRAN has download rates of 299.6 Mbit/s and 150.8 Mbit/s.
"""

fetaqa_sql_wiki_demonstration = """
Based on the table, context, and SQL query results, answer the question.

Table: [['Party', 'Party', 'Candidate', 'Votes', '%', '±'], ['-', 'Republican', 'James R. Thompson (incumbent)', '1,816,101', '49.44', '-'], ['-', 'Democratic', 'Adlai Stevenson III', '1,811,027', '49.30', '-'], ['-', 'Libertarian', 'Bea Armstrong', '24,417', '0.66', '-'], ['-', 'Taxpayers', 'John E. Roche', '22,001', '0.60', '-'], ['-', 'N/A', 'write-ins', '161', '0.00', 'n-a'], ['Majority', 'Majority', 'Majority', '5,074', '0.14', '-'], ['Turnout', 'Turnout', 'Turnout', '3,673,707', '-', '-'], ['-', 'Republican hold', 'Republican hold', 'Swing', '-', '-']]
Context: Incumbent Governor James R. Thompson, a Republican, narrowly won reelection to a third term, defeating Democrat Adlai Stevenson III by merely 5,074 votes.
Question: The table is about Results of 1982 Illinois gubernatorial election. Who won the 1982 Illinois gubernatorial election, and how many votes was the margin?
Query: SELECT Candidate, Votes FROM table;
Result: [['Candidate', 'Votes'], ['James R. Thompson (incumbent)', '1,816,101'], ['Adlai Stevenson III', '1,811,027'], ['Bea Armstrong', '24,417'], ['John E. Roche', '22,001'], ['write-ins', '161'], ['Majority', '5,074'], ['Turnout', '3,673,707'], ['Republican hold', 'Swing']]
Answer: Thompson prevailed in the 1982 Illinois gubernatorial election by a 5,074 vote margin.

Table: [['Finish', 'Start', 'No', 'Name', 'Qual', 'Laps', 'Status'], ['1', '4', '3', 'United States Bobby Rahal', '213.550', '200', '170.722 mph'], ['2', '6', '7', 'United States Kevin Cogan', '211.922', '200', '+1.441 seconds'], ['3', '1', '4', 'United States Rick Mears (W)', '216.828', '200', '+1.881 seconds'], ['4', '8', '5', 'Colombia Roberto Guerrero', '211.576', '200', '+10.558 seconds'], ['5', '9', '30', 'United States Al Unser, Jr.', '211.533', '199', 'Flagged'], ['6', '3', '18', 'United States Michael Andretti', '214.522', '199', 'Flagged'], ['7', '11', '20', 'Brazil Emerson Fittipaldi', '210.237', '199', 'Flagged'], ['8', '12', '21', 'United States Johnny Rutherford (W)', '210.220', '198', 'Flagged'], ['9', '2', '1', 'United States Danny Sullivan (W)', '215.382', '197', 'Flagged']]
Context: Michael and Mario Andretti led the speed chart for the day, both over 210 mph. 
Question: The table is about Race box score of 1986 Indianapolis 500. How did Michael and Mario Andretti do?
Query: SELECT * FROM table WHERE Name LIKE '%Michael%' OR Name LIKE '%Mario Andretti%';
Result: [['Finish', 'Start', 'No', 'Name', 'Qual', 'Laps', 'Status'], [6, 3, 18, 'United States Michael Andretti', 214.522, 199, 'Flagged'], [32, 30, 2, 'United States Mario Andretti (W)', 212.3, 19, 'Ignition']]
Answer: Michael Andretti finished with a run of 214.522 mph, faster than Mario.

Table: [['No.', 'Album', 'Artist', 'Released', 'Chart', 'Sales'], ['1', 'First Love', 'Hikaru Utada', '10 March 1999', '1', '7,672,000'], ['2', 'B\'z The Best "Pleasure"', "B'z", '20 May 1998', '1', '5,136,000'], ['3', 'Review', 'Glay', '1 October 1997', '1', '4,876,000'], ['4', 'Distance', 'Hikaru Utada', '28 March 2001', '1', '4,472,000'], ['5', 'B\'z The Best "Treasure"', "B'z", '20 September 1998', '1', '4,439,000'], ['6', 'A Best', 'Ayumi Hamasaki', '28 March 2001', '1', '4,312,000'], ['7', 'Globe', 'Globe', '31 March 1996', '1', '4,136,000'], ['8', 'Deep River', 'Hikaru Utada', '19 June 2002', '1', '3,605,000'], ['9', 'Umi no Yeah!!', 'Southern All Stars', '25 June 1998', '1', '3,592,000']]
Context: sold more than one million copies, a feat mostly achieved by domestic acts.
Question: The table is about List of best-selling albums by domestic acts of List of best-selling albums in Japan. How many copies did "Pleasure" sell in 1998 alone, and how long was it the best selling album in Japan?
Query: SELECT Album, Artist, Released, Sales FROM table LIMIT 3;
Result: [['Album', 'Artist', 'Released', 'Sales'], ['First Love', 'Hikaru Utada', '10 March 1999', '7,672,000'], ['B\'z The Best "Pleasure"', "B'z", '20 May 1998', '5,136,000'], ['Review', 'Glay', '1 October 1997', '4,876,000']]
Answer: B'z The Best "Pleasure" sold more than 5 million copies in 1998 alone, making it a temporary best-selling album in Japanese music history, until being surpassed by Utada Hikaru's First Love in 1999.

Table: [['Aircraft', 'In Service', 'Orders', 'Passengers', 'Notes'], ['Airbus A320-200', '10', '—', '180', 'All to be replaced by Boeing 737-800. Aircraft to be transferred to Virgin Australia Regional Airlines.'], ['Boeing 737-800', '5', '—', '186', 'Aircraft transferred from Virgin Australia'], ['Total', '15', '-', '-', '-']]
Context: Tigerair Australia flies their 737-800 in a 180 seat capacity with 42 'Extra Leg Room' seats, 30 'Up Front' seats and 108 regular Economy seats.
Question: The table is about Fleet of Tigerair Australia. How many passengers can that plane hold?
Query: SELECT Aircraft, Passengers, Notes FROM table;
Result: [['Aircraft', 'Passengers', 'Notes'], ['Airbus A320-200', '180', 'All to be replaced by Boeing 737-800. Aircraft to be transferred to Virgin Australia Regional Airlines.'], ['Boeing 737-800', '186', 'Aircraft transferred from Virgin Australia'], ['Total', '-', '-']]
Answer: The Tigerair Australia fleet consists of the following aircraft and Virgin Australia announced that the entire A320 fleet will be replaced with Boeing 737-800 aircraft.

Table: [['Year', 'Production', 'Role', 'Venue', 'Notes'], ['2002', 'The Music Man', 'Winthrop Paroo', 'Hollywood Bowl', 'Los Angeles'], ['2004', 'Caroline, or Change', 'Noah Gellman', 'Ahmanson Theatre', 'National tour'], ['2005', 'Dead End', 'Philip Griswald', 'Ahmanson Theatre', 'Regional'], ['2012', 'The Power of Duff', 'Ricky Duff', 'Powerhouse Theatre', 'Regional'], ['2012', 'The Black Suits', 'Chris Thurser', 'Center Theatre Group', 'Regional'], ['2012–2013', 'The Book of Mormon', 'Elder Arnold Cunningham', 'PrivateBank Theatre', 'Chicago'], ['2014–2015', 'The Book of Mormon', 'Elder Arnold Cunningham', "Eugene O'Neill Theatre", 'Broadway'], ['2015', 'Dear Evan Hansen', 'Evan Hansen', 'Arena Stage', 'Washington, D.C.'], ['2016', 'The Secret Garden', 'Dickon', 'David Geffen Hall', '25th anniversary concert']]
Context: In December 2016, Platt originated the title role in Dear Evan Hansen on Broadway at the Music Box Theatre.
Question: The table is about Theatre credits of Ben Platt (actor). When and in what play did Platt appear at the Music Box Theatre?
Query: SELECT * FROM table WHERE Venue = 'Music Box Theatre';
Result: [['Year', 'Production', 'Role', 'Venue', 'Notes'], ['2016–2017', 'Dear Evan Hansen', 'Evan Hansen', 'Music Box Theatre', 'Broadway']]
Answer: In 2016 and 2017, Platt played in Dear Evan Hansen on Broadway at the Music Box Theatre.

Table: [['User equipment Category', 'Max. L1 data rate Downlink (Mbit/s)', 'Max. number of DL MIMO layers', 'Max. L1 data rate Uplink (Mbit/s)', '3GPP Release'], ['NB1', '0.68', '1', '1.0', 'Rel 13'], ['M1', '1.0', '1', '1.0', 'Rel 13'], ['0', '1.0', '1', '1.0', 'Rel 12'], ['1', '10.3', '1', '5.2', 'Rel 8'], ['2', '51.0', '2', '25.5', 'Rel 8'], ['3', '102.0', '2', '51.0', 'Rel 8'], ['4', '150.8', '2', '51.0', 'Rel 8'], ['5', '299.6', '4', '75.4', 'Rel 8'], ['6', '301.5', '2 or 4', '51.0', 'Rel 10']]
Context: EUTRAN has the following features: Peak download rates of 299.6 Mbit/s for 4×4 antennas, and 150.8 Mbit/s for 2×2 antennas with 20 MHz of spectrum.
Question: The table is about User Equipment (UE) categories of E-UTRA. What are the download rates of EUTRAN?
Query: SELECT `Max. L1 data rate Downlink (Mbit/s)` FROM table;
Result: [['Max. L1 data rate Downlink (Mbit/s)'], ['0.68'], ['1.0'], ['1.0'], ['10.3'], ['51.0'], ['102.0'], ['150.8'], ['299.6'], ['301.5'], ['301.5'], ['2,998.6'], ['452.2'], ['452.2'], ['603.0'], ['603.0'], ['391.7'], ['391.7'], ['750'], ['979'], ['25,065'], ['1,174'], ['1,566']]
Answer: EUTRAN has download rates of 299.6 Mbit/s and 150.8 Mbit/s.
"""

################################
########### ReAct ##############
################################

hotpotqa_6shot_react_prompt = '''
Question    What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into? 
Thought 1   I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area. 
Action 1    Search[Colorado orogeny] 
Observation 1   The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. 
Thought 2   It does not mention the eastern sector. So I need to look up eastern sector. 
Action 2    Lookup[eastern sector] 
Observation 2 (Result 1 / 1)    The eastern sector extends into the High Plains and is called the Central Plains orogeny. 
Thought 3   The eastern sector of Colorado orogeny extends into the High Plains. So I need to search High Plains and find its elevation range.
Action 3    Search[High Plains] Observation 3 High Plains refers to one of two distinct land regions
Thought 4   I need to instead search High Plains (United States). 
Action 4    Search[High Plains (United States)]
Observation 4   The High Plains are a subregion of the Great Plains. From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3] 
Thought 5   High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft. 
Action 5    Finish[1,800 to 7,000 ft] 

Question    Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who? 
Thought 1   The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after. 
Action 1    Search[Milhouse]
Observation 1   Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2   The paragraph does not tell who Milhouse is named after, maybe I can look up "named after". 
Action 2    Lookup[named after] 
Observation 2   (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3   Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon. 
Action 3    Finish[Richard Nixon] 

Question    Which documentary is about Finnish rock groups, Adam Clayton Powell or The Saimaa Gesture? 
Thought 1   I need to search Adam Clayton Powell and The Saimaa Gesture, and find which documentary is about Finnish rock groups. 
Action 1    Search[Adam Clayton Powell] 
Observation 1   Could not find [Adam Clayton Powell]. Similar: [’Adam Clayton Powell III’, ’Seventh Avenue (Manhattan)’, ’Adam Clayton Powell Jr. State Office Building’, ’Isabel Washington Powell’, ’Adam Powell’, ’Adam Clayton Powell (film)’, ’Giancarlo Esposito’]. 
Thought 2   To find the documentary, I can search Adam Clayton Powell (film). 
Action 2    Search[Adam Clayton Powell (film)]
Observation 2   Adam Clayton Powell is a 1989 American documentary film directed by Richard Kilberg. The film is about the rise and fall of influential African-American politician Adam Clayton Powell Jr.[3][4] It was later aired as part of the PBS series The American Experience.
Thought 3   Adam Clayton Powell (film) is a documentary about an African-American politician, not Finnish rock groups. So the documentary about Finnish rock groups must instead be The Saimaa Gesture.
Action 3    Finish[The Saimaa Gesture]

Question    What profession does Nicholas Ray and Elia Kazan have in common?
Thought 1   I need to search Nicholas Ray and Elia Kazan, find their professions, then find the profession they have in common. 
Action 1    Search[Nicholas Ray] 
Observation 1   Nicholas Ray (born Raymond Nicholas Kienzle Jr., August 7, 1911 - June 16, 1979) was an American film director, screenwriter, and actor best known for the 1955 film Rebel Without a Cause.
Thought 2   Professions of Nicholas Ray are director, screenwriter, and actor. I need to search Elia Kazan next and find his professions.
Action 2    Search[Elia Kazan]
Observation 2   Elia Kazan was an American film and theatre director, producer, screenwriter and actor. 
Thought 3   Professions of Elia Kazan are director, producer, screenwriter, and actor. So profession Nicholas Ray and Elia Kazan have in common is director, screenwriter, and actor. 
Action 3    Finish[director, screenwriter, actor] 

Question    Which magazine was started first Arthur’s Magazine or First for Women? 
Thought 1   I need to search Arthur’s Magazine and First for Women, and find which was started first. 
Action 1    Search[Arthur’s Magazine] 
Observation 1   Arthur’s Magazine (1844-1846) was an American literary periodical published in Philadelphia in the 19th century. 
Thought 2   Arthur’s Magazine was started in 1844. I need to search First for Women next. 
Action 2    Search[First for Women] 
Observation 2   First for Women is a woman’s magazine published by Bauer Media Group in the USA.[1] The magazine was started in 1989. 
Thought 3   First for Women was started in 1989. 1844 (Arthur’s Magazine) < 1989 (First for Women), so Arthur’s Magazine was started first. 
Action 3    Finish[Arthur’s Magazine] 

Question    Were Pavel Urysohn and Leonid Levin known for the same type of work? 
Thought 1   I need to search Pavel Urysohn and Leonid Levin, find their types of work, then find if they are the same. 
Action 1    Search[Pavel Urysohn]
Observation 1   Pavel Samuilovich Urysohn (February 3, 1898 - August 17, 1924) was a Soviet mathematician who is best known for his contributions in dimension theory. 
Thought 2   Pavel Urysohn is a mathematician. I need to search Leonid Levin next and find its type of work. 
Action 2    Search[Leonid Levin] 
Observation 2   Leonid Anatolievich Levin is a Soviet-American mathematician and computer scientist. 
Thought 3   Leonid Levin is a mathematician and computer scientist. So Pavel Urysohn and Leonid Levin have the same type of work. 
Action 3    Finish[yes]

'''

fever_3shot_react_prompt = '''
Determine if there is Observation that SUPPORTS or REFUTES a Claim, or if there is NOT ENOUGH INFORMATION.

Claim   Nikolaj Coster-Waldau worked with the Fox Broadcasting Company.
Thought 1   I need to search Nikolaj Coster-Waldau and find if he has worked with the Fox Broadcasting Company.
Action 1    Search[Nikolaj Coster-Waldau] 
Observation 1   Nikolaj William Coster-Waldau (born 27 July 1970) is a Danish actor and producer. He graduated from the Danish National School of Performing Arts in Copenhagen in 1993,[1] and had his breakthrough role in Denmark with the film Nightwatch (1994). He played Jaime Lannister in the HBO fantasy drama series Game of Thrones, for which he received two Primetime Emmy Award nominations for Outstanding Supporting Actor in a Drama Series.. Coster-Waldau has appeared in numerous films in his native Denmark and Scandinavia, including Headhunters (2011) and A Thousand Times Good Night (2013). In the U.S, his debut film role was in the war film Black Hawk Down (2001), playing Medal of Honor recipient Gary Gordon.[2] He then played a detective in the short-lived Fox television series New Amsterdam (2008), and appeared in the 2009 Fox television film Virtuality, originally intended as a pilot.
Thought 2   Because he "appeared in the 2009 Fox television film Virtuality", he should have worked with the Fox Broadcasting Company.
Action 2    Finish[SUPPORTS]

Claim   Stranger Things is set in Bloomington, Indiana.
Thought 1   I should search for Stranger Things, and see if it is set in Bloomington, Indiana.
Action 1    Search[Stranger Things] 
Observation 1   Stranger Things is an American science fiction horror drama television series created by the Duffer Brothers. Set in the 1980s, primarily in the fictional town of Hawkins, Indiana, the series centers on a number of mysteries and supernatural events occurring around the town and their impact on an ensemble of child and adult characters.
Thought 2   The observation says that it is set in a "fictional town of Hawkins, Indiana", so it is not set in Bloomington.
Action 2    Finish[REFUTES]

Claim   Beautiful reached number two on the Billboard Hot 100 in 2003.
Thought 1   I need to search the song Beautiful and find if it reached number two on the Billboard Hot 100 in 2003.
Action 1    Search[Beautiful]
Observation 1   Could not find [Beautiful]. Similar: [’Beautiful’, ’Beautiful, Beautiful’, ’A Beautiful Mind (film)’, ’Beautiful (Christina Aguilera song)’, ’Life Is Beautiful’].
Thought 2   From suggestions, I should search "Beautiful (Christina Aguilera song)" to find the song.
Action 2    Search[Beautiful (Christina Aguilera song)]
Observation 2   "Beautiful" is a song recorded by American singer Christina Aguilera for her fourth studio album, Stripped (2002).
Thought 3   It does not mention Billboard, so I need to look up "Billboard Hot 100" to find if it reached number two on it in 2003.
Action 3    Lookup[Billboard Hot 100]
Observation 3   (Result 1 / 3) The song peaked at number two on the Billboard Hot 100 in the United States, where it was certified Gold for 500,000 units shipped.
Thought 4   It only says the song peaked at number two on the Billboard Hot 100, but not if it was in 2003. I am not sure if this claim is true or not.
Action 4    Finish[NOT ENOUGH INFO]

'''


################################
########### MedMCQA ###########
################################

medmcqa_s1_prompt_demonstration = """
Strictly follow the format of the below examples, provide two rationales before answering the question. The answer must be A, B, C, or D.
Q: Hyper viscosity is seen in A. Cryoglobulinemia B. Multiple myeloma C. MGUS D. Lymphoma
A: First, The term cryoglobulinemia refers to the presence in the serum of proteins that precipitate at temperatures below 37 degrees C and redissolve on rewarming. Second, The elective treatment for hyperviscosity syndrome, whether associated with monoclonal, mixed, or polyclonalcryoglobulinemia, is plasma exchange. The answer is A.

Q: Splenomegaly may be a feature of: A. Megaloblastic anemia B. Sickle cell anemia C. Thalassemia D. G6PD deficiency
A: First, Splenomegaly refers strictly to spleen enlargement, and is distinct from hyperspineism , which connotes overactive function by a spleen of any size. Second, the tip of the spleen may be palpable in a newborn baby up to 3 months of age Early sickle cell anemia may present with splenomegaly. The answer is B.

Q: Hamartomatous lung tissue is? A. Hypoplasia of lung B. Congenital cyst C. Lobar sequestration D. Congenital cystic adenomatoid malformation
A: First, Congenital cystic adenomatoid malformation (CCAM): Hamartomatous Q or dysplastic lung tissue. Second, usually confined to one lobe. The answer is D.

Q: Bicipital aponeurosis lies over which structure in cubital fossa:- A. Median cubital vein B. Radial nerve C. Brachial aery D. Anterior interosseous aery
A: First, icipital aponeurosis lies superficial to the brachial aery and median nerve. -lies deep to superficial veins. Second, -provides protection for the deeper structures during venepuncture at cubital fossa. -routinely released to decompress the median nerve The answer is C.

Q: Most dangerous paicles causing pneumoconiosis are of size A. 1-5 micron B. <1 micron C. 5-15 micron D. 10-20 micron
A: First, In pneumoconiosis, the most dangerous paicles range from 1-5 micron in diameter, because they may reach the terminal small airway and settle in there lining notes. Second, The solubility and cytotoxicity of paicles ,modify the nature of pulmonary response. The answer is A.

Q: In a patient of liver disease, which maneuvers, may lead to the development of hyperammonemia? A. Protein restriction B. The use of neomycin C. The use of loop diuretics D. A branched-chain amino acid-enriched protein mixture
A: First, The use of loop diuretics promotes kaliuresis. Second, and therefore may lead to hyperammonemia. The answer is C.

"""

medmcqa_s2_edit_prompt_demonstration = """
Strictly follow the format of the below examples. The given sentence may have factual errors, please correct them based on the given external knowledge.
Sentence: the Alpher-Bethe-Gamow paper was invented by Ralph Alpher.
Knowledge: discoverer or inventor of Alpher-Bethe-Famow paper is Ralph Alpher. 
Edited sentence: the Alpher-Bethe-Gamow paper was invented by Ralph Alpher.

Sentence: Ralph Alpher was advised by Hans Bethe.
Knowledge: doctoral advisor of Ralph Alpher is George Gamow.
Edited sentence: Ralph Alpher was advised by George Gamow.

"""

################################
########### Phy ###########
################################

# phy_s1_prompt_demonstration = """
# Strictly follow the format of the below examples, provide two rationales before answering the question. The answer must be A, B, C, or D.
# Q: The best type of laser with which to do spectroscopy over a range of visible wavelengths is A. a dye laser B. a helium-neon laser C. an excimer laser D. a ruby laser
# A: First, a dye laser is known for its tunability across a wide range of wavelengths, including the visible spectrum, making it suitable for various spectroscopy applications. Second, helium-neon, excimer, and ruby lasers have fixed wavelengths and are not tunable across a range of visible wavelengths, limiting their versatility in spectroscopy. The answer is A

# Q: In the diamond structure of elemental carbon, the nearest neighbors of each C atom lie at the corners of a A. square B. hexagon C. cube D. tetrahedron
# A: First, the diamond cubic structure is a crystal lattice arrangement formed by repeating a unit cell with atoms at its corners and the center of each face. Second, each carbon atom in the diamond structure forms four single bonds with four other carbon atoms arranged tetrahedrally around it. The answer is D.

# Q: The sign of the charge carriers in a doped semiconductor can be deduced by measuring which of the following properties? A. Specific heat B. Thermal conductivity C. Electrical resistivity D. Hall coefficient
# A: First, the Hall coefficient indicates the nature of charge carriers in a material. Second, other listed properties don’t provide direct information about the charge carriers' sign. The answer is D.

# """

phy_s1_prompt_demonstration = """
Strictly follow the format of the below examples, provide two rationales before answering the question. The answer must be A, B, C, or D.
Q: The best type of laser with which to do spectroscopy over a range of visible wavelengths is A. a dye laser B. a helium-neon laser C. an excimer laser D. a ruby laser
A: First, a dye laser is known for its tunability across a wide range of wavelengths, including the visible spectrum, making it suitable for various spectroscopy applications. Second, helium-neon, excimer, and ruby lasers have fixed wavelengths and are not tunable across a range of visible wavelengths, limiting their versatility in spectroscopy. The answer is A

Q: In the diamond structure of elemental carbon, the nearest neighbors of each C atom lie at the corners of a A. square B. hexagon C. cube D. tetrahedron
A: First, the diamond cubic structure is a crystal lattice arrangement formed by repeating a unit cell with atoms at its corners and the center of each face. Second, each carbon atom in the diamond structure forms four single bonds with four other carbon atoms arranged tetrahedrally around it. The answer is D.

Q: The sign of the charge carriers in a doped semiconductor can be deduced by measuring which of the following properties? A. Specific heat B. Thermal conductivity C. Electrical resistivity D. Hall coefficient
A: First, the Hall coefficient indicates the nature of charge carriers in a material. Second, other listed properties don’t provide direct information about the charge carriers' sign. The answer is D.

Q: Which of the following conditions will ensure that angular momentum is conserved? I. Conservation of linear momentum II. Zero net external force III. Zero net external torque A. I and II only B. I and III only C. II and III only D. III only
A: First, angular momentum is conserved when there is no net external torque acting on the system. Second, conservation of linear momentum and the absence of a net external force are not sufficient to ensure the conservation of angular momentum. The answer is D.

Q: A microwave oven is connected to an outlet, 120 V, and draws a current of 2 amps. At what rate is energy being used by the microwave oven? A. 10 W B. 30 W C. 60 W D. 240 W
A: First, the rate at which energy is used, or power, can be calculated using the formula: Power (P)=Voltage (V)×Current (I). Second, substituting the given values, Voltage (V)=120V and Current (I)=2A, will give the power consumed by the microwave oven. The answer is D

Q: For which of the following thermodynamic processes is the increase in the internal energy of an ideal gas equal to the heat added to the gas? A. Constant temperature B. Constant volume C. Constant pressure D. Adiabatic
A: First, in a constant volume process, there is no work done by or on the gas, and thus, the increase in internal energy of the gas is equal to the heat added to the gas. Second, in the other processes, part of the heat added goes into performing work, so the increase in internal energy is not equal to the heat added. The answer is B.

"""

phy_s2_edit_prompt_demonstration = """
Strictly follow the format of the below examples. The given sentence may have factual errors, please correct them based on the given external knowledge.
Sentence: the Alpher-Bethe-Gamow paper was invented by Ralph Alpher.
Knowledge: discoverer or inventor of Alpher-Bethe-Famow paper is Ralph Alpher. 
Edited sentence: the Alpher-Bethe-Gamow paper was invented by Ralph Alpher.

Sentence: Ralph Alpher was advised by Hans Bethe.
Knowledge: doctoral advisor of Ralph Alpher is George Gamow.
Edited sentence: Ralph Alpher was advised by George Gamow.

"""

################################
########### Bio ###########
################################

# bio_s1_prompt_demonstration = """
# Strictly follow the format of the below examples, provide two rationales before answering the question. The answer must be A, B, C, or D.
# Q: During the period when life is believed to have begun, the atmosphere on primitive Earth contained abundant amounts of all the following gases EXCEPT A. oxygen B. hydrogen C. ammonia D. methane
# A: First, primitive Earth had a reducing atmosphere, rich in hydrogen, ammonia, and methane. Second, oxygen wasn’t abundant as it mostly existed in compounds. The answer is A. 

# Q: Invertebrate immune systems possess which of the following? A. Cytotoxic T-lymphocytes B. Phagocytes C. B-cells D. Helper T-cells
# A: First, invertebrates possess innate immunity with components like phagocytes. Second, adaptive immunity elements like T-cells and B-cells are absent in them. The answer is B.

# Q: A gas phase is generally absent from which of the following biogeochemical cycles? A. Water B. Carbon C. Sulfur D. Phosphorus
# A: First, the phosphorus cycle primarily involves solid and liquid phases. Second, the other cycles include a gas phase. The answer is D.

# """

bio_s1_prompt_demonstration = """
Strictly follow the format of the below examples, provide two rationales before answering the question. The answer must be A, B, C, or D.
Q: During the period when life is believed to have begun, the atmosphere on primitive Earth contained abundant amounts of all the following gases EXCEPT A. oxygen B. hydrogen C. ammonia D. methane
A: First, primitive Earth had a reducing atmosphere, rich in hydrogen, ammonia, and methane. Second, oxygen wasn’t abundant as it mostly existed in compounds. The answer is A. 

Q: Invertebrate immune systems possess which of the following? A. Cytotoxic T-lymphocytes B. Phagocytes C. B-cells D. Helper T-cells
A: First, invertebrates possess innate immunity with components like phagocytes. Second, adaptive immunity elements like T-cells and B-cells are absent in them. The answer is B.

Q: A gas phase is generally absent from which of the following biogeochemical cycles? A. Water B. Carbon C. Sulfur D. Phosphorus
A: First, the phosphorus cycle primarily involves solid and liquid phases. Second, the other cycles include a gas phase. The answer is D.

Q: Which of the following is not known to be involved in the control of cell division? A. Cyclins B. Protein kinases C. Checkpoints D. Fibroblast cells
A: First, cyclins, protein kinases, and checkpoints are all crucial components in the regulation of the cell cycle and cell division. Second, fibroblast cells are a type of cell involved in the synthesis of the extracellular matrix and collagen but are not components that regulate cell division. The answer is D.

Q: A mutation in a bacterial enzyme changed a previously polar amino acid into a nonpolar amino acid. This amino acid was located at a site distant from the enzyme’s active site. How might this mutation alter the enzyme’s substrate specificity? A. By changing the enzyme’s pH optimum B. By changing the enzyme’s location in the cell C. By changing the shape of the protein D. An amino acid change away from the active site cannot alter the enzyme’s substrate specificity.
A: First, a mutation away from the active site can still alter the enzyme's shape, impacting substrate specificity. Second, the other options don’t directly relate to changes in substrate specificity due to a mutation. The answer is C.

Q: Which of the following contain DNA sequences required for the segregation of chromosomes in mitosis and meiosis? A. Telomeres B. Centromeres C. Nucleosomes D. Spliceosomes
A: First, centromeres are essential for chromosome segregation during cell division. Second, the other options are not involved in the segregation of chromosomes. The answer is B.

"""

bio_s2_edit_prompt_demonstration = """
Strictly follow the format of the below examples. The given sentence may have factual errors, please correct them based on the given external knowledge.
Sentence: the Alpher-Bethe-Gamow paper was invented by Ralph Alpher.
Knowledge: discoverer or inventor of Alpher-Bethe-Famow paper is Ralph Alpher. 
Edited sentence: the Alpher-Bethe-Gamow paper was invented by Ralph Alpher.

Sentence: Ralph Alpher was advised by Hans Bethe.
Knowledge: doctoral advisor of Ralph Alpher is George Gamow.
Edited sentence: Ralph Alpher was advised by George Gamow.

"""