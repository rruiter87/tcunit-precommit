import xml.etree.ElementTree as ET


def check_unit_test_method_names(xml_content):
    root = ET.fromstring(xml_content)
    methods = root.findall(".//Method")

    for method in methods:
        method_name = method.get("Name")
        implementation = method.find(".//ST").text

        if implementation:
            test_start = implementation.find("TEST('")
            if test_start != -1:
                test_end = implementation.find("');", test_start)
                test_name = implementation[test_start + 6 : test_end]

                if test_name == method_name:
                    print(f"Method '{method_name}' matches the TEST name.")
                else:
                    print(
                        f"Method '{method_name}' does NOT match the TEST name '{test_name}'."
                    )
                    return False

    return True
