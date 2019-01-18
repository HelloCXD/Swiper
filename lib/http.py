import json


# 统一返回json的格式
from django.http import HttpResponse


def render_json(data, code=0):
    result = {
        "data": data,
        "code": code,
    }

    json_str = json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True)

    return HttpResponse(json_str)



