std_output_bool = True
file_output_bool = True
csv_file_output_bool = True
outputfile = open("ManagementModule.out","w")
csvoutputfile = open("ManagementModule.csv","w")

def output(mmtitle, mmelement):
    if (mmelement is not None):        
        if isinstance(mmelement, str):
            mmelementformatted = mmelement
        else:
            mmelementformatted = mmelement.text
    else:
        mmelementformatted = ""
    if std_output_bool:
        print(format(mmtitle, '>30') + format(str(mmelementformatted),'<30'))
    if file_output_bool:
        outputfile.write(format(mmtitle, '>30') + format(str(mmelementformatted),'<30') + '\n')
    if csv_file_output_bool:
        csvoutputfile.write(str(mmelementformatted) + ',')