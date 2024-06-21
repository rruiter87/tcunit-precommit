import re
import xml.etree.ElementTree as ET
from collections import namedtuple
from typing import List

Mismatch = namedtuple("Mismatch", ["method_name", "test_name"])


def find_mismatched_test_names(xml_content: str) -> List[Mismatch]:
    root = ET.fromstring(xml_content)
    function_block_name = root.find(".//POU").get("Name")
    methods = root.findall(".//Method")

    mismatches = []
    pattern = re.compile(r"TEST(?:_ORDERED)?\('([^']+)'\)")

    for method in methods:
        method_name = method.get("Name")
        implementation = method.find(".//ST").text

        if implementation:
            matches = pattern.findall(implementation)
            for test_name in matches:
                if test_name != method_name:
                    print(
                        f"Method '{function_block_name}.{method_name}' does NOT match the TEST name '{test_name}'."
                    )
                    mismatches.append(Mismatch(method_name, test_name))

    return mismatches


def fix_test_names(xml_content: str, mismatches: List[Mismatch]) -> str:
    for mismatch in mismatches:
        old_test_call = f"TEST('{mismatch.test_name}');"
        new_test_call = f"TEST('{mismatch.method_name}');"
        xml_content = xml_content.replace(old_test_call, new_test_call)

    return xml_content
