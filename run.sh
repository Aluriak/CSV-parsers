# delete any previous data
rm data.csv

# run once for create the csv file
python3 csv_test.py

# run again for compare the two parser
python3 csv_test.py

# show the csv content
echo "Here is the data.csv file content: "
cat data.csv
