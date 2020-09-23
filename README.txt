In this assignment Dependies are the files that are used in each files, and it generate some output files which are there in Generates
Output File section.

NOTE : All the code run in Python3 environment. Before running code we have to install all the plugins in python3.

RUN : To run all code automatically run : ./assign1.sh , this will run the entire code.
========================================================================================================================================
SNo   Program                                Plugins               Dependencies                         Generates Output File
========================================================================================================================================
1.    neighbor-districts-modified.sh         json                  neighbor-districts.json              neighbor-districts-modified.json 
                                             pandas                mapAllDictToOne.csv
                                             
2.    case-generator.sh                      json                  FINAL_EDIT_DISTANCE.csv              cases-week.csv
                                             pandas                raw_data1.csv                        cases-month.csv
                                             collections           raw_data2.csv                        cases-overall.csv
                                             datetime              districts.csv                        districtTOstate.csv
                                                                   neighbor-districts-modified.json     neighbor-districts-modified.csv

3.    edge-generator.sh                      json                  neighbor-districts-modified.json     edge-graph.csv                                                           
                                             pandas
                                             
4.    neighbor-generator.sh                  collections           edge-graph.csv                       neighbor-week.csv
                                             pandas                cases-week.csv                       neighbor-month.csv
                                             statistics            cases-month.csv                      neighbor-overall.csv
                                                                   cases-overall.csv                 
                                                                   
5.    state-generator.sh                     collections           districtTOstate.csv                  state-week.csv
                                             pandas                neighbor-districts-modified.csv      state-month.csv
                                             statistics            edge-graph.csv                       state-overall.csv
                                                                   cases-week.csv
                                                                   cases-month.csv
                                                                   cases-overall.csv
                                                                   
6.    zscore-generator.sh                    pandas                cases-week.csv                       zscore-week.csv                                 
                                                                   cases-month.csv                      zscore-month.csv
                                                                   cases-overall.csv                    zscore-overall.csv
                                                                   neighbor-week.csv
                                                                   neighbor-month.csv
                                                                   neighbor-overall.csv
                                                                   state-week.csv
                                                                   state-month.csv
                                                                   state-overall.csv
                                                                   
7.    method-spot-generator.sh               pandas                cases-week.csv                       method-spot-week.csv
                                                                   cases-month.csv                      method-spot-month.csv
                                                                   cases-overall.csv                    method-spot-overall.csv
                                                                   neighbor-week.csv
                                                                   neighbor-month.csv
                                                                   neighbor-overall.csv
                                                                   state-week.csv
                                                                   state-month.csv
                                                                   state-overall.csv    
                                                                   
8.    top-generator.sh                       pandas                zscore-week.csv                      top-week.csv
                                             collections           zscore-month.csv                     top-month.csv
                                                                   zscore-overall.csv                   top-overall.csv
                                                                   method-spot-week.csv
                                                                   method-spot-month.csv
                                                                   method-spot-overall.csv
======================================================================================================================================== 
NOTE : For individual run of the code first run the codes that generates the dependencies used. Then run the particular code.
                                                                 