#!/bin/sh
PRE_SNAKE="___dojogen___"
POS_SNAKE="___dojogen___"

PRE_PASCAL="___class_dojogen___"
POS_PASCAL="___class_dojogen___"

PRE_DOWN="___down_dojogen___"
POS_DOWN="___down_dojogen___"

PRE_CAMEL="___camel_dojogen___"
POS_CAMEL="___camel_dojogen___"


for FILE in `find . -name "*$PRE_SNAKE*"`; do NEW=`echo $FILE | sed -e "s/$PRE_SNAKE/$POS_SNAKE/"`; mv "$FILE" "$NEW"; done
find . -type f -exec sed -i "s/$PRE_SNAKE/$POS_SNAKE/g" {} ";"

for FILE in `find . -name "*$PRE_PASCAL*"`; do NEW=`echo $FILE | sed -e "s/$PRE_PASCAL/$POS_PASCAL/"`; mv "$FILE" "$NEW"; done
find . -type f -exec sed -i "s/$PRE_PASCAL/$POS_PASCAL/g" {} ";"

for FILE in `find . -name "*$PRE_DOWN*"`; do NEW=`echo $FILE | sed -e "s/$PRE_DOWN/$POS_DOWN/"`; mv "$FILE" "$NEW"; done
find . -type f -exec sed -i "s/$PRE_DOWN/$POS_DOWN/g" {} ";"

for FILE in `find . -name "*$PRE_CAMEL*"`; do NEW=`echo $FILE | sed -e "s/$PRE_CAMEL/$POS_CAMEL/"`; mv "$FILE" "$NEW"; done
find . -type f -exec sed -i "s/$PRE_CAMEL/$POS_CAMEL/g" {} ";"
