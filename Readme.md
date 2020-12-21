
# Installation
Create a new folder "whatver_name"
cd "whatver_name"
git clone the repo or copy the repo in "whatver_name"

> Make sure you have python3 installed

`brew install python3`

`yum install python3`


### Activate python3 venv

`source "whatever_name"/ck/venv/bin/activate`

`pip3 install -r requirements.txt`


### To Run the App
This would run the app in below desired cases

`python3 app.py FIFO`

`python3 app.py Matched`

### Logs are located in the log folder
Where every order is logged and you can check current order and mean of total orders/ order wait time/courier wait time
> Sample log and csv file are attached in the logs folder


### Optional for visualization
After you run both cases FIFO/Matched. There are analysis_file.csv generated in logs.
These files are read by plottting and a realtime mean courier wait and mean order wait time are plotted for every order.

`python3 plotting FIFO`

`python3 plotting Matched`

### Testing

For running all unit test

`python -m unittest discover -p 'test*'`

For running single test 

`python -m unittest <filename(without.py)>`

`python -m unittest test_reception`

### Whole Picture:

Run below python commands in new terminal

terminal 1:`python3 app.py FIFO`

terminal 2:`python3 app.py Matched`

> Make sure analysis file have generated

terminal3: `python3 plotting FIFO`

terminal4: `python3 plotting Matched`


## Rerunning:
make suree you truncate the analysis file.
`truncate -s0 analysis_fifo.csv`
`truncate -s0 analysis_matched.csv`
        OR
`truncate -s0 *.csv`

(Plots will be generated for visualization)
