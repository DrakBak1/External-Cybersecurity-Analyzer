import json
from pathlib import Path

CONFIG_PATH = (Path(__file__).resolve().parent/ "config"/ "ports"/ "sensitive_services.json")

def Load_Rules():
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return json.load(file)

def Analyze_Ports(OPEN_PORTS):
    rules = Load_Rules()
    analyzed_results = []
    for port in OPEN_PORTS:
        if port["service"].lower() in rules:
            analyzed_port_object = {
                "port": port["port"],
                "service": port["service"],
                "status": "review",
                **rules[port["service"]]
            }
            analyzed_results.append(analyzed_port_object)
    return(analyzed_results)