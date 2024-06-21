import re
import xml.etree.ElementTree as ET
from collections import namedtuple
from typing import List

Mismatch = namedtuple("Mismatch", ["method_name", "test_name"])
pattern = re.compile(r"TEST(?:_ORDERED)?\('([^']+)'\)")


def find_mismatched_test_names(xml_content: str) -> List[Mismatch]:
    root = ET.fromstring(xml_content)
    function_block_name = root.find(".//POU").get("Name")
    methods = root.findall(".//Method")

    mismatches = []

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
    def replacer(match):
        test_name = match.group(1)
        for mismatch in mismatches:
            if test_name == mismatch.test_name:
                return match.group(0).replace(mismatch.test_name, mismatch.method_name)
        return match.group(0)

    xml_content = pattern.sub(replacer, xml_content)

    return xml_content
