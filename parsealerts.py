from xml.etree import ElementTree

std_output_bool = True
file_output_bool = True
csv_file_output_bool = True
csv_header_bool = True

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

def outputcsvendofline():
        csvoutputfile.write('\n')

print('\n')
print("Start - Processing Management Module")

altree = ElementTree.parse('ManagementModule.xml')

alerts = altree.findall('./DataGroups/DataGroup/AlertBase/Name')

for al in altree.iter('AlertBase'):
    output('Alert Name: ', al.find('Name'))
    output('Is Active: ', al.attrib['IsActive'])
    output('Alert Description: ', al.find('Description'))
    for alf in al.iter('PeriodInSeconds'):
        output('PeriodInSeconds: ', alf.find('PeriodInSeconds'))
        output('Metric Level Notification: ', al.find('MetricLevelNotification'))
        output('Alert Trigger Mode: ', al.find('AlertTriggerMode'))
        output('Caution Action Delay: ', al.find('CautionActionDelay'))
        output('Danger Action Delay: ', al.find('DangerActionDelay'))
    for alcal in al.iter('CautionActionList') :
        for alcid in alcal.iter('ActionID') :
            output('Caution Action MM Name: ', alcid.find('ManagementModuleName'))
            output('Caution Action Name: ', alcid.find('ConstructName'))
    for aldal in al.iter('DangerActionList') :
        for aldid in aldal.iter('ActionID') :
            output('Danger Action MM Name: ', aldid.find('ManagementModuleName'))
            output('Danger Action Name: ', aldid.find('ConstructName'))
    for almgid in al.iter('MetricGroupingID'):
        output('Management Module Name: ', almgid.find('ManagementModuleName'))
        output('Metric Grouping: ', almgid.find('ConstructName'))
    output('Alert Combine Operator: ', al.find('AlertCombineOperator'))
    output('Alert Compare Operator: ', al.find('AlertCompareOperator'))
    output('Caution Target Value: ', al.find('CautionTargetValue'))
    output('Danger Target Value: ', al.find('DangerTargetValue'))
    output('Caution Min Num Per Period: ', al.find('CautionMinNumPerPeriod'))
    output('Caution Alert Period: ', al.find('CautionAlertPeriod'))
    output('Danger Min Num Per Period: ', al.find('DangerMinNumPerPeriod'))
    output('Danger Alert Period: ', al.find('DangerAlertPeriod'))
    outputcsvendofline

print("End - Processing Management Module")

outputfile.close()
csvoutputfile.close()