import json
df_edges=""""""
def generate_amcharts_json(df):
    json_network={}
    for obj in df['result']['data']["@value"]:
        key_from=obj["@value"]['objects']["@value"][1]["@value"]['outV']
        key_to=obj["@value"]['objects']["@value"][1]["@value"]['inV']
        if key_from not in json_network:
            json_network[key_from]={'name':key_from,'linkWith':[],"value":5}
        if key_to not in json_network:
            json_network[key_to]={'name':key_to,'linkWith':[],"value":5}
        json_network[key_from]['linkWith'].append(key_to)
    return {"data":list(json_network.values())}


def lambda_handler(event, context):
    return generate_amcharts_json(json.loads(df_edges))
