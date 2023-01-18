from xml.etree import ElementTree

std_output_bool = True
file_output_bool = True
csv_file_output_bool = True
csv_header_bool = True

outputfile = open("ManagementModule.out","w")
csvoutputfile = open("ManagementModule.csv","w")

def formatoutput(mmelement):
    formattedoutput = ''
    if (mmelement is not None):
        if isinstance(mmelement, str):
            formattedoutput = str(mmelement)
        else:
            formattedoutput = str(mmelement.text)
    formattedoutput = formattedoutput.replace(',', '-')
    formattedoutput = formattedoutput.replace('\n', ' ')
    return formattedoutput 

def processoutput(file_output_line, csv_output_line, csv_header_line, label, metricvalue):
    file_output_line = file_output_line + '\n' + label + ': ' + metricvalue
    csv_output_line = csv_output_line + metricvalue + ','
    if csv_header_bool:
        csv_header_line = csv_header_line + label + ','
    return file_output_line, csv_output_line, csv_header_line

def outputcsvendofline():
        csvoutputfile.write('\n')

print('\n')
print("Start - Processing Management Module")

altree = ElementTree.parse('ManagementModule.xml')

alerts = altree.findall('./DataGroups/DataGroup/AlertBase/Name')

for al in altree.iter('AlertBase'):

    file_output_line = ''
    csv_header_line = ''
    csv_output_line = ''    

    file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Alert Name', formatoutput(al.find('Name')))
    file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'IsActive', formatoutput(al.attrib['IsActive']))
    file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Alert Description', formatoutput(al.find('Description')))
    file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Frequency', formatoutput(al.find('Frequency')))
    for alfreq in al.iter('Frequency'):
        file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Period In Seconds', formatoutput(alfreq.find('PeriodInSeconds')))
    file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Metric Level Notification', formatoutput(al.find('MetricLevelNotification')))
    file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Alert Trigger Mode', formatoutput(al.find('AlertTriggerMode')))
    file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Caution Action Delay', formatoutput(al.find('CautionActionDelay')))
    file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Danger Action Delay', formatoutput(al.find('DangerActionDelay')))
    for alcal in al.iter('CautionActionList') :
        file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Caution Action List', formatoutput(alcal.find('CautionActionList')))       
        for alcid in alcal.iter('ActionID') :
            file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Caution Action MM Name', formatoutput(alcid.find('ManagementModuleName')))
            file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Caution Action Name', formatoutput(alcid.find('ConstructName')))
    for aldal in al.iter('DangerActionList') :
        file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Danger Action List', formatoutput(aldal.find('CautionActionList')))       
        for aldid in aldal.iter('ActionID') :
            file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Danger Action MM Name', formatoutput(aldid.find('ManagementModuleName')))
            file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Danger Action Name', formatoutput(aldid.find('ConstructName')))
    for almgid in al.iter('MetricGroupingID'):
            file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Management Module Name', formatoutput(almgid.find('ManagementModuleName')))    
            file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Construct Name', formatoutput(almgid.find('ConstructName')))    
    file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Alert Combine Operator', formatoutput(al.find('AlertCombineOperator')))
    file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Alert Compare Operator', formatoutput(al.find('AlertCompareOperator')))
    file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Caution Target Value', formatoutput(al.find('CautionTargetValue')))
    file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Danger Target Value', formatoutput(al.find('DangerTargetValue')))
    file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Caution Min Num Per Period', formatoutput(al.find('CautionMinNumPerPeriod')))
    file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Caution Alert Period', formatoutput(al.find('CautionAlertPeriod')))
    file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Danger Min Num Per Period', formatoutput(al.find('DangerMinNumPerPeriod')))
    file_output_line, csv_output_line, csv_header_line = processoutput(file_output_line, csv_output_line, csv_header_line, 'Danger Alert Period', formatoutput(al.find('DangerAlertPeriod')))

    print(file_output_line + '\n')
    outputfile.write(file_output_line + '\n')
    if csv_header_bool:
        csvoutputfile.write(csv_header_line + '\n')
    csvoutputfile.write(csv_output_line + '\n')

    csv_header_bool = False

print("End - Processing Management Module")

outputfile.close()
csvoutputfile.close()