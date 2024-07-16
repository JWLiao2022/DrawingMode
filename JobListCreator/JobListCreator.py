import xml.etree.cElementTree as ET

def createANewJobList(resolution, folderPath, inputCIFfileName, outputXMLFileFullPath):

    ArrayOfPositionListItem = ET.Element("ArrayOfPositionListItem")
    PositionListItem = ET.SubElement(ArrayOfPositionListItem, "PositionListItem")

    ET.SubElement(PositionListItem, "DoseCorrection").text = "1.0"
    ET.SubElement(PositionListItem, "FocusCorrectionUM").text = "0"
    ET.SubElement(PositionListItem, "GroupName").text = ""
    ET.SubElement(PositionListItem, "ExposureMode").text = "0"
    ET.SubElement(PositionListItem, "LocalAlignment").text = "None"
    ET.SubElement(PositionListItem, "AlignmentPointdXMM").text = "0"
    ET.SubElement(PositionListItem, "AlignmentPointdYMM").text = "0"
    ET.SubElement(PositionListItem, "RealTimeCorrectFocus").text = "false"
    ET.SubElement(PositionListItem, "RoundVectorCoordinatesToGrid").text = "true"
    ET.SubElement(PositionListItem, "BeamName").text = resolution
    ET.SubElement(PositionListItem, "CascadeLocalAlignmentToFollowingJobs").text = "false"
    ET.SubElement(PositionListItem, "FocusLockGroup").text = "2"
    ET.SubElement(PositionListItem, "VectorFileOpeningProgressPercent").text = "0"
    ET.SubElement(PositionListItem, "CancelCIFParsing").text = "false"
    ET.SubElement(PositionListItem, "MultipassOrder").text = "2"
    ET.SubElement(PositionListItem, "StitchingDoseCorrectionPercent").text = "0"
    ET.SubElement(PositionListItem, "LightsourceName").text = "405nm"
    ET.SubElement(PositionListItem, "Quality").text = "2"
    ET.SubElement(PositionListItem, "InvertExposure").text = "false"
    ET.SubElement(PositionListItem, "EnableStitchingOverlap").text = "true"
    ET.SubElement(PositionListItem, "X").text = "0"
    ET.SubElement(PositionListItem, "Y").text = "0"
    ET.SubElement(PositionListItem, "LayerIndex").text = "0"
    ET.SubElement(PositionListItem, "RealTimeFocusCorrectionSelection").text = "Fastest"
    ET.SubElement(PositionListItem, "Name").text = inputCIFfileName
    ET.SubElement(PositionListItem, "FolderName").text = folderPath

    tree = ET.ElementTree(ArrayOfPositionListItem)
    ET.indent(tree, '   ')
    tree.write(outputXMLFileFullPath, encoding="utf-8", xml_declaration=True)