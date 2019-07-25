#! /usr/bin/env bash

###########################################################################
# Retrieves USD to INR conversion rates for a list of dates specified
# in dd/mm/yyyy format.

# Input: The dates are provided through an input file, one date per line.
# Output: The output is printed on the screen and is self-explanatory.
###########################################################################

#set -x         # prints out whatever it is executing
set -o nounset # does not allow unset variables to be used

ARGS=1        # Number of arguments expected.
E_BADARGS=65  # Exit value if incorrect number of args passed.

test $# -ne $ARGS && echo -e "\033[1mUsage: $0 [input date file]\033[0m" && exit $E_BADARGS

# Get the location of the script no matter where you ran it from
SCRIPT_PATH=$(cd `dirname ${0}`; pwd)

DATE_FILE=$1
website="https://www.exchange-rates.org"

echo
echo "Getting rates from $website..."
echo

for date in `cat ${DATE_FILE}`
do
    day=`echo $date | cut -d/ -f1`
    month=`echo $date | cut -d/ -f2`
    year=`echo $date | cut -d/ -f3`

    url="$website/Rate/USD/INR/$month-$day-$year"

    echo -n "$date --> "
    curl $url 2>/dev/null | grep -oE "1 US Dollar = [0-9]{2}\.[0-9]{4} Indian Rupees on [0-9]{1,2}/[0-9]{1,2}/[0-9]{4}"
done
