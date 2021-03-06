

archive_analytics.values.service='wb';archive_analytics.values.server_name='wwwb-app16.us.archive.org';archive_analytics.values.server_ms=436;

__wbhack.init('https://web.archive.org/web');




Trip Routing







 Trip Routing 

Your employer, the California Car Club (CCC), has decided to provide a 
trip routing service to its members. Your job is to write a program 
which reads a list of departure point-destination point pairs and 
calculates the shortest routes between them. For each trip, your 
program will print a report which itemises the names of each city 
passed through, with route names and leg distances.

Input

Input to your program will be in two parts.


The first part is a map in
the form of a list of highway segments. Each segment is designated 
by a line containing four fields which are separated by commas. The 
first two fields are 1-20 characters each, and are the names of the 
cities which are at each end of the highway segment. The third field 
is the 1-10 character name of the route. The fourth field is the number 
of miles between the two endpoints, expressed as a positive integer. 
The highway segment list will be terminated by an empty line.


The second part of the input is a list of departure point-destination
point pairs, one per line. The departure point is given first, followed 
by a comma and the destination point. Each of the cities is 
guaranteed to have appeared in the first part of the input data, and 
there will be a path that connects them. The list is terminated by the 
end of file.

Output

The output should be a series of reports, one for each departure
point-destination point pair in the input. Each report should be in
exactly the same form as those in the example below.
There should be two blank lines
before each report (including the first one).

Sample input

San Luis Obispo,Bakersfield,CA-58,117
Bakersfield,Mojave,CA-58,65
Mojave,Barstow,CA-58,70
Barstow,Baker,I-15,62
Baker,Las Vegas,I-15,92
San Luis Obispo,Santa Barbara,US-101,106
San Luis Obispo,Santa Barbara,CA-1,113
Santa Barbara,Los Angeles,US-101,95
Bakersfield,Wheeler Ridge,CA-99,24
Wheeler Ridge,Los Angeles,I-5,88
Mojave,Los Angeles,CA-14,94
Los Angeles,San Bernardino,I-10,65
San Bernardino,Barstow,I-15,73
Los Angeles,San Diego,I-5,121
San Bernardino,San Diego,I-15,103

Santa Barbara,Las Vegas
San Diego,Los Angeles
San Luis Obispo,Los Angeles

Sample output

From                 To                   Route      Miles
-------------------- -------------------- ---------- -----
Santa Barbara        Los Angeles          US-101        95
Los Angeles          San Bernardino       I-10          65
San Bernardino       Barstow              I-15          73
Barstow              Baker                I-15          62
Baker                Las Vegas            I-15          92
                                                     -----
                                          Total        387


From                 To                   Route      Miles
-------------------- -------------------- ---------- -----
San Diego            Los Angeles          I-5          121
                                                     -----
                                          Total        121


From                 To                   Route      Miles
-------------------- -------------------- ---------- -----
San Luis Obispo      Santa Barbara        US-101       106
Santa Barbara        Los Angeles          US-101        95 
                                                     -----
                                          Total        201



Note: There will be no extraneous blanks in the input. There will be no
more than 100 cities in the map and no more than 200 highway
segments. The total distance in each best route is guaranteed to fit 
within a 16-bit integer.



