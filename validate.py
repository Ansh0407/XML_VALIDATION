from lxml import etree

def validate_xml(xml_filename, xsd_filename):
    try:
        
        xml_doc = etree.parse(xml_filename)
        xsd_doc = etree.parse(xsd_filename)

        schema = etree.XMLSchema(xsd_doc)
        is_valid = schema.validate(xml_doc)

        if is_valid:
            print(f"{xml_filename} is valid according to {xsd_filename}.")
        else:
            print(f"{xml_filename} is NOT valid according to {xsd_filename}.")
            print("Validation errors:")
            for error in schema.error_log:
                print(error)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    xml_file = "2347212_lab4.xml"  
    xsd_file = "2347212_lab4.xsd" 
    validate_xml(xml_file, xsd_file)
