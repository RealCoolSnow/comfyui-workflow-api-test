import json
from urllib import request, parse

# 读取文件全部内容
workflow = '/Users/coolsnow/code/ComfyUI/workflows/api/sdxl_lightning_workflow_full.json'
with open(workflow, 'r') as f:
    prompt_text = f.read()


def queue_prompt(prompt):
    p = {"prompt": prompt}
    print(f"queue prompt: {p}")
    data = json.dumps(p).encode('utf-8')
    req = request.Request("http://127.0.0.1:8188/prompt", data=data)
    resp = request.urlopen(req)
    print("response:", resp.read().decode('utf-8'))

prompt = json.loads(prompt_text)
# set the text prompt for our positive CLIPTextEncode
prompt["6"]["inputs"]["text"] = "masterpiece best quality man"

# set the seed for our KSampler node
# prompt["3"]["inputs"]["seed"] = 5


queue_prompt(prompt)
