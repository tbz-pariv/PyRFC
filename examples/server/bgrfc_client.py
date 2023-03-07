import sys
from pyrfc import Connection

c = Connection(dest=sys.argv[1])

unit = c.initialize_unit()

name = "BGRFC_TEST_OUTIN"
counter = "00001"

print("unit:", unit, name, counter)
c.fill_and_submit_unit(
    unit,
    [
        (
            "STFC_WRITE_TO_TCPIC",
            {"TCPICDAT": [f"{name:20}{counter:20}{unit['id']:32}"]},
        )
    ],
    queue_names=["RFCSDK_QUEUE_IN"],
    attributes={"lock": 1},
)
c.close()
